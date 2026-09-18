# CODEX — live index for `chapters_rebuilt/`

**This directory is LIVE continuity.** The seven files in `bluesilver_codex/` are SUPERSEDED
and must not be read as continuity.

**Authority order:**
1. The user's words
2. `bluesilver_foundation/REBUILD_CONTINUITY.md` — the authoritative ledger
3. This codex — derived views of that ledger
4. `chapters_rebuilt/` — the text itself
5. `SOUL_LAND_UNIVERSAL_KIT/` — method and law

Where this codex and `REBUILD_CONTINUITY.md` disagree, **the continuity file wins.**

---

## What lives where

| File | Contents |
|---|---|
| `CHARACTERS.md` | Home, A Yin, the nine named humans, the beasts, kill count |
| `TIMELINE.md` | the 1837 anchor, anchor table, fixed events, canon reconciliation |
| `PLACES.md` | the valley, the glade, grid nineteen, the bands, distance matrix |
| `RELATIONSHIPS.md` | the bond map, the two refusals, the human chain |
| `GLOSSARY.md` | ground-language (fixed at eleven words), abilities, Hall vocabulary |

## Not duplicated here

| Subject | Lives in |
|---|---|
| Canon receipts and citations | `bluesilver_foundation/CANON_NOTES.md` |
| Beast law, ring tiers, Titled Douluo | `bluesilver_bible/BEAST_LAW.md` |
| The seven-point chapter contract | `bluesilver_foundation/REBUILD_PLAN.md` |
| Standing rules | `bluesilver_foundation/NO_MISTAKE_LIVE_RULES.md` |
| Method, prose law, audit gates | `SOUL_LAND_UNIVERSAL_KIT/` |

These are **live, not superseded.** Do not copy their contents into this codex — a second
copy is a second thing to drift.

---

## The story in one breath

A Blue Silver Emperor grass breaks soil in a hunted forest in ≈1837 DC. He learns within a
year that his world runs on rings — that beasts die so humans can advance. He decides, at
year 98, in front of a friend, that he will not participate. He keeps a seam for four
centuries. He invents a language of eleven words with two other beings, both of whom die of
age. He refuses twice to take what is offered him. He walks twenty-one years to a valley
where 391 of his kind were harvested in single seasons, and refuses it too. A being forty
thousand years older than him, who has been counting the dead alone for four centuries,
gives him a name: **Home**.

**Kill count: zero. Fifteen chapters. Seven hundred and fifty-three years to the naming.**

---

## The premise and why it is hard

A plant protagonist in a franchise built on hunting. Three structural problems, and how the
rebuild solved each:

| Problem | Solution |
|---|---|
| A plant cannot act | ground-listening, the root-mass, the keeper's post |
| A plant cannot speak | ground-language — eleven words, tap → pulse → stamp |
| Nothing contests a plant | **the forest is hunted.** Spirit Hall, contracts, grids, seals |

The third is the one the rejected draft never used. Canon says Star Dou is a hunting ground.
A serial set there in which nobody hunts is not Soul Land.

---

## Beings at a glance

| Being | Years | Fate |
|---|---|---|
| Home (the protagonist) | 0–775+ | named at 753 |
| the mantis | 61–104 | natural death |
| the shadow cat | 163 | **maimed, survives** |
| the night-walker | 301–468 | dies at his edge — **REFUSAL 1** |
| the found one | 402–630 | dies of age |
| the liar | 592 | caged, **released** |
| the nine great ones | 735– | eight remain |
| the old king | –746 | natural death — **REFUSAL 2** |
| A Yin | 753– | names him |

## Humans at a glance

Nine, all named, all with a decision. **None killed.**

surveyor (~193) · thin man (~243) · Pell (~360) · Kesh (~440) · Orrin Vase (~508) ·
Drem (~592) · Ilen Marr (~700) · Tefer Hallum (~751) · Berrit Ohn (~753)

---

## Verification

Run before calling any chapter or codex file done:

```
python3 SOUL_LAND_UNIVERSAL_KIT/tools/verify.py blue_silver/chapters_rebuilt/
```

**Current result: 15 files, 33,100 prose words, 0 failures, 0 warnings.**

The three codex files with prose-facing constraints (`CHARACTERS.md`, `TIMELINE.md`,
`PLACES.md`, `GLOSSARY.md`) were checked for unreadable script, literal backslash-n and
placeholder text: all clean.

---

## What is still open

- The nine human dossiers live here and in `REBUILD_CONTINUITY.md` §4. They are not yet
  mirrored into the superseded `bluesilver_codex/CHARACTERS.md`, and should not be — that
  file is history.
- `CREATURES.md` has no live replacement. Beast detail is in `CHARACTERS.md` §THE BEASTS and
  in `bluesilver_bible/BEAST_LAW.md`. A separate live creatures file is not currently needed;
  create one only if beast detail outgrows the characters file.
