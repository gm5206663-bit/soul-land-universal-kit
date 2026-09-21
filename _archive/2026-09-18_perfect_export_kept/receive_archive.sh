#!/usr/bin/env bash
# receive_archive.sh — find the handoff archive in uploads/ no matter what it
# was renamed to, verify it, unzip it, and (optionally) run the restore gate.
#
# Accepts:
#   1. A raw zip with ANY name/extension (detected by PK magic bytes), e.g.
#      handoff.md  (the user renamed .zip -> .md to beat an upload filter)
#   2. Base64 text of the zip, single file or split chunks named
#      handoff_b64.txt / handoff_b64_01.txt ... (bulletproof vs text transport)
set -u
UP=/home/user/uploads
ROOT=/home/user
ZIP_DST=$ROOT/Soul_Land_3_Project_handoff_2026-09-03.zip

echo "=== scanning $UP for archive material ==="
found=""

# --- route 1: raw zip by magic bytes (PK\x03\x04) -------------------------
while IFS= read -r -d '' f; do
  sig=$(head -c4 "$f" | od -An -tx1 | tr -d ' \n')
  if [ "$sig" = "504b0304" ]; then
    echo "RAW ZIP detected (PK magic): $f ($(du -h "$f" | cut -f1))"
    found="$f"
  fi
done < <(find "$UP" -maxdepth 1 -type f -size +1k ! -name 'HANDOFF.md' -print0)

# --- route 2: base64 text chunk(s) ----------------------------------------
mapfile -t b64 < <(find "$UP" -maxdepth 1 -type f \( -iname '*b64*' -o -iname '*handoff*.txt' -o -iname '*handoff*.md' \) ! -name 'HANDOFF.md' -size +50k 2>/dev/null | sort)
if [ -z "$found" ] && [ "${#b64[@]}" -gt 0 ]; then
  echo "BASE64 candidate(s):"
  printf '  %s\n' "${b64[@]}"
  cat "${b64[@]}" | tr -d '\r\n ' > /tmp/archive.b64
  echo "decoding $(wc -c < /tmp/archive.b64) bytes of base64 ..."
  if base64 -d /tmp/archive.b64 > "$ZIP_DST" 2>/dev/null; then
    found="$ZIP_DST"
    echo "decoded -> $ZIP_DST"
  else
    echo "!! base64 decode FAILED — chunks may be incomplete or corrupted"
  fi
fi

if [ -z "$found" ]; then
  echo "NO ARCHIVE FOUND YET. Expected: a renamed zip (PK magic) or base64 chunk(s)."
  echo "Files currently in uploads:"
  ls -la "$UP"
  exit 2
fi

# --- stage the raw zip (route 1 may point into uploads/) ------------------
if [ "$found" != "$ZIP_DST" ]; then
  cp "$found" "$ZIP_DST"
fi

echo; echo "=== integrity test (unzip -t) ==="
if ! unzip -t "$ZIP_DST" > /tmp/unztest.log 2>&1; then
  echo "!! ZIP FAILED INTEGRITY TEST — tail of log:"
  tail -5 /tmp/unztest.log
  exit 3
fi
tail -1 /tmp/unztest.log
echo "zip entries: $(unzip -l "$ZIP_DST" | tail -1 | awk '{print $2}')"

echo; echo "=== extracting into $ROOT ==="
unzip -o "$ZIP_DST" -d "$ROOT" > /tmp/unz.log && tail -3 /tmp/unz.log

echo; echo "=== restore protocol ==="
cd "$ROOT/Soul_Land_3_Project" || { echo "!! Soul_Land_3_Project/ not found after extract"; exit 4; }
echo "--- chapters on disk: $(ls chapters/chapter_*.md 2>/dev/null | wc -l)"
echo "--- canon extracts: $(ls canon_extract/chapters/canon_*.txt 2>/dev/null | wc -l)"
echo "--- checks present: $(ls checks/*.py checks/*.sh 2>/dev/null | wc -l) script files"
echo; echo "--- python3 checks/state.py ---"
python3 checks/state.py || { echo "!! state.py failed"; exit 5; }
echo; echo "--- sh checks/run_all.sh (THE gate) ---"
sh checks/run_all.sh
rc=$?
echo; echo "run_all.sh exit code: $rc"
exit $rc
