# RAILS — the standing rules of this project

Adopted from SOUL_LAND_BOOTSTRAP.md on 2026-09-09. Every future document and chapter in
this project obeys these. If prose would break a rule, stop and ask the author.

## R1 — Canon honesty
- Tag everything: `[canon]` / `[design]` / `[user ruling]`.
- Never present invention as canon. Absence in what we read is not absence in the source.
- User rulings override and are recorded in CANON_LEDGER.md with their date.
- Evidence tiers: 1 original novel text · 2 official donghua/manhua · 3 official database
  · 4 fan wiki / encyclopedia (pointer only) · 5 secondary coverage. Receipts record tier.

## R2 — Prose hygiene
- English only. ZERO CJK anywhere, including file names.
- Exact figures only in panels, ledgers, tables, footers. Prose uses round/felt numbers.
- Real line breaks only; no literal backslash-n artifacts.
- No TODO/FIXME/placeholder residue in finished documents (templates may hold placeholders).

## R3 — Story law (author-locked)
| Law | Locked? | Text of the law |
|---|---|---|
| {FILL — e.g. mercy / no killing} | {no} | |
| {FILL — powers dormant until earned} | {no} | |
| {FILL — no staging of major canon-beat meetings before readiness} | {no} | |
| {FILL} | {no} | |

A law becomes binding the turn the author locks it. Broken law = stop, ask, fix.

## R4 — Process
- One source of truth per topic (bible); mirrors update the same turn.
- STATUS_PANEL current at the end of every working turn; SERIAL_LOG appended every turn.
- OPEN questions move to bible when decided, same turn.
- No chapter until the author says. Corrections before content. "Verify everything" means
  a full project audit in one pass.

## R5 — Naming (upload-safe)
- File/folder names: ASCII letters, digits, underscore, dot. No spaces, no specials, no CJK.
- Story names: clean Latin names, no collision with major canon names unless intended and
  flagged. Never use characters that break chats or file systems ( / \ : * ? " < > | ).
- Renames happen everywhere, in one turn.

## R6 — Portability
- Plain Markdown, relative references only, no external dependencies. The project must be
  recreatable from SOUL_LAND_BOOTSTRAP.md in a fresh chat.
