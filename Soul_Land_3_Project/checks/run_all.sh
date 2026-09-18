#!/bin/sh
# checks/run_all.sh — the verification suite (rebuilt miniature, 2026-08-30).
# The original eleven-layer suite was not uploaded; these two layers are the ones
# that catch the two-copies disease (D1–D8) and the frozen-progression disease.
set -e
cd "$(dirname "$0")/.."
echo "── Layer 0: state.py (re-derive from footers) ──────────────────"
python3 checks/state.py
echo
echo "── Layer 1: verify_footer_facts.py (cross-check every copy) ────"
python3 checks/verify_footer_facts.py
echo
echo "── Layer 1b: prose_floor.py (appearance window; counts advisory) ──"
python3 checks/prose_floor.py
echo
echo "── Layer 2: verify_locks.py (locks · voice · retired numbers) ─"
python3 checks/verify_locks.py
echo
echo "── Layer 3: sync_audit.py (docs carry end-of-chapter state) ───"
python3 checks/sync_audit.py
echo
python3 checks/zero_tolerance.py || exit 1
echo
python3 checks/presence_audit.py || exit 1
echo
python3 checks/workspace_audit.py || exit 1
echo
echo "run_all: exit 0"
echo '--- Layer 7: divergence ---'
python3 checks/divergence_engine.py || exit 1
echo '--- Layer 9: completeness ---'
python3 checks/completeness_audit.py || exit 1
