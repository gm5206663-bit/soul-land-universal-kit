# RE-RAIL RECEIPT — 2026-09-20
### Soul Land 2 · The Unraveled Tide (Jiang Che)

**Trigger:** full-corpus audit (five repos) found four files carrying four
different live edges and a gate that failed every chapter for apparatus read
as prose. **Author's instruction (2026-09-20):** Size 2 re-rail — keep the
story, re-lay the governance; fix the gate's scope; review before push.

## 1. Live edge — resolved

| File | Before | After |
|---|---|---|
| `THE_CODEX.md` header | "CHAPTER 21 WRITTEN … Status: FOUNDATION LOCKED (pre-Chapter 1)" | v15.2 · LIVE — after Chapter 21 "Round One" |
| `THE_CODEX.md` chapter list | "Chapter 21: (NEXT …)" unmarked | marked SUPERSEDED (pre-write plan, preserved) |
| `THE_CODEX.md` Quick Reference | "rank ~25, two rings" (design era) | flagged SUPERSEDED (serialization: rank 10 at ch1; 17-peak at ch21) |
| `JIANG_CHE_STATUS.md` | "through Chapter 15 · v4.1" | "through Chapter 21 · v4.2" + dated correction note |
| `CONTINUATION_PROMPT.md` | "through Chapter 8" + "then write Chapter 2" | points at `foundation/STATUS_PANEL.md`; next = Chapter 22; ghost `/home/user/…` paths fixed |

The single source of truth is now `foundation/STATUS_PANEL.md`.

## 2. Files written (new)

| File | sha256 (16) | Size |
|---|---|---|
| `README.md` | `4e78418d0b35b498` | 3,788 B |
| `foundation/STATUS_PANEL.md` | `98e94a8040f20fca` | 6,471 B |
| `foundation/CURRENT_STATE_MANIFEST.json` | `2eb65abadf2fb418` | 3,183 B |
| `foundation/NO_MISTAKE_LIVE_RULES.md` | `7b9e7d625b050161` | 5,442 B |
| `foundation/KNOWLEDGE_FIREWALLS.md` | `3bf51fb907b51dd6` | 3,480 B |
| `foundation/CANON_LEDGER.md` | `c646f58bac7ab1e5` | 5,590 B |
| `foundation/CONTINUITY.md` | `1f7f830e09dec301` | 2,119 B |
| `foundation/SERIAL_LOG.md` | `b9b5427c9c58e6ac` | 3,433 B |
| `foundation/OPEN.md` | `309123fc0420df3a` | 2,379 B |
| `THE_CODEX.md` | `ba2577fba5bfbbfb` | 131,763 B |
| `JIANG_CHE_STATUS.md` | `f72f9e6347cd4081` | 12,794 B |
| `CONTINUATION_PROMPT.md` | `a032bf97f1e79160` | 6,319 B |
| `../CODEX/06_PROJECT_SOUL_LAND_2.md` | `ba2577fba5bfbbfb` | 131,763 B |
| `../SOUL_LAND_UNIVERSAL_KIT/tools/verify.py` | `d74587dd920ed336` | 23,281 B |
| `../SOUL_LAND_UNIVERSAL_KIT/tools/selftest.py` | `73b774beacccfc95` | 17,401 B |

## 3. Chapter hygiene (22 files)

43 recorded edits — full verbatim ledger: `2026-09-20_HYGIENE_CHANGE_LEDGER.md`.
- 15 CJK spans moved to `foundation/CANON_LEDGER.md` §E (canon-title glossary);
  two dialogue lines translated (OPEN ruling R2 — author may veto).
- 169 bookkeeping marks (✓/✅) removed from chapter tails; the test
  assertions they marked remain as text.
- 7 measurement numerals converted to words (rank ten / twenty-nine /
  twenty-three, six-forty, two against one). Name-digits (Room 108) kept per
  OPEN ruling R1.
- **No story sentence was rewritten.** Prose word count: 75,705 → 61,618 is
  the gate's story-only count (apparatus excluded), not a loss.

## 4. Gate — unified and re-proven

Two files named `verify.py` (a 288-line chapter gate and a 93-line project
scanner, divergent) reconciled into one, v2.2, installed byte-identical in
all three kit locations; both originals archived under
`_archive/2026-09-20_gates_unified/` (never deleted).

What changed in the gate, and how each change is pinned:
- Apparatus boundary (title / metadata head / bookkeeping tail / fences) is
  explicit and **announced** in the output (`[apparatus: head+tail]`).
  Red-tested: a closing paragraph with no apparatus signal is still story
  and its digits still fail.
- Head may carry quoted canon titles (SL3 shape) — red-tested both ways.
- Name-digits exempt (Room 108, Dorm333, ch 17); measurement digits
  (rank 29, 6:04, year 163) still fatal — red-tested.
- CJK remains fatal file-wide in chapters — red-tested (the corpus fix is in
  the files, not the checker).
- Dialogue counts curly quotes (Gate A's rule, kept).
- Filename law now admits the corpus's own date-hyphen convention
  (OPEN ruling R4).

**selftest.py: 22/22 — every defect still caught.**

## 5. Verification (this run)

- Chapter gate `verify.py chapters/`: **22/22 PASS, 0 failures**
  (22 PASS lines).
- Project sweep `verify.py --project .`: **VERDICT: PASS — all hard gates
  clean** (CJK in 8 foundation/codex docs reported as advisory, ruling
  pending R3).
- Mirror `../CODEX/06_PROJECT_SOUL_LAND_2.md` == `THE_CODEX.md` (same sha256).
- Gate selftest at all three install locations: PASS.

## 6. Open (in `foundation/OPEN.md`)

R1 name-digits · R2 the two dialogue translations · R3 corpus-wide mark
convention (SL3 carries 826) · R4 filename-law hyphens. Canon checks 2–5.

**Live edge after this receipt:** after Chapter 21 "Round One."
**Next:** Chapter 22 (canon 17-3/4) — on the author's go.

## Addendum (2026-09-20, same day, after the author's flag)

The receipt's row "rank 10 at ch1; 17-peak at ch21" carried the re-rail's
rank-mapping error: **17-peak is Yuhao's rank (verging 18); Jiang Che's Ch21
edge is 29 (the wall at thirty)**. The serialization's own text is the source
(ch15 record + ch15/16 prose, cited in the correction). All governance files
were repaired the same turn; the hygiene and gate claims in this receipt are
unaffected. Full correction record: `foundation/SERIAL_LOG.md` +
`foundation/STATUS_PANEL.md` §0 + manifest `known_corrections`.
