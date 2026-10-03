#!/bin/sh
# push_kit.sh — upload this whole workspace (the kit repo) to GitHub.
#
#   usage:  tools/push_kit.sh <FRESH_PAT>
#
# The token is used for this one command only and is never stored in any file.
# Make a fine-grained token for gm5206663-bit/soul-land-universal-kit
# with permission  Contents: Read and write,  push, then REVOKE it.
set -e
TOKEN="$1"
[ -n "$TOKEN" ] || { echo "usage: $0 <fresh-token>"; exit 1; }
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
git -C "$ROOT" push "https://x-access-token:${TOKEN}@github.com/gm5206663-bit/soul-land-universal-kit.git" HEAD:main
