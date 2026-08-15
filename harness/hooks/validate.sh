#!/usr/bin/env bash
# Harness validation gate — run before declaring prompt/host/model work done.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "== harness: import check =="
if [[ -d .venv ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi
python -c "from li_sim.engine import load_profiles, load_schedule; load_profiles(); load_schedule(); print('imports ok')"

echo "== harness: evals =="
python harness/evals/run_all.py

echo "== harness: validate passed =="
