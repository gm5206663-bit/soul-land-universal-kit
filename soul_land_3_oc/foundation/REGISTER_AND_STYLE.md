# REGISTER AND STYLE — the voice, the gate, and the pre-ship drill

> **R11 is the law this file serves:** the register objects are the **Fire Phoenix project's own chapters** (the author's proved voice) with *The Golden Lion* ch 1 as sibling — read them before writing; write in that voice or do not write. This file records what that voice measures, how our chapters have measured against it, and the exact drill every chapter passes before it ships.

## 1 · The register objects

- **Primary:** the Fire Phoenix corpus — the author's own serial, read as law (living mirror: `scratch/repos/storyos-site/` — read-only; the `_archive/2026-09-30_park/` copies; `SL_ARCHIVE/sl4_foundation_v2/` notes). Measured signature: avg 8–9 / median 6–7, fragments and one-line paragraphs carrying rhythm, dialogue-forward.
- **Sibling:** *The Golden Lion* ch 1.
- **Method, never copy:** from the corpus we take voice, structure, and discipline — never text, never scenes. Receipts of what was learned live in `SERIAL_LOG` and the ledgers.

## 2 · What the voice does (the working rules)

1. **Short declarative sentences, beat by beat.** Fragments allowed and welcome as structure ("Gold." / "The habit.").
2. **Scenes, not essays.** Open on the child or the day; world facts arrive in short plain paragraphs, then get out of the way.
3. **Dialogue-forward; kid-logic; dry adults.** Children talk like children; adults answer deadpan.
4. **Emotion stated plainly, one line at a time.** "He did not blame the child." "He stayed." No literary narrator, no aphorism stacking.
5. **Motifs repeat verbatim as structure** (ours, so far: *"We are still richer than most."* · *"Nine ranks to go."* · the sea working at the harbor wall · the water tap · the one line in the back of the practice book · two kitchens · *"The pig earns its bowl."*).
6. **Plain similes only, sparingly.** No ornate metaphor chains, no precious images — if a line sounds like a quiet English novel instead of a Soul Land serial, it fails whatever its numbers say.
7. **Endings: short, warm, forward.**

## 3 · The measured gate (hard caps)

| Gate | Cap | Tool |
|---|---|---|
| Sentences over 60 words | **0** | `tools/measure_sl3p.py <chapter>` |
| "the way" per chapter | **≤ 2** | `grep -o "the way"` |
| CJK characters in prose | **0** | same tool |
| Dialogue-forward | yes — dialogue paragraphs in the 50s–70s for a full chapter (our range so far) | same tool |
| Average sentence length | SOFT — house range 11–14 so far; the number is necessary, the voice is the point (R11) | same tool |
| Voice target (new chapters, R21) | **ALL avg ≤ 12 (aim 8–10), median ≤ 8** — the register object's own band (the author's serial, measured live 2026-10-02: 8.6–9.8 / med 6–7; ch1–ch5 drifted 11.1 → 17.3) | same tool |
| Numbers as stat-speak | none | read-through; R8 |

**Measured history (final bodies):**

| Chapter | Words | ALL avg/med/o60 | NARR avg/med/o60 | Dialogue paras | CJK | "the way" |
|---|---|---|---|---|---|---|
| Ch 1 — *The Reading* (v5) | 4,263 | 11.1 / 8 / 0 | 11.6 / 8 / 0 | 58 | 0 | 2 |
| Ch 2 — *The House and the Road* | 5,677 | 13.9 / 11 / 0 | 15.8 / 13 / 0 | 60 | 0 | 2 |
| Ch 3 — *A Bowl and a Name* | 6,881 | 13.6 / 9 / 0 | 15.6 / 12 / 0 | 70 | 0 | 0 |
| Ch 4 — *A Thousand Times* | 9,788 | 12.3 / 10 / 0 | 14.4 / 12 / 0 | 101 | 0 | 0 |

## 4 · The header block (every chapter)

`# Chapter N: Title` then one blockquote carrying: **Canon reference** (which SL3 chapters, fetched when, where) · **the beats carried** (the full list, so a reader can check fidelity at a glance) · **Dual track** (what the OC parallel does in this chapter) · **Seals kept** (LSP-10 · R13/DRG-01 · NAE-02 — and what else applies) · **canon rows cited** · **the receipts pointer** (`canon_coverage/…`). Then a `**Timeline:**` line. Then the chapter. It ends `*End of Chapter N.*`

## 5 · The pre-ship drill (in order — no skips)

1. **Fetch** the canon block live; read it fully (R1). Record the beat list.
2. **Write** (R11 register; R12 dual track; **R15 — mark each canon beat public · private · parallel · butterfly-touchable, choose the felt butterflies *before* prose (`foundation/CANON_BUTTERFLY_PROTOCOL.md` §2/§6), and read the open obligations in `bible/BUTTERFLY_LEDGER.md` for this window**; seals from `KNOWLEDGE_FIREWALLS`). **2b. The two-engine blueprint (R21 — `foundation/HOW_TO_WRITE.md`):** canon beats marked public/private/parallel/touchable; **the OC beats written as events** (want · obstacle · cost · outcome); the collision seams named; the lock-4 sentence written — *Su Yan wants ___, and ___ stands in the way, and it will cost ___.*
3. **Measure:** `python3 tools/measure_sl3p.py <chapter>` — fix every over-60 and every "the way" past 2.
4. **Style pass script** (if needed): exact old strings only; anchor-grep before writing; a MISS exits and **the chained commit silently skips** — verify `git log` after any chain.
5. **Receipts:** `canon_coverage/Canon_Coverage_Chapter_0N.md` (beat tables, handling notes, seals, metrics) + ledger updates (`LSP`, `SP`, `PAIR`, `HOUSEHOLD`) + `SERIAL_LOG` entry + `audits/Chapter_0N_audit.md` + **the butterfly pass:** every touched ledger line's *last echo* updated, new lines entered **with their obligations named at birth**, what fell due paid (or closed dated **Quiet**), and the chapter's **deletion-test answer** written into the coverage doc. **5b. The R21 tests (into `audits/Chapter_0N_audit.md`):** **the actor test** (in his scenes: doing, or watching/filing/noting?) · **the reaction test** (name the canon character whose behavior changed because he was there) · **the event count** (≥ 2 value-changes, ≥ 1 costing something real). **5c. The panels:** `SU_YAN_STATUS` (**the win-copy — rebuilt from the chapter itself, same turn; H13: the status file is the state, never a pointer sheet**) · `RELATIONSHIPS` · `TIMELINE` · `CANON_CHARACTER_STATE` — refreshed the same turn (the author's own directive: *"update everything, everytime"*). **H14:** every claim in them is line-checked against the page it cites before delivery.
6. **One commit**, chained: `cd /home/user/kit && python3 <script> && git add --sparse -A && git commit -m "…"`.
7. **Verify:** `git log --oneline -2`, `git status --porcelain` clean, greps for each new artifact, re-measure if any chapter text changed after the last measure.
8. **Present** the chapter; report in the author's register: canon carried, OC parallel, seals, metrics, receipts. Never claim more than the files show.

## 6 · The standing tooling

- Measure tool: `tools/measure_sl3p.py` — ships with the serial (the build-time working copy was `/home/user/scratch/measure_sl3p.py`, same tool).
- Applied scripts live in `/home/user/scratch/` — **never re-run an applied script.**
- Sparse checkout; stage with `git add --sparse -A`; repo identity `arena-agent`.
