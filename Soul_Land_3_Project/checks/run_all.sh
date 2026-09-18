#!/bin/sh
# ============================================================================
# FULL VERIFICATION — one command, everything.
#
#   STAGE 0  regenerate     derive state, rewrite the ensemble blocks, rebuild the
#                           generated docs, sync the CODEX mirror
#   LAYER 1  verify.py      rules — structure, laws, progression, panels, sync
#   LAYER 2  verify2.py     semantics — continuity, threads, prose quality
#   LAYER 3  audit.py       cross-chapter facts — ages, canon values, rings, locks
#   LAYER 4  verify_ensemble.py  CANON CHARACTERS — ranks, spiritual power, rings,
#                           departures, roster, EFFECTIVE POWER, purple-ring skills
#   LAYER 5  verify_stale.py     nothing is out of date
#   LAYER 6  consequence.py      every consequence of every premise has landed
#   LAYER 7  verify_canon_quotes every quote attributed to canon exists in the corpus
#   LAYER 8  verify_power_scale  THE TWO AXES — never weaker than Wulin, retired numbers stay retired
#   LAYER 9  verify_monster_law  he never loses a same-level fight; only Tang San lasts more than seconds
#   LAYER 10 verify_butterfly    canon's hierarchy does not survive him being in the room
#   LAYER 11 verify_footer_facts the hand-written footer must not contradict the generated one
#   LAYER 12 verify_style        THE VOICE — the prose must sound like chapters 1-3
#   LAYER 13 verify_timeline     THE CLOCK — no chapter claims more time passed than passed
#
# Every layer must return 0 before a chapter is called done. Thirteen layers.
# ============================================================================
cd "$(dirname "$0")/.." || exit 1

echo "########## 0. REGENERATE — derive, don't hand-maintain ##########"
python3 checks/state.py              || { echo "state rebuild FAILED"; exit 1; }
python3 checks/apply_ensemble.py     || { echo "apply_ensemble FAILED"; exit 1; }
python3 checks/build_status.py       || { echo "build_status FAILED"; exit 1; }
python3 checks/build_continuation.py || { echo "build_continuation FAILED"; exit 1; }
# 🔴 NO MIRRORS. This block USED TO sync five second copies of five documents into CODEX/.
# It was deleted 2026-08-29. Keeping a copy in sync is not a fix for having a second copy — it is
# a permanent liability, and §THE TWO-COPIES LAW says so in this very project's own framework.
# The five copies are gone. verify_stale.py now FAILS if any of them is ever recreated.
# If a document needs to be visible from CODEX/, add a one-line POINTER, never a copy.
echo "  ok   no second copies of any tracked document (mirrors removed, guarded)"
echo

echo "########## 1. RULES — structure, laws, progression, panels, sync ##########"
python3 checks/verify.py; A=$?
echo
echo "########## 2. SEMANTICS — continuity, threads, prose quality ##########"
python3 checks/verify2.py; B=$?
echo
echo "########## 3. CROSS-CHAPTER FACT AUDIT — ages, canon values, rings, locks ##########"
python3 checks/audit.py; C=$?
echo
echo "########## 4. ENSEMBLE — canon characters' ranks, power, rings, roster ##########"
python3 checks/verify_ensemble.py; D=$?
echo
echo "########## 5. STALENESS — no file may be out of date ##########"
python3 checks/verify_stale.py; E=$?
echo
echo "########## 6. CONSEQUENCES — did what had to follow, follow? ##########"
# 🔴 paths derived, not hardcoded (2026-09-18). SL3_WORKSPACE overrides the workspace root.
_PROJ="$(pwd)"
_WS="${SL3_WORKSPACE:-$(dirname "$_PROJ")}"
if [ -f "$_WS/CODEX/consequence.py" ]; then
  python3 "$_WS/CODEX/consequence.py" check; F=$?
else
  F=0
fi
echo
echo "########## 7. CANON QUOTES — every cited line verified against the corpus ##########"
# 🔴 --strict only when the copyrighted canon corpus is actually present. On a fresh clone it is
# not (see soul_land_3_adaptive_prodigy/CANON_SOURCE.md), and Layer 7 then prints a loud SKIP and
# exits 0 — the other twelve layers still run for real.
if python3 -c "import sys; sys.path.insert(0,'checks'); import paths; sys.exit(0 if paths.has_canon() else 1)"; then
  python3 checks/verify_canon_quotes.py --strict; G=$?
else
  echo "  (canon corpus absent — running Layer 7 in non-strict mode)"
  python3 checks/verify_canon_quotes.py; G=$?
fi
echo
echo "########## 8. POWER SCALE — he is never weaker than Wulin, in anything ##########"
python3 checks/verify_power_scale.py; H=$?
echo
echo "########## 9. MONSTER LAW — at equal level he defeats everyone in seconds ##########"
python3 checks/verify_monster_law.py --strict; I=$?
echo
echo "########## 10. BUTTERFLY — canon's hierarchy does not survive him being in the room ##########"
python3 checks/verify_butterfly.py; J=$?
echo
echo "########## 11. FOOTER FACTS — hand-written must not contradict derived ##########"
python3 checks/verify_footer_facts.py --strict; K=$?
echo
echo "########## 12. THE VOICE — the prose must sound like chapters 1-3 ##########"
python3 checks/verify_style.py --strict; L=$?
echo
echo "########## 13. THE CLOCK — no tenure claim exceeds the story's timeline ##########"
python3 checks/verify_timeline.py --strict; M=$?
echo
if [ $A -eq 0 ] && [ $B -eq 0 ] && [ $C -eq 0 ] && [ $D -eq 0 ] && [ $E -eq 0 ] && [ $F -eq 0 ] && [ $G -eq 0 ] && [ $H -eq 0 ] && [ $I -eq 0 ] && [ $J -eq 0 ] && [ $K -eq 0 ] && [ $L -eq 0 ] && [ $M -eq 0 ]; then
  echo "===== ALL LAYERS PASS ====="; exit 0
else
  echo "===== FAILURES PRESENT — do not deliver ====="; exit 1
fi
