# AUTRONOMOUS

Keiran Baker's customised foundation built on [NomaDamas/Ultron](https://github.com/NomaDamas/Ultron).

## Try it before NODE-001 is installed

[Open the browser demo setup](https://codespaces.new/PUGZ-autronomous/AUTRONOMOUS/tree/build/autronomous-foundation?quickstart=1) and follow the [short demo guide](docs/TRY_DEMO_NOW.md). Codespaces runs a temporary development computer; nothing is installed on your travel laptop. The demo launcher explicitly selects simulated providers and separate test state. This is not the permanent worker host.

For a repeatable server/restart check in an installed development environment:

```bash
.venv/bin/python scripts/smoke_demo.py
```

## Start here

```bash
./run.sh
```

Open **http://localhost:8799** for commands, **/dashboard** for the control room, and **/manual** for the user guide. Python 3.11+ and internet access for dependency installation are required. This launcher binds to localhost; do not expose the local operator session to the public internet.

**Default execution is deterministic demo mode.** Real worker computers, live AI validation, business operations, payments, financial budgets and unattended scheduling are not connected in this release.

## Foundation release

- AUTRONOMOUS branding on the existing command surface and control room.
- Runtime status distinguishes demo from a selected, unverified live adapter.
- Persistent, actor-audited **Pause new runs / Resume new runs** control.
- Paused admission blocks new commands and benchmarks; already admitted work may finish.
- Six planned roles: SCOUT, FORGE, MERCURY, GROWTH, LEDGER and CRITIC.
- Business 001 objective: GBP 1 external revenue, with settlement and costs reconciled.
- Revenue is unconnected; the software audit ledger is not financial accounting.
- A complete [user manual](docs/AUTRONOMOUS_USER_MANUAL.md), also served at `/manual`.

The web engine's runs, modules, feedback and metrics currently reset on restart. Model settings and the new-run pause persist separately. A global emergency stop and durable web engine are future milestones.

## Home PC and replaceable devices

AUTRONOMOUS will run on the home PC, NODE-001. Travel laptops and phones are replaceable control screens: closing or losing one must not stop the workers. Essential state, schedules and service credentials belong on the home node, with a separate backup. Remote access and recovery are still deployment work; see [NODE-001 requirements](docs/NODE_001_REQUIREMENTS.md).

## Verify

```bash
.venv/bin/python -m pytest -q
```

For packaging and validation details, see [BUILD_NOTES.md](docs/BUILD_NOTES.md). For inherited architecture and configuration, see [README_UPSTREAM.md](README_UPSTREAM.md). The technical Python package, cookies, and `ULTRON_` settings retain upstream names for compatibility. Both `autronomous` and `ultron` CLI entry points are supplied; they expose the inherited config CLI, not an autonomous business scheduler.

## Provenance

### Real vs seam

The inherited G001-G007 baseline and GAP1-GAP7 hardening cover real harness contracts, safety gates and audit behaviour. The default Hermes execution remains a deterministic demo seam. Live Hermes validation and business automation are separate work; upstream architecture details are preserved in README_UPSTREAM.md.

Based on upstream commit `2d1789795551e828ccc2efc4fe22f3b59b130d59`. The MIT licence and original notice remain in [LICENSE](LICENSE). No home PC was modified, and no paid model, marketplace or payment service was activated during the build.
