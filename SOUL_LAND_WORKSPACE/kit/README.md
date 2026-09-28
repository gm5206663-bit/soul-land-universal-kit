# SOUL LAND UNIVERSAL KIT
### A complete authoring foundation for Soul Land (Douluo Dalu) fan fiction.
### Era-agnostic. OC-agnostic. Built to be dropped into a new project and followed.

Created 2026-09-18. Distilled from four working serials:

| Source | What it donated |
|---|---|
| **SL4 Fire Phoenix** (189,000 words, 31 chapters) | The mature method: butterfly protocol, anti-nerf lock, knowledge firewalls, live-rules discipline, status-panel parity |
| **Blue Silver** (33,120 words, rebuilt) | What failure looks like: the five-point diagnosis, spine law, five-register rule, and the date-endpoints-first continuity law |
| **SOUL_LAND_NEW** | Franchise-neutral craft distillation (METHOD.md) |
| **SL1 Gu Yuan** | Long-haul ledger discipline at ~98 chapters |

---

## WHAT THIS IS

A foundation, not a story. It contains:

1. **The world** — verified canon spine, so no agent invents mechanics that don't exist.
2. **The method** — how to write, distilled from what actually worked.
3. **The laws** — the locks that prevent the specific failure modes these serials hit.
4. **The templates** — so project setup takes minutes, not a day.
5. **The tooling** — a verification script, because quality that isn't checked isn't real.

It does **not** contain a premise, a protagonist, or a plot. Those are yours to choose.

---

## AUTHORITY ORDER

When anything contradicts anything else, this is the resolution order. Write it into your
project's README so a future agent doesn't have to guess.

```
1. The user's explicit words           (highest — always)
2. This project's locked docs          (the locks you set in 02_PROJECT_SETUP)
3. This kit's laws                     (method and continuity law)
4. This kit's canon spine              (verified world facts)
5. Any earlier project                 (craft reference ONLY — never canon)
```

Rule 5 is the one agents break. An earlier serial's OC, dates, ranks and relationships are
**not** importable. What is importable is craft: pipeline, audit culture, ledger discipline.

---

## HOW TO USE IT

Four steps. Do them in order.

**Step 1 — Read `00_START_HERE.md`.** Fifteen minutes. It tells you what to read next and
what to decide first.

**Step 2 — Set your locks (`02_PROJECT_SETUP.md`).** Before a single word of prose: era,
protagonist, canon entry point, what you will never do. Projects that skip this drift.

**Step 3 — Copy `templates/` into your project.** Fill in the status panel and the
continuity ledger. These are your two sources of truth; everything else derives from them.

**Step 4 — Write, then verify.** Every chapter runs `tools/verify.py`. The gates are not
optional and they are not negotiable, because every failure in §2 of `03_STORY_LAW.md`
shipped through a chapter that "looked fine."

---

## FILE MAP

```
SOUL_LAND_UNIVERSAL_KIT/
├── README.md                  ← you are here
├── 00_START_HERE.md           onboarding, read order, the pre-chapter gate
├── 01_CANON_SPINE.md          the verified world: ranks, rings, beasts, factions, eras
├── 02_PROJECT_SETUP.md        opening a new serial: file tree and the twelve locks
├── 03_STORY_LAW.md            spine law, causality, the five failures, progression
├── 04_CANON_BUTTERFLY.md      how canon and your divergence coexist
├── 05_POWER_LAW.md            anti-nerf, measurement parity, no plot armor
├── 06_KNOWLEDGE_FIREWALLS.md  who knows what, and what must stay protected
├── 07_PROSE_LAW.md            language, registers, panel discipline, filename law
├── 08_CONTINUITY_LAW.md       the date-endpoints-first rule and one-source-of-truth
├── 09_AUDIT_LAW.md            the audit loop and the hard gates
├── 10_HANDOFF_LAW.md          handing off without regressing
├── templates/                 copy these into your project — destination in brackets
│   ├── PROJECT_README.md          [project root]
│   ├── HANDOFF.md                 [project root]
│   ├── STATUS_PANEL.md            [foundation/]
│   ├── CANON_LEDGER.md            [foundation/]  highest-authority file
│   ├── CONTINUITY.md              [foundation/]
│   ├── NO_MISTAKE_LIVE_RULES.md   [foundation/]
│   ├── CANON_NOTES.md             [foundation/]
│   ├── CHARACTERS.md              [codex/]
│   ├── TIMELINE.md                [codex/]
│   ├── PLACES.md                  [codex/]
│   ├── KNOWLEDGE_FIREWALLS.md     [codex/]
│   ├── CHAPTER_TEMPLATE.md        [chapters/]
│   └── SERIAL_LOG.md              [audits/]
└── tools/
    ├── verify.py              the gate script — run it on every chapter
    └── selftest.py            proves the gate has teeth — run after editing verify.py
```

**Run `python3 tools/selftest.py` after any edit to `verify.py`.** It builds throwaway
chapters containing one known defect each, and confirms every one is caught. A gate that
passes everything verifies nothing, and the only way to know a gate works is to feed it
something broken.

**Every file the laws tell you to create has a template.** If a law says "record this in
`codex/TIMELINE.md`", the template is in `templates/TIMELINE.md`. There are no files you are
told to make and left to invent.

---

## THE ONE-PARAGRAPH VERSION

Soul Land fan fiction fails in five specific ways, and this kit exists because all five were
committed in a single 90,000-word serial: **no canon spine** (nothing from the source world
actually happens), **nothing contested** (no antagonist with a face), **no felt progression**
(ranks and rings never move on the page), **one register repeated** (every chapter sounds the
same), and **apparatus outgrowing the story** (status panels and ledgers longer than the
scenes). The kit's job is to make each of those structurally impossible — through locks you
set before drafting, a per-chapter contract you check before writing, and a script you run
before shipping.

Everything else here is detail.
