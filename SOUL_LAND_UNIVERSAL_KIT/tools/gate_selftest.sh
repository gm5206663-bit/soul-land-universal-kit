#!/usr/bin/env bash
# SCOPE FIXTURE — prove the gate reacts to its inputs.
#
# THE SCOPE LAW: one defect — a check that reports success while covering less
# than it claims. A gate is only tested when it has been SEEN to fail on every
# way its scope can shrink. The gate's own --selftest proves the checks work on
# text; this fixture proves the gate notices when the TEXT IT POINTS AT changes
# underneath it. Both are needed. A gate that passes here but was never made to
# fail on a shrunk scope is exactly the storyos stage that reported
# "stage built: 57 files" while holding zero chapters.
#
# Usage:  tools/gate_selftest.sh [path-to-live_book_gate.py]
# Exit 0 = every perturbation was caught. Exit 1 = the gate missed one.

set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
GATE="${1:-$HERE/live_book_gate.py}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
BOOK="$TMP/book"
LOG="$TMP/gate.log"

pass=0; fail=0
say() { printf '  %-58s %s\n' "$1" "$2"; }

build_book() {
  rm -rf "$BOOK"
  mkdir -p "$BOOK/chapters" "$BOOK/manuscript" "$BOOK/foundation"
  cat > "$BOOK/chapters/Chapter_01.md" <<'EOF'
He counted the ruts in the road and said nothing to anyone that day.

"Sit," she said, and he sat. "Eat," she said, and he ate. "Now," she said, and he went.

That was the whole of the lesson, and he carried it east like a folded map.
EOF
  cp "$BOOK/chapters/Chapter_01.md" "$BOOK/manuscript/Chapter_01.md"
  printf 'GATE EXEMPTION: none — this fixture book carries no exemptions.\n' > "$BOOK/README.md"
}

run_gate() {                       # never through a pipe — capture the code
  python3 "$GATE" "$BOOK" > "$LOG" 2>&1
  echo $?
}

expect() {                         # expect <want-rc> <label>
  local want="$1" label="$2" rc
  rc=$(run_gate)
  if [ "$rc" = "$want" ]; then
    say "$label" "caught (exit $rc)"; pass=$((pass+1))
  else
    say "$label" "MISSED — exit $rc, wanted $want"; fail=$((fail+1))
    sed -n '1,12p' "$LOG" | sed 's/^/      | /'
  fi
}

echo "SCOPE FIXTURE — does the gate notice when its inputs change?"
echo "================================================================"

# 0. the clean book must PASS, or nothing below means anything
build_book; expect 0 "clean book passes"

# 1. what ships is not what was gated: the reader edition loses a chapter
rm "$BOOK/manuscript/Chapter_01.md"; expect 1 "reader edition missing a chapter"

# 2. the floor: speech is stripped from the live text
build_book
python3 - "$BOOK/chapters/Chapter_01.md" <<'EOF'
import sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read().replace('"', '')
open(p, 'w', encoding='utf-8').write(t)
EOF
cp "$BOOK/chapters/Chapter_01.md" "$BOOK/manuscript/Chapter_01.md"
expect 1 "live text loses its speech (dialogue floor)"

# 3. published without an author edition
build_book; rm "$BOOK/chapters/Chapter_01.md"
expect 1 "published chapter with no author edition"

# 4. a dead directory appears: the gate must gate the live one and say so
build_book
mkdir -p "$BOOK/chapters_old"
cp "$BOOK/chapters/Chapter_01.md" "$BOOK/chapters_old/Chapter_02.md"
printf 'chapters_old/ is superseded — do not use. The live text is chapters/.\n' >> "$BOOK/README.md"
expect 0 "dead directory beside the live one does not fail the book"
grep -q 'dead directory not gated' "$LOG" && { say "dead directory reported, not silently skipped" "reported"; pass=$((pass+1)); } \
  || { say "dead directory reported, not silently skipped" "NOT REPORTED"; fail=$((fail+1)); }

# 5. an exemption must cite a receipt that exists
build_book
printf 'GATE EXEMPTION: dialogue-floor — trust me (foundation/NOWHERE.md)\n' >> "$BOOK/README.md"
expect 1 "exemption citing a receipt that does not exist"

echo "================================================================"
printf 'SCOPE FIXTURE: %d caught, %d missed\n' "$pass" "$fail"
[ "$fail" -eq 0 ] || { echo "REFUSING TO REPORT SUCCESS — the gate is blind to a shrunk scope"; exit 1; }
echo "every way the scope can shrink was seen to fail"
