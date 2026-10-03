import sqlite3
import time

import pytest
from fastapi.testclient import TestClient

from ultron.app.control import ControlStore
from ultron.app.server import create_app


@pytest.fixture
def client(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTRONOMOUS_STATE_DIR", str(tmp_path))
    monkeypatch.setenv("ULTRON_CONFIG_DIR", str(tmp_path / "config"))
    return TestClient(create_app())


def pause(client, value=True):
    csrf = client.get("/dashboard").cookies["ultron_csrf"]
    return client.post("/api/autronomous/control", headers={"X-CSRF-Token": csrf}, json={"paused": value})


def test_pause_blocks_execution_without_mutating_engine_and_survives_restart(client):
    assert pause(client).status_code == 200
    engine = client.app.state.triage
    before = engine.current_pointer_version()
    csrf = client.cookies["ultron_csrf"]
    for kind in ("SUBMIT_REQUEST", "RUN_BENCHMARK"):
        response = client.post("/api/action", headers={"X-CSRF-Token": csrf}, json={
            "type": kind, "payload": {"request_text": "must never run"},
            "csrf_token": csrf, "active_pointer_version": before,
        })
        assert response.status_code == 423
    assert engine.current_pointer_version() == before
    assert engine.last_manifest is None
    restarted = TestClient(create_app())
    assert restarted.get("/api/autronomous").json()["control"]["paused"] is True
    assert pause(restarted, False).status_code == 200
    csrf = restarted.cookies["ultron_csrf"]
    assert restarted.post("/api/action", headers={"X-CSRF-Token": csrf}, json={
        "type": "SUBMIT_REQUEST", "payload": {"request_text": "test resumed demo"}, "csrf_token": csrf,
    }).status_code == 200
    events = restarted.get("/api/autronomous").json()["control"]["events"]
    assert [e["paused"] for e in events] == [False, True]
    assert all(e["actor"] == "local-operator" for e in events)


def test_pause_requires_session_scope_and_csrf_and_rejects_coercion(client):
    assert client.post("/api/autronomous/control", json={"paused": True}).status_code == 401
    csrf = client.get("/dashboard").cookies["ultron_csrf"]
    assert client.post("/api/autronomous/control", json={"paused": True}).status_code == 403
    assert client.post("/api/autronomous/control", headers={"X-CSRF-Token": "wrong"}, json={"paused": True}).status_code == 403
    assert client.post("/api/autronomous/control", headers={"X-CSRF-Token": csrf}, json={"paused": "false"}).status_code == 422
    session = client.cookies["ultron_session"]
    store = client.app.state.session_store
    principal = store.resolve(session, time.time())
    from ultron.auth.principal import Principal
    limited = Principal(subject=principal.subject, scopes=frozenset())
    # Resolve a restricted principal while retaining the session's legitimate CSRF.
    original = store.resolve
    store.resolve = lambda *args: limited
    try:
        assert client.post("/api/autronomous/control", headers={"X-CSRF-Token": csrf}, json={"paused": True}).status_code == 403
    finally:
        store.resolve = original
    assert client.get("/api/autronomous").json()["control"] == {"paused": False, "events": []}


def test_status_is_honest_and_manual_has_security_headers(client):
    status = client.get("/api/autronomous")
    assert status.json()["execution_mode"] == "demo"
    assert status.json()["business"]["verified_revenue_gbp"] is None
    assert all(w["status"] == "planned" for w in status.json()["workers"])
    assert status.json()["capabilities"]["web_engine_restart_persistence"] is False
    manual = client.get("/manual")
    assert manual.status_code == 200
    assert "default-src 'self'" in manual.headers["Content-Security-Policy"]
    assert "AUTRONOMOUS" in manual.text


def test_live_default_pauses_and_corrupt_state_never_silently_resumes(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTRONOMOUS_STATE_DIR", str(tmp_path))
    monkeypatch.setenv("ULTRON_ADAPTER", "pinned-hermes")
    client = TestClient(create_app())
    assert client.get("/api/autronomous").json()["control"]["paused"] is True
    (tmp_path / "control.sqlite3").write_bytes(b"corrupt")
    with pytest.raises(sqlite3.DatabaseError):
        ControlStore()
