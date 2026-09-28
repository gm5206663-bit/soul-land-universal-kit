# CHAPTER 22 VALIDATION — "Knockout Brackets"
### Soul Land 2 · The Unraveled Tide. 2026-09-20. (SL4-style per-chapter
### validation, adopted for SL2 from `soul_land_4_fire_phoenix` footers.)

Status: **PASS** — after a post-push self-audit against the rest of the
author's corpus (SL4 footer standard, SL3, the SL2 chapters 1–21). Seven
micro-fixes applied to `chapters/chapter_22.md` before this receipt; gate
re-run green.

## 1. Gates (post-fix)

- Chapter gate `verify.py chapters/`: **23/23 PASS** (Ch22 included; 0
  failures).
- Project sweep `verify.py --project .`: **PASS — all hard gates clean**.
- Selftest `selftest.py`: **22/22** (no checker weakened; the fix pass
  touched prose only, no gate edits).
- Prose length: ~2,887 words (above the 2,500 v15 floor).

## 2. Canon beats — receipt → on-page → verdict

| Beat (receipt source) | On-page in Ch22 | Verdict |
|---|---|---|
| Bracket's posting: top sixty-four from the one hundred fifty (Ch17 draft receipt) | Panel 1 — the boards, the tree, the cut of the cut | PASS |
| The eighty-six crossed out (150 − 64, the draft's arithmetic) | Panel 1 — "eighty-six more names"; Panel 5 count | PASS |
| Champion's prize "extremely rare" (Ch17 draft receipt) | Panel 1 — re-read at the board; contents left two words | PASS |
| Ma Xiaotao at the venue (codex 17-4 note; Ch14/18/19 receipts) | Panel 2 — the red line, the brazier's quiet, the whisper; no interaction with the room | PASS |
| Inner court lore: red = inner court, top ten, its own ground (Ch19 receipt) | Panel 2 — "the inner court's ground where the outer school's chalk did not reach" | PASS |
| "Fire control so precise — a fire-attribute soul?" (Ch18 debut receipt) | Panel 2 — the whisper grown a day of venue; kept the outer school's wrong answer | PASS |
| The ring-hunt setup: the prize, the window, the shape (Ch15/16 receipts) | Panel 4 — the ledger's page: wall at thirty, forest south, water-kin, Sun Flower's precedent, the seed question; **NOT YET** | PASS |

## 3. The twelve locks — checklist

1. **Era** — PASS (no era-mixing; Shrek/Tang Sect/soul-tools texture only).
2. **Protagonist** — PASS (no prodigy rings beyond the two yellow; no second soul; AT never his identity on-page).
3. **Canon entry** — PASS (17-4 beats on-page; the named beats from lock 3 all still intact in the record).
4. **Spine** — PASS (the sect's survival crisis stays the antagonist; the stall's loop feeds it).
5. **Power ceiling** — PASS (no rank change; the wall at thirty named, not reached; the third ring a story, not a stat; no unearned mastery).
6. **Identity** — PASS (public: Jiang Che, the courier, third disciple, Class One, Room 108; private layers held).
7. **Absolutes** — PASS (author go given: "next chapter"; English-only, zero CJK — gate-verified; no measurement digits in prose — gate-verified; no nerf, no unearned inflation; corrections receipted — this file).
8. **Canon immunity** — PASS (Ma Xiaotao's beat is presence, not an event on her; her later fate untouched; the Ch18 blink stays a blink).
9. **Measurement** — PASS (rank state only in the codex lines + panel; prose carries words: "twenty-six", "twenty-nine" never spoken as numbers; the wall "at thirty" in words).
10. **Voice** — PASS (multi-panel, 5 panels / 4 POVs; ≥3 spoken lines per panel; Person Law beats: the coal, the fish's turn, the not-calm texture; no lecturing, no kit-recap, no author-winks — the tic scan below is the receipt).
11. **Cadence** — PASS (~2,887 words; gate green before "done"; state synced same turn; log entry same turn).
12. **Handoff** — PASS (panel is the live edge; the continuation prompt points at the panel; the Chapter-23 guard now sits in the chapter tail).

## 4. Provenance audit (the SL4 practice, adopted)

- **Receipt-sourced (author's files):** the bracket's structure and the
  eighty-six cut (Ch17 draft receipt) · the prize (Ch17) · Ma Xiaotao's
  debut texture, the inner-court lore, the borrowed-turtle banking (Ch14/18/19
  receipts) · the hunt's shape (Ch15/16 receipts, including "the forest
  south, the water-kin beasts his father had hunted for twenty years, the
  Sun Flower's precedent") · the ninety seconds, the names, "the ground
  wins", the fox's two-dangerous-teams beat (Ch21 tail).
- **OURS (flagged in the coverage receipt, none replacing canon):** Group
  Forty-Seven and its word "the watching" (a designed canon-lawful ensemble
  team — record only; no members, souls, or fate given) · the stall's coal to
  the forge (the year's little closed loop) · the eraser (image only).
- **Checked and NOT used:** the later-canon material surfaced by the research
  passes (the continental-tournament arc: the Judgment Sword, the Sun Moon
  Team, the Holy Spirit Cult's later use of her, the Black Phoenix) — **zero
  leakage into the prose**; the chapter knows her only as the Ch14-19 receipts
  know her.
- **No in-world clock invented** beyond the established "Assessment day two"
  (Ch21 = day one).
- **No character gains information from author knowledge:** the room's read
  of Group Forty-Seven comes from the board (an empty ledger) + Yuhao's
  established 50 m detection + the fox's Ch21 beat; the courier's read of the
  red comes from the receipts' texture ("fire control so precise") as a
  structure-read; the hunt's page is his own plan (Ch15 texture: "he was
  planning it"), not omniscience.

## 5. Forbidden future / currentization avoided

- The prize's contents (stays two words).
- Group Forty-Seven's members, souls, fate, or the match's result (Ch23).
- The hunt's departure and its target (the departure is at the wall at
  thirty; he is 29).
- Ma Xiaotao's later arc (the Judgment Sword, the Black Phoenix, the cult) —
  surveyed, not used.
- The knockout's second line or beyond.
- Any rank change; the wall at thirty not reached; the 18-verge held at
  "verging" (Yuhao), not crossed.
- Xiao Xiao's flute (the lid stays on).

## 6. Self-audit fixes (2026-09-20, after the push, against the corpus)

Comparison targets: `soul_land_4_fire_phoenix` (SL4 footer standard),
`Soul_Land_3_Project`, `soul_land_holy_spirit` / `blue_silver` /
`soul_land_devouring_dragon`, and SL2 chapters 1–21 (voice/tic baseline).

| # | Found | Fixed |
|---|---|---|
| 1 | "the room — all four of it, because the room was four now" — conflated the room (three) with Group One (four) | "the four of Group One — the room plus Xiao Xiao, the four-part machine the first round had finished proving" |
| 2 | "the year would need a word for" motif used 3× in one chapter (a tic against the Ch21 baseline) | cut to 1× (the fox's doctrine payoff, kept deliberate) |
| 3 | "a noise like a market deciding what to be afraid of" — paralleled Ch21's "a market having a nightmare" too closely | "a noise like a market that had found out what day it was" |
| 4 | "the brazier at the stall's coals" — garbled image | "the stall's brazier" |
| 5 | "a sixth-year's wrist from yesterday's draw" — chronology error (the draw was Ch17, several days before day one) | "carried over from the first round" |
| 6 | "the grill's last coal went under" | "went out" |
| 7 | The closing paragraph reused three of Ch21's signature sentences near-verbatim (back-to-back chapters) — the "Same time" refrain kept (deliberate series echo), the rest rewritten | new close; the refrain stays |

**Tic scan after fixes:** "the year would need a word" 0 · "cadence that was
theirs" 0 · "load-bearing comfort" 0 · "yesterday" 0 · "a market" 1 (varied) ·
"the year will need a word" 1 (kept, deliberate).

**Format verdict vs siblings:** head (title + Canon Reference + Timeline +
rule) and tail (Summary / Canon Preserved / Tests Run / Character States)
match the SL2 in-project format of chapters 1–21 — kept. SL4's minimal-head /
rich-footer shape was NOT imported (project-internal consistency wins over
cross-project mimicry); SL4's *disciplines* were imported (this receipt, the
Chapter-23 guard in the tail, the provenance/forbidden-future checks below,
and the per-chapter validation step added to panel §7). SL3/SL4 rank-digit
habits in prose were NOT imported (they are exactly what gate 4 exists to
catch — the standing R3 corpus ruling covers them).

## 7. State sync (same turn, hash-verified mirror)

Panel (after Ch22) · codex Ch22 record · manifest (edge 22, patterns all
match) · continuity debts (prize's contents added; bracket/ma-xiaotao rows
updated) · dossier v4.3 · serial log · `CODEX/06` mirror (sha256 identical).

## 8. Chapter 23 guard

As written in the chapter tail: open on the morning of Group One vs Group
Forty-Seven; canon 17-5 research-first; the carry-forward list and the
do-not-consume list bind Ch23's writing.
