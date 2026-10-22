#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/manage.py verify
python3 -m unittest discover -s tools -p 'test_*.py' -v
# Match reality: blocked work must refuse, genuinely resolved prerequisites may pass.
# Synthetic positive/negative fixtures test this without changing real source records.
python3 - <<'PY'
import subprocess
import sys
sys.path.insert(0, 'tools')
import manage
expected = 2 if manage.blockers(manage.ROOT) else 0
run = subprocess.run([sys.executable, 'tools/manage.py', 'ready'])
if run.returncode != expected:
    raise SystemExit(f'FAIL: readiness disagrees with actual blockers: expected {expected}, got {run.returncode}')
print('PASS: structural checks, regression tests and honest readiness/blocker agreement.')
PY
