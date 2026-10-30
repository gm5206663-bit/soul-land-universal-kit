#!/bin/sh
# tools/run_all.sh — the thin runner. ONE command, every check, exit 0 means green.
#
# This file is the door, not the law. The law is
#   https://github.com/gm5206663-bit/how-to-write-fanfiction  (guide v3.3 / law v5.7)
# If this runner and the guide disagree, the guide wins and this file is the thing that is wrong.
#
# WHY A THIN RUNNER AND NOT A COPY OF THE GUIDE'S TOOLS
#   The guide's rule is "one copy of one thing". Twelve repositories each holding their own copy
#   of check_manifest.py would be twelve methods, and they would drift. So this runner holds no
#   rules of its own: it calls the checks that live in THIS repository and reports what ran.
#
# EDIT THE TWO MARKED LINES, THEN COMMIT. Nothing else here needs to change.
#
# USAGE
#   sh tools/run_all.sh            # everything
#   sh tools/run_all.sh --quick    # skip the selftests (local iteration only)
#
# EXIT  0 all green · 1 anything red

cd "$(dirname "$0")/.." || exit 2

QUICK=0
[ "${1:-}" = "--quick" ] && QUICK=1

PASS=0; FAIL=0; FAILED=""; CSS=0

layer() {  # layer <name> <accepted exit codes, comma separated> <command...>
  name="$1"; codes="$2"; shift 2
  out=$("$@" 2>&1); rc=$?
  for c in $(printf '%s' "$codes" | tr ',' ' '); do
    if [ "$rc" = "$c" ]; then
      PASS=$((PASS+1))
      printf '  PASS  %-32s %s\n' "$name" "$(printf '%s\n' "$out" | grep -E 'SELFTEST:|RESULT:|^PASS:|ALL GREEN|OK$' | tail -1)"
      return 0
    fi
  done
  FAIL=$((FAIL+1)); FAILED="$FAILED $name"
  printf '  FAIL  %-32s exit %s (accepted: %s)\n' "$name" "$rc" "$codes"
  printf '%s\n' "$out" | grep -E 'FAIL|ERROR|Error|Traceback' | grep -v '^  PASS' | head -6 | sed 's/^/          /'
}

echo "======================================================================"
echo " $(basename "$(pwd)") — the battery"
echo "======================================================================"

# ---- EDIT LINE 1: the gates this repository actually has -------------------
# One line per check. Accepted exit codes come second: a gate that returns 2 for
# "warnings only" is normal — list both, 2,0, and say so in a comment.
layer "structure gate"      "0"   python3 tools/verify.py
# layer "style gate"        "0,2" python3 tools/style_gate.py
# layer "canon copy"        "0"   python3 tools/canon_copy.py
# ---------------------------------------------------------------------------

# ---- EDIT LINE 2: the selftests --------------------------------------------
# A gate that has never been seen to fail is not a gate. Keep these.
if [ "$QUICK" -eq 0 ]; then
  layer "gate selftest"     "0"   python3 tools/verify.py --selftest
  # layer "selftest suite"  "0"   python3 tools/selftest.py
fi
# ---------------------------------------------------------------------------

# ---- manifest: independent proof (do not remove) ---------------------------
# The repository must be able to prove its files are the files it checked.
if [ -f MANIFEST.sha256 ]; then
  layer "manifest"          "0"   python3 tools/manifest.py
else
  printf '  SKIP  %-32s %s\n' "manifest" "no MANIFEST.sha256 yet — see docs/METHOD_CONFORMANCE.md §5"
  CSS=$((CSS+1))
fi

echo "----------------------------------------------------------------------"
if [ "$FAIL" -eq 0 ]; then
  printf '  ALL GREEN — %s layers held\n' "$PASS"
  [ "$CSS" -gt 0 ] && printf '  %s layer(s) skipped — a skip is not a pass, it is an open item\n' "$CSS"
  exit 0
fi
printf '  %s held | %s FAILED:%s\n' "$PASS" "$FAIL" "$FAILED"
echo "  Do not ship. Fix the gate if the gate is wrong; fix the work if the work is wrong."
echo "  Weakening a gate to make this line green is the one move the method forbids."
exit 1
