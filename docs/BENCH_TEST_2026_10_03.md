# Before-home test results - 3 October 2026

## Scope

Code under test: the AUTRONOMOUS foundation at commit 7fe8847e9765c834c6e0776ad3d343ade910fa73 plus the demo launcher, Codespaces configuration and smoke script in this update. No home PC, travel laptop, paid AI provider or cloud codespace was modified or started.

## Results

| Check | Result |
| --- | --- |
| Real loopback web-server startup | Passed |
| Four components explicitly in demo mode | Passed |
| Manual and dashboard asset responses | Passed |
| Demo command returns result cards and run provenance | Passed |
| Missing CSRF rejected | Passed |
| Pause rejects new commands and benchmarks | Passed |
| Persistent pause after server process is stopped and a new process starts | Passed |
| Restart retains the documented in-memory run-history limitation | Passed: web run history resets |
| Resume permits another demo command | Passed |
| Pause/resume control audit survives restart | Passed |
| Demo shell launcher overrides inherited live selectors and uses separate state | Passed |
| Shell syntax and Codespaces JSON syntax | Passed |

Executed: .venv/bin/python scripts/smoke_demo.py. The script prints a JSON report, starts two successive server processes, then removes its temporary state. The separate launcher check was performed with inherited selectors set to live; the launcher replaced all four with demo paths and the status endpoint confirmed this.

Targeted regression suite: tests/test_autronomous_control.py, tests/test_gap3_durable.py, tests/test_gap8_live.py and tests/test_gap8_redteam.py. Result: **39 passed, 2 skipped**. Live-seam tests use test doubles and unavailable-dependency checks; this does not validate an actual model/Hermes account. An inherited FastAPI/Starlette deprecation warning remains.

The previous full foundation suite remains **465 passed, 6 skipped**. This update adds a test-launch route and diagnostics without changing the application engine; no new full-suite result is claimed.

## Still to exercise

- Creating the actual GitHub Codespaces container and forwarding its private port.
- GitHub browser authentication and phone login/layout.
- Live Hermes/model execution, model billing and real task outputs.
- Durable web-engine run/module history.
- Home hardware resource use, firmware power recovery, OS/service startup, private remote access and backup restoration.

The Codespaces setup is a temporary demo bench. Its dependency preparation and actual cloud image build have not been executed here. Costs/remaining included allowance on the owner's GitHub account have not been inspected; no paid usage was enabled.
