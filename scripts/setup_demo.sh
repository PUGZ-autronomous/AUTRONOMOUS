#!/usr/bin/env bash
# Installs into the development machine, not the browser user's laptop.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi
.venv/bin/python -m pip install --disable-pip-version-check --timeout 30 -e ".[dev]"
echo "Demo environment ready. Run: bash scripts/start_demo.sh"
