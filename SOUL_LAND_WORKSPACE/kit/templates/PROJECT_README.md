# <PROJECT NAME> — <one-line premise>

### <Era>. <Protagonist>. Created <date>.
### Not the <other project> story. Other projects are REFERENCE ONLY — craft, never canon.

---

## WHAT THIS IS

<One paragraph. What the story is, who it follows, where it sits in the timeline.>

**Status:** <FOUNDATION / DRAFTING / LIVE EDGE CHAPTER N>

---

## AUTHORITY ORDER

```
1. The user's explicit words
2. This project's locked docs (NO_MISTAKE_LIVE_RULES.md)
3. SOUL_LAND_UNIVERSAL_KIT laws (method and continuity)
4. SOUL_LAND_UNIVERSAL_KIT canon spine (verified world facts)
5. Any earlier project — craft reference ONLY, never canon
```

---

## THE LIVE EDGE

**Chapter N — "<title>"**

Single status source: `foundation/STATUS_PANEL.md`
Single continuity ledger: `foundation/CONTINUITY.md`

---

## FILE MAP

```
foundation/
  STATUS_PANEL.md          THE single status source
  CONTINUITY.md            THE single continuity ledger
  NO_MISTAKE_LIVE_RULES.md the locks, current after chapter N
  CANON_NOTES.md           receipts and confidence tags
  CANON_LEDGER.md          every canon beat touched, and how
  SERIAL_LOG.md            per-chapter record
codex/
  CHARACTERS.md  TIMELINE.md  PLACES.md  KNOWLEDGE_FIREWALLS.md
chapters/
  Chapter_NN_<Title>.md
audits/
  <date>_<subject>.md
```

---

## THE TWELVE LOCKS

Set before drafting. See `02_PROJECT_SETUP.md`.

```
 1. ERA            —
 2. PROTAGONIST    —
 3. CANON ENTRY    —
 4. SPINE          — "___ wants ___ from my protagonist, and will ___ to get it."
 5. POWER CEILING  —
 6. IDENTITY       —
 7. ABSOLUTES      —
 8. CANON IMMUNITY —
 9. MEASUREMENT    —
10. VOICE          —
11. CADENCE        —
12. HANDOFF        —
```

---

## VERIFICATION

```
python3 tools/verify.py chapters/
```

A chapter is not done until this passes with zero failures.
