#!/usr/bin/env bash
# Restore the approved private GitHub origin when this sandbox's transient .git/config is reset.
set -euo pipefail

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
REMOTE_URL="https://github.com/gm5206663-bit/fire-phoenix-workshop.git"

cd "$ROOT"
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

echo "origin configured as: $(git remote get-url origin)"
echo "This command configures a remote only; it does not push."
