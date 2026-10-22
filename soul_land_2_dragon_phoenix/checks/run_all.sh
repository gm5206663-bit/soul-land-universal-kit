#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/manage.py verify
python3 -m unittest discover -s tools -p 'test_*.py' -v
# This release contains a foundation, not an authorized prose chapter.
set +e
python3 tools/manage.py ready
code=$?
set -e
if [ "$code" -ne 2 ]; then
  echo "FAIL: foundation-only release must honestly refuse chapter readiness (expected exit 2, got $code)."
  exit 1
fi
echo 'PASS: structural checks, regression tests and expected pre-draft refusal.'
