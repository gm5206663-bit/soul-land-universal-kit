#!/usr/bin/env bash
# Create and verify a dated, local-only Git bundle backup. Invoke with: bash tools/create_git_bundle_backup.sh [output-dir]
set -euo pipefail

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
OUTPUT_DIR=${1:-"$ROOT/backups"}
STAMP=$(date +%Y%m%d-%H%M%S)
BUNDLE="$OUTPUT_DIR/fire-phoenix-$STAMP.bundle"

mkdir -p "$OUTPUT_DIR"
cd "$ROOT"
git diff --exit-code
git status --porcelain --untracked-files=all | grep -q . && {
  echo "Refusing backup: tracked or untracked working-tree changes exist." >&2
  exit 1
} || true

git bundle create "$BUNDLE" --all
git bundle verify "$BUNDLE"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$BUNDLE" > "$BUNDLE.sha256"
fi

echo "Verified Git bundle: $BUNDLE"
echo "This bundle excludes ignored local-only quarantine files by design."
