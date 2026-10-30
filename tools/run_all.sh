#!/bin/sh
# tools/run_all.sh — the kit's own battery. One command, every layer, exit 0 means green.
#
# WHY THIS EXISTS
#   On 2026-10-30 a conformance pass measured all thirteen repositories against the method
#   in `how-to-write-fanfiction` (docs/03: "The battery is one command and must exit 0").
#   The kit scored 3 of 5. It had a gate (`tools/check.py`), a manifest and a status — but no
#   battery of its own, because every battery in it belonged to a serial
#   (`lan_shen/checks/run_all.sh`, `adaptive_prodigy/checks/run_all.sh`). The repository that
#   holds the whole corpus was the one repository you could not check in one command.
#
#   This file is that command. It runs the kit's own layers and then each serial battery that
#   exists, and it reports a coverage line, because the method is explicit:
#   "a coverage line is a claim — it gets checked like one."
#
# USAGE
#   sh tools/run_all.sh            # every layer
#   sh tools/run_all.sh --quick    # skip the selftests and the per-serial batteries
#
# EXIT
#   0 every layer held · 1 anything red

cd "$(dirname "$0")/.." || exit 2

QUICK=0
[ "${1:-}" = "--quick" ] && QUICK=1

PASS=0; FAIL=0; FAILED=""

layer() {  # layer "<name>" "<accepted exit codes>" command...
  name="$1"; codes="$2"; shift 2
  out=$("$@" 2>&1); rc=$?
  for c in $(printf '%s' "$codes" | tr ',' ' '); do
    if [ "$rc" = "$c" ]; then
      PASS=$((PASS+1))
      tail="$(printf '%s\n' "$out" | grep -E 'SELFTEST:|RESULT:|KIT-CHECK:|^PASS:|ALL GREEN' | tail -1)"
      printf '  PASS  %-34s %s\n' "$name" "$tail"
      return 0
    fi
  done
  FAIL=$((FAIL+1)); FAILED="$FAILED $name"
  printf '  FAIL  %-34s exit %s (accepted: %s)\n' "$name" "$rc" "$codes"
  # the REASON must be on the screen, not buried in a log the author has to open
  printf '%s\n' "$out" | grep -E 'FAIL|ERROR|Error|Traceback' | grep -v '^  PASS' | head -6 | sed 's/^/          /'
}

echo "======================================================================"
echo " SOUL LAND UNIVERSAL KIT — the kit's own battery"
echo "======================================================================"

# 1. the kit's gate: links, spine, manifest, structure, duplicates
layer "1 check.py (strict)" "0" python3 tools/check.py --strict

# 2+3. the selftests — a gate that has never been seen to fail is untested
if [ "$QUICK" -eq 0 ]; then
  layer "2 check.py --selftest"     "0" python3 tools/check.py --selftest
  layer "3 conformance --selftest"  "0" python3 tools/method/conformance.py --selftest
  # the drop-in manifest tool that six repositories will use; its selftest is the only proof
  # it can catch a tampered tree, and an unproven proof is not proof
  layer "3b manifest --selftest"    "0" python3 tools/method/manifest.py --selftest
fi

# 4. link sweep over the governing documents, uncached
layer "4 docs links" "0" python3 tools/check.py

# ---- the serial batteries that exist ---------------------------------------
# The kit holds fourteen serials. Two carry a one-command battery; the rest carry their own
# gates and are measured by the register. The count is printed rather than assumed, so a
# serial gaining a battery shows up here instead of being silently missed.
if [ "$QUICK" -eq 0 ]; then
  # Each serial battery carries its own shebang and some use bashisms (`set -o pipefail`).
  # Running them all with `sh` failed soul_land_2_dragon_phoenix with "Illegal option -o
  # pipefail" — a bug in THIS file, not in that serial. Run each the way its author meant.
  found=0
  for b in */checks/run_all.sh; do
    [ -f "$b" ] || continue
    found=$((found+1))
    case "$(head -1 "$b")" in
      *bash*) interp=bash ;;
      *)      interp=sh ;;
    esac
    layer "5.$found ${b%/checks/run_all.sh}" "0" "$interp" "$b"
  done
  if [ "$found" -eq 0 ]; then
    printf '  INFO  %-34s %s\n' "serial batteries" "none found — run the register for the corpus"
  fi
fi

# ---- the corpus layer ------------------------------------------------------
# The serial batteries above cover five of the fourteen projects. A battery that covers the
# projects it happens to know about is doing what the guide warns about: "registering what
# they happened to look at, not what was there." These two layers cover the WHOLE tree —
# every chapter-bearing directory on disk, all 33 of them, with a coverage line.
if [ "$QUICK" -eq 0 ]; then
  # READ-ONLY ON PURPOSE. The first version of this layer wrote refreshed account_report.*
  # files into the tracked tree, which silently broke their byte-identity with the copies in
  # SOUL_LAND_WORKSPACE/kit/ — a gate that mutates the repository manufactures the very drift
  # it was hired to detect. Regenerating state is an explicit act (`tools/register_drift.py
  # --write`, `account.py report --out-prefix …`), never a side effect of checking.
  layer "6 account control centre" "0" python3 SOUL_LAND_UNIVERSAL_KIT/tools/account.py report \
        --root . --out-prefix "${TMPDIR:-/tmp}/kit-account-report"
  layer "7 register drift"         "0" python3 tools/register_drift.py
fi

echo "----------------------------------------------------------------------"
TOTAL=$((PASS+FAIL))
if [ "$FAIL" -eq 0 ]; then
  printf '  ALL GREEN — %s layers held, 0 failed\n' "$PASS"
  printf '  coverage: %s of %s layers attempted\n' "$PASS" "$TOTAL"
  exit 0
fi
printf '  %s held | %s FAILED:%s\n' "$PASS" "$FAIL" "$FAILED"
printf '  coverage: %s of %s layers attempted\n' "$PASS" "$TOTAL"
echo "  Do not ship. Fix the gate if the gate is wrong; fix the work if the work is wrong."
exit 1
