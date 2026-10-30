# The list, in the browser — no terminal, no token

Everything below is clicks. Do **①** for certain; **②–⑤** are tidy-ups you can do any time or not at all.

Repo for ①–③: `github.com/gm5206663-bit/soul-land-universal-kit`

---

## ① Delete the two junk issues — 4 clicks, the only real trash

These are mine, not yours: one is a half-written duplicate, one is a permission probe.

For **each** of `issues/6` and `issues/7`:

1. Open the issue
2. Top-right, next to the issue title → click **`•••`**
3. Choose **Delete issue** → confirm

The real Lan Shen issue is **#8** — complete, with full evidence. Don't delete that one.

---

## ② Stop old branches piling up — 1 click

1. Repo → **Settings** (top bar, right of "Insights")
2. Left sidebar → **General**
3. Scroll to **Pull Requests**
4. Tick **Automatically delete head branches**

---

## ③ Fix the stale published site — 3 clicks

`storyos-site` currently publishes from an old `gh-pages` branch last touched 2026-09-23, while the real content sits on `main`.

1. Repo → `github.com/gm5206663-bit/storyos-site/settings/pages`
2. **Build and deployment → Source** → dropdown → **Deploy from a branch**
3. Branch: **`main`** · folder: **`/published-site`** → **Save**

Pages rebuilds in about a minute at `gm5206663-bit.github.io/storyos-site/`.

⚠ The content on `main` last changed 2026-10-12 — newer than what is published, but not current either. This fixes *where* it publishes from, not *how fresh* it is.

---

## ④ Install the kit's self-check — 5 clicks, all copy-paste

The repo has the CI file ready at `tools/ci/kit-self-check.draft.yml`, but my connection isn't allowed to push files into `.github/workflows/`.

1. Open `github.com/gm5206663-bit/soul-land-universal-kit/blob/main/tools/ci/kit-self-check.draft.yml`
2. Click **Raw** → select all → **copy**
3. Go to `github.com/gm5206663-bit/soul-land-universal-kit/tree/main/.github/workflows`
4. **Add file** → **Create new file**
5. Name it exactly `kit-self-check.yml`
6. Paste into the big text box → scroll down → **Commit changes** → confirm

From then on every push to the kit's governing files runs the gate.

---

## ⑤ Releases — optional, only if you want the history tidy

Your work is ahead of its release history in four repos. To cut one:

1. Open the repo → right sidebar **Releases** → **Draft a new release**
2. **Choose a tag** → type the tag name below → **Create new tag on publish**, target **main**
3. Title + description → **Publish release**

| Repo | Suggested tag | Title |
|---|---|---|
| `soul-library` | `v2.2-2026-10-30` | Soul Library — 2026-10-30 |
| `stark_heir` | `stark-heir-ch5-2026-10-30` | Stark Heir — Chapters 1–5 gated |
| `mcu_eternal_fanfic` | `eternals-ch3-paused-2026-10-30` | The Eternals — Chapter 3, paused at the edge |
| `adaptation-talent` | `adaptation-talent-v2.0-2026-10-30` | Adaptation Talent — v2.0 |

**Honestly optional.** Nothing depends on tags; the prose is already safe in git.

---

## What is already done — nothing below needs you

| | |
|---|---|
| The kit has a gate | `tools/check.py` + `MANIFEST.sha256` — passes `--strict`, 0 errors |
| Disclosure route | `SECURITY.md` |
| Labels readable | `author-gated` · `system-cheat` · `next` |
| Milestone exists | #1 · *The desk — every decision awaiting the author* |
| Five decisions filed | issues #8–#12, full evidence in each |
| Kit release | `account-era-2026-10-30` |
| The audit | `reports/GITHUB-AUDIT-2026-10-30.md` |
| Supergirl's fix | written, proved green (53/53) — `reports/supergirl-reaccept-2026-10-30/` |

---

## One thing worth knowing

`supergirl-adrian-vale` has a genuinely failing gate — seven accepted chapter hashes that no longer match their files after a real repair. It has failed since 2026-10-13 and it is **supposed** to fail: the record is stale, not the prose.

The fix is tested and sitting in the kit. It needs one session pointed at that repository, which I cannot do from here. If you ever want it closed, start a new Arena session on `supergirl-adrian-vale` and say: *"apply the re-acceptance script from soul-land-universal-kit/reports/supergirl-reaccept-2026-10-30/"*.

---

# Part 2 — bringing the other twelve repositories to the method

`docs/METHOD_CONFORMANCE.md` is the scorecard. This is the click path. Tiers are ordered so
stopping halfway still leaves the account better than it was.

**The cheapest real win is Tier 1: six repositories, one paragraph each, five minutes of clicks
each, and it closes R5 — "names the law" — everywhere it is still missing. Six of thirteen
repositories do not name the guide at all; after this, none of them.**

---

## Tier 1 — one paragraph per README (closes R5 in 4 repos)

Open each repository's `README.md` in the browser, click the **pencil** (Edit), and paste this
directly under the first heading. Then **Commit changes** with the message shown.

Repositories: `supergirl-adrian-vale` · `the-authors-desk` · `storyos-site` ·
`mcu_eternal_fanfic` · `stark_heir` · `the-universal-storyline-creation`

```markdown
**The method:** this repository is held to
[`how-to-write-fanfiction`](https://github.com/gm5206663-bit/how-to-write-fanfiction)
(guide v3.3 / law v5.7). Where the two disagree, the guide wins. One command checks this
repository: `sh tools/run_all.sh`.
```

Commit message: `Cite the law (R5) — how-to-write-fanfiction v3.3/v5.7`

That paragraph is not decoration. It is the pointer that lets the next agent correct the repo
instead of guessing at it, which is the whole reason the guide asks for it.

---

## Tier 2 — a battery per repository (closes R1 in 5 repos)

Repositories: `sara` · `adaptation-talent` · `pokemon-adaptation` · `mcu_eternal_fanfic` ·
`stark_heir` · `storyos-site` · `the-universal-storyline-creation`

For each one:

1. Open `tools/` → **Add file** → **Create new file**
2. Name it `run_all.sh`
3. Paste the contents of
   [`tools/method/template/run_all.sh`](../tools/method/template/run_all.sh)
4. Edit the **two marked lines** so they name *that* repository's real checks
5. **Commit changes** → message: `Add the one-command battery (R1)`

The runner prints every layer it ran and every layer it skipped. A skipped layer is not a pass —
it prints that too, so the gap is visible instead of assumed.

**Do not add a check you have not run.** If a layer reds out on the first try, that is the battery
doing its job on day one — record it and fix the work, not the line.

---

## Tier 3 — the proof of bytes (closes R3 in 6 repos)

Order: `storyos-site` → `soul-library` → `the-authors-desk` → `mcu_eternal_fanfic` →
`stark_heir` → `the-universal-storyline-creation`

1. Create `tools/manifest.py` from
   [`tools/method/manifest.py`](../tools/method/manifest.py) — add file, paste, commit:
   `Add the portable manifest tool (R3)`
2. Then, once, from a session that can run it:
   `python3 tools/manifest.py --write` and commit the resulting `MANIFEST.sha256`

`soul-library` note: its `sentinel.html` looks like proof and is not — it contains no hashes at all
(checked: zero matches). A status page is a claim about state; a manifest is proof about bytes.

---

## Tier 4 — state that rebuilds itself (closes R4 in 4 repos)

`sara` · `soul-library` · the profile README · `the-universal-storyline-creation`

Each needs a status file generated from the tree at the end of a turn, not a paragraph someone
remembered to update. The guide's Ship Law wording: if it is not rebuilt, it is a memory, and
memories drift silently.

---

## The one thing that is *not* a click

`adaptive_prodigy` ch116 opens the Hawk-Soul Union on-page; the lock says first use is reserved.
That is a decision about your own prose, and three options are written out in
`docs/METHOD_CONFORMANCE.md` §4. Nothing should be clicked until you pick one — the gate is
correctly red, and it will stay red, on purpose, until the ruling exists.
