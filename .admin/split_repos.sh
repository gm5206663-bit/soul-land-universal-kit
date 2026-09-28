#!/usr/bin/env bash
# Split the published repo: fiction goes PRIVATE, the kit goes PUBLIC.
#
# Usage:
#   ./split_repos.sh <token>
#
# What it does, in order:
#   1. Makes gm5206663-bit/soul-land-projects PRIVATE  (removes fiction from public view)
#   2. Creates gm5206663-bit/soul-land-universal-kit  (PUBLIC, kit only)
#   3. Pushes the kit-only history to it
#
# The token is used inline and never written to any file or git config.
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <github-token>"
  exit 1
fi

TOKEN="$1"
OWNER="gm5206663-bit"
SRC="$OWNER/soul-land-projects"
KIT_REPO="$OWNER/soul-land-universal-kit"
AUTHOR_NAME="Gaurav Meena"
AUTHOR_EMAIL="309063472+gm5206663-bit@users.noreply.github.com"
API="https://api.github.com"

echo "==> 0. checking token"
LOGIN=$(curl -sS -H "Authorization: token $TOKEN" "$API/user" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('login',''))")
if [ -z "$LOGIN" ]; then
  echo "    token rejected — aborting, nothing changed"
  exit 1
fi
echo "    authenticated as: $LOGIN"

echo "==> 1. making $SRC PRIVATE (fiction leaves public view)"
curl -sS -X PATCH -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" \
  "$API/repos/$SRC" -d '{"private":true}' -o /tmp/patch.json -w "    HTTP %{http_code}\n"
python3 -c "
import json; d=json.load(open('/tmp/patch.json'))
print('    now:', 'PRIVATE' if d.get('private') else 'STILL PUBLIC — check manually')
"

echo "==> 2. building kit-only history"
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
cp -r /home/user/SOUL_LAND_UNIVERSAL_KIT/. "$WORK/"
cp /home/user/.gitignore "$WORK/"
rm -rf "$WORK/tools/__pycache__"
cd "$WORK"
git init -q -b main
git config user.name  "$AUTHOR_NAME"
git config user.email "$AUTHOR_EMAIL"
git add -A
git commit -q -F - <<'MSG'
Soul Land Universal Kit — portable authoring foundation

A complete, era-agnostic authoring kit for Soul Land (Douluo Dalu) fan fiction.
Drop it into a new project and follow it. Contains no premise, protagonist, or plot.

  11 law files (00-10)   world canon, story law, prose law, continuity, audit
  13 templates           copy into your project, destination-tagged
  tools/verify.py        7 hard gates
  tools/selftest.py      proves the gate has teeth

Distilled from four working serials, including one 90,000-word draft that was
written and rejected for five diagnosable reasons. Each of those five failure
modes is now made structurally impossible by a rule and a machine check.

Start at 00_START_HERE.md.

Derivative fan work. Soul Land belongs to Tang Jia San Shao.
MSG
echo "    built: $(git ls-files | wc -l) files, 1 commit"

echo "==> 3. creating $KIT_REPO (public)"
curl -sS -X POST -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" \
  "$API/user/repos" \
  -d "{\"name\":\"soul-land-universal-kit\",\"description\":\"Portable authoring kit for Soul Land (Douluo Dalu) fan fiction — canon spine, story law, prose law, audit gates, templates, and a self-testing verification script\",\"private\":false,\"has_issues\":true,\"has_wiki\":false}" \
  -o /tmp/new.json -w "    HTTP %{http_code}\n"
python3 -c "
import json; d=json.load(open('/tmp/new.json'))
print('    created:', d.get('full_name', d.get('message','FAILED')))
"

echo "==> 4. pushing kit"
GIT_TERMINAL_PROMPT=0 git push \
  "https://x-access-token:${TOKEN}@github.com/${KIT_REPO}.git" HEAD:refs/heads/main 2>&1 | sed 's/^/    /'

rm -f /tmp/patch.json /tmp/new.json
echo
echo "==> done"
echo "    kit     (public) : https://github.com/$KIT_REPO"
echo "    fiction (private): https://github.com/$SRC"
echo
echo "    Revoke this token now: https://github.com/settings/tokens"
