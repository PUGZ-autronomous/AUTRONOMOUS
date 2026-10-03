# AUTRONOMOUS foundation build notes

Build date: 3 October 2026. Branch: `build/autronomous-foundation`.

## Starting point and changes

Upstream: NomaDamas/Ultron, commit `2d1789795551e828ccc2efc4fe22f3b59b130d59`.

The original README is preserved as README_UPSTREAM.md. The original MIT licence and attribution remain unchanged. The Python package, upstream engine and configuration names remain compatible; the distribution now supplies an additional `autronomous` CLI alias.

This release changes the user-facing branding, adds an honest runtime/worker/mission panel, serves the manual at `/manual`, and persists a new-run admission pause with actor-attributed control history. The pause gates web SUBMIT_REQUEST and RUN_BENCHMARK actions after session/CSRF checks. It is not cancellation, a process supervisor, a spending limit or control of direct Python engine calls.

The worker roles and Business 001 are planning definitions. Revenue remains null/unconnected. No account, payment, API key, home PC, operating system or paid provider was changed. The web engine remains in memory; only model settings and admission control persist in this launcher.

## Validation

- Unmodified upstream baseline: 461 passed, 6 skipped.
- Final suite: 465 passed, 6 skipped. Skips require live prerequisites; live providers are not validated.
- Added behavioural checks cover paused command/benchmark rejection, unchanged engine state when denied, recovery across application recreation, resume, audit actor/history, session/scope/CSRF enforcement, strict boolean input, live first-start pause and corrupt-state failure.
- JavaScript syntax checked for the command and control-room scripts.
- PDF manual rendered and visually inspected; six pages.
- A real headless browser check was attempted but could not run: the runtime had no Chromium executable, and the browser download returned an invalid archive. Desktop/mobile visual UI testing remains outstanding. No browser pass is claimed.
- Existing FastAPI/Starlette deprecation warnings remain in the inherited suite.

## Run locally

Use Python 3.11+ and execute `./run.sh` from the project directory. The launcher installs editable dependencies and binds to 127.0.0.1:8799. It intentionally does not install a boot service. See docs/AUTRONOMOUS_USER_MANUAL.md for use, recovery, configuration and limitations.

The manual HTML is generated from the Markdown guide using `scripts/render_manual.py` in an environment containing reportlab. Its PDF output is written to the parent workspace's output folder.

## Handoff and GitHub

The authenticated GitHub account is PUGZ-autronomous. At build time the installation selected all repositories but returned no accessible repositories. Both PUGZ-autronomous/AUTRONOMOUS and PUGZ-autronomous/Ultron returned 404. No remote write or pull request was performed. The available GitHub operations did not include repository creation/forking.

Update, 3 October 2026: the user has now created https://github.com/PUGZ-autronomous/AUTRONOMOUS. Write access is verified and its main branch matches the upstream baseline. The foundation and replaceable-device requirements are being submitted on build/autronomous-foundation for review. NODE-001 is the home PC; the current travel laptop is a control client.

The source ZIP contains the exact committed source and a self-contained Git bundle with the foundation branch and upstream main history. A fresh checkout can be recovered with:

```bash
git clone AUTRONOMOUS-foundation.bundle AUTRONOMOUS
cd AUTRONOMOUS
git switch build/autronomous-foundation
```

Once a user-owned fork exists, use its confirmed URL as `origin`, retain NomaDamas/Ultron as `upstream`, push the foundation branch and open a pull request. Do not push changes into the upstream author's repository. Do not merge or activate live providers as part of the handoff without the appropriate subsequent instruction.

## Next exit criteria

1. Make the user-owned fork accessible and preserve this branch there.
2. Run the desktop/mobile browser check in a browser-capable environment.
3. Verify one pinned real Hermes worker in an isolated runtime, with bounded usage and an actual recorded cost.
4. Wire the durable engine into the web launcher and prove run/history recovery without changing adapter selection or safety semantics.
5. Inspect NODE-001 specifications; configure private access, boot recovery and backups.
6. Choose Business 001's product/channel; add payments and financial reconciliation before displaying revenue or profit.
7. Add a scheduler, queue, enforceable spend reservations and a genuine cancellation/emergency-stop mechanism before unattended business operations.
