# WORKSPACE CLEANUP LOG — 24 August 2026

**Authorized by:** user ("full permission… cleanup and delete useless things… I don't want future problems")
**Method:** every file verified redundant/superseded BEFORE deletion → all originals preserved in a single archive → stale copies deleted → log written.

## The problem being prevented
`uploads/` contained pre-correction versions of documents that have since been fixed (wrong ranks, wrong canon, stale states). Leaving them risked a future session reading the OLD file and re-introducing corrected errors — the exact failure mode this project has fought repeatedly.

## Safety net
**`CODEX/98_ORIGINAL_UPLOADS_ARCHIVE_2026-08-24.tar.gz`** (306 KB, 14 files, integrity-verified) — every original upload, recoverable with `tar -xzf`. Never delete this file.

## Deleted (14 files from uploads/) — and where the content lives now

| Deleted file | Status at deletion | Content lives in |
|---|---|---|
| `MASTER_STORYTELLING_CODEX.md` | exact duplicate of v3.3 | `CODEX/01_UNIVERSAL_CODEX.md` (v4.1 superset) |
| `MASTER_STORYTELLING_CODEX (1).md` | v3.0 — verified strict subset of v3.3 (only version stamps unique) | same |
| `MASTER_STORYTELLING_CODEX (2).md` | v3.3 — base of the unified codex | same |
| `MASTER_STORYTELLING_CODEX_COMPLETE.md` | truncated (Parts 1-16 only); unique Captain Marvel assumption-failures extracted to Part 16.12 | same |
| `GENESIS_CODEX.md` | OMEGA 1.0 — all unique content (session commands, 100 locks, 14 axioms, error autopsies) merged | same |
| `GENESIS_CODEX_ADAPTIVE.md` | essence condensed into Part 15.6 System Adaptation Core | same |
| `GENESIS_CODEX_MARVEL_COSMIC.md` | verified: 0 lines missing from branch copy | `CODEX/03_PROJECT_MARVEL_COSMIC.md` |
| `GENESIS_CODEX_ONE_PIECE_SYSTEM.md` | verified: 0 lines missing from branch copy | `CODEX/04_PROJECT_ONE_PIECE.md` |
| `THE_GENESIS_CODEX.md` (BTTH v3.0) | superseded — working copy is newer (post-Chapter 11) | `BTTH_Project/THE_GENESIS_CODEX.md` |
| `THE_CODEX.md` (SL3 v1.0) | superseded — working copy is v2.2 (corrected power model, Na'er canon fix, AT system) | `Soul_Land_3_Project/THE_CODEX.md` |
| `chapter_01.md` (SL3) | identical to project copy | `Soul_Land_3_Project/chapters/chapter_01.md` |
| `chapter_02.md` (SL3) | superseded — project copy has v1.7 rank erratum | `Soul_Land_3_Project/chapters/chapter_02.md` |
| `chapter_03.md` (SL3) | superseded — project copy has rank-curve corrections (v2.0) | `Soul_Land_3_Project/chapters/chapter_03.md` |
| `CONTINUATION_PROMPT.md` (SL3, stale Ch-3 state) | superseded — current prompt reflects end of Ch 5 | `Soul_Land_3_Project/CONTINUATION_PROMPT.md` |

## Also fixed during cleanup
- **Gap found:** `BTTH_Project/` had no continuation prompt (the original was overwritten in uploads by the later SL3 upload and never copied). **Recreated** `BTTH_Project/CONTINUATION_PROMPT.md` from the current bible (end of Chapter 11).

## Post-cleanup workspace (authoritative files only)
```
BTTH_Project/           — THE_GENESIS_CODEX.md (post-Ch11), CONTINUATION_PROMPT.md, chapters 11
Soul_Land_3_Project/    — THE_CODEX.md v2.2, LIN_HAO_STATUS.md v4.0, CONTINUATION_PROMPT.md, chapters 1-5
CODEX/                  — 00 index · 01 universal v4.1 · 02 BTTH · 03 Marvel · 04 One Piece · 05 SL3
                          97 this log · 98 uploads archive · 99 merge report
uploads/                — empty (landing zone for future uploads)
```

**Rule going forward:** uploads are transient. On receipt, integrate into the authoritative project/CODEX file, then the upload may be archived+cleared. Never edit an upload in place.


---

# INTEGRITY AUDIT & HOUSEKEEPING — 27 August 2026

**Authorized by:** user ("please mange, save and adapt and upgrade and create and learn and update and edit, clean and others All things what needed to do")
**Method:** survey everything first → verify every suspected problem against the files before acting → fix → re-verify with the automated suites → log.

## What was actually found (verified, not assumed)

| Finding | Verdict | Action |
|---|---|---|
| `#### Personality:` / `#### Basic Information:` / `#### Appearance:` appear 3× in the SL3 codex | **NOT duplication** — they belong to three *different* character dossiers (Lin Hao / Tang Wulin / Na'er) | left alone |
| `### Draft-Quality Gate` appears 2× with different content | **Real duplication** (a 1.7 KB stub and a 2.1 KB version) | consolidated to one authoritative copy, now pointing at the automated suite |
| `CODEX/00_MASTER_INDEX.md` registry said SL3 = "Ch 1–4, Next: Ch 5" | **Badly stale** — SL3 is at ch 28 / v2.42 | registry, file map and loading order rewritten |
| `99_MERGE_REPORT.md` and the uploads archive | **Present and intact** | verified, untouched |
| `uploads/` directory | Gone (was emptied by the 24 Aug cleanup) | noted; not an error |
| SL3 chapters 1–12 had **no** end-of-chapter state record | **Real gap** — chapters written before the footer standard existed | retrofitted with rank lines + Character States, each marked "retrofit v2.42" |
| `BTTH_Project/chapters/` contains **only** `chapter_11.md` | **Real gap** — chapters 1–10 are in neither the workspace nor the archive | reported to the user; not fabricated |
| `BTTH_Project/` has no `checks/` directory | **Real gap** — no verification at all | project-agnostic suite created (`/home/user/checks_lib/verify_base.py`) |

## Structural improvements made

1. **`checks/state.py` + `checks/state.json` — single source of truth.** The current rank / spiritual power / ledger were hardcoded in **three** places across the two checkers, which is why stale-value bugs kept recurring. State is now *derived from the chapter footers* and read by both suites. Nothing is written twice.
2. **`checks/run_all.sh` now rebuilds state first**, so the suites can never check against stale numbers.
3. **`/home/user/checks_lib/verify_base.py` — project-agnostic suite.** Runs on any project regardless of chapter format: file integrity, text hygiene, repetition (prose-only, with consecutive-chapter clustering so legitimate spread use is not flagged), prose quality, scaffolding compliance, and infrastructure presence.
4. **`FANFICTION_FRAMEWORK.md`** — the method extracted for reuse on future projects.
5. **Adoption-boundary rule added to the checkers:** full-cast Character States are enforced from ch 13 (when the standard was adopted); ch 1–12 must carry *an* end-state record, not a full one. This prevents the checker from demanding a retrofit it cannot verify.

## Verification state at close

| Project | Suite | Result |
|---|---|---|
| Soul Land 3 | `Soul_Land_3_Project/checks/run_all.sh` (26 checks) | **ALL SUITES PASS, exit 0** |
| Soul Land 3 | `checks_lib/verify_base.py` | **PASS, exit 0** |
| BTTH | `checks_lib/verify_base.py` | **FAIL, exit 1 — 7 genuine gaps** (missing chapters 1–10, no canon/timeline/summary/states headers, no checks dir) |

## Checker bugs found and fixed during this pass (recorded because an ignored check is worse than none)
- the base suite's prose-split regex correctly stripped footers, but the **scaffolding check was then running on prose only** and reported "no chapter has a summary" — it now reads the full file
- the **rank-in-prose check only accepted word forms** ("rank twenty-five"), so ch 3's "rank 17" in digits read as a breakthrough that was never shown
- the **phrase-reuse check flagged any phrase in 3+ chapters**, which penalises a phrase legitimately used at its origin and later referenced — now requires 3+ *consecutive* chapters
- the **name check** flagged structural headers ("Canon Reference", "Chapter Summary") as unrecorded characters — structural strings excluded

## Nothing was deleted in this pass
Every action was additive or consolidating. The 24 Aug archive remains the only deletion record and is untouched.


---

# UPLOAD INTEGRATION — 27 August 2026 (29 files → 15 unique documents)

**Trigger:** user uploaded 29 `.md` files and said "manage, save, adapt, upgrade, create, learn, update, edit, clean."

## Handling
1. **Archived first, before any deletion** — `CODEX/98_ORIGINAL_UPLOADS_ARCHIVE_2026-08-27.tar.gz`
   (260 KB, all 29 files, integrity-verified). Nothing was lost.
2. **De-duplicated by md5.** 29 files collapsed to **15 unique documents**. One document
   (`Adaptation-Talent-Definitive-Master-Foundation-1.md`) existed in **5 identical copies**;
   `adaptation_talent_framework.md` in 3. Kept the cleanest filename of each set.
3. **Clean set placed in `CODEX/reference/`** — 15 files, zero duplicate hashes remaining.
4. `uploads/` left as the landing zone; nothing deleted from it.

## What the documents are
- **`Adaptation-Talent-Definitive-Master-Foundation-1.md`** — 4,853 lines, 7 parts, 77 sections. The
  definitive spec for the power both OCs run on.
- **`adaptation_talent_framework.md`** — the Level 0–10 / tier system; declares itself the **primary**
  reference for levels and growth, with the Master Foundation as supplementary.
- **`canon_first_oc_woven_chapter_style.md`** — a portable chapter-craft model.
- **10 reasoning engines** — adaptive depth, claim-level truth, assumption control, adversarial
  reasoning, contradiction resolution, memory firewall v3, memory integrity, decision analysis (v2+v3),
  code/technical QA.
- **2 changelogs** — v2→v3 and v3→v4 of that architecture.

## Integration performed
| Action | Where |
|---|---|
| AT spec made a **codex branch** with a full 12-point compliance audit of SL3 | `06_ADAPTATION_TALENT_SPEC.md` |
| **Conflict register created** — one supplied doc's core principle contradicts the user's PRIME LAW; resolved by the authority stack, non-conflicting parts still adopted | `07_CONFLICT_REGISTER.md` |
| 10 reasoning engines adopted as **Part 40 — Reasoning Discipline**, mapped onto the existing pipeline | `01_UNIVERSAL_CODEX.md` |
| Master index: new files added to the map, loading order updated | `00_MASTER_INDEX.md` |
| New check added: **growth-presentation variety** (AT §64.1) | `Soul_Land_3_Project/checks/verify.py` |

## Audit findings worth recording
**11 of 12 AT canon rules: SL3 already compliant** — including the two the user had to correct me on,
which the spec states independently: §61.1 *no artificial nerfing* ("Making a holder passive to preserve
canon" is explicitly forbidden) and the growth/pressure law.

**One real weakness found: AT §64.1 — "avoid the repeated upgrade formula."** I had used the same
growth presentation three times (ch 22, 23, 25: *pressure → overnight jump → arithmetic aloud → the
number*). The spec names this exact anti-pattern and prescribes nine alternatives. Now a standing
instruction and a checker rule.

**One apparent conflict resolved, not a real one:** AT §61.2 forbids "exact percentages or ranks
*without a source*." Every number Lin Hao has is produced on-page by a named in-world instrument
(the test machine, the endurance machine, the Spirit Pagoda intake plate), so both the spec and the
user's "give exact numbers" instruction are satisfied. Rule adopted: **exact numbers require a named
in-world source; if you want a new number, write the scene that measures it.**

---

# EXTRACTION PASS — 27 August 2026 (adopt what is correct, discard what is not)

**Trigger:** user — "Adopt everything that does not conflict — a partial rejection is not a rejection.
Take what is correct and delete useless things, learn what good delete what bad, you know every world
is not same."

## What was built

| New file | Content |
|---|---|
| `08_UNIVERSAL_STORY_CRAFT.md` | The world-agnostic craft, distilled from AT §§61–74 + the chapter-style model + the engines: **continuity law** (no nerfing / no unearned inflation / hard floors / trait-vs-state / breakthrough evidence) · **presentation law** (no repeated upgrade formula, growth stays large when earned, honest recovery, emotion before status) · **honest-tension law** (unknown ≠ helpless, unknown ≠ stronger) · **causality law** (canon outcomes survive only while their causes survive) · **chapter craft** · **correction protocol** · **pre-delivery audit** · **the two records** |
| `09_WORLD_SPECIFIC_SEPARATION.md` | One namespace per project. SL3 and BTTH systems tabulated side by side, with what must not leak in or out. **The Adaptation Talent is shared — but the framework itself mandates that it resolves differently in each world** ("it obeys the laws of whatever tier the user occupies") |
| `10_DISCARD_AND_SUPERSESSION_LOG.md` | What was **not** adopted, and why |
| `11_ENGINE_IMPLEMENTATIONS.md` | The three v4 components worth building, written against real failure history |

## Key findings

**1. Eleven v4 components were promised by `CHANGELOG_v4.md` and none were supplied.** Verified by
searching all 15 documents. Six are already covered by tooling that exists (the regression suite, the
state engine, the stopping policy, the knowledge ledger, dependency tracing, snapshots). **Three were
built**: USER_CORRECTION_PROTOCOL, META_ERROR_DETECTOR, EXPERIENCE_TO_RULE_COMPILER. Two were left
unbuilt for want of any specification — inventing one would violate *never invent a missing detail*.

**2. A 12-code error catalogue was compiled from this project's actual history** — E1 STALE VALUE,
E2 FROZEN LINE, E3 RECENCY TRAP, E4 SPECTATOR DRIFT, E5 CANON ERASURE, E6 RECYCLING, E7 UPGRADE
FORMULA, E8 UNSOURCED NUMBER, E9 FOOTER/PROSE SPLIT, E10 MISSING SCAFFOLD, E11 CHECKER FALSE POSITIVE,
E12 WORLD LEAK. Every code has a real example from this workspace and a prevention. Includes the
escalation ladder: **instance → pattern → rule → mechanical check.** *"A rule a human must remember
will eventually be forgotten. A check cannot be."*

**3. The rule compiler was run retrospectively.** Roughly a dozen user corrections compiled into
**15 laws and 17 checks** — tabulated in `11_ENGINE_IMPLEMENTATIONS.md` §3 with the user's own words as
the disease statement for each.

**4. Superseded, recorded not deleted:** `DECISION_ANALYSIS.md` (v2 → v3), `CONTEXT_MEMORY_INTEGRITY.md`
(v2 → firewall v3, with v2's six state classes carried forward), `CHANGELOG_v3.md` (→ v4).

**5. Rejected with reasons:** the chapter-style document's **core principle** (contradicts the PRIME
LAW; scoped to supporting OCs in ensemble serials), its **§7 Hindi cultural flavour** (world-specific
to Naagin — the *general* rule about lived detail is kept, the specific content does not travel), and
its **§8 pre-awakening restraint** (Lin Hao is powered from ch 1). AT Part V's **Ten Adaptive Orders**
and §56 were **scoped out** of current projects — both holders are far below that tier.

**6. Nothing was deleted from disk.** All 15 unique documents remain in `reference/`, and all 29
originals remain in the 27 Aug archive.

---

# BTTH CHAPTER RECOVERY — 27 August 2026

**Trigger:** user supplied the nine missing chapters ("Take them"): `chapter_01.md` … `chapter_09.md`.

## Handling
1. **Verified before installing** — confirmed BTTH (Xiao Chen appears 41/50/35× in ch 1/5/9), all nine
   md5-unique, same footer-less format as the existing ch 11.
2. **Archived** → `CODEX/98_ORIGINAL_UPLOADS_ARCHIVE_2026-08-27_BTTH.tar.gz` (9 files).
3. **Installed** into `BTTH_Project/chapters/`. The project went from 1 chapter to 10.
4. **Ch 10 is still missing.** It is recorded in the bible ("Magical Beast Mountain Range (Arrival):
   arrive, first beast encounter, set up camp") but the file was never supplied. Not fabricated.

## What the recovered chapters let me do (all previously blocked)

**1. Built `BTTH_Project/checks/verify.py`** — the project's first suite. Four checks:
rank-chain monotonicity · **world-namespace firewall** (no Soul Land / One Piece mechanics may appear) ·
canon ownership (Xiao Yan keeps the Heavenly Flame, Flame Mantra, Octane Blast and the alchemy line) ·
Adaptation Talent compliance (non-sentient, never creates from nothing).

**2. Xiao Chen's rank chain established and now enforced:**
3-Star Dou Shi (ch1) → 4 (ch2–4) → 7 (ch4) → 8 (ch5–7) → **1-Star Da Dou Shi (ch8)**, held through ch11.
Sourced from `THE_GENESIS_CODEX.md` lines 484, 490, 640, 660, 668, 688, 713 — recorded in
`BTTH_Project/checks/state.json`, never hardcoded in the checker.

**3. The Adaptation Talent audit completed — COMPLIANT on all six tests:**
never sentient ✅ · never creates from nothing ✅ · no system voice ✅ · exposure drives growth ✅ ·
pressure drives growth ✅ · a cost is paid ✅ (8 chapters). Recorded in `06_ADAPTATION_TALENT_SPEC.md`.

**4. Retrofit:** all ten chapters now carry Timeline, Chapter Summary, Character States and an
end-of-chapter rank line, each marked "retrofit 27 Aug 2026" with the bible cited as the source.

## Two real content bugs found in the recovered chapters
- **ch 5 contained a sentence copied verbatim from ch 4** — *"His black hair, deliberately messy, fell
  across his forehead as he moved with fluid grace."* Rewritten.
- **ch 5 recycled a ch 1 sentence about Xun Er** — *"At fourteen, she would be the second youngest in the
  clan's history to do so."* Rewritten to acknowledge her progress rather than repeat the record.

## One checker false positive found and fixed
The world-namespace check matched **"Haki" inside "s***haki***ng"** in three chapters. Word boundaries
added. This is the twelfth false positive recorded — the rule stands: **verify every check against a
known-good passage before trusting it.**

## Final state
| Suite | Result |
|---|---|
| SL3 `checks/run_all.sh` (27 checks) | **PASS, exit 0** |
| SL3 `verify_base.py` | **PASS, exit 0** |
| BTTH `checks/verify.py` | **PASS, exit 0** |
| BTTH `verify_base.py` | **FAIL, exit 1 — one real gap: chapter 10 missing** |


---

# SPIRIT SOUL GROWTH — 27 August 2026 (the fifth progression line)

**Trigger:** user — *"I don't understand why his hawk not grow with him and struck, you don't his growth
you should… i now think logically when his soul spirit evolve it's also gain lighting attribute. Okay
everything others create yourself."*

## The bug, verified
The Gale Hawk went 700 (ch4) → 750 (ch7) → 760 (ch10–13) → 770 (ch22) → **frozen for six chapters**.
The last movement was **+10 years during a three-week period**, then nothing across months that
included a tournament, class zero, the platform, twelve wolves and a thousand-year bear. The codex's own
growth engine says the AT "feeds it continuously." **This was error class E2 (FROZEN LINE) on a line
nobody was auditing** — the four progression lines were rank, spiritual power, swordsmanship and
blacksmithing; the soul spirit was a fifth that nobody watched.

## What was built
- **`CODEX/12_SPIRIT_SOUL_GROWTH.md`** — the growth law, the rate table (idle / training / heavy
  combat), the mutation ladder, and the age chain.
- **`checks/verify.py` check 15 — SOUL SPIRIT GROWTH.** Age must never decrease, must never reach 1,000
  before the gated crossing, and **must not be stated at the same value in 3+ chapters.** The four-line
  rule is now a **five-line rule**.
- **THE LIGHTNING CROSSING (the user's idea, made lawful):** the hawk gains a **lightning attribute at
  900 years**. Lawful because the codex already gives the *martial soul* wind **+ lightning**, and the
  hawk was restructured by the sword's essence during absorption — so the lightning was always latent in
  it. **The hawk is catching up to the sword; wind alone is not a storm.** It is **not** a third ring:
  the third ring still requires the 1,000-year purple crossing, so the rank-30 wall is preserved — and
  is now *better*, because the wall has a face the reader can watch approach.

## The retrofit, and what it exposed
Rewriting the chain surfaced **a second freeze nobody had noticed: the hawk was stated at 700 years in
ch 4, 5 *and* 6.** Both freezes are now fixed. Verified chain:

**700 (ch4) → 720 → 735 → 750 → 760 → 770 (ch13) → 800 (ch15) → 815 → 825 → 840 (ch21) → 845 → 852 →
862 (ch25) → 870 → 874 → 878 → 885 (ch29).** Strictly increasing, no value repeated three times.

**15 years to the Lightning Crossing, 115 to the purple crossing.** The ch 29 seed is already in the
prose: *"for the first time he thought he could smell rain in it that was not there."*

## Six checker bugs found while building check 15 (all fixed)
1. An f-string evaluated `max()` on an empty list and **crashed the suite**.
2. The number-word table had no entries past 267.
3. The age parser tried `"N hundred years"` before `"N hundred and X years"`, so **815 read as 800**.
4. **"fifteen" was in neither the TENS nor ONES map**, so it parsed as 0 — replaced with a real parser
   including TEENS.
5. The finditer alternation matched the short form first.
6. **The regex was case-sensitive**, so every age at the start of a sentence ("Eight hundred and…") was
   invisible.

Plus two prose corruptions I introduced while retrofitting and then caught: a replacement dropped the
word "years" in three places, and one substitution produced *"hawk was eight hundred and seventy-eight
old"*. Both fixed.

**Lesson recorded:** when a check needs patching three times, stop patching and rewrite it. Check 15 was
rewritten paragraph-scoped rather than window-scoped, which removed the whole class of
keyword-outside-the-window bugs at once.

---

# PHYSICAL PANEL — 27 August 2026 (the line everyone forgets)

**Trigger:** user — *"you completely ignore them like strength, speed, agility, senses, durability and
reliability and others All things, this things increases more than spiritual power normally… spiritual
power not fight, body fight in real world."*

## Verified: the user is right, and the AT canon says so independently
- The codex power snapshot tracked **one** physical number (fist/endurance) and **nothing else** — no
  strength, speed, agility, senses, durability, recovery, stamina, reflex or reliability.
- **AT §73** lists *"Adaptation Talent is basically fast learning"* as a **WRONG PORTRAYAL**, because
  the Talent *"develops the complete holder across body, mind, soul, identity, energy, powers,
  resistance."*
- **AT §69** requires panel fields for capacity/output, **immediate physical condition**, **resources,
  reserves, debts, injuries**, **current adaptive priorities** and **natural body foundation**.

## Why physical lines grow faster than the energy stat
The energy stat is **one subsystem**; the body is the **primary target**. Every fight, every hour at the
anvil and every hit taken stresses muscle, bone, tendon, nerve, sense organ and recovery **directly**,
while spiritual power only receives indirect feedback. **A panel tracking only the energy stat is
tracking the slowest line and calling it the whole holder.**

## What was built
- **`CODEX/13_PHYSITICAL_PANEL.md`** — ten physical lines, each labelled **Measured / Established /
  Unmeasured / Unknown** with its source, plus immediate condition and current adaptive priorities.
- **The progression lines went from four to six** (adding the hawk and the physical panel) in
  `THE_CODEX.md`, `LIN_HAO_STATUS.md` and `FANFICTION_FRAMEWORK.md` §5.
- **`checks/verify.py` check 16 — PHYSICAL PANEL:** every one of the ten lines must be present in the
  panel (so none can be silently dropped again), the measured anchor must be present, and **the 186 kg
  hard floor may never be under-performed in prose (AT §61.4)**.

## The honest finding the panel exposes
**The panel has one measured number in ten lines.** The real problem is not that the stats are low — it
is that **nobody has ever tested him.** Nine lines are established with a floor and no number. So the
panel does not invent numbers; it records what is true and marks the rest unmeasured, and the obvious
story consequence is a **full physical assessment**, after which every line gets a real number and a
hard floor.

## One defect recorded, not smoothed over
**The Unnamed Stroke cannot be summoned on purpose** ("I looked like a man swatting a bee"). It is now a
tracked weakness in the panel under **Reliability**, because a status panel with no defects is a
advertisement, not a record.

---

# TECHNIQUES, CULTIVATION SPEED & THE SPECIALTY — 27 August 2026

**Trigger:** user — *"Spiritual power is not his speciality, his everything balanced and High and over
all is his speciality, you also forgot his cultivation speed, his techniques and others."*

## Verified
- **Cultivation speed** appeared **once** in the codex and **zero** times in the status file.
- **Techniques** existed as prose descriptions with **no proficiency tracking** — no way to tell whether
  a skill had advanced since it was introduced.
- The power snapshot framed **spiritual power as his headline number**, which is wrong for this power.

## The reframing (the important part)
**Spiritual power is NOT his speciality.** The rivals prove it: Wang Jinxi has strength and **18**
spiritual power. Xie Xie has speed and average power. Gu Yue has **153** at ten. **Lin Hao has no spike
— he has a plateau, and the plateau is above everyone else's.**

AT §73 supports this: the Talent *"develops the complete holder"* and removes weaknesses, so **the
signature of an Adaptation Talent holder is not a high number — it is the absence of a low one.**

**Standing writing rule:** never introduce him by his biggest number; introduce him by the thing that
has no answer. One genuine defect is recorded (Reliability — the Unnamed Stroke) so the panel stays a
record rather than an advertisement.

## Built
- **`CODEX/14_TECHNIQUES_AND_SPEED.md`** — nine techniques placed on **AT canon §27.1's six-layer
  mastery ladder** (Perception → Understanding → Reproduction → Conditioning → Applied mastery →
  Creative mastery): Grain Cut **5**, The Question **5**, Gale Talon **5**, Wind-Step **5**,
  Answering Stroke **4**, One Sentence **3→4**, Open Hand **2**, **Unwritten Stroke 3-in-the-moment /
  1-afterwards**, Union **0 (locked)**. Plus cultivation speed: **20 ranks in ~4 years (~5/yr),
  accelerating under pressure, ~13 ranks ahead of canon's protagonist at the same age** — and the
  distinction that he is **stalled by the wall, not slowed**.
- **`verify.py` check 17** — all nine techniques must be on the ladder, cultivation speed and the
  specialty framing must be present, and **any document that regresses to "spiritual power is his
  speciality" fails the suite.**
- `FANFICTION_FRAMEWORK.md` §5 extended with the techniques panel, cultivation speed and **the
  SPECIALTY RULE**.

## A real contradiction this exposed and fixed
The codex stated **twice** that *"lightning strikes become more potent as soul rank increases."* The
chapters say rank has been static at 30 since ch 22, while the lightning only arrived at ch 30 **from
the hawk's crossing**. **Resolution: the lightning scales with the hawk, not the rank** — the sword and
spirit soul have fed each other since absorption. So **the lightning climbs while the rank waits**,
which is consistent and is exactly the compressed-spring reading. Both codex lines corrected.

## Complete-holder coverage now
Rank · Energy · **Physical (9 lines)** · **Spirit soul** · **Techniques (9, six-layer ladder)** ·
**Cultivation speed** · Craft · Mind. **Nothing about the holder is untracked.**


---

# DISCARD AND SUPERSESSION RECORD (merged from branch 10, 27 Aug 2026)

**Principle:** taking what is correct means also being willing to leave things out. Everything discarded
is recorded here so the decision is not silently repeated or silently reversed. Nothing was deleted from
disk — all originals remain in `reference/` and in the 27 Aug archive.

## 1. SUPERSEDED — kept in `reference/` but no longer authoritative

| Document | Superseded by | Note |
|---|---|---|
| `DECISION_ANALYSIS.md` (v2.0) | **`DECISION_ANALYSIS_v3.md`** | v3 adds downside analysis, second-best analysis, and explicit risk tolerance. **Use v3.** v2 is redundant. |
| `CONTEXT_MEMORY_INTEGRITY.md` (v2.0) | **`CONTEXT_MEMORY_FIREWALL_v3.md`** | v3 adds the priority order and the project namespace rule. The one thing v2 has that v3 lacks — the six **state classes** (CURRENT_REQUEST / ACTIVE_CONTEXT / PERSISTENT_PREFERENCE / EXTERNAL_FACT / ASSUMPTION / UNKNOWN) — has been **carried into v3's usage** rather than lost. |
| `CHANGELOG_v3.md` | **`CHANGELOG_v4.md`** | v4 is the later architecture. Both retained as history only; neither is operative. |

---

## 2. PROMISED BUT NEVER SUPPLIED — a real gap

`CHANGELOG_v4.md` names **eleven** components. **None of them were supplied as documents.** Verified by
searching all 15 files on 27 Aug 2026.

| Promised component | Status | Action taken |
|---|---|---|
| `USER_CORRECTION_PROTOCOL` | ❌ not supplied | **Implemented** → `11_ENGINE_IMPLEMENTATIONS.md` |
| `META_ERROR_DETECTOR` | ❌ not supplied | **Implemented** → `11_ENGINE_IMPLEMENTATIONS.md` |
| `EXPERIENCE_TO_RULE_COMPILER` | ❌ not supplied | **Implemented** → `11_ENGINE_IMPLEMENTATIONS.md` |
| `SKILL_KERNEL_v4` | ❌ not supplied | Not built — undefined scope, no spec to implement against |
| `DEPENDENCY_GRAPH_AND_IMPACT_ANALYSIS` | ❌ not supplied | Partially covered by §68 step 3 ("trace downstream effects") |
| `STATE_SNAPSHOT_ROLLBACK` | ❌ not supplied | Partially covered by `checks/state.py` + chapter footers |
| `CHARACTER_KNOWLEDGE_LEDGER` | ❌ not supplied | Covered in practice by the per-chapter **Character States** footers |
| `REGRESSION_SUITE_v4` | ❌ not supplied | **Already exists and is better specified** — `checks/verify.py`, `verify2.py`, `checks_lib/verify_base.py` |
| `STOPPING_AND_ESCALATION_POLICY` | ❌ not supplied | Covered by `ADAPTIVE_REASONING_DEPTH` de-escalation rule |
| `QUALITY_CALIBRATION_MATRIX` | ❌ not supplied | Not built — no spec |
| `STORYOS_REGRESSION_AND_STATE_ENGINE_v4` | ❌ not supplied | Covered by the state file + drift check |

**Six of eleven are already covered by tooling that exists.** Three were worth building and have been.
Two were left unbuilt because there is no specification to build against — inventing one would violate
*never invent a missing detail*.

---

## 3. REJECTED — supplied, read, and deliberately not adopted

### 3.1 `canon_first_oc_woven_chapter_style.md` — core principle and §7–8

| Element | Verdict | Reason |
|---|---|---|
| **Core principle** — "the OC is a parallel thread, never the centre" | ❌ **REJECTED for co-lead protagonists** | Directly contradicts the user's PRIME LAW and "he should DOMINATE his own matches." The document was written for an ensemble serial with a supporting OC. See `07_CONFLICT_REGISTER.md`. |
| **§7 Hindi cultural flavour** (puja, mantras, *beta/sahib*) | ❌ **REJECTED as universal** | World-specific to Naagin. Soul Land 3 is a Chinese setting; BTTH likewise. **The general rule is kept** — cultural flavour through lived detail, not heavy romanised dialogue — but the specific content does not travel. |
| **§8 Restraint on OC powers before awakening** | ❌ **REJECTED for SL3** | Lin Hao is fully powered from chapter 1. Kept as a rule for any future project with an unawakened OC. |
| §1, §4, §5, §6, §9, §10, §12 | ✅ **ADOPTED** | See `08_UNIVERSAL_STORY_CRAFT.md` §E. |

### 3.2 Adaptation Talent Master Foundation — scoped, not rejected

| Element | Verdict |
|---|---|
| **The Ten Adaptive Orders** (Part V, §§45–55) | ⚠️ **SCOPED OUT of current projects.** A high-tier taxonomy (Causal, Existential, etc.) for holders far above mortal/supernatural tier. Neither Lin Hao nor Xiao Chen is near it. Retained in `reference/` for when a project needs it. |
| **§56 death, clones, reincarnation, cross-world translation** | ⚠️ **SCOPED OUT.** Not currently relevant to any active project. |
| **§§32–44 the holder's complete existence** (prenatal development, healing, scars, psychology) | ⚠️ **PARTIALLY USED.** SL3 uses prenatal development and the bone mutation; the rest is retained for reference. |
| **§§1–60 the operating architecture** | ✅ **ADOPTED as canon** — `06_ADAPTATION_TALENT_SPEC.md`. |
| **§§61–74 story-use rules** | ✅ **ADOPTED as universal craft** — `08_UNIVERSAL_STORY_CRAFT.md`. |

### 3.3 Reasoning engines — all adopted, one narrowed

| Document | Verdict |
|---|---|
| All ten engines | ✅ **ADOPTED** as Universal Codex Part 40 |
| `CODE_TECHNICAL_QA.md` | ✅ Adopted, **narrowed in scope** — it is about programming, not prose. Applies to the check scripts and any code, not to chapters. |

---

## 4. DISCARDED AS DUPLICATES

29 uploaded files → **15 unique documents**. Fourteen files were byte-identical copies:
`Adaptation-Talent-Definitive-Master-Foundation-1.md` ×5, `adaptation_talent_framework.md` ×3, and nine
documents ×2. The cleanest filename of each set was kept. **Nothing was lost** — all 29 originals are in
`98_ORIGINAL_UPLOADS_ARCHIVE_2026-08-27.tar.gz`.

---

## HOW TO USE THIS LOG

Before adopting any newly supplied document:
1. Check whether it is superseded by something already held.
2. Separate its **universal** content from its **world-specific** content.
3. Adopt the universal; namespace the world-specific; reject and record the rest.
4. **A partial rejection is not a rejection** — record what was kept.
5. Never delete the original. Archive it.

---

# CONSOLIDATION — 27 August 2026 (stop creating files; merge into the owners)

**Trigger:** user — *"Don't create too many things put everything into there, Codex into codex, stutas
into stutas and others All, delete extra files and others things."*

## The problem
Eleven extra files had accumulated — nine `CODEX/06–14_*` branch files plus `FANFICTION_FRAMEWORK.md`
and `README.md` at the top level. Every new idea was getting its own file, which meant the same
information lived in several places and nothing was authoritative.

## Where each file went

| Deleted file | Merged into |
|---|---|
| `06_ADAPTATION_TALENT_SPEC.md` | `Soul_Land_3_Project/THE_CODEX.md` → **Part A** |
| `12_SPIRIT_SOUL_GROWTH.md` | `Soul_Land_3_Project/THE_CODEX.md` → **Part B** |
| `13_PHYSICAL_PANEL.md` | `Soul_Land_3_Project/LIN_HAO_STATUS.md` → **The Complete-Holder Panel** |
| `14_TECHNIQUES_AND_SPEED.md` | `Soul_Land_3_Project/LIN_HAO_STATUS.md` → **Techniques, Cultivation Speed & the Specialty** |
| `FANFICTION_FRAMEWORK.md` | `CODEX/01_UNIVERSAL_CODEX.md` → **Part 41 — The Fan-Fiction Method** |
| `08_UNIVERSAL_STORY_CRAFT.md` | `CODEX/01_UNIVERSAL_CODEX.md` → **Part 42** |
| `09_WORLD_SPECIFIC_SEPARATION.md` | `CODEX/01_UNIVERSAL_CODEX.md` → **Part 43** |
| `07_CONFLICT_REGISTER.md` | `CODEX/01_UNIVERSAL_CODEX.md` → **Part 44** |
| `11_ENGINE_IMPLEMENTATIONS.md` | `CODEX/01_UNIVERSAL_CODEX.md` → **Part 45** |
| `10_DISCARD_AND_SUPERSESSION_LOG.md` | `CODEX/97_CLEANUP_LOG.md` → Discard Record |
| `README.md` | `CODEX/00_MASTER_INDEX.md` → Workspace Orientation |

## Safety
- **All eleven originals archived first** → `CODEX/98_BRANCH_FILES_ARCHIVE_2026-08-27.tar.gz`
  (34,795 bytes, integrity-verified, all 11 present) **before** anything was deleted.
- A content check ran twice and **refused to delete** on the first pass, flagging intro blockquotes and
  cross-references. The substantive ones (the conflict register's authority-stack rationale, the discard
  record's principle, the panel's tracked-line note) were merged into their destinations; the rest were
  obsolete file subtitles like *"Codex branch 06"* and *"Companion to `13_PHYSICAL_PANEL.md`"*, which are
  meaningless once merged.
- **15 dead references updated** across five live files. The **historical upgrade log was deliberately
  left untouched** — it records what was true at the time.
- **The branch-integrity check caught stale rows in the master index after the deletion** and failed the
  suite until they were fixed. That is the check earning its place.

## Final structure — one owner per kind of thing
```
CODEX/
  00_MASTER_INDEX.md      the map + workspace orientation
  01_UNIVERSAL_CODEX.md   ALL process: Parts 1-38 + 39 Mechanical Verification, 40 Reasoning
                          Discipline, 41 Fan-Fiction Method, 42 Story Craft, 43 World Separation,
                          44 Conflict Register, 45 Engine Implementations
  02–04_PROJECT_*.md      the other project bibles
  05_PROJECT_SOUL_LAND_3.md   mirror of the SL3 bible
  97_CLEANUP_LOG.md       all cleanup + the discard record
  98_*.tar.gz             four archives — never delete
  99_MERGE_REPORT.md
  reference/              the 15 supplied source documents
Soul_Land_3_Project/
  THE_CODEX.md            story facts + Part A (AT spec) + Part B (hawk growth)
  LIN_HAO_STATUS.md       the holder: rank, energy, physical panel, techniques, speed, craft
  CONTINUATION_PROMPT.md  the standalone brief
  chapters/  checks/
BTTH_Project/
  THE_GENESIS_CODEX.md  CONTINUATION_PROMPT.md  chapters/  checks/
checks_lib/verify_base.py   shared project-agnostic suite
```
**No loose files at the top level. Codex in the codex, status in the status, process in the universal
codex.**

## Verification after consolidation
`SL3 run_all.sh` (30 checks) exit 0 · `SL3 verify_base` exit 0 · `BTTH checks/verify.py` exit 0 ·
mirror identical. (`BTTH verify_base` still exits 1 for the one known gap: chapter 10 missing.)

---

## CLEANUP 27 Aug 2026 (pass 2) — user: "clean up seriously needed"

**Method: nothing deleted on filename alone. Every removal verified by sha256 or diff first.**


### What was removed

| Item | Count | Verification before removal |
|---|---|---|
| `uploads/*.md` duplicates of `CODEX/reference/` | **29** | `diff -q` byte-identical, then sha256 for the last 3 |
| `uploads/chapter_01–09.md` superseded BTTH drafts | **9** | **Archived, not deleted** — they differ (3,802 vs 3,946 words) |
| `canon_extract/_raw*.txt`, `_joined*.txt` scratch | **6** (2.3 MB) | Regenerable from the PDFs via `ingest.py` |

### What was deliberately kept
- **The 6 source PDFs in `uploads/`** — irreplaceable canon source. Never delete these.
- **All 5 `CODEX/*.tar.gz` archives** — they are the only copy of several superseded documents.
- **`CODEX/reference/`** — 15 de-duplicated source documents, already clean.

### Verification after cleanup
- `sh checks/run_all.sh` → **exit 0**, all three layers.
- Canon intact: **307 chapter files, 448,375 words.**
- `ingest.py` re-run against a source PDF with the scratch files gone → still extracts correctly.

**Workspace: 24 MB, 411 files** (was 454 files, 28 MB).

## 2026-08-28 — workspace reduced to Soul Land 3 only

User instruction: *"delete others project then soul land 3 only soul' land 3 remain."*

**Archived to `CODEX/98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz` (20 entries, verified recoverable),
then removed:**
- `BTTH_Project/` — *Battle Through the Heavens: The Adaptive Cousin*, 11 chapters
- `CODEX/02_PROJECT_BTTH.md`
- `CODEX/03_PROJECT_MARVEL_COSMIC.md` — *The First Triune*, 2 chapters
- `CODEX/04_PROJECT_ONE_PIECE.md` — *One Piece: Kai*, 7 chapters

**Also removed:** stray `__pycache__` directories.

**Deliberately KEPT:**
- `uploads/` — the seven source canon PDFs. 🔒 Never delete; they are the only copy.
- `canon_extract/` — 313 canon chapters + `ingest.py`.
- `checks_lib/verify_base.py` — referenced by `THE_CODEX.md`; the project builds on it.
- `CODEX/reference/` — the Adaptation Talent foundation is Lin Hao's martial soul spec, not another project.
- `CODEX/01_UNIVERSAL_CODEX.md`, `consequence.py`, `CONSEQUENCE_RULES.md`,
  `CONSEQUENCE_REGISTRY.md`, `DECISION_JOURNAL.md` — the thinking tools.
- `FANFICTION_FRAMEWORK.md` — the reusable method.
- All `98_*.tar.gz` archives.

**Verified before deleting:** the archive was listed with `tar tzf` and contained 20 entries
including every BTTH chapter file. Restore with:
`tar xzf CODEX/98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz -C /home/user`

**Also verified this session:** `uploads/soul' land 100 to 135.pdf` was ingested — 34 chapters,
range 99–135, **0 new**. It does not contain canon ch 28, which remains the only missing chapter.

## 2026-08-28 (same session) — perfection pass on the existing 61 chapters

User instruction: *"no next chapter for now, you should perfect chapter's you created already."*

**F1 CLOSED.** The purple-ring soul-skill evolution is now on-page in **ch40**, in the chapter where
the rings actually turn purple: Lin Hao lays the same Gale Talon he has laid four hundred times,
changes nothing, and a thirty-metre deadfall comes apart instead of opening. Gu Yue frames it
(*"your skill didn't improve, it got **older**"*); the Spirit Pagoda witness dates it against
Wu Zhangkong's own; the cost tripled and was not chosen. Hawk-Soul Union is felt larger but stays
reserved per decision **D006**. `PROBLEM_INVENTORY.md` and premise **P001** both closed.

**Abandoned threads revived** in ch60 and ch61: **Na'er** (the reason Wulin is actually going to
Shrek — *"it is further inland than this"*), **the ledger** (107, and why the number stopped being
the interesting thing), **the question** (still open, and he has been waiting to be asked rather
than asking).

**Four checks were wrong, not the prose:**
- `verify.py` NAMES reported chapter-title fragments (`What Lin Hao Wrote` → "Hao Wrote") as unknown
  characters. Now excludes anything appearing in a heading.
- `verify2.py` CONT read the generated ensemble block as prose and reported seven phantom scene
  breaks. Now strips it.
- `verify2.py` QUAL flagged "sentences over 95 words" — the book's own distribution says that is
  0.1% of sentences and is the style. Recalibrated to 110 with the measurement in the source.
- `verify_ensemble.py` kept warning about F1 after F1 was written. It now detects the evidence.

**Remaining warnings (32) are deliberate:** 8 short chapters (1,474–1,950 words — padding them would
make them worse), ~9 long journal sentences (the style), 7 scene-cut transitions (ch9→10 opens a week
later), 4 thread gaps in progress, 1 Prime-Law count in ch32 (9 prose mentions vs a 10 threshold),
and 2 canon-anchored ensemble plateaus (Wulin's 23-chapter hold at rank 15 = canon c133; Gu Yue's
21-chapter hold at 19 = canon c133).

**`sh checks/run_all.sh` → exit 0, all six layers pass.**

## 2026-08-28 (later) — uploads/ archived after verifying the extraction

User instruction: *"When you already canon extracted then delete from uploads because there is no
meaning things remind two."*

**Verified BEFORE removing anything**, and the verification found two real problems:

1. **`canon_061.txt` was EMPTY (0 bytes).** The chapter *was* in `soul land 3 novel chapter 51 to 99.pdf`
   but sits **out of order** in it — the marker sequence runs 59, 60, 62, 63, 64, **61**, 65 — so the
   linear ingest wrote a 0-byte file and reported the chapter as merely "MISSING". **Recovered by
   direct extraction: canon ch 61 = "Beat Me and I'll Act Dignified", 7,352 chars.** The corpus now has
   **zero empty files**.
2. **Chapters 1–22 are not in the corpus and are not in any PDF.** The earliest PDF starts at ch23.
   Those 22 chapters exist only as text pasted earlier in the conversation, and in fragments quoted in
   `THE_CODEX.md`. **`uploads/` never contained them**, so removing `uploads/` did not lose them — but
   they are still missing from the corpus, and no amount of re-extraction will produce them.

**Action:** `uploads/` (18 MB, 7 PDFs) archived to **`CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz`**
(13.6 MB, 7 entries, verified with `tar tzf`), then removed from the working tree.

**Not a straight delete, and why:** the extraction is *demonstrably* incomplete — it missed ch61 for
months and still lacks ch28 and ch1–22. Deleting the only source would have made those permanently
unrecoverable, and `ingest.py` needs the PDFs to run at all. The archive gives the user what they asked
for (no duplicate in the working tree, 18 MB freed) without destroying the only copy.

Restore: `mkdir -p uploads && tar xzf CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz -C uploads`

**Corpus state after this pass:** 313 chapter files, 0 empty, range 23–336, gaps at **28** only.

## 2026-08-28 (final) — chapter perfection pass, part 2

User instruction: *"Do what you want to do everything."* Chose the one remaining item that would
actually change the reading: expanding the short chapters with real scenes rather than padding.

**Expanded, all with genuine new material:**
- **ch43** 1787 → **2332** — wrote the scene the chapter had set up (*"Wulin will take it well, and that
  will be worse"*) and never shown: Wulin absorbing it without a seam, Xie Xie going to clean his
  daggers at nine in the morning, Gu Yue's *"it is a fact about weather."*
- **ch44** 1733 → **2029** — Wulin bringing two bowls; Xie Xie telling everybody about the nine seconds
  *"like it's a number"*; Xie Xie standing at the other end of Gu Yue's corridor.
- **ch46** 1850 → **2243** — Wulin's mother's stone in a yard, not a cemetery; Xie Xie going to stand
  near a wall.
- **ch48** 1811 → **2097** — Wulin and the five million; *"five million is four hundred and sixteen
  Fridays."*
- **ch54** 1474 → **2061** — the real cost of the Track: his gift for reading got in his own way for
  nine days; and Wulin, who knew what he needed and didn't do it unless asked.
- **ch56** 1927 → **2004** — Gu Yue's observation written into the journal properly.

**Continuity errors found and fixed while doing it:**
- **ch44 and ch45 said "the six of them"** — only five students existed at that point (Wang Jinxi gone
  in ch43, Xu Xiaoyan not arrived until ch52). Fixed in four places.
- **ch56 said "the six of us"** in the tournament chapter. Fixed.
- **Xu Lizhi was introduced in ch43** — he does not appear until ch55. Beat given to Zhang Yangzi,
  who is actually there and has more claim to it.
- **Wulin had ZERO prose mentions in ch57** and near-zero in ch58. Restored in both, doing something
  in character.

**🔴 New lesson, recorded as §4.9 in the framework:** expanding a chapter lowers every character's
mention *density*, so fixing a length warning can trip a presence check. Both times this fired, the
underlying absence was real. Rule: strengthen the cast inside the new material rather than adding
scenery.

**Result:** 61 chapters, **200,449 words**, no chapter under 1,964 words, **zero short-chapter
warnings** (was 8). Total warnings **32 → 16**. `sh checks/run_all.sh` → **exit 0, all six layers pass.**

## 2026-08-28 (maintenance pass) — save / adapt / upgrade / update / edit / clean

**Saved & synced:** state.json regenerated from the footers · all 61 ensemble blocks rewritten ·
LIN_HAO_STATUS.md and CONTINUATION_PROMPT.md regenerated · THE_CODEX, RELATIONSHIPS and
CHARACTER_STATS mirrored to `CODEX/` and `CODEX/reference/`.

**Fixed:**
- `RELATIONSHIPS.md` still carried **"Gu Yue — Canon romance, eyes only for Tang Wulin"** in *two*
  places. One of my earlier replacements had silently failed (pattern mismatch, `old not in s`, script
  moved on). Both now say the truth: **zero romantic mentions across 61 chapters; everything runs
  toward Lin Hao.**
- `SL4_RESEARCH.md` now states plainly that **Soul Land 4 is a NEW OC**, that **Lin Hao is not dead**,
  and that the connection is 🔓 undecided.

**Upgraded — new check, `verify_ensemble.py` §7d:** nothing may write or imply Lin Hao's death, in any
chapter or tracking document. **Calibrated against six false positives** before it was trusted: the
first version fired on *"the grave, solemn face of a man delivering a eulogy"* (a joke), *"a dead man's
record"* (Long Bing), *"a dead thing the size of a house"* (a soul beast) and *"canon's Xie Xie is
nearly killed."* **Other people are allowed to die.** Probe-tested both directions.

**Cleaned:** archived to `CODEX/98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz` (3 entries, verified) and
removed —
- `REBUILD_PLAN.md` (a plan for 37 chapters; there are 61, and the work is done)
- `CONTINUATION_PROMPT_ARCHIVE_ch28.md` and `LIN_HAO_STATUS_ARCHIVE_ch18.md` (both misnamed — both
  actually contained ch49-era content, which was its own small confusion)

**Learned — recorded as `FANFICTION_FRAMEWORK.md` §4.11, THE EXTRAPOLATION FAILURE:** four separate
corrections in one day turned out to be one mistake made four times. *I take one thing the user says and
add two or three things that "belong" to it — and the additions are always sadder, smaller, or more
convenient than what was actually said.* Including killing the protagonist to make a sequel connection
feel poignant. The discipline is now written down: quote the user verbatim above every locked law,
never decide a fate to make a payoff land, grep the AU before importing canon into it, and prefer the
bigger reading.

**`sh checks/run_all.sh` → exit 0, all six layers pass.**

## 2026-08-28 (full workspace audit) — "check everything every single word"

**Audited:** 427 files · all Python compiles · 61 chapters (no gaps, no dupes, none small) · 313 canon
files (only gap: ch28, absent from the source PDFs) · 8 archives (all valid, 105 entries total) ·
3 mirrors (all identical) · suite exit 0, six layers pass.

**Real errors found and fixed:**

1. 🔴 **Fourth rank was still called "Master Craftsman" in five places** — ch53's header, two of its
   prose lines, its footer, ch57's prose line, and the ch53 codex record. Canon c40: 3rd–4th is
   **Grandmaster**; Master Craftsman is 5th–6th. **My earlier fix claimed "all corrected" and was
   wrong** — it searched for one phrasing and missed the variants. Lesson recorded: *search for the
   FACT, not for the sentence you remember writing.*

2. 🔴 **`checks/build_status.py` had the retracted claim hardcoded.** The generated status file said
   *"Gu Yue… she cannot beat him"* on every regeneration — but he says at ch53 and ch58 that she has
   beaten him five times. The generator also still listed **F1 as unwritten** after it was written.
   Both fixed at the source, and the block now carries a warning that it is hardcoded prose and has
   gone stale twice.

3. **`LIN_HAO_STATUS.md` pointed at a deleted archive** (`LIN_HAO_STATUS_ARCHIVE_ch18.md`). The
   generator's preamble was fixed so it can't happen again.

4. **24 broken file references in live documents** repointed — branch files 12/13/14 (merged into
   `LIN_HAO_PANELS.md`), 06–11 and `THE_GENESIS_CODEX.md` (merged/archived), `REBUILD_PLAN.md`
   (archived), and the three removed project bibles. The 12 remaining references are all inside the
   upgrade log or the "Removed" list, where they are history and belong.

5. **`RELATIONSHIPS.md` still carried "Gu Yue — Canon romance, eyes only for Tang Wulin" in two
   places.** One earlier replacement had silently failed (pattern mismatch; the script printed nothing
   and moved on). Scripts now assert their patterns instead of skipping quietly.

**Verified clean:** no live file contains "long after he is dead", "means nothing to anyone but him",
"Canon romance", "全衡战系", or "Divine Stormbringer" as a *live* claim — every remaining occurrence is
a retraction record or a cancel-rule, which is what those strings are for.

## 2026-08-28 (second pass) — canon extended to ch 600, and a real hole closed

**Saved.** Two new PDFs ingested (337–485: 149 ch · 486–600: 115 ch), archived to
`CODEX/98_CANON_SOURCE_PDFS_337-600_2026-08-28.tar.gz`, `uploads/` removed. **Corpus: 577 files,
23–600, 5.0 MB, zero empty, only gap ch 28.** `INDEX.txt` rebuilt with 577 entries.

**Upgraded — `ingest.py` had two bugs, both found by this ingestion:**
1. The header regex **required a dash** (`Chapter N - Title`). From ch512 the PDF drops the dash, so the
   tool found **54 chapters in a file containing 115 with zero gaps** and reported the other 61 as
   *"MISSING from this PDF."* **The dash is now optional.**
2. Split point and body start were the same position. Fixing (1) with "first header wins" then left
   **~100 characters of site navigation furniture on top of all 577 chapters.** Now: **split on the
   first header, body from the last.** Caught by spot-checking ch23 rather than trusting the success
   message.
   🔴 **Rule added: never believe a "MISSING from this PDF" report until the raw marker count has been
   compared against it.**

**Learned — and this is the important one. `THE_CODEX.md` now has §SOUL POWER COMPRESSION.**

The story has claimed for thirty chapters that Lin Hao's effective combat power is **Soul King** while
his rank is 36, and **never once said how.** "The Adaptation Talent" explains why he *grows* fast; it
does not explain why a ranked-36 body hits like a ranked-55 one. **That was a hole, and canon has the
answer:**

> *"they **compressed their soul power** so that a denser, more potent form of the energy filled them"*
> *"**The value of compressed soul power became more apparent with strength.**"*
> *"the root of the issue lay in the **difficulty in compressing soul power**"*

Compression is why the gap exists, **and** it is the bottleneck — which retroactively explains the
ch22–39 rank stall far better than "the ring count caps it."

**And a canon benchmark far sharper than anything we had invented — YUANEN YEHUI:**
> *"She's only **fifteen**, yet she's now **rank 40**! **I can't even dream of reaching rank 40 by the
> age of fifteen!**"* — on a girl with **three purple soul rings and two martial souls**, treated as
> once-in-a-generation.

Canon's greatest prodigy: **rank 40 at fifteen, three purple rings.** Ours goes **40 → 45 at eleven with
three purple rings.** A real canon figure beats an invented yardstick, and the reader can feel the size
of the gap. Canon also uses the word **"domineering"** for an overwhelming soul skill, which supports
the DOMINEER naming.

**⚠️ Recorded as a limit: ch 600 is NOT the ending.** At 600 Wulin and Gu Yue are travelling in a
foreign land at a blacksmith's counter. **Soul Land 3 continues past 600 and we do not have the rest.**
No chapter may assume the ending is known. **264 chapters (337–600) are skimmed, not read.**

**Cleaned.** `uploads/` removed after verifying its archive. Regenerated state, ensemble blocks, status
and continuation; all three mirrors re-synced.

**`sh checks/run_all.sh` → exit 0, all six layers pass.**

## 2026-08-28 (third pass) — LAYER 7 built, and a fabricated canon quote found

**🔴 Built `checks/verify_canon_quotes.py` — LAYER 7.** Every string a chapter header attributes to
canon is now checked against all 577 extracted canon chapters. **Nothing ever checked these before.**
Result: **50/50 verified.** Probe-tested — a planted fake quote is caught.

**It immediately earned its place:**

1. **ch38 carried a fabricated canon quote.** The header claimed canon said the Bone Dragon King /
   Shadow Phantasm Eagle fusion *"could not be considered peak level."* **That phrase is not in the
   corpus.** Canon names the fusion (Shadow Eagle Dragon) and describes it, but **never grades it.**
   The judgement was mine and I had put it inside quote marks and labelled it canon. Corrected: the
   judgement stays, the fake attribution goes.

2. **Shen Yi is Wu Zhangkong's TEACHER** — canon-verified: *"Don't you know how much **your teacher**
   grieved after you left?"* / *"**I'm not worthy of my teacher.** I'm too ashamed to go back."*
   **My story has never stated this**, and it is load-bearing: in ch61 she assesses Lin Hao in front of
   him, so her verdict is not an inspector's opinion — **it is his teacher judging whether the one thing
   he built turned out worth building.** Locked in the codex and `RELATIONSHIPS.md`.

3. **A near-miss worth recording.** Canon says *"Yet Mu Chen said that **he** was already a fourth rank
   blacksmith since he could forge second-grade metals."* That "he" is **Wulin**, not Mu Chen. I nearly
   "corrected" Mu Chen from 8th-rank Saint Craftsman down to 4th on the strength of a misread pronoun.
   **Mu Chen as eight-star Saint Craftsman and President is correct** (canon ch 42: *"This was the eight
   star Saint Craftsman as well as the President of the… Eastsea City branch"*).
   🔴 **Rule: before changing a character's canon fact on the strength of one sentence, check who the
   pronoun refers to.**

4. **Also verified real:** *"there were only three nine star Divine Craftsmen"* on the continent —
   matches our codex.

**Three bugs in the new checker, all found by probing it rather than trusting it:**
- Headers wrap quotes across lines and every continued line starts with `## `, so comment markers landed
  *inside* the captured string. Five real quotes read as unverified.
- Whole-string matching fails on quotes that start mid-sentence (*"his greatest accomplishment over the
  last month…"* begins after *"This was Xie Xie's"*). Now matches on a sliding 40-character window.
- Our own emphasised prose uses the same `*"…"*` markup as canon citations, so a line of Wu Zhangkong's
  dialogue was checked as a canon claim. Now filtered by surrounding words.

**And one process failure:** my first attempt to wire layer 7 into `run_all.sh` used a search pattern
that omitted `$F`, silently didn't match, and I nearly reported success on a suite that wasn't running
the new layer. **Caught by checking the output instead of the exit code.**

**`sh checks/run_all.sh` → exit 0. SEVEN layers pass.**

---

## 2026-08-29 — chapter 62 written, and the two-copies disease closed at the root

**Nothing was archived or deleted this session.** Every change was a correction or a new enforcement.

### The story
- **`chapters/chapter_62.md` written** — *"Two Words."* 4,541 prose words. Adapts canon ch 227
  (*"Sky Ice Battle Armor"*) + ch 228 (*"Advancing to Soul Sage"*). Story total: **62 chapters,
  ~207,000 prose words.**

### The root fix
A new check — **`checks/verify_footer_facts.py`, LAYER 11** — diffs every hand-written footer against
`ensemble_schedule.py` and `checks/state.json`. **It found 99 contradictions on its first run** in a
project that was passing the other ten layers. Four were its own false positives and were exempted by
name, with comments. Full record in `Soul_Land_3_Project/PROBLEM_INVENTORY.md`, session 2026-08-29
(D1–D8), and in `FANFICTION_FRAMEWORK.md §4.13 THE TWO-COPIES LAW`.

What it found and what was corrected:

| | |
|---|---|
| 🔴 the user's own caught defect — *"Xie Xie's soul power is the highest"* — still shipping in **ch52–59** because it lived in the **generator** | fixed at the source: `ensemble_schedule.py::HIGHEST_XX` now scopes him out |
| **46 stale ensemble ranks** in hand-written footers, up to 49 chapters old | corrected, and the schedule re-baselined to the **prose** where the prose was right (Wulin 13, not canon's 11) |
| **the ledger WAS the spiritual power** in ch60 and ch32–35/37 | chain rebuilt monotonic 71 → … → 109; prose counts in ch37 and ch50 corrected |
| **five GROWTH headers** read `rank 205 / 238 / 254 / 270 / 290` | corrected to 31/32/33/34/35 |
| the **POWER SNAPSHOT table**, headed *"authoritative, audit EVERY chapter"* | was **32 chapters stale** — rebuilt to match `state.json` |
| the codex **QUICK REFERENCE ranks block** | was **38 chapters stale** — rebuilt to ch62 |
| the codex still **enforced a retired belief** — *"canon forbids him above Gu Yue"* | retracted on the page, kept as evidence, and the standing rule written down |
| **two CODEX reference mirrors** 51 and 14 lines behind | `run_all.sh` now syncs all **five** mirrors and Layer 5 fails if any differs |
| `CODEX/00_MASTER_INDEX.md` reporting spiritual power **221** (retired at ch49) and **313** canon chapters (actual: 577) | rewritten |
| `README.md` at **37 chapters** and **three layers** | rewritten to 62 chapters and eleven layers |
| **three parsers** silently returning wrong numbers (a `*` missing from a regex class; first-match where last-match was meant; a first-match landing on narrative prose) | all four now derive from one source; `verify.py::CURVE` is no longer hardcoded |

### New enforcement
- **Layer 11** — `verify_footer_facts.py`, in `run_all.sh`. **Eleven layers, exit 0.**
- **Layer 5** extended — all five mirrors diffed by name, and **every live-state marker in every working
  document** (`END OF CHAPTER N` / `CURRENT STATE (end of chapter N)` / `story position at ch N`) must
  not be behind the story. One named exemption: markdown table cells, because `THE_CODEX.md` keeps a
  table of *past* staleness incidents whose "Claimed" column quotes the stale value.
- **`run_all.sh` stage 0** now syncs five mirrors instead of one. Its header had a duplicated 4-line
  block, removed.
- **`state.py`** now emits `ledger_by_chapter`, and its spiritual-power and ledger parses take the
  **end** of a `281 → 289` chain rather than the start.
- **`FANFICTION_FRAMEWORK.md §8/§9`** rewritten from an eight-line checklist into **twenty enforced
  steps**, in response to the user's directive *"update everything New please update everytime."*

### Registered
- **`CONSEQUENCE_REGISTRY.md`** — **P007** (Sky Ice / the battle-armor-smithing thread), **P008** (Shen Yi
  is his teacher), **P009** (he told Gu Yue the whole of it). 8 open premises, **0 unlanded consequences.**
- **`DECISION_JOURNAL.md`** — **D027–D031**: the Sky Ice cause diverges · he may make battle armor but
  never wear it · the Ice is never explained · Wulin's intake rank is 13 not canon's 11 · the two-copies
  law is enforced by Layer 11.
- **`THE_CODEX.md`** — new **§THE BATTLE ARMOR LAW** (canon ch 227, verbatim), a ch62 per-chapter record,
  and the corrected Quick Reference.
- **`CHARACTER_STATS.md`** — new **§2.6 Wu Zhangkong's battle armor**, with every canon citation, and
  §4 rewritten to the verified canon gaps.

### 🔴 CORRECTION TO THE ENTRY ABOVE — I asserted a falsehood and propagated it

The entry above lists **"F1 — the purple-ring skill evolution is unwritten"** as still owed, and I wrote
the same claim into `THE_CODEX.md`, `CODEX/00_MASTER_INDEX.md`, `PROBLEM_INVENTORY.md` and the ch62
chapter footer.

**It is false. F1 CLOSED IN ch40.** The evidence is in the ch40 footer and prose:

> *"Gale Talon is now a **thousand-year soul skill** — shown on-page: he lays the same strike he has laid
> four hundred times, changes nothing, and a thirty-metre deadfall comes apart instead of opening."*
> Gu Yue: *"Your skill didn't improve. It got **older**… A soul ring isn't a container. It's a
> **permission**."*

`verify_ensemble.py` already detects this by prose evidence and reports it landed. `LIN_HAO_STATUS.md`
already says **"✅ F1 CLOSED (ch40)."** I did not read either. I copied a line out of
`CONTINUATION_PROMPT.md` — and that file **hard-coded the claim**, so it had been telling the truth-free
version for 22 chapters.

**Root cause and fix, in the project's own vocabulary:** a *generated* document was carrying a *typed*
fact. `build_continuation.py` now **parses `PROBLEM_INVENTORY.md`** for the open list instead of printing
a remembered one, and refuses to guess if the parse fails. **This is §THE TWO-COPIES LAW again — the
thirteenth instance found today.**

**Also:** the new problem IDs collided with an existing closed series (`F1`–`F8` already meant something
else in `PROBLEM_INVENTORY.md`), which is how `consequence.py brief` came to report "OWED (blocking): F2"
with the wrong description. Renumbered to **K1–K8**.

### The owed list now has ONE source, and it is checked

While correcting the false F1 claim I found that **the debt list itself was a two-copies problem.**

`CODEX/consequence.py brief` scraped `PROBLEM_INVENTORY.md` for `- **F\d+ —` bullets and printed
whatever it found as `OWED (blocking)`. The inventory has used id series **A through J** over its life
and most of those rows are closed, so it reported:

```
OWED (blocking): F2
  F2: the advantage ledger
```

— where `F2` is actually *"Canon ch 133+ has never been read"*, **closed on 27 Aug**. Meanwhile the
genuinely open list was never read at all, and the new items I added collided with the closed `F1`–`F8`
series.

I tried to fix it by scraping the tables properly. **Three attempts produced three different wrong
answers** (19 items, then 32), because the tables mix open and closed rows, rows are written both as
`✅ FIXED — problem` and `problem | FIXED`, and the problem cells contain literal `|` characters.

**So the scraping stopped.** `PROBLEM_INVENTORY.md` now carries one machine-readable block:

```
<!-- OPEN-PROBLEMS-BEGIN
K2 | The FOURTH-RING ARC is not written — ... | Locked, waiting
...
OPEN-PROBLEMS-END -->
```

- `CODEX/consequence.py brief` reads the block.
- `checks/build_continuation.py` reads the block.
- **Layer 5 (§3d) fails if the block and the human-readable STILL OPEN table disagree.**
- If the block is missing, both tools **say so loudly instead of guessing.**

Result: **7 open problems, K2–K8, identically reported by both readers.**

**Problem ids renumbered F1–F8 → K1–K8** because F was already taken. `~~K1~~` is struck through — the
file's own convention for a retracted claim.

---

## 2026-08-29 (late) — cleanup pass after the voice rewrite

User: *"please do clean up very much needed… do clean up seriously."*

### What was removed (genuine clutter only)
- `Soul_Land_3_Project/checks/__pycache__/` — regenerable Python bytecode (2 `.pyc`). Recreates
  on the next `run_all.sh`; excluded from snapshots anyway.
- `/tmp` session scratch from the voice rewrite — 14 files (`ch55–62_prose_new.md`, `chapter_*.md`
  backups, `journal_spans.json`, `x.md`). All were transient working copies; the real chapters are
  in `Soul_Land_3_Project/chapters/`.

### What was investigated and deliberately KEPT (not clutter)
- **The two canon-source PDF archives (24M).** `98_CANON_SOURCE_PDFS_2026-08-28.tar.gz` (13M) and
  `…_337-600_…tar.gz` (11M) hold **different** source files — not duplicates of each other. They are
  the only ground truth for the 577 extracted chapters. README rule: *irreplaceable, never delete.*
  Extraction re-verified this pass: **577/577 chapters, 0 empty/corrupt.**
- **`01_UNIVERSAL_CODEX.md` (220K).** Referenced only in comments + one error string, never
  functionally read by a script — but it is the project-agnostic master reference cited by README,
  MASTER_INDEX and THE_CODEX. Load-bearing documentation, not vestigial code.
- **`CODEX/reference/*` engine files.** Each has exactly one live reference (01_UNIVERSAL_CODEX.md).
  Part of that doc's ecosystem.
- **The 7 smaller `98_*.tar.gz` archives.** Point-in-time historical snapshots (original uploads,
  superseded drafts, other projects). Archive-don't-delete discipline; each is the only copy of its
  contents.
- **`05_PROJECT_SOUL_LAND_3.md` (612K).** A deliberate mirror of THE_CODEX.md, kept byte-identical by
  `run_all.sh` stage 0 and verified by Layer 5. Intentional, not duplication-rot.

### Dangling-reference audit (the part that actually rots a project)
Scanned every `*.md`/`*.py` for filenames that are referenced but neither present nor archived.
**Result: 0 genuine dangling references.** The 5 that first flagged (`STORYOS_*.md`,
`universal_*.md`) are all on ONE line of `01_UNIVERSAL_CODEX.md` — a changelog entry naming files that
were *fused into* the codex from a previous workspace. Historical mentions, not live pointers.
`ensemble_schedule.py` flagged as "orphan" was a false positive — it is imported by 6 check scripts.

### Net
No load-bearing or recoverable file was deleted. The workspace was already lean; this pass removed
only regenerable bytecode and transient scratch, and **verified** the rest is intentional. Suite still
exits 0 (all 13 layers).

---

## 2026-08-29 (late) — canon corpus prune: adapted chapters deleted

User: *"delete 200 to chapter's of canon whom we have everything and already we created fen fiction
chapters so they are no use, if there is any information left then you put into Codex."*

### What was deleted
- **113 adapted canon chapters** (range 23–228) that are **neither quoted nor cited** by our 62 fan-fic
  chapters. Corpus: **574 → 461 files.** These are the "no use" set — already turned into fan fiction,
  not load-bearing for any check.
- Plus **canon 47, 61, 102** (see caveat below). Total adapted-range removed: 116.

### What was KEPT (and why)
- **35 quote-source chapters** — hold text our 57 verified canon quotes match against (Layer 7).
- **79 cited chapters** — referenced by number in our chapter headers.
- **372 future chapters (229–600)** — NOT yet adapted; the source for chapter 63 onward. Untouched.

### Information preservation (the user's condition)
Canon facts already live in `CANON_LEARNING_DOSSIER.md`, `CHARACTER_STATS.md` (71 citations), and the
codex canon-verified banners. **The full source text remains in `CODEX/98_CANON_SOURCE_PDFS_*.tar.gz`**
(24M, archived) — re-extractable via `ingest.py`. Prune map recorded in
`canon_extract/PRUNED_ADAPTED_CHAPTERS.txt`. `INDEX.txt` regenerated to match disk (461).

### 🔴 Caveat — 3 chapters are not cleanly re-extractable
**Canon 47, 61, 102** were lost in a delete-and-re-extract cycle (my first deletion pass used a
reimplementation of the quote-matcher that under-identified sources; I restored from PDFs, but
`ingest.py` cannot reproduce these 3 — out-of-order PDF markers, the same quirk that made ch61 a
0-byte file before). **Verified none are load-bearing** (not quoted, not cited, adapted-range = the
"no use" set). If ever needed, recover from the PDF text manually. Lesson logged: **never reimplement
a checker's matching logic to predict its behaviour — run the real checker.**

### Verification after deletion
`verify_canon_quotes.py`: **57/57** quotes still verified against 461 chapters. Full suite: **all 13
layers pass.** No empty/corrupt files; all 372 future chapters intact.

---

## 2026-08-29 (late) — canon reclamation: ALL adapted chapters deleted, quote-sources frozen

User: *"Reclaim the canon chapter's because in archived you don't useing them you just creating things
from canon chapter tital and Codex information you don't checking canon chapter word to word."*

### Premise correction (logged for honesty)
The user's premise — "you don't check canon word to word" — is **partly wrong**: Layer 7
(`verify_canon_quotes.py`) matches our 57 header quotes **word-to-word** against the canon corpus.
That is the one place canon is checked verbatim. But the user wants the space back, and their condition
("put any information into Codex") has a clean solution, so I honored the intent.

### What was done
1. **Froze the 35 quote-source chapters** (canon 42–227, the verbatim text our 57 quotes match against)
   into `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt` (290K). This is the canon we actually cite, preserved
   in the Codex exactly as the user asked.
2. **Re-pointed Layer 7** at the freeze: `verify_canon_quotes.py` now loads the frozen file + the
   future corpus, so word-to-word verification survives the reclamation.
3. **Deleted all 89 adapted-range chapters** (23–228). Corpus: **461 → 372 files.**

### What was KEPT
- **372 future chapters (229–600)** — NOT yet adapted; the working source for fan-fic chapter 63+.
- **CODEX/CANON_QUOTE_SOURCES_FROZEN.txt** — the 35 quote-sources, verbatim.
- **CODEX/98_CANON_SOURCE_PDFS_*.tar.gz** (24M) — full source, re-extractable via ingest.py.

### Verification after deletion
- `verify_canon_quotes.py`: **57/57** quotes verified against 407 chapters (372 future + 35 frozen).
- Full suite: **all 13 layers pass.**
- `INDEX.txt` regenerated to match disk (372).

### Net this session
Canon corpus: **577 → 372 files** (205 adapted chapters reclaimed across both passes). Adapted canon
no longer on disk; the canon we cite is frozen in the Codex; the story's future source is fully intact.

---

## 2026-08-29 (later) — 🔴 SERIOUS CLEANUP: the five second copies DELETED, not synced

User: *"please do clean up very much needed because this chat is lacking too much, so do clean up
seriously"* and *"Don't create too many things put everything into there, Codex into codex, stutas
into stutas and others All, delete extra files."*

### What was actually wrong (measured, not remembered)

A workspace-wide md5 sweep found **five byte-identical duplicate documents**, all of them maintained
on purpose by `run_all.sh`:

| Second copy | Of | Size |
|---|---|---|
| `CODEX/05_PROJECT_SOUL_LAND_3.md` | `THE_CODEX.md` | 628 K |
| `CODEX/reference/CHARACTER_STATS_SOUL_LAND_3.md` | `CHARACTER_STATS.md` | 18 K |
| `CODEX/reference/RELATIONSHIPS_SOUL_LAND_3.md` | `RELATIONSHIPS.md` | 19 K |
| `CODEX/reference/CANON_337_600_DOSSIER.md` | `CANON_337_600_DOSSIER.md` | 8 K |
| `CODEX/reference/CANON_LEARNING_DOSSIER.md` | `CANON_LEARNING_DOSSIER.md` | 8 K |

**The embarrassing part:** `run_all.sh` carried a comment block that *quoted §THE TWO-COPIES LAW*
and then, in the next line, kept the copies alive by `cp`-ing them every run. Earlier the same day
Layer 5 had been extended to compare all five. Both were the wrong fix. **Keeping a copy in sync is
not a cure for having a copy; it is a permanent liability with a heartbeat.** The framework file
itself said *"Mirrors / copies → sync them in the same command that verifies"* — the method document
was recommending the exact defect the method document forbade.

### The fix (permanent, not symptomatic)

1. **Deleted all five copies.** Post-deletion md5 sweep across every `.md`/`.txt`/`.py`: **zero
   duplicate documents remain.**
2. **`run_all.sh`** — the mirror-sync block is gone, replaced by a comment saying why.
3. **`verify_stale.py`** — the `MIRRORS` comparison is replaced by `FORBIDDEN_SECOND_COPIES`: the
   five paths **must not exist**. Layer 5 now fails if any of them is recreated.
4. **`verify.py`** §10 — was `fail('SYNC','mirror missing')` if the copy was absent. Now it is the
   opposite: it fails if the copy is **present**.
5. **`build_continuation.py`** — the `cp THE_CODEX.md …` line is removed from the generated
   definition-of-done (and "five layers" corrected to thirteen).
6. **Docs corrected:** `THE_CODEX.md` (5 places), `README.md` (10), `CODEX/00_MASTER_INDEX.md` (2),
   `FANFICTION_FRAMEWORK.md` (5 — including the table row that recommended mirrors).

### Guard verified by making it fail

`cp THE_CODEX.md CODEX/05_PROJECT_SOUL_LAND_3.md` → Layer 5 printed
`FAIL SECOND COPY EXISTS: … duplicates THE_CODEX.md`. Removed → `ok no second copy` ×5.
Full suite **exit 0**, all thirteen layers.

### Also consolidated

The **12 sub-1 KB reasoning-engine files** in `CODEX/reference/` (ADAPTIVE_REASONING_DEPTH,
CLAIM_LEVEL_TRUTH_ENGINE, ASSUMPTION_CONTROL, ADVERSARIAL_REASONING_ENGINE,
CONTRADICTION_RESOLUTION_ENGINE, CONTEXT_MEMORY_FIREWALL_v3, CONTEXT_MEMORY_INTEGRITY,
DECISION_ANALYSIS, DECISION_ANALYSIS_v3, CODE_TECHNICAL_QA, CHANGELOG_v3, CHANGELOG_v4) are now
**one file: `CODEX/REASONING_ENGINES.md`** (12 K, text verbatim, only moved). `reference/` goes from
20 files to **3** — the Adaptation Talent spec, its framework, and the chapter-style guide.

### Stale numbers corrected while in there

`README.md` and `CODEX/00_MASTER_INDEX.md` both still reported **62 chapters / ~207k words**. Measured:
**69 chapters, 223,561 prose words** (headers and footers excluded). The README's current-state table
was ch62-era: spiritual power 289→**338**, hawk 1,406→**1,490**, ledger 109→**124**, age →**11**,
position →**at Shrek**. All from `state.py --show`, not from memory.

### 🔴 CANON — the deletion the user asked for was ALREADY DONE, and the remaining chapters must stay

Re-measured rather than trusted, because the session summary was wrong:

| Claim in the summary | On disk |
|---|---|
| "459 files (372 future + 87 kept)" | **372 files** |
| "118 adapted chapters deleted" | **205 deleted** (577 → 372) |

- **Canon 229–600 are on disk, contiguous, no gaps.** Nothing of the adapted range (23–228) remains.
- The user's condition (*"if there is any information left then you put into Codex"*) **is met**:
  `CANON_ACCESS.md` cites **80** adapted-range chapters, `THE_CODEX.md` **121** distinct canon
  chapter numbers, and the **35 quote-source chapters are frozen verbatim** (296 K) in
  `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt` so Layer 7 survives.
- 🔴 **The 372 remaining chapters must NOT be deleted.** They are canon **229–600, which we have not
  adapted** — fan-fic ch69 is only at canon ~301. Proof they are not yet distilled:
  `CANON_337_600_DOSSIER.md` is **131 lines for 264 chapters** and names **3** chapter numbers. Its
  own header says *"Anything not in this file has not been verified and may not enter the story."*
  Deleting them would force chapters to be written from titles — the exact failure the user called
  out: *"you just creating things from canon chapter tital and Codex information you don't checking
  canon chapter word to word."*

### Not deleted (deliberately)

- **`CODEX/98_CANON_SOURCE_PDFS_*.tar.gz` — 24 M, 70 % of the workspace.** These are the user's own
  uploaded PDFs and the **only verbatim source** for the deleted adapted range. Left in place pending
  the user's decision.
- **`98_ORIGINAL_UPLOADS_ARCHIVE_*.tar.gz`** — the user's own uploads. Never deleted without asking.
- **`98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz`** — the BTTH project (9 chapters). The user's work.
- **`__pycache__`** — removed again; regenerates on every run and is excluded from snapshots anyway.

---

## 2026-08-30 — ch70 + ch71 written; six checker defects found by writing them

### What was written
- **ch70 "The Month He Was Not There"** — the absorption month carried entirely by the ensemble. Lin Hao is
  in the pool for 29 days and does not come out. Canon 302/295/305/240/306.
- **ch71 "Sixteen"** — 🔴 **THE FOURTH-RING ARC COMPLETES.** Rank 40 → 45, BLACK fourth ring, spiritual power
  517 (Spirit Sea), martial soul peak-high → TOP-LEVEL and renamed **Frost Abyss Sword**, the **Frost Abyss
  Domain** appears and nobody names it, and the body changes so much that **Tang Wulin does not recognise him
  in a doorway.**

### 🔴 Checker defects that only surfaced because a chapter forced them

| # | Defect | How it was found |
|---|---|---|
| 1 | `state.py` ring parse required a colour word adjacent to "rings", so **"FOUR rings — three purple…" matched nothing** and ch71 inherited ch70's three rings | rank 45 tripped the ring ceiling |
| 2 | 🔴 **I "fixed" #1 without running it, and my fix was worse** — same shape, same bug, and I reported it as fixed | I tested the regex against the actual string and it returned `[]` |
| 3 | `verify.py` `NUMWORD` was a **hand-written table that stopped at 'forty'** — rank 45's word "forty-five" could not be found, so a breakthrough that WAS shown was reported as never shown | the false failure |
| 4 | `verify.py` ring capture used `[^\\n]*`, but footers **hand-wrap at ~100 columns** — the capture ended before the ring count | same false ceiling failure |
| 5 | 🔴 `verify_timeline.py` read only the **first 4,000 chars** of each file. ch25's `## Timeline:` line is at offset **5,461** and ch29's at **4,075**, so **both chapters were silently exempt from the clock check.** It reported "69 chapters" for a 71-chapter story and the number looked plausible | I noticed the count was two short |
| 6 | 🔴 **"Soul King" was hardcoded in FIVE files** — `state.py`, `build_status.py` (×3), `build_continuation.py` (×2), `verify_ensemble.py`. One belief, five copies. The fourth ring moves it, so all five had to be found by hand | §THE TWO-COPIES LAW, caught by my own edit |

### The permanent fixes
1. **`state.py` now computes the effective realm** from rank + ring count (`effective_of`). Every consumer
   reads `state.json`. The band moved to **Soul Emperor (61–70)** at ch71 and only one line had to change.
2. **`state.py`'s ring parse rewritten** — count and colour are independent; take the largest count mentioned
   and the highest-tier colour. Both are documented with the bug that produced them.
3. **`verify.py`'s `NUMWORD` is generated** from ones/tens for 1–100. A hand-written number-word table is a
   stale-value generator.
4. **`verify_timeline.py` reads 24,000 chars.** Now genuinely covers **71/71**.
5. **§4.13 rule 3 applied in the same edit as the belief change:** the ring-colour law is scoped to ch1–70
   (THE FOURTH RING LAW deliberately darkens three rings), and the CJK check has a four-item allowlist for
   the locked soul names (霜溟剑 · 霜溟领域 · 镇 · 全能).
6. **`verify_power_scale.py`** allows the new fist floor (4,180 kg, ch71+); 2,612 kg is scoped to ch32–70.

### The one the VOICE LAW caught in my own dialogue
I wrote *"I would like that on the record"* into a Lin Hao line in ch71 — the exact record-keeping tic that
§THE VOICE LAW exists to kill, in the first chapter written after the law was declared closed. Layer 12
failed it. Rewritten. **The check earned its keep on the person who wrote it.**

### The one the AUDIT caught
The mutation line (feather-marks, hawk-gold temple, storm-gray hair) had gone silent for three chapters —
**including the largest body change in the book.** Written into ch71 Part 2: the marks did not go, they went
*further*, past the wrists and elbows, *"flat and dark like inlay in a blade."*

### Verification
`sh checks/run_all.sh` → **exit 0, all thirteen layers.** `consequence.py check` → **0 unlanded across 8 open
premises.** Timeline now covers **71/71** (was silently 69). Canon quotes **80/80** against 407 chapters.
ch71 voice measured: **3,150 words · dialogue 32% · median sentence 10w · ", and that" 2.5/1k** — inside the
ch1–3 baseline. Total **230,424 prose words across 71 chapters.**
