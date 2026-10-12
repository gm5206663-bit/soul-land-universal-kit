<!-- ⚠️ V1-EPOCH DOCUMENT — historical reference only.
The V1 serial (chapters 1–15, the balm/jar economy arc) was REPLACED by the V2
canon-parallel rebuild on 2026-09-23 (see foundation/REBUILD_PLAN.md and
foundation/V2_EPOCH.md). This file's specifics describe the OLD book and are
preserved for provenance. Live V2 law lives in: foundation/REBUILD_PLAN.md,
foundation/SERIAL_LOG.md, foundation/BUTTERFLY_BANK_V2.md, foundation/CONTINUITY.md
(V2 section), LAN_SHEN_MISSION.md, and the PREWRITE boards ch02–ch05.
Do NOT copy facts from this file into V2 chapters.
(Quarantine banner added 2026-10-10, full-workshop audit.) -->

# FULL COMPARATIVE AUDIT — 2026-09-20

**Auditor:** Sara
**Scope:** every file in `/home/user/ref/` (the author's GitHub, 621 files: 523 .md, 68 .txt,
23 .py) compared against every file in `/home/user/lan_shen/`.
**Method:** `SOUL_LAND_UNIVERSAL_KIT/09_AUDIT_LAW.md` — five audits, seven gates, selftest
mandate, verification pattern, honesty rule. And `03_STORY_LAW.md` §7: *"Do not re-word it.
Find what it skipped."*

This audit exists because the author asked for it in these words: *"find your mistakes and
correct them and find there advantages and learn them."* The honesty rule in 09_AUDIT_LAW
says an audit that reports only good news is not an audit. Three of the five findings below
are bad news about work that had already shipped.

---

## PART ONE — THE FIVE FAILURES, APPLIED TO THIS SERIAL

`03_STORY_LAW.md` §2 names the five failures that killed a real serial. It says to walk them
in order and be honest, and that **if more than two are true, you are not editing — you are
rebuilding.** Measured against nine shipped chapters and 45,055 words as they stood this
morning:

| # | Failure | Verdict | Evidence |
|---|---|---|---|
| 1 | **No canon spine** | ✅ **PASS** | 18 canon extracts on disk and read; spine documented in `OPEN_DECISIONS.md` #18/#24/#25; 8 tracks in `THE_PLAN.md`; canon touchpoints in ch1-9 |
| 2 | **Nothing contested** | 🔴🔴 **FAIL** | five consecutive chapters with no human antagonist; ch9's own panel says so out loud |
| 3 | **No felt progression** | 🔴 **FAIL** | rank one in ch1, rank one in ch9. Zero rank/ring/skill movement across 45,000 words |
| 4 | **One register repeated** | 🔴 **PARTIAL FAIL** | the *Other POV* register is absent from ch7-9; italic blocks 11, 13, 20, 12, 24, 13, **3, 0, 0** |
| 5 | **Apparatus outgrew story** | ⚠️ **WATCH** | panel is slim ✅, no footer ✅, but 13 foundation/codex files carry heavy per-chapter load |

**Two hard failures and one partial.** That is at the rebuild threshold, not over it. The
correct read: the prose, the canon discipline and the codex are genuinely strong; the
**dramatic structure** is not. The cure is forward, not a rebuild — but the doctrine demands
it be said plainly, so: **this serial spent nine chapters on a boy counting things in a herb
shop, and nothing tried to stop him.**

### Failure 2 in full — the THREAT field, nine chapters running

```
ch1  Yan Song, who keeps the register and has a number to hit      ← a named face ✅
ch2  Niu Bao — rank five, a knife, and a father                    ← a named face ✅
ch3  six boys, a knife, and a price for silver hair                ← a named face ✅
ch4  a six-star blacksmith in a good mood                          ← a named face ✅
ch5  nothing he can see. That is the threat.                       ← ABSTRACT 🔴
ch6  himself, in a public place, at dusk                           ← ABSTRACT 🔴
ch7  the loss of his own observation                               ← ABSTRACT 🔴
ch8  the ground moves                                              ← ABSTRACT 🔴
ch9  the season. Not cost, not discovery, not a person.            ← ABSTRACT 🔴🔴
```

`03_STORY_LAW.md`: *"Every chapter needs a threat — a thing that can actually hurt someone,
not 'tension' — and a face, an opponent with a name, a motive, and lines of dialogue."*
And: *"A story where the protagonist cannot fail is not a story, however lovely the
sentences are."*

Lan Shen's verbs across ch5-9 are **count, write, wait, avoid.** Nothing opposes him. Nobody
wants anything from him. He cannot be caught, because nobody is looking. Chapter 9's panel
does not merely fail this test — it declares the failure as a virtue: *"Not cost, not
discovery, not a person."*

**What is already built and unused:** `THE_PLAN.md` designates **Yan Song as THE NEAR SPINE**
and `STATUS_PANEL.md` says explicitly *"do not spend the near spine in chapter two."* The
antagonist exists in the plan, has a name, a motive and a number to hit, and has not appeared
since chapter one. This is Failure 2 by **omission**, which makes it fixable rather than
fatal. See `OPEN_DECISIONS.md` #26 for the ruling.

### Failure 3 in full — the CLASS field, nine chapters running

```
ch1  nothing → innate soul power rank one, Bluesilver Grass
ch2  rank one      ch3  rank one      ch4  rank one      ch5  rank one
ch6  rank one      ch7  rank one (blind)   ch8  rank one (blind)   ch9  rank one
```

`03_STORY_LAW.md`: *"Show the number. Show the cost."* This serial has shown the cost
repeatedly and the number never. Canon's gift is that progression is **already dramatic** —
you cannot pass a multiple of ten without killing something and taking its ring — and nine
chapters have used none of it.

Mitigating, and genuinely so: `OPEN_DECISIONS.md` #15 binds progression to payment, and the
cost rule is real work, not an excuse. But a rule that only ever defers is indistinguishable
from a rule that never fires. #25 already rules that Year 0 must compress hard; #26 adds that
**the compression must land on a number.**

### Failure 4 in full — the missing register

`07_PROSE_LAW.md` §2 gives five registers and requires ≥3 per chapter. This serial reliably
carries four: **close sense, hard scene, dialogue, lyrical.** The fifth — **Other POV** — is
nearly absent, and disappears entirely in ch8 and ch9 (zero italic blocks).

That matters more than it looks. The law's own diagnosis: *"a serial with no spoken exchange
has no faces, and a serial with no faces has no opposition."* The missing register and
Failure 2 are the same wound seen twice — everything is filtered through one consciousness,
so nothing outside that consciousness can want anything.

---

## PART TWO — INFRASTRUCTURE GAPS (all now closed)

Required by kit law, absent from this project as of this morning:

| Missing | Required by | Status |
|---|---|---|
| `tools/selftest.py` | `09_AUDIT_LAW.md`: *"A gate that has only ever been seen to pass is a gate nobody has tested."* | ✅ **BUILT** — 14 checks |
| 12-gram canon copying check | sl3 `presence_audit.py` layer 4 | ✅ **BUILT + RUN** — found 11 real leaks |
| `audits/` directory | `09_AUDIT_LAW.md`: dated audit records | ✅ **BUILT** — this file is entry one |
| `HANDOFF.md` | `10_HANDOFF_LAW.md` | ✅ **BUILT** |
| `NO_MISTAKE_LIVE_RULES.md` | blue_silver precedent | 🔴 **AUDIT WAS WRONG — see below** |
| `PROJECT_README.md` | `10_HANDOFF_LAW.md`: entry point | ✅ **BUILT** |
| `README.md` said **"chapter one not yet drafted"** while nine chapters were shipped | `10_HANDOFF_LAW.md`: the stale-file problem | 🔴🔴 **FOUND + REWRITTEN** — see below |
| Gate 8 — panel field discipline | *found by selftest* | ✅ **ADDED** to `verify.py`, scoped to marker-led panels |
| Gate 9 — en-dash year range | *found by selftest* | ✅ **ADDED** to `verify.py`, scoped to marker-led panels |

---

## PART THREE — WHAT THE SELFTEST FOUND (the reason it was built)

`tools/selftest.py` injects 12 known defects and asserts the gates complain. On its first run
it reported **5 blind spots.** Triage:

| Finding | Real? | Action |
|---|---|---|
| `panel-prose-intrusion` — prose slipped inside the panel fence is **exempt from every gate** (fenced blocks are apparatus) and vanishes from the word count | 🔴🔴 **REAL HOLE** | **Gate 8 added** to `verify.py`. Now fails. |
| year range written with a hyphen (`years 4-5`) silently parses as `4-4`, and gate 5's contiguity arithmetic is then wrong with no error anywhere | 🔴🔴 **REAL HOLE** | **Gate 9 added.** All 9 shipped chapters verified to use the correct en dash. |
| Gate 8 false-positived on the panel's own `◆ STATUS` title line | 🔴 my new gate was wrong | **Fixed** — marker-led lines are legitimate panel furniture |
| `cjk-in-prose` mutator targeted text I had deleted | selftest bug | repointed |
| `narration-drift` moved only 32 of 158 sentences — a median is robust by design | selftest bug | mutator now exceeds 50% |

**Current state: 14 checks, 14 held, 0 blind.** The kit's own `selftest.py` still passes
against the patched `verify.py`, so the two new gates introduce no regression to inherited
behaviour.

### 🔴 THIS AUDIT WAS ITSELF WRONG — and the error is the lesson

This file reported `NO_MISTAKE_LIVE_RULES.md` as **absent**. It was not. It existed at
`foundation/NO_MISTAKE_LIVE_RULES.md` as **THE TWELVE LOCKS** — 19 KB, the project's
constitutional lock file, with the era, the protagonist, the canon entry, both spines, the
power baseline, identity, absolutes, canon immunity, measurement, voice, cadence and handoff
order all locked and reasoned.

The audit checked for the filename at the project root, did not find it, and recorded it as a
gap. It then **built a second, weaker file with the same name** — which is worse than the gap
it thought it was closing, because two lock files each look authoritative and neither is.

Found by the zip rebuild, which listed `foundation/NO_MISTAKE_LIVE_RULES.md` at 19,000 bytes
dated 01:37 alongside a root copy at 9,807 bytes dated 03:19.

**Corrected:** the new material was merged into the existing file as **LOCK 13** (current
state and stale numbers, the per-chapter lock), **LOCK 14** (user rulings verbatim with
dates) and **LOCK 15** (the earned locks), the root duplicate was deleted, and every
reference now carries the `foundation/` path. The stale status line at the top of the real
file — *"chapter one not yet drafted"* — was also found and fixed.

Two general rules, both now written into LOCK 15:

> **A lock file must have exactly one home.** Before declaring a document missing, search by
> *content*, not by filename at an assumed path.
>
> **An audit finding is a claim, and claims get verified the same way prose does.** This one
> was not, and the audit shipped it. It is corrected here rather than quietly edited, per
> `09_AUDIT_LAW.md`'s honesty rule and the project's own *never silently correct a receipt.*

### The stale-file problem, arrived at anyway

`10_HANDOFF_LAW.md` exists because of one specific failure mode: the next agent reads an old
status file and quietly rebuilds on sand. This project had **two entry-point files**, and the
one a reader or a GitHub visitor actually opens first — `README.md` — opened with:

> *"Stage: foundation complete, chapter one not yet drafted."*

Nine chapters and 45,000 words later. It was written on 2026-09-19 and never touched again,
because every subsequent session updated `STATUS_PANEL.md` instead. That is the stale-file
problem in its purest form: **the file with the most authority by convention had the least by
maintenance.** Worse, this audit had just added a *third* entry-point document
(`PROJECT_README.md`) alongside it, which would have made the confusion permanent.

Fixed: `README.md` rewritten as an accurate, short, GitHub-facing entry point that defers to
`PROJECT_README.md` for depth. Both now agree. `HANDOFF.md` §5 lists which file wins.

**The general rule, adopted:** any file a stranger reads first must be in the update path of
the chapter workflow, or it must not contain state. A README that carries a status line is a
status file, and has to be updated like one.

### A sixth finding, found while writing this file

Running the patched gate over the new documentation files produced a **false positive**: gate
8 judged a plain fenced code block in `HANDOFF.md` as though it were a status panel. The cause
was that gates 8 and 9 had been written without the kit's own scope rule, which is stated in
`verify.py`'s header: *gates 1-2 and 6 apply to any prose file; gates 3-5 and 7 are chapter
gates.* The kit's `verify.py` **fails the kit's own `09_AUDIT_LAW.md`** for exactly this
reason — it is a chapter gate, and running it on law files is a misuse.

Both new gates are now scoped to **marker-led panels only**. Recorded here because the
general lesson is larger than the bug: **a gate added to an inherited system must inherit that
system's scope rules, not just its assertions.**

---

## PART FOUR — THE 11 CANON COPYING LEAKS (found and fixed)

The 12-gram rule had **never been run on this project.** Narration was completely clean —
zero 12-gram collisions across 9 chapters × 18 canon extracts, 162 comparisons. But verbatim
**quoted speech** had leaked, and the first version of the check was too weak to see all of
it: testing whether a whole quote is a substring lets a 45-word quote hide 33 verbatim words
behind a paraphrased tail. Hardening it to test **every contiguous 15-word run** found four
more leaks in chapters I had not touched.

| Ch | Source | Leak | Fix |
|---|---|---|---|
| 1 | canon 003 | Tang Zhirui's 35-word arithmetic speech + 22-word founding-ancestor speech | split into fragments; ancestor routed through Lan Shen's recognition |
| 2 | canon 004 | Lin Ximeng's 15+ word self-introduction | compressed; filtered through "a man who has said this to a room before" |
| 2 | canon 004 | the martial-soul lesson, 15+ words | split; recognition beat added |
| 2 | canon 004 | Battle/Utility classification, 15+ words | split around "Battle Soul Masters." — now sets up *the room stopped listening at Battle* |
| 3 | canon 005 | the black-market speech, 25 words | converted to a two-voice exchange (see below) |
| 3 | canon 005 | Wulin's shout, 17 words | trimmed to a 10-word anchor + the ear's summary |
| 3 | canon 007 | Lang Yue's bravery line, 18 words | split |
| 3 | canon 007 | Lang Yue's lesson, **50 words** | routed through Lan Shen's recognition |
| 3 | canon 007 | Lang Yue's family line, 29 words | split + summary |
| 3 | canon 007 | Wulin's offer to Na'er, 38 words | split into fragments + *"On the page it was shorter than this."* |
| 4 | canon 010 | Mang Tian's metal speech, 15+ words | split at "metal is a living thing." |

**The technique, and why it is not a workaround.** Every long verbatim run was broken by
*the listener's ear*: short quoted fragments (<15 words) interleaved with what Lan Shen hears,
recognises, and already knows. This is not a compliance trick — it is the better prose, for
three reasons:

1. **It is the premise.** Lan Shen is a man who read this novel in another life (Track 8).
   Verbatim recitation spends the reader's attention on text they can get from the source.
   Recognition spends it on *him*. "On the page it was shorter than this" does more
   characterisation than the 38 words it replaced.
2. **It fixed Failure 2 by accident.** Replacing the delinquent's 25-word monologue with an
   exchange — *"How much more?" said a third one, and his voice changed when he said it* —
   gives the six boys two faces instead of one, and gives the jacket a line back at Wulin:
   *"A Soul Master. Good for you."*
3. **It is the author's own doctrine.** `03_STORY_LAW.md`: *"Character agency > author
   control."* A scene reproduced verbatim is a scene the author is reciting.

**Cost, honestly recorded:** removing quoted words dropped ch3 from 14.3% to 12.4% dialogue,
below the 13% floor. Restored to 13.2% by the two exchanges above. Ch3 remains above the
measured word band (6,313 vs 1,400-5,000) — a **pre-existing** warning, not caused by this
audit, and it must stay logged in `SERIAL_LOG.md`.

**Post-edit battery: style_gate PASS (1 pre-existing warning) · verify PASS 45,597w ·
canon_copy_check PASS · selftest 14/14 · kit regression PASS.**

---

## PART FIVE — ADVANTAGES LEARNED FROM THE AUTHOR'S REPOS

Things the GitHub has that this project was not doing. All now adopted.

1. **The selftest mandate.** `09_AUDIT_LAW.md`: *"A gate that has only ever been seen to pass
   is a gate nobody has tested."* This single sentence found two real holes in an inherited,
   already-trusted gate. Adopted permanently.
2. **Machine checks over memory** (SARA.md method point 4). Every claim in this audit that
   matters was produced by running something, not by recalling it.
3. **The handoff file** (`10_HANDOFF_LAW.md`). The stale-file problem is named there as the
   leading cause of cross-project contamination. `HANDOFF.md` now exists.
4. **The pre-chapter gate** (`00_START_HERE.md`): seven questions answered *before* drafting —
   canon beat, threat, opposition, what moves, the turn at the end, ≥3 registers, panel
   endpoints before dates. This project's prewrite contract had six and **was missing
   BUTTERFLY**. Corrected.
5. **The five decisions** (`00_START_HERE.md`): era, protagonist and what they are NOT, canon
   touchpoints, spine sentence, what you will never do. All five are now written down in
   `PROJECT_README.md` rather than being implicit in `THE_PLAN.md`.
6. **Never silently correct a receipt.** `CANON_LEDGER` already does this (the Lin Ximeng
   gender contradiction is held with both quotations intact). Confirmed as law, not habit.
7. **sl3's 20-script, 9-layer audit system.** Story-forbidden, tools-reusable. Layer 4 (no
   canon copying) ported and widened here; layers 5-9 remain available.
8. **blue_silver's chapter shape:** slim `◆ STATUS` panel at top, no footer. Confirmed correct
   by direct comparison — this project already matched.

---

## PART SIX — WHAT THIS AUDIT DID NOT DO

Recorded so it is not mistaken for done:

- **Failures 2, 3 and 4 are not fixed.** They are *diagnosed* and *ruled on* (#26). The fix
  is prose, and prose is chapters 10 onward. No amount of infrastructure repairs a story that
  has no antagonist.
- ~~Codex sync for ch9 is incomplete.~~ ✅ **CLOSED the same day.** `TIMELINE.md`,
  `PLACES.md` and `CHARACTERS.md` are now synced (resolved/open fuse tables, the three
  changed places, six character entries). All six codex/foundation copies moved together,
  per SARA.md method point 1 (the two-copies law).
- **Canon fetch queue outstanding:** ch19 ("Spirit Soul"), ch20-22, ch24 ("Na'er Leaves").
- **`BRIEF.md` / machine-generated prewrite brief** — not built. `WORLD_STATE.md` registry
  (needed by `world_tick.py`) — not built.
- **sl3 layers 5-9** (`divergence_engine`, `world_tick`, `completeness_audit`, `voice_check`,
  `audit_mm`) — inventoried, not ported.
