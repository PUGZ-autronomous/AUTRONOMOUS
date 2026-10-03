#!/usr/bin/env bash
# An explicitly simulated, separate test bench. No home-node installation.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ ! -x .venv/bin/python ]; then
  echo "Run bash scripts/setup_demo.sh first." >&2
  exit 1
fi
export ULTRON_ADAPTER=fake
export ULTRON_UI_GENERATOR=fake
export ULTRON_MODULE_SYNTH=fake
export ULTRON_VLM=fake
export ULTRON_LIVE_MODEL=0
export ULTRON_DOTENV_PATH="$PWD/.autronomous_demo/unused.env"
export ULTRON_CONFIG_DIR="$PWD/.autronomous_demo/config"
export AUTRONOMOUS_STATE_DIR="$PWD/.autronomous_demo/state"
export ULTRON_SECURE_COOKIES=0
if [ "${CODESPACES:-false}" = "true" ]; then
  export ULTRON_SECURE_COOKIES=1
  echo "Codespaces: keep port 8799 PRIVATE. Open its forwarded browser address."
fi
echo "AUTRONOMOUS DEMO: all four execution components are simulated."
echo "http://localhost:8799/dashboard"
exec .venv/bin/python -m uvicorn ultron.app.server:create_app --factory --host 127.0.0.1 --port 8799
