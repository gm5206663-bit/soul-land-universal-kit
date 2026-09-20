# STATUS PANEL — SOUL LAND 2 · THE UNRAVELED TIDE
### The single source of truth for where this story is.
**If any other file disagrees with this panel, that file is wrong. Repair it the same turn.**

**Live edge: after Chapter 21 — "Round One."**

---

## 0. Re-rail (2026-09-20)

The governance layer was rebuilt after a corpus audit found **four files carrying
four different live edges** (codex header: "Chapter 21 written … pre-Chapter 1";
codex chapter list: "Chapter 21 NEXT"; status file: "through Chapter 15";
continuation prompt: "through Chapter 8"). The live edge is **Chapter 21**, which
exists and is written. Every status claim below now traces to the codex's
per-chapter "Ranks:" lines and the Chapter 21 character-states tail. Design-era
numbers that the serialization superseded are flagged in place, not deleted.
Receipt: `audits/2026-09-20_RE_RAIL_RECEIPT.md`.

---

## 1. Latest written artifacts

- Latest prose: `chapters/chapter_21.md` — **Round One** (canon 17-2/3 held; the
  corrected Group One shape; the floor; the bear team; the debrief; the names).
- Codex record: `THE_CODEX.md` "Chapter 21: Round One (WRITTEN)" — canon
  receipts, the floor, the 90-second round, "Ranks: 17-peak / 23 / 29, Group
  One at 4-0."
- OC dossier: `JIANG_CHE_STATUS.md` v4.2 (synced to this edge).
- Mirror: `../CODEX/06_PROJECT_SOUL_LAND_2.md` (byte-identical to THE_CODEX.md;
  verify with a hash before trusting it).

---

## 2. Source position

- Canon consumed through **canon ch 17-3** (the dual-control spar and the
  kite-flying held whole; the bear team = canon's own first-round texture).
- Next source boundary: **canon ch 17-3/4** (the knockout bracket; Ma Xiaotao
  at the grounds; the ring hunt — all still *not triggered*).
- Next fic chapter: **Chapter 22.**

---

## 3. Current scene after Chapter 21

- Group One is **4-0** in the first round; the year's rumor is running
  ("Group One rearranges the ground and the ground wins"); the names are
  multiplying (the courier, the weather, the hammer, the boring one).
- The corrected shape is running: Group One is the room plus Xiao Xiao —
  Yuhao's field, Wang Dong's correctness, Xiao Xiao's cauldron, the courier's
  floor: the four-part machine canon's trio always needed, completed.
- The courier holds the medics' corner; the damage-ledger is running;
  nineteen mends today, eleven minutes of fighting, four wins.
- The prince's official position: "very dangerous, extremely handsome,
  *sorry about the bell*."

## 4. Character states (end of Chapter 21)

| Who | State |
|---|---|
| **Jiang Che** (the courier) | Rank **17-peak**; two yellow rings (Overlord Vine, Sun Flower — see canon ledger); the floor; the medics' corner; 19 mends; the damage-ledger running |
| **Huo Yuhao** | Rank **23**; Class One monitor; the field; the fish stall; the sect's third |
| **Wang Dong** | Rank **29**; kills *correctly*; the bear bet collected; the butterfly named |
| **Xiao Xiao** | The cauldron; the flute **held all day** (her decisive fight is later, per her doctrine) |
| **Tang Ya** | Sect master; the grill; "excellent sect work"; the sect's economics alive |
| **Bei Bei** | The first disciple; the dragon of blue lightning; the gentlest dangerous |
| **Ma Xiaotao** | The red veil; the pink eyes; not at the grounds yet (not triggered) |
| **Xiao Jiu (the fox)** | Present in every scene; the tactical reads; the True Cascade running; her years L4-sealed |

**Ranks line (source of truth for rank, from the codex chapter records):**
**17-peak / 23 / 29** — unchanged through Chapters 17–21; the 20 wall (the
third ring) is the next growth gate and has not been reached.

---

## 5. Power law (the construction)

Jiang Che is not a normal soul master whose stats a talent modifies; **he is a
construction of the Adaptation Talent** — every level, ring and breath built by
it since conception. The AT is never visible, never voiced, non-sentient, and
**never named in prose.** Its expression in this holder is martial-soul-centered
(the Blue Silver Tide Grass is a living adaptation project: LIFE core, WATER
carrier, LIGHT feeder). Rings integrate to 100% (Perfect-Integration Law);
the clean current is **never the poison path** (hard lock). Ring-config law:
rings 1–2 yellow, 3–4 purple, 5–7 black; the third ring is **reserved** as the
20-wall event and is a story, not a stat.

> **SUPERSEDED DESIGN NOTE:** the codex Quick Reference and the v4.1 status
> file describe "arrives already BUILT (rank ~25, two rings)." The serialization
> opened at Chapter 1 with him at **rank 10, two yellow rings**, and the
> per-chapter records carry the real trajectory (17-peak by Ch17–21). The
> design number is kept for provenance, flagged here, and is **not** a live
> value. Do not write "rank 25" as current.

---

## 6. Firewalls (who knows what) — see `KNOWLEDGE_FIREWALLS.md`

- **L1** — the AT is invisible to everyone, including the boy (he experiences
  results, never the engine).
- **L4** — the white ring / the ice worm's choice: the reader and the fox know;
  the public story is "a baboon and a lucky ring"; Yuhao's public account is
  "shock of his first kill."
- The fox's true years are sealed; the True Cascade (the red veil / Ma Xiaotao's
  fire) is the fox's archive, not shared.
- **No romance is pre-decided.** Nothing is aimed.

---

## 7. Next (Chapter 22)

1. Read `foundation/NO_MISTAKE_LIVE_RULES.md` and this panel.
2. Research-first: fetch canon **ch 17-3/4** (the knockout bracket; Ma Xiaotao
   at the grounds; the ring-hunt setup) from the primary source — do not write
   from memory.
3. Write the canon coverage receipt **before** prose.
4. Set the chapter's panel endpoints before dates.
5. Preserve the ranks line (17-peak / 23 / 29) unless the canon beat earns a
   change — the third ring is **not** triggered here.
6. Run `verify.py` (chapter gate + `--project`) and the selftest before calling
   it done; update this panel, the codex record, the dossier, the manifest and
   the mirror in the same turn; log it in `SERIAL_LOG.md`.

## 8. Gate status

- Chapter gate (`verify.py chapters/`): **22/22 PASS** (2026-09-20, gate v2.1).
- Project sweep (`verify.py --project .`): clean hard gates; CJK now lives in
  `foundation/CANON_LEDGER.md` (the glossary), not in chapter files.
- Selftest (`selftest.py`): **22/22** — every defect still caught, apparatus
  digits still exempt, CJK in a chapter still fatal.
