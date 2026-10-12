# LAN SHEN

A dual-track reincarnation serial set in **Soul Land 3: The Legend of the Dragon King**
(Douluo Dalu 3), by Tang Jia San Shao. Non-commercial fan work — see
[NOTICE.md](NOTICE.md).

> **V2 EPOCH — canon-parallel rebuild in progress · 2 chapters shipped and gated ·
> 8,779 prose words · Awakening Day + First School Day, Year 0 · next: ch3, the foundling girl (canon 005).**
> Started 2026-09-19 · epoch reset 2026-09-23 · V2 live 2026-09-26 · gates: 9 layers ALL GREEN.

**Map:** [STATUS.md](STATUS.md) lists every file, its role, and the live numbers — auto-generated, always current.

**The doctrine (what makes this build different):** canon runs *on the page*, complete
and unskipped, in Wulin's own close-third. The original character lives in parallel —
same clock, same streets — and a butterfly effect is only logged when the two tracks make
contact on the page. Canon shown, never skipped; the OC added, never centered.

A man who read this story dies and is reborn inside it, in Glorybound City, two doors down
from Tang Wulin. He awakens **Bluesilver Grass at innate soul power rank one** — publicly a
trash soul. His real edge is high spiritual power and a lifetime of adult method in a child's
body, and for thirteen chapters his entire project has been **not to be noticed**.

---

## Read in this order

| File | What it is |
|---|---|
| **`PROJECT_README.md`** | The full entry point: the five decisions, the layout, the doctrine |
| **`HANDOFF.md`** | What is true *now*, the authority order, and which file wins when two disagree |
| **`foundation/NO_MISTAKE_LIVE_RULES.md`** | **The sixteen locks.** Constitution + current state + every user ruling verbatim with its date |
| **`SARA.md`** | The partner's self-file — who Sara is, the standing rules in the author's own words, and a growth ledger that is appended to every session |
| `chapters/` | The serial — V2 live: 2 chapters (8,779w) · V1 archived: 15 chapters (see below) |
| `audits/` | Dated audit records. Entry one is the full comparative audit of 2026-09-20 |
| `checks/run_all.sh` | **One command, nine layers.** `sh checks/run_all.sh` → ALL GREEN, exit 0 |
| `LICENSE` | MIT for the tooling; derivative-work notice for the prose |
| `_kit_reference/NOTICE.md` | Why the vendored kit copy is kept, and which files are authoritative |

## The chapters — V2 LIVE

| # | File | Words | Beat |
|---|---|---|---|
| 01 | Chapter_01_What_the_Master_Said.md | 3,846w | Awakening Day. A father does the arithmetic out loud. Canon 001-002. |
| 02 | Chapter_02_The_Fifteen.md | 4,933w | First school day + forge door. Canon 003-004. |

**Total V2 prose:** 8,779 words · 9-layer gate ALL GREEN.

## The chapters — V1 ARCHIVED (15 chapters, pre-rebuild, kept for reference)

> V1 was retired 2026-09-23. The numbers below are `style_gate.py` counts post-repair. They are **not live** — V2 is the live serial.

```
01  What He Said              5,843w   Awakening Day. A father does the arithmetic out loud.
02  The Second Weed           4,847w   Lin Ximeng's homeroom. Battle versus Utility.
03  Two Doors Down            6,436w   Na'er found. Six boys, a knife, a price for silver hair.
04  Five Kilograms            5,411w   Mang Tian's workshop. Metal is a living thing.
05  The Better Version        5,499w   Exclusion. The first flicker of Track 8.
06  What Grows in Cracks      4,345w   The garden. Twenty seconds cost him a month.
07  Six Days                  4,790w   Blind, and six days of somebody else's invitation.
08  The Complaint             3,528w   The first returned jar. The gauge leaves the family.
09  Steps                     4,964w   Nine months. The offset is permanent. The garden empties.
10  The Column                4,578w   Year 1, Awakening Day. Na'er has no martial soul, and
                                       the register has no column for it.
11  Four Hours                3,782w   He puts himself on the books, and finds out where the
                                       four hours are.
12  The Middle                3,526w   Fifteen months. A stopwatch, a narrow column, and four
                                       minutes ten weeks running — the average that starts to
                                       look like something no child has ever produced.
13  Made Up                   5,314w   A teacher asks what to do with a girl who has nothing on
                                       the day everybody shows what they have. He gives her the
                                       answer he was given. Then he writes a story, and the story
                                       turns out to be true.
14  The Empty Case            5,785w   Old Pei's carry trade: who buys is answered — nobody
                                       here. The ladder spoken at the Pagoda counter. The list
                                       moves one to two. The first frost window missed.
15  Ten Minutes               3,800w   The Other-POV slot: Na'er's night, dawn and beach, in
                                       italics. The ring stays reader-knowledge. The street
                                       learns the neighbor's door is crossed — rank ten,
                                       seventh in class, a thousand a month — and on the shore
                                       she asks the only future-question she has.
```

## Gates

Nothing ships without **`sh checks/run_all.sh`** returning exit 0, plus one check that cannot
be automated:

```bash
sh checks/run_all.sh        # nine layers, ALL GREEN, exit 0
sh checks/run_all.sh --quick
```

```
1  verify.py            9 structural gates (7 inherited from the kit + 2 local)
2  style_gate.py        voice law, measured from the author's corpus
3  canon_copy_check.py  narration 12-grams · quoted runs >= 7 words · density <= 120 words
4  marker-leak grep     no codex glyph may reach finished prose (8 glyphs, widened 2026-09-20)
5  privacy grep         no personal email, token, noreply id or sandbox domain
6  build hygiene        no __pycache__ / .pyc / .bak / .DS_Store
7  selftest.py          20 checks — proves every gate can fail
8  kit selftest.py      inherited-gate regression against the vendored kit
9  banned_token_check.py  regression tokens — values known-dead (added 2026-09-20)
```

Layer 2 legitimately returns **2**, not 0: `style_gate.py` is three-state and chapter three runs
above the house word band by design. That is documented, permanent, and accepted.

The ninth check is **check (d): date arithmetic.** Every "N days ago / N days later", and every
stated duration, is recomputed by hand against the day map. It is invisible to every script and
it is the highest-yield check in the project — it caught nine month-count errors in chapter nine
alone and four stale year counts in chapter thirteen.

🔴 **Chapters one to four were re-voiced on 2026-09-20.** They had been staging canon scenes
partly by transcribing the translation's dialogue; layer 3 now measures that and they carry
between zero and sixty-three verbatim canon words each, against two hundred and ninety-seven in
chapter three before the pass. The word counts above are post-repair.

## Doctrine

Built on the author's own `SOUL_LAND_UNIVERSAL_KIT`: the five decisions and the
seven-question prewrite gate (`00_START_HERE`), the five failures and the per-chapter
contract (`03_STORY_LAW`), language law and the five registers (`07_PROSE_LAW`), the audit
and selftest mandate (`09_AUDIT_LAW`), and the handoff and stale-file law (`10_HANDOFF_LAW`).

The style model is `blue_silver/chapters_rebuilt/`. The voice thresholds in `style_gate.py`
are **measured from that corpus, not chosen by taste.**

Identity: **Sara.**

---

*Canon source material is fetched and held as read-only receipts in `canon_extract/chapters/`
(001-018). Receipts are never edited and never silently corrected — a variance is logged and
both readings are held.*
