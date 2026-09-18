# HANDOFF — READ THIS FIRST IN A NEW CHAT

_Created 2026-09-03 after Chapter 101 was written, gated, synced, and presented, and after the Layer-6 rebuild (PROBLEM_INVENTORY BF3). This file is the cold-start brief: it tells a fresh agent (with a fresh, empty session memory) how to stand the project up and keep writing. The workspace itself remains the source of truth — this file points, it does not replace._

**KICK-OFF MESSAGE (paste this, with the zip uploaded, as your first message in the new chat):**

> I've uploaded `Soul_Land_3_Project_handoff_2026-09-03.zip` — my continuing fanfiction project (Soul Land 3 / Legend of the Dragon King, OC-first). Unzip it, read `HANDOFF.md` first and follow the RESTORE PROTOCOL exactly, then read the briefing files it names. When the verification line is green, tell me the position line and stop — we'll proceed to chapter 102 together.

---

## 1 · RESTORE PROTOCOL (do exactly this, in order)

```bash
unzip Soul_Land_3_Project_handoff_2026-09-03.zip -d /home/user   # creates /home/user/Soul_Land_3_Project
cd /home/user/Soul_Land_3_Project
python3 checks/state.py      # re-derive state from the 101 chapter footers -> checks/state.json
sh checks/run_all.sh        # THE gate. Must end green: every layer reports 0 FAIL.
```

**Expected:** 101 chapters on disk · end state `rank 45 · sp 2824 · hawk 3199 · ledger 168` · all nine layers 0 FAIL (zero_tolerance, presence_audit, workspace_audit, sync_audit, completeness_audit, divergence_engine, world_tick, voice/prose layers, prewrite_board). If anything is red, STOP and read PROBLEM_INVENTORY.md's newest block before touching anything — do not "fix" a red by weakening a checker (see §7, the BF3 law).

Then read, in this order:
1. **`BRIEF.md`** — the machine-generated cockpit, already aimed at chapter 102.
2. **`CONTINUATION_PROMPT.md`** — the story constitution: position, the Butterfly Law v2, the Spectator Test, the All-or-Nothing State Line, the locks, the read-list for THE_CODEX / CHARACTER_STATS / DIVERGENCE_LEDGER / STYLE_GOLD.
3. **`LIN_HAO_STATUS.md`** top block — who Lin Hao is right now.
4. **`PROBLEM_INVENTORY.md`** — read the CURRENT open list only (its own warning explains why).
5. This file's §3–§6 (pipeline + laws that postdate the CONTINUATION_PROMPT).

## 2 · WHAT THIS PROJECT IS

A 101-chapter (and counting) fanfiction of *Soul Land 3: Legend of the Dragon King*, built OC-first: **Lin Hao** (ice/wind/water/lightning + the father's-iron sword, four rings incl. one BLACK, effective Soul Emperor baseline) walks beside canon's Tang Wulin class — but canon is the SPINE, not the script (**Butterfly Law v2**). Every chapter is one canon chapter spent as **ore** (fetched, distilled to `canon_extract/chapters/canon_NNN.txt`), derived through our divergences, gated by a nine-layer check suite, and followed by a ten-document sync ritual. Voice: close-third, arithmetic-as-soul, grain-reads, perspective panels from other characters' own eyes. Story prose ≥ 2,800 words. All numbers trace to `CHARACTER_STATS.md` §1 or are labelled AU.

**Position at handoff: end-canon-286 · 101 chapters · all layers green.**
Chapter 101 "What the Sword Was" = canon 286: the lake lesson (weapon intent's first test passed vs a live master), the promotion ("we confer"), the love ledger spoken once, the two-word armor dream set, the Spirit Pagoda history fed to thread D22.

## 3 · THE CHAPTER PIPELINE (every chapter, no exceptions)

1. **`python3 checks/brief.py`** — MANDATORY STEP 0. Regenerates `BRIEF.md` aimed at the next chapter. Never write from a stale brief.
2. **`python3 checks/prewrite_board.py`** — the USE-EVERYTHING board (laws, traits, kit, live wires with last-used stamps, locks). Answer the world-pressure items and the FORWARD-TICK in your head before drafting.
3. **FETCH THE CANON CHAPTER AS ORE** (§4 below). Title-verify. Distill to `canon_extract/chapters/canon_NNN.txt`. If fetch fails: try mirrors in order, then queue and tell the user — never write from memory of canon, never build on teasers.
4. **WRITE THE CHAPTER** (`chapters/chapter_NN.md`). Header declares the canon span. Voice targets from BRIEF (dialogue %, cliff rotation, 1–2 gold patterns, LH ≥ 4 turns, presence ≥ 5 markers). Footer contract: rank/SP/hawk/ledger ALL-or-nothing (Law gg) · SPECTATOR TEST: PASS · 🦋 BUTTERFLIES SHOWN · WIRES: SPENT/ALIVE/RESTED · D-rows cited.
5. **`python3 checks/voice_check.py N`** — before sync; catches ghost gate (<5 presence markers).
6. **`python3 checks/state.py && sh checks/run_all.sh`** — expect the known S-FAILs pre-sync (docs still point at the old chapter); anything else red = a real defect, fix at source.
7. **THE SYNC RITUAL** (ten docs, same turn): CONTINUATION_PROMPT · CHARACTER_STATS §0 · LIN_HAO_STATUS · LIN_HAO_PANELS · THE_CODEX (QUICK REF + Current Ranks + any law that moved) + CODEX/05 twin · CANON_ACCESS (range + NEXT) · BUTTERFLY_REGISTRY · RELATIONSHIPS (events + core rows — see Law yy) · POWER_MODEL (stations) · WORLD_STATE (named actors) · PROBLEM_INVENTORY (session block). Then `python3 checks/build_butterfly_effects.py` and re-run run_all to green ×2.
8. **`present_file` the chapter** — the user reads it in the viewer.
9. Core rows and headings refresh EVERY sync (Law yy) — appends are not updates.

## 4 · CANON FETCH QUICK CARD

- **Full method + history: `CANON_ACCESS.md`. Master title index: `canon_extract/CANON_INDEX_23_600.txt`** (the board prints the expected title).
- **NEXT: canon 287 "Black Steamed Buns"** — novelfull slug `chapter-287-*.html` (novelfull numbering = canon+0); novelhall ID **10716132** (novelhall numbering = canon same, IDs sequential from 266=10716111). Title-verify every fetch.
- Mirror status at handoff: **novelfull works**; novelhall flaky; readnovelfull/recipe v2 and freewebnovel history in CANON_ACCESS; ceritasilu dead. Wuxiaworld proper = ~150-word teasers — **never build on teasers**.
- Disk range: canon 229–286 held (`canon_extract/chapters/`). Fetch 287 BEFORE writing ch102 — canon is ore, fetched fresh, never recalled from model memory.

## 5 · LAWS THAT POSTDATE THE CONTINUATION_PROMPT (verbatim standing user corrections)

- **(yy) THE STALE-CORE CATCH (09-03):** user: "You don't even update the relationship list single time… nothing added after ~ch68… please check others Also." Finding: RELATIONSHIPS cores frozen at ch79 under 21 chapters of appends; THE_CODEX Current Ranks stale (repeat offender). **LAW: append-only docs rot at the core — appends are not updates. Core rows/headings refresh EVERY chapter-sync; when rot is found in one doc, sweep siblings for the same disease.** (Machine-enforced: Layer 6 heading-staleness guard + Layer 3 sync_audit.)
- **(zz) THE UTILIZATION MANDATE (09-03):** user: "check everything like literally everything… you don't use everything — check everything, USE everything, and do everything." **LAW: every organ gets USED — banks extended, genealogy mapped at birth, live power classes in POWER_MODEL, named world actors get WORLD_STATE rows.** (Machine-enforced: Layer 9 `checks/completeness_audit.py` — banks ≤6 ch old; STORM/break threads genealogy-mapped; power-bible coverage; brief targets.)
- **(BF3) THE RED-TEST LAW (09-03):** a structural edit to any checker MUST be followed by a deliberate RED-test (break something real, watch the checker catch it) before green is trusted — a checker edited into a no-op still prints green. This bit three times (see PROBLEM_INVENTORY BF1–BF3).
- Known soft spot, flagged for the next carry: the Layer-6 **voice-tic list is the restored known subset** ("on the record" class) — extend it from a chapter sweep at the next carry audit.

## 6 · CHAPTER 102 SPECIFICS (canon 287 "Black Steamed Buns")

The registration morning; the working students' first day; **the arranged apology to Elder Cai — her RELATIONSHIPS page's VERDICT is owed here, and the disciple question ("which door did you take?") gets its answer**. Canon 286 left these loaded: Shen Yi's counsel; Wulin arranging the apology; the DISCIPLE door named; the boys'/girls' rooms; "working student isn't an easy thing" (hidden tone); the two-word armor decision (simplest piece first, name it with two words — **seam: our Wulin's rings = three + the blood ring; canon's "two rings" figure is NOT imported**). Expect Bun-adjacent dining-hall texture per the title. Voice: pick the dial from BRIEF and say which; the ch101 cliff was short-stark — rotate.

**Key numbers at handoff:** LH rank 45 · SP 2,824 · hawk 3,199 · ledger 168 HELD ("after the elders, before the continent") · smith 5th (Master Craftsman) · trials 70 · 🔴 weapon intent promoted ("we confer") · Emperor baseline, ceiling UNREVEALED. Ensemble: Wulin 28 · Xie Xie 33 · Gu Yue 31 · Xu Xiaoyan 30 — all five working students, Shrek outer court. Storm clocks: D24 first payment ch101 · D22 biggest meal ch101 · D23 fed · D17/W01 paid big ch99–100. **HELD list (carry): see CONTINUATION_PROMPT header** — the registration · the apology · Cai's verdict · the disciple answer · dorms/duties · D23's word · CCC-D · the summons' reply · the letter · the tin · Old Tang · the seal NAME (never) · the duel conditional · the sword to Shen Yi · Na'er · Gu Yue's nature · WZK origin · armor worn · fusion door · blade forger · what answered · the ape · Mu Chen's first · the giver · "Divine Stormbringer" (cancelled) · the Union opening · Feng Wuyu · the Sixth.

## 7 · SHARP EDGES (recent, from PROBLEM_INVENTORY — read the file for the full set)

- **Never repair a checks file by string-splice surgery** — rewrite the whole file deliberately, imports included (BF1–BF3 class).
- Insert new checks BEFORE the `for x in fails` detail loop, or fails count but never print.
- Expected S-FAILs exist only pre-sync; a post-sync red is a real defect. Never weaken a guard to pass it.
- Heredocs: emoji in escape form; anchor reads via f-string tails; one block per write behind `count==1` assertions.
- E2B/network outage mid-chapter → the queued-fix workflow (finish the turn, queue the repair, tell the user).
- The workspace is the source of truth. Session memory lies by omission; files don't.

---

*End of handoff. Everything else lives where it should: the laws in CONTINUATION_PROMPT and THE_CODEX, the debts in PROBLEM_INVENTORY, the voice in STYLE_GOLD, the numbers in CHARACTER_STATS and checks/state.json. Write chapter 102 the way the project writes chapters: derive, don't obey — and don't manufacture.*
