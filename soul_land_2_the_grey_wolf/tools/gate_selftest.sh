#!/usr/bin/env bash
# SCOPE FIXTURE — SOUL LAND 2 / THE GREY WOLF
#
# House law: "A gate that has only ever been seen to pass is a gate nobody
# has tested."  and  "If you add an eighth gate, add an eighth fixture."
#
# The style gate can fail in two ways: it can miss a defect that is there
# (a false pass), or it can pass because it looked at nothing (a scope
# failure). The old gate did both: chapters 07-10 were published while the
# gate read `chapters/` and found six files. This fixture tests the SECOND
# failure mode — that the gate notices when its scope is not whole.
#
# Seven fixtures. Every one of them breaks the tree on purpose, runs the
# gate, and restores the tree. If any fixture does not fail the gate, the
# gate is not trustworthy and this script exits non-zero.
#
# Run:  bash tools/gate_selftest.sh

set -u
cd "$(dirname "$0")/.." || exit 1
ROOT="$PWD"
TMP="$(mktemp -d)"
OUT="$TMP/gate.out"
RESTORE=()

cleanup() {
  for r in "${RESTORE[@]:-}"; do
    [ -n "$r" ] && [ -e "$r" ] && mv "$r" "${r%.hidden*}"
  done
  rm -rf "$TMP"
}
trap cleanup EXIT

pass=0; fail=0
ok()  { printf '  \033[32mPASS\033[0m  %s\n' "$1"; pass=$((pass+1)); }
bad() { printf '  \033[31mFAIL\033[0m  %s\n' "$1"; printf '        %s\n' "$2"; fail=$((fail+1)); }

# Command substitution, never a pipe: `cmd | tail` returns tail's exit code
# and this house has already been burned by that twice.
gate() { python3 tools/style_gate.py > "$OUT" 2>&1; echo $?; }

expect_pass() {
  local label="$1" code; code=$(gate)
  if [ "$code" -eq 0 ]; then ok "$label"; else bad "$label" "gate exited $code: $(grep -m1 '^FAIL' "$OUT")"; fi
}
expect_fail() {
  local label="$1" want="$2" code; code=$(gate)
  if [ "$code" -eq 0 ]; then bad "$label" "gate PASSED — it did not notice"
  elif ! grep -q "$want" "$OUT"; then bad "$label" "exited $code but never said '$want'"
  else ok "$label"; fi
}

hide() { mv "$1" "$TMP/hidden_$(basename "$1")"; RESTORE+=("$TMP/hidden_$(basename "$1")"); }
show() { local h="$TMP/hidden_$(basename "$1")"; mv "$h" "$1"; for i in "${!RESTORE[@]}"; do
         [ "${RESTORE[$i]}" = "$h" ] && unset 'RESTORE[i]'; done; }

printf '\nSCOPE FIXTURE — the grey wolf style gate\n'
printf '%s\n' "──────────────────────────────────────────────────────────────────────"

# ── 1. the clean tree passes ─────────────────────────────────────────────
expect_pass "1. clean tree — the gate passes"

# ── 2. an author edition with no reader edition ──────────────────────────
mv manuscript/Chapter_10_The_Combat_Exam.md "$TMP/R10.md"
expect_fail "2. chapter never published — gate names the gap" "author edition exists but no reader edition"
mv "$TMP/R10.md" manuscript/Chapter_10_The_Combat_Exam.md

# ── 3. THE ORIGINAL DEFECT: a published chapter with no author edition ───
cp chapters/Chapter_10_The_Combat_Exam.md "$TMP/C10.md"
rm chapters/Chapter_10_The_Combat_Exam.md      # author edition gone, published copy stays
expect_fail "3. published but never gated — the chapters 07-10 defect" "PUBLISHED with no author edition"
cp "$TMP/C10.md" chapters/Chapter_10_The_Combat_Exam.md

# ── 4. the dialogue floor ────────────────────────────────────────────────
cp chapters/Chapter_06_The_Hem_Road.md "$TMP/C06.keep"
sed -i 's/"//g' chapters/Chapter_06_The_Hem_Road.md
expect_fail "4. dialogue stripped to zero — floor of 3 holds" "dialogue 0 < floor 3"
cp "$TMP/C06.keep" chapters/Chapter_06_The_Hem_Road.md

# ── 5. the 60-word ceiling ───────────────────────────────────────────────
cp chapters/Chapter_06_The_Hem_Road.md "$TMP/C06.keep"
python3 - <<'PY'
p='chapters/Chapter_06_The_Hem_Road.md'
t=open(p,encoding='utf-8').read()
t=t.replace('He walked it north because honest ground asked no questions and led where he needed.',
 'He walked it north because honest ground asked no questions and led where he needed and the walking itself was the whole of the honest arithmetic of a life spent counting every rut and every stone and every field bird that rose ahead of him and settled again behind him in the grey light of an early autumn morning that asked nothing of him at all and gave nothing back.',1)
open(p,'w',encoding='utf-8').write(t)
PY
expect_fail "5. a 70-word sentence injected — over60 still bites" "sentence(s) over 60 words"
cp "$TMP/C06.keep" chapters/Chapter_06_The_Hem_Road.md

# ── 6. what ships is not what was gated (stale reader edition) ───────────
cp manuscript/Chapter_06_The_Hem_Road.md "$TMP/R06.keep"
printf '\nAn orphan line that the author edition never held.\n' >> manuscript/Chapter_06_The_Hem_Road.md
expect_fail "6. reader edition drifted from its author edition" "reader edition is not the author edition"
cp "$TMP/R06.keep" manuscript/Chapter_06_The_Hem_Road.md

# ── 7. absence of scope is a failure ─────────────────────────────────────
hide chapters; hide manuscript
expect_fail "7. nothing to read — the gate refuses to pass empty" "0 files found"
show chapters; show manuscript

printf '%s\n' "──────────────────────────────────────────────────────────────────────"
printf '  %d of %d fixtures behaved\n\n' "$pass" "$((pass+fail))"
[ "$fail" -eq 0 ] || { printf 'SCOPE FIXTURE FAILED — do not trust this gate.\n\n'; exit 1; }
printf 'SCOPE FIXTURE PASSED\n\n'
