#!/usr/bin/env bash
# Optional Agent Reach bootstrap for AUTRONOMOUS (macOS/Linux).
# Run manually on the HOST running the agents, not in CI or at Ultron startup.
# No sudo, no system package changes, no browser cookie access.
set -euo pipefail

if ! command -v pipx >/dev/null 2>&1; then
  echo "pipx is required. Install it using your OS package manager and try again." >&2
  echo "Official guide: https://pipx.pypa.io/stable/installation/" >&2
  exit 2
fi

if ! command -v agent-reach >/dev/null 2>&1; then
  echo "[agent-reach] Installing the Panniantong GitHub project via pipx..."
  pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
else
  echo "[agent-reach] Existing command found; leaving it untouched."
  echo "[agent-reach] Verify its source before use; another project shares this package name."
fi

if ! command -v agent-reach >/dev/null 2>&1; then
  echo "Installed, but agent-reach is not on PATH. Run 'pipx ensurepath', reopen your shell, and retry." >&2
  exit 2
fi

echo "[agent-reach] Read-only dependency check (no --system flag)..."
agent-reach install --env=auto

echo "[agent-reach] Channel diagnostics..."
agent-reach doctor

echo "[agent-reach] Core check complete. Missing system tools or optional channels"
echo "are NOT installed automatically. Review docs/AGENT_REACH.md first."
