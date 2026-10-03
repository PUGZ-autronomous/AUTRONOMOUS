"""Exercise real server processes, demo requests and persistent pause recovery.

Run from the installed source checkout: .venv/bin/python scripts/smoke_demo.py
No paid providers, external task tools, or existing operator state are used.
"""

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time

import httpx


ROOT = Path(__file__).resolve().parents[1]


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def stop(process):
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def boot(env, log):
    # Pick a loopback port for this test. Readiness checks also verify the child
    # remains alive; an occupied port cannot masquerade as our server.
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "ultron.app.server:create_app", "--factory", "--host", "127.0.0.1", "--port", str(port)],
        cwd=ROOT, env=env, stdout=log, stderr=log,
    )
    client = httpx.Client(base_url=f"http://127.0.0.1:{port}", trust_env=False, timeout=5)
    try:
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            check(process.poll() is None, "Server exited before becoming ready")
            try:
                if client.get("/api/autronomous").status_code == 200:
                    check(process.poll() is None, "Server exited during readiness")
                    return process, client
            except httpx.RequestError:
                pass
            time.sleep(0.1)
        raise RuntimeError("Server did not become ready")
    except BaseException:
        client.close()
        stop(process)
        raise


def session(client):
    response = client.get("/dashboard")
    check(response.status_code == 200, "Control room unavailable")
    return response.cookies["ultron_csrf"]


def set_pause(client, csrf, paused):
    response = client.post("/api/autronomous/control", headers={"X-CSRF-Token": csrf}, json={"paused": paused})
    check(response.status_code == 200, "Pause change failed")


def command(client, csrf, kind="SUBMIT_REQUEST"):
    status = client.get("/api/toolbelt").json()
    return client.post("/api/action", headers={"X-CSRF-Token": csrf}, json={
        "type": kind, "csrf_token": csrf,
        "active_pointer_version": status["active_pointer_version"],
        "payload": {"request_text": "Prepare a digital product evaluation checklist"},
    })


def main():
    report = {"mode": "demo", "checks": []}
    with tempfile.TemporaryDirectory(prefix="autronomous-smoke-") as directory:
        env = dict(os.environ)
        env.update({
            "ULTRON_ADAPTER": "fake", "ULTRON_UI_GENERATOR": "fake",
            "ULTRON_MODULE_SYNTH": "fake", "ULTRON_VLM": "fake", "ULTRON_LIVE_MODEL": "0",
            "AUTRONOMOUS_STATE_DIR": directory + "/state",
            "ULTRON_CONFIG_DIR": directory + "/config",
            "ULTRON_DOTENV_PATH": directory + "/unused.env", "ULTRON_SECURE_COOKIES": "0",
        })
        with (Path(directory) / "server.log").open("w") as log:
            process, client = boot(env, log)
            try:
                status = client.get("/api/autronomous").json()
                check(not any(status["components"].values()), "A live component was selected")
                check(status["business"]["verified_revenue_gbp"] is None, "Unconnected revenue must stay unknown")
                check(client.get("/manual").status_code == 200, "Manual unavailable")
                check(client.get("/static/dashboard.js").status_code == 200, "Dashboard asset unavailable")
                report["checks"].append("demo mode, unknown revenue, manual and dashboard assets")
                csrf = session(client)
                check(client.post("/api/autronomous/control", json={"paused": True}).status_code == 403, "Missing CSRF accepted")
                result = command(client, csrf)
                check(result.status_code == 200 and result.json().get("envelope"), "Demo command did not return result cards")
                check(len(client.get("/api/runs").json()["runs"]) > 0, "Run was not recorded")
                report["checks"].append("demo command produces cards and run provenance")
                set_pause(client, csrf, True)
                for kind in ("SUBMIT_REQUEST", "RUN_BENCHMARK"):
                    check(command(client, csrf, kind).status_code == 423, "Paused execution accepted")
                report["checks"].append("pause blocks commands and benchmarks; CSRF is enforced")
            finally:
                client.close()
                stop(process)
            process, client = boot(env, log)
            try:
                check(client.get("/api/autronomous").json()["control"]["paused"], "Pause lost during real process restart")
                check(client.get("/api/runs").json()["runs"] == [], "Documented in-memory run reset changed")
                report["checks"].append("pause survives process restart; web run history currently resets")
                csrf = session(client)
                check(command(client, csrf).status_code == 423, "Restart bypassed pause")
                set_pause(client, csrf, False)
                check(command(client, csrf).status_code == 200, "Resume failed")
                events = client.get("/api/autronomous").json()["control"]["events"]
                check([item["paused"] for item in events] == [False, True], "Control history did not persist")
                report["checks"].append("resume restores demo execution and preserves control audit history")
            finally:
                client.close()
                stop(process)
    report["passed"] = True
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
