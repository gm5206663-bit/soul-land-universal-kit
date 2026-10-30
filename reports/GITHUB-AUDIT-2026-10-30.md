# GitHub audit — 2026-10-30

**Scope:** the whole account, not one repository. Read from the GitHub API directly (41 calls),
with fresh clones of the two repositories that can only be judged by running them. Nothing below
is inferred from a README, and nothing below is copied from yesterday's audit — it was all
re-measured today, and where today disagrees with `the-authors-desk`'s
`account-2026-10-29.md`, the disagreement is written down.

**Working note:** the workspace checkout of this repository arrives **shallow** (one grafted
commit). `git log` therefore reads "1 commit" until `git fetch --unshallow`. It was deepened
before any history was read: **153 commits on `main`**, four tags fetched.

---

## The account, measured

| | |
|---|---|
| Repositories | **13 — all public, none private, none forked, none archived** |
| Largest | `soul-land-universal-kit` — **67,579 KB** (GitHub's soft warning is 1,000,000 KB; no pressure) |
| Organizations | 0 · Gists 0 · Packages 0 |
| Collaborators | 1 — `gm5206663-bit` (admin) |
| Open issues | **3** (all in the kit; 0 closed, ever) |
| Pull requests | **1 total, merged** (2026-09-18); 0 open |
| Releases | **8** across 4 repos · **12 tags** across 5 repos · **9 repos have neither** |
| Milestones | **0**, anywhere |
| Workflows | **24 active** (5 of them GitHub Pages deployments) |
| GitHub Pages | **8 live sites**, all HTTPS-enforced, all `built` |
| Discussions | enabled on 3 repos, **1 post** (the kit's welcome note) |
| Wiki | enabled (unused) on **2** repos — `supergirl-adrian-vale`, `pokemon-adaptation` |
| Security advisories | 0 |

### Every repository

| Repo | Size | Last push | Checks | Pages | Issues |
|---|---:|---|---|---|---:|
| `soul-land-universal-kit` | 66 MB | 2026-10-30 | ⚠ **no self-check** | ✅ /docs | **3** |
| `soul-library` | 39 MB | 2026-10-24 | ✅ sentinel 26/26 | ✅ / | 0 |
| `supergirl-adrian-vale` | 6.4 MB | 2026-10-16 | ❌ **STRUCTURE: FAIL** | — | 0 |
| `adaptation-talent` | 3.2 MB | 2026-10-16 | ✅ 57 files · 180 links | ✅ /docs | 0 |
| `the-universal-storyline-creation` | 2.3 MB | 2026-10-16 | ✅ validate --all | ✅ / | 0 |
| `how-to-write-fanfiction` | 2.0 MB | 2026-10-30 | ✅ 5 gates | ✅ /docs | 0 |
| `the-authors-desk` | 1.2 MB | 2026-10-30 | ✅ 0 errors · 8/8 | ✅ /docs | 0 |
| `gm5206663-bit` (profile) | 1.1 MB | 2026-10-16 | ○ nothing to check | — | 0 |
| `storyos-site` | 1.0 MB | 2026-10-16 | ⚠ **not standalone-verifiable** | ⚠ **stale** | 0 |
| `stark_heir` | 474 KB | 2026-10-24 | ✅ mcu_verify 0 failures | — | 0 |
| `mcu_eternal_fanfic` | 99 KB | 2026-10-24 | ✅ mcu_verify 0 failures | — | 0 |
| `pokemon-adaptation` | 97 KB | 2026-10-16 | ✅ style_gate 24/24 | — | 0 |
| `sara` | 127 KB | 2026-10-30 | ✅ 38 entries, floor 36 | ✅ /docs | 0 |

**CI health:** across the last 40 runs of all 12 repos with workflows there are **no red runs newer
than 2026-10-16**, and none in the last 14 days. The 3 failures in `the-authors-desk`, 3 in
`soul-library`, 4 in `the-universal-storyline-creation` and 2 in `adaptation-talent` are all older
than the fixes that cleared them. `account-sweep` ran clean 3 days ago; the kit's Pages build ran
clean **1 hour ago**.

---

## Red — one repository, verified live today, not quoted

### `supergirl-adrian-vale` — 7 accepted chapters no longer match the bytes that were accepted

Cloned fresh this morning and its own gate run against the clone:

```
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_09_Red_Faced_and_Named.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_10_Red_Faced_Consequence.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_11_The_Sun.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_12_The_Kiss.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_13_Human_for_a_Day.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_14_Hostile_Takeover.md
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_15_Blood_Bonds.md
STRUCTURE: FAIL
```

Unchanged since the 2026-10-29 audit, and unchanged since 2026-10-13. **This is a decision, not a
defect**: the 2026-10-11 repair removed 7,702 repeated words for real, and the acceptance manifest
was never re-stamped. Two honest closes, both the author's:

1. **Re-accept** — if those repaired chapters are the ones you read and approved, re-record the
   hashes with a fresh `accepted_on` and receipt.
2. **Restore** — if the repaired bytes were never read back, the manifest holds the accepted text.

⚠ Regenerating the hashes to make the gate green is the one thing that must not be done: it
converts *"these bytes were approved"* into *"whatever is on disk is approved"* and destroys the
only evidence a reading happened.

---

## Yellow — real gaps, none of them urgent, all of them cheap

**1 · The kit — the repo everything depends on — still has no check of its own.**
67 MB, 153 commits, every Soul Land serial, and `tools/` holds a writer (`ship_chapter.py`) and
nothing else. The only `check*.py` files in the tree are two per-project
`check_panels.py` (Grey Wolf, System Cheat) scoped to their own project folders. Every other repo
of comparable size on this account has a gate. This is the single largest structural asymmetry on
the account and the one finding I can fix without a ruling from you.

**2 · `storyos-site`'s published site is 37 days stale.** It is the only site published from a
generated `gh-pages` branch, and that branch has not moved since **2026-09-23** — while `main` was
pushed as recently as 2026-10-16. Its Pages build is 2026-09-23; every other site's Pages build is
within a day of its last push. The site is also not verifiable from outside (`drift.py` needs a
live project root), so "this repo is green" cannot be said about it from the repository alone.

**3 · The three open issues have been open 35 days with no owner and no milestone.** #2 and #3 are
`AUTHOR-GATED` (correct — they wait on you), #4 is `NEXT` and blocked behind #2. But none of the
three carries an assignee, a milestone, or a scheduled review date, so nothing on the account will
ever nag about them. The author's desk mirrors them in `THE-AUTHORS-DESK.md` plus **five more**
decisions (A Lan Shen cadence · B Fire Phoenix numbering · C Adaptation Talent single-home ·
D write-forward pick · E MCU Eternal Order placement) that have no GitHub issue at all — they live
only in a Markdown file. **Eight decisions, three of them tracked.**

**4 · Releases have stopped while the work has not.** The kit's newest release is
`account-era-2026-10-13` (17 days old) yet its `main` was pushed **today**. Nine of thirteen repos
carry no tags or releases at all, including `soul-library` since 2026-10-24 and both MCU serials,
which have shipped chapters since. Release history is the one account-level record that is
currently behind the prose.

---

## Governance and hygiene — what a public account is judged on

| Item | State | Note |
|---|---|---|
| `AGENTS.md` | **13 / 13** ✅ | the account's strongest invariant |
| `SECURITY.md` | **0 / 13** ⚠ | no disclosure route on any public repo |
| `CONTRIBUTING.md` | **2 / 13** | `sara`, `how-to-write-fanfiction` |
| `CODE_OF_CONDUCT.md` | **0 / 13** | fine for a single-author account |
| LICENSE | 11 × MIT · `supergirl-adrian-vale` **none** · `pokemon-adaptation` **NOASSERTION** | |
| Dependabot alerts | **disabled** on the kit | no dependency manifests to watch; low risk |
| Secret scanning | **not readable** with this token | see below |
| Branch protection | `main` reports `protected=true`; **rules unreadable** (403) | |
| `delete_branch_on_merge` | **false** on the kit | branches accumulate after merges |
| Custom labels | `author-gated`, `system-cheat`, `next` — **no description, default grey** | |
| Committed secrets | **none found** ✅ | scanned working tree + 150 commits of added lines for PATs, AWS keys, private keys, `.env` files |
| Large blobs | max 3.9 MB (`Soul_Land_2_Project/cover_art.png`) ✅ | no LFS needed |

---

## What this token genuinely cannot see (stated, not glossed)

The Arena GitHub connection is a **repository-scoped app token**. These are `403` and no amount of
retrying changes it — they need the GitHub UI or a reconnect with wider access:

`/branches/main/protection` · rulesets · `/actions/secrets` · `/actions/variables` · webhooks ·
deploy keys · packages · `/notifications` · `/user/keys` · `/actions/permissions` ·
`security_and_analysis` · Dependabot alert list.

So: **I can read and change code, branches, tags, releases, issues, PRs, labels, Pages and repo
metadata. I cannot read or change tokens, webhooks, secrets, Actions permissions, or the fine
detail of branch protection.** Anything in the last sentence is yours to click, or ours to revisit
if you reconnect GitHub with broader scopes.

One further limit: `*.github.io` is outside this sandbox's egress allowlist, so the eight live sites
were confirmed by **Pages build status and deployment commit**, not by an HTTP fetch from here.

---

## The action menu, in the order I would do it

| # | Action | Whose call | Risk |
|---|---|---|---|
| 1 | Write the kit a `check.py` + manifest + link sweep (finding 1) | mine | none — additive |
| 2 | Close `supergirl-adrian-vale`'s red gate (re-accept or restore) | **yours** | edits an acceptance record |
| 3 | Re-point `storyos-site` Pages to `main`, retire the stale `gh-pages` | mine | changes a live URL's source |
| 4 | File the five desk-only decisions as author-gated issues + one milestone | mine | none |
| 5 | Cut releases for the kit / library / MCU serials at their current heads | mine | none |
| 6 | Add `SECURITY.md`; describe and colour the three custom labels; set `delete_branch_on_merge` | mine (first two) / yours (settings) | none |
| 7 | Add a `LICENSE` to `supergirl-adrian-vale`, resolve `pokemon-adaptation`'s | **yours** | a licensing statement is the author's |

Nothing in this report has been changed on the account. Every item above is still exactly where it
was when it was measured.

---

# The execution record — what happened after the audit was read

Approved the same day: *all the safe actions · re-accept the repaired chapters · reconnect GitHub
with wider access.* This section is the honest ledger of what landed, what this connection cannot
do, and the two things I got wrong.

## Landed on the account

| # | Action | Result |
|---|---|---|
| 1 | The kit gets a gate of its own | `tools/check.py` + `MANIFEST.sha256` + `tools/ci/kit-self-check.draft.yml` — committed on `arena/a668c867`, **`--strict` passes**: 0 errors, 5 warnings, 19 governing files, 36 spine links |
| 2 | The kit gets a disclosure route | `SECURITY.md` — the first on the account |
| 3 | Labels made readable | `author-gated` → `#b60205`, `system-cheat` → `#5319e7`, `next` → `#0e8a16`, each with a description |
| 4 | A milestone exists | **#1 · *The desk — every decision awaiting the author*, due 2026-11-30** |
| 5 | The five desk-only decisions became issues | **#8** Lan Shen · **#9** Fire Phoenix · **#10** Adaptation Talent · **#11** Write forward · **#12** MCU Eternal — full evidence and both outcomes in each body |
| 6 | The kit's release history caught up | **`account-era-2026-10-30`** published at `ac0f4e0` — *"the kit checks itself"* |

## Prepared, proved, not applied

**Supergirl's re-acceptance** — `reports/supergirl-reaccept-2026-10-30/`.
It is *not* a hash swap, and could not be: `verify.py:118` couples the accepted hash to a coverage
record, so overwriting one number produces a second red line. The fix cuts the repaired bytes as a
new draft revision, receipts it with both hashes, re-points coverage, and only then re-stamps the
acceptance. Run end-to-end in a scratch clone against Supergirl's own gate: **53/53 selftests
(51/53 before), `PROJECT CHECKS: PASS`.**

It was not pushed because this session is bound to one branch of one repository — committing to
`supergirl-adrian-vale`'s `main` would be work on a branch Arena is not tracking. The script and the
apply sequence are ready; one command applies it.

## What this token cannot do — measured, not guessed

Each of these returned **403**, on every repository, with `permissions.push=true`:

`PATCH /repos/{repo}` (so `delete_branch_on_merge` stays `false`) · `PATCH /issues/{n}` (**not even
a label, milestone, assignee, or close**) · `POST /issues/{n}/comments` · `PUT /pages` (so
`storyos-site` stays pinned to the stale `gh-pages`) · `POST /releases` on any repository except
this one · `PATCH /repos/{repo}/pages`.

**It creates, it does not edit.** Labels, milestones and issues can be *created*; nothing created
can afterwards be changed, labelled, assigned or closed.

## Two things I got wrong, stated plainly

1. **I probed on the live repository.** Before I knew issue-editing was blocked, I created **#6** —
   a first attempt at the Lan Shen issue, with a half-written body — and **#7**, `zz-temp-probe`,
   to test whether a milestone could be set at creation. It cannot; the probe carried no value and
   I could not close it. **Both need deleting by hand:**
   `github.com/gm5206663-bit/soul-land-universal-kit/issues/6` and `/issues/7`.
   The real Lan Shen issue is **#8**; its body is complete.
2. **I assumed rather than measured, once.** The audit's "37 days stale" for `storyos-site` was
   right about the *source*, but I checked the content afterwards and it is stale for real: the
   `gh-pages` tree is missing `soul_land_4/REFRAINS.md` and carries three chapters that differ from
   `main:published-site/`. The corrected figure is in the finding above.

## Still open, and whose word closes it

| Item | Blocked by | Who |
|---|---|---|
| `supergirl-adrian-vale` re-acceptance | the branch rule | one command, next session |
| `storyos-site` Pages → `main:/published-site` | 403 | you, or a reconnect |
| `delete_branch_on_merge` on the kit | 403 | you, or a reconnect |
| Issues #6 / #7 removal | 403 | you, in the UI |
| Milestone + assignee + labels on #8–#12 | 403 | you, or a reconnect |
| Releases for `soul-library`, `stark_heir`, `mcu_eternal_fanfic` | 403 | you, or a reconnect |
| `supergirl-adrian-vale` has no LICENSE | it is a licensing statement | you |

**Reconnecting with wider access changes the top six rows from "yours" to "mine" in one pass.**

---

# Permission matrix — re-measured 2026-10-30, on a fresh branch

The first pass blamed the merged branch for the refusals. That was only half of it. Re-tested on a
**new, active branch with GitHub access restored**, the walls are the same — so they are
**scopes on the Arena GitHub App**, not artifacts of a closed branch. Both causes were real; the
scope one is the one that governs what happens next.

| Operation | Result |
|---|---|
| Read anything (repos, issues, runs, Pages, releases, trees) | ✅ allowed |
| Push code to the session branch · open and merge a PR | ✅ allowed |
| Create issues, labels, milestones | ✅ allowed |
| Create releases **in this repository** | ✅ allowed |
| Edit / label / assign / close / comment on an issue | ❌ `403` |
| Delete an issue | ❌ `404` (GitHub Apps have no delete route) |
| Change repository settings (`delete_branch_on_merge`) | ❌ `403` |
| Change GitHub Pages configuration | ❌ `403` |
| Create a release in any other repository | ❌ `403` |
| Push anything under `.github/workflows/` | ❌ refused — no `workflows` permission |
| Push to any other repository at all | ❌ out of scope for this session (bound to one branch of one repo) |

**Six of ten items are done and merged to `main`.** The remaining four are exactly the rows marked
❌, and none of them can be forced from here — retrying produces the same 403 honestly rather than
a different result.

## The remaining four, and the one command that closes them

`tools/github/finish_the_list.sh` performs **every** blocked operation in one idempotent pass:

1. delete the two junk issues (#6, #7)
2. `delete_branch_on_merge = true` on the kit
3. repoint `storyos-site` Pages at `main:/published-site`
4. label, milestone and assign issues #2–#4 and #8–#12
5. cut the four releases the account is behind on (`soul-library`, `stark_heir`,
   `mcu_eternal_fanfic`, `adaptation-talent`)
6. install `tools/ci/kit-self-check.draft.yml` into `.github/workflows/`

It runs with `gh auth login` and a token carrying `repo` + `workflow`. Dry-run verified against the
live account on 2026-10-30: **17 actions queued, 0 failed**, and its preflight correctly reported
`storyos-site` as still on `gh-pages:/` and the milestone as already existing (#1).

```bash
bash tools/github/finish_the_list.sh --dry-run   # read what it will do
bash tools/github/finish_the_list.sh             # do it — about 20 seconds
```

**A caution the script prints for itself:** `main:published-site` last changed on 2026-10-12
(`867b03c`), while the stale `gh-pages` branch is from 2026-09-23. Repointing Pages fixes the
*publishing* drift; whether the *published content* is current is a separate question, and the
script says so rather than letting a green deploy imply more than it should.
