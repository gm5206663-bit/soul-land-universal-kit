<!-- ⚠️ V1-EPOCH DOCUMENT — historical reference only.
The V1 serial (chapters 1–15, the balm/jar economy arc) was REPLACED by the V2
canon-parallel rebuild on 2026-09-23 (see foundation/REBUILD_PLAN.md and
foundation/V2_EPOCH.md). This file's specifics describe the OLD book and are
preserved for provenance. Live V2 law lives in: foundation/REBUILD_PLAN.md,
foundation/SERIAL_LOG.md, foundation/BUTTERFLY_BANK_V2.md, foundation/CONTINUITY.md
(V2 section), LAN_SHEN_MISSION.md, and the PREWRITE boards ch02–ch06.
Do NOT copy facts from this file into V2 chapters.
(Quarantine banner added 2026-10-10, full-workshop audit.) -->

# HANDOFF — Lan Shen (Soul Land 3 reincarnation)

**Rewritten: 2026-09-20**, after the full comparative audit and the shipping of chapter thirteen.
Read this first. Every other file in this project says what is true; this one says what is
true *now*, and which of the others to trust.

---

## 1. One-paragraph state

A reincarnation serial set in *Soul Land 3: Legend of the Dragon King*, in Glorybound City,
Years 0-2. The protagonist **Lan Shen** is a self-insert: a man who died in our world and woke in
this one at birth, who read the source novel in his previous life and remembers parts of it. He
awakened **Bluesilver Grass at innate soul power rank one** — a "trash" martial soul — but his
real edge is **high spiritual power** and a lifetime of adult method in a child's body. He lives
two doors down from Tang Wulin and has spent thirteen chapters keeping himself unremarkable while
building a herb-shop materials base for cultivation-aiding food. **Thirteen chapters are shipped
and gated, 3,848 prose words, and the serial now stands in the late autumn of Year 3, end of ch15.**

🔴🔴 **A full workspace audit and management pass ran on 2026-09-20. No chapter was written.**
It found that chapters one to four had been staging canon partly by **transcribing the
translation's dialogue** — 785 verbatim canon words between them, 297 in chapter three alone —
while `canon_copy_check.py` reported PASS, because its threshold was 15 words and every borrowed
run sat between 8 and 14. Forty-two passages were re-voiced, the threshold was rebuilt from corpus
evidence, and the defect is now a regression test. It also found the butterfly ledger had stopped
at chapter nine, that a live personal email was sitting in `OPEN_DECISIONS.md`, and that the
author's own prose had been read but never measured. **Full record: `SERIAL_LOG.md`, entry
"FULL WORKSPACE AUDIT AND MANAGEMENT PASS — 2026-09-20". Promoted to `LOCK 16`.**

**The whole suite is now one command: `sh checks/run_all.sh` → ALL GREEN, 9 layers, exit 0.**

🔴 **THE GITHUB SWEEP, 2026-09-20.** Two repositories were read in full: `storyos-site`
(the framework and web app) and `the-universal-storyline-creation-`, which had been a dead
placeholder and is now the **CONTROL CENTRE** — an append-only state layer for every serial.
**This project was not registered in it and now is:** 57 contributions filed (1 project, 12
locks, 14 firewalls, 8 anchors, 6 decisions, 7 corrections, 6 canon claims, 3 notes), validated
by their own validator with no issues, ingested, and rebuilt with their selftest still 102/102.
Three instruments came back the other way: `BANNED_TOKENS.json`, `banned_token_check.py`
(layer 9) and `scan_project.py`. Layer 9 immediately found **nine fourth-wall breaks in shipped
prose** — the word "canon" inside Lan Shen's own interiority in chapters 2, 3, 4 and 5, which
Lock 7.6 forbids and which eight gate layers had never caught, because every existing gate
judges whether prose is well-formed and none can know that a word belongs to the author rather
than to the character. All nine were repaired to memory framing. Full account in
`foundation/SERIAL_LOG.md`, last entry.

🔴🔴 **Chapter twelve found the shape of the serial: THE FLAT LINE.** Lin Ximeng stopped walking
the rows and started measuring them. Lan Shen lands four minutes, eighth of fifteen, every time,
for a whole term. His real ceiling is nine and he has told nobody. Lin Ximeng needed a control for
a boy he cannot explain, chose Lan Shen, and wrote down that exactly one child in fifteen did not
move. **The control is the anomaly and he does not know it.** Lan Shen wrote *why is this
straight* under ten fours and does not think it is a dangerous question.

🔴🔴 **Chapter thirteen fired TRACK 8 — the author ruling, on paper, for the first time.** A
teacher at Na'er's ordinary school asked what to do with a girl who has nothing on the day
everybody shows what they have, and Lan Shen answered with the solution the academy had handed
him: **give her a job.** Then he wrote Na'er a story — ten pages at the back of the notebook, a
girl in a city of nine million who can feel everything and cannot switch it off and stands still
in doorways. 🔴 **And he wrote the only true sentence he has produced in two lives, about her, by
accident, because the paragraph before it needed a paragraph after it.** Canon 019, fetched this
session, independently confirms that faculty in Na'er. He read it back, recognised it, thought
about burning it, and did not. It is on the second row of the shelf, square to the edge, where his
mother can reach it, in the same book as the counts, the column of fours, and a falsehood.

🔴🔴 **AND THE NUMBER MOVED THE WRONG WAY.** Thirty thousand Federation Coins — his target since
ch6, 2,727 days of his sister's mornings — turned out to be **the floor, not the price.** Canon
019 shows what it actually buys: a ten-centimetre defective **Grass Snake** from position one
hundred of exactly one hundred, and Wulin crying for the first time in his life. 🔴 **Lan Shen
does not know this and must not.** He knows the direction; he does not know the snake.

🔴 **Next: chapter fourteen. YEAR 3. Canon 013 is the anchor — the workshop, Mang Tian, the
hammer, Wulin nine. Then 014-019: the money, rank ten, the stars, the spiritual power test, 38,
the random draw, and the Grass Snake.** Ch12 built the wall that has kept the test from happening
(a helmet, a hall, a hundred Federation Coins nobody in Glorybound City will spend on a child who
is already doing perfectly well) — 🔴 **the ch14 prewrite must say what brings that wall down, and
it must not be convenience.** Per `#28`, ch14 stays in Lan Shen's own register; **ch15 is the
Other-POV slot, and Na'er is the most valuable unread interior in the serial.**

## 2. Authority order

1. **The user's words** — rulings recorded verbatim in `foundation/OPEN_DECISIONS.md` and
   `foundation/NO_MISTAKE_LIVE_RULES.md` (the sixteen locks).
2. **Project locked documents**, in this order:
   `foundation/THE_PLAN.md` · `foundation/OPEN_DECISIONS.md` · `foundation/STATUS_PANEL.md`
   · `codex/KNOWLEDGE_FIREWALLS.md` · `codex/CANON_LEDGER.md`
3. **Kit laws** — `/home/user/ref/SOUL_LAND_UNIVERSAL_KIT/00..10`.
4. **Kit canon spine** — `canon_extract/chapters/canon_001..018_excerpt.txt` (fetched receipts).
5. **Earlier projects — craft only, never canon.** `/home/user/ref/blue_silver/`,
   `sl4_fire_phoenix/`, `SOUL_LAND_NEW/`. And `/home/user/ref/reference/sl3_lin_hao/` is
   **story-FORBIDDEN, tools-reusable** (see §8).

## 3. Edge

```
CHAPTER SHIPPED   Thirteen — "Made Up"        chapters/Chapter_13_Made_Up.md
NEXT CHAPTER      Fourteen — 🔴🔴 YEAR 3. CANON 013: the workshop, Mang Tian, the hammer.
                  🔴 #28: ch14 is Lan Shen's own register. Ch15 is the Other-POV slot.
                  🔴🔴 #27 MUST NOT BE STATED — the mechanism is now earned. Explaining it
                  voids three chapters of work.
AGE               eight throughout ch13. 🔴 Turns nine in Year 3's late autumn.
DATE              🔴 years 2–2 in ch13: last week of the Year 2 winter → the autumn of Year 2,
                  about nine months, #25 compression. 🔴 **Roughly one year of serial time
                  remains before canon 013.**
RANK              innate soul power rank one. Bluesilver Grass. 🔴 NOT MOVED IN 13 CHAPTERS
                  — and cannot: rank ten needs a ring and a ring needs a kill
ON THE BOOKS      working student, four hours a week, east-wing storeroom, Tuesdays and
                  Fridays. Hours in four books that agree. Second year of three.
🔴🔴 THE NUMBER   FOUR MINUTES. Term two and term three of Year 2, once four and a quarter.
                  Real ceiling NINE MINUTES, told to nobody, in his own book only.
🔴🔴 THE MONEY    THIRTY THOUSAND IS THE CHEAP ONE. 1 FC = 1 copper. 30,000 = 2,727 days of
                  Lan Yue's mornings = 7.5 years. 🔴 The white is 70,000 = 6,364 days = 17.4
                  years. 🔴 NOBODY HAS DONE THAT SECOND SUM OUT LOUD AND NOBODY MUST BEFORE
                  YEAR 3. He does NOT know 70,000, or 1,000,000, or the counts 73 and 11.
🔴🔴 TRACK 8      FIRED ON PAPER, ch13. Ten pages, ~1,500 words, back of the notebook. 🔴 NOT
                  SOLD. NOT OUT OF THE HOUSE. Nobody in Glorybound City buys stories. The whole
                  material base is a paper shop on the long street and a man with a case who
                  comes twice a year.
SOUL POWER        not measured. 🔴 NOBODY'S IS. No helmet exists in Glorybound City. Canon 017's
                  test is the instrument; canon 018 gives Wulin 38 at AGE NINE, YEAR 3.
SPIRITUAL POWER   HIGH (author ruling), with large effects. Unmeasured on the page.
RINGS / SKILLS    none.
CLASS SIZE        🔴 17 (Year 0) → 16 (Year 1) → **15 (Year 2)**. 🔴 Na'er's sixes is 29, two
                  of them rank one. Different registers, different buildings.
SENSE             🔴🔴 USED ZERO TIMES. FIVE SEASONS RUNNING. Bank 20,100 (Year 2 spring) →
                  42,600 peak (Year 2 summer) → down through autumn. 🔴 THE BANK AND THE
                  ACADEMY GROUNDS (sixty thousand, sown, under the east wing) ARE DIFFERENT
                  NUMBERS AND DIFFERENT PLACES.
                  🔴 COST RULE: cost is WIDTH, not TIME. #15 binds.
                  🔴 UNITS: ch11's ten/eleven are SECONDS. Ch12's four/nine are MINUTES.
IDENTITY          concealed, 🔴 **and slightly breached, on purpose, for somebody else.** Tang
                  Ziran has asked "how long have you had it" and been told "a while". Madam Zhou
                  wrote something in pencil and timed a look at him. Su Wan has named the road.
HAPPENED IN CH13  ✅ TRACK 8 fired on paper · ✅ Madam Zhou, new face · ✅ Na'er calls the
                  twenty-nine names · ✅ Lang Yue's canon 011 job staged · ✅ the 30,000
                  re-priced as a floor · ✅ Lan Yue's ticket four → five · ✅ Na'er's four months
                  came due, on time, as predicted in ch12 · ✅ canon 019 FETCHED AND HELD
NOT YET HAPPENED  the spiritual power test (canon 017, Year 3) · any rank movement · any ring
                  · any skill · 🔴 A MANUSCRIPT BEING SOLD, OR LEAVING THE HOUSE · 🔴 LAN SHEN
                  FORESEEING THE GRASS SNAKE · anybody finding the ten pages on the second row ·
                  anybody reading Zhou's pencil line · anybody learning what Yan Song wrote in
                  the rank column · Qin Wu's three anomaly forms being read · Na'er leaving
                  (canon 015/024) · the Year 3 workshop (canon 013) · 🔴 #27 being resolved OR
                  STATED · 🔴 Su Wan being answered
```

## 4. Locked decisions

| Lock | Value | Reversible? |
|---|---|---|
| **ERA** | Soul Land 3, *Legend of the Dragon King*, Glorybound City, Years 0-2 | No |
| **PROTAGONIST** | Lan Shen. Reincarnated adult in a child's body. Self-insert — his previous life **is the user** | No |
| **WHAT HE IS NOT** | 🔴 **No adaptation talent** — the user's only explicit "NOT". Everything else that was ever described as a cap was **never approved by the user** and has been removed | No |
| **CANON ENTRY** | canon 001 (Awakening Day) through canon 018 (Random Draw), all fetched and on disk | No |
| **SPINE** | `OPEN_DECISIONS.md` #18 — the convergence on the same object is the spine; #26 adds that a **number must move** and a **face must oppose** | Refinable |
| **POWER CEILING** | 🔴 **NONE.** The user never approved a hard ceiling. Limits are time, visibility, capital, rank and other people — **never ability** | No |
| **IDENTITY** | Concealed. He may write anything **except the truth** (Track 8) | No |
| **ABSOLUTES** | Royal bloodline is **CLOSED** to Lan Shen (canon restricts it to A Yin's descendants) · no manuscript before Year 2 · Track 8 does not fire before Year 1 | No |
| **CANON IMMUNITY** | Never silently correct a receipt. Lin Ximeng's gender contradiction (canon 004 *his* / canon 012 *she*) is held with **both quotations verbatim**; ruling is **MALE** per canon 004 | No |
| **MEASUREMENT** | Federation Coins; three-tier spirit soul prices 30,000 / 70,000 / 1,000,000 (canon 016); Spirit Origin 1-50 (canon 018) | No |
| **VOICE** | The `blue_silver/chapters_rebuilt/` model. Narration median 7-11 words; `, and` chains ≤20/1k; dialogue 13-30% | No |
| **CADENCE** | 3,500-5,000 words per chapter. ch3 (6,455) and ch1 (5,852) exceed it and are logged as deliberate | Refinable |

## 5. Live files vs stale files

🔴 **This table was stale on 2026-09-20 and has been rebuilt.** It listed `codex/CANON_LEDGER.md`
and `codex/CONTINUITY.md`, which are not the real paths (both live in `foundation/`); it claimed
**~30% decay**, which was never true and is now contradicted by a maintained figure; and every
"synced through ch9" line was four chapters out of date while §1, §3 and §9 of this same file had
been synced to ch13. **A handoff that is partly updated is worse than one that is honestly old,**
because the reader trusts the parts that look current.

| Path | Status |
|---|---|
| `SARA.md` | **LIVE** — the partner's self-file. 🔴 **Appended every session, whatever else the session did** |
| `README.md` `PROJECT_README.md` `HANDOFF.md` | **LIVE** — the three entry points. All three carry a word count, so all three are in the update path |
| `LICENSE` | **LIVE** — MIT for the tooling, derivative-work notice for the prose. Added 2026-09-20 |
| `.gitignore` | **LIVE** — added 2026-09-20 after a committed `__pycache__` was found |
| `checks/run_all.sh` | **LIVE** — one command, nine layers, exit 0. Added 2026-09-20 |
| `foundation/BANNED_TOKENS.json` | **LIVE** — the list of values that are known-dead. Five categories, each with its own scope. Also records `owned_elsewhere` (eight rules this file must not duplicate) and `not_banned_deliberately` (phrases an instrument cannot judge honestly). Added 2026-09-20 |
| `tools/banned_token_check.py` | **LIVE** — layer 9. Imports the four honesty rules from `storyos-site/scripts/drift.py`. Has a `--file` mode so `selftest.py` can prove it can fail. Added 2026-09-20 |
| `tools/scan_project.py` | **LIVE** — generates `foundation/CURRENT_STATE_MANIFEST.json` by measuring the tree, including running the gate battery rather than asserting it green. Run it after any chapter ships. Added 2026-09-20 |
| `foundation/CURRENT_STATE_MANIFEST.json` | **GENERATED — never hand-edit.** Machine-readable current state. Where a hand-written document disagrees with it, it wins, because it was measured |
| `foundation/STATUS_PANEL.md` | **LIVE** — sole source for the per-chapter record and the serial totals. Uses **style_gate** word counts |
| `foundation/NO_MISTAKE_LIVE_RULES.md` | **LIVE** — **the sixteen locks.** 🔴 The only copy; a second was created at the root on 2026-09-20 and merged and deleted. **LOCK 16 is the transcription lock** |
| `foundation/OPEN_DECISIONS.md` | **LIVE** — sole source for rulings. 🔴 **#29 is the newest**; #26 (the four failures) and #28 (the register rotation) are **binding** |
| `foundation/THE_PLAN.md` | **LIVE** — the eight tracks. Track 8 = the author, **fired on paper in ch13** |
| `foundation/STYLE_LAW.md` | **LIVE** — the voice, imported and measured. 🔴 **§0.5 is the sentence-level DNA table**, added 2026-09-20 |
| `foundation/CANON_LEDGER.md` | **LIVE** — 🔴 **B1–B73 butterflies · RUNNING DECAY ~15% (maintained) · the divergence economy S1–S10.** B44–B74 and both new sections were added 2026-09-20; before that the ledger stopped at ch9 |
| `foundation/CONTINUITY.md` | **LIVE** — anchors, ages, forward references. **Synced through ch13** |
| `foundation/CANON_NOTES.md` | **LIVE** — canon analysis and receipts-in-context |
| `foundation/SERIAL_LOG.md` | **LIVE** — bookkeeping lives here, never in chapter footers |
| `foundation/PREWRITE_ch10…13.md` | **LIVE** — the pre-draft boards, each with its outcome of record appended |
| `codex/KNOWLEDGE_FIREWALLS.md` | **LIVE** — what Lan Shen knows vs what he may show. **73 rows; 65–73 are ch13** |
| `codex/CHARACTERS.md` | **LIVE** — **synced through ch13**, including the RELATIONSHIP SPINE. 🔴 Read the two-characters-one-letter-apart block before writing Lan Yue or Lang Yue |
| `codex/TIMELINE.md` | **LIVE** — **synced through ch13.** Carries the resolved/open fuse tables and the ch12–13 compression entries |
| `codex/PLACES.md` | **LIVE** — **synced through ch13** (ordinary school, paper shop). 🔴 Read the bench entry before any measurement scene |
| `audits/2026-09-20_FULL_COMPARATIVE_AUDIT.md` | **LIVE** — the five-failures diagnosis and everything fixed |
| `tools/verify.py` `style_gate.py` `canon_copy_check.py` `selftest.py` | **LIVE** — 🔴 forks of the kit tools, not copies. `canon_copy_check.py` was rebuilt from corpus evidence on 2026-09-20 |
| `../SOUL_LAND_UNIVERSAL_KIT/` | **The kit — one copy, at the repo root.** The vendored copy was not carried over in the 2026-10-12 consolidation (one-home law; see `IMPORTED.md`). Layer 8 of the suite runs its `tools/selftest.py` |
| `canon_extract/chapters/*.txt` | **LIVE RECEIPTS** — never edit, never "correct." 🔴 **A receipt may quote canon. It may NEVER quote the serial** |
| `/home/user/fix/**` | **WORKSPACE ROOT, OUTSIDE THIS REPO** — the author's security and cleanup pack. Source of `LICENSE`, the TWO-COPIES LAW and the privacy lesson |
| `/home/user/github-token-setup.md` | 🔴🔴 **COMPROMISED CREDENTIAL. NEVER OPEN, NEVER USE, NEVER COPY INTO THIS REPO.** Outside the repo by design |
| `/home/user/ref/reference/sl3_lin_hao/**` | 🔴 **FORBIDDEN AS STORY.** Craft and tools only. Never import a character, place or event |
| `/home/user/ref/SOUL_LAND_NEW/**` `/home/user/ref/blue_silver/**` | **REFERENCE** — dropped and rebuilt projects respectively. Craft only |
| `/home/user/lan_shen.zip` | 🔴 **REBUILD AFTER EVERY SESSION.** It is a distribution artifact and goes stale silently |

**When two files disagree:** the user's words win, then `OPEN_DECISIONS.md` (highest-numbered
ruling wins), then `STATUS_PANEL.md`, then the codex. A canon receipt is never overruled by
any of them — it is only ever *interpreted*.

## 6. Open questions

- **#25 compression** — Year 0 must end within three to five chapters from ch9. Two are now
  spent on the audit rather than on chapters; ch10 must open Year 1.
- **#24 the Four** — eyes three, sense four, same corner, one minute apart. **Deliberately
  unresolved.** Parked on purpose, in a book on an open shelf. Do not resolve it by accident.
- **#22 lossy memory** — "four hundred chapters and I remember the ones I liked." He must be
  allowed to be *wrong* about canon. Not yet exercised on the page.
- **#26(a) which face** — Yan Song is the named near spine and the audit argues he is the
  correct face for a number that moves. Not yet executed.
- **Canon fetch queue** — ch19 ("Spirit Soul"), ch20-22, ch24 ("Na'er Leaves") are **not on
  disk**. 🔴 Never rule on a canon fact without the next chapter in hand; R11 was wrong
  exactly this way.

## 7. Known gaps

- `BRIEF.md` / a machine-generated prewrite brief — **not built**. The prewrite gate is
  currently answered by hand from `OPEN_DECISIONS.md` #26(d).
- `WORLD_STATE.md` registry — **not built**. Required by sl3's `world_tick.py` if that is
  ever ported.
- sl3 audit layers 5-9 (`divergence_engine`, `world_tick`, `completeness_audit`,
  `voice_check`, `audit_mm`) — **inventoried, not ported**.
- Ch3 is 6,313 words against a 5,000 ceiling. **Pre-existing, deliberate, logged.**

## 8. Do-not list

- 🔴 **Never import sl3 story content.** `reference/sl3_lin_hao/` is a forbidden serial. Its
  20 check scripts are reusable; its characters, places and events are not.
- 🔴 **Never use the git token.** The user pasted one twice. It is compromised. All repos are
  public — read anonymously, and never push on the user's behalf.
- 🔴 **Never cap his ability.** The user rejected hard ceilings. Limits are time, visibility,
  capital, rank, other people. Not talent.
- 🔴 **Never put real personal details of the user in a public repo.** The previous life is
  the user; handle it with respect and keep specifics out.
- 🔴 **Never write "eleven years" backwards.** The motif is forward-looking only; his previous
  life is "the other life."
- 🔴 **Never let a codex marker reach prose.** No 🔴, no field labels, no apparatus in chapters.
- 🔴 **Never silently correct a canon receipt.** Log the variance and hold both readings.
- 🔴 **Never rule on a canon fact without fetching the next chapter.** R11 did and was wrong.
- 🔴 **Never skip check (d)** — date arithmetic is invisible to every gate and has produced
  month-count errors in ch6, ch8 and ch9 (nine in ch9 alone).
- 🔴 **Never embed multi-paragraph prose in Python string literals.** Use heredoc files.
  A triple-quote collision and a mixed-type list bug have both already cost edits.

## 9. Last verification

Run from `/home/user/lan_shen`:

**One command:** `sh checks/run_all.sh` → **ALL GREEN, 9 layers, exit 0**, 2026-09-20.

| # | Layer | Command | Result | Date |
|---|---|---|---|---|
| 1 | Structural gate (9 gates) | `python3 tools/verify.py chapters` | **PASS** — 15 files, 3,848 prose words, 0 failures, contiguity holds across years 0-1-2-3 | 2026-09-21 |
| 2 | Voice / style gate | `python3 tools/style_gate.py chapters` | **PASS (warnings)** — exit 2 by design; 1 warning: ch3 above the word band (pre-existing, logged, permanent) | 2026-09-20 |
| 3 | Canon transcription | `python3 tools/canon_copy_check.py` | **PASS** — exhaustive comparisons (14 chapters x 21 extracts). 🔴 **Thresholds rebuilt from the corpus this session:** runs >= 7 words fail, density > 120 verbatim words fails. Previously 15 words with no density check, which hid 785 verbatim words in ch1-4 | 2026-09-20 |
| 4 | Marker-leak grep | `checks/run_all.sh` | **PASS** — no codex glyph in any chapter | 2026-09-20 |
| 5 | Privacy grep | `checks/run_all.sh` | **PASS** — 🔴 **new layer. A live personal email was found in `OPEN_DECISIONS.md` and removed.** Proven to fire by planting a leak | 2026-09-20 |
| 6 | Build hygiene | `checks/run_all.sh` | **PASS** — 🔴 **new layer.** A committed `__pycache__` was removed and `.gitignore` added | 2026-09-20 |
| 7 | Gate selftest | `python3 tools/selftest.py` | **PASS** — 20 checks, 20 held, 0 blind. 🔴 **Four new checks, including a regression that injects the exact ch3 transcription shape** | 2026-09-20 |
| 8 | Kit regression | `python3 ../SOUL_LAND_UNIVERSAL_KIT/tools/selftest.py` | **PASS** — forked `verify.py` introduces no inherited-gate regression. (*2026-10-13: the vendored copy is gone with the 2026-10-12 consolidation — the suite now runs the kit’s one copy at the repo root.*) | 2026-09-20 |
| 9 | Regression tokens | `python3 tools/banned_token_check.py` | **PASS** — 0 failures, 23 exempt receipts. 🔴 **New 2026-09-20.** Reads `foundation/BANNED_TOKENS.json`. On its first run it found nine fourth-wall breaks in shipped prose and two current-state documents asserting superseded values | 2026-09-20 |

Note the deliberate difference in word counts: `verify.py` reports **3,848** and
`style_gate.py` sums to **3,848**. They extract prose slightly differently — the gap is a
small near-constant per chapter (9-19 words), not a divergence in what either one measures.
`STATUS_PANEL.md`
uses the **style_gate** figures — keep it that way or the two will appear to disagree.

---

*Writing rules for whoever rewrites this: never "as previously discussed" — there is no
previously. Never "recently" — give the date. If unsure whether something is still true,
mark it `[unverified]`. Shorter is better; a handoff nobody reads protects nothing.*
