# Soul Land Projects

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
| [`blue_silver/`](blue_silver/) | *Blue Silver* — a pre-canon serial about a Blue Silver Emperor grass named Home. 15 chapters, ~33,100 words, Book One complete | **Book One complete** |
| [`sl4_fire_phoenix/`](sl4_fire_phoenix/) | *Fire Phoenix* — an SL4-era serial, Yan Shuo'er, Lan Xuanyu's cohort | In progress (edge: Ch31) |
| [`SOUL_LAND_NEW/`](SOUL_LAND_NEW/) | An earlier separate OC project, and the franchise-neutral craft base the kit extends | Reference |
| [`reference/sl3_lin_hao/`](reference/sl3_lin_hao/) | An SL3-era project, kept for reference | Reference |
| [`soul_land_starter/`](soul_land_starter/) | A scaffold for starting a new serial | Scaffold |
| [`uploads/`](uploads/) | Incoming handoff packs and working files from earlier sessions | Archive |

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

---

## Licence and takedown

This is non-commercial fan fiction, published in good faith. If you are a rights holder and
want any part of this removed, open an issue and it will be taken down promptly.
