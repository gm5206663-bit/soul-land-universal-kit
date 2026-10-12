# SERIAL_LOG.md — per-chapter record

One row per chapter, appended after the sync completes. Never edited retroactively;
corrections get their own row noting what they fixed.

🔴 **This file carries the bookkeeping that used to live in a chapter footer.** There is no
footer. `07_PROSE_LAW.md`: *"A footer in the chapter file is apparatus outgrowing story. It
is failure mode five and it is revoked."* A reader never sees this file.

**The sync** (per chapter, in order — `NO_MISTAKE_LIVE_RULES.md` Lock 11):

```
 0. prewrite gate — the seven questions, plus: declare the dialogue dial, pick 1-2 gold
    patterns, check the cliff rotation against the previous chapter's cliff
 1. draft
 2. tools/verify.py       ← portability floor. Zero failures.
 3. tools/style_gate.py   ← THE VOICE WALL. Zero failures, and answer every warning.
 4. SERIAL_LOG.md         ← this file
 5. STATUS_PANEL.md       ← the single status source
 6. CONTINUITY.md         ← anchor table, forward refs, character register
 7. CANON_LEDGER.md       ← if a canon beat was touched, plus the decay column
 8. KNOWLEDGE_FIREWALLS.md← the Notice Ledger, if anyone noticed anything
 9. CHARACTERS.md         ← first/last appearance
10. TIMELINE.md           ← if the frame moved
11. OPEN_DECISIONS.md     ← if a ruling was consumed or created
```

A chapter is not done when it reads well. It is done when all of these are green.

---

## THE LOG

| Ch | Title | Words | verify | style | dlg% | Rank | SP | Rings | Year | Age | What moved | Turn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | What He Said | 5,666 | **PASS** 0F 0W | **PASS** 0F 0W | 29.4% | 1 (innate) | untested | 0 | 0 | 6 | knowledge · bond · resource | went in to be a number nobody remembers; came out with a line in the register, a cup on a sill, and a promise said aloud |
| 9 | Steps | 4,964 | **PASS** 0F 0W | **PASS** 0F 0W | 13.5% | 1 | 0 | 0 | 42-323 | 🔴 knowledge · 🔴 bond | Nine months, eight holidays, one lie told eight times, and a black bar over a name |
| 8 | The Complaint | 3,528 | **PASS** 0F 0W | **PASS** 0F 0W | 16.9% | 0 | 0 | 0 | 20-41 | 🔴 knowledge · bond | A jar that is not wrong, a corner that is nearly still, and a man who refuses to sell the only stick that measures his own work |
| 7 | Six Days | 4,790 | **PASS** 0F 0W | **PASS** 0F 0W | 15.9% | 1 | 0 | 0 | 15-20 | knowledge · cost · 🔴 bond | A blind boy counts thirty-one paces in his father's stride, and his mother asks him one question at a cart |
| 6 | What Grows in Cracks | 4,345 | **PASS** 0F 0W | **PASS** 0F 0W | 16.5% | 1 | 0 | 0 | 7-14 | knowledge · 🔴 cost · bond | A man who has never heard the word makes a gauge, and his son finds out why there was never much grass in Glorybound City |
| 5 | The Better Version | 5,496 | **PASS** 0F 0W | **PASS** 0F 0W | 18.6% | 0 | 1 | 0 | 6 | knowledge · cost · 🔴 craft | He looks at a pair of healed hands, gets caught writing one good sentence, and finds he has written the same night twice |
| 4 | Five Kilograms | 5,395 | **PASS** 0F 0W | **PASS** 0F 0W | 20.2% | 1 | untested | 0 | 0 | 5 | knowledge · resource · 🔴 appetite | He takes a box of balm across the city, swings a six-star blacksmith's test hammers, and walks out of the hall having found the only door in this world that was built for him |
| 3 | Two Doors Down | 5,986 | **PASS** 0F 0W | **PASS** 0F 0W | 14.4% | 1 | untested | 0 | 0 | 5 | knowledge · bond · cost · 🔴 a second silence | Na'er arrives a day late and with an extra witness. He manufactures the crowd that saves her, withholds the thing that would have saved Wulin's teeth, and then finds his brother through a wall |
| 2 | The Second Weed | 4,698 | **PASS** 0F 0W | **PASS** 0F 0W | 24.2% | 1 | untested | 0 | 0 | 6 | knowledge · bond · resource · 🔴 a lie | the first day of school. He sees the gold at the root — the one thing in the room worth seeing — and says nothing, and lies to Wulin about it |
| ~~1~~ | ~~What He Did Not Say~~ | ~~3,298~~ | ~~PASS~~ | **FAIL** | ~~5.2%~~ | — | — | — | — | — | **REBUILT — see the record below** | — |

---

## 🔴 CHAPTER ONE — REBUILT, NOT REVISED (2026-09-19)

### What happened

Chapter one was written, passed `tools/verify.py` with zero failures and zero warnings, was
declared done, synced across seven files, and packaged. The author read it and said:

> *"You makeing some serious mistakes in writing style go check my projects all completely
> because and learn everything, there is written everything, you just needed learn them"*

He was right. `verify.py` is a portability floor. It checks CJK, digits, marker discipline,
dialogue *count*. It cannot see that a chapter is a 3,300-word interior monologue in which
nobody talks and nothing happens. The author's own projects already contained the diagnosis,
the measurement, the doctrine and a machine check for all of it, in
`reference/sl3_lin_hao/Soul_Land_3_Project/STYLE_GOLD.md` and the SL3 CODEX's **VOICE LAW
(locked v3.10)** — which exists because the author once wrote the identical correction:
*"the writeing style of your is very bad you should write like you write Frist three
chapters."*

### The measurement that settled it

```
                                   words   dlg lines   dlg%   median sent   ", and"/1k
SL3 ch1  ← THE VOICE BAR           5,389       122    20.6%      11           16.9
SL3 ch75 ← the author's bar        4,891       138    31.0%       7
SL4 ch31                           8,194       212    21.0%       8
Blue Silver REJECTED ch1           4,627         0     0.0%       —           18.2
────────────────────────────────────────────────────────────────────────────────────
Lan Shen ch1, FIRST DRAFT          3,296        21     5.2%      12            —
Lan Shen ch1, REBUILT              5,666       200    29.4%      11           19.6
```

The first draft had the same dialogue profile as the **rejected** Blue Silver draft that the
author had already thrown away once. Three of the five failures in `03_STORY_LAW.md` were
live: **nothing contested**, **one register repeated**, **apparatus outgrew the story**.
Per §7 of that file — *"If more than two are true, you are not editing. You are rebuilding.
Say so plainly and do it."*

### The five specific defects

| # | Defect | Evidence | Cure in the rebuild |
|---|---|---|---|
| **D1** | **Spectator Test failed** | he watched a ceremony, watched his mother, watched a Spirit Master, and made a private vow. Zero acts of his own | five acts: reads a notice, negotiates a fee, changes a register line, asks an unprecedented question, proposes an experiment |
| **D2** | **Dialogue 5.2% / 21 lines** | the voice bar is 20.6% / 122 lines | 29.4% / 200 lines. The dial is declared in the panel |
| **D3** | **A fifty-line footer** | CANON TOUCHED · BUTTERFLY · PANELS · FORBIDDEN STILL · NUMBERS · REGISTERS USED | deleted. All of it moved into this file. `◆` count 2 → 1 |
| **D4** | **An eleven-field panel** | LIVE EDGE · DATE · POSITION · AGE · two character blocks · MOVED · TURN | slim: STATUS · KIND · AGE · CLASS · THREAT · BOND · DIALOGUE · LAW · TURN |
| **D5** | **M7 — the canon MC worshipped at a distance** | Lan Shen had watched Wulin "from across a shared wall" for four years and never spoken to him | they are friends from line one, they banter, they eat together, they make a plan together |

Also fixed: **M8** (ended in solitude → now ends at a table with two families and two cups),
**M2** (talent named → talent embodied as counting, reading a notice, growing things),
**M3** (world rules stated → world rules *priced*: the stipend, the fee, the tray of coins).

### What the rebuild added that the first draft did not have

- **A threat with a face and a name.** Yan Song at a table inside the gate, with a register,
  a tray of coins, and a number to send upward before the bursar goes home. He is polite, he
  is reasonable, and he is a wall. He wants a clean register and a cheap class; Lan Shen
  offers him cheap. That is a conflict of objectives, not weather.
- **The method.** He wins with *information* — the seventh line of a notice he has read four
  times in four years. This is the OC's method, established before he has a word for it,
  exactly as `SL3_FOUNDATION_LESSONS.md` §1 requires of chapter one.
- **The character ruling, all of it, on the page.** Playful with boys (the spoon). Uncomfortable
  with girls his own age (the green coat — four things to say, all rejected, ears the colour of
  the radishes). Interest-driven not hard-working (*"he had done all of it because he liked
  it. The liking had never once felt like work."*). Imagination (the two-cups experiment,
  invented at a table, aloud). Loves food and cooks (egg, scallion, the soft ginger; his
  father tastes it twice and says four words). The staff (a callus, mentioned once, unexplained).
- **Two canon receipts used for the first time.** Canon 003's *"one in a million"* speech,
  given to Tang Ziran. And 🔴 **Wulin's mother is a Lan** — canon-given, not invented — so
  the street has called these two households relations for eleven years. Free warmth, free
  cover, and the reason a shared dinner needs no explanation.

### Gold patterns used (two, deliberately — never a checklist)

- **#2 Arithmetic as Soul** — *"Four hundred and eleven people. Sixty-two of them children.
  Fifteen of those children were the right age, which meant roughly one of them,
  statistically, would come out with soul power."* Plus one price-clause: *"the honest
  version is cheaper for everybody."*
- **#5 The First Hand In** — *"Wulin's hand was on his sleeve and then it was on his hand,
  and it was the first hand in, because it always was."* Positional, never announced.
- **#12 The Ongoing Image** carries the cliff — *"The water in the cups was still moving."*
  Chosen because the previous cliff was long-lyrical-and-solitary; the rotation law says
  end on process when the threat is offstage.

**Banked, not spent:** the two cups (callback-object economy — an arc must spend one old
object and bank one new one) · the seventh line of the notice · the staff callus ·
"one grey jar ends it" · Qin Wu's second sheet · Meilin's list.

### Style metrics at ship

```
prose words              5,666        (house band 2,600-5,500; a serial's ch1 may run long)
dialogue                 29.4%        200 spoken lines   dial declared: standard 13-30%
median sentence          11           (bar 9-11)
narration-only median    10           (bar 9-11)
", and" chains           19.6 / 1k    (voice bar 16.9 · the famous drift chapter 26.7)
protagonist spoken turns 63           (law: >= 4)
◆ markers                1            (law: 1 per chapter)
fenced blocks            1            (law: 1 — the panel. No footer)
panel fields             9            (law: <= 8 + DIALOGUE/TURN)
CJK / digits / bold      0 / 0 / 0
banned tics              0
registers                dialogue · close sense · hard scene · other POV (Qin Wu, italics) · lyrical
```

⚠️ Two accepted, reasoned positions, recorded rather than hidden:
- **Word count 5,666** is above the house band's top. Justified: SL3's own chapter one, the
  named voice bar, runs 5,389. `style_gate.py` warns above 6,000.
- **`, and` chains at 19.6/1k** are above the voice bar's 16.9 and below the drift's 26.7.
  Eighteen run-on sentences were split to get here from 25.3. Tracked; tighten further in ch2.

### Canon touched — the record that used to be a footer

```
canon 001 "Awakening Day"          HELD IN FULL — canon_extract/chapters/canon_001_excerpt.txt
canon 002 "Martial Soul Awakening" HELD IN FULL — canon_002_excerpt.txt, 8 sections
canon 003 "Little Wulin's Family"  HELD IN FULL — canon_003_excerpt.txt, 7 sections
canon 004 "Entering the Academy"   RECEIPTED (R2) — used only for the gold-at-the-root
                                   reservation, which is NOT staged here

CHANGES TO CANON: one additional child in the awakening batch; one additional line in the
register; one margin note on a second sheet; one margin note in a register; one supply
arrangement between a herb shop and an academy. Nothing about the ceremony altered. No canon
line reassigned. No canon event moved. Wulin's rank, his grass, his scream, the golden lines,
the patriarch tale, his father's speech, his exhaustion, his nap and the three cycles all
stand exactly as canon has them.
```

### Blocked on

Nothing for chapter two's street and household material. Still owed before those beats:
canon 004 (`entering-the-academy`), 005–007 (Na'er), 008 (`learning-to-forge`). Slugs are
verified against the author's own `readnovelfull_map.txt`.

### Next

Chapter two. Per the standing locks: Yan Song's opposition is **not** to be spent yet — he
was reasonable in chapter one and the near spine is worth more later. The two cups are
banked and should be checked, not spent. The spiritual power question he asked Qin Wu is now
a live wire with a three-year fuse.
---

## CHAPTER TWO — THE SECOND WEED (2026-09-19)

### Prewrite gate, filled before drafting

```
1. CANON BEAT — canon 004 "Entering the Academy", HELD IN FULL on disk. Stays true: free
   compulsory tuition (so the fee is materials only, never tuition) · three years elementary ·
   a teacher at the front door for the Soul Master class only · the chubby knife boy, rank 5,
   "Knife God Douluo", "I can casually chop your Bluesilver Grass into tatters" · Wulin shows
   his grass and DOES NOT NOTICE the gold at the root · the other students boast and form
   groups and ignore him · Lin Ximeng introduces himself, is startled, the class roars, he
   recovers and smiles · the classifications (tool/beast, rank ten is the door, Battle vs
   Utility) in the morning, meditation in the afternoon · the teacher spends the least time on
   Wulin (canon 005 retrospective) · limitless lunch, better food, "Rice Bucket".
   Canon 005 held in part; its opening (the unhappy walk out) is the chapter's last scene.

2. THREAT — the room. Sixteen children ranking each other out loud before lunch. Named and
   faced: Niu Bao, rank five, whose father has already told him what he is for.

3. FACE — Niu Bao (motive: rank five is the best in the room and he checked) and Lin Ximeng
   (motive: three years, sixteen children, teach to the middle, spend the hands where the
   hands are needed). Both have dialogue. Neither is a villain.

4. MOVEMENT — knowledge (rank ten is the door, said aloud; Battle vs Utility, heard by one
   child) · resource (nine jars valued, a receipt with a number and no name) · bond (they sit
   together, eat together, walk home together) · 🔴 a lie (the first one to Wulin).

5. BUTTERFLY — see the decay row. Four, all causal.

6. REGISTERS — dialogue · hard scene (the introductions, the knife, the canteen) · close sense
   (the gold, the soup, the meditation) · OTHER POV (Niu Bao, italics, marked — gold pattern
   #7, the legend accumulating in an outside voice) · lyrical (spare, the walk home).

7. TURN — chapter one he spoke and it cost nothing. Chapter two he stays silent and it costs
   him, and he lies, and then he writes the truth in a book his mother can reach.

DIAL      standard 13-30% → ran 24.2%
GOLD      #7 the perspective doctrine panel (Niu Bao) · #9 the callback-object economy (the
          cups CHECKED — "day three, no change in either"; the book SPENT) · #2 arithmetic as
          soul, one price-clause only ("nine is fine. Nine is better than fine")
CLIFF     short-stark (three sentences), rotating off ch1's ongoing image
PANEL     endpoints set first: opens Year 0 day two, the storeroom; closes Year 0 day two,
          night, the shelf by the window. No date in the chapter contradicts this.
```

### The standing question (firewalls)

> What does he know going in that he must not act on, and where is the moment when acting on
> it would be so much easier than not acting on it?

He knows the gold at the root is the first visible sign of the thing that will eventually
save and nearly kill his brother. He sees it on the first day, two seconds after Wulin turns
his hand over, in front of fifteen other children. He could say *look at the root* and Wulin
would look, and would see, and would go home a different boy.

He does not. **The reason is not noble**: a gold root is a report, and a report is a man in
an orange robe remembering a question, and Lan Shen has already spent one crack in his cover.
He weighs his own safety against his brother's hope in about a second and a half, and he
chooses himself, and the chapter does not let him feel good about it.

Then Wulin asks him directly — *"You looked at my grass for a long time today"* — and he lies.
Firewall 0 held: the reincarnation is never spoken. **Firewall 1 broke, quietly, and that is
the point: the first lie to Wulin is the first debt in the book.**

### Canon 004/005 receipts used for the first time

- 🔴 **"After your soul power reaches rank ten, then you're able to become a Soul Master."**
  Said aloud, in a classroom, on the first day. A rank-one child is nine ranks from having a
  title at all. This is the bottleneck `THE_PLAN.md` Track 3 predicted, now canon-stated.
- 🔴 **"By cultivating your soul power, you're able to upgrade your martial soul."** Canon
  hands the upgrade path out in the first lesson, in the same breath. This is the legal
  in-world basis for every route in Track 4.
- 🔴 **"Utility Soul Masters."** Canon's non-combat track, named on day one. For a rank-one
  child this is a real door, and it is the only sentence in the lesson that Lan Shen hears.
  This is the six-track plan arriving as a six-year-old's attention span.
- 🔴 **"Even the Spirit Pagoda had records on these children."** (canon 005) — the far spine
  is canon, not invention. A soul-power child is protected by paperwork. Lan Shen is in that
  file at rank one. Held for chapter three; not staged here.
- 🔴 **Free, compulsory tuition** — three years elementary, six intermediate. Any fee staged
  in this serial must be materials, books or supplies. Chapter one's "materials fee and a
  book list" is compliant; checked.
- **The gold at the root is a day-two fact**, not a day-one fact, and canon states nobody can
  find it without meticulous examination. A boy who has spent four years looking at roots
  through a reading glass is exactly such an examiner. Legal.

### Style metrics at ship

```
prose words               4,698      (house band 2,600-5,500)
dialogue                  24.2%      149 spoken lines   dial declared: standard 13-30%
median sentence           11 all / 9 narration           (bar 9-11)
", and" chains            16.0 / 1k                      (voice bar 16.9 — BELOW it)
viewpoint turns           32 attributed                  (law: >= 4)
◆ markers / fences        1 / 1                          (law: 1 / 1)
CJK / digits / bold       0 / 0 / 0
banned tics               0
registers                 5 of 5
```

Both gates clean, zero warnings. Red-test discipline observed on `style_gate.py` after every
edit to it this session — see `foundation/STYLE_LAW.md` §9.

### Blocked on

Canon 005 chunk 2 (the scene after *"I'm a man. I'll p—"*), canon 006 "Bringing Her Home",
canon 007 "Stay Here And Be My Little Sister". **Do not stage Na'er past the point held.**
Canon 008 "Learning to Forge" before any forge scene.
---

## CHAPTER THREE — TWO DOORS DOWN (2026-09-19)

### Prewrite gate, filled before drafting

```
1. CANON BEAT — canon 005 (rest) + 006 + 007 + 008 (opening). FOUR canon chapters, all now
   held in full on disk. Stays true: Na'er squats by the roadside, silver hair, amethyst eyes,
   shabby, dirt-stained, does not speak · the delinquents, the black-market line about the two
   other continents, the lift, the small scream · "What are you doing?" · Wulin kicked, tumbles
   two metres, gets up, charges · the dagger, "F*ck off if you don't want to die" · the light
   blue ring, the grass in the palm, the faint undulation · 🔴 the records reasoning IN THE
   THIEF'S HEAD, held in order · "Such bad luck" · she falls on her bottom · "Don't be scared.
   I'm a man. I'll protect you" · the mist in the pupils · "My name is Na'er" · Lang Yue's
   expression changing · the wash · the three questions and "Five and a half" · the
   Administrative Office · 🔴 the first meditation and "he could sense some of the world's
   Bluesilver Grass" · Tang Ziran opposite him at night · "Originally, he himself…" LEFT CUT ·
   🔴 the brave-and-wise speech VERBATIM · "Men won't make that kind of mistake" · no records
   on Na'er · "At worst, I'll just have to eat a little less" · "You have to ask Na'er" ·
   "Why don't you stay and be my little sister?" · "En." · the bottomless pit · the divider ·
   "Dad, I'm going to meditate now."
   Moved: one day. Canon puts Na'er on the walk home from the FIRST day; ch2 already spent
   that walk. She arrives on the second day. Logged as butterfly B8, and it is what pushed
   decay across the 15% line.

2. THREAT — six boys with a knife and a price for silver hair. Named and faced: the jacket.
   Second threat, quieter: the wall, and what is on the other side of it.

3. FACE — the jacket (motive: silver hair sells), Tang Ziran (motive: his son came home with
   a split lip and he is going to teach him something before it happens again), Su Wan (motive:
   her son is bleeding and he is lying about it). All three have dialogue. None is a villain.

4. MOVEMENT — knowledge (the grass is one organism; rank is pressure not reach; his brother's
   soul is a well with floors in it) · 🔴 cost (the first instance of the comprehension price,
   staged at last — see OPEN_DECISIONS #13) · bond (Na'er, and the brotherhood's second debt).

5. BUTTERFLY — see the decay row. Five, one of them large.

6. REGISTERS — dialogue · hard scene (the street) · close sense (the mist, the grass, the
   copper) · eavesdropped canon (the wall as a delivery mechanism for canon 006-007, which
   keeps every interior Tang scene intact and un-witnessed) · lyrical (the ending, long).

7. TURN — chapter one he spoke. Chapter two he stayed silent to protect himself. Chapter three
   he stays silent to protect Wulin's love, and pays for a power in his own head, and finds
   that the story he read is now happening two doors down without him.

DIAL      standard 13-30% → ran 14.4%
GOLD      #7 the perspective doctrine (canon's interior Tang scenes delivered through a wall,
          so the reader gets them and the POV does not enter them) · #9 the callback-object
          economy (the two cups, the book, the rag, the shelf) · #2 arithmetic as soul ("eleven
          seconds", "nine ranks to the door")
CLIFF     long-lyrical, rotating off ch2's short-stark
PANEL     endpoints set first: opens Year 0 day four, the Lan table; closes Year 0 day four,
          deep night, the bed against the wall.
```

### The standing question (firewalls)

> What does he know going in that he must not act on, and where is the moment when acting on
> it would be so much easier than not acting on it?

Two answers this chapter, and the second is the one that hurts.

**The street.** He knows the thugs will drop her. He knows why: canon puts the reasoning in
the jacket's head — *the government maintained special records on these children. Even the
Spirit Pagoda had records on these children.* He could have said it thirty seconds earlier and
Wulin would never have left the ground. He does not say it, because a six-year-old who says
that sentence says it in a voice that has been in a room where they say that sentence, and
there is no such room.

He writes the verdict himself, at the bottom of the page: *"I could have stopped the kick. I
chose the cover instead… I am not going to pretend that being right is the same as being
clean."*

**The eyes.** He sees the mist in Na'er's pupils. He knows it means something. Firewall 4
holds — he does not know *what*. And then he makes the opposite choice from the street: he
withholds it from Wulin, not to protect himself, but because a boy told that his new little
sister has something wrong with her eyes will be frightened of her. 🔴 **The first silence
that is a gift rather than a shield.**

### Style metrics at ship

```
prose words               5,986      (house band 2,600-5,500 — 🔴 OVERRUN, see below)
dialogue                  14.4%      116 spoken lines   dial declared: standard 13-30%
median sentence           9 all / 9 narration            (bar 9-11 — bottom of it)
", and" chains            11.7 / 1k                      (voice bar 16.9 — well below)
viewpoint turns           attributed throughout
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
banned tics               0
registers                 5 of 5
```

🔴 **THE OVERRUN, SAID PLAINLY.** The house band is 2,600-5,500 and this chapter is 5,986.
It carries four canon chapters (005 rest, 006, 007, 008 opening) and splitting it would have
left a 2,100-word second half, below the floor. It was cut four times — 6,483 → 5,986, five
hundred words out — and every remaining beat is load-bearing. **Accepted and logged, not
excused.** Chapter four returns to the band.

### Blocked on

Canon 008 chunk 2 is held. **Canon 009 "Gifted" and canon 010 "I Will Protect You In The
Future" are NOT fetched.** Chapter four stages Mang Tian's workshop and must not be drafted
before 009 is held.
### Defects found and fixed in ch3 after the first clean gate pass

The gates caught the style. **They did not catch these — a human read did.** Logged so the
next chapter is checked for the same three things:

| # | Defect | How it was found | Fix |
|---|---|---|---|
| D1 | 🔴 **Timeline collision with ch2.** Ch2 closed on the night of day three, at the shelf, with the book. Ch3 as first drafted also ran on day three, and ended at the same shelf the same night — two different book entries in one night, one of which ch2 had already shown without Na'er in it | re-read of ch2's closing scene against ch3's opening | **Na'er moved to day four.** Ch3 now opens with the second day of school — a cultural-class morning, which is canon 008's own calendar. Butterflies B8/B9 logged; decay crossed 15% as a direct result |
| D2 | 🔴 **"eleven years" used backwards, three times.** Ch1/ch2 established the motif as a *forward* prolepsis ("would remember for eleven years", "would think about for eleven years") plus two in-world durations (Qin Wu's tenure, the two families' shared wall). Ch3 used it three times to mean *time since his previous life*, which contradicts all of them | grep across all three chapters for the motif | All three backward uses → **"the other life"**, matching ch2's established "two lives" / "two lifetimes" phrasing. One correct forward prolepsis then added at the mist in Na'er's pupils, so the motif is carried rather than dropped |
| D3 | 🔴 **Four stray `🔴` markers left in the prose** — codex annotation bleeding into the manuscript | grep after first draft | Removed. **Added to the post-draft checklist:** `grep -c "🔴" chapters/*.md` must be 0 |

**New standing check, added to the post-draft routine:** after both gates pass, grep the
chapter for (a) codex markers, (b) any recurring numeric motif used in a new direction, and
(c) the previous chapter's closing position/date. The gates cannot see any of the three.
---

## 🔴🔴 AUTHOR RULING — TRACK 8 (2026-09-20, between ch4 and ch5)

> The author ruled that **Lan Shen's previous life was an author.** He read and watched very many
> kinds of fiction — novels, drama, serials, film — and could write and create his own work and
> sell it. In the Soul Land world that work would be unique and good, so of course it sells.

**Accepted in full and built, not queued.** `THE_PLAN.md` now runs **eight tracks.**

| Consequence | Where |
|---|---|
| 🔴🔴 `THE_PLAN.md` is a **plot outline**, not a plan. Eight tracks = arcs. He has written himself a plot and is the only reader | `THE_PLAN.md` · `CHARACTERS.md` |
| 🔴 **Track 8 is the only zero-capital track**, therefore the only route to 30,000 Federation Coins before he can earn with a hammer. Track 5 feeds the family, Track 7 is the life's work, **Track 8 buys the spirit soul** | `THE_PLAN.md` T8 · `TIMELINE.md` |
| 🔴 **The front is Lan He.** Three tracks now converge on the father — shop, balm, pen name. **The plan made to survive alone has routed itself through one other person** | `THE_PLAN.md` T8 · `#21` |
| 🔴🔴 **The first audience is Na'er.** Track 8 begins as the only thing he can do about a girl who stopped eating that is not asking her what is wrong | `#20` + `#21` |
| 🔴🔴 **The forbidden masterpiece.** He knows professionally that the story he is living would be magnificent and can never sell a word of it. He will write it anyway, badly disguised, once | `#21(d)` |
| 🔴 **No revision to ch1-4 required.** The book on the shelf, the externalised numbers, the draft-vs-revision habit, and ch4's killed two-word line were already craft habits. **Ch4's *"He put the pen down on the shelf and did not write it"* is now retroactively the most important sentence in Book One** | `CONTINUITY.md` |

**Not staged.** No story exists on the page in ch1-4. 🔴 **Earliest: Year 1, oral, to Na'er. No
manuscript before Year 2.**

---

## CHAPTER FOUR — FIVE KILOGRAMS (2026-09-20)

### Prewrite gate, filled before drafting

```
1. CANON BEAT — canon 009 "Gifted" + canon 010 "I will protect you in the future", both now
   held in full on disk. Stays true: Lang Yue collects Wulin at the gate · the twenty-minute
   walk, no vehicles · the shabby front, three words, the smell of metal · the chaotic hall
   full of soul-machine components · the workbench just barely taller than Wulin · the
   half-metre table, the round lump, the soul machine screen · two hammers, five kilograms
   each, a third of a metre of handle, heads half a foot by ten centimetres · a thousand
   strikes · the test was a tactful refusal · Wulin's second session, 150 more, swaying,
   caught, would have collapsed · hands swollen · 🔴 "You two have raised a good child. I'll
   accept him as my disciple. From tomorrow onwards… the same time… smear this ointment on his
   arms" · the bottle to Lang Yue · her tears · 🔴 the forging doctrine VERBATIM · 🔴 "Spirit
   Master and Machine Master, those were the dreams of all young boys" · Na'er's trace of
   blankness · the memory question · 🔴 "Big Brother Lin" · "This is your home now" · the first
   smile · "protect you in the future" · the closed bedroom door · "I'll feed you then" ·
   Na'er, You're the best.
   NOT staged (held for ch5): canon 011 — the argument in full, 🔴 "godly talent", 🔴 six-star
   blacksmith, the adoption, Lan Yue going to work, the shoulder lamp, the unbruised arms,
   the golden veined pattern on the forehead, "investigate in the morning".

2. THREAT — Mang Tian in a good mood. A six-star craftsman who has just been astonished by a
   number is a man who asks questions he would not ask on a bad day.

3. FACE — Mang Tian (motive: pride, a favour owed to Tang Ziran, and a hall full of work) and
   Lan He (motive: his son has just talked him into a delivery round and he does not like how
   good the argument was). Both have dialogue. Neither is a villain.

4. MOVEMENT — knowledge (🔴 the third door) · resource (a box of balm, a shop's name in a
   six-star blacksmith's head, a correction to the winter ratio) · cost (he is told, to his
   face, that there is nothing in that hall for him).

5. BUTTERFLY — see the decay row.

6. REGISTERS — dialogue · hard scene (the hammers) · close sense (the rebound, the skin over
   the knuckles, the smell of metal) · interior arithmetic · lyrical (spare; the hall).

7. TURN — ch3 he found a power in his own head. Ch4 he finds an idea in somebody else's hall,
   and it is the first thing in the serial that did not come from the book.

DIAL      standard 13-30% → ran 20.2%
GOLD      #9 the callback-object economy (🔴 the staff callus from ch1 PAID — "You've turned
          something." "A stick.") · #2 arithmetic as soul (two hundred and six; fifty of a
          hundred and fifty counted) · #7 the perspective doctrine (canon 011's closed door
          staged as a wall that carries nothing, because the chimney is in it)
CLIFF     short-stark, rotating off ch3's long-lyrical
PANEL     endpoints set first: opens Year 0 day five, the classroom; closes Year 0 day five,
          night, the shelf.
```

### The standing question (firewalls)

> What does he know going in that he must not act on, and where is the moment when acting on
> it would be so much easier than not acting on it?

The moment is **the screen.** Mang Tian asks him what he wants to know and Lan Shen asks the
one question a machine person would ask: *the screen only counts a hit if it's hard enough —
so there's a line. Who's it hard enough for?* That is a craftsman's question and it is
available to a bright six-year-old. He asks it and Mang Tian resets the screen and says
*pick them up*, and nothing about any of it requires the reincarnation.

The near-break is two beats later. Told to keep going, what comes out of his mouth in the
first draft is: *the next fifty won't teach me anything, they'll just take the skin off, and
I've got four years of skin I need for other things.* That is a thirty-year-old's sentence. He
catches it and shoves it back down — 🔴 **and the shoving shows.** Mang Tian looks at him and
asks who taught him to hold a hammer, and the chapter does not let him answer well.

Firewall 0 held. Firewall 2's laundering rule held: every advantage he takes is laundered
through a herb shop, a father, a box and a stick he has been turning for two years.

### 🔴 The two canon-fidelity defects caught on the read-through (not by the gates)

| # | Defect | Fix |
|---|---|---|
| D4 | 🔴 **Wulin reported Mang Tian's thoughts as speech.** Canon 010's *"his strength could still be trained later, but… such an unwavering determination… too precious"* is **free indirect narration of Mang Tian's feelings — never spoken.** Wulin could not have heard it, and handing it to the POV would have been a Firewall 4 breach in both directions | Rewritten: Wulin reports only what was said (*"He said we've raised a good child. To Mom."*) and then **infers** the rest from behaviour — *"he caught me when I was going over, and he didn't tell me to stop until he had to, and you don't do that for somebody you thinks is rubbish."* Canon's interior stays interior; the child gets to be perceptive instead of informed |
| D5 | 🔴 **"eleven years" drifting backwards, three times** — the exact defect class logged as ch3's D2 | All three → *"the other life."* Ch4 now carries exactly one forward prolepsis, matching the motif's established direction |

**The standing check caught D5 and a manual canon read caught D4.** Both are now in the
post-draft routine: after the gates pass, (a) grep for codex markers, bold and digits; (b)
grep every recurring numeric motif for direction; (c) check the previous chapter's closing
position and date; 🔴 **(d) NEW — check every line of reported speech against the canon
excerpt to confirm canon actually SPOKE it.**

### Style metrics at ship

```
prose words               5,395      (house band 2,600-5,500 — ✅ back inside it)
dialogue                  20.2%      146 spoken lines   dial declared: standard 13-30%
median sentence           10 all / 8 narration           (bar 9-11)
", and" chains            13.0 / 1k                      (voice bar 16.9 — below)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
banned tics               0
registers                 5 of 5
```

Cut from 5,355 with 26.5/1k chains (a hard FAIL, the drift rate of SL3 ch60) to 13.0/1k in one
pass of 43 targeted splits. **The chain-rate check earned its place in the gate this chapter.**

### Blocked on

Canon 011 is **held in full** and not yet staged — it is chapter five's whole payload. Canon
012 "Three Years Later" is the hard time-skip this serial has sworn to WALK, not jump
(`codex/TIMELINE.md`). **Do not draft ch5 past canon 011 until 012 is fetched.**
---

## CHAPTER FIVE — THE BETTER VERSION (2026-09-20)

### Prewrite gate

```
1. CANON BEAT — canon 011 "Astonishing Recovery", held in full. Everything in it happens
   BEHIND A WALL and the chapter is about the wall. Stays true: 🔴 the argument with Lan Yue
   "restraining her emotions in order to prevent the two children outside from hearing" ·
   "Ah Yue" · 🔴🔴 Mang Tian's verdict relayed ("godly talent", "6 star blacksmith") —
   **NEITHER REACHES LAN SHEN** · 🔴 the adoption, muttered to himself, "Mnn" · 🔴 the decision
   that Lan Yue will go and find a job · Wulin showing Na'er his martial soul, "next year's
   Awakening Day" · 🔴🔴 the night scene — shoulder lamp, unbruised arms, golden veins fading,
   "investigate in the morning" · 🔴 the morning misunderstanding (mother credits father, father
   knows he did nothing) · Wulin forgetting to meditate · school day = Soul Master topics.
   ⚠️ **Serial offset:** this serial's day six is a CULTURAL day, not an SM day, because the
   Na'er arrival moved one day (B5). Canon's "we're learning about martial souls today" is
   therefore NOT used. The alternation is preserved; only the offset moved.

2. THREAT — 🔴 nothing he can see. For four years he has known more than everybody. This
   morning something happened two doors down that is not in the book, and he missed it.

3. FACE — Wulin (clean hands, a sister on paper) · Lin Ximeng (a small black book) · Lan He
   (scales, a candle, eleven weights) · Su Wan and Lan Yue at the pump (money) · 🔴 Tang Ziran,
   SEEN BUT NOT KNOWN — a light on a shoulder, from two houses away, through a gap.

4. MOVEMENT — knowledge (partial; the gap is the subject) · cost (he learns he prettifies the
   truth) · 🔴 craft (Track 8's first flicker, on page, in a school exercise, crossed out).

5. BUTTERFLY — see the decay row.

6. REGISTERS — close sense · hard scene (classroom, back room) · dialogue · lyrical (the light,
   the ending). 4 of 5. Other POV correctly absent.

7. TURN — ch4 he found an idea in somebody else's hall. Ch5 he finds a defect in himself.

DIAL      standard 13-30% → ran 18.6%
GOLD      #9 callback-object economy (🔴 the book on the open shelf, ch1 → now holds two
          versions of one night) · #2 arithmetic as soul (fourteen hours; two days gone of
          seven; eleven weights) · #7 perspective doctrine — 🔴🔴 **canon 011's entire payload
          is staged as EXCLUSION.** The reader gets a light through a gap between two houses.
CLIFF     medium/proleptic, rotating off ch4's short-stark.
PANEL     opens Year 0 day six, the yard; closes Year 0 day six, deep night, the floor.
```

### 🔴 Track 8 arrives on the page (author ruling, 2026-09-20)

The chapter was drafted the same day the author ruled that **Lan Shen's previous life was an
author**, and the ruling is what the chapter is about. Per `CONTINUITY.md` forbidden, no story
may exist before Year 1 and no manuscript before Year 2 — so ch5 stages only the **first
flicker**: a cultural-class exercise, three sentences, and a crossed-out line.

> *The man was hitting the slat and the horse stood still and watched him, the way a horse
> watches, which is not the way a person watches, and every third hit made a different noise
> because the wood had already split further than the man thought.*

🔴 **He crosses it out and writes the safe version underneath.** Then at night, writing the true
account of the shoulder light, he finds his hand has already produced a *better* version — with
four invented details in it — and **he does not cross that one out.**

The chapter's law: **a record is only worth what its worst version is worth, and he has just
discovered he does not write the worst version.** He started keeping the book because he did not
trust his memory. He had not thought about what would happen to the record.

### 🔴 The true-misdirection, which is worse than a lie

Asked where he got the word "further," he says: *"I heard it. My dad. He says it about the wood
in the shop. He says it splits further than you think and you have to cut it off."*

**That is true.** His father says exactly that about bloodroot, every autumn, and said it three
days ago. 🔴 **Lie count for ch5 is therefore 0 — and this is the first time he has used a true
statement as a shield.** Running total: ch1 1, ch2 1, ch3 1, ch4 0, ch5 0 lies / 1 misdirection.

Separately, the second version in the book is 🔴 **the first falsehood he has committed to
paper** — not told to anyone, written down, and kept.

### 🔴 Canon-fidelity defects caught on the read-through (check d)

| # | Defect | Fix |
|---|---|---|
| D6 | Wulin reported the adoption as addressed speech. Canon 011: *"Tang Ziran **muttered to himself**"* | Rewritten as an overheard mutter: *"Dad said it last night — he didn't say it to anybody, he just said it, out loud, to himself, and mum said mnn."* Canon's quality preserved, and more childlike |
| D7 | 🔴 Lan Yue had **already got the job** with fixed hours and wages, on the morning after canon's night in which the family only *decided she would go and look*. Canon 011 as held says nothing about a specific job | Rewritten as a **lead, not a job**: a place on the noodle street, "they'll tell me Monday." Su Wan's balm gift becomes conditional (*"if you do end up with your hands in hot water"*) — which makes it kinder, not weaker |

**Check (d) has now caught a defect in two consecutive chapters.** It is standing.

### Style metrics at ship

```
prose words               5,496      (house band 2,600-5,500 — ✅ inside)
dialogue                  18.6%      83 spoken lines    dial declared: standard 13-30%
median sentence           10 all / 9 narration           (bar 9-11)
", and" chains            14.4 / 1k                      (voice bar 16.9 — below)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
registers                 4 of 5
```

Drafted at 5,643w / 19.1 chains / median 8-7. Two passes of targeted merges, splits and
**deletions** brought it inside on all three. Chains 104 → 74.

### Blocked on

Canon 016 "The Starry Sky and the Vast Sea" (the beach, the seven colours' aftermath) and 🔴
**canon 017 "Spiritual Power Test"** — the instrument that `OPEN_DECISIONS.md` #18 says is the
only thing in this world that can see Lan Shen. **Do not stage any measurement of him until 017
is held.**
---

## CHAPTER SIX — WHAT GROWS IN CRACKS (2026-09-20)

### Prewrite gate

```
1. CANON BEAT — none staged. This is a walking chapter, covering days seven to fourteen, the
   eight days between canon 011's night and the next canon event. 🔴 It exists to pay two
   things off and plant one: the grass sense returning (#13/#15), the economic weather canon 011
   invited, and THE GARDEN (canon 014-015, `OPEN_DECISIONS.md` #19, ruled "not before ch6").

2. THREAT — himself, in a public place, at dusk, with two children walking toward him.

3. FACE — Lan He (motive: eleven years of being wrong about wax, and a son who says "two
   lines"). Wulin (motive: his friend is sitting alone in a garden bleeding). Both have
   dialogue and neither is an obstacle.

4. MOVEMENT — 🔴 knowledge (the city is paved; cost is width not time; one strand in forty
   thousand has a direction) · 🔴 cost (a month of blindness, estimated, uncertain) · bond
   (Wulin walks him home the long way).

5. REGISTERS — hard scene (the stick, the nail) · close sense (the garden, the biggest
   sensory set-piece so far) · dialogue · lyrical. 4 of 5.

6. TURN — ch5 he found a defect in his record. Ch6 he finds a defect in his measuring
   instrument: himself. He has been calibrating against the worst ground on the continent.

DIAL      standard 13-30% → ran 16.5%
GOLD      #9 callback-object economy (🔴 the stick; 🔴 ch4's two-hundred-and-six and square
          hammers invoked as the part of his mind that should have stopped) · #2 arithmetic as
          soul (2,727 days of eleven copper; seven and a half years; the doubling estimate) ·
          #7 perspective doctrine — canon 014-015's garden is found by the boy canon never
          puts there
CLIFF     short-stark ("There was nothing under them."), rotating off ch5's proleptic
PANEL     opens Year 0 day seven, the classroom; closes day fourteen, deep night, the bed.
```

### 🔴 Track 7's first rung, on the page — and canon did not supply it

`THE_PLAN.md` Track 7 ruled that it starts as **standardising his father's balm**. Ch6 stages
it, and the mechanism is deliberately small enough for a six-year-old:

> A dip-stick. One burned line. **"I've been doing it by eye for eleven years. By eye is why
> it's wrong in the winter… by eye is no use at all to anybody else."**

Lan Shen's contribution is not the stick — his father already made it. It is three refinements:
**two lines, not one** (one where it's right, one where it's ruined, because you cannot find the
middle without both); **on both faces** (because it rolls on the bench); and **the numbers on
the stick, not the paper** (because the paper is in the drawer and the drawer is shut).

🔴 **And Lan He is the one who solves the real problem.** He writes the figures, realises the
wax will hide them, and cuts them in with a nail and a hammer instead. *"That'll take wax.
That'll take water. That'll last as long as I do."*

> **The point of the scene: a man who has never heard the word "gauge" invents a gauge, and his
> six-year-old son recognises it.** Track 7 does not need Lan Shen to be an engineer. It needs
> him to be the only person in the room who knows that what his father just did has a name, and
> that the name is worth something.

Also staged: **the balm slips now carry a line saying which stick the batch was made against.**
That is a batch record. In Year 0. In a herb shop.

### 🔴 #15 REFINED — the cost is WIDTH, not time

`OPEN_DECISIONS.md` #15 ruled the cost as *eleven seconds → nosebleed, migraine, white line,
one week of total loss*. Ch6 discovers the rule is wrong in a way that makes it worse:

```
STREET  (day 11)   ten seconds, twice, let go on purpose  → NOTHING. No cost at all.
GARDEN  (day 14)   four seconds to find it, twenty held    → nosebleed, white face,
                                                            total loss, estimated one month
```

> 🔴 *"The cost was not the length of time and never had been. The cost was the **width**."*

**Why this is legal under #15:** the ruling says *"any chapter that lets him reach further, hold
longer, or read more clearly than the last one must SAY what he paid."* He holds longer — and
pays roughly four times the previous price, stated on the page, with the arithmetic shown twice
and then shown a third time with a different answer. **Progression is bought, not granted.**

🔴 **And it retroactively explains ch3.** Eleven seconds cost him a week — but eleven seconds of
*what?* A street. Forty strands, mostly growing in cracks. **He has been calibrating his own
ceiling against the sparsest ground available.** That is the chapter's law and its title.

### 🔴🔴 THE GARDEN — found, entered, and paid for

Canon 014: *"a powerful attraction force from a strand of Bluesilver Grass."* Canon 015: Wulin
breaks through to rank 10 there. `#19` ruled it the most important location in Book One after
the shared wall, and ruled **"not before ch6."** Ch6 stages it.

Held exactly:
- Range unchanged (one street) — 🔴 **it is density, not reach.** *"It was not louder, it was
  more, and more was worse than louder, because louder you can brace against and more just
  keeps coming."*
- Resolution stays LOW. He gets **shape, not content**: *"Not brighter. Not bigger… this one was
  pulling at him, in a straight line, and it was the only thing in forty thousand that had a
  direction."* ❌ No number, no rank, no colour, no gold. #15 held.
- ❌ Does not reach Na'er — she is five and a half and unawakened. Nothing to feel.
- ❌ Wulin does not feel him. Asymmetry held. Wulin arrives **on foot and shouting**, not
  through the sense.

🔴🔴 **THE ESCALATION, AND IT IS DELIBERATE: #15's "may never be demonstrated in front of
anybody" is breached — partially, and by accident.**

He is caught mid-sense by Wulin and Na'er. What they see is **a white boy on a bench with a
bloody nose.** Not the sense. 🔴 **The cost was seen. The capability was not.** That is the
distinction the ruling was protecting, and the chapter holds it — but Su Wan will hear about a
nosebleed in a public garden from a nine-year-old who tells his mother everything, and
`#15`'s "the cost is paid alone until Su Wan is deliberately invited in" is now **on a clock.**

### The lie

*"he told his mother he was going to see whether Zhao had any more jars, which was a lie but a
small and checkable one, and she did not stop him because she had stopped stopping him in the
third week of the month."*

Running total: ch1 1 · ch2 1 · ch3 1 · ch4 0 · ch5 0 lies + 1 true misdirection · **ch6 1.**

🔴 **And a new movement in the book:** for two chapters he has been withholding (ch4) and
fabricating (ch5). In ch6 he writes down the thing that makes him look worst — *"I did not stop
at four."* **The record is unreliable in one direction and honest in another, and he has not
noticed the difference.**

### Style metrics at ship

```
prose words               4,345      (house band 2,600-5,500 — ✅ inside, deliberately short)
dialogue                  16.5%      75 spoken lines   dial declared: standard 13-30%
median sentence           10 all / 10 narration         (bar 9-11 — ✅ dead centre)
", and" chains            14.5 / 1k                     (voice bar 16.9 — below)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
registers                 4 of 5
```

Drafted at 24.3/1k chains (a WARN). One pass of 28 targeted splits → 14.5/1k. **The chain
problem is now a known first-draft tendency, not a surprise: budget one splitting pass into
every chapter.**

### Blocked on

🔴 **The month of blindness.** He is now without the grass sense until roughly day forty. That
is a long gap and the serial must not quietly restore it. `#15`'s progression rule binds.

Canon 016 "The Starry Sky and the Vast Sea" (the beach, Na'er's question answered) is **held in
part** — ch15's tail is the question, ch16 is the answer. Not yet fetched. Canon 018 "Random
Draw" is where the number in ch17 would have been revealed, and canon does not give it.
---

## CHAPTER SEVEN — SIX DAYS (2026-09-20)

### Prewrite gate

```
1. CANON BEAT — none. Days fifteen to twenty are empty in canon. 🔴 This chapter exists to
   honour two promises made in ch6: the six days, and "the cost is paid alone" (which ch6
   breached). It also pays the Su Wan fuse that KNOWLEDGE_FIREWALLS row 27 lit.

2. THREAT — the loss of his own observation. He has four seconds of data, six days old, and no
   instrument left to check it with. Nobody is trying to stop him. He is trying to remember.

3. FACE — 🔴 SU WAN, at last given real weight (2 mentions in ch4, 2 in ch6). She goes to a
   ruin alone, finds nothing, tells nobody, then tells him. Wulin hands him an excuse already
   wrapped up. Both have dialogue and neither is an obstacle.

4. MOVEMENT — 🔴 knowledge (three laws, all negative) · cost (two sticks, both taken) · bond
   (🔴🔴 Wulin knowingly accepts a lie and decides to carry it).

5. REGISTERS — domestic (supper, the back room, the window) · hard scene (the counting) ·
   dialogue · close sense AS ABSENCE. 4 of 5.

6. TURN — ch6 he found the most important thing in the world. Ch7 he finds out he cannot find
   it again, and that the city is not the only thing that moves under him.

DIAL      standard 13-30% → ran 15.9%
GOLD      #9 callback-object economy (🔴 the bench, the nail head, the two sticks, the hem) ·
          #2 arithmetic as soul (31 paces in father's stride vs 40 in his own; eleven lines of
          which eight are worthless) · #7 perspective doctrine
CLIFF     🔴 question, unanswered — rotating off ch6's short-stark
PANEL     opens Year 0 day fifteen, the bedroom floor; closes day twenty, the corner by the
          drain, behind a cart.
```

### The three laws of the blind week

🔴 **This chapter's entire payload is negative knowledge. Nothing is gained. Three things are
learned, and all three are about the failure of an instrument he built himself.**

```
LAW ONE   (day 15)  Memory is a worse instrument than sense, and it degrades while you hold it.
                    Eleven lines written from a bedroom; eight are things anyone could have told
                    him without going; the three that are his are the three he is least sure of.
                    "The writing down had made it feel like more than it was."

LAW TWO   (day 18)  An observation without an instrument is not an observation. It is a
                    sentence.  — "she went." / "or a cart. I cannot check."

LAW THREE (day 20)  🔴🔴 THE PLACE IS THE INSTRUMENT. He could not remember whether the tree
                    was left or right of the mound for FIVE DAYS. He stands where he had been
                    sitting and knows it in half a second.
```

> 🔴 **Law three is the chapter's real discovery and it is Track 7 through and through.** He
> spends eleven lines failing to do what standing in the right place does in half a second.
> **The answer to losing an instrument is not a better memory. It is a better position.** That
> is what a gauge is. That is what a marked stick is.

### 🔴🔴 THE TWO STICKS — and the chapter's law about the world

He marks the most important place in his life with a piece of broken something, about as long as
his forearm, with a knot at one end.

```
STICK ONE   thirty-one paces in his father's stride. A boy runs past, pulls it out without
            slowing down or looking at it, throws it six paces left, keeps going.
STICK TWO   at the edge of the flattened wrestling grass. A girl pulls it out about ten minutes
            later, hits her brother with it, is told to put it down, and puts it down somewhere
            completely different.
```

> 🔴 *"I am not going to be able to hold this. **It is not the grass that moves. It is
> everything else.**"*

He does not go and get either stick. He watches both leave. **This is the first time the serial
has shown the world simply not caring, and it is done without a villain.**

### 🔴🔴 WULIN — the brotherhood takes its first real load

The exchange is the chapter's hinge and it is almost entirely Wulin's:

> *"My mum said was it the heat."* … *"It was the heat."* … *"See. I told her."*

Then, back up the bank, Wulin returns **on his own**, without the other children:

```
"You can just tell me."        "I know."
"You told me it was the heat." "I know."
"And it wasn't the heat."      "No."
   → Wulin nodded slowly, the way he nodded when he had been given a thing he did not want and
     had decided to carry it.  "All right. Then it wasn't the heat."
```

🔴🔴 **This is the first time Wulin has knowingly accepted a lie from Lan Shen and chosen not to
press.** He is not stupid — *"He was nine and he had been told for nine years that he was not a
subtle person, and he was not. He was also not stupid. The two things were not the same."*

**The brotherhood is now load-bearing in a way it was not before.** Wulin carries something he
does not understand, on purpose, for a friend who will not explain it.

### 🔴 SU WAN — she went

```
DAY 18  comes home from the market with grass seed on her hem. 🔴 He works out where she has
        been from her skirt, because Glorybound City is paved and nothing in the district goes
        to seed. Supper. Nobody says anything about a garden.
DAY 19  standing at the window that has never in six years had a reason to be stood at.
        "I went and had a look at it. On the way back from the market. I thought I'd see what
        it was." … "There isn't anything there, Shen." … 🔴 "You told me you were going to
        Zhao's for jars. Zhao is the other way."
DAY 20  "I'll walk you there. And I'll walk you back. You can go and be with Wulin. I'll be
        somewhere I can see you. That's not a question either."
```

🔴🔴 **She caught the ch6 lie. He does not deny it. She does not press it.** And she walks him
there anyway — which is the "stopped stopping him" decision from ch6, now tested and held.

> 🔴 **And the horror of her position, stated plainly: she went to the place that hurt her son
> and could not find the thing that did it.** *"I stood in it for about ten minutes and I could
> not work out what it was about that place."* She is not wrong. There is nothing there.

Her one true question, at the blanket: *"Did you find what you were looking for."* He answers
*"No."* — 🔴 **the first true thing he has said to her about the garden.** She nods *"as though
he had answered a different question"* and says *"That's all right. You can come back."*

### The lie

*"It was the heat," he said.* — to Wulin, on day nineteen, after Wulin had already offered it.

> 🔴 **The chapter is explicit about the economy of it:** *"He thought about the fact that his
> brother had just handed him the entire thing already wrapped up, with the paper on it, and
> that it would be ungrateful not to take it, and that taking it would cost him nothing at all."*

Running total: ch1 1 · ch2 1 · ch3 1 · ch4 0 · ch5 0 + 1 misdirection · ch6 1 · **ch7 1.**

🔴 **And the book keeps moving.** Ch4 withheld, ch5 fabricated, ch6 recorded his own failure,
**ch7 records almost nothing — he writes five lines and a date.** The record is thinning exactly
when it should be fattest, because there is nothing he can verify. #23 escalation held.

### 🔴 Firewall 4 seed — one look, nothing more

> *"Na'er was standing very still in the middle of the grass, not doing anything, with her hands
> at her sides. Lan Shen looked at her for a second. Then he looked away, because there was a
> thing about her standing like that which he had noticed before and had decided was nothing."*

Canon 016 gave three unexplained Na'er data points the same day this was drafted. ❌ **Do not
develop this. #20's ruling is Year 3.**

### Style metrics at ship

```
prose words               4,790      (house band 2,600-5,500 — ✅)
dialogue                  15.9%      130 spoken lines   dial declared: standard 13-30%
median sentence            9 all /  8 narration          (bar 9-11 — ✅)
", and" chains             9.4 / 1k                      (voice bar 16.9 — 🔴 best in serial)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
registers                 4 of 5
Lan Shen speaks           31x  (ch6: 17x — 🔴 most in the serial)
```

🔴 **First draft FAILED two gates** (dialogue 5.4% — lines averaged 3.8 words against ch6's 8.8;
chains 32.6/1k; median 13.0). One full rewrite pass, expanding speech and splitting sentences
**simultaneously**, cleared all three at once. **New protocol: the first draft's dialogue lines
must average 8+ words, or the chapter is a monologue with interruptions.**

Ten date-arithmetic errors caught in the standing check (d) — 🔴 **every "N days ago" in a draft
must be recomputed against the day map before the gate, because the gate cannot see the calendar.**

### Blocked on

🔴 **THE UNANSWERED QUESTION.** The chapter ends mid-exchange, behind a cart, at the corner by
the drain: *"There's a bench with a slat missing." / "Is that the one."* Ch8 must open on it.

🔴 **The sense is still out until roughly day forty.** #15 binds. Do not restore early. He has
no marks left — both sticks are gone — and nothing but numbers in a book.

Canon 018 "Random Draw" is the next unfetched beat. Canon 016 is held in full.
---

## CHAPTER EIGHT — THE COMPLAINT (2026-09-20)

### Prewrite gate

```
1. CANON BEAT — none. Days twenty to forty-one. 🔴 This chapter closes three ch7 fuses: the
   unanswered question, Lan He being owed a scene, and the blind month running to day forty.

2. THREAT — the ground moves. His instrument is fine and the world under it is not, and from
   the inside those two are indistinguishable.

3. FACE — 🔴 LAN HE, at last. Given the shop, the counter, and the refusal. Su Wan, extracting
   a promise. Zhao, arriving for jars and leaving with a question.

4. MOVEMENT — 🔴 knowledge (four laws, all of them about measurement) · bond (the deal with
   his mother; his father handing him a knife and saying nothing) · 🔴 no cost paid and none
   granted.

5. REGISTERS — domestic · hard scene (the counter, the stick) · compression (twenty-one days) ·
   dialogue. 4 of 5.

6. TURN — ch7 he could not find the thing. Ch8 he finds out that finding it was never going to
   be the hard part. Holding still long enough to measure it is.

DIAL      standard 13-30% → ran 16.9%
GOLD      #9 callback-object economy (🔴 the dip-stick leaves the crock for the first time;
          🔴 a second stick with three unnumbered marks; the nail head; the hem) · #2 arithmetic
          as soul (nine numbers from twenty-eight to thirty-four; ninety paces against a hundred
          and forty; eleven days of three) · #7 perspective doctrine
CLIFF     🔴 object — he goes and gets the second stick out from under his bed. Rotating off
          ch7's question and ch6's short-stark.
PANEL     opens Year 0 day twenty, the corner by the drain; closes day forty-one, the front
          room doorway.
```

### 🔴 ZERO LIES

First chapter since ch4 with no lie in it, and the first with no misdirection either. He
answers his mother's question truthfully, confirms the bench truthfully, names the nail head
truthfully. **The only untruth in the chapter is a projected one** — *she is going to ask me
every month what I am counting. I am going to say steps. She is going to let me.* That is a plan
to lie, not a lie, and it has not been spent.

Running total: ch1 1 · ch2 1 · ch3 1 · ch4 0 · ch5 0+1 · ch6 1 · ch7 1 · **ch8 0.**

### 🔴🔴 THE FOUR LAWS OF MEASUREMENT — the chapter's entire payload

```
LAW ONE    THE STREET IS NOT A NUMBER. THE STREET IS A NUMBER PER DAY.
           Nine mornings of counting the same ninety paces by eye: 31, 33, 30, 28 (rain, not
           trusted), 32… running from twenty-eight to thirty-four and never settling.
           🔴 *"Forty was a number the sense had given him once, in the second week, on a
           street, in weather. It was not the street. It was the street on a day."*
           🔴 *"He had spent a fortnight grieving an instrument that had never been accurate in
           the first place, and had not once asked himself what it was accurate TO."*

LAW TWO    THE INSTRUMENT CAN BE RIGHT AND STILL NOT BE ENOUGH.
           Mrs Guo's complaint. The dip-stick says the balm is above the lower line and below
           the upper, same as every jar that week. 🔴 Her hands are worse because the WATER GOT
           COLDER. Lan He: *"The balm's all right. That's not the same as it being enough."*

LAW THREE  🔴🔴 YOU HAVE TO KEEP SOMETHING THAT DOES NOT MOVE.
           The three thin things in the angle of his own wall. Nobody sweeps them, nobody trod
           them, one goat got in once. Counted eleven days running. Always three.
           **He has invented a control group.**

LAW FOUR   🔴🔴 THE CONTROL DISAGREES WITH ITSELF.
           Day forty. The sense comes back. Eyes: three. Sense: four. Same corner, same evening,
           one minute apart. He kneels in the dirt with his face a hand from the ground and
           counts three from every side he can manage.
           *"There is nothing that stays still. Not the street. Not the garden. Not the wall.
           🔴 So the answer is not to find something that stays still. The answer is to keep
           counting the thing that nearly does, and to write down what it did, so that when it
           moves you know it moved and you know which one of you it was."*
```

### 🔴🔴 #15 PROGRESSION AUDIT — the strictest compliance yet

He paid a month. **He got back exactly what he had.**

> *"He sat on the floor of his bedroom with his hand flat and felt three things in a hand's
> width of dirt. That was all. It was enough. It was exactly what had been there when it went
> away."*

No wider reach. No finer resolution. No new capability. 🔴 **The only thing that changed is the
number in the corner, and that number may be an error.** `#15`'s rule — *"any chapter that lets
him reach further, hold longer, or read more clearly than the last one must SAY what he paid"* —
is satisfied in the strongest possible way: **a chapter that takes the price and refuses to give
the goods.**

### 🔴🔴 LAN HE INVENTS THE CALIBRATION MASTER

Zhao comes for jars, sees the slips, sees the stick, and asks:

> **"How much for the stick."**

And Lan He — who has never heard the word *standard*, *calibration*, or *master* — refuses:

> 🔴🔴 *"You want one, I'll make you one, and I'll show you where the lines go. It'll be yours
> and you can put your own numbers on it. **But you don't take this one, because this one's the
> one my jars were made against, and if it goes to the academy then the academy's got my jars'
> measure and I've got nothing.**"*

**That is a reference standard that must not leave the laboratory.** He has independently
derived the difference between a measuring instrument and the instrument that calibrates it,
from nine years of making balm in a commoner district.

> 🔴 Zhao's reply: *"That's a new way of talking."* — *"It's a new way of doing it."* —
> **"Who taught you that."** And: *"Lan He's hand was on the crock. He did not turn around."*

**He is now suspicious in a way he was not in ch6.** In ch6 he said *"give it here."* In ch8 he
is asked where it came from and does not answer. 🔴 **He is counting, and the count has changed
character.**

### 🔴 Lan Shen's projection — and the chapter's irony

> *"he is going to make Zhao one. Zhao is going to take it to the bursar. The bursar is going to
> write it down. In a year there will be a stick in the academy storeroom with two lines on it
> and somebody's name cut into the end. **And nobody will know it came out of this room.**"*
>
> *"that is exactly how it is supposed to work. I am the only person in this city who knows
> that. I am six years old, and I cannot feel my own wall from the front room."*

🔴 **Track 7's thesis, spoken from the front room doorway by a boy holding a broom he is not
using:** a standard works precisely by losing its author.

### 🔴 The second stick

Made day twenty-four, from the offcut rack, with his father's knife and nail and hammer handed
over **without a word**. Two lines each face, numbers cut in, and 🔴 **three marks on one face
and the same three on the other, unnumbered, "because he did not know what the numbers were
yet."**

> *"He had made it for a thing that did not exist yet."*

It has been under his bed for seventeen days. **The chapter ends with him going to get it.**

### Style metrics at ship

```
prose words               3,528      (house band 2,600-5,500 — ✅ shortest yet, deliberately)
dialogue                  16.9%      76 spoken lines   dial declared: standard 13-30%
median sentence           11 all /  8 narration         (bar 9-11 — ✅)
", and" chains            12.2 / 1k                     (voice bar 16.9 — below)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
registers                 4 of 5
Lan Shen speaks           22x
```

First draft FAILED one gate only (chains 29.7/1k). One pass of 34 targeted splits → 12.2/1k.
🔴 **Twelve date-arithmetic errors caught in check (d) again** — every "nineteen days / a month"
was wrong against the day map. **Check (d) has now caught errors in two consecutive drafts; it is
not optional and it must run before the gate, because the gate cannot see a calendar.**

### Blocked on

🔴🔴 **THE FOUR.** Eyes say three, sense says four, same corner, one minute apart. `#24` opens
on it. **Do not resolve it quickly.**

🔴 **The second stick is in his hand.** Ch9 must say what it is for.

🔴 **Zhao is going to the bursar.** The gauge is leaving the family — as a copy, with somebody
else's numbers on it. That is Track 7's threshold and it is now crossed.

Canon 019 "Spirit Soul" and canon 020-022 are unfetched. Canon 016-018 are held in full.

---

## CHAPTER NINE — STEPS (2026-09-20)

### 🔴🔴 THE COMPRESSION CHAPTER — `#25` executed

`#25` ruled that Year 0 must end within three to five chapters. **Ch9 covers days forty-two to
roughly three hundred and twenty-three — about nine months — in 4,964 words.** Ch8 covered
twenty-one days. Ch7 covered six.

```
DAY 42      the second stick comes out from under the bed. "Three batches."
DAY 42-72   the three batches, in the evenings, against his father's knife and pot
DAY 51      🔴 HOLIDAY ONE — 31,000. "Steps." THE LIE IS TOLD FOR THE FIRST TIME
DAY ~65     six washerwomen in the yard. Four better, one same, one worse
DAY 81      HOLIDAY TWO — 19,000. 🔴 The bench has a new slat nailed over the gap
DAY ~95     🔴🔴 THE ACADEMY NOTE. Four dozen jars, "marked with the batch and the measure"
DAY ~107    🔴🔴 THE OFFSET DISCOVERED — six weeks of two columns, always one apart
DAY 111     HOLIDAY THREE — 2,000. Four people in the garden
DAY 141     HOLIDAY FOUR — he does not go
DAY ~150    🔴 the corner goes to one, then to nothing above the dirt. The sense still says one
DAY 171-231 HOLIDAYS FIVE, SIX, SEVEN — rain, the shop, two days ill
DAY ~200    the balm goes to the academy in four crates in the coldest week.
            "We're the ones with a stick."
DAY ~235    the thaw. The corner comes back: 2/3, then 4/5, then 7/8. 🔴 THE OFFSET HOLDS
DAY 261     🔴 HOLIDAY EIGHT — 38,000. And NOTHING at thirty-one paces
DAY ~323    🔴🔴 THE NOTICE. Awakening Day in six weeks.
```

🔴 **The holiday rhythm worked exactly as `#25` predicted it would.** Eight visits, four of them
a single number and a sentence. **That is the serial's metronome and it can now skip months.**

### 🔴🔴 THE LIE IS TOLD — eight times

`#25` logged it as designed and unspent. Ch9 spends it:

> *"What are you counting."* — **"Steps."** — *"How many steps have you done."* — **"A lot."**
> She looked at him. He looked at the bank. *"All right,"* she said.

🔴 **"And that was how it went for the next four months."** By holiday eight she no longer asks
what, only how many.

Running total: ch1 1 · ch2 1 · ch3 1 · ch4 0 · ch5 0+1 · ch6 1 · ch7 1 · ch8 0 · **ch9 1, told
eight times.** 🔴 **The first lie in the serial that is a standing arrangement rather than an
event.**

### 🔴🔴 THE OFFSET — `#24` refined, and NOT resolved

```
AUTUMN   eyes 3 / sense 4     (eleven days, then six weeks of two columns)
WINTER   eyes 2 / sense 3  →  eyes 1 / sense 2  →  eyes 0 / sense 1
SPRING   eyes 2 / sense 3  →  eyes 4 / sense 5  →  eyes 7 / sense 8
```

> *"A thing that is always wrong by one is not wrong. It is one out, and one out in the same
> direction every time, and a number that is one out in the same direction every time can be
> corrected, and correcting it means you know what the one is."*
>
> 🔴 *"it is not one out. It is one more. It has been one more the whole time. **I have been
> counting leaves.**"*

🔴🔴 **HE DOES NOT DIG.** He thinks about it for most of a week, in a thaw, in his own yard,
where "worms" would have been a true reason:

> *"if I dig it up I will see it and I will not know what it is, and it will be dead, and I will
> have spent a thing I cannot get back to answer a question I can answer later by waiting. The
> offset is one. It has been one for five months. It is not going to stop being one."*
>
> *"so I will subtract it."*
> *"and now I have a number I can trust, and **I do not know what it counts**."*

**`#24` held exactly as ruled: mechanism unconfirmed, nothing resolved, nothing dug.**

### 🔴🔴 TRACK 7 CROSSES ITS THRESHOLD — the gauge becomes a specification

The academy's note, on paper with the academy's mark:

> *four dozen jars of the medicinal balm, the price the same as the spring price, and* 🔴 **"each
> jar was to be marked with the batch and the measure it had been made against."**

**An institution has specified the gauge in writing.** Not adopted it — *required* it.

Lan He reads it three times and understands the cost immediately:

> *"That's not four dozen jars. That's four dozen chances to be told you're a liar."*
> — **"That's what it's for."**

🔴🔴 **AND THE SECOND "WHO TAUGHT YOU THAT."** Zhao asked it in ch8. Lan He asks it in ch9, in
the same words:

```
"Who taught you that."      (Lan Shen stands very still by the shelf and waits)
"You did."
"I did not."
"You said it's right and it isn't enough. You said it in the back room with the jar in your
 hand, and then you put it down and you didn't do anything, and now they've sent a note."
"That's not teaching."
"It's the same thing."
"It isn't the same thing at all, 🔴 and if you say it in front of anybody I'll tell them
 you're six."
```

🔴 **He is now complicit AND defensive.** That is a different position from ch6's *"give it
here"* and ch8's hand on the crock. **He is protecting the story, not the son.**

And at supper, about the academy's thirty-day terms: *"Are we half the district."* — **"No.
We're the ones with a stick."** 🔴 **The family's self-conception has changed in nine months.**

### 🔴 Track 5 pays off: the three batches

```
ONE    winter balm + more wax.  Stays on. Comes off on everything. "It makes the washing
                                slippery." FAILED
TWO    winter balm + tallow.    Cheaper, softer, and it smelled. 🔴 *"Cheaper isn't a smell.
                                You can sell dear and you can sell cheap and you cannot sell
                                stinking, and that's the whole of the trade."* FAILED, FIRE
THREE  winter balm + less wax + more oil + 🔴 **a handful of something from a paper twist on
                                the top shelf that his father would not name.** Thin. Goes on
                                thin. Does not come off in the water. 🔴 **PASSED**
```

🔴 **The unnamed ingredient is deliberate and must stay unnamed.** The herb shop ruling says the
materials base supports cultivation-aiding products. **A herb seller's top-shelf paper twist is
the correct place for that to start, and it should not be explained in Book One.**

The test: six washerwomen, jars with no slip and a number scratched under the lid, nine days.

> 🔴 *"four say better. One says same. One says worse. **It was a warm week. I do not know.**"*
> *"that is the same sentence I wrote about the street. **Everything I have is the same
> sentence.**"*

### 🔴🔴 THE GARDEN DIES AND COMES BACK — and the strand is not there

```
day 51   31,000   grass still up, browner at the top
day 81   19,000   🔴 THE BENCH HAS A NEW SLAT — nailed over the gap, the wrong colour, so the
                  nail head is under new wood and the man can sleep on it again.
                  🔴 **His thirty-one paces were measured from a broken slat that no longer
                  exists.** He logs it: *"the bench has a new slat."*
day 111   2,000   four people in the garden. Grass a hand high, yellow. The bench is wet.
                  🔴 He stands at thirty-one paces: *"I cannot find it in the winter because
                  there is nothing to find it in. That is not the same as it not being there."*
                  Then: *"but it might be."*
day 261  38,000   the thaw, the grass a hand high and growing, the new slat gone grey.
                  🔴🔴 **He walks it in three lines. There is nothing. Not one of thirty-eight
                  thousand is pulling at him in a straight line.**
```

> 🔴 **THE STRAND IS GONE, OR WAS NEVER WHERE HE MARKED, OR IS UNDER THE DIRT LIKE THE FOURTH.**
> He cannot tell, and the serial must not tell him. **He has now lost the most important thing
> he ever found twice — once to cost, once to season.**

### 🔴🔴 Su Wan: "That's not a thing a six says"

```
"Steps."                     "Yes."
"How many."                  "A lot."
"More than last time."       "More than last time."
"It'll be there next month." "Yes."
"You don't believe me."      "I believe you. It'll be there. 🔴 That's not the same as it
                              being the same."
  → She was quiet for a while. **"You're six."**  "Yes."  **"That's not a thing a six says."**
  → He did not answer, because there was no answer that was not worse than the silence, and
    🔴 **she let the silence stand, which was the thing she had got best at in eight months.**
  → Then she held out her hand, and he took it.
```

🔴 **She has stopped asking what and started asking how many. That is not surrender — it is a
mother learning the shape of a thing she cannot be told.**

### 🔴🔴 THE CLIFF — `#23` takes its fourth step

Awakening Day notice in the corridor, at the height of a grown-up's chest, walked past four
times before read. Six weeks.

He writes her name in the book. Then he looks at it:

> *"This was a thing that was going to happen. It was going to happen in six weeks, in a
> chamber, in front of the whole district, and there would be a woman two doors down who would
> know the date and the hour and who had not been told.*
>
> *And there was a shelf in the front room, second row, square to the edge, that his mother
> could reach."*

🔴🔴 **He blacks it out — "the way a man blacks something out rather than the way a child crosses
something out" — and then understands that a black bar over a name is the loudest thing on a
page. So he writes instead: *the girl two doors down.***

Then the three lines, and then a line through the third:

> *and there is not one thing I can do about it, and I have already decided that I am not going
> to.*  →  🔴 **"that is not true. There is one thing. I am not going to do it yet."**

**`#23` escalation: hidden (ch4) → edited (ch5) → self-accusing (ch6) → thin (ch7-8) → 🔴
OBFUSCATED (ch9).** He has now removed a name and replaced it with a description that is true
and identifies nobody. **That is not hiding. That is drafting.**

🔴 **Last line of the chapter:** *"He shut the book and put it back on the shelf square to the
edge, second row, where his mother could reach it, because he had never once in two lives been
able to keep a thing like that anywhere else."*

### Style metrics at ship

```
prose words               4,964      (house band 2,600-5,500 — ✅)
dialogue                  13.5%      107 spoken lines   dial declared: standard 13-30%
median sentence           10 all /  9 narration          (bar 9-11 — ✅)
", and" chains            16.1 / 1k                      (voice bar 16.9 — just below)
◆ markers / fences        1 / 1
CJK / digits / bold       0 / 0 / 0
registers                 4 of 5  (hard scene · domestic · close sense as absence · dialogue)
Lan Shen speaks           22x
```

🔴 **Draft process notes:** the first draft FAILED three gates (an unreadable marker in the
panel, dialogue 9.2%, chains 25.7/1k). Fixed by stripping panel markers, adding four dialogue
scenes (the tallow batch, the six washerwomen, the second "who taught you that", the supper
exchange) and running 31 chain splits. 🔴 **Two script syntax errors came from replacement text
ending in a double-quote adjacent to a triple-quote delimiter — use heredoc files for any
replacement containing trailing quotes.**

🔴 **Check (d) caught nine month-count errors** ("five months" where the day map said eight),
plus an internal inconsistency (an offset found on the fortieth morning but described as
covering eleven weeks). **Third consecutive chapter. It is the highest-yield check in the
protocol.**

### Blocked on

🔴🔴 **AWAKENING DAY, SIX WEEKS.** Year 1 opens. Canon 011-012: **Na'er awakens with NO MARTIAL
SOUL.** `#20` and `THE_PLAN` Track 8 both fire here — 🔴 **a story told OUT LOUD to a girl who
has gone quiet, never written. No manuscript before Year 2.**

🔴 **"There is one thing. I am not going to do it yet."** What is the one thing? Unspecified,
deliberately. **Do not specify it soon.**

🔴 The offset. The unnamed ingredient in the paper twist. The strand, twice lost.

---

## 🔴🔴 AUDIT ENTRY — 2026-09-20 · FULL COMPARATIVE AUDIT (no chapter shipped)

**Trigger:** author directive — *"comper the project you created to my GitHub all and find
your mistakes and correct them and find there advantages and learn them... Make yourself
Sara... you are my partner, we needed growth, like seriously."*

**Scope:** all 621 files of `/home/user/ref/` against all of `/home/user/lan_shen/`.
**Record:** `audits/2026-09-20_FULL_COMPARATIVE_AUDIT.md` (entry one in `audits/`).

### Findings

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | **Failure 2 — nothing contested.** ch5-9 all carry an abstract THREAT; ch9's panel says "not a person" | 🔴🔴 HARD FAIL | Ruled: `OPEN_DECISIONS.md` **#26(a)** FACE LAW. Not yet executed in prose |
| 2 | **Failure 3 — no felt progression.** rank one in ch1, rank one in ch9 | 🔴 HARD FAIL | Ruled: **#26(b)** NUMBER LAW. Not yet executed |
| 3 | **Failure 4 — Other POV absent from ch7-9.** Italic blocks: 11,13,20,12,24,13,3,0,0 | 🔴 PARTIAL | Ruled: **#26(c)** REGISTER LAW. Not yet executed |
| 4 | Prewrite contract had six items, missing **BUTTERFLY** (answered after drafting, in the ledger — backwards) | 🔴 | Fixed: **#26(d)** — seven items, pre-draft |
| 5 | **11 verbatim canon dialogue runs** in ch1-4, up to 50 contiguous words | 🔴🔴 | **FIXED — all 11 rewritten** |
| 6 | `tools/selftest.py` absent. "A gate that has only ever been seen to pass is a gate nobody has tested" | 🔴 | **BUILT — 14 checks, 14 held** |
| 7 | **Gate hole:** prose inside the panel fence is exempt from every gate and vanishes from the word count | 🔴🔴 | **FIXED — gate 8 added to `verify.py`** |
| 8 | **Gate hole:** a hyphen in `years 4-5` parses as `4-4` silently and corrupts the contiguity gate | 🔴🔴 | **FIXED — gate 9 added. All 9 chapters confirmed to use the en dash** |
| 9 | 12-gram canon copying check never run | 🔴 | **BUILT — `tools/canon_copy_check.py`** |
| 10 | `HANDOFF.md`, `PROJECT_README.md`, `audits/` absent | 🔴 | **BUILT — all three** |
| 10b | 🔴 **THE AUDIT ITSELF WAS WRONG:** it reported `NO_MISTAKE_LIVE_RULES.md` as absent. It existed at `foundation/` as **THE TWELVE LOCKS** (19 KB). A duplicate was built at the root | 🔴🔴 | **MERGED into the real file as LOCK 13/14/15; root duplicate DELETED; all references repathed** |
| 10c | 🔴 `README.md` said *"chapter one not yet drafted"* with nine chapters shipped — and so did the status line atop THE TWELVE LOCKS | 🔴🔴 | **BOTH FIXED.** `README.md` rewritten as an accurate public entry point |
| 11 | `codex/TIMELINE.md`, `PLACES.md`, `CHARACTERS.md` not synced for ch9 | ⚠️ | **FIXED this entry** |
| 12 | `lan_shen.zip` predates ch9 and the audit | ⚠️ | **REBUILT this entry** |

### The 11 canon-copying leaks, and the technique used

Narration was **completely clean** — zero 12-gram collisions across 162 comparisons (9
chapters × 18 extracts). Every leak was **quoted speech**: canon 003 (ch1, Tang Zhirui,
35w + 22w), canon 004 (ch2, Lin Ximeng, three runs), canon 005 (ch3, the black-market
speech 25w; Wulin's shout 17w), canon 007 (ch3, Lang Yue 18w + **50w** + 29w; Wulin's offer
to Na'er 38w), canon 010 (ch4, Mang Tian 15w+).

**Technique: break each run with the listener's ear.** Short quoted fragments (<15 words)
interleaved with what Lan Shen hears, recognises, and already knows. Not a compliance trick —
it is the better prose, because the premise is that he *read this book*: verbatim recitation
spends the reader's attention on text they can get from the source, while recognition spends
it on him. *"On the page it was shorter than this"* does more characterisation than the 38
words it replaced. It also repaired Failure 2 incidentally: the delinquent's monologue became
a two-voice exchange, and the jacket now answers Wulin — *"A Soul Master. Good for you."*

**First version of the check was too weak.** Testing whether a whole quote is a substring
lets a 45-word quote hide 33 verbatim words behind a paraphrased tail. Hardened to test
**every contiguous 15-word run**, which found four more leaks in chapters not yet touched.

### Cost, honestly recorded

Removing quoted words dropped **ch3 from 14.3% to 12.4% dialogue — below the 13% floor.**
Restored to **13.2%** via the two new exchanges. Ch3 is now **6,313 words** against a 5,000
ceiling: **pre-existing and deliberate**, logged here as required by the gate's own warning.

### Battery after the edits — all five green, 2026-09-20

```
verify.py            PASS   9 files · 45,597 prose words · 0 failures · 0 warnings
style_gate.py        PASS   (1 warning: ch3 above word band — pre-existing)
canon_copy_check.py  PASS   162 comparisons · 0 findings
selftest.py          PASS   14 checks · 14 held · 0 blind
kit selftest.py      PASS   patched verify.py introduces no inherited-gate regression
```

**No chapter was written, shipped or advanced by this entry.** The audit corrected four
shipped chapters (ch1-4, dialogue only), added two gates, built five files and one
directory, and ruled on three structural failures that **remain open and binding from ch10**.


---

# CHAPTER TEN — "The Column"  ·  shipped 2026-09-20  ·  4,532 words

**File:** `chapters/Chapter_10_The_Column.md` · **Prewrite board:** `foundation/PREWRITE_ch10.md`

## Position and frame

```
PLACE      Red Mountain Academy — the yard, the chamber, the table with the register.
           Then the Tang doorstep, at night.
DATE       🔴🔴 years 0–1. THE YEAR TURN. Forty-three days of term break (Year 0, days
           324-365), then Year 1 Awakening Day, day 366.
AGES       Lan Shen six → seven. Wulin six → seven. Na'er five and a half → six and a half.
RANK       🔴 rank one. Unchanged, and cannot change — rank ten needs a ring and a ring
           needs a kill. The number that moves in this chapter is Na'er's, and it moves
           to blank.
SENSE      Not used. He stands in the widest thing he has ever stood in — a chamber full of
           souls being lit — with his hands in his pockets, and does NOT reach. Cost rule
           respected by refusal rather than by payment. When Na'er's turn comes the sense
           reads nothing at all, because there is nothing lit to read.
THE OFFSET 🔴 PAID OFF, QUIETLY. He counts the room, gets twenty-five, subtracts the one that
           is always there, gets twenty-four, recounts with his eyes, gets twenty-four.
           *Right for the first time in eight months.*
```

## Canon touched

| Canon | Beat | Held how |
|---|---|---|
| 🔴🔴 **012** | *"she didn't possess any martial soul at all... rarely seen throughout the history of the continent"* | **STAGED LIVE.** Canon reports it in retrospect; this chapter is in the room. The record is rare and it is noticed |
| **011** | *"Next year's Awakening Day, Na'er will also awaken her martial soul."* | The calendar anchor. Year 1 confirmed by Na'er arriving at five and a half (canon 006) |
| 🔴 **014** | the seven-coloured ring | **NOT TOUCHED. Firewall 4 holds.** Year 3, nobody in the room. Not hinted at |
| **015** | the stipend belongs to **Official Soul Masters**, 1,000 FC a month | 🔴 **Check (d) caught an error here.** First draft had Yan Song say "a stipend at eleven." Canon ties it to becoming a Soul Master proper, not to a rank number. **Corrected before shipping** |

## #26 — the three binding corrections, EXECUTED for the first time

```
(a) FACE LAW      ✅ Yan Song. Named, motivated (he wants the register clean), never raises
                  his voice, 20+ spoken lines. Plus Qin Wu, Na'er, Wulin, Lang Yue, Bo.
                  First chapter since ch4 with a human THREAT. Five-chapter run broken.
(b) NUMBER LAW    ✅ Na'er's record → blank. The gauge → a FOURTH office (Zhao → bursar →
                  storeroom → ceremony). Qin Wu's anomaly forms two → three. The thirty-day
                  payment resolved (paid on the twenty-ninth; Yan Song checked).
                  🔴 And ch1's unpaid "working student" line, nine chapters old, is ANSWERED.
(c) REGISTER LAW  ✅ OTHER POV returned — Qin Wu, in italics, the ceremony from behind the
                  hand. Absent from ch7, ch8, ch9 (italic blocks 3, 0, 0). Five registers
                  used: other POV, hard scene, dialogue, close sense, lyrical.
(d) BUTTERFLY     ✅ Answered PRE-DRAFT for the first time in this serial, in
                  PREWRITE_ch10.md. It propagates: a blank in his register → the register is
                  not clean → Yan Song has a frame for "impossible measurement" he did not
                  have in canon → he LOOKS → Qin Wu files a third anomaly form → two reports,
                  one about too much and one about too little, now sit in the same drawer in
                  the same small city in the same two years. 🔴 THE DRAWER IS THE FAR SPINE.
```

## Wires left open

- 🔴🔴 **WHAT YAN SONG WROTE IN THE RANK COLUMN.** Not zero — he explained at length that a
  dash is the wrong fact. Lan Shen did not step across to look, and does not know. **Deliberate.
  Do not reveal soon.**
- 🔴🔴 **THE OFFER STANDS UNTIL THE TERM STARTS.** Working student: fee off his father's
  account, four hours a week, and — the actual threat — **on the books**. Being on the books
  is four hours a week in a building in front of a man who keeps a register. He spent a year
  not being in a column. He said *"There is one thing. I am not going to do it yet"* — which
  is ch9's line, now given a referent without being spent. 🔴 **Note: the line now does double
  duty. Do not let a third use flatten it.**
- 🔴🔴 **YAN SONG HAS STARTED LOOKING AT HIM.** `CHARACTERS.md` names this as the Book One
  climax arriving early: *"being noticed by Yan Song is the first step toward being noticed by
  the thing above Yan Song."*
- 🔴 **QIN WU'S THIRD ANOMALY FORM** is going up in the post. Two are in a drawer. Three is a
  pattern, and patterns get read.
- 🔴 **NA'ER HAS BEEN WRITTEN AS NOTHING AND SHE KNOWS IT.** She is not crying. It is the
  silence of a child who has been in a room while adults discussed her. Lan Shen recognises it
  because he has been that child for a year.
- 🔴🔴 **TRACK 8 HAS FIRED.** The mountain story, told OUT LOUD on the Tang doorstep, in the
  dark, with no paper anywhere near him. He declares it a made-up thing before he starts
  (*"Not a true thing. A made-up thing."*) and obeys the governing rule: **he may write
  anything except the truth.** She asks whether he made it up just now or already had it.
  🔴 **He had already had it, for four years and another lifetime, and he lies.** That lie is
  the chapter's, and it is the first one he tells for her benefit rather than his own.
- 🔴 **THE GRASS IN THE GARDEN IS COMING BACK** — green at the roots, three days before the
  ceremony. He did not touch it. The counting resumes.

## Gates

```
verify.py            PASS   4,539w · yrs 0-1 · 112 dialogue lines · 0 failures 0 warnings
style_gate.py        PASS   4,532w · dialogue 23.1% · median 9 all / 7 narr · chains 15.2/1k
                              · Lan Shen speaks 28x · 0 failures 0 warnings
canon_copy_check.py  PASS   180 comparisons (10 chapters x 18 extracts) · 0 findings
selftest.py          PASS   14 checks · 14 held · 0 blind
kit selftest.py      PASS   no inherited-gate regression
Serial total         50,136 prose words across ten chapters. Year 0 closed.
```

## Two things the gates caught that the drafting did not

1. 🔴 **GATE 5 FIRED — AND IT WAS RIGHT.** The panel first said `years 1–1`. Ch9 ends at
   year 0, so the gate reported a GAP. The gate's convention is that a chapter spanning a year
   boundary carries **both** years — and the chapter genuinely opens on the forty-three days of
   term break, which are still Year 0. **The panel was factually wrong, not merely
   non-compliant.** Corrected to `years 0–1`, and the AGE field now says six for the break and
   seven from Awakening Day.
2. 🔴 **CHECK (d) CAUGHT A LOADED MOTIF.** First draft had "the whole of the walk home, which
   was eleven minutes." **"Eleven minutes" is already spent** — ch1's gold network appeared
   eleven minutes before Qin Wu's margin note, and ch3 refers back to it. Reusing it for a walk
   home would have flattened it. Removed. Same class of error as the "eleven years" motif
   misuse already in LOCK 15.

## Deliberate non-events

No rank movement. No ring. No skill. No spiritual power reading — canon 017's test is Year 3
and Wulin measures 38 at nine, not at seven. The grass sense was not used and nobody paid a
cost, because the chapter's discipline is **refusal**. #23's notebook was not opened and the
falsehood in it was not resolved. "There is one thing" was not specified.

---

# CHAPTER ELEVEN — "Four Hours"  ·  shipped 2026-09-20  ·  3,778 words

**File:** `chapters/Chapter_11_Four_Hours.md` · **Prewrite board:** `foundation/PREWRITE_ch11.md`

## Position and frame

```
PLACE      the Lan table · 🔴 the east-wing storeroom, forty feet from Lin Ximeng's classroom
           · the garden gate · the yard pump · the office book
DATE       Year 1. The new term starts day three hundred and seventy-five, nine days after
           Awakening Day. The chapter spans roughly the first month of the Year 1 term.
AGES       Lan Shen seven. Wulin seven. Na'er six and a half — 🔴 NOT at the academy.
           Lan Yue eleven.
RANK       🔴 rank one. ELEVEN CHAPTERS RUNNING. Cannot move: rank ten needs a ring and a
           ring needs a kill.
SENSE      used ONCE, ten seconds, on the returning bank. 🔴 **No cost.** Let go before ten
           became eleven. Count resumed: 19,400 at the bank, 19,600 on the second holiday.
```

## THREE ERRORS CAUGHT BEFORE SHIPPING (all by the prewrite, none by a gate)

```
🔴🔴 1. CH10 CONTINUITY ERROR — found during the ch11 prewrite.
      Ch10's offer gave him "a place in the normal class." He has been IN the Soul Master
      class since ch2 (sixteen children, Lin Ximeng's homeroom), and ch1 established how:
      medicinals supplied in lieu of the fee, subject to valuation. The offer was therefore
      a demotion dressed as a gift. CH10 WAS CORRECTED AND RE-GATED (4,532w → 4,578w).
      The corrected version is sharper: last year was barter and finished in an afternoon;
      this is four hours a week and a name in a column.

🔴🔴 2. "ELEVEN SECONDS" WAS INVERTED AGAINST #15.
      First draft had him take eleven seconds and let go "because eleven seconds was what he
      had paid nothing for once before." That is exactly backwards. #15 and ch3/ch4/ch6
      establish: TEN seconds on the street cost nothing; ELEVEN seconds in ch3 cost a
      nosebleed and a week of total loss; ch6 has him let go "before the ten became an
      eleven." Corrected to ten, and the eleven is now named as the number that took a week
      out of him. 🔴 NO GATE CAN SEE THIS. Check (d) class.

🔴 3. NA'ER OUT OF SCHOOL CONTRADICTED RECEIPT R2.
      R2: schooling is nine years, free and COMPULSORY. The added scene had her saying
      "I'm not going to school." Corrected: she is not in the SOUL MASTER class, and she
      starts next year in the ordinary one, a year behind, which she has worked out for
      herself. 🔴 The corrected version is better — "I'll be the biggest one in it, because
      I'll be six and three quarters and they'll be six. That's what being behind means."
```

## Also corrected in the codex during this prewrite

```
🔴🔴 "LAN ZHI" DOES NOT EXIST. The ch9 sync created a CHARACTERS entry under an invented name
      for Lan Shen's father. The father is LAN HE (name means "blue river"), per the household
      table and per ch1, where the whole table turns on his four words "He's better than me."
      Corrected, with the error recorded rather than quietly edited.

🔴🔴 LAN YUE / LANG YUE ARE TWO DIFFERENT CHARACTERS, ONE LETTER APART.
      LAN  YUE (no g) = AU-ORIGINAL, Lan Shen's SISTER, staged ch1, 4, 5, 6, 7, 8, 9, 11.
      LANG YUE (with g) = CANON, Tang Wulin's MOTHER, staged ch3, ch10.
      No shipped chapter uses both. CHARACTERS.md had a single conflated entry; it is now
      split, with the disambiguation stated above both rows. THIS IS A LIVE HAZARD.
```

## Canon touched

🔴 **Year 1 is canon-silent** — canon 012 is *"Three Years Later."* The beat is therefore a
**precondition**, not an event: canon 012 has Lin Ximeng discovering the cause of Wulin's fast
cultivation, and a man does not discover that out of nowhere. **Ch11 stages the file being
kept in the year it starts to have content.**

Also held: **R2 (schooling is nine years, free and compulsory)** · **canon 004 (Lin Ximeng,
homeroom, three years, MALE per the ruling)** · 🔴 **canon 017/018 untouched — Wulin is seven
and the test is at nine.**

## #26 — the binding corrections, executed a second time

```
(a) FACE          ✅ LIN XIMENG. THE DETECTOR. Named, motivated (he wants an explanation),
                  on page and inside his own head. He never raises his voice either — two men
                  in this serial now do not raise their voices, and they are the two most
                  dangerous people in it. Plus Su Wan, Lan He, Lan Yue, Na'er.
(b) NUMBER        ✅ his name goes into a column with SIXTEEN HOURS against it, in a hand that
                  is not Yan Song's · the black book's six-month hole starts filling · the fee
                  becomes formal · the garden count resumes and rises · 🔴 and Lan Yue's
                  "four hundred and sixty-eight weeks / a thousand eight hundred and seventy
                  hours" arithmetic, done at a pump in four seconds
(c) REGISTER      ✅ Other POV again — Lin Ximeng, italics. Five registers used.
(d) BUTTERFLY     ✅ pre-drafted. TWO ANOMALIES IN ONE SMALL CLASS: canon 012's solo
                  investigation becomes a comparative one, and a man comparing two unexplained
                  boys finds the difference faster than he would find either alone.
```

## Wires left open

- 🔴🔴 **LIN XIMENG CANNOT TELL INTEREST FROM RELIEF.** He wrote one line at the top of a new
  page and then sat with the book open, *"because he was an honest man in the specific way that
  men who keep records are honest, and he wanted to be quite sure, before he wrote anything
  else, that what he was feeling was interest and not relief. He could not tell the
  difference."* 🔴 **He wrote the not-telling down too.**
- 🔴🔴 **THE OFFICE BOOK HAS HIS NAME AND SIXTEEN HOURS AND NOTHING ELSE.** No note, no dash,
  no mark. Written in **a hand that is not Yan Song's.** Contrast with Na'er's column, which
  has something in it that nobody has seen.
- 🔴 **THE STOREROOM IS FORTY FEET FROM THE CLASSROOM.** He found out on the first afternoon,
  after agreeing. *"I bought four hours a week and I did not ask where the four hours were."*
  He priced the cost correctly and located it wrongly.
- 🔴 **LAN YUE HAS BEEN GIVEN A SCENE AND A STANDING DEMAND.** Seven chapters as a delivery
  mechanism, then: *"I want you to tell me one thing. Any one thing. Not the jar thing, not the
  garden thing, not the count. One thing about you that isn't about work."* He answered
  **the canteen soup.** She said *"Next Wednesday you get a second one and I'm not asking for
  it. You just have it ready."* He said he would. She said he wouldn't. 🔴 **HE COULD NOT FIND
  A FACT ABOUT HIMSELF THAT WAS NOT A MEASUREMENT, A PLAN OR A LIE — and the not-finding was so
  fast it felt like an answer to a question he had not known he was being asked. DO NOT DROP
  THIS.**
- 🔴 **SU WAN HAS NOT BEEN ANSWERED.** *"A boy who has an answer that good at seven has been
  keeping it somewhere. Where have you been keeping it."* — *"Everywhere."* And: *"Have you
  counted what you're getting for it."* He gave her the supplier-vs-books arithmetic. She said
  *"That's a good answer too"* and *"That's the problem with them."* 🔴 **She is the most
  dangerous person in Book One and she is not hunting him. Do not soften her.**
- 🔴 **NA'ER KNOWS WHAT SHE IS.** *"Nobody asks me if I want to be in anything. They ask if I
  have one."* And she is in his book now: *Na'er came*, in the smaller hand, under a count.
  She asked why her name was in it. He said *"Because you came."*
- 🔴 **HE STILL HAS NOT LOOKED AT THE OTHER BOOK.** The rank column, the yard, the tray of
  coins. *"He had decided in the autumn that he was not going to look at things until he was
  ready, and he was not ready. Not yet."*

## Gates

```
verify.py            PASS   3,785w · yrs 1-1 · 115 dialogue lines · 0 failures 0 warnings
style_gate.py        PASS   3,778w · dialogue 25.5% · median 10 all / 7 narr · chains 13.2/1k
                              · Lan Shen speaks 32x · 0 failures 0 warnings
canon_copy_check.py  PASS   198 comparisons (11 chapters x 18 extracts) · 0 findings
selftest.py          PASS   14 checks · 14 held · 0 blind
kit selftest.py      PASS   no inherited-gate regression
Serial total         53,967 prose words across eleven chapters.
```

## Drafting notes

First draft ran **26.6/1k chains — a hard fail and the worst in the serial** (ch4 was 26.5).
Twenty-five paragraphs carried two or more. One tightening pass brought it to **13.2/1k**,
below the 16.9 voice bar. 🔴 **The pattern is now established across four chapters: budget one
tightening pass per draft, always, and expect the first measurement to be over.**

---

# CHAPTER TWELVE — "The Middle"  ·  shipped 2026-09-20  ·  3,526 words

**File:** `chapters/Chapter_12_The_Middle.md` · **Prewrite board:** `foundation/PREWRITE_ch12.md`

## Position and frame

```
PLACE      🔴 a ground-floor room in the east wing, DIRECTLY ABOVE THE SOWN GRASS · the
           east-wing storeroom · the Lan table on a Wednesday · the yard pump, in the dark ·
           the gate of Na'er's ordinary school
DATE       🔴 years 1–2. Ch11 closed in the first month of the Year 1 term. Ch12 runs about
           fifteen months: the rest of Year 1 (spring peak, summer), then 🔴 **Year 2's first
           term (autumn)**, closing in **the winter of Year 2**.
AGES       Lan Shen seven, then eight (birthday in late autumn; Su Wan tells him he has not
           said). Wulin the same. Na'er seven and three quarters. Lan Yue eleven.
RANK       🔴 rank one. TWELVE CHAPTERS RUNNING. Cannot move: rank ten needs a ring and a ring
           needs a kill.
SENSE      🔴🔴 **USED ZERO TIMES ON PURPOSE.** This is the chapter's engine. Sixty thousand
           strands directly under the floor for a whole term, and he does not touch one.
           Self-timed ceiling: NINE MINUTES, hands shaking slightly, no nosebleed, no white
           line. Bank counted every holiday: peaked at 41,200 in midsummer, down again through
           autumn, written down every time, touched never.
```

## 🔴🔴 SEVENTEEN DEFECTS CAUGHT BEFORE SHIPPING

Ch11 caught three, all in the prewrite. Ch12 caught seventeen, and only four of them came from
a gate. **Check (d) is now demonstrably the highest-yield instrument in the kit** — it found
nine defects that no gate can find, including one knowledge-firewall breach.

```
FROM THE GATES (4)
 1. Gate 2      digit in prose — "Year 2 term".                    → "the second year's term"
 2. style_gate  dialogue 10.0%, floor is 13%.                      → +2 dialogue scenes
 3. style_gate  ', and' chains 26.7/1k. TENTH consecutive chapter
                over the bar on first draft.                       → tightening pass → 18.7/1k
 4. style_gate  bold **form** used for EMPHASIS. Voice Law s6 says
                bold marks a term, never stress.                   → de-bolded

FROM CHECK (d) — THE MANUAL READ (13)
 5. 🔴 "four years" x2 — ch1's clock starts at age two, he is seven. → "five years"
    (The third "four years", Lin Ximeng's black book, is CORRECT: ch11 said three, +1 year.)
 6. 🔴 "forty-one thousand strands" under the academy floor — 41,200 is the BANK's summer
    peak. Two unrelated places sharing a number reads as a false echo. → "sixty thousand"
 7. 🔴 STRUCTURAL: the Wulin-at-the-door scene was inserted BEFORE the meditation it follows.
    "Afterwards" happened first.                                   → moved below the reflection
 8. 🔴 GENDER: Jiang Ning referred to as "he" three times. Ch2 established her —
    "Jiang Ning's ears went pink and her chin stayed up."          → she/her throughout
 9. 🔴 ARITHMETIC: "fifteen of them... sixteen the year before... one family gone to the
    harbour... one new boy" = 16 − 1 + 1 = 16, not 15.             → two gone, one arrived
10. 🔴 CHRONOLOGY: the measuring was set in "the second term" of Year 1, but ch11 fixes Year 1
    at SIXTEEN children. The fifteen only exists in Year 2.        → moved to Year 2, term 1
11. 🔴 DERIVATIVE: once the measuring moved, "a term and a half" of weekly numbers could not
    fit inside a chapter that ends in the same winter.             → "a whole term", ten weeks
12. 🔴 DERIVATIVE: his own column listed nine numbers against "a term and a half".
                                                                    → ten numbers, ten weeks
13. 🔴 DERIVATIVE: "Second term, third week... Summer term, first week" — those are Year 1
    terms, and the measuring is now Year 2.                        → "Third week... Eighth week"
14. 🔴 "eight was the number he needed" — EIGHTH is a POSITION; four minutes is the number.
    The sentence asks for a duration and supplies a rank.          → "four was the number that
                                                                      put him eighth"
15. 🔴 UNITS — THE WORST ONE. "*The street was eleven.*" Ch11's eleven is SECONDS
    (ten free, eleven costs a week). Ch12's clock runs in MINUTES. In a passage about
    minutes, "the street was eleven" silently converts a loaded motif into a different
    unit and destroys it.                                          → "The street was eleven
                                                                      seconds and it took a
                                                                      week out of me"
16. 🔴 "nine was twice what the class was doing" — the class does four. Nine is 2.25x.
                                                                    → "more than twice"
17. 🔴 "it had been there for two years while he sat above it every afternoon" — the GRASS is
    two years old; HE has been at the academy one year.             → split the two clocks
```

## 🔴 KNOWLEDGE-FIREWALL BREACH, CAUGHT

Lin Ximeng's italic section read: *"Three and three quarters — once, in the week his sister
started work at the harbour."*

Two separate failures in nine words:

- **Firewall.** Lin Ximeng has no route to knowing when Lan Yue starts a job. He watches a
  corridor, not a household. Firewall rows exist precisely to stop this.
- **Fact.** Lan Yue does not work at the harbour. Ch5 and ch8 both put her washing dishes on
  the noodle street, eleven copper a day.

Replaced with something a man standing in a doorway CAN see: *"once, in the week the boy had a
cold."*

🔴 **Lesson: an Other-POV section is a firewall audit, not a stylistic choice.** Every fact in
another character's head must be reachable by that character. Run the reachability question
line by line, every time.

## 🔴 DEVIATION FROM PREWRITE — RECORDED, NOT EXCUSED

`PREWRITE_ch12.md` ruled that **Other POV would deliberately not be used** this chapter,
because ch10 (Qin Wu) and ch11 (Lin Ximeng) had already used it twice running.

The Lin Ximeng italic section was written anyway.

Reason: the flat line is the chapter's discovery, and **it is only visible from inside the man
keeping it.** From Lan Shen's side, four minutes looks like success. Only Lin Ximeng can see
fifteen children scatter and one not move. Cutting the section would have cut the chapter's
only piece of dramatic irony, and the ending — *"why is this straight"* — would have had
nothing to be ironic against.

Status under #26(c): **legal.** The rule requires Other POV at least once per three chapters;
it does not cap it. But three consecutive chapters makes it the DEFAULT rather than the
exception, and a default register is not a register.

🔴 **BINDING ON CH13: Lan Shen's own register, unless there is a stated reason it cannot be.**

## Canon touched

```
012  "Three Years Later"     🔴 HELD, and now PARTIALLY STAGED. Canon 012 has Lin Ximeng
                             guiding Wulin after discovering his spiritual power. Ch12 stages
                             the BEGINNING of that guidance: two desks instead of sixteen rows,
                             a hand on two shoulders, notes about form. The discovery itself is
                             still ahead and still needs the helmet.
                             🔴 Na'er has NO martial soul in canon 012 — honoured: she starts
                             the ordinary school, in the sixes, a year behind, and the chapter
                             names what that costs without spending it.
013-018                      held, untouched. Next anchor 013 (Year 3).
017/018  spiritual power     🔴 Wulin's 38 is STILL UNMEASURED. It belongs to age nine, Year 3.
                             Ch12 puts the reason for the delay in Lin Ximeng's own head:
                             proving it "needed a helmet and a hall and a hundred Federation
                             Coins that nobody in Glorybound City was going to spend on a child
                             who was already doing perfectly well."
R2   schooling               🔴 HELD. Nine years, free and compulsory. Na'er in school, not out.
```

## #26 — the binding corrections, executed a third time

```
(a) FACE      Lin Ximeng escalates from OBSERVER to INSTRUMENT. Ch11 he kept a file. Ch12 he
              keeps a CONTROL. A watch, a narrow column, fifteen names, and a boy he cannot
              explain who is being used to explain another boy. Also on page: Su Wan, Lan Yue,
              Wulin, Na'er, Jiang Ning (first speech since ch2), the boy at the back.
(b) NUMBER    🔴🔴 THE FLAT LINE. Four minutes, ten weeks, eighth of fifteen, every time.
              His real ceiling is nine and it costs him nothing. Bank 41,200 peak. Academy
              grounds sixty thousand strands, untouched once. Hours: four books, agreeing.
(c) REGISTER  Other POV, third chapter running. Legal, but see DEVIATION above. 🔴 Binding on
              ch13.
(d) BUTTERFLY 🔴🔴 #26 RE-AUDIT NOW FALLS DUE. Ch13 must re-run all four from scratch.
```

## 🔴🔴 #27 — "the thing he could not find" — HELD, UNRESOLVED, ADVANCED ONE STEP

Ch11: he searched for one fact about himself that was not a measurement, a plan or a lie, and
could not find one.

Ch12: **Lan Yue starts keeping a list.**

He brings four substitutes across four Wednesdays — the canteen soup, the smell of the storeroom
in the morning before the window is opened, a way of walking home two streets longer than the
short way that he has never once taken the short way on. She rejects each one:

> *"That's about work."*
> *"It's about soup."*
> *"It's about soup at your work. Next."*

Then she explains what she is doing:

> *"Because you're not going to say the real one, so I'm going to write down all the ones you
> say instead, and one day there'll be enough of them that it'll add up to a person, and I
> won't have to ask."*

She writes them on the back of a noodle ticket in a hand worse than his. He is seven, she is
eleven, and he goes to bed and works out whether that was a threat. Decides it was not. Then
decides **that the reason it was not a threat was worse.**

🔴 **RULING STANDS: do not resolve, do not let him agonise.** The Wednesday is a metronome, not
a crisis. Track 8 is the eventual answer — a man with nothing about himself can still make
things up — and it must be EARNED, never stated.

🔴 **New this chapter: the list is a physical object.** The noodle ticket exists. It is in the
house. Somebody could find it.

## Wires left open

- 🔴🔴 **THE FLAT LINE IS IN A BLACK BOOK IN A DRAWER WITH THE REGISTER.** Lin Ximeng has
  written, at the top of a fresh page, in the hand he uses for dates, that *in fifteen children
  measured once a week for a whole term, there was exactly one whose number did not move.* He
  has been to the office twice about Wulin and been told there is no procedure. He did not go a
  third time, *because a man who goes to an office three times about two children in a small
  city acquires a reputation that has nothing to do with either child.*
- 🔴🔴 **"WHY IS THIS STRAIGHT."** Written in the smaller hand, underneath ten fours, at the
  back of the book on the second row of the shelf. He does not have an answer, does not think
  it is a dangerous question, and goes to bed. 🔴 **It is the most dangerous thing in the
  house and he has filed it with the soup.**
- 🔴 **NOT ONE OF LIN XIMENG'S NOTES WAS ABOUT WHAT HE WAS DOING.** *"Your breathing's high."
  "You're holding your jaw." "You're counting — that's fine, keep counting, count slower."* All
  form, for a whole term, because there was nothing to say about the rest. 🔴 **"You're
  counting" made him go cold all the way down.** The man saw it and let it go.
- 🔴 **NINE MINUTES IS IN THE BOOK AND NOWHERE ELSE.** Hands shaking slightly, no nosebleed, no
  white line, door shut, standing up, on a Tuesday in the second week. He did not go higher,
  because the price was width and a rule tested in one direction is not a rule.
- 🔴 **SU WAN HAS NOW DESCRIBED IT BETTER THAN HE DID.** *"How's the man with the book."* He
  started to say *"He hasn't got a—"* and stopped, because in his house a thing is decided by
  whoever describes it most accurately first. He said *"He's got a book."* She asked what was
  in it about him. He said *"A number."* 🔴 **She then said "You can hold still for longer than
  four minutes" — she has never been told the number, and she got the shape of it right.**
- 🔴 **NA'ER IS IN THE SIXES WITH TWENTY-NINE CHILDREN AND NO MARTIAL SOUL.** *"They're all
  six. And I'm seven and three quarters and I'm taller than the teacher."* She was not taller
  than the teacher. She was going to say something else and did not. He worked out that in four
  months somebody would find out, and that the finding-out would be worse than the ceremony,
  because the ceremony had been one afternoon and the school was every day. 🔴 **He put the
  crate in the cart and did not say any of it to anybody.**
- 🔴 **LAN YUE'S NOODLE TICKET.** Four answers, written down, in a hand worse than his.
- 🔴 **JIANG NING WENT BACK IN.** Two minutes, then back in, then out again. Lin Ximeng wrote
  two down twice. Wulin: *"That's not right. You can't put the same number twice."* Lan Shen:
  *"You can if it happened twice."* Wulin: *"It didn't happen twice. The second one was
  shorter. I was watching."* 🔴 **Wulin was right and Lan Shen let him be wrong, because a
  boy who argues with a record has to have a reason to want it changed.**
- 🔴 **THE NEW BOY WITH THE COUGH IS GETTING WORSE, and Lin Ximeng has put it in a letter to a
  man he does not know, "because that was a thing you could do something about."** Unspent.
- (carried) the office book's hand is not Yan Song's · the rank-column book is still unopened ·
  Na'er is in Lin Ximeng's book · Su Wan is still unanswered.

## Deliberate non-events

```
❌ He did not touch the grass under the east wing. Sixty thousand strands, a whole term.
❌ He did not go above nine minutes.
❌ Nobody measured anybody's spiritual power. No helmet exists in this city.
❌ Wulin did not learn he is being used as a comparison.
❌ Lan Shen did not tell anybody about Na'er's school.
❌ Lin Ximeng did not go to the office a third time.
❌ #27 was not resolved, and Lan Shen did not agonise about it.
❌ The rank-one Bluesilver Grass did not move. Twelve chapters.
```

## Gates

```
verify.py            PASS   3,526 prose words · yrs 1–2 · 81 dialogue lines · 0 failures
                              0 warnings
style_gate.py        PASS   3,526w · dialogue 13.5% · median 10 all / 7 narr · chains 18.7/1k
                              · Lan Shen speaks 30x · 0 failures 0 warnings
canon_copy_check.py  PASS   216 comparisons (12 chapters x 18 extracts) · 0 findings
selftest.py          PASS   14 checks · 14 held · 0 blind
Serial total         57,502 prose words across twelve chapters.
```

## Drafting notes

First draft ran **26.7/1k chains — a hard fail, and the NINTH consecutive chapter over the bar
on first measurement (ch4 26.5, ch6 24.3, ch11 26.6, ch12 26.7 are the logged ones).** A single tightening pass brought it to 18.7/1k, which is over the 16.9
voice bar but under the 20 hard bar, so it passes with a note rather than clean.

🔴 **Dialogue needed two attempts.** First pass added ~120 spoken words and landed at 12.9% —
0.1 short of the 13 floor. A second, smaller pass on the pump scene took it to 13.5%. Lesson:
**when the gap is under one point, add a scene, not sentences.** Sentences get absorbed by the
rising denominator.

🔴 **The compression (#25) worked and is now the model.** Eleven scenes, fifteen months, no
calendar. The chapter never states a date except "the winter of the second year", and nothing
needed one.

🔴 **Check (d) found nine defects the gates could not, including a firewall breach and a unit
collision that would have destroyed a loaded motif.** Standing protocol confirmed at the
highest yield yet.


---

# CHAPTER THIRTEEN — "Made Up"  ·  shipped 2026-09-20  ·  5,314 words

**File:** `chapters/Chapter_13_Made_Up.md` · **Prewrite board:** `foundation/PREWRITE_ch13.md`

## Position and frame

```
PLACE      🔴 the ordinary school, four streets away — a classroom after the bell, twenty-nine
           chairs in six rows, a blackboard wiped in the middle and not at the edges · the Lan
           step · the Tang door · the yard pump · the bench in the back room · the notebook
DATE       🔴 years 2–2. About nine months: last of the Year 2 winter → the autumn of Year 2.
AGES       Lan Shen eight. Wulin eight. Na'er eight (turned eight in the winter). Lan Yue
           eleven, nearly twelve — never stated flatly, per the prewrite.
RANK       🔴 rank one. THIRTEEN CHAPTERS RUNNING.
SENSE      🔴🔴 ZERO USES. FOUR SEASONS RUNNING. Bank: 20,100 at the end of winter → peak
           42,600 in midsummer → down through autumn. Counted every time, touched never.
REGISTERS  🔴🔴 LAN SHEN'S OWN. #28 SATISFIED. NO OTHER POV. First time since ch9.
```

## 🔴🔴 #26 RE-AUDIT — EXECUTED A FOURTH TIME, FROM SCRATCH

```
(a) FACE      🔴 NEW FACE REQUIRED — ch12 had passed on a returning one, and Lin Ximeng had
              carried three chapters running. **MADAM ZHOU delivered.** She is not a villain,
              she has no backstory, and she wants an answer rather than a fight. Tang Ziran
              also got his best scene. ✅
(b) NUMBER    🔴 ch12's trick (a number that does not move) could not be repeated. **Something
              had to change value, and it had to change for the worse.** Thirty thousand
              stopped being the price and became the floor. ✅
(c) REGISTER  🔴🔴 #28 BINDING. No Other POV. Lan Shen's own register. Four of five registers
              used. ✅ **NO DEVIATION THIS CHAPTER.**
(d) BUTTERFLY Run pre-draft (the unit table and the year table are now mandatory reads) and
              post-draft. Twenty-two defects. ✅
```

## 🔴🔴 TWENTY-TWO DEFECTS CAUGHT BEFORE SHIPPING

Ch11 caught three. Ch12 caught seventeen. Ch13 caught twenty-two — **and eleven of them were
caught PRE-draft, by the prewrite's new mandatory unit and year tables, which were created
because ch12 failed both.**

```
FROM THE GATES (5)
 1. style_gate  ', and' chains 26.4/1k. ELEVENTH consecutive chapter over on first draft.
                 → tightening pass → 17.3/1k, clean, no warning.
 2. style_gate  bold used for emphasis (Lan Yue's fifth list entry). → italics.
 3. style_gate  dialogue 30.1%, ceiling 30%. 🔴 Fixed by ADDING NARRATION, not by cutting
                 dialogue — ~165 words into the writing-at-night scene, which needed them
                 anyway. → 27.0%.
 4. 🔴 CODEX MARKERS LEAKED INTO PROSE, TWICE. The exact ch3 defect class, recurring in
                 chapter thirteen. → stripped.
 5. 🔴🔴 canon_copy_check FAILED — and it was a FALSE POSITIVE I MANUFACTURED. The canon 019
                 receipt quoted ch6's own prose verbatim ("thirty thousand was two thousand
                 seven hundred and twenty-seven days of eleven copper"). The checker treats
                 everything under canon_extract/ as canon, so ch6 was flagged for copying
                 itself. → paraphrased in the receipt.
                 🔴 **NEW RULE: A CANON RECEIPT MAY QUOTE CANON. IT MAY NEVER QUOTE THE SERIAL.**

FROM CHECK (d) — PRE-DRAFT, via the new mandatory tables (2)
 6. 🔴 codex/PLACES.md had both grass counts labelled one year out (it called ch11's forty
                 thousand "Year 1" when ch11 sits in Year 1's autumn looking back at Year 0's
                 summer). Caught while researching, before drafting.
 7. 🔴 The 1 FC = 1 copper rate was already fixed in CONTINUITY row 6. Found by grep, not
                 re-derived. Re-deriving it would have produced a second, conflicting rate.

FROM CHECK (d) — POST-DRAFT (15)
 8.  🔴 SCALE: "four thousand words on the first night and eleven thousand on the second and
                 third" = fifteen thousand handwritten words on nine pages. Impossible.
                 → 400 / 600 / 500 = about fifteen hundred words on ten pages.
 9.  🔴 OBJECT PERMANENCE: the pages were "nine sheets, folded once" handed across a table,
                 while also living in a notebook on a shelf. → the notebook travels; nothing
                 is torn out.
10.  🔴 LOADED-NUMBER COLLISION: the manuscript was "eleven pages" of a "nine pages" story.
                 Eleven is ch11's seconds motif; nine is ch12's minutes ceiling.
                 → a dozen unused pages, ten used.
11.  🔴 UNFULFILLED PREWRITE ITEM: movement #2 — the 30,000 → 70,000 re-pricing, called "the
                 chapter's real number" on the board — was NOT IN THE DRAFT AT ALL. Caught only
                 by grepping the shipped chapter for "thirty thousand". → new scene added,
                 sourced from a remark Lin Ximeng makes in class (canon 018's free convergence),
                 so it stays inside the firewall and does not foresee the Grass Snake.
12.  🔴 CONTRADICTION: Madam Zhou says "I've had the note in my drawer since Friday" — she
                 wrote it and gave it to Na'er. → "I wrote that note on Friday and I read it
                 four times before I let her take it home."
13.  🔴 IMPOSSIBLE WITNESS: Zhou says "I saw her give it to a boy at the gate." The handover
                 happened at the Lan step, four streets away. → "She told me she had given it
                 to a boy first."
14.  🔴 DAY-OF-WEEK COLLISION (three-way): the doorstep scene is a Tuesday; Tang Ziran tells
                 Zhou he got it on Monday; and "leaving it in a house for three days" from
                 Friday only lands on Monday. Tuesdays are also his jar-washing days, which
                 would put him at the academy. → the doorstep is now a Monday. One edit fixed
                 all three.
15.  🔴 STALE YEAR COUNT: "Lan Shen had known him for three years." Tang Ziran lives two doors
                 down; he has known him all his life. → "had lived two doors down from him all
                 his life in this street."
16.  🔴 Same class: "a conversation he had been sitting inside for three years." → "for years."
17.  🔴 CHRONOLOGY: "He counted four pages. Then he did not count them any more." sat three
                 paragraphs BEFORE anything had been written. → merged into the writing passage.
18.  🔴 STALE YEAR COUNT: "Thirteen years of a skill carried like a coin sewn into a lining."
                 He is eight. → "Eight years."
19.  🔴 STALE YEAR COUNT: "He had spent seven years working out how to afford a floor." The
                 30,000 arithmetic dates from ch6, when he was six. → "two years."
20.  🔴 STALE YEAR COUNT: "He had not thought about typing once in three years." → "once since
                 he got here."
21.  🔴 PANEL/PROSE SPLIT: the panel said the chapter ends midsummer; the last scene runs
                 through the autumn. → panel now says autumn, nine months.
22.  🔴 PLAUSIBILITY: eleven-year-old reading fifteen hundred words "in about forty minutes."
                 → twenty.
```

🔴🔴 **THE DOMINANT DEFECT CLASS THIS CHAPTER WAS STALE YEAR COUNTS — FOUR OF THEM (15, 18, 19,
20), all the same error, all in the same direction, all invisible to every gate.** Ch9 had nine
month-count errors. Ch12 had two. Ch13 had four. 🔴 **This is now the serial's single most
reliable source of defects and check (d) is the only instrument that finds any of them.**

## Canon touched

```
🔴🔴 019 "Spirit Soul"  FETCHED AND HELD THIS SESSION. The Grass Snake. Ten centimetres,
                       earthen yellow, rhombus scale, weakest of its species, "harmless human
                       raised livestock." Defective — no soul beast genes at all. POSITION ONE
                       HUNDRED OF EXACTLY ONE HUNDRED. 🔴 Fuse within twenty-four hours or it
                       dies; renouncing is allowed. Wulin cries for the first time — not for
                       Bluesilver Grass, not for poverty, not for a thousand hammer swings, not
                       for three years of forging, but because *"all of his efforts were like
                       bubbles that easily popped."* Tang Ziran: *"Lin Lin, let's go home."*
                       🔴🔴 NA'ER: *"Big brother, big brother, don't cry"* — she abandons wiping
                       his tears to hold his head instead, and *"she could feel the pain and
                       suffering in his heart in its entirety."*
                       🔴🔴 **THIS RE-PRICES THE WHOLE SERIAL. Thirty thousand — the number Lan
                       Shen has been working toward since ch6, on the page — is the price of the
                       hundredth slot.** His target was never 30,000.
016  price table        Random 30,000 FC · ten-year WHITE 70,000 (73 in stock) · hundred-year
                       YELLOW 1,000,000 (11 in stock). 🔴 **The price follows the age, not the
                       quality.** That is the sentence Lin Ximeng says in class, and it is the
                       hinge of the chapter.
011  Lang Yue's job     🔴 STAGED. She goes to find work; a dye house, four mornings a week,
                       indigo on her hands. Canon 011 receipt honoured.
013-018                held, untouched. Next anchor 013 (Year 3, the workshop).
R2   schooling          🔴🔴 HELD AND LOAD-BEARING. Madam Zhou cannot expel Na'er — nine years,
                       free and compulsory. **Her inability to remove the problem is the entire
                       shape of the scene.** Elementary = three years; "the second year of
                       three" carries over from ch12.
```

## 🔴🔴 TRACK 8 — FIRST MANUSCRIPT IN THIRTEEN CHAPTERS

The author ruling (2026-09-20) made Lan Shen a professional author in his previous life. For
twelve chapters that ruling existed only as backstory. Ch13 puts it on paper.

```
THE OBJECT    Ten pages at the back of the notebook, second row of the shelf, square to the
              edge. The same notebook that holds the counts of grass, the column of fours,
              *why is this straight*, and 🔴 a falsehood (#23). It now also holds a story.
THE WORDS     About fifteen hundred. Four hundred the first night, six hundred the second,
              five hundred the third. The ending written three times; the third is the first
              with two sentences taken out of the middle.
THE CRAFT     *that is what it always was. You write three and you keep one and the one you
              keep is the one you thought of first with the rubbish removed.* And: *he knew it
              was good in the specific way he had known it in the other life, which was not a
              feeling so much as a cessation of arguing.*
THE FIRST     🔴 "What he wrote was not about a girl with no martial soul." Made in about two
DECISION      seconds, and correct, *"because he had spent five years learning what a thing
              looked like when it was aimed at a child who was being pitied. A girl with no
              martial soul is a girl with a hole in the middle of her. You do not write that.
              You write the other thing."*
THE CONCEAL   The story is set in a city of nine million. Not Glorybound. Deliberate.
🔴🔴 THE      He wrote, in the middle of the fifth page, that the girl could feel it when a
TRUTH         person in the same room was working out whether to say a thing, and that she had
              learned to leave before they finished working it out, because the finishing was
              worse than the not-saying.
              *He had not put that in for Na'er. He had put it in because the paragraph before
              it needed a paragraph after it.*
              🔴🔴 **Canon 019 independently confirms the faculty: "she could feel the pain and
              suffering in his heart in its entirety." Ch3's mist behind her pupil, never told
              to anybody, is now on paper, in his hand, in his own book.**
              🔴 He read it back, recognised it, thought about burning it for about as long as
              it takes to decide not to, closed the notebook, and went to bed.
```

🔴 **THE GOVERNING RULE HELD: he may write anything except the truth. He wrote the truth anyway
— about somebody else, by accident, in service of a paragraph.** That is not a break in the rule.
That is the rule being more interesting than it looked.

## 🔴🔴 #27 — HELD, UNRESOLVED, ADVANCED ONE REAL STEP

He could not give Lan Yue a fact about himself. He gave her a story instead.

> *"It's not a saying one. It's a giving one."*

She read it, and she asked the only question that mattered:

> *"So how do you know about the doorways."*

And:

> *He did not have an answer, and he found that he was not, for once, reaching for one, and
> that the not-reaching was so unfamiliar that he had to look at it before he could speak.*
>
> *"I made it up," he said.*
> *"That's not an answer."*
> *"It's the only one I've got."*

Then she filed it:

> *"It's a fifth one," said Lan Yue, and wrote, at the bottom of the list, under *the soup* and
> *the storeroom in the morning* and *the long way home*, the words *wrote a story about a girl
> who could feel everything and says she made her up*.*

> *It was a category error. A list of facts about a person is not the same as a list of things a
> person has done, and a story is a thing done, and she had filed it with the soup.*
>
> *He did not tell her so.*

🔴 **RULING STANDS: do not resolve, do not let him agonise.** He did not agonise. He noticed the
category error, decided not to correct it, and went to bed. The Wednesday remains a metronome.

🔴 **New this chapter: Track 8 and #27 have touched.** A man with no facts about himself can
make things up — and the thing he made up contained the only true sentence he has written in
two lives. **The serial has now demonstrated the mechanism without stating it.** That is exactly
what OPEN_DECISIONS #27 required. Do not explain it in ch14.

## Wires left open

- 🔴🔴 **THE STORY EXISTS.** Ten pages, back of the notebook, second row of the shelf, square to
  the edge, **where his mother can reach it.** It contains an accurate description of a faculty
  nobody knows Na'er has. Lan Yue has read it. Na'er has read it. Su Wan has not.
- 🔴🔴 **TANG ZIRAN NOTICED.** *"You didn't think that up in the room." — "No." — "How long have
  you had it." — "A while."* He nodded once, said nothing more, and put his hand briefly on the
  back of Lan Shen's neck, **which was a thing nobody in that street did.** 🔴 **Canon 011's
  live fuse — Tang Ziran is investigating his son — is now pointed at a second child. Unspent.**
- 🔴🔴 **MADAM ZHOU WROTE SOMETHING ON THE INSIDE COVER OF HER REGISTER, IN PENCIL, QUICKLY, THE
  WAY A PERSON WRITES A THING DOWN BEFORE THEY HAVE DECIDED WHETHER TO KEEP IT.** She also
  looked at him at the door for about as long as it takes to say a name. 🔴 **That is the Yan
  Song gesture from ch10, given to a different adult by a different author, and it is the third
  time an adult in this serial has timed a look at him.**
- 🔴 **SU WAN HAS NAMED THE ROAD.** *"Nothing is obvious. Obvious is what people call a thing
  when they cannot see the road it came down… But there is a road. I would like to know where it
  starts. And one day you will be old enough that you will want somebody to ask."* 🔴 **She is
  no longer waiting. She is asking on a schedule, and she has told him so.**
- 🔴 **"THIRTY THOUSAND IS THE CHEAP ONE."** Written at the front of the book in the counting
  hand, because it was a count and not a thought. He has spent two years affording a floor.
- 🔴 **NA'ER CALLS THE NAMES.** Twenty-nine, in order, from memory by the third Thursday. Madam
  Zhou wrote something four words long in the third column, and it was not *quiet*. 🔴 **The
  column that goes to the district now has a fact in it about a child with no martial soul.**
- 🔴 **WULIN'S READING OF IT IS BETTER THAN LAN SHEN'S AND HE DOESN'T KNOW.** *"Na'er gets to
  call the names. Everybody in the sixes gets called and she does the calling. That's better
  than being in it." — "It's not better than being in it." — "It is if you're the one holding
  the list."* 🔴 **Lan Shen let that stand too.**
- 🔴 **LAN YUE'S TICKET NOW HAS FIVE ENTRIES AND A CATEGORY ERROR IN IT.**
- 🔴 **TWO OF THE TWENTY-NINE IN THE SIXES ARE RANK ONE.** Zhou: *"rank one at six is not a
  verdict, it's a weather report."* Unspent.
- 🔴 **THE PAPER SHOP ON THE LONG STREET, AND THE MAN WHO COMES FROM OUT OF THE CITY WITH A CASE
  TWICE A YEAR.** A bound book costs more than a good jar of anything Lan He makes. 🔴 **This is
  the first infrastructure of Track 8 and it is entirely unexploited.**
- (carried) the flat line and *"why is this straight"* · nine minutes · "you're counting" · the
  new boy's cough and Lin Ximeng's letter · what Yan Song wrote in the rank column · Qin Wu's
  three forms · Lan Yue's noodle ticket as a findable object.

## Deliberate non-events

```
❌ He did not touch the grass. Four seasons running.
❌ Nobody's spiritual power was measured. No helmet exists in Glorybound City.
❌ 🔴 THE GRASS SNAKE WAS NOT FORESEEN. He reached the PRICE, never the snake. Canon 019 is the
   reader's knowledge, not his.
❌ The manuscript was not sold, shown to an adult who could use it, or taken off the shelf.
❌ Na'er was not fixed. Her Thursdays were made bearable, which is all LOCK 8 permits.
❌ Su Wan was not answered.
❌ #27 was not resolved, and Lan Shen did not agonise.
❌ The rank-one Bluesilver Grass did not move. Thirteen chapters.
❌ Lin Ximeng did not appear in a scene. One reported remark, no dialogue, no interior.
```

## Gates

```
verify.py            PASS   5,326 prose words · yrs 2-2 · 150 dialogue lines · 0 failures
                              0 warnings
style_gate.py        PASS   5,314w · dialogue 27.0% · median 12 all / 9 narr · chains 17.3/1k
                              · 0 failures 0 warnings 🔴 (no warning: chains under the hard bar
                              and dialogue inside the band on the shipped draft)
canon_copy_check.py  PASS   247 comparisons (13 chapters x 19 extracts) · 0 findings
selftest.py          PASS   14 checks · 14 held · 0 blind
Serial total         62,828 prose words across thirteen chapters.
```

## Drafting notes

🔴 **The tightening pass is now ELEVEN chapters deep as a guaranteed cost.** First draft 26.4/1k,
shipped 17.3/1k. The pass is not a contingency; it is step four of drafting and should be
scheduled as such.

🔴 **DIALOGUE OVER THE CEILING IS A DIFFERENT PROBLEM FROM DIALOGUE UNDER THE FLOOR.** Ch12 sat
0.1 below 13% and needed a whole new scene. Ch13 sat 0.1 above 30% and needed ~165 words of
NARRATION — which improved the chapter, because the writing-at-night scene was the Track 8
payoff and was thin. 🔴 **When a dial is over, add the register you neglected. Do not trim the
one that worked.**

🔴🔴 **GREP THE SHIPPED CHAPTER FOR THE PREWRITE'S PROMISED NUMBERS.** The 30,000 → 70,000
re-pricing was called "the chapter's real number" on the board and was simply absent from the
draft. No gate can detect a missing scene. `grep -n "thirty thousand" chapters/Chapter_13*.md`
returns nothing, and that is the check.

🔴 **THE UNIT TABLE AND THE YEAR TABLE, ADDED TO THE PREWRITE AFTER CH12, WORKED.** They caught
the PLACES.md off-by-one before drafting and prevented a re-derivation of the coin rate. But
four stale year counts still got through into the prose — all of them about how long a
relationship or a skill has existed, none of them about a date. 🔴 **ADD A THIRD PRE-DRAFT
TABLE: "EVERY DURATION IN THIS CHAPTER, AND ITS START DATE."**

🔴 **CODEX MARKERS LEAKED INTO PROSE AGAIN, IN CHAPTER THIRTEEN.** This is the ch3 defect class
and it has now happened twice. It is invisible to every gate. 🔴 **`grep -c "🔴" chapters/<new>.md`
must be zero before anything else is checked, because it takes one second.**


---

## 🔴🔴 FULL WORKSPACE AUDIT AND MANAGEMENT PASS — 2026-09-20 (no chapter written)

**Author's instruction, verbatim:** *"There is many more things you should learn, there is clean
up manges and many like tooo many things, please i seriously said check everything and manage
perfectly completely, you have everything please."*

**No chapter was written, shipped or advanced by this entry.** Everything below is repair,
gate-building and ledger maintenance. The story edge is unchanged: end of ch13, autumn of Year 2.

### What was read that had never been read

The workspace root had been treated as scenery. It is instruction:

| Path | What it gave |
|---|---|
| `fix/RUN_ME.md` + `cleanup.sh` + `scrub_email.sh` + `mailmap.txt` + `push_to_github.sh` + `LICENSE` | the TWO-COPIES LAW · the MIT+derivative-work license shape · the H1-numeral rule · the en-dash panel-range regex · *"a number written to satisfy a check is worse than a warning left honest"* · the privacy leak class |
| `uploads/chapter_75.md` | 🔴 **the author's own prose, named in his own `REFERENCE_MAP.md` as the quality bar.** Measured for the first time — see §0.5 of `STYLE_LAW.md` |
| `uploads/NEW_CHAT.md` + `CORRECTIONS.md` + `README.md` | the user-correction culture: do not parrot · do not present files instead of talking · no skill-name stickers · turn law · play full · *find what a trashed scene skipped* |
| `SOUL_LAND_NEW/foundation/PERFECT_STORYLINE_METHOD.md` | the 56-section master method |
| `SOUL_LAND_NEW/foundation/PANEL_BUTTERFLY_DOCTRINE.md` | 🔴 the Butterfly Law · the Perspective Panel Doctrine · legend in outside voices · superlative scoping · the divergence economy |
| `SOUL_LAND_NEW/foundation/METHOD.md` `SL3_FOUNDATION_LESSONS.md` `REFERENCE_MAP.md` | the ten craft laws · the SL1/SL3 quarantine rule · what the uploads are *for* |
| `SARA.md` (archived) | 🔴 the growth-ledger law, and the post-mortem of a dropped project |
| `soul_land_starter/` `SOUL_LAND_UNIVERSAL_KIT/templates/` | the canonical project skeleton — used to check for missing files |

### Finding 1 — 🔴🔴 THE TRANSCRIPTION. The worst defect in the serial, and a gate I wrote said it was clean.

`canon_copy_check.py` reported **PASS on all thirteen chapters**. Its quoted-speech threshold was
**15 words**. Measured reality:

```
                 verbatim canon words     longest run     verdict
ch1                       155                 9w         transcript in places
ch2                       191                13w         transcript in places
ch3                       297                14w         🔴 whole scenes transcribed
ch4                       142                 8w         transcript in places
ch5-13                  0 to 77             5w (generic) clean — written in the house voice
```

Every borrowed run in ch1–4 sat **between 8 and 14 words** — the longest exactly one under the
limit. The first four chapters were staging canon partly by copying the translation's dialogue,
including Lin Ximeng's entire homeroom speech, the whole delinquent scene, and the whole
orphanage dinner. **This is the failure the imported Butterfly Law names explicitly: if a canon
scene can be dropped in unchanged, the OC has been erased from his own story.**

It also explains a measurement that had been sitting unexplained: ch1 and ch2 have the lowest
`did not` density and the lowest structural-simile rate in the serial, because large stretches
were not in my voice at all.

**Repaired.** 42 passages re-voiced across ch1–4 and ch11. Every canon *fact* survives; only the
transcription goes. Post-repair: **0 to 63 verbatim words per chapter, longest run 8w → 0.**

### Finding 2 — 🔴 the gate threshold was chosen before the evidence

15 words was picked because it *sounded* like "a long quote must be a deliberate choice." The
corpus said 7. Rebuilt from measurement:

```
check A   narration 12-grams                      unchanged
check B   verbatim run inside one quote  >= 7w    was 15w
check C   verbatim canon words per chapter > 120  🔴 NEW — catches density, which no single
                                                       run reveals. ch3's disease was many
                                                       short quotes, none over 14 words.
          (6-word floor for counting, so generic English does not inflate the figure)
```

Plus `--budget-fail` / `--budget-warn` / `--report` so the thresholds are testable in isolation.

`selftest.py` gained **section [3]**, four checks, including a regression that injects the exact
ch3 shape — a cluster of 8–14 word runs, none reaching 15 — and fails if the gate passes it.
**14 checks → 18. All held, 0 blind.**

🔴 **The first draft of section [3] was itself broken** and the selftest caught it: I mutated
`_PAD_UNIT` lines expecting them to be dialogue, and they are narration, so two mutators silently
did nothing and reported SILENT. *A gate that has never been seen to fail is a gate nobody has
tested* — including the test.

### Finding 3 — 🔴 the butterfly ledger had stopped at chapter nine

Rows ran **B1–B43, ending at ch9**. Four chapters shipped after that with canon-holding recorded
in appended sync tables and **no divergence rows at all**. And no running decay total existed
anywhere, so the file's own 0/5/15/30/50 ladder had nothing to measure against. Naively summing
the per-row percentages gives **70%** — which would put the serial past its mid-serial turn at
ch9 and is meaningless.

**Added:** B44–B74 (31 rows, ch10–13) · a maintained **RUNNING DECAY = ~15%**, unchanged since
ch3, with the reason (nothing since B9 has moved a canon event he remembers) and the three routes
to ~30% · and the **divergence economy S1–S10** with magnitude, horizon, `last paid` and child
rows. Per-row percentages are now explicitly labelled **local magnitudes that do not add.**

🔴 **S3 is flagged as the worst unpaid thread: the gold at the root has been written down since
ch3 and unpaid for ten chapters.** Deliberate — but deliberate and forgotten look identical from
outside, so it is now written where it can be seen.

### Finding 4 — 🔴 a live personal email was inside the repository

`OPEN_DECISIONS.md` contained the author's real Gmail address, **inside the paragraph explaining
why personal detail must stay out of a public repository.** He has already had that exact address
reach public git history once — `fix/scrub_email.sh` exists to remove it. The file was making the
leak it was warning about. Removed and reworded.

**Layer 5 of `checks/run_all.sh` now gates the leak class** — personal email, token prefix,
noreply id, sandbox domain — built from string pieces so the script does not match itself, and
**proven to fire by planting a leak and watching it fail.** The author's chosen name in `LICENSE`
is public by design and is not a leak.

🔴 **The compromised token in the workspace root was never opened, never used, and is now named
in `HANDOFF.md` §5 as never-open/never-use/never-copy.**

### Finding 5 — 🔴 the style bar had been read and never measured

Nine sentence-level markers measured against `uploads/chapter_75.md` and written into
`STYLE_LAW.md` §0.5. Two real gaps, both to be applied **forward from ch14** — rewriting shipped
chapters to a later voice is the rebuild trap that cost `blue_silver` 90,000 words:

- 🔴 **the `remembered`/`forgot` construction** — his bar 3.8/1k, this serial **0.0 at ch13**.
  Body parts and objects carrying memory, used for reaction and never for exposition.
- 🔴 **noun-phrase fragments in the scanning beat** — his bar 5.1/1k, this serial **0.0 at ch13**.
- ✅ Already right: zero exclamation marks, and plain `said` as the default tag (12.6–13.3 vs 14.3).
- 🔴 **He writes interrogatives with a full stop, not a question mark.** Target zero.
- 📈 **The trend is upward and real:** negation density 5.6 (ch1) → 11.7 (ch13).

### Finding 6 — a lesson was logged and never promoted, so it was re-learned

Re-voicing ch3 dropped its dialogue share from 14.3% to **13.0%, under the 13% floor**.
`SERIAL_LOG.md` already recorded that **this exact thing happened and was solved** in an earlier
de-transcription pass. The lesson lived in a chronological log and not in the LOCKS, so it was
re-hit within a day.

Restored to **13.5%** with two *new* exchanges in the house voice — never by putting the canon
back: the delinquents get their own three-line exchange (*"That's silver." / "She's filthy. Look
at her face." / "Face washes."*), which also serves the Perspective Panel doctrine, and Lang Yue
answers Wulin's shout. Promoted to **LOCK 16.3**.

🔴 **RULE: a lesson that lives only in a log gets re-learned. Logs are records; LOCKS are rules.
Every lesson is promoted to a LOCK in the same turn it is learned.**

### Built

| Thing | Why |
|---|---|
| `checks/run_all.sh` | 🔴 one command, eight layers, exit 0 = ALL GREEN. Modelled on SL3's own suite. Layers 4–6 (marker leak, privacy, build hygiene) did not exist as gates at all |
| `SARA.md` | 🔴 **the self-file, asked for by name and caught frozen once already.** Growth ledger at §5, appended every session |
| `LICENSE` | a public repo with `license: null` legally means "all rights reserved." MIT for the tooling, derivative-work notice for the prose, Tang Jia San Shao credited, scope rewritten for this repo's layout |
| `.gitignore` | a committed `tools/__pycache__/selftest.cpython-313.pyc` was found in the tree and removed |
| `_kit_reference/NOTICE.md` | 🔴 TWO-COPIES: the vendored kit and `tools/` hold two different `verify.py` and two different `selftest.py`. The notice says which is authoritative and why the copy is safe to keep |
| `STYLE_LAW.md` §0.5 | the measured DNA table |
| `NO_MISTAKE_LIVE_RULES.md` **LOCK 16** | eight promoted lessons, the transcription lock chief among them |
| `CANON_LEDGER.md` B44–B74 · RUNNING DECAY · S1–S10 | the ledger repair |

### Decided NOT to build, and why

**No `GLOSSARY.md`. No `RELATIONSHIPS.md`.** The kit's twelve templates call for neither,
`CHARACTERS.md` already carries a RELATIONSHIP SPINE, and the power-term and house-spelling
distinctions already live in LOCK 5 and LOCK 11. Creating them would fork facts that have one
authority each — a TWO-COPIES violation, and gold-plating the author did not ask for. Recorded
here so a future session does not "discover" the gap and duplicate.

### Documentation repaired

`HANDOFF.md` §5 was **stale in ways §1, §3 and §9 were not**: it listed `codex/CANON_LEDGER.md`
and `codex/CONTINUITY.md` (both actually live in `foundation/`), claimed **~30% decay** which was
never true, and carried "synced through ch9" on four files that were synced to ch13. Rebuilt, with
the staleness named at the top of the table. `PROJECT_README.md`'s LAYOUT map carried `~30%`,
"43 rows", "18 receipts", "the fifteen locks" and "15-word verbatim runs" — all rebuilt.

🔴 **Word-count sources were mixed.** `README.md`'s chapter table carried figures that matched
neither gate after the re-voicing; `STATUS_PANEL.md` stated a `verify.py` total above a
`style_gate` table. Convention now written down: **headline totals are `verify.py` (62,994);
per-chapter tables are `style_gate.py` (62,863 summed); never mix the two inside one table.**

### Battery after the pass — all eight layers green, exit 0

```
sh checks/run_all.sh
  1 verify.py            PASS   13 files · 62,994 prose words · 0 failures · 0 warnings
  2 style_gate.py        PASS   exit 2 by design · 1 warning (ch3 word band, permanent, logged)
  3 canon_copy_check.py  PASS   247 comparisons · 0 findings · max 63 verbatim words in any chapter
  4 marker-leak grep     PASS   no codex glyph in any chapter
  5 privacy grep         PASS   proven to fire by planting a leak
  6 build hygiene        PASS   __pycache__ removed, .gitignore added
  7 selftest.py          PASS   18 checks · 18 held · 0 blind
  8 kit selftest.py      PASS   now run from the vendored copy, not from ../ref/
```

Layer 8 previously pointed at `../ref/SOUL_LAND_UNIVERSAL_KIT/`, **outside the repository**, so
the suite would break for anyone who cloned it. Now runs from `_kit_reference/`.

### What this pass did NOT do

- 🔴 **Did not rewrite ch1–4 to ch13's voice profile.** The drift is the record of the learning.
  Only the transcribed dialogue was re-voiced.
- **Did not resolve `OPEN_DECISIONS` #26, #27 or #29.** All still open and binding.
- **Did not touch S8's deadline.** Canon 017/018's 38 is still unspent, and **B62 is the wall.**
  Ch14's prewrite inherits the question: does the helmet arrive for a reason the world would
  supply on its own, or because the plot needs it? **B59 — Lin Ximeng's letter to a man he does
  not know — is already loaded for exactly this.**
- **Did not fetch canon 020–022 or 024.** Fetch queue unchanged.

---

## 2026-09-20 — THE GITHUB SWEEP: two new repositories read, three instruments built, nine fourth-wall breaks found in shipped prose

**The author's instruction:** *"Check my GitHub again there is many things new that can help you
lots you understand yourself everything when you do."* Two repositories were new or changed since
the last sweep: `storyos-site` (350 files, pushed 04:27) and `the-universal-storyline-creation-`,
which had been a dead placeholder and was revived into a working system at 03:45. Both were
cloned, read, and copied into `ref/`.

### What the two repositories are

**`the-universal-storyline-creation-` is now the CONTROL CENTRE** — a state layer for every
serial. `state/` holds canon, laws, firewalls, an append-only growth log and one file per
project; `tools/` validates and ingests contributions; `index.html` and `TRANSFER_BOOTSTRAP.txt`
are generated artifacts. Any agent on any platform files a JSON contribution into `intake/drop/`
and runs `make ingest`. Eight kinds: project, firewall, anchor, canon, lock, decision,
correction, note. **Append-only — nothing silently overwrites; a correction keeps the old value
visible beside the new one with its reason.** Its `state/laws.json` carries the twelve locks and
seven gates that this project was built from, and its selftest is 102 negative tests.

**`storyos-site`** is the web app and framework around the same idea: an independent drift
scanner (`scripts/drift.py`) that deliberately does not trust the project's own validator, plus
`BANNED_TOKENS.json` and a generated `CURRENT_STATE_MANIFEST.json`.

### `lan_shen` was not registered in it. It is now.

`PROTOCOL.md` states the minimum for a project to be safely handable: file a project, all twelve
locks, one firewall per character who knows anything, and an anchor per fixed date. **57
contributions were filed** — 1 project, 12 locks, 14 firewalls, 8 anchors, 6 decisions,
7 corrections, 6 canon claims, 3 notes. Validated with their own validator (**PASS, no issues**,
after three warnings were fixed rather than shipped past: a redundant `project` field on the
project record, and two `earliest_change` values too thin to do their job). Then ingested and
rebuilt: selftest stayed **102/102**, `index.html` 161,448 bytes, `TRANSFER_BOOTSTRAP.txt`
1,129 lines, and `state/projects_registry.json` now names `lan_shen` as live at Chapter13. The
growth log attributes the filing to this agent with a timestamp.

Lock 4 was filed as the kit requires — a sentence with all three blanks filled, both spines.
Note that `extract_state.py` measured six projects in `ref/` but not this one, because this
serial lives at the workspace root rather than under `ref/`; that is a clone-location artifact,
not a defect, and `make measure` re-run beside the real workspace would pick it up.

### Three instruments built into this project

1. **`foundation/BANNED_TOKENS.json`** — the list of values that are known-dead. Five
   categories, each declaring its own scope, because the defect classes live in different parts
   of the tree. `verify.py` gate 3 already forbids every digit in prose, so `stale_stat_drift`
   is a docs-only category and scanning chapters for it would be theatre; `foundation/` uses
   "canon" as a technical term hundreds of times, so `fourth_wall` is prose-only.
2. **`tools/banned_token_check.py`** — layer 9. Imports the four honesty rules from
   `storyos-site/scripts/drift.py`, which exist because a naive scan gets each of them wrong in a
   specific way: claim class, section context, sentence scope, self-file. Without rule 2 the
   scanner reported 2,660 findings, nearly all of them correct history; with it, 16, then 10,
   then 0. **A scanner that cries wolf on receipts gets ignored, and an ignored scanner is worse
   than no scanner.**
3. **`tools/scan_project.py` → `foundation/CURRENT_STATE_MANIFEST.json`** — generated, never
   hand-written. Every number is counted off the disk at generation time, including the gate
   result, which is run rather than asserted. It imports `style_gate.split_prose` instead of
   reimplementing a word counter, because the first reimplementation reported 62,866 where the
   gate reported 62,863 — a third convention in a project that already has two.

### What layer 9 found on its first run — nine real defects in shipped prose

**The word "canon" appeared in Lan Shen's own interiority in four shipped chapters.** Lock 7.6
and the Firewall 0 narration rule forbid exactly this: he experiences the past life as *memory*,
never as fiction, and may not think in terms of canon, the novel, the plot or the author.
Thirteen chapters and eight gate layers had never caught it, because every existing gate judges
whether prose is well-formed and none can know that a word belongs to the author rather than to
the character.

| Ch | Line | Was | Became |
|---|---|---|---|
| 2 | 401 | "it had been asked **in canon** to an empty street" | "he remembered it being asked to an empty street" |
| 3 | 247 | "brave, **canonically** brave, exactly as brave as he had been **on the page**" | "brave, brave in the exact way he remembered, exactly as brave as he had been the first time" |
| 3 | 428 | "**On the page** it was shorter than this" | "He remembered it shorter than this" |
| 4 | 210 | "**Canon had said** that in so many words" | "He remembered that being said in so many words" |
| 4 | 394 | "That was what **canon had said**" | "That was what he remembered" |
| 5 | 74 | "**Canon had not said** the hands were fine" | "He did not remember the hands being fine" |
| 5 | 76 | "*Canon said the opposite.*" | "*He remembered the opposite.*" |
| 5 | 78 | "**Canon had a whole chapter about it**" | "There had been a whole chapter about it" |
| 5 | 350 | "*Canon has a chapter about this.*" | "*There is a chapter about this.*" |

The distinction that made these repairable rather than deletable: **"canon" is meta-vocabulary,
but "I read it in the other life" is memory.** The author ruling of 2026-09-20 makes his previous
life a professional writer's, so remembering a book he read is legitimate and good. The banned
item is the term used by someone standing outside a story. All nine repairs preserve the memory
framing and remove only the meta-term.

Two further findings, both in current-state documents asserting a superseded value as true NOW:

- **`OPEN_DECISIONS.md` §8 said cadence was "currently locked at 2,200–3,500 words per
  chapter"** — the exact figure Lock 11 corrects, and corrects *by name*, as taken from the
  plant-POV serial which is the wrong model for a human protagonist in a city. A live
  contradiction between two current-state documents, in the file that lists open decisions, so
  it read as though cadence were still unruled. Rewritten as a ruled entry with the receipt kept.
- **`PROJECT_README.md` said "eighteen receipts on disk, ch001-018"** when `canon_extract/`
  holds nineteen. Corrected.

### Decisions NOT to build, and why

- **`on the page` is deliberately not a banned token.** It produced two false positives
  (ch8: his own notebook; ch10: Yan Song's register) for one true hit (ch3:428), and this serial
  is full of literal pages — the notebook, the register, the herb-shop slips, the manuscript. A
  rule an instrument cannot apply honestly is worse than no rule. The true hit was repaired by
  hand and the reasoning is recorded in the config under `not_banned_deliberately`.
- **`marker_emoji` and `privacy` were removed from the config after being written.** Layer 4
  already greps chapters for the working glyphs and layer 5 already greps the whole repo for the
  author's real email, ghp_ tokens, the sandbox id and the arena.local host — building each
  pattern from pieces so the script does not match itself. A generic email regex here would be a
  weaker second copy of a stronger rule. TWO-COPIES forbids it. Layer 4's glyph list was instead
  widened from two glyphs to eight, and the config now carries an `owned_elsewhere` map naming
  the home of eight rules this file must not duplicate.
- **The lock-numbering collision is documented, not renumbered.** `## 11. CADENCE` and
  `## 🔒 LOCK 11 — THE HOUSE SPELLING` both claim 11, and 12 likewise. Every reference already in
  the project (`PREWRITE_ch10`, `PREWRITE_ch13`, `SERIAL_LOG`, `STYLE_LAW`, `HANDOFF`) means the
  live lock, which was checked before writing anything. A NUMBERING block at the top of
  `NO_MISTAKE_LIVE_RULES.md` now states the rule: **a bare `LOCK n` always means the live lock;
  cite constitution locks by name.** Renumbering would require editing `SERIAL_LOG.md` and the
  `PREWRITE_ch*` snapshots, which are append-only receipts — and falsifying a receipt to fix a
  label is the worse error. Sixteen locks remain in force.
- **`extract_state.py` was not modified** to reach this project. It is their instrument, in their
  repository, measuring their workspace.

### The gate caught me

Importing `style_gate` into `scan_project.py` wrote `tools/__pycache__`, and layer 6 (build
hygiene) failed the build on it. **Fixed by suppressing the bytecode, not by teaching the hygiene
layer to tolerate it** — a generated file in the tree is the defect, and lowering a gate to pass
is forbidden. Recorded because it is the second time this session a new instrument was caught by
an existing one before it could ship.

### Selftest extended 18 → 20

The kit's `negative_test_rule`: a gate that has never been seen to fail is a gate nobody has
tested. `banned_token_check.py` gained a `--file` mode so `selftest.py` can inject "in canon"
into the clean sample and confirm the gate fires, then confirm it stays silent on the clean
sample. Both hold. 20/20.

### Totals moved

The nine repairs changed the counts by three words: **`verify.py` 62,994 → 62,997**, and
`style_gate.py` summed over the same files **62,863 → 62,866**. The gap between the two
conventions is unchanged. Both dead figures were added to `stale_stat_drift` in the same turn,
per the lesson-promotion law — a defect found once must become impossible, not merely fixed.
The serial-total ladder in LOCK 13 gained a rung and demoted 62,994 rather than overwriting it.

**End state: 9 layers, ALL GREEN, exit 0. Selftest 20/20. Control Centre selftest 102/102.
Layer 9 reports 0 failures and 23 exempt receipts.**

---

## 2026-09-20 (second sweep) — the kit moved to verify v2.2 while this serial was mid-audit; the fork was rebased

**The author's instruction, again:** *"Check my GitHub again there is many things new that can help
you lots."* Two repositories had been pushed at 05:54–05:55, twenty-six minutes after the previous
sweep cloned them. The new commits:

- kit `ee9969d1` — *"SL2 The Unraveled Tide: Size-2 re-rail + unified verify gate (v2.2)"*, 45 files
- projects `4e1370a3` — *"Install unified verify gate (v2.2) — byte-identical to the kit"*

### What v2.2 is

The kit had **two files named `verify.py` with two rule sets and two verdicts for the same
project** — a 288-line chapter gate and a 93-line project scanner. v2.2 is one file doing both
jobs, and its own rule for the merge was: *neither previous rule set was weakened; where the two
disagreed, the stricter reading is kept and the disagreement is named in the output.* 598 lines.

It found a real bug in v1 while being written: **"prose extraction returned an empty panel on 230
of 230 chapter files. The gate was working correctly and measuring the wrong text."** v2 removes
three apparatus regions before classifying prose — (A) fenced blocks, (B) the head (title plus
metadata up to and including the first `---`), (C) the tail from `## End of Chapter N` to EOF —
conservatively, so that a region is stripped only when it cannot be story.

It also adds a **name-digit exemption** to gate 3, red-tested in both directions: `Room 108`,
`Dorm333`, `Rank39`, `ch17` pass, while `rank 29` and `6:04` still fail. And it fixes the dialogue
regex to count **curly quotes**, because "counting only the straight form reported those chapters
as having no dialogue at all."

### The decision to rebase, and the measurement that drove it

`tools/verify.py` here was a v1 fork: the kit's 288 lines plus two local gates. Three questions
decided it.

1. **Does v2.2 agree with the fork on this corpus?** Both PASS. Fork 62,997 words, v2.2 62,988 —
   nine words of head apparatus in chapters 1–9 that v1 counted as story. v2.2 reports
   `[apparatus: head]` for ch1–9 and `[apparatus: NONE]` for ch10–13, which have no `---`.
2. **Is the curly-quote gap live or latent?** Measured, not assumed: **zero curly open-quotes in
   all thirteen chapters**, and both regexes count 1,541 dialogue spans. Latent, not live — but a
   false negative sitting in a HARD gate, waiting for the first chapter that types a smart quote.
   That is the whole reason the kit fixed it.
3. **Are the local gates portable?** v2.2 keeps the same `verify_file` shape, the same
   `split_fences` returning `(panel, outside, extra_blocks)`, and the same `MARKER` / `PANEL_RANGE`
   / `PANEL_ANY`. Only `PANEL_FIELD` had to be carried across.

So: **rebased.** `tools/verify.py` is now upstream v2.2 verbatim plus local gates 8 (panel field
discipline) and 9 (the en dash is load-bearing), 655 lines, with a header that says gates 1–7 are
the kit's and must be edited upstream and rebased, never patched here. `_kit_reference/` was
re-vendored to v2.2 in the same pass, which is what its own `NOTICE.md` instructs — *"if the
upstream kit changes, re-vendor the whole directory in one commit; do not patch a file inside
it."* Only the two tools files had changed upstream, so the law documents and templates are
untouched and still current.

**Selftest held 20/20 against the rebased gate**, which is the evidence that the two local gates
survived the port rather than being silently no-opped — the kit's own warning is that *"a checker
edited into a no-op still prints green."* Layer 8 now runs v2.2's 22-check selftest.

### The project sweep, and why it is not a tenth layer

v2.2's `--project .` mode was run against this serial: **VERDICT PASS** — 0 bad filenames, CJK in
0/13 chapters, 0 chapters with digits in the story, 0 chapters under three spoken lines, and
**0/13 chapters carrying a footer**, which is Lock 9 (*no footer, none, not one line*) proved by
an instrument for the first time rather than asserted by a document.

It was **not** added as a gate layer. Its extra findings are advisory by the kit's own definition
— *"reported with counts, never fails the build alone"* — and its hard gates would run over the
chapters a second time beside layer 1, which TWO-COPIES forbids. Instead `tools/scan_project.py`
now runs the sweep and records every count in `CURRENT_STATE_MANIFEST.json`, where an advisory
belongs: reported, dated, and measured.

### One open item surfaced, deliberately not acted on

`[cjk-docs] docs carrying CJK: 23/48 (advisory, ruling pending)`. The kit's position is that
*"codexes carry name glosses by established practice — reported as a list, awaiting an author
ruling."* Stripping name glosses from 23 documents is an author decision, not an agent one, so it
is recorded here and left alone. Chapters are 0/13 and that is the hard gate.

### Totals

**verify.py 62,997 → 62,988** (v2.2 strips head apparatus). style_gate.py unchanged at **62,866**.
The gap between the two conventions narrowed from 131 words to 122 for exactly that reason, and
the convention note now says so. 62,997 was banked in `stale_stat_drift` in the same turn, and the
serial-total ladder gained a rung rather than overwriting one — it now reads 62,828 → 62,994 →
62,997 → **62,988 CURRENT**, with each superseded figure keeping its reason.

**End state: 9 layers ALL GREEN, exit 0. Selftest 20/20. Kit selftest 22/22 on the vendored v2.2.
Control Centre selftest 102/102.**

---

## CHAPTER FOURTEEN — "The Empty Case" (shipped 2026-09-20)

**5,785 words (style_gate) / 5,794 (verify) · 14 chapters · serial totals 68,782 (verify
v2.2) / 68,651 (style_gate).** Gates: 9 layers ALL GREEN. Style: PASS clean — ', and'
12.8/1k (under the 16.9 bar), dialogue 26.6% on the standard dial, median 11/11, 64
protagonist turns. **First chapter written under STYLE_LAW §0.5:** remembered/forgot 15
(~2.6/1k), three fragment clusters, zero question marks, zero exclamation marks, plain
said-tags, ~5 prose em-dashes.

**Span:** years 2–3, ~one year, compression. **Anchor:** canon 013 staged as reception
only (the doorstep news; the workshop stays shut). **Canon 020/021 were fetched and
receipted this session (21 receipts).** The **progression ruling** (LOCK 14, 2026-09-20)
landed: the list moves one → two publicly while the private number stays felt and
unwritten — slow exterior for its own reason, and the school's two instruments now
contradict each other on paper, which is the helmet's road.

**Track 8's question answered:** who buys — nobody here. The coast copy-shops, through a
man whose case comes home empty: 12–20 copper, one part in three, never carried twice.
First window missed. First money by the hand: washhouse letters (81 → 64 copper jar).
New faces: **Old Pei**, **Qiao**.

### Defects caught this chapter (prewrite outcome carries the full detail)

1. canon_copy FAIL — one 9-word run echoing canon 014's "actually an extra two hundred."
   Gate-caught, re-voiced pre-ship. **Canon facts must arrive re-voiced even as numbers.**
2. ', and' drift 21.1/1k → 12.8 after 35 curated splits. Fixed in the work, not the gate.
3. One '?' in dialogue against the full-stop interrogative law. Fixed; literal greps now
   standard in the DNA pass.
4. One stale-duration instance of ch13's class ("five years running" for a three-year
   practice) — caught by eye during the mandatory audit.
5. Two CJK characters typed mid-draft; removed pre-battery. First at-composition instance.

**Carry to ch15:** Other-POV slot (Na'er ranked first) · canon 014/015 anchors (the ring
is reader-knowledge only) · fetch 022/024 before locking the ch15 board · the file must
accrete, not resolve · the sewn book waits for the thaw.


---

## SESSION NOTE 2026-09-21 (pre-ch15) — fourth GitHub sweep: kit gained two laws

Sweep found: **NEW REPO** `the-universal-storyline-creation-` (the Devouring Dragon serial's
registry/site), kit pushes TODAY, and `soul-land-projects` gaining `seed_of_creation` (an
SL2.5-era scaffold from a sibling session — no chapters, awaiting its spine ruling; read,
nothing to import). Kit `verify.py` HEAD = our vendored v2.2 **byte-identical**; no re-vendor.

**IMPORTED — kit 07_PROSE_LAW §10 SCOPE LAW + §11 PLAIN LANGUAGE LAW** (author rulings made
on the DD serial, carried by the kit to all projects): imported to `STYLE_LAW.md` §0.6 with
application decision — **forward from ch15, no retroactive rewrite** (blue_silver law).
New artifacts: `foundation/PLAIN_WORD_LIST.md` (vocabulary classified: retired none · flagged
14 terms · WATCH "the stairs"/"the file") and `tools/plain_word_check.py` (advisory, never
fails; baselines: door=49 mostly literal, bank=45, stairs=1, file=0 in prose). DD's own two
chapters were cut 4,008→2,728 and 4,673→~3.x under these laws; the per-chapter word budget
is DD-local — the principle binds here, the number does not. Battery: 9 layers ALL GREEN.

---

## CHAPTER FIFTEEN — "Ten Minutes" (shipped 2026-09-21)

**Board:** `foundation/PREWRITE_ch15.md`. The Other-POV slot — **Na'er, in the established
italic form** (first full chapter in her hands; she opens it and closes it), Lan Shen's
own register second. Span: canon D0 night → D1 evening. First chapter under kit SCOPE +
PLAIN laws (§0.6) AND the last one drafted without a readability ceiling.

**Staged (canon 014 tail + 015 held in full, all re-voiced):** the money-night interior
(30,200 put behind the pickle jar; the doll placed silently — violet eyes, dyed silver
hair, first workshop wage, cabbage-week smuggler, secret daughter-name); Wulin slips out;
🔴 **the seven-color ring is reader-knowledge ONLY** — Na'er sleeps through it and her
interior holds dream-sensation (wide, warm, **seven somethings by the chairs, never
colors, never faces**); the dawn "Lin Lin" street-call, voice tearing; the dew-wet boy,
gem-luster skin, safety-voice, "I know, Mom"; breakfast (her bottomless hunger, "your
eyes are bright," mother's kettle-test hand, "Congratulations, big brother"); test today,
Pagoda first-thing D2, 🔴 **Lang Yue's day-off REFUSED** (she holds the house — a title,
not a chore). School: "Rank ten. The school's measure says ten." Two crossed in spring,
four more since — **seventh.** Lin Ximeng's flat stipend speech (a thousand a month, fused
ring = official). Lan's drawer: the thousand, the eight empty seats. Supper: kettle days;
the jar 64 → 66. The beach: ten minutes, gravel and shells, moon like a plate of rice,
"You've grown — nearly to my nose," 🔴 **the question re-voiced ("would you come looking")
and the promise re-voiced ("I'm going to look after you your whole life")**; she keeps it
where the doll's name lives; she does not count the way home. Close: the chapter's law.

**Defect of record — THE READABILITY RULING.** First draft passed all nine layers. The
author read it and ruled it unreadable anyway: **14.7 similes/1k** (ch01: 5.0), 29
`which`, six double-simile sentences, a 59-word stacking sentence. The author named the
target register: his own Fire Phoenix serial (avg 9.0-word sentences, ~5 similes/1k,
short paragraphs, dialogue-led). **Measure what's measured: the gates had floors and no
ceilings, and the drift grew unobserved for four chapters.** The chapter was rewritten
whole in the Fire Phoenix register — same doors, new walls — and STYLE_LAW gained §0.7,
the readability ceiling (sentence average ≤11 · similes ≤6/1k · "the way" ≤6 · say it
once · short paragraphs · dialogue carries). Floors + ceilings = the band. Pre-battery
fixes on the first draft (kept in the rewrite): watch-term "stairs" ×3 removed, invented
name "Hale's" removed, a forbidden "for three years" of Na'er's interior removed, a face
leak (Lan's mother knowing the Tang pickle-jar) removed.

**Shipped:** 3,871 words style_gate / 3,866 verify · fifteen chapters · **72,648 prose
words (verify) / 72,544 (style_gate)** · dlg 14.4%, 62 turns · spectator law satisfied
(Lan Shen five spoken turns: breakfast mother → Bao at the rail → "Count on it" → supper
mother) · 9 layers ALL GREEN.

**Carry to ch16:** canon 016 §2+ (the buy morning — Na'er holds the house) + canon 017
(the test: 38; the kind Spirit Master and the waived fee — ch14's posted clerk was NOT
that man) · canon 022/024 receipts already on disk · **first draft ch16 UNDER §0.7
ceilings — do not draft purple and prune after** · the spent-check instrument still
unbuilt · the ceiling greps to build into a tool.

**CORRECTION ROW (same day) — the deeper pass.** Authorly: "check deeper." Found: "the way"
had survived the rewrite at 9 (Fire Phoenix's real density: 0.0–0.6/1k), and §0.7's own
ceilings were two notches too soft versus the corpus they claim to calibrate against.
Eleven further kills; similes 7.5 → 3.7/1k; surviving "the way" 6 total (3 literal).
Shipped totals after the pass: 3,800 style / 3,795 verify; serial 72,577 / 72,473. The
correction and the lesson stand together: calibrate against the target corpus, not
against my own first reading of it.
