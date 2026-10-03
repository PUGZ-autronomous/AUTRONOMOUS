"""Persistent admission control. This is not cancellation of in-flight work."""

import os
import sqlite3
import time
from pathlib import Path

from pydantic import BaseModel, ConfigDict, StrictBool


class ControlWrite(BaseModel):
    model_config = ConfigDict(extra="forbid")
    paused: StrictBool


class ControlStore:
    def __init__(self, *, initially_paused: bool = False):
        directory = Path(os.getenv("AUTRONOMOUS_STATE_DIR", "~/.local/state/autronomous")).expanduser()
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.path = directory / "control.sqlite3"
        with self._connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY CHECK(id=1), paused INTEGER NOT NULL CHECK(paused IN (0,1)))")
            db.execute("CREATE TABLE IF NOT EXISTS control_events (id INTEGER PRIMARY KEY, created_at REAL NOT NULL, actor TEXT NOT NULL, paused INTEGER NOT NULL)")
            db.execute("INSERT OR IGNORE INTO control VALUES (1, ?)", (int(initially_paused),))
        self.path.chmod(0o600)

    def _connect(self):
        return sqlite3.connect(self.path, timeout=10)

    def snapshot(self):
        with self._connect() as db:
            row = db.execute("SELECT paused FROM control WHERE id=1").fetchone()
            if row is None or row[0] not in (0, 1):
                raise RuntimeError("Invalid admission control state")
            events = db.execute("SELECT created_at, actor, paused FROM control_events ORDER BY id DESC LIMIT 10").fetchall()
        return {"paused": bool(row[0]), "events": [{"created_at": t, "actor": a, "paused": bool(p)} for t, a, p in events]}

    def set_paused(self, paused: bool, *, actor: str):
        with self._connect() as db:
            db.execute("UPDATE control SET paused=? WHERE id=1", (int(paused),))
            db.execute("INSERT INTO control_events(created_at, actor, paused) VALUES (?, ?, ?)", (time.time(), actor, int(paused)))
        return self.snapshot()


WORKER_PLAN = [
    {"name": name, "purpose": purpose, "status": "planned"}
    for name, purpose in [
        ("SCOUT", "Research opportunities and gather evidence"),
        ("FORGE", "Build products, tools and drafts"),
        ("MERCURY", "Prepare and operate sales channels"),
        ("GROWTH", "Test marketing and measure results"),
        ("LEDGER", "Reconcile revenue, fees and costs"),
        ("CRITIC", "Check evidence and challenge weak proposals"),
    ]
]
