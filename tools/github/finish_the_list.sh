#!/usr/bin/env bash
# FINISH THE LIST — every account operation the Arena GitHub App cannot do.
#
# WHY THIS EXISTS
#   The connected GitHub App can read everything and write code, issues (create
#   only), labels, milestones and releases *in this repository*. It cannot:
#     · edit, label, close or delete an issue      -> 403
#     · change repository settings                 -> 403
#     · change GitHub Pages configuration          -> 403
#     · create releases on any other repository    -> 403
#     · push anything under .github/workflows/     -> refused (no `workflows`)
#   Those five walls block four items on the 2026-10-30 audit. This script does
#   them in one pass, with a credential that has the scopes to.
#
# WHAT IT DOES — idempotent, safe to re-run
#   1. deletes the two junk issues (#6, #7)
#   2. turns on "automatically delete head branches" in the kit
#   3. points storyos-site's Pages at main:/published-site (kills the stale site)
#   4. labels, milestones and assigns issues #8-#12 and #2-#4
#   5. cuts the releases the account is behind on
#   6. installs tools/ci/kit-self-check.draft.yml into .github/workflows/
#
# HOW TO RUN
#   Requires the GitHub CLI (https://cli.github.com) and a token with
#   `repo`, `admin:repo_hook`, `workflow` — i.e. a classic PAT or `gh auth login`.
#
#       gh auth login                       # one time, in a terminal
#       bash tools/github/finish_the_list.sh --dry-run
#       bash tools/github/finish_the_list.sh
#
#   Nothing here is destructive except step 1, which deletes two issues that are
#   known junk (a half-written duplicate and a permission probe).

set -uo pipefail

OWNER=gm5206663-bit
KIT=$OWNER/soul-land-universal-kit
MILESTONE='The desk — every decision awaiting the author'
DRY=0
[[ ${1:-} == --dry-run ]] && DRY=1

done_count=0; skipped=0; failed=0
say()   { printf '  %s\n' "$*"; }
head2() { printf '\n\033[1m%s\033[0m\n' "$*"; }
run() {  # run "<description>" <command...>
  local label=$1; shift
  if (( DRY )); then say "would: $label"; ((skipped++)); return 0; fi
  if out=$("$@" 2>&1); then say "done: $label"; ((done_count++)); return 0
  else say "FAILED: $label"; printf '        %s\n' "${out%%$'\n'*}"; ((failed++)); return 1; fi
}

head2 "Preflight"
if ! command -v gh >/dev/null; then
  echo "gh is not installed. Install it: https://cli.github.com" >&2; exit 2
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "Not signed in. Run: gh auth login" >&2; exit 2
fi
say "$(gh api user --jq .login) — $(gh auth status 2>&1 | grep -o 'Token scopes:.*' || echo 'app token')"

head2 "1 · Delete the two junk issues (#6 duplicate, #7 probe)"
for n in 6 7; do
  title=$(gh api "repos/$KIT/issues/$n" --jq .title 2>/dev/null) || { say "#$n already gone"; ((skipped++)); continue; }
  run "delete #$n — ${title:0:60}" gh api -X DELETE "repos/$KIT/issues/$n"
done

head2 "2 · Automatically delete head branches after merge"
run "delete_branch_on_merge on $KIT" \
  gh api -X PATCH "repos/$KIT" -F delete_branch_on_merge=true --jq '.delete_branch_on_merge'

head2 "3 · storyos-site Pages: gh-pages -> main:/published-site"
current=$(gh api "repos/$OWNER/storyos-site/pages" --jq '.source.branch + ":" + (.source.path // "/")' 2>/dev/null || echo 'none')
say "currently: $current"
if [[ $current == 'main:/published-site' ]]; then
  say 'already correct'; ((skipped++))
else
  run 'repoint Pages at main:/published-site' \
    gh api -X PUT "repos/$OWNER/storyos-site/pages" \
      --input - <<< '{"source":{"branch":"main","path":"/published-site"}}'
  say 'NOTE: verify main:published-site is current before publishing —'
  say '      its own last commit is 2026-10-12 (867b03c).'
fi

head2 "4 · Labels, milestone and assignee on the open issues"
ms=$(gh api "repos/$KIT/milestones" --jq ".[] | select(.title==\"$MILESTONE\") | .number" 2>/dev/null | head -1)
if [[ -z $ms ]]; then
  run 'create the milestone' gh api "repos/$KIT/milestones" \
    -f title="$MILESTONE" -f state=open -f due_on='2026-11-30T00:00:00Z' \
    -f description='Every decision awaiting the author. An agent may prepare, never rule.'
  ms=$(gh api "repos/$KIT/milestones" --jq ".[] | select(.title==\"$MILESTONE\") | .number" | head -1)
fi
say "milestone number: ${ms:-none}"
for n in 2 3 4 8 9 10 11 12; do
  gh api "repos/$KIT/issues/$n" >/dev/null 2>&1 || { say "#$n missing"; ((skipped++)); continue; }
  run "#$n -> milestone + assignee + author-gated" \
    gh api -X PATCH "repos/$KIT/issues/$n" \
      -F "milestone=$ms" -f "assignees[]=$OWNER" \
      -f "labels[]=author-gated" --jq '.number'
done

head2 "5 · Releases the account is behind on"
cut_release () {  # cut_release <repo> <tag> <name> <body>
  local repo=$1 tag=$2 name=$3 body=$4
  local sha; sha=$(gh api "repos/$repo/commits/main" --jq .sha)
  if gh api "repos/$repo/releases/tags/$tag" >/dev/null 2>&1; then
    say "$repo: $tag already exists"; ((skipped++)); return 0
  fi
  run "$repo -> $tag" gh api "repos/$repo/releases" -X POST \
    -f tag_name="$tag" -f target_commitish="$sha" -f name="$name" -f body="$body" --jq '.tag_name'
}

cut_release $OWNER/soul-library v2.2-2026-10-30 \
  'Soul Library — 2026-10-30' \
  'The reading shelf at its 2026-10-24 head: 312 chapters across 18 serials, full-text search, zero tracking, sentinel 26/26.'

cut_release $OWNER/stark_heir stark-heir-ch5-2026-10-30 \
  'Stark Heir — Chapters 1–5 gated' \
  'The MCU Stark Heir serial at its 2026-10-24 head: five chapters shipped and gated, canon running fully on-page in film order (IM1 beats 1–12 staged), cast web and chapter index filed.'

cut_release $OWNER/mcu_eternal_fanfic eternals-ch3-paused-2026-10-30 \
  'The Eternals — Chapter 3, paused at the edge' \
  'Chapter 3 shipped and gated; the serial is PAUSED at the edge by author order, files intact. Released as a dated record of the edge, not a finished book.'

cut_release $OWNER/adaptation-talent adaptation-talent-v2.0-2026-10-30 \
  'Adaptation Talent — v2.0, 17 holders across 5 worlds' \
  'Universal law v2.0 locked: 57 files, 180 links, a module for every holder, full provenance with MANIFEST.sha256.'

head2 "6 · Install the kit's CI"
if [[ -f .github/workflows/kit-self-check.yml ]]; then
  say 'already installed'; ((skipped++))
elif [[ -f tools/ci/kit-self-check.draft.yml ]]; then
  if (( DRY )); then say 'would: copy tools/ci/kit-self-check.draft.yml -> .github/workflows/'; ((skipped++))
  else
    mkdir -p .github/workflows
    cp tools/ci/kit-self-check.draft.yml .github/workflows/kit-self-check.yml
    git add .github/workflows/kit-self-check.yml
    git -c user.name=Sara -c user.email=sara@local commit -q \
      -m "ci: install kit-self-check — the gate now runs on every push to the spine"
    say 'committed — push this branch to arm it'
    ((done_count++))
  fi
else
  say 'draft missing'; ((failed++))
fi

head2 "Result"
printf '  %d done · %d already-correct · %d failed\n' "$done_count" "$skipped" "$failed"
(( DRY )) && echo '  (dry run — nothing was changed)'
(( failed )) && exit 1
exit 0
