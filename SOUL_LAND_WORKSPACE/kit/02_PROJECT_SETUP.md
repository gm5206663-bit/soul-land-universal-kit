# 02 — PROJECT SETUP

Opening a new serial. Do all of this **before** drafting chapter one. Every step here is
cheap now and expensive later.

---

## THE FILE TREE

```
your_project/
├── README.md                    ← authority order, file map, live edge
├── foundation/
│   ├── STATUS_PANEL.md          ← THE single status source
│   ├── CONTINUITY.md            ← THE single continuity ledger
│   ├── NO_MISTAKE_LIVE_RULES.md ← the locks, current after chapter N
│   ├── CANON_NOTES.md           ← receipts and confidence tags
│   ├── CANON_LEDGER.md          ← every canon beat touched, and how
│   └── SERIAL_LOG.md            ← per-chapter record
├── codex/
│   ├── CHARACTERS.md
│   ├── TIMELINE.md
│   ├── PLACES.md
│   └── KNOWLEDGE_FIREWALLS.md
├── chapters/
│   └── Chapter_01_….md
└── audits/
    └── <date>_<subject>.md
```

Copy `templates/` into `foundation/` and fill it in. Do not invent your own layout — the
layout is what lets a fresh agent orient in one read.

### Two rules about the tree

**One status source.** `STATUS_PANEL.md` is the only file that states current rank, rings,
age and position. Every other file derives from it. The moment two files both claim to be
current, one is stale and nobody knows which.

**Filename law.** ASCII letters, digits, underscores and dots only. No spaces, no special
characters, no non-ASCII. Upload-safe names survive transfer between agents and platforms;
pretty names do not.

---

## THE TWELVE LOCKS

Set these before drafting. Write them into `NO_MISTAKE_LIVE_RULES.md`. Anything you cannot
answer now will be answered by accident later, and the accident will be in chapter forty.

```
 1. ERA            — which series, which years, which DC range
 2. PROTAGONIST    — who, and explicitly what they are NOT
 3. CANON ENTRY    — the specific canon beats this serial touches (name ≥5)
 4. SPINE          — who wants what from the protagonist, and what they'll do
 5. POWER CEILING  — the strongest the OC becomes, and what they never get
 6. IDENTITY       — public name vs true name; what the reveal costs
 7. ABSOLUTES      — what the protagonist will never do, ever
 8. CANON IMMUNITY — which canon characters' fates may not be rerouted
 9. MEASUREMENT    — how rank and rings are shown on the page
10. VOICE          — POV, tense, register rules
11. CADENCE        — chapters per pass, words per chapter, when audits run
12. HANDOFF         — what a fresh agent must read first
```

### Lock 4 is the one that matters most

Write it as a full sentence with all three blanks filled:

> **"______ wants ______ from my protagonist, and will ______ to get it."**

Blue Silver shipped 90,000 words without one. The rebuild's entire engine was filling that
sentence in: *Spirit Hall wants rings from the soul beasts of Star Dou, and sends hunters
into the forest to take them* — and the protagonist is a soul beast living in that forest.
One sentence, and suddenly fifteen chapters had a spine.

If you cannot fill the blanks, you do not have a story yet. You have a setting.

---

## THE STATUS PANEL

The single source of truth for current state. See `templates/STATUS_PANEL.md`.

Required fields, minimum:

```
LIVE EDGE        — the last chapter that counts, by number and title
PROTAGONIST      — name(s), rank, soul power, rings held (colour + source beast)
POSITION         — where they physically are
KNOWN BY WHOM    — who knows what about them
FORBIDDEN NOW    — what has NOT happened yet, with the chapter it is reserved for
```

That last field is the one people omit and the one that saves you. "No third ring yet —
reserved for chapter 40" stops chapter 22 from granting it because the scene wanted one.

---

## THE CONTINUITY LEDGER

See `templates/CONTINUITY.md`. Required:

- **The anchor table.** Every dated event, by chapter. One row each. This is what you check
  new dates against *before* writing them.
- **The forward references.** Every "X years later" and "she would not learn until" claim,
  with the chapter that pays it off.
- **The character register.** Everyone named, with first and last appearance.

The anchor table is the most valuable single artifact in the kit. Set the panel endpoints
for a chapter first, then write every in-chapter date against the table. See
`08_CONTINUITY_LAW.md` for why this is non-negotiable.

---

## WHAT GOOD SETUP LOOKS LIKE

A finished setup is maybe 2,000 words across four files. It should take an afternoon.

The failure mode is the opposite: 25,000 words of world bible before chapter one exists.
That is procrastination with a file extension. Set the twelve locks, write the panel, draft
chapter one, and let the codex grow from things that actually happened on the page.

**Nothing enters the codex until it happens in a chapter.** A codex full of things that
never appear is a lie you maintain at your own expense.
