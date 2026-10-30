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
