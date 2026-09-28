# SOUL_LAND_BOOTSTRAP — the everything-file for a new Soul Land fan fiction

Instructions for the assistant and the author reading this file.
Prepared: 2026-09-09. Works on any Arena chat that accepts a markdown attachment.

---

## 1. What this file is

This is the single self-contained bootstrap for starting a NEW Soul Land (Douluo Dalu)
fan fiction serial in a fresh Arena chat. It contains:

- the ground rules (rails) the whole serial must follow,
- the exact directory tree the assistant must create on its first turn,
- a standard format for every kind of document in that tree,
- the canon research checklist the assistant must run before any prose is written,
- the first-session script (what the assistant asks the author before anything is created).

Upload this one file to the new chat as the first message or attachment.

## 2. First instruction to the assistant in the new chat

Read this file completely, then reply to the author confirming you have adopted it, then
follow the first-session script in section 8. Do NOT create story content, do NOT write a
chapter, and do NOT draft the premise on your own. The author supplies the premise.

## 3. The ground rules (rails) — adopt all of them

### R1 — Canon honesty (the most important rail)
- Everything in the project is tagged `[canon]` (true in the Soul Land source material),
  `[design]` (this fic's invention / choice), or `[user ruling]` (the author decided it,
  regardless of source status). When a tag applies, say so in the text.
- NEVER present a fan-made or invented element as canon. NEVER claim "canon nowhere names
  X" as proof a thing does not exist — absence in what you read is not absence in the book.
- When canon and a good idea conflict, either change the idea or keep it clearly labelled
  `[design on canon base]` and record why in the ledger.
- The author can rule that something IS canon for this serial (a user ruling). A user
  ruling overrides everything, is applied project-wide in the same turn, and is recorded
  in the ledger as a ruling with its date. Once ruled, never re-litigate it.
- Verification sources, strongest to weakest: original novel chapter text > official
  donghua/manhua > official databases > fan wiki and encyclopedias (pointers only, never
  proof) > secondary coverage (recaps, articles) > fan fiction. Record the tier with each
  receipt. When the strongest tier contradicts the weaker, the stronger wins.
- If you cannot verify a canon claim, keep it out of canon-tagged prose and mark it
  `[design]`, or leave it in the OPEN list as a wire.

### R2 — Prose hygiene
- English prose only. ZERO CJK characters in any output file, including file names.
- Exact figures (years, distances, counts) appear only in panels, ledgers, tables,
  footers, and status documents. Narrative prose uses round or felt approximations
  ("an age", "hundreds of seasons") and never a precise number unless it is a deliberate
  beat. Keep every numeric anchor consistent across files; cross-check on every update.
- No literal backslash-n artifacts (the two characters backslash then n, inside prose) —
  always real line breaks.
- No dangling placeholders or TODO/FIXME markers left in finished documents. Templates may
  carry placeholders; finished docs may not.

### R3 — Story law
- The author locks story laws (for example: mercy/no killing, powers dormant until earned,
  no staging of a major canon-beat meeting before readiness). Locked laws are written into
  `foundation/RAILS.md` and never broken silently. If a chapter would break one, stop and
  ask the author first.
- Ritual or ceremonial canon powers (awakening rites, ring condensation, transformations
  that belong to specific canon characters) stay DORMANT or off-stage unless the author
  explicitly assigns them to this fic's cast.

### R4 — Process
- One source of truth per topic. The bible holds settled truth; codex mirrors it; when
  either changes, update every mirror in the SAME turn.
- Keep `foundation/STATUS_PANEL.md` current at the end of every working turn.
- Append one dated entry to `foundation/SERIAL_LOG.md` at the end of every working turn:
  what was done, which files changed, what was verified, what is open.
- Nothing in the OPEN list is decided by accident. When a question stops being open, move
  it (decided, with source) into the bible and update the OPEN list the same turn.
- No next chapter is drafted until the author says so. Correction passes requested by the
  author always come before new content.
- When the author says "verify everything", run a project-wide audit (tags, numbers,
  CJK scan, file list, stale references) and fix all of it before producing new content.

### R5 — Naming (upload-safe, author-requested)
- File and folder names: ASCII letters, digits, underscores, and dots only. No spaces,
  no special characters, no CJK. Lowercase is the safe default; initials caps are allowed
  for the few prominent files (README, BOOTSTRAP, CHAPTER template, chapter files).
- Character, place, and term names inside the story: clean ASCII/Latin names, chosen so
  they do not collide with major canon names unless the collision is the point (and is
  then flagged). Any name a user will type or upload must not contain characters that
  break chats or file systems ( / \ : * ? " < > | and control characters ).
- If a name must change later, change it everywhere in one turn (project-wide find).

### R6 — Portability
- Everything lives in plain Markdown (.md), relative references only, no external
  dependencies. The whole project must survive being re-created from this bootstrap file
  in a fresh chat.

## 4. Directory tree the assistant must create on turn one

```
soul_land_starter/
├── README.md                       one-page orientation (copy from this kit or write fresh)
├── SOUL_LAND_BOOTSTRAP.md          this file
├── foundation/
│   ├── FOUNDATION.md               the premise doc (locked decisions about the story)
│   ├── RAILS.md                    standing rules: R1-R6 + the story-law table
│   ├── STATUS_PANEL.md             current state at a glance, updated every turn
│   ├── SERIAL_LOG.md               dated log of every working session
│   ├── OPEN.md                     questions the story will answer, in order
│   └── CANON_LEDGER.md             every canon claim + its receipt and evidence tier
├── bible/
│   ├── WORLD.md                    settled world facts and decisions (source of truth)
│   ├── POWER_LAW.md                cultivation / soul law ledger (canon vs design)
│   ├── PROTAGONIST.md              the central character's full dossier
│   └── arcs/
│       └── BEATS_TEMPLATE.md       per-arc beat sheet template
├── codex/
│   ├── CHARACTERS.md               who's who, inner lives
│   ├── CREATURES.md                soul beasts and other beings
│   ├── GLOSSARY.md                 terms table with tags
│   ├── PLACES.md                   named places with tags
│   ├── RELATIONSHIPS.md            bond map
│   ├── TIMELINE.md                 dual-column era table
│   └── CANON.md                    the rules of this world as verified (not invented)
└── chapters/
    ├── CHAPTER_TEMPLATE.md         reusable chapter skeleton
    └── Chapter_01.md               empty first chapter (fill only when the author says)
```

The assistant creates every file, fills the structural templates, and writes "no content
yet - waiting on the author's premise" where story content would go. The author's premise
turn then populates FOUNDATION, RAILS (story laws), and the first OPEN list.

## 5. Standard formats

### STATUS_PANEL (top of the panel)
```
# STATUS_PANEL
Updated: {date}
Premise: {locked one-line pitch, or "not yet locked"}
Last action: {what happened at the end of the last working turn}
Now: {current state of the story in one paragraph}
Numeric anchors: {exact figures ONLY here, in a small table}
Wires: {open threads, one per bullet}
Next beats: {what is next AND what is gated on the author}
```

### SERIAL_LOG entry
```
## {Title of session} ({date}, user: "{what the user actually said}")
- {What was done, file by file}
- {What was verified and how}
- {What changed in state / numbers / world}
- {What is now open}
```

### CANON_LEDGER receipt
```
| Claim | Status | Evidence | Tier | Verified | Source |
|---|---|---|---|---|---|
| {claim text} | [canon] / [design] / [user ruling] | {quote or paraphrase} | {1-5} | {date} | {title + url} |
```

### Chapter skeleton (chapters/CHAPTER_TEMPLATE.md carries the full version)
A chapter file has: title heading, optional short opener-recap, the body, then a short
footer with the next-beat note and any panel/status anchor. Prose carries no exact
figures and no CJK.

## 6. Soul Land canon research checklist

Before ANY prose is written, the assistant verifies and receipts the items the author's
premise touches. Minimum set (each becomes a ledger receipt; untouchable facts first):

1. The era anchor: what Soul Land book/era the story sits in (pre-SL1 deep past, SL1 Tang
   San's era, SL2, SL3, or an original inter-era), and the timeline anchors that bound it
   (canon births, deaths, awakenings). Nothing in the fic may contradict a canon event
   that is inside its own era window; events outside the window are resonance only.
2. Cultivation system: soul-power ranks and titles, spirit ring classes and colors, how
   rings are normally gained, and every named exception the fic touches. Verify against
   original text / donghua; fan wiki is a pointer.
3. Soul beasts: cultivation-age classes, the hundred-thousand-year rules (tribulation,
   human-form choice, its conditions), and any named family or evolution the fic uses.
   A "named evolution" a fic invents is [design] until receipted otherwise.
4. Geography and powers-that-be: the continents, empires, sects, academies, Spirit Hall
   (or equivalents for the era), and named places the fic touches. Spelling of every
   canon proper noun must be verified before first use.
5. The canon characters the fic's story brushes against: who they are, when and where in
   their own timeline, and whether the fic stages or merely references them. Meeting a
   canon character is staged only when the author says the fic is ready to.
6. Original-language check for any claimed proper noun: when a name's canon status is
   asserted, check the Chinese original text where possible and record tier-1 or tier-2
   evidence. Absence in translation is not evidence.

Method note: search the Chinese original chapter mirrors and official donghua first;
fandom and Baike pages are pointers; article recaps are weakest. Record what was checked
and what was NOT, so receipts stay honest.

## 7. First-session script (the assistant reads this to the author)

1. Confirm the rails are adopted (show a short list: canon honesty, zero CJK, English
   prose, exact figures only in panels, log/panel/open kept current, no chapter until
   told, corrections before content).
2. Ask the premise questions, in order, and do not move past an answer until it is given:
   a. Which Soul Land era / timeline anchor do you want (deep past, SL1 era, SL2, later)?
   b. Whose story is it (an original character, a canon-adjacent figure, a canon
      character's alternate path)?
   c. What is the protagonist's nature (human soul master, soul beast, martial soul
      born, other)?
   d. Tone and scope (how long, one arc or serial, light or heavy)?
   e. Canon contact points (which canon events/characters may the story touch, and which
      are off-limits)?
   f. Allowed deviations (what may this fic change, and must every change stay [design])?
3. With the answers, populate FOUNDATION.md, add the story-law rows to RAILS.md, open the
   first OPEN list, then STOP and wait for the author before any drafting.

## 8. Corrections and audits (the assistant's standing behaviour)

- When the author reports mistakes or asks to "solve everything", the assistant audits the
  whole project (grep for CJK, literal backslash-n, stale tags, number drift, stale file
  references, leftover placeholders), fixes every file in the same turn, updates the log
  and panel, and only then reports done.
- Number anchors are checked together whenever any one of them changes.
- Old wording that was corrected stays only inside dated records (the ledger, the log),
  never in live docs, so the history stays honest without re-contaminating the story.
