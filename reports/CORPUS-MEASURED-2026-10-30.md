# The corpus, measured — 2026-10-30

**What this is.** Every registered book re-measured from disk today, every declared edge checked
against what is actually written, and every defect the measurement surfaced named. No count in this
file was typed from memory: it comes from `tools/register.py` run over this repository at
`HEAD`, and from the chapters themselves.

**Why it exists.** The register is a generated file, and generated files rot the moment nobody
regenerates them. It had not been regenerated since **2026-10-13**. One book had moved and no page
on the account said so.

---

## The corpus today

**16 registered books · 283 chapters · 1,211,566 words.** The 2026-10-13 register said
**282 · 1,209,710** — the difference is one chapter, and it is the whole finding below.

| words | ch | book | over-60 | floor hits |
|---:|---:|---|---:|---:|
| 523,356 | 116 | `adaptive_prodigy` | 0 | 0 |
| 270,659 | 52 | `soul_land_4_fire_phoenix` | 0 | 0 |
| 80,127 | 24 | `Soul_Land_2_Project` | 0 | 0 |
| 65,081 | 24 | `soul_land_devouring_dragon` | 0 | **11** |
| 63,691 | 7 | `soul_land_3_oc` | 0 | 0 |
| **34,067** | **8** | **`lan_shen`** | 0 | 0 |
| 25,956 | 9 | `qian_xunji` | 0 | 0 |
| 25,792 | 10 | `soul_land_2_the_grey_wolf` | 0 | 0 |
| 25,379 | 4 | `Miraculous_Project` | 0 | 0 |
| 22,487 | 8 | `soul_land_2_new` | 0 | 0 |
| 19,360 | 6 | `soul_land_new` | 0 | 0 |
| 18,605 | 5 | `soul_land_1_fire_dragon_lizard` | 0 | 0 |
| 15,802 | 4 | `soul_land_system_cheat` | 0 | 0 |
| 13,696 | 4 | `soul_land_holy_spirit` | 0 | 0 |
| 3,802 | 1 | `soul_land_3_new` | 0 | 0 |
| 3,706 | 1 | `dragon_prince_yuan_native_oc_fanfiction` | 0 | 0 |

**Zero sentences over sixty words, corpus-wide.** That law has held across every book since the
2026-10-13 repair, and it still holds today.

---

## What moved, and what failed to notice

### `lan_shen` — a shipped chapter that reached no ledger but the one that mattered

Chapter 8, *Clean Hands*, shipped **2026-10-16**. Its own `SERIAL_LOG.md` recorded it properly as
REVISION 12, with the gates, the word count, and two honest flags. Everything above the serial —
`REGISTER.md`, `PROJECTS.md` — still said **7 chapters / 32,211 words**, because neither is
regenerated automatically and nobody ran the command.

| | said | measured |
|---|---|---|
| chapters | 7 | **8** |
| words | 32,211 | **34,067** |
| delta | — | +1 chapter, +1,856 words |

Both files corrected today. This is the failure mode the kit's own law names — *counts are measured,
never typed* — and the fix is mechanical: the register regenerates in one command, and
`tools/check.py` now stamps `REGISTER.md`'s generating tool into the kit's manifest so a stale
register is at least visible.

### A provenance receipt that does not verify

`PROJECTS.md` carried `lan_shen/` → *repo `lan_shen`, commit `cc8c180`*. Today:

```
$ git cat-file -t cc8c180
fatal: Not a valid object name cc8c180
$ gh api repos/gm5206663-bit/lan_shen      → 404 Not Found
```

The repository is gone and the commit exists nowhere in this history. The row is **not deleted** —
provenance history is history, and erasing it would hide the fact that a copy once existed — but it
now says plainly that it cannot be checked against anything.

---

## The defect that had no gate: the zero `?`/`!` law

`lan_shen`'s REVISION 12 closed with:

> *CH7 DEFECT FLAG: ch7 contains 11 question marks; the zero ?/! rule is not enforced by any gate.*

The second half was true and important. The first half was **aimed at the wrong chapter.**

Measured today, narration only (quoted spans stripped, which is what the law governs — every
PREWRITE board says *"zero ? and ! in prose"*, and a character may ask a question in dialogue):

| chapter | narration `?` | narration `!` | all `?` | all `!` |
|---|---:|---:|---:|---:|
| Ch01 | 0 | 0 | 1 | 0 |
| Ch02 | 0 | 0 | 1 | 0 |
| Ch03 | 0 | 0 | 0 | 0 |
| **Ch04** | **1** | 0 | 6 | 1 |
| **Ch05** | **5** | 0 | 29 | 5 |
| Ch06 | 0 | 0 | 11 | 1 |
| Ch07 — the flagged one | **0** | **0** | 13 | 12 |
| Ch08 | 0 | 0 | 0 | 0 |

**ch7's prose is clean; every one of its 13 `?` and 12 `!` sits inside quotation marks.** The real
violations are six, in ch4 (1) and ch5 (5).

**What was built.** `style_gate.py` check **5b** counts `?`/`!` in narration only, and the selftest
grew three cases so the detector cannot go blind: a narrating question, a narrating exclamation, and
a **quoted** question that must *not* misfire. Suite: **20/20** (was 17).

**Why it warns rather than fails.** Clearing the six means rewriting shipped prose. That is the
author's word, not a repair, so `QE_ENFORCE = "warn"` — one constant, flipped to `"fail"` the day
those six are cleared. Advisory is not blind: the selftest proves the detector speaks.

---

## The largest open quality defect on the account

`soul_land_devouring_dragon`: **11 of 24 chapters sit below the dialogue floor.** It is the only
book in the corpus carrying a floor-hit count at all. Its canon-voice rollout is measured at
**12 of 24** chapters rewritten (next: Ch 13), so the two figures describe the same work from
opposite ends — the rewrite is also the repair.

Nothing else in the corpus has a structural defect. Zero over-sixty sentences anywhere, zero
registered books unaccounted for, **33 of 33 chapter-bearing trees** classified (28 under a book,
5 archived or inbox).

---

## What only the author can decide, restated and current

| Where | The open call | State |
|---|---|---|
| `lan_shen` Ch8 | **3,192 words against a 3,800–5,000 band** — flagged, deliberately not padded | the light-unit case is written in REVISION 12; the author may accept it as-is |
| `lan_shen` | **mother's name: "Lang Yue" (shipped text, codex) vs "Lan Yue" (CONTINUITY row 6, canon-011 receipt)** | ch8 follows the shipped text; the conflict is unresolved |
| `lan_shen` ch4 + ch5 | **six narration `?`** under the zero law | mechanical to fix, but it is rewriting prose |
| `lan_shen` | **arc map re-cadence** (desk item A) — filed as issue #8 with the full measurement | awaiting |
| `soul_land_4_fire_phoenix` | **V2 public-promotion numbering** — staged C48–C55, `apply_authorization: NOT_GRANTED` (issue #9) | awaiting |
| `supergirl-adrian-vale` | **seven stale acceptances** — fix written and proved green (53/53) in `reports/supergirl-reaccept-2026-10-30/` | needs one session on that repo |

---

## How to keep this from rotting again

1. **Regenerate, don't retype.** `python3 SOUL_LAND_UNIVERSAL_KIT/tools/register.py --root . --out REGISTER.md` after any chapter ships.
2. **The kit's gate now stamps what it governs.** `tools/check.py --strict` covers the manifest; run it before saying the corpus is in order.
3. **A shipped chapter updates three things in the same commit:** its `SERIAL_LOG.md` row, `PROJECTS.md`'s count, and `REGISTER.md`'s regeneration. ch8 did the first and skipped the other two — which is exactly how a corpus of 1.2 million words ends up one chapter short of its own record.

---

# Addendum — the name rule, measured (2026-10-30, later the same day)

## I nearly broke the corpus

Drafting a "fix" for the ch8 name flag, I had a mass replacement ready: `Lan Yue` → `Lang Yue`
across 105 lines of records, on the strength of one count — canon spells Wulin's mother
**66 × "Lang Yue" · 8 × "Lan Yue" · 3 × "LANG YUE"**, so the g-form wins.

Then the codex stopped me:

```
LANG YUE  (with a g)  = canon. TANG WULIN'S MOTHER.
LAN  YUE  (no g)      = AU-ORIGINAL. LAN SHEN'S SISTER.
```

**They are two different people, separated by one letter, deliberately.** That replacement would
have merged an OC into a canon character across five chapters of shipped prose — the exact failure
the file exists to prevent. Measured before anything was written; nothing was written.

## What the flag in REVISION 12 actually was

> *"NAME CONFLICT (author call): the mother is 'Lang Yue' in shipped text and codex; CONTINUITY
> row 6 and the canon 011 receipt note say 'Lan Yue'."*

**Settled by count, and closed.** Canon spells the mother both ways. "Lan Yue" in those records is
an alternative spelling of the same woman, not a second person. The house form is right; the shipped
text matches it. No conflict, no ruling needed.

## What the measurement found instead

`codex/CHARACTERS.md` states:

> *"No shipped chapter uses both spellings. Ch1, 4-9 use only Lan Yue; ch3 and ch10 use only Lang
> Yue. That separation is load-bearing and must be maintained."*

Measured across all eight shipped chapters:

| | |
|---|---:|
| `"Lan Yue"` | **0** |
| `"Lang Yue"` | **46** |

ch2 ×8 · ch4 ×10 · ch5 ×10 · ch7 ×8 · ch8 ×10; ch1, ch3 and ch6 name her not at all.

**The claim is false for every chapter it lists.** And it names ch10, which does not exist — the
serial's edge is ch8.

Two readings, and they are not equivalent:

**(a) The codex is right and the prose collapsed the sister.** Then five chapters need a naming
sweep. Supporting it: the noodle-street washer job — six to eleven, eleven federation coins,
starting Monday — is given on the page to **Lang Yue**, while the codex assigns *"the noodle-street
job"* to the sister. And `CANON_LEDGER` row 69 stages canon 011's job-hunt for Lang Yue at ch13, so
the same job may be staged twice, once per woman.

**(b) The codex is wrong and only the mother is named.** Then the sister has never reached the page,
and a rule the serial calls load-bearing governs a character who does not appear.

**Neither reading was adopted.** (a) means rewriting five shipped chapters; (b) means deleting a
rule the corpus treats as load-bearing. The evidence is recorded in the codex block itself, marked
**MEASURED — AWAITING RULING**, and `SERIAL_LOG` REVISION 14 carries the same. No name changed, no
prose touched.

## Two smaller things, also measured

**The `?`/`!` detector had the line-wrap bug the log already documented.** REVISION 4's "METRIC
PARITY HARMONIZATION" found that a quotation straddling a hard newline defeats a line-scoped quote
counter. My check 5b had exactly that flaw — ch1, ch2 and ch3 contain wrapped quotations that
survived it. Hardened to strip across newlines. The six narration violations are unchanged (ch4 ×1,
ch5 ×5), so the original finding stands; what changed is that ch1's dialogue share now measures
**48.6%** — above the standard ceiling, inside the `lesson` band. Its dial may need declaring.

**The six narration `?` are real.** I checked whether my stripper was fooling itself: chapters 4
and 5 contain **zero** multi-line quotations, so the `?` at ch4:25, ch5:23 and ch5:147 sit in
narration honestly — free-indirect thought and one italic interior monologue. The law says prose
carries none. Still the author's call, still `QE_ENFORCE = "warn"`.

## The lesson, once

**A count can be right and the conclusion still wrong.** 66-to-8 was a true measurement of the wrong
question: *how does canon spell one woman's name* is not *how many women are named*. The codex was
the only file that could tell the difference, and it was one line I had not read yet.

---

# Addendum 2 — going deeper: the sister, the citation audit, and one claim I retracted

## 1 · The two-character question is closed — and I owe a retraction

Addendum 1 reported, with a table, that `codex/CHARACTERS.md`'s rule *"Ch1, 4-9 use only Lan Yue"*
is **"false for every chapter it lists"** because the shipped chapters measure `"Lan Yue"` **0** and
`"Lang Yue"` **46**.

**That was an over-read, and it is retracted.** `"Use"` never meant `"name"`. The prewrite board
states the intended sense exactly:

> `PREWRITE_ch11.md` — *"She has been in seven chapters (ch1, 4, 5, 6, 7, 8, 9) and has never had a
> scene of her own."*

The sister is **present in the household and unnamed on the page**. Zero occurrences is not
evidence against her existence — it is the condition the board describes. And her first scene is
owed at **ch11**, which is unwritten, so the plan is intact and nothing is late.

The rule stands, unchanged, and it binds hardest exactly where she first speaks.
`PREWRITE_ch11.md` already carries it in its own gate list, verbatim. **No prose was touched.**

The codex now says what it meant, with the measurement beside it. REVISION 15 records both the
finding and the retraction **in the same place**, because an over-read published as a defect makes
the records less trustworthy than the error it was chasing.

## 2 · Two record defects the deeper pass did find

**`CONTINUITY.md` named the wrong woman.** Its firewall note read *"Lan Yue washes dishes on the
noodle street (ch5, ch8), eleven copper a day"* — but the washer job is **Lang Yue's**, given on
the page in ch8 and canon 011's own beat (*"Next week I'll go into town and find work… I've found
one"*). The note credited it to the sister. Corrected in place, with a dated banner rather than a
silent edit.

**`CANON_LEDGER` row 69 calls canon 011 "held exactly" at ch13 — but ch8 already spent it.**
Lang Yue finds the job on the page: eleven federation coins, six to eleven, starting Monday. The
dye house at ch13 is therefore either a **second** job (a butterfly — canon's search resolves in a
day, the serial keeps her hunting) or the same beat staged twice. Flagged **SPENT EARLY**, left for
the board. It is the defect class this ledger already names for *"Lin Lin"* in row 74.

## 3 · The citation audit — 522 paths, five verdicts

No gate had ever checked whether the files the records cite still exist. `lan_shen/tools/record_links.py`
now does, across all 33 record files:

| verdict | count | meaning |
|---|---:|---|
| **OK** | 371 | resolves where cited |
| **MOVED** | 117 | exists elsewhere in the kit — prints the real path |
| **ARCHIVED** | 23 | in the one-home archive in history — recoverable by `git show` |
| **PLANNED** | 7 | names a chapter not yet written — a plan, not a citation |
| **EXTERNAL** | 2 | `storyos-site/scripts/drift.py` — a real file, in another repository |
| **DELETED** | 1 | was here, removed, recoverable from history |
| **MISSING** | **11** | *nowhere* |

Every class is a pass except MISSING, and the tool's selftest proves all six can be told apart:
a moved file, a planned chapter, an archived one, a deleted one, a missing one, and — the case that
matters most — **no history at all**.

### The 11 missing, and their deadline

`state/canon.json` · `state/laws.json` · `state/projects_registry.json` · `TRANSFER_BOOTSTRAP.txt` ·
`extract_state.py` · `mailmap.txt` · `fix/RUN_ME.md` · `foundation/PREWRITE_ch04_draft_block.md` ·
`scripts/drift.py`.

These are cited by `SERIAL_LOG` and `CANON_NOTES` and exist **nowhere in this repository's history**
— they belonged to the standalone `lan_shen` repository, which was deleted in the 2026-10-12
consolidation. GitHub's restore window for a deleted repository is **90 days**, which closes
**around 2027-01-10**. After that they are gone, and the citations point at nothing permanently.

**This is the only time-sensitive finding in the report.** If those state files matter, they should
be pulled back through GitHub's restore before that date. If they don't, the records should say so.

## 4 · The trap that nearly produced a false alarm

Mid-investigation I concluded that **`_archive/v1_epoch_ch01-15/` — where V2_EPOCH.md says V1's
15 chapters and 72,577 words were "archived, not deleted" — had never existed**, and that
`_archive/2026-10-12_one-home/` (478 files) was equally absent. Both lookups failed. Both
conclusions were wrong, and the cause was one word: **shallow**.

This workspace clones `--depth 1`. On a shallow checkout `git log` reports **1 commit** and
`9379d40` is simply an unknown object, so **every recovery instruction in this repository reads as
false**. `git fetch --unshallow` took the history to **333 commits**, and then:

```
$ git ls-tree -r --name-only 9379d40^ -- _archive/2026-10-12_one-home/ | wc -l
478
$ ... | grep v1_epoch
_archive/2026-10-12_one-home/lan_shen_v1_epoch/v1_epoch_ch01-15/Chapter_05_The_Better_Version.md
```

**Nothing is lost.** V1's chapters are there, under a path one level deeper than `V2_EPOCH.md`
says. The documentation's recovery command is correct; the checkout was not.

`record_links.py` therefore never reports MISSING when history is unavailable — it reports
**UNVERIFIABLE** and says why. A resolver that reads *"no history"* as *"no file"* would have marked
478 recoverable files as lost, which is precisely the failure this pass was auditing for.

---

# Addendum 3 — the deadline was wrong, and the tool is what proved it

**Correction to Addendum 2.** It reported **11 missing citations** and called them time-sensitive:

> *"They exist nowhere in this repository's history… GitHub restores deleted repos for 90 days,
> which closes around 2027-01-10. The only time-sensitive finding in this report."*

**That was wrong.** The number is **one**, and there is no deadline attached to the other ten.
I found this by making the tool look properly instead of by re-reading the report.

## What the eleven actually were

Every one was resolved individually against the live account on 2026-10-30:

| citation | where it really is | verdict |
|---|---|---|
| `state/canon.json` | `the-universal-storyline-creation` — **4,312 B** | alive, another repo |
| `state/laws.json` | same — **10,030 B** | alive, another repo |
| `state/projects_registry.json` | same — **24,534 B** | alive, another repo |
| `extract_state.py` | same, in `tools/` | alive, another repo |
| `scripts/drift.py`, `storyos-site/scripts/drift.py` | `storyos-site` — **13,650 B** | alive, another repo |
| `TRANSFER_BOOTSTRAP.txt` | the deleted standalone repo | **history**, not a dependency |
| `mailmap.txt` | same | **history** |
| `fix/RUN_ME.md` | same | **history** |
| `foundation/PREWRITE_ch04_draft_block.md` | **nowhere** | **genuinely gone** |

The eight "alive" ones are the Control Centre's and StoryOS's own files, cited from `CANON_NOTES`
and `SERIAL_LOG` with phrases like *"per the Control Centre `state/canon.json` ring_ages table"* and
*"it is their instrument, in their [repository]"*. **The citation was telling me where they lived.**
I was reading a cross-repo pointer as a missing local file.

The three "history" ones appear only inside `SERIAL_LOG`'s own table of *what the old standalone
repository gave* — and the laws they carried (TWO-COPIES, the en-dash range regex, the H1-numeral
rule, *"a number written to satisfy a check is worse than a warning left honest"*) are already
resident in this project's own files. Nothing is owed.

## The one that is truly gone

**`foundation/PREWRITE_ch04_draft_block.md`** — the 1,894-word canon-006 staging draft of
2026-09-23, named by `PREWRITE_ch04.md` as *"the raw body to re-voice and reassemble."*

It is absent from the working tree, from all **335** commits, and from the 478-file one-home
archive (whose `lan_shen_v1_epoch` holds 18 files and no draft block). It has never existed in this
repository.

- **Impact on the prose: none.** Chapter 4 was re-voiced from canon 006 directly and passed verify,
  style, canon_copy and banned-token.
- **Impact on the evidence trail: real.** Nobody can now check the board's claim that a 1,894-word
  draft existed, or compare the published chapter against the body it was rebuilt from.

It is recorded under `known_loss` in `tools/citation_sources.json` with the full evidence, and
`PREWRITE_ch04.md` carries a dated banner. **The author decides:** restore it (the deleted-repository
window still exists) or amend the board to say the draft did not survive.

## What changed in the tooling

`tools/record_links.py` gained three verdicts and one policy:

| verdict | meaning |
|---|---|
| `EXTERNAL` | lives in a named sibling repo — read from `tools/citation_sources.json`, every entry with its own evidence |
| `HISTORICAL` | a record of something deliberately gone; not a dependency |
| `KNOWN-LOSS` | cited, genuinely gone, already written down with the decision it needs |

**Policy:** a known loss is **printed, not failed**. The account's own sweep header states the
reason — *"a weekly red badge over known findings is a badge people learn to ignore."* A gate that
stays red forever over a finding already on paper trains people to skip the gate. New breakage still
fails, because an unlisted missing file has no entry in the registry.

## The gate is now layer 10

`checks/run_all.sh` runs it with the rest of the suite:

```
  PASS  1 verify.py                RESULT: PASS
  PASS  2 style_gate.py            RESULT: PASS (warnings)
  PASS  3 canon_copy_check.py      RESULT: PASS — no verbatim canon copying detected.
  PASS  4 marker-leak grep         no codex markers in any chapter
  PASS  5 privacy grep             no personal email / token / sandbox id
  PASS  6 build hygiene            no __pycache__ / .pyc / .bak / .DS_Store
  PASS  7 selftest.py              RESULT: PASS — every injected defect was caught and named.
  PASS  8 kit selftest.py
  PASS  9 banned_token_check.py    RESULT: PASS (all findings were exempt receipts)
  PASS  10 record_links.py         RESULT: PASS
  ALL GREEN — 10 layers held, 0 failed
```

522 citations: **379 ok · 117 moved · 20 archived · 8 external · 8 historical · 7 planned ·
1 known loss · 0 missing.**

## Second correction, same cause

Addendum 1 mis-read a codex line; Addendum 2 mis-read a citation. Both times the error was the same
shape: **treating a number as a conclusion.** 66-to-8 measured a spelling, not a population. Eleven
missing paths measured a search, not a loss — eight of them were never supposed to be here.

The tool now encodes the difference. That is the only durable fix: not being more careful next time,
but making the careful distinction something the machine refuses to skip.
