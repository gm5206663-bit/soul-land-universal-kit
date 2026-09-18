#!/bin/sh
# checks/verify.sh — light invariant gates for SOUL_LAND_NEW (言天宇 project)
# Run from repo root:  sh checks/verify.sh
# Keeps the two-copies law + the "nothing is absolute" law mechanical.

cd "$(dirname "$0")/.."
FAIL=0

say()  { printf '%s\n' "$*"; }
fail() { say "❌ $*"; FAIL=1; }
ok()   { say "✅ $*"; }

# --- 1. Two-copies law: the key numbers must agree across CURRENT_STATE + STATUS + BIBLE ---
for n in "30" "1,300" "3,200" "先天满魂力"; do
  c=$(grep -c -- "$n" bible/CURRENT_STATE_PRE11.md bible/TIANYU_STATUS_PRE11.md bible/BIBLE_TIANYU.md 2>/dev/null | awk -F: '{s+=$2} END{print s}')
  if [ "$c" -ge 3 ]; then ok "number '$n' present in all 3 core docs ($c)";
  else fail "number '$n' missing from a core doc (only $c hits)"; fi
done

# --- 2. Stale-number guard (the old nerf class) ---
if grep -rqn "rank 27\|Rank 27\|yellow first ring\|~800 years\|800-year.*first" bible/ 2>/dev/null; then
  fail "stale rank-27 / yellow-first-ring number found — kill it at the source"
else ok "no stale 27 / yellow-first numbers"; fi

# --- 3. Nothing-is-absolute: no bare immunity phrasing on the ring doctrine ---
BAD=$(grep -rn "no mutation ever\|never mutates;\|too supreme to bend\|never fuses, never mutates" bible/ 2>/dev/null)
if [ -n "$BAD" ]; then fail "absolute-claim phrasing still present: $BAD"; else ok "ring doctrine holds the living-threshold (no absolute immunity)"; fi

# --- 4. Who-knows firewall: nobody outside the circle is credited with the dragon ---
if grep -rqn "马小桃.*knows.*黑暗圣龙\|贝贝.*knows.*黑暗圣龙\|唐雅.*knows.*黑暗圣龙\|苏凝.*knows.*黑暗圣龙\|world.*knows.*黑暗圣龙" bible/ chapters/ 2>/dev/null; then
  fail "knowledge-firewall leak (dragon known beyond the circle)"
else ok "knowledge firewall intact (dragon confined to the circle)"; fi

# --- 5. Dragon never visibly ringed ---
if grep -rqn "黑暗圣龙.*第.*魂环\|dragon.*third ring\|圣龙.*紫\|圣龙.*黑.*ring" bible/ 2>/dev/null; then
  fail "dragon described as ringed — load-bearing violation"
else ok "dragon stays ringless (双生武魂 hidden)"; fi

# --- 6. Chapters present & footer carries the contract ---
set -- chapters/chapter_*.md
if [ ! -f "$1" ]; then fail "no chapters found at all"; fi
for ch in chapters/chapter_*.md; do
  [ -f "$ch" ] || continue
  b=$(basename "$ch" .md)
  grep -q "🦋 BUTTERFLIES SHOWN" "$ch" && grep -q "WIRES:" "$ch" \
    && ok "$b footer contract present" || fail "$b footer missing the contract"
  # Perspective-Panel Doctrine (Law 2.1): every chapter must stage ≥1 canon-sourced
  # panel belonging to someone who is not 言天宇. Grep the panel marker.
  if grep -q "### Panel:" "$ch" && grep -q "### Panel ends" "$ch"; then
    ok "$b carries a non-OC panel (multiple perspectives)"
  else
    fail "$b has no non-OC panel — Perspective-Panel Doctrine violated"
  fi
done

# --- 7. Prose hygiene: no leftover leak/count/name artifacts in chapters ---
BAD7=$(grep -rn "Classroom three\|work-study boy\|Grandfather's idea\|million years of cold\|forty-three\|forty-fourth\|Yuan!\|43 others\|duke's bastard\|Duke's" chapters/ 2>/dev/null)
if [ -n "$BAD7" ]; then fail "prose artifact(s) still present: $BAD7"; else ok "prose clean of count/leak artifacts"; fi

# --- 8. Bible hygiene: no stale scale/age markers ---
BAD8=$(grep -rn "43 others + him\|~14–17 now\|Rank ~27–28 → 30\|ep ~7–8 / novel" bible/ 2>/dev/null)
if [ -n "$BAD8" ]; then fail "bible stale marker(s) still present: $BAD8"; else ok "bible clean of stale markers"; fi

say ""
if [ "$FAIL" -eq 0 ]; then say "verify: all gates green (exit 0)"; else say "verify: $FAIL gate(s) red — fix at source, not by weakening a check"; fi
exit "$FAIL"
