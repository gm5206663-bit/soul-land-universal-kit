#!/bin/sh
# soul_land_3_new — prove the gate, then run it. Must exit 0 before any chapter is "done".
set -e
cd "$(dirname "$0")/.."
python3 checks/verify.py --selftest
echo "---"
python3 checks/verify.py
