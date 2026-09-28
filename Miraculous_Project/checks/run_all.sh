#!/usr/bin/env bash
# THE GATE — run after every chapter sync AND at any time. Red = fix before
# the next chapter. Order: truth → never-allowed → locks → presence → voice →
# cockpit → sync → ledger → docs → world → utilization → evidence build.
cd "$(dirname "$0")/.."
fail=0
for c in state zero_tolerance prose_floor verify_locks presence_audit voice_check brief sync_audit divergence_engine workspace_audit world_tick completeness_audit; do
  if ! python3 checks/$c.py; then fail=1; fi
done
python3 checks/build_butterfly_effects.py || fail=1
echo "=============================================="
if [ $fail -eq 0 ]; then echo "GATE: GREEN — the story is honest"; else echo "GATE: RED — fix the FAILs above before writing on"; fi
exit $fail
