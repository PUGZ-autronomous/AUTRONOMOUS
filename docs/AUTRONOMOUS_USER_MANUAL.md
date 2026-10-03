# AUTRONOMOUS user manual

Version 0.1.0-foundation | 3 October 2026 | Owner: Keiran Baker

## 1. Start here

AUTRONOMOUS is our customised version of NomaDamas/Ultron. This first build gives you an agent command screen, a control room, an honest runtime status, a persistent pause for new runs, and a plan for six worker roles. It is the foundation of the business system we discussed.

The default is DEMO MODE. It produces repeatable example results without a real AI worker. A successful demo proves the interface and control flow work; it does not prove that an agent researched a market, created a sellable product, or earned money.

The eventual aim is to research an opportunity, build something useful, sell it, reconcile the money and learn from the result. Business 001's first target is GBP 1 from a genuine external customer, with settlement and costs recorded. That business is still planned.

## 2. What works in this version

- Command screen: submit a request, display validated result cards, attach a supported image, and give feedback.
- Control room: inspect module evolution, recent runs, evidence, audit events, settings and session metrics.
- Mode indicator: shows a demo Hermes adapter or a selected live adapter. Live selection is explicitly unverified.
- Pause new runs: blocks newly admitted commands and benchmarks through the web API. Resume reopens admission.
- Persistent pause history: the pause flag and last ten control events are displayed through the status API; the complete history is stored locally.
- Worker plan: shows the six agreed roles as planned, with no invented activity.
- User manual: available from both screens and at /manual.

Not connected yet: real worker computers, Agent Zero, recurring schedules, store accounts, customer payments, financial reconciliation, enforced spending budgets, private remote deployment, or a global emergency stop. The existing web engine keeps its run/module state in memory. Its runs, feedback, module changes and metrics reset when the server restarts.

Upstream contains a separate SQLite engine implementation. That implementation is not wired into this web launcher, so the presence of SQLite code does not make the web dashboard restart-safe.

## 3. Install and open it

Use a local Linux or macOS machine with Python 3.11 or newer. For Windows, we will choose WSL or a separate Linux drive after inspecting your PC. Preserve existing files before changing operating systems.

If you have the source ZIP, extract it and open a terminal in the AUTRONOMOUS folder containing run.sh. If you have the Git bundle, clone it to recover the complete source and history:

```bash
git clone AUTRONOMOUS-foundation.bundle AUTRONOMOUS
cd AUTRONOMOUS
git switch build/autronomous-foundation
```

Start the application:

```bash
./run.sh
```

The launcher creates a Python environment, installs dependencies and starts a local server. Internet access is needed for dependency installation. Leave the terminal open while using it.

Open http://localhost:8799 for commands. Open http://localhost:8799/dashboard for the control room. Open http://localhost:8799/manual for this guide. These addresses refer to the machine running the server; they do not reach your home PC from Phuket by themselves.

The default port is 8799. If it is already in use, start with PORT=9000 ./run.sh and use localhost:9000. To select an installed Python version, use PYTHON=python3.11 ./run.sh.

## 4. Your first five-minute test

1. Open the control room. Confirm DEMO MODE and six planned roles.
2. Open Chat and submit: "Prepare a checklist for evaluating a digital product idea."
3. Inspect the result cards. They are demo output, not live research. Return to the control room to inspect the run and audit entries.
4. Press Pause new runs. Submit another command; the server should reject it with a paused message. Benchmarks are also blocked.
5. Stop the server with Ctrl+C, start ./run.sh again and check that the pause remains. The earlier run history will have reset.
6. Press Resume new runs and try another demo command.

For the automated checks, run .venv/bin/python -m pytest -q from the project folder. Tests requiring live services are skipped without their prerequisites; passing the suite does not validate a paid model connection.

## 5. The command screen

The command bar is where you ask for work. The canvas is where result cards appear. It is not a full transcript of everything a worker has done.

Replace (A) replaces the working canvas with the next result. Accumulate (B) keeps a bounded collection of results. Pins preserve selected cards within that browser session; they are not a durable file archive. Feedback contributes to the upstream harness evaluation workflow, not automatic proof that a product makes money.

Image input accepts one PNG, JPEG or WebP up to 4 MiB, within the upstream dimension limits. Vision output is demo output unless a real vision provider is selected and configured.

Each request can trigger a main run and a candidate/canary evaluation. That matters when live providers are connected: one click need not mean one paid model call. This release has no hard GBP spending cap.

## 6. The control room, in plain English

Core & mission tells you the selected execution mode, whether new runs are paused, and Business 001's planned objective. Revenue is shown as unconnected, rather than a made-up zero balance or sales figure.

Worker plan describes future responsibilities. A planned worker is not a running container, process or AI session.

Evolution ecology shows harness modules: small packages that shape prompts, tools, interface or policies. Seed means an initial module. Candidate means a proposed change. Survivor means a retained module. Decaying means becoming less useful. Pruned means removed from the active set. Quarantined means isolated after a safety problem. Lineage shows which module a new version came from.

Runs & evidence shows recorded executions and their provenance. A manifest describes the run's configuration. Evidence supports an evaluation. The append-only ledger here records software actions and audit events; it is not your bank account, business turnover or profit ledger.

Personalization / Self-evolution shows redacted usage summaries, feedback and proposals. It is not a permanent business memory system in this web release.

Safety / approvals shows upstream permission requests and evaluation state. The underlying mutation APIs are gated. This is not yet the proposed centre for approving advertising spend, supplier purchases or marketplace launches.

Model settings lets you save provider URLs, model names and keys. Keys are write-only in the interface, with redacted status returned. A configured key does not activate a live execution adapter or prove that a provider works. Metrics counts events during the current server process.

## 7. Pause, resume and restart

Pause new runs checks admission before a new web command or benchmark is accepted. A request already past that checkpoint can continue, including its candidate evaluation. Pause does not cancel a model request, stop a subprocess, close a browser or revoke a payment credential. It also does not control direct Python calls outside this web server.

The pause flag survives a restart. Its control history records the local operator identity and timestamp. On a brand-new state directory, demo mode starts enabled and a selected live Hermes adapter starts paused. Existing state wins: switching adapters is not a substitute for pressing Pause.

Stop this local server by pressing Ctrl+C in its terminal. Restart with ./run.sh. This release does not install a boot service. Automatic restart after a power cut remains deployment work.

Persistent files are separate from the source code. By default, admission state is in ~/.local/state/autronomous/control.sqlite3 and model settings are in ~/.config/ultron/secrets.json. AUTRONOMOUS_STATE_DIR changes the control location; ULTRON_CONFIG_DIR changes the settings location. Keep these directories separate from the repository and back them up securely. Model keys are stored locally as owner-restricted plaintext JSON, not encrypted vault storage.

If control state is unreadable or corrupt, startup fails rather than silently enabling execution. Preserve that file and investigate. Do not delete it just to get past a pause.

## 8. Meet the future workers

- SCOUT: researches opportunities and gathers sources, demand signals and competing prices.
- FORGE: builds products, tools, prototypes and drafts.
- MERCURY: prepares and operates approved sales channels.
- GROWTH: tests marketing and measures results.
- LEDGER: reconciles revenue, fees, refunds, AI usage and other costs.
- CRITIC: checks evidence and challenges weak proposals.

AUTRONOMOUS will coordinate these roles. They do not need six separate PCs. A role is a responsibility; a runtime is the actual isolated environment that executes it. Worker allocation, task routing and visible desktops still need implementing and testing.

Business cells will eventually own their objective, accounts, files, permissions, costs and outcomes. The first cell is planned as a small digital-product experiment. No product category or marketplace has been selected yet.

## 9. Before real AI or remote access

Keep this build on localhost. Opening either main page grants a local operator session automatically; there is no real login screen or multi-user authentication. CSRF protection helps protect requests but is not a substitute for controlling who can reach the server. Do not expose port 8799 publicly or forward it from the router.

Private remote access will be configured separately and tested from a second device. A tunnel/private network must restrict reachability to your devices. The server should continue binding to 127.0.0.1 unless we deliberately redesign and verify the access boundary.

Live activation has several independent parts: the Hermes adapter, generative UI, module synthesis and vision. ULTRON_ADAPTER=pinned-hermes selects the existing Hermes integration seam. ULTRON_UI_GENERATOR=model and ULTRON_MODULE_SYNTH=model select paid model-backed paths; ULTRON_VLM=model selects vision. The inherited ULTRON_ names and ultron Python package remain for compatibility.

Do not treat the upstream installation snippets as a verified live deployment. We must check the pinned Hermes API, isolate the worker runtime, configure a provider, perform a small bounded real run, verify the actual result and record the bill. The current Hermes runner changes process-wide working-directory/environment state during execution; concurrent live work needs an isolation review before use.

For now, leave the live selectors unset. No paid keys, store credentials or payment access are required for the demo. Saving a key while a model-backed component is selected can enable costs; the dashboard mode describes Hermes execution and does not certify every component is free.

## 10. NODE-001: hardware and recovery plan

Use the home PC first if its specification is suitable. We still need CPU, RAM, SSD capacity, GPU and current operating system. Do not buy a mini PC or wipe Windows before that check.

Planning target: a 64-bit processor, preferably four or more cores, 16 GB RAM and an SSD with ample free space. 32 GB RAM helps with multiple workers. API-backed AI does not require a powerful GPU; local-model requirements depend on the model and must be sized separately.

Buy only what the PC check shows is missing: an installation USB if we choose Linux, an Ethernet cable if needed, a separate SSD if we need to preserve the current drive, and optionally a UPS sized for the measured PC and router load. Prices and exact part numbers have not been researched for this build.

The eventual recovery chain is: power returns, firmware powers on, operating system boots, service/container runtime starts, AUTRONOMOUS restarts, private access reconnects, health checks run. Pause must stay paused through that chain. Full-disk encryption requiring a password at every boot would interrupt unattended recovery; choose its unlock design deliberately.

We will prove recovery with a controlled restart and a power-loss test only after backups and the hardware plan are ready. Restarts alone cannot repair a failed disk, router or motherboard.

## 11. Build sequence and timing

Foundation: this release provides branding, runtime visibility, admission control, role definitions and this manual. It is ready for local demo verification.

Next milestone: validate one real isolated worker and persistent web engine state. Planning estimate: 2-5 focused development sessions, depending on upstream compatibility. The exit test is a genuine bounded task, recorded result/cost and successful restart recovery.

After that: private NODE-001 deployment, boot recovery and backups. Planning estimate: 1-3 sessions after PC access and hardware choices are available. The exit test is secure access from another device plus recovery without a local login.

Then: Business 001, a chosen digital product, human-reviewed publishing, real payment integration and reconciled accounting. Planning estimate: 1-3 weeks of focused work after the foundations pass. Store approval and external services can extend this. Time to the first customer sale is unknown.

Finally: add schedules, the task queue, enforceable monetary limits, approval decisions and worker cancellation. Promote autonomy only after the relevant controls are tested. These are planning ranges, not a promise of passive income or a Phuket living budget.

## 12. Troubleshooting and ownership

Page will not load: confirm the terminal still runs, use the selected port and check the startup log. If the PC is remote, localhost on your phone points to your phone, not the server.

Session or CSRF error: reload the main page to obtain a fresh session, then retry. Opening another main page refreshes the browser cookies. Do not work around errors by removing server checks.

Command is paused: open the control room and Resume new runs when appropriate. Restarting is deliberately not a way around the pause.

Live unavailable / HTTP 503: the selected live integration lacks prerequisites or cannot complete. It should fail closed. Switching to demo changes the type of result; it does not fix live execution.

History disappeared: the current web engine is in memory. Restart persistence for that engine is a future milestone. The pause/settings files persist separately.

Dependency installation fails: confirm Python 3.11+, internet access and the error in the terminal. Keep the source and state directories; avoid repeated destructive reinstalls.

AUTRONOMOUS is a customised fork of NomaDamas/Ultron at upstream commit 2d1789795551e828ccc2efc4fe22f3b59b130d59. The original MIT licence and copyright notice are retained in LICENSE. This fork keeps the upstream source package and environment names to make future updates manageable.

Source: https://github.com/NomaDamas/Ultron
