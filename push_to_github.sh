#!/usr/bin/env bash
# Push this repo to GitHub and stamp the commits with the real author.
#
# Usage:
#   ./push_to_github.sh <github-username> <repo-name> <author-name> <author-email> <token>
#
# The token is used inline and is never written to .git/config or any file.
set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "usage: $0 <github-username> <repo-name> <author-name> <author-email> <token>"
  exit 1
fi

USER="$1"; REPO="$2"; ANAME="$3"; AEMAIL="$4"; TOKEN="$5"
cd "$(dirname "$0")"

echo "==> stamping commits as: $ANAME <$AEMAIL>"
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch -f --env-filter "
  export GIT_AUTHOR_NAME='$ANAME'
  export GIT_AUTHOR_EMAIL='$AEMAIL'
  export GIT_COMMITTER_NAME='$ANAME'
  export GIT_COMMITTER_EMAIL='$AEMAIL'
" -- --all >/dev/null

git config user.name  "$ANAME"
git config user.email "$AEMAIL"

echo "==> authors now:"
git log --format='    %h  %an <%ae>'

echo "==> pushing to github.com/$USER/$REPO (token used inline, not stored)"
# x-access-token is the conventional username for PAT auth. The credential is
# passed in the URL for this one command and is not saved to any config.
GIT_TERMINAL_PROMPT=0 git push \
  "https://x-access-token:${TOKEN}@github.com/${USER}/${REPO}.git" \
  HEAD:refs/heads/main

echo
echo "==> done: https://github.com/${USER}/${REPO}"
echo "    Revoke the token now: GitHub > Settings > Developer settings > Tokens"
