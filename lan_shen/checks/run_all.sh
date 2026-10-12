#!/bin/sh
# run_all.sh — the whole gate suite in one command. POSIX sh; no bash required.
#
# Modelled on Soul_Land_3_Project/checks/run_all.sh, the author's own established
# shape: one command, every layer, exit 0 means ALL GREEN.
#
# Nothing here writes anything. Every layer is read-only. Run it:
#   - before shipping a chapter
#   - after any ledger sync
#   - before publishing this repository anywhere
#
# Usage:  sh checks/run_all.sh          (from the repository root)
#         sh checks/run_all.sh --quick  (skip the two selftests)
#
# Exit codes. verify.py and canon_copy_check.py use 0=pass, 1=fail. style_gate.py
# uses a three-state contract — 0=pass, 1=fail, 2=pass-with-advisory-warnings — so
# layer 2 accepts 0 and 2. Chapter three runs above the house word band by design
# and is logged as deliberate in SERIAL_LOG, which means a bare 0 is not reachable
# for that layer and 2 is its honest green.

cd "$(dirname "$0")/.." || exit 2

QUICK=0
[ "${1:-}" = "--quick" ] && QUICK=1

PASS=0; FAIL=0; FAILED=""

layer() {  # layer "name" "accepted-exit-codes" command [args...]
  name="$1"; codes="$2"; shift 2
  out="$("$@" 2>&1)"; rc=$?
  ok=0
  for c in $(printf '%s' "$codes" | tr ',' ' '); do [ "$rc" = "$c" ] && ok=1; done
  if [ "$ok" = 1 ]; then
    PASS=$((PASS+1))
    tail="$(printf '%s\n' "$out" | grep -E 'RESULT|[0-9]+ files|[0-9]+ checks' | tail -1)"
    printf '  PASS  %-26s %s\n' "$name" "$tail"
  else
    FAIL=$((FAIL+1)); FAILED="$FAILED $name"
    printf '  FAIL  %-26s exit %s (accepted: %s)\n' "$name" "$rc" "$codes"
    printf '%s\n' "$out" | grep -E '  FAIL|  WARN|BLIND' | head -12 | sed 's/^/          /'
  fi
}

plain() { PASS=$((PASS+1)); printf '  PASS  %-26s %s\n' "$1" "$2"; }
bad()   { FAIL=$((FAIL+1)); FAILED="$FAILED $1"
          printf '  FAIL  %-26s %s\n' "$1" "$2"
          printf '%s\n' "$3" | head -8 | sed 's/^/          /'; }

echo "======================================================================"
echo " LAN SHEN — full gate suite"
echo "======================================================================"

layer "1 verify.py"           "0"   python3 tools/verify.py chapters
layer "2 style_gate.py"       "0,2" python3 tools/style_gate.py chapters
layer "3 canon_copy_check.py" "0"   python3 tools/canon_copy_check.py

# ---- 4. codex markers must never reach prose -------------------------------
# The ch3 defect class, twice: working glyphs left inside finished prose.
# Widened 2026-09-20 from two glyphs to the full working set. The ch13 leak was
# a red circle; nothing said the next one could not be a tick or a warning sign.
leak="$(grep -l '🔴\|🟢\|🟡\|🔵\|✅\|❌\|⚠️\|⭐' chapters/*.md 2>/dev/null)"
if [ -z "$leak" ]; then plain "4 marker-leak grep" "no codex markers in any chapter"
else bad "4 marker-leak grep" "codex markers leaked into prose" "$leak"; fi

# ---- 5. privacy: no personal identity may be published ---------------------
# The author has already had one live personal email reach public git history
# (see fix/scrub_email.sh in the workspace root, outside this repo). This repo is
# destined to be public. Gate the leak CLASS, not one string — and build the
# pattern from pieces so this file does not match itself.
AT='@'; DOT='.'
P1="gm5206663${AT}gmail${DOT}com"
P2="ghp_[A-Za-z0-9]{20}"
P3="309063472[+]"
P4="${AT}arena${DOT}local"
hits="$(grep -rniE "$P1|$P2|$P3|$P4" \
        --include='*.md' --include='*.py' --include='*.txt' --include='*.sh' . 2>/dev/null)"
if [ -z "$hits" ]; then plain "5 privacy grep" "no personal email / token / sandbox id"
else bad "5 privacy grep" "personal identity or credential in a public-bound repo" "$hits"; fi

# ---- 6. build hygiene ------------------------------------------------------
junk="$(find . -name '__pycache__' -o -name '*.pyc' -o -name '*.bak' -o -name '.DS_Store' 2>/dev/null)"
if [ -z "$junk" ]; then plain "6 build hygiene" "no __pycache__ / .pyc / .bak / .DS_Store"
else bad "6 build hygiene" "generated files committed to the tree" "$junk"; fi

# ---- 7/8. the gates must be able to fail ----------------------------------
# A gate that has never been seen to fail is a gate nobody has tested.
if [ "$QUICK" -eq 0 ]; then
  layer "7 selftest.py"      "0" python3 tools/selftest.py
  layer "8 kit selftest.py"  "0" python3 _kit_reference/tools/selftest.py
fi

# ---- 9. regression tokens --------------------------------------------------
# The layers above judge whether prose is WELL-FORMED. None of them can know that
# a particular number used to be right and now is not, or that a particular word
# belongs to the author rather than to the character. That knowledge only exists
# as a list, and this layer reads the list: foundation/BANNED_TOKENS.json.
# Imported from storyos-site. On its first run it found eight fourth-wall breaks
# in shipped prose and two current-state documents asserting superseded values.
layer "9 banned_token_check.py" "0" python3 tools/banned_token_check.py

echo "----------------------------------------------------------------------"
if [ "$FAIL" -eq 0 ]; then
  printf '  ALL GREEN — %s layers held, 0 failed\n' "$PASS"
  echo "----------------------------------------------------------------------"
  python3 tools/status_gen.py "9 layers ALL GREEN ($(date +%F))" 2>/dev/null | sed 's/^/  STATUS: /'
  exit 0
fi
printf '  %s held | %s FAILED:%s\n' "$PASS" "$FAIL" "$FAILED"
echo "----------------------------------------------------------------------"
echo "  Do not ship. Fix the gate if the gate is wrong; fix the work if the"
echo "  work is wrong. Never lower a threshold to make a layer pass."
python3 tools/status_gen.py "FAILED: $PASS held, $FAIL failed ($(date +%F))" 2>/dev/null | sed 's/^/  STATUS: /'
exit 1
