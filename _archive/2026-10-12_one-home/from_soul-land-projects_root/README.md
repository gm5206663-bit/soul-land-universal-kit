# Soul Land Projects

> ⛔ **ARCHIVED 2026-09-23 — READ-ONLY.**
> This repository duplicated five paths of the live workspace byte-for-byte
> (`SARA.md`, `SOUL_LAND_NEW/`, `blue_silver/`, `soul_land_starter/`,
> `SOUL_LAND_UNIVERSAL_KIT/`) — exactly the two-copies staleness problem this
> workspace's own laws warn about. The **live public workspace is
> [`soul-land-universal-kit`](https://github.com/gm5206663-bit/soul-land-universal-kit)**.
> Nothing was deleted; the repository is frozen as-is for provenance. Details:
> `soul-land-universal-kit/README.md`, addition dated 2026-09-23.

A working archive of original **Soul Land (Douluo Dalu)** fan fiction, plus the reusable
authoring kit those serials were built with.

Everything here is **derivative, non-commercial fan work**. Soul Land / 斗罗大陆 and all its
characters, settings, and terms belong to **Tang Jia San Shao (唐家三少)** and the original
rights holders. Nothing here is official, and nothing here is for sale.

---

## What is in this repository

| Path | What it is | State |
|---|---|---|
| [`SOUL_LAND_UNIVERSAL_KIT/`](SOUL_LAND_UNIVERSAL_KIT/) | A portable, era-agnostic authoring kit — world canon, story law, prose law, audit gates, templates, and a working verification script | **Complete, verified** |
| [`seed_of_creation/`](seed_of_creation/) | *Seed of Creation* — an SL2.5-era serial: the son of the God of Destruction and the Goddess of Life, sealed and fallen to Douluo when the Divine Realm is swept away | **Foundation — scaffolded, four rulings pending, no chapters** |
| [`blue_silver/`](blue_silver/) | *Blue Silver* — a pre-canon serial about a Blue Silver Emperor grass named Home. 15 chapters, ~33,100 words, Book One complete | **Book One complete** |
| ~~`sl4_fire_phoenix/`~~ → [`_archive/2026-09-19_stale_sl4_copy_at_ch31/`](_archive/2026-09-19_stale_sl4_copy_at_ch31/) | *Fire Phoenix* — Yan Shuo'er, Lan Xuanyu's cohort. ⛔ **ARCHIVED 2026-09-19:** this copy was stale at Ch31 and byte-identical to a copy already archived in `soul-land-universal-kit` (172/172 files, zero unique content). The live project is at **Ch52** in the private repo `gm5206663-bit/soul_land_4_fire_phoenix` | Superseded — do not read |
| [`SOUL_LAND_NEW/`](SOUL_LAND_NEW/) | An earlier separate OC project, and the franchise-neutral craft base the kit extends | Reference |
| [`reference/sl3_lin_hao/`](reference/sl3_lin_hao/) | An SL3-era project, kept for reference | Reference |
| [`soul_land_starter/`](soul_land_starter/) | A scaffold for starting a new serial | Scaffold |
| [`uploads/`](uploads/) | Incoming handoff packs and working files from earlier sessions | Archive |

> **`_archive/` — DO NOT USE.** Added 2026-09-19. Holds superseded material that must never be
> read as current. `_archive/2026-09-19_stale_sl4_copy_at_ch31/` is the stale Chapter-31 copy of
> Soul Land 4 Fire Phoenix; the project itself is at Chapter 52 elsewhere. Moved by `git mv` —
> 172 renames, all `R100`, zero deletions, zero content changes. Each directory carries a
> `README_STALE_ARCHIVED.md`.

---

## Start here if you want to write with this

```
SOUL_LAND_UNIVERSAL_KIT/00_START_HERE.md
```

The kit is the most transferable thing in this repo. It exists because a 90,000-word serial
was written and then rejected for five specific, diagnosable reasons — and each of those
five failure modes is now made structurally impossible by a rule and a check.

The short version of the thesis: Soul Land fan fiction fails in five ways, and each one is
catchable before it costs you a rebuild.

1. **No canon spine** — nothing from the source world actually happens
2. **Nothing contested** — no antagonist with a face
3. **No felt progression** — ranks and rings never move on the page
4. **One register repeated** — the same narrative voice for fifteen chapters
5. **Apparatus outgrowing story** — panels and ledgers longer than the fiction

Run the gate before calling any chapter done:

```bash
python3 SOUL_LAND_UNIVERSAL_KIT/tools/verify.py path/to/chapters/
```

Prove the gate itself works before trusting it:

```bash
python3 SOUL_LAND_UNIVERSAL_KIT/tools/selftest.py
```

---

## Reading order for the fiction

*Blue Silver* is the most finished serial. Start at
[`blue_silver/HANDOFF.md`](blue_silver/HANDOFF.md), which says what is current and which
directories are live versus superseded, then read
[`blue_silver/chapters_rebuilt/`](blue_silver/chapters_rebuilt/).

Note that `blue_silver/chapters/` is a **rejected earlier draft**, kept for history. It fails
29 automated gates. The live text is `chapters_rebuilt/`.

---

## Honesty conventions used throughout

Every project here tags its claims, because the fastest way to break a long serial is to
quietly confuse invention with canon.

| Tag | Meaning |
|---|---|
| `[canon]` | Verified against source material or multiple independent secondary sources |
| `[fan]` | Widely repeated and plausible, but not verified against primary text |
| `[disputed]` | Sources disagree; a reading was picked and recorded |
| `[design]` | Invented for this project, permitted by canon but not stated in it |
| `[user ruling]` | Settled by the author; outranks every other tag |

No claim in these projects was verified against the original Chinese text. `[canon]` here
means "multiple secondary sources agree," which is a weaker guarantee than it sounds like.
Where a plot depends on a mechanic, the files say so and ask you to re-check.

---

## Known imperfections

Stated plainly rather than buried:

- The human rank ladder in `SOUL_LAND_UNIVERSAL_KIT/01_CANON_SPINE.md` was checked against
  Baidu Baike EN, anime setting summaries, and fandom rank tables, which agree — but rank
  names vary by translation, and the file lists the variants rather than pretending one is
  correct.
- The beast-law rows in that same file rest on **one** compiled source, not independent
  agreement. They are the weakest thing in the kit and are labelled as such.
- Superseded directories are bannered rather than deleted. Nothing here has been quietly
  rewritten; corrections are stamped with what they replaced.
- The kit's `01_CANON_SPINE.md` is **SL1-weighted**. `seed_of_creation/` works in the SL2.5 era,
  which that file does not describe, so the project carries its own era receipts in
  [`seed_of_creation/foundation/CANON_NOTES.md`](seed_of_creation/foundation/CANON_NOTES.md),
  flags its seven single-source rows by name rather than letting them carry plot, and states plainly
  that its DC anchor is **derived arithmetic with a ±25-year margin**, not a canon date.
- That same project records a premise collision rather than hiding it: canon states, in the God
  of Destruction's own quoted words, that he and the Goddess of Life cannot have a child — and
  the protagonist is their son. It is logged as a user ruling over canon, with the cost written
  down, and the story is built on the contradiction instead of around it.

---

## Licence and takedown

This is non-commercial fan fiction, published in good faith. If you are a rights holder and
want any part of this removed, open an issue and it will be taken down promptly.
