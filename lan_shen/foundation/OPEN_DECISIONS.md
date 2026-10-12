# OPEN_DECISIONS.md — what is still waiting on the author

Everything here is a **ruling only the author can make**. Nothing in this file blocks
drafting chapter one except item 1. Everything else blocks something later.

The kit's precedent: `seed_of_creation` shipped 18 foundation files and **zero chapters**,
blocked on four rulings, rather than guessing. Guessing is what cost `blue_silver` a
90,000-word rebuild.

---

## ✅ SETTLED 2026-09-19 — no longer blocking

### 1. Glorybound City or Eastsea? — **RULED BY CANON: Glorybound City**

Canon ch1, fetched and held on disk (`canon_extract/chapters/canon_001_excerpt.txt`), opens
the entire novel with:

> *"Glorybound City was a small town sitting on the border between the ocean and the eastern
> coast of the Sun Moon Federation."*

Red Mountain Academy is in it; the awakening ceremony happens there; Wulin walks home to it.
This is the novel's first line, not an inference. **Option A adopted. Chapter one is written
to it.** The existing `Soul_Land_3_Project` keeps its Eastsea AU as an independent serial.

<details><summary>the original open question, retained for provenance</summary>

### 1. Glorybound City or Eastsea?

Canon ch4, fetched and receipted (`CANON_NOTES.md` R2), puts Wulin's childhood in
**Glorybound City** at **Red Mountain Academy**, with Tang Ziran and Lang Yue as parents.

The existing `Soul_Land_3_Project` (Lin Hao) sets its early era in **Eastsea**.

These cannot both be canon for the same city. Three options, with costs:

| Option | Cost |
|---|---|
| **A. Use canon: Glorybound City** *(recommended, and what the foundation currently assumes)* | The two SL3 projects visibly disagree. Fine if they are declared independent AUs — which `README.md` already does. |
| **B. Use Eastsea** | Contradicts a receipted primary source. Would need the receipt annotated as "translation variance, ruling overrides" — and the variance is not actually plausible here, since Glorybound and Eastsea are different places, not different spellings. |
| **C. Both — he is from Glorybound and later moves to Eastsea** | Canon may support a move; not held on disk. Would need canon ch1–22 fetched to check. Slower, possibly richer. |

**Ruling needed:** A, B, or C.

</details>

---

## 🟠 BLOCKS BOOK ONE, NOT CHAPTER ONE

### 2. How much of *you* goes into the past life?

You ruled that the OC's previous life was **yourself**. That is a real choice with a real
consequence, and I did not act on it fully — deliberately.

**What I did:** the past life is written as *a young man in a world where Soul Land was a
story*. No name, no city, no family, no personal detail.

**Why:** these repositories are **public**. Anything autobiographical you put in them is
permanent, searchable, and harvestable — and you have already had one privacy leak this week
(a live personal email address sitting in public git history; see `fix/scrub_email.sh` in the
workspace root, outside this repo). Personal detail in a public fanfic is the same class of
exposure, and this file must not itself become the second leak.

**What you can rule:**
- **(a)** Keep it anonymous. *Recommended.* The character works either way.
- **(b)** Add texture without identity — a country, a job, an age, a reason he stopped
  reading at SL4. Safe, and it sharpens the voice considerably.
- **(c)** Full self-insert with real detail. Your call, your life — but say it explicitly and
  I will write it, and I would still recommend against a real name.

Also worth ruling: **why did he stop at half of SL4?** That gap is free story. A reason
(death, boredom, no time, the translation stalled) becomes a character wound.

### 3. ~~Does the knife boy get redeemed, or does he stay small?~~ ✅ RULED, ch2 (2026-09-19)

Canon gives him one scene and no name (`CANON_NOTES.md` R2). This project names him and
gives him a life.

**RULING: he is named Niu Bao, and he takes (b) now with (c) reserved.**

Ch2 stages him as (b) — he stays small. Chubby, rank five, a short knife, a father who has
already told him what he is for, and a thumb that counts against his trouser seam. He says
his canon boast and gets answered by a rank-one child, and the answer is the only thing in
the room that has ever not gone his way. He is not a villain. He is a boy with a number who
has just met a boy with a worse number who does not care.

**(c) is reserved, not rejected.** Niu Bao is rank five at Red Mountain Academy, which is a
good number in Glorybound City and nothing at all in the wider world. The register will
eventually hurt him too — and the scene where he finds that out is worth more than any
redemption arc spent early. **Do not soften him before Book Two.** Do not give him a
backstory chapter. He earns his turn by costing Lan Shen something first.

- ~~(a) Redeemed slowly~~ — rejected. Too expensive in page time for a rank-five child.
- **(b) Stays small** — ✅ **active, ch2 onward.**
- **(c) Ally against Yan Song** — 🔴 reserved. The register hurts everyone with a low number.

### 4. Su Wan — how sharp is the mother?

She is currently written as **the most dangerous person in Book One**, because she notices
things and because lying to someone kind is harder than lying to an enemy.

- **(a)** Keep her sharp. She never proves anything. She just never quite stops wondering.
  *Recommended — this is the best sustained tension available in a childhood arc.*
- **(b)** Soften her. Warmer book, weaker firewall.
- **(c)** She finds out. 🔴 Requires a Lock 6 ruling and would detonate Book One.

### 5. The first ring

Canon ch20 is titled *"Fusion"*. Lan Shen's ring selection is where his meta-knowledge
actually pays — but his grass is ordinary and his soul power is rank 1, so his first ring
hunt is a genuine problem: **he may not be strong enough to kill what he knows he needs.**

- **(a)** He gets the ring he planned, and it costs more than he expected.
- **(b)** He cannot get the ring he planned and has to improvise a worse one *better* — the
  most on-thesis option, and the hardest to write.
- **(c)** Someone gets it for him, and now he owes them. Feeds the near spine.

---

## 🟡 DOES NOT BLOCK ANYTHING, DECIDE WHENEVER

### 6. Chinese characters for the names
Currently proposed: **Lan Shen, Lan He, Su Wan, Yan Song, Qin Wu** — the characters for
each are recorded in `codex/CHARACTERS.md`, which is the only place Lock 10 permits them.
Confirm or replace. Meanings, and why each name was chosen, are in that file.

### 7. Serial title
Working title: **Lan Shen**. Alternatives the premise supports:
*Rank One* · *The Waste Slot* · *The Deep Blue* · *What The Register Missed* ·
*The Boy Who Read Ahead*.

### 8. Cadence — ⚠️ RULED, no longer open
🔴 **Corrected 2026-09-20 by layer 9 (`tools/banned_token_check.py`).** This entry said
"currently locked at 2,200–3,500 words per chapter (blue_silver's passing band) with an audit
every ten." Both halves were superseded and this document had not been told:

- **The band is 2,600–5,500 prose words**, the measured house band. Lock 11 records that the
  2,200–3,500 figure came from the *plant-POV* serial, which is the wrong model for a human
  protagonist in a city. SL3's own lifetime average is 3,078 across 92 chapters.
- **The audit runs at every chapter edge**, not every ten: `sh checks/run_all.sh`, nine layers,
  exit 0 required before a chapter is called shipped.

Cadence is therefore not an open decision. It is settled in `NO_MISTAKE_LIVE_RULES.md` Lock 11,
which wins over this file. Kept here as a receipt rather than deleted, so the next agent can see
that a current-state document once contradicted a lock.

---

## ALREADY RULED (do not re-ask)

| Question | Ruling | Source |
|---|---|---|
| Reincarnator? | Yes | author, 2026-09-19 |
| Adaptation talent? | **No** — explicit divergence from Lin Hao | author, 2026-09-19 |
| Meta-knowledge scope | SL1, 2, 2.5, 3 (mostly), 3.5, 5, ~half of 4, "all the important things" | author, 2026-09-19 |
| Spiritual power | Good, because reborn | author, 2026-09-19 |
| Age and place | Same age and place as Tang Wulin | author, 2026-09-19 |
| Martial soul | Normal Bluesilver Grass | author, 2026-09-19 |
| Innate soul power | **1** | author, 2026-09-19 |
| Body training | Six years before awakening | author, 2026-09-19 |
| Relationship to Wulin | Brother / close friend — but a real child in a real new body | author, 2026-09-19 |
| How they become brothers | **Neighbour families** — the brotherhood starts with the parents | author, 2026-09-19 |
| OC name | **Lan Shen** | author, 2026-09-19 |
| Spine | Delegated to the agent: *"I don't understand… continue naturally"* | author, 2026-09-19 |
| Power ceiling | Delegated to the agent | author, 2026-09-19 |

---

## 🟡 RECORDED AGAINST THE KIT, NOT HIDDEN

**This foundation is 11,500 words. The kit's guidance is ~2,000.**

`SOUL_LAND_UNIVERSAL_KIT/02_PROJECT_SETUP.md` says: *"A finished setup is maybe 2,000 words
across four files. It should take an afternoon. The failure mode is the opposite: 25,000
words of world bible before chapter one exists."*

This is 5.8x over the guidance and twelve files instead of four. `seed_of_creation` shipped
30,809 words of setup against the same guidance and recorded it honestly with a defence; this
is the same situation and gets the same treatment rather than being quietly ignored.

**The defence:** the receipt-heavy files (`CANON_NOTES.md`, `CANON_LEDGER.md`) are quotation,
not invention — they are the NO-CANON LAW's paperwork, and they shrink once canon ch1-22 is
held on disk and the quotes stop needing to be re-recorded. `KNOWLEDGE_FIREWALLS.md` is long
because a meta-knowledge protagonist has five firewalls where an ordinary OC has none; that
complexity is in the premise, not in the prose about it.

**The concession:** `PLACES.md`, `TIMELINE.md` and `CHARACTERS.md` carry padding — tables of
"NOT HELD" items that exist to prevent invention, and could be one line each instead of a
section. They are cheap to cut and should be, at the first audit.

**The commitment:** no further foundation files are created until chapter three is written.
The apparatus is frozen. If a new file seems necessary before then, that is a symptom of
avoiding the drafting, and it gets written in `audits/` instead.
---

## 🟠 NEW, FROM THE 2026-09-19 CHARACTER RULING

### 9. Which door does the grass take?

`THE_PLAN.md` Track 4 establishes that **royal bloodline is canonically closed** (A Yin's
descendants only — Tang San and Tang Wulin). Three legal doors remain:

- **A** Second awakening, non-royal (Tang Ya's precedent) — requires innate soul power, which
  is the one thing Lan Shen does not have
- **B** The hundred-thousand-year route — a grass that cultivated past the mark. Matches your
  "age doesn't matter to him."
- **C** Partial mutation (Silver-marked precedent) — a *marked* grass, not an emperor. Matches
  your "mutation, even a little bit."

**Currently written as:** he plans for C, dreams of B, and does not yet know A is closed.
Overrule freely.

### 10. How much does he know about the Spirit Pagoda?

Canon makes the Pagoda the organisation that **runs the awakening ceremony, conducts the
spiritual power tests, and controls every soul spirit on the continent** — and it has a
genocide in its history. Lan Shen knows all of this at age six, and he is standing in its
classroom. Ruling needed: does he **fear** it, **use** it, or **plan to burn it**? Each makes
a different book.

### 11. Girls his own age

You ruled he was uncomfortable with girls his age and a virgin in the last life. Canon puts
**Gu Yue** next to him for nine school years, and he knows what she becomes. Currently written
as a **blocked axis that is the point rather than a problem to solve** — he will be unable to
act normally around her and it will read as awe. Confirm, or rule differently.

### 12. Does the playfulness land in chapter two?

Chapter one is watchful and controlled, which suits a boy alone in a crowd on verdict day. But
you ruled him **playful with boys**, and that register is not in the chapter yet. Chapter two
should introduce at least one boy his own age and let him be quick, teasing and warm — or the
character will set as a brooder. Confirm you want that early.

### 13. ~~The comprehension price is unplanted~~ ✅ **STAGED, ch3 — CLOSED**

`THE_PLAN.md` Track 1 claimed that hard use of spiritual power costs him something physical.
Chapter one did not stage it. Chapter two did not stage it either, correctly — it is a chapter
about a classroom and a canteen, and a nosebleed in it would have been the apparatus showing
through.

**Chapter three staged it.** The first instance is on page, with a mechanism, a number, a
witness and a consequence:

```
TRIGGER      he reaches for his brother's martial soul through a wall, on purpose, to read
             the gold at the root from the inside
DURATION     about eleven seconds of "reach" before it breaks him
COST         a sound like a door closing in another room · a white line across the inside of
             his eyes · a nosebleed onto his shirt · a fall (he got his shoulder down before
             his head, which was training) · copper in the mouth
AFTERCOST    🔴 total loss of the sense. He tried twice more on the floor. Nothing. No ditch,
             no crack in the paving, no lamp. The door shut.
RECOVERY     unmeasured. He tells himself a week, and then, honestly, "see if the eleven
             seconds gets longer."
WITNESS      🔴 Su Wan. Not Wulin.
```

**Why not Wulin.** The working preference logged earlier was "Wulin sees it," so that the
brotherhood would have a debt in both directions. **Rejected on drafting, and the rejection is
the better ruling:** the entire engine of chapter three is *asymmetry*. Lan Shen can feel his
brother and his brother cannot feel him. If Wulin witnesses the cost, the asymmetry becomes a
shared secret, and a shared secret is a conversation — and this serial needs the conversation
to not happen for a long time.

So the cost is paid alone, on a floor, at night, and cleaned up. And then **Su Wan walks in.**
She looks at the rag, at the three drops, at the smear. She does not ask what it is. She wipes
his face, takes the evidence out of the room, and says:

> *"Don't do whatever this is at night, when I'm asleep. Do it in the day, where I can see it."*

🔴 **That is the ruling, and it is worse than either option listed above.** She has not
accused him. She has not forgiven him. She has **asked to be present**, and she has done it in
a form he can accept without explaining anything — which means that the day he does it in the
daylight, in front of his mother, is the day the firewall comes down, and she has just
scheduled it.

**Standing rule from here on:** the price is never free, never offstage, and never paid twice
in the same chapter. Every hard use gets a duration, a cost, an aftercost, and a witness or a
deliberate absence of one.

### 14. The book is on an open shelf. When does someone read it?  🔴 NEW, ch2 · 🔴🔴 **ESCALATED ch5 — SEE #23**

Chapter two ends with Lan Shen writing the truth about the gold at the root into the book
Su Wan already knows about and has already permitted — and leaving it on an open shelf, in a
room she walks through, in a house with a neighbour boy who visits.

This was chosen over a hidden book because a hidden book is a spy thriller and an open book
is a family. But it is now a loaded gun with no scheduled discharge.

- **(a)** Su Wan reads it. She already knows he goes away. Reading *"gold at the root, day
  one, told nobody"* would hand her a fact she cannot act on and cannot un-know. 🔴 The
  sharpest scene available in Book One.
- **(b)** Wulin reads it. He is the subject of the sentence. He has been told "No."
- **(c)** Nobody reads it for eighty chapters, and it is a slow fuse that pays in Book Two.
- **(d)** He moves it after ch3, having thought about it, and the moving is the beat.

**Recommended: (d) then (a).** He leaves it out for a week because leaving it out is a kind
of hope, then he hides it because hope is not a plan — and Su Wan notices the hiding, which
is worse than the book. Needs a ruling before ch4.

**UPDATE, ch3 — the shelf has been weaponised by canon's own logic.** Su Wan found the blood,
looked at the shelf he blamed, and saw a book square to the edge on the second row. She said
nothing. **The book and the lie are now in the same sentence in her head.** Ch3 also added
Na'er's entry to it — silver hair, amethyst, mist behind the pupil — which means the shelf now
holds the gold at the root *and* the one thing Lan Shen has sworn Wulin will never learn.
**Ruling still needed before ch5, and the pressure has gone up.**

---

### 15. 🔴🔴 THE GRASS SENSE — what it is, what it costs, and what it may never do  · NEW, ch3 · 🔴🔴 **COST RULE REFINED ch6 — SEE BELOW**

Chapter three gave Lan Shen a capability **that is not in the book he read**: at rank one, in
meditation, he felt every strand of Bluesilver Grass in the street as a single organism, and
felt his brother's martial soul through a wall.

Canon 006/007 supplies the seed (*"he could sense some of the world's Bluesilver Grass"*;
*"sense the tiny existences in the air, as they were quietly absorbed into his body"*), and the
author's ruling supplies the reason it works better for him than for Wulin — **high spiritual
power**. But canon gives that sense to Wulin, diffusely, on his first night. It does not give
anybody a *reading*. This is ours, and it needs hard walls.

**RULED — the capability:**

```
NAME          the grass sense (never named on page; he has no word for it yet)
RANGE         one street. Not a city. Not a continent.
WHAT IT IS    every strand of Bluesilver Grass in range, felt as ONE organism, plus any
              other martial soul of the same or a compatible type that is "lit" — i.e.
              currently meditating or actively using its soul
RESOLUTION    🔴 LOW. He felt "a thing under the light — deep, folded, layered, like looking
              down a well and seeing that the well has floors." He did NOT read a number, a
              rank, a colour, or the gold. He got shape, not content.
DIRECTION     🔴 ASYMMETRIC, and this is load-bearing. He feels Wulin. Wulin does not feel
              him. Reason, in-world: Wulin's first-night awareness is diffuse and he has no
              framework to sort one loud strand out of the street's noise. Lan Shen has four
              years of practice and high spiritual power, and is aiming.
COST          🔴🔴 **REFINED, ch6 — THE COST IS *WIDTH*, NOT TIME.**
              #13's rule (eleven seconds → nosebleed, migraine, white line, one week of total
              loss) was measured on a STREET and is not a general law.
                STREET, day 11  ten seconds, twice, let go on purpose → **NOTHING. No cost.**
                GARDEN, day 14  four seconds to find it, twenty held → white line, collapse of
                                the field from forty thousand to one, nosebleed, **total loss,
                                estimated one month**
              🔴 *"The cost was not the length of time and never had been. The cost was the
              width."* Ch3's eleven-seconds-for-a-week is retroactively explained: he was
              calibrating against the sparsest ground available to him — grass growing in
              cracks under a paved city.
PROGRESSION   🔴 SLOW AND MEASURED. The plan is that the eleven seconds gets longer with
              repetition, not with plot convenience. Any chapter that lets him reach further,
              hold longer, or read more clearly than the last one must SAY what he paid.
```

**RULED — what it may NEVER do:**

- ❌ **It may never read the gold at the root.** He reached for exactly that in ch3 and got a
  shape and a nosebleed. The gold stays a *visual* fact, found by a reading glass and four
  years of patience. If the grass sense could read it, the entire six-track plan collapses
  into one nightly meditation.
- ❌ **It may never detect a soul beast, a spirit soul, a seal, or a soul ring.** Wrong
  instrument. It senses *plant-type martial soul in range*, nothing else.
- ❌ **It may never reach Na'er.** 🔴 She is not a grass child, whatever she is. Firewall 4.
  If the sense ever returns something on her, that is a Book Two reveal and it must be paid
  for enormously.
- ❌ **Wulin may never feel it** before his own spiritual power canonically explodes — and
  when he does, it must arrive as canon's doing (the golden colossus, the seals), not ours.
- ❌ **It may never be demonstrated in front of anybody.** #13's ruling stands: the cost is
  paid alone until Su Wan is deliberately invited in.
  🔴🔴 **PARTIALLY BREACHED, ch6, by accident — and the distinction held.** Wulin and Na'er
  arrived while Lan Shen was mid-sense. **What they saw was a white boy on a bench with a bloody
  nose. The COST was seen; the CAPABILITY was not.** Wulin has told his mother. *"The cost is
  paid alone"* is now on a clock.

**The one thing this buys him, and it is enough:** he now knows, in his own body rather than
from a page, that *rank is pressure and not reach* — and that the worst martial soul on the
continent is the most abundant plant on the planet and is all one thing. That is a strategic
insight no rank-one child in canon ever gets, and it is the foundation of Track 4.

---

### 16. 🔴 The spirit soul door — can a rank-one grass child be "fast"?  · NEW, ch3

Canon 008 hands over the entire financial spine of Book One in Tang Ziran's voice:

> *"The first is to be a genius Soul Master with an exceedingly fast cultivation speed. Those
> geniuses will be granted their first spirit soul free of charge. However, it's clear that
> your Bluesilver Grass won't qualify for that opportunity. Therefore, we are left only with
> the second method of purchasing one."*

Canon slams that door on Wulin. **It slams harder on Lan Shen**, who is rank one and whose
father runs a herb shop. But the criterion canon names is **speed**, not starting rank — and
chapter three has just established that his grass drinks continuously, that the whole street
is one organism, and that his spiritual power is high.

Two available roads, and they are not mutually exclusive:

- **(a) He cannot be fast.** Then he needs money, and the medicinal-supply arrangement is his
  only income, and the road to a spirit soul runs through Yan Song and the academy — the
  **near spine**. Grittier, slower, more human.
- **(b) 🔴 He can be fast, and the Spirit Pagoda notices.** The genius door is administered by
  the same organisation that keeps his file at rank one. Walking through it means walking into
  the **far spine** on purpose, with his own name on the paperwork.

**Recommended: (a) first, then (b).** Spend Book One's first arc on (a) — money, jars, a
valuation, a register-keeper who is not yet a wall. Let (b) arrive as the *consequence* of (a)
succeeding, so that the far spine is entered because he was too good at being poor, not
because the plot needed him. **Ruling needed before the rank-ten arc (canon 015-era).**

---

## 🟠 NEW, FROM CHAPTER FOUR AND THE CANON 012-015 FETCH (2026-09-20)

### 17. 🔴 THE THIRD DOOR — machine / interchangeability  · staged ch4

**Full reasoning lives in `THE_PLAN.md` TRACK 7 and `CANON_NOTES.md` R8 + R9 Finding 3.**
Summary: canon 010 says every first-rate component is hand-forged because *"a machine will
never be able to grasp the veins of the metal."* Canon 013 then shows a nine-year-old spending
two hours hand-forging ten spherical ankle-joints when *"if the work was done with a mold, it
would only have to be pressed twice."* In a workshop with **three people in it.**

> 🔴🔴 **Nothing on this continent is interchangeable.** Every fitted pair in every soul machine
> was made for each other, by hand, one at a time. A broken part cannot be replaced — only
> re-made and re-fitted by somebody as good as the man who made the first one.

The fix is not better forging (canon forbids it). It is **jigs, gauges, tolerances** — three
ideas needing no soul power, no rank, no martial soul.

Rulings needed:

- **(a) When does he act on it?** 🔴 Track 7 starts as **standardising his father's balm** —
  recipe, measure, wax seal — because he is six, toolless, penniless, and just refused.
  Reserved for Book Two at the earliest: soul machines, mecha, spirit refining, anything
  touching the Spirit Pagoda's industrial arm.
- **(b) 🔴 Does he ever say the idea out loud?** Not at six. A child explaining
  interchangeability is a child explaining he has been somewhere else (Firewall 0). The first
  plausible listener is 🔴 **Tang Ziran — canon's machine repairman**, whose *"skill in
  repairing machines was quite ordinary"* and who has spent his life fitting parts that do not
  fit. **He is also the man investigating his son with a soul-machine lamp.** That collision is
  the best scene available and must not be spent early.
- **(c) 🔴 Does he get back into that hall?** *"There's nothing here for you."* / *"Don't come
  back with a box."* Canon owns the forge and Wulin owns the apprenticeship — **neither may be
  taken from him. Lan Shen may never be Mang Tian's apprentice.** The door back in is commerce,
  not craft: a balm that keeps on a smith's hands in winter, on schedule, priced right. Mang
  Tian already knows Lan He's name and already thinks the ratio is wrong. **A correction is an
  invitation to come back with a better batch.** Do not reopen inside ten chapters.
- **(d) The cost.** Standardising anything requires somebody else to agree to the standard.
  🔴 **The one track that is purely his own cannot be done alone** — the exact opposite of
  everything else in his plan.
- **(e) 🔴 The book is now self-censored.** He wrote the numbers and withheld the idea. The shelf
  has gone from *hidden* to *edited*, and editing is the more dangerous habit: he has started
  deciding what a future reader is allowed to know. **#14's next escalation should cost him.**

### 18. 🔴🔴 THE SPIRITUAL POWER PARADOX — how does he ever get seen?  · R9, canon 012 · ✅ **RESOLVED BY CANON 017, R11 — SEE BELOW**

> ✅ **RESOLVED, 2026-09-20.** Canon 017 is held in full and answers all three questions.
> **The instrument:** a metal helmet with linked arms that strap the head in, a hum, a soft
> white glow, and a **soul transmitter screen**. It measures **degree within Spirit Origin**
> (realm 1 of 6: Spirit Origin → Spirit Connection → Spirit Sea → Spirit Abyss → Spirit Domain →
> Divine Origin). **The cost:** it normally charges a fee — waived for Wulin because the clerk
> liked him. **The catch:** 🔴🔴 *"the Spirit Pagoda will make a record of your spiritual power's
> strength"* and *"Ordinary people can't look into the world of Soul Masters"* — the father waits
> outside.
>
> 🔴🔴 **THE CENTRAL DILEMMA: the only instrument in this world that can see Lan Shen is the
> instrument that FILES him.** He must reach rank 10 to be taken there at all, because the test
> is administered at the point of buying a spirit soul. **To be seen, he must first buy —
> 30,000 Federation Coins.** Track 8 makes the money, the money buys the test, the test reveals
> Track 1, and the file it creates is Track 7's enemy. **That is the spine of Book One.**
>
> 🔴🔴 **CORRECTED TWICE — canon 016 then canon 018. See `CANON_NOTES.md` R12 and R13.**
>
> (i) R11 said *"canon never gives Wulin's number."* **FALSE.** Canon 018 opens with it:
> **WULIN = 38.** The clerk = 87, a 28th rank Soul Grandmaster, and he says *"only."*
> 🔴 **SOUL RANK AND SPIRITUAL POWER ARE DECOUPLED.** Spirit Origin is 1-50 total; ≤15
> elementary, 15-30 intermediate, 30-45 advanced, 45-50 peak.
>
> (ii) **The record is PORTABLE.** *"I'm going to have the machine make a record for you, so you
> can hand it over once you attend an intermediate Soul Master academy."* 🔴🔴 **He carries it.
> He can see it, keep it, lose it, alter it — and he is required to present it.**
>
> (iii) 🔴🔴 **THE ANSWER TO #18 — RULED, R13.** Canon 018's first line says the numbers
> *"settled within a range."* Canon names settling as normal. **So: LAN SHEN'S READING DOES NOT
> SETTLE.** The clerk's astonishment is about the *behaviour of the instrument*, not the size of
> the value. It obeys "different kind, not bigger number," it is safe inside a 1-50 ceiling, it
> is Track 7's perfect enemy, and 🔴 **it is #15's grass sense in official form — shape not
> content, range not number.** It also creates a better file problem: **what does the Pagoda
> write down when the machine will not settle?** RESERVED, not spent — he is six, canon puts the
> test at nine.

Canon 012, on how Wulin's secret was found:
> *"Later, she discovered the cause of Tang Wulin's fast cultivation speed. **This child's
> spiritual power was far higher than his peers**, enabling him to cultivate with more focus
> and thus, speed."*

🔴 **High spiritual power is detected in canon by exactly one measurement: rank velocity.**
Lan Shen has more of it than Wulin and he is rank 1, staying rank 1.

> **His one permanent, unassailable advantage is invisible in precisely the test that reveals
> it** — and a rank-three boy climbing normally will look *better* to every teacher on the
> continent.

This is not a problem to solve. **It is the engine of Book One.** Three rulings:

- **(a) Does he ever get measured?** Canon supplies the instrument: **chapter 17 is titled
  "Spiritual Power Test."** 🔴 **NOT YET FETCHED — now the top of the queue.** Canon 015
  confirms a *soul power* test apparatus already exists at the academy and runs on request.
  Two machines, two measurements: **rank is public and free; spiritual power is neither.**
  Until ch17 is held, stage no measurement of Lan Shen.
- **(b) 🔴 Does he WANT to be measured?** No — for four chapters at least. A man who has spent
  four years being invisible does not volunteer for a machine that could make him visible.
  **He should be dragged to it, not walk to it.**
- **(c) Who sees the number?** In ascending danger: **Lin Ximeng** (safe; delighted; useless) →
  🔴 **Qin Wu** (already holding a margin note about a second sheet that was never filed, ch1 —
  **the correct first reader**) → **the Spirit Pagoda** (far spine, not Book One).

> 🔴🔴 **AND THE CONVERGENCE, WHICH IS THE SPINE OF THE WHOLE PROJECT:** a spiritual power test
> is a soul machine. **Track 1 (the advantage nobody can see) and Track 7 (the only trade he
> understands better than anyone alive) meet at the same object.** The instrument that can
> finally measure him is the instrument he is uniquely qualified to build, calibrate, distrust
> and improve.

### 19. 🔴🔴 THE GARDEN — wild Bluesilver Grass, two doors down  · R9 + R10, canon 014-015 · ✅ **STAGED, ch6 — SEE `codex/PLACES.md`**

Canon 014: *"There was a small garden in the commoners' area that Tang Wulin lived in… As soon
as he entered the garden, he felt **a powerful attraction force from a strand of Bluesilver
Grass.**"*

🔴🔴 **Canon 015: WULIN BROKE THROUGH TO RANK 10 IN THAT GARDEN.**
> *"I was meditating in the garden. I think I've broken through to the 10th rank."*

And from inside the breakthrough: blue specks of light congregating from all around him, the
fragrance of Bluesilver Grass in every cell, everything turning *"a bizarre blue color"* — and

> 🔴🔴 *"**Faint golden lines lit up on his forehead with the same pattern as before**, extending
> outwards. After extending all over his skin, the golden lines gradually withdrew."*

**"The same pattern as before" is canon 011's golden veins** — the ones Tang Ziran watched
*FADING* under his shoulder lamp and decided to investigate. **They did not fade. They went
into him.** Canon 015 shows them coming back out through his skin.

Lan Shen discovered in ch3 that he can feel grass through a wall, and in ch4 that the sense
costs eleven seconds of blindness and a nosebleed. **The garden is in his street.**

| Ruling | Answer |
|---|---|
| 🔴 **Binding constraint** | **The garden may HELP him. It must not FIX him.** Canon gave Wulin a breakthrough there because Wulin was already at the bottleneck with rank 3 innate and three years of forging. Lan Shen is rank 1 with nothing. **What the garden gives him is control of the sense — not a rank.** |
| When does he find it? | Not before ch6. He has left the commoner's district only once, walking east to the workshop |
| What does it cost? | Something that cannot be hidden from his mother. **Su Wan already knows he bleeds at night and has told him to do it by day** |
| 🔴 Does Wulin know it is special? | Canon says Wulin feels the pull too. **Two boys who both feel a plant calling, in the same garden, is where the brotherhood stops being a wall.** Do not spend early |
| 🔴 Royal blood? | **NO.** Canon restricts Bluesilver Emperor descent to A Yin's line and Track 4 door A is closed. **The garden must not be a shortcut.** It can be a teacher, never a source |

### 20. 🔴🔴 NA'ER IS LEAVING, AND THE SERIAL ALREADY KNOWS IT  · R10, canon 015

> 🔴 **SEEDED, ch7 — one look, nothing more.** *"Na'er was standing very still in the middle of
> the grass, not doing anything, with her hands at her sides. Lan Shen looked at her for a
> second. Then he looked away, because there was a thing about her standing like that which he
> had noticed before and had decided was nothing."* Canon 016 was fetched the same day and gave
> three unexplained Na'er data points. ❌ **Do not develop this before Year 1's Awakening Day.**

Canon 015's last line, with nothing after it:
> *"Would you miss me if I left one day, big brother?"*

**Canon 024 is titled "Na'er Leaves."** Canon planted it nine chapters early, on a gravel beach,
at night — and her brother did not hear it, because he had just made rank 10 and guessed she was
sad about not having a martial soul.

Supporting tells, all canon 015:
- 🔴 **Her eyes are purple now.** *"clear purple eyes which now displayed a fantastic splendor."*
  Changed overnight, the morning after the seven-coloured ring fused into her brow. Wulin does
  not notice.
- 🔴 **She is not eating breakfast.** Canon built her entire characterisation on food — she
  smiled for the first time when offered a meal (canon 010), she eats four to six times a normal
  child. **A Na'er with a blank stare at breakfast is a Na'er who is somewhere else.**
- She asks to go to the beach at night, looks out at the ocean, then up at the stars.

**(a) 🔴 Does Lan Shen see any of it?** Not the beach — Firewall 4, canon has only the two of
them there. But:
- **He can see her eyes.** They share a street, and Lan Shen has memorised every table in this
  world including the ring-colour one. **Purple is not a colour a five-year-old's eyes are.**
- **He can see her not eating.** Su Wan feeds that household; the ginger arrangement is standing.
  A child who stops eating is the loudest signal in a poor family.
- 🔴 **And he is the only person in Glorybound City whose entire skill set is noticing what other
  people walk past.**

**(b) 🔴 What does he DO with it?**
Nothing. That is the point. He is seven, then eight, then nine, watching a girl get quiet, and
he cannot ask her — because asking means admitting he has been watching, and being watched is
the one thing he has spent four years making sure never happens.

> 🔴 **RULING: Lan Shen notices Na'er's departure before anyone, tells no one, does nothing, and
> is still thinking about it eleven years later.** This is the emotional counterweight to Track 7
> — the appetite that made him look up — and the first thing in the serial he fails at purely
> because of who he is.

**(c) Does the serial stage canon 024?** Yes, it is canon. 🔴 **But from the wrong side of a
wall, or from a street, or from a harbour road — never from inside the event.** Lan Shen's whole
life is arriving after. Ch3 already established the pattern: canon has Wulin alone in the
awakening chamber, so Lan Shen sees only the aftermath.
**🔴 Make that the law of the serial, not an accident.**

---

### 21. 🔴🔴 TRACK 8 — THE AUTHOR.  · ✅ **FIRST FLICKER STAGED, ch5 — the horse sentence** What he writes, who signs it, and when it costs him  · author ruling 2026-09-20

**Full reasoning in `THE_PLAN.md` TRACK 8. The ruling that created it, in the author's words:**
> *"What Lan Shen is in last life — a author. He read and see too many types fictions and drama
> and novels and many things, he can write and create his own and can sell them. I think for
> Soul Land world they are very unique and good so of course he can."*

**Accepted in full, and it is load-bearing.** Canon's era is semi-industrial (soul machines with
buttons and screens, mass coinage, compulsory schooling, continental institutions) so books,
broadsheets and commercial storytelling exist. 🔴 **What does not exist is a century of
commercial serial fiction refining *how to make a reader unable to stop*.** That is his product.
Form, not content.

Already ruled, not re-openable:
- 🔴 **Track 8 is the only track with no capital requirement.** Paper and a pen, both owned. It
  is therefore the only realistic route to **30,000 Federation Coins** before he is old enough to
  earn with a hammer. Track 5 feeds the family; Track 7 is the life's work; **Track 8 buys the
  spirit soul.**
- 🔴 **The front is Lan He.** Three tracks now converge on the father — the shop, the balm, the
  pen name. **The plan he made to survive alone has routed itself through one other person.**
- 🔴🔴 **The first audience is Na'er.** Not a publisher. A little girl two doors down who has
  stopped eating breakfast. Track 8 begins as the only thing he can do about #20 that is not
  asking her what is wrong.
- 🔴 **The governing rule: he may write anything except the truth.** Every story he sells must be
  inventable by someone who has never left this continent.

Still open:

**(a) 🔴 What is the FIRST thing he actually writes?** Ruled: not a novel. He is six with no
distribution. The realistic first product is **an oral serial** — a story told out loud to Na'er,
then to the street's children, then written down by somebody else, then copied, then traded.
🔴 **He does not write it. He tells it, and it escapes.** That is the correct mechanism and it
must stay that way: the first thing of his that reaches the world does so without his name on it
and without his permission.

**(b) 🔴 When does Lan He find out, and how badly does it go?** Needs a chapter. Constraints: Lan
He has already said *"That's a good answer, and I don't like that you had it"* twice and is
counting. He must be told the writing is his son's and **must not** be told where the ideas come
from. 🔴 **Recommended: Year 2, and it goes better than Lan Shen expects, which frightens him
more than anger would** — because his father is *proud*, and pride is a form of being seen.

**(c) 🔴 The visibility collision.** Track 8's success makes people look for the author.
Firewall 0 says being looked for is fatal. **When does he first get careless?** Recommend: never
by choice. 🔴 **Somebody else should get close — a reader, a bookseller, a schoolteacher who
notices the voice — and he should have to decide whether to let them.**

**(d) 🔴🔴 THE FORBIDDEN MASTERPIECE. Does he ever write the true story?**
He knows, professionally, that the story he is living would be magnificent. He can never sell a
word of it. **So he will spend years inventing lesser work for money while the best thing he
will ever know sits unsold in his head.**
- Recommended answer: **he writes it anyway, badly disguised, once — and it is the best thing he
  ever does, and he cannot stop himself.** A silver-haired girl who goes away. A boy who cannot
  cultivate. A dragon under the sea. 🔴 **It should not be published in Book One.** It should be
  written, hidden, and known to the reader.
- 🔴 **And the disguise must be thin enough that Wulin could recognise it.** That is the fuse.

**(e) What genre does he break the continent with first?** Unruled. Candidates: mystery (the
form's whole pleasure is withheld information, which is his native condition) · revenge ·
romance (🔴 he was uncomfortable with girls his own age in both lives and would be *excellent*
at writing them, and would hate that he was) · children's serial (available at six, and it is
where Na'er starts). **Recommended: children's serial first, mystery second.**

**(f) Does any of it ever reach canon's institutions?** The Spirit Pagoda, the academies, the
Federation. 🔴 **Reserved. Not in Book One.** But note the shape: a continent-wide organisation
that controls information and charges for access is exactly the kind of body that eventually
buys stories. That is a Book Three problem.

---

### 22. 🔴🔴 THE MEMORY IS LOSSY — "four hundred chapters and I remember the ones I liked"  · staged ch5

Ch5, standing in a yard at six in the morning, having just realised that a boy's hands healed
overnight and that canon has a whole chapter about it:

> *"He had the shape of it. A chapter title, maybe, or not even that — a page he had turned
> quickly, a family being warm, a father being worried, a paragraph he had read without reading.
> He had four hundred chapters in his head and had read perhaps sixty properly, and this was
> somewhere in the thirty he had moved through at speed with his thumb."*
>
> *"Nothing about a lamp."*
>
> *"So. That's what it is. Four hundred chapters and I remember the ones I liked."*

🔴🔴 **THIS IS A STRUCTURAL RULING AND IT RETROACTIVELY GOVERNS EVERYTHING.**

Until now the project has treated the meta-knowledge as a reference work — something he can
consult, which decays because events diverge (`CANON_LEDGER.md`). That was too generous. The
truth is worse and much more usable:

> **He does not have the book. He has a memory of having read the book.**
>
> It is lossy, it is biased toward what entertained him, it is strongest where the fights were
> and weakest where the families were, and it degrades on retrieval rather than on divergence.
> He skimmed. He was reading on a phone at two in the morning. He liked the parts where things
> happened.

Consequences, all binding:

| Consequence | Effect |
|---|---|
| 🔴 **Canon knowledge is a skill check, not a lookup** | He cannot be relied on to know things. He can be relied on to *try*, and to sometimes come up empty, and to be confidently wrong |
| 🔴 **Domestic canon is the blind spot** | Family scenes, meals, money, school, mothers crying — **he skimmed all of it.** And that is exactly where this serial lives |
| 🔴 **Combat and power canon is his strong suit** | Ranks, rings, beasts, tournaments, who beats whom. He read those properly |
| 🔴 **The decay column now has two causes** | Divergence (the world moved) **and retrieval** (he never had it). `CANON_LEDGER.md` should track both |
| 🔴 **It makes the paradox worse** | He is bad at exactly the thing his survival depends on — knowing what happens to the people next door |

**And the rhyme with Track 8, which is not a coincidence:**

> 🔴 He skipped the family chapters because they were not the good part. **He is now an author,
> and the family chapters are the only part he has.** The thing he was too bored to read is the
> thing he is uniquely equipped to write, and the thing he is standing inside, and the thing he
> keeps failing to notice until it has already happened.

**(a) How often may he fail to remember?** Often. 🔴 **Recommended: he fails to retrieve
something important at least once every three chapters**, and the failure must cost him
something, not just worry him.

**(b) May he ever be confidently WRONG?** 🔴 **Yes — and he should be, once, badly, in Book One.**
A misremembered detail that he acts on. That is the highest-value use of this ruling and it has
not been spent yet.

**(c) Does he ever realise the memory is unreliable?** Ch5 is the realisation. 🔴 **Do not let
him solve it.** He cannot re-read a book that does not exist. The only available response is to
start writing everything down faster — which is what he is already doing, and which is why the
book on the shelf is the most important object in the serial.

🔴 **And that lands him straight back in #14: the record is now unreliable in a second way.**
The memory was lossy. **The book is edited.** He has no trustworthy account of anything.

### 23. 🔴 #14 ESCALATED — the book now holds a falsehood  · staged ch5

`#14` asked: *the book is on an open shelf — when does someone read it?* It has now been
escalated twice and needs re-ruling.

```
ch1-3   The book exists. Notes only. True. On an OPEN shelf, second row, where his mother
        can reach it.
ch4     🔴 First WITHHOLDING. He writes the numbers and not the idea. The record becomes
        incomplete — but everything in it is true.
ch5     🔴🔴 First FABRICATION. Two versions of one night, one above the other. The second
        has four invented details: a man who has done it before, a duration, a bottle, and
        arms with nothing wrong with them. **He did not cross it out, because it was better.**
```

> 🔴 **The escalation is: hidden → edited → false.** And each step was taken for a *craft*
> reason, not a security reason. He is not covering his tracks. **He is improving the prose.**

Rulings needed:
- **(a) When does someone read it?** Still unruled, and now much more dangerous — because a
  reader would find the second version and believe it, and would learn about a light on a
  man's shoulder. 🔴 **Su Wan has already looked at the shelf and not said so (ch3).**
- **(b) 🔴 Does he ever notice what he has done to his own record?** He has not, yet. The
  chapter ends with him understanding that by the end of the year he would not be able to say
  whether the boy woke up. **Recommended: the moment he needs the true version and cannot
  recover it, in a crisis, and it matters.**
- **(c) Does Track 8 make this worse?** 🔴 **Yes, permanently.** Every story he ever writes is
  practice at making false things compelling. He is getting better at the exact skill that
  destroys his only reliable instrument. **This is the serial's central irony and it should
  never be resolved.**

---

## 24. 🔴🔴 THE FOUR — eyes three, sense four, same corner, one minute apart  · NEW, ch8

### The fact

Day forty. The sense comes back after twenty-six days out. He feels three thin things in a
hand's width of dirt in the angle of his own wall — the control group he has counted with his
eyes eleven days running and written down eleven times as three, one of which is a stump since
the goat got in on day thirty-three.

> He counts **four**.
> He kneels in the dirt with his face a hand from the ground and looks at the angle from every
> side he can manage. **There are three.** *"He could have sworn to it in front of anybody."*
> He writes: *eyes: three. sense: four. same corner, same evening, one minute apart. **I do not
> know which is wrong.***

### The readings available — and the ruling

| # | Reading | Cost | Verdict |
|---|---|---|---|
| a | The sense is wrong. He has been blind for twenty-six days and it came back miscalibrated | Cheap. Kills the instrument's credibility for a chapter | ❌ Too easy, and it wastes the control |
| b | The eyes are wrong. **The fourth is under the dirt** — a seed, a root, a shoot not yet surfaced | 🔴 The sense reports living plant matter; eyes report only what is above ground | 🔴🔴 **PRIMARY. Held open.** |
| c | Something is under the wall that is not grass | Escalates to Firewall territory | ❌ Reserved. Not in Book One |
| d | Both are right and they are measuring different things | 🔴 **This is the actual answer and it is the chapter's law** | 🔴🔴 **RULED** |

> 🔴🔴 **RULING: (d) is the truth and (b) is the most likely mechanism, and the serial must never
> confirm either on the page.**
>
> **He cannot check (b) without digging up his own yard in front of his mother.** He does not do
> it. He does not do it for a long time. And when he finally does, **it must not be to satisfy
> curiosity about the four — it must be because something else forced the ground open.**
>
> 🔴 **Why this matters structurally:** it is the exact shape of #15's grass sense (shape, not
> content) and of R13's ruling on the spiritual power test (a range, not a number). 🔴🔴 **His
> instrument, his nature, and the machine that will eventually measure him all report the same
> way: they tell him something is there and refuse to tell him what.**
>
> **The four is not a plot device. It is the serial's epistemology, arriving as a gardening
> problem.**

### Do / do not

```
DO    let him write both numbers down and neither belief
DO    let him keep counting. The count continues. The disagreement continues
DO    let the stump be part of the problem — a stump is alive and is not visible as a plant
DO    let this make him distrust the sense in a way that is not fear but bookkeeping
DON'T resolve it in ch9. DON'T resolve it by digging. DON'T resolve it at all before Year 1
DON'T let anyone else see the four. It is in the book and the book is on an open shelf
```

🔴 **Cross-references:** #15 (the sense reports shape not content) · #22 (lossy memory) ·
#23 (the book: hidden → edited → false, and now **incomplete**) · R13 (a range, not a number).

---

## 25. 🔴 THE YEAR-0 GAP — canon supplies nothing for three years  · NEW, 2026-09-20

Canon 011 is the family argument. **Canon 012 is titled "Three Years Later."** Between them the
canon is silent, and the serial is currently at **day forty-one of Year 0** with about
**three hundred and twenty days of Year 0 still unspent**, plus Years 1 and 2.

```
YEAR 0, day 41    ← WE ARE HERE
YEAR 1            Na'er awakens — NO MARTIAL SOUL. She goes quiet. 🔴 TRACK 8 OPENS HERE,
                  as a story told OUT LOUD to her, never written. (STATUS_PANEL: no manuscript
                  before Year 2.)
YEAR 3            Wulin counts 30,200 Federation Coins on a table. Canon 012 resumes.
```

🔴🔴 **THE PACING PROBLEM.** Ch6 covered eight days. Ch7 covered six. Ch8 covered twenty-one.
At that rate Year 0 alone is another fifteen chapters, and nothing happens in most of them.

> **RULING: compress hard from ch9 onward.** The blind month proved the serial can hold
> twenty-one days in 3,500 words. 🔴 **Target: Year 0 should end within the next three to five
> chapters**, using season turns, school terms, and the second-holiday rhythm (already
> established: every month, Su Wan walks him to the garden, he counts, she asks nothing) as the
> compression joints.
>
> 🔴 **The holiday rhythm is the serial's metronome and it is already built.** Use it to skip
> months. Each visit: he counts, the numbers move, she stands where she can see him, nothing
> happens. **Until something does.**

**What must survive the compression:** the gauge spreading (Zhao → bursar → academy storeroom) ·
Lan Yue's job · the balm's reputation · the body work · Lin Ximeng's three years of watching ·
🔴 **and the Four, unresolved, in a book on an open shelf.**

---

# 26. 🔴🔴 THE THREE BINDING CORRECTIONS — nothing contested, nothing moves, one voice  · NEW, 2026-09-20, from `audits/2026-09-20_FULL_COMPARATIVE_AUDIT.md`

## The diagnosis, stated without softening

The audit walked `03_STORY_LAW.md` §2 across nine shipped chapters. Failure 1 (no canon
spine) **passes** — eighteen extracts read, spine documented, eight tracks planned. Failure 5
(apparatus) is a **watch**. The other three are real:

```
FAILURE 2 — NOTHING CONTESTED.   ch5, ch6, ch7, ch8, ch9 all carry an abstract THREAT.
                                 ch9's panel declares it: "Not cost, not discovery,
                                 not a person."
FAILURE 3 — NO FELT PROGRESSION.  rank one in ch1, rank one in ch9. No number moved
                                 in 45,000 words.
FAILURE 4 — ONE REGISTER.        Other POV is absent from ch7-9. Italic blocks across
                                 the serial: 11, 13, 20, 12, 24, 13, 3, 0, 0.
```

`03_STORY_LAW.md`: *"A story where the protagonist cannot fail is not a story, however
lovely the sentences are."* Lan Shen's verbs across five chapters are **count, write,
wait, avoid.** Nothing opposes him, nobody wants anything from him, and he cannot be
caught because nobody is looking.

**Two hard failures is the threshold at which the kit says "you are not editing, you are
rebuilding."** That verdict is *declined here, and the reason is recorded:* the prose, the
canon discipline and the codex are strong, and Failure 2 is an **omission** rather than a
wrong choice — `THE_PLAN.md` already names **Yan Song as THE NEAR SPINE**, and
`STATUS_PANEL.md` already says *"do not spend the near spine in chapter two."* The
antagonist was built and then never used. That is repairable forward. It is not repaired
yet, and no amount of infrastructure repairs it — only chapters do.

## The insight that closes two failures at once

Failures 2 and 3 are the same wound. **A number that moves makes him visible, and
visibility makes him contested.**

Canon supplies both halves for free. Canon 017 is the spiritual power test — a metal
helmet, six realms, a number filed in a record. Canon 018 opens by giving Wulin's number:
38. The author's character ruling says Lan Shen's spiritual power is **HIGH, with large
effects.** So the test is where a number moves, and the number it moves to is the kind of
number that gets a boy noticed.

And the man who keeps the register for the Soul Master class, who has a number to hit, who
appeared in chapter one and has not been spent — **is the correct face for a number that
moves.** Yan Song is not a villain bolted on to satisfy a checklist. He is the institutional
consequence of Failure 3 being fixed.

## THE THREE BINDING CORRECTIONS

> ### (a) FACE LAW — every chapter gets a person
> From ch10 onward, **every chapter's THREAT field must name a person** who wants something
> from Lan Shen, or from someone he protects, and who has **at least three spoken lines**.
> Abstract threats (the season, his own instrument, the ground moving) are permitted **at
> most once per arc**, and only in a chapter that also carries a named face at lower
> pressure. A chapter whose only opposition is interior meditation **does not ship** —
> `03_STORY_LAW.md` §3 makes this a hard rule, not a guideline.
>
> **The prewrite gate now checks this before drafting, not after.** See (d).

> ### (b) NUMBER LAW — something must move
> **At least one number moves every two chapters**: a rank, a measurement, a spiritual power
> reading, a sum of money, a count of days that resolves into a date, a gauge that spreads to
> a new office. `03_STORY_LAW.md`: *"Show the number. Show the cost."*
>
> #15 still binds — progression is paid for, and cost is **width, not time** (a dense
> twenty seconds in the garden cost a nosebleed and about a month). But **a rule that only
> ever defers is indistinguishable from a rule that never fires.** Cost governs *how much*
> a number may move. It does not govern *whether*.
>
> 🔴 Year 0's compression (#25) must land on numbers. Each holiday visit already has him
> count; **the counts must visibly differ from each other**, and by the end of Year 0
> something in his body or his record must read higher than it did in chapter one.

> ### (c) REGISTER LAW — the fifth register returns
> **Other POV at least once every three chapters**, and it must be a real scene from behind
> another pair of eyes — not Lan Shen inferring what someone thought. `style_gate.py` already
> supports a declared `POV:` panel field and skips the Spectator Test for it, so this needs
> no new tooling, only use.
>
> Ch10 or ch11 **must** carry one. The natural candidates, all already on the board:
> **Lin Ximeng**, who has watched for three years and has a file; **Yan Song**, reading a
> register with a number in it that does not match; **Na'er**, in the hour after she is told
> she has no martial soul; **Su Wan**, who has never once asked what he is counting.

> ### (d) THE PREWRITE CONTRACT IS NOW SEVEN ITEMS, NOT SIX
> `00_START_HERE.md` requires seven questions before drafting. This project's gate had six
> and was missing **BUTTERFLY** — it was being answered afterwards, in `CANON_LEDGER`'s
> decay rows, which is backwards. From ch10:
>
> ```
> 1. CANON BEAT — what canon does this touch, and how does it stay true?
> 2. THREAT     — what can hurt someone here?          ← must be a PERSON (Face Law)
> 3. FACE       — who opposes, named, with ≥3 lines of dialogue?
> 4. MOVEMENT   — what changes: rank, ring, skill, bond, resource, knowledge, NUMBER?
> 5. BUTTERFLY  — what does his existence change about canon?      ← NEW, now pre-draft
> 6. REGISTERS  — ≥3 of the five, and is Other POV due? (Register Law)
> 7. TURN       — what is true at the end that was not true at the start?
> ```
> `03_STORY_LAW.md` §4: *"A rule that is never broken is not a butterfly — it changes
> nothing downstream. If your divergence changes nothing, do not claim it changed the story."*

## Do / do not

**Do** — spend Yan Song deliberately and soon, with a motive stated in his own dialogue ·
let a number move on the page · put one chapter behind someone else's eyes · let opposition
be **institutional** as well as personal (a register, a file, a gauge, a bursar) because
that is the pressure a hidden boy actually feels · keep the holiday metronome as the
compression joint.

**Do not** — invent a villain to satisfy the checklist · let an abstract THREAT run a sixth
chapter · treat #15's cost rule as permission to defer forever · put Other POV in as a
paragraph of Lan Shen guessing · let the face arrive without a want.

## Status

🔴 **OPEN — BINDING FROM CH10.** Diagnosis complete, ruling made, corrections not yet
executed in prose. Re-audit after ch12 against all three failures.

---

## 🔴 #26 STATUS UPDATE — CHAPTER TEN EXECUTED ALL THREE CORRECTIONS (2026-09-20)

**#26 is no longer only a ruling. It has been executed once, in prose, and the serial has ten
chapters and 50,136 words.**

```
(a) FACE LAW      ✅ EXECUTED. Yan Song named, motivated, 20+ spoken lines, and he never
                  raises his voice. The five-chapter run of abstract threats (ch5-9) is
                  broken. Plus Qin Wu, Na'er, Wulin, Lang Yue, Bo.
(b) NUMBER LAW    ✅ EXECUTED. Na'er's record moves to blank. The gauge reaches a FOURTH
                  office. Qin Wu's anomaly count two → three. The thirty-day payment
                  resolves. And ch1's unpaid "working student" line, nine chapters old, is
                  answered rather than forgotten — 03_STORY_LAW §5: "an honest 'not now'
                  beats accidental forgetting." It is now an explicit "not yet."
(c) REGISTER LAW  ✅ EXECUTED. Other POV returned (Qin Wu, italics). Five registers used.
                  Italic blocks across the serial now: 11,13,20,12,24,13,3,0,0,🔴 restored.
(d) BUTTERFLY     ✅ Answered PRE-DRAFT for the first time. See foundation/PREWRITE_ch10.md.
```

🔴 **THE INSIGHT HELD.** "A number that moves makes him visible, and visibility makes him
contested." Na'er's blank is the number, and the man who wants a clean register is now looking
at the boy whose family supplies it. **Failure 2 and Failure 3 were the same wound and the
same chapter closed both.**

**Re-audit is due after ch12**, per #26. The three failures are not "fixed" by one chapter —
they are fixed by a run of them.

## 🔴 #25 UPDATE — YEAR 0 IS CLOSED

Ch10 spans `years 0–1`. The forty-three days of term break were skipped in one paragraph, which
is the compression #25 demanded. **Year 0 ended inside the target of three to five chapters
from ch9 — it took one.**

🔴 **The same problem now recurs at larger scale.** Canon 012 is *"Three Years Later"* and
canon 013 (the workshop) is Year 3. **Roughly two years of serial time remain unspent and
canon is silent on all of it.** What must survive: the gauge spreading · Lan Yue's job · the
balm's reputation · the body work · Lin Ximeng's three years of watching · 🔴 **the Four,
unresolved, in a book on an open shelf** · and now **the offer, and the column, and the third
form in the post.**

## 🔴 #21 UPDATE — TRACK 8 HAS FIRED

The mountain story. Told **out loud**, on the Tang doorstep, in the dark, with no paper anywhere
near him. No manuscript before Year 2 — **held.** He declared it a made-up thing before he
started, and he obeyed the governing rule: *he may write anything except the truth.*

🔴🔴 **And she asked whether he had made it up just now or already had it, and he lied.** He had
had it for four years and another lifetime. **That is the first lie in the serial told for her
benefit rather than his own.**

## 🔴 #20 UPDATE — NA'ER IS LEAVING, AND NOW SHE HAS A REASON TO BE QUIET

Canon 015 has her leaving. `#20` was staged on the assumption that she goes quiet. **Ch10 gives
the quiet a cause that canon does not supply:** she has been written into a register as nothing,
in public, by a man using the voice he keeps for the four-times-a-year version. 🔴 **Do not let
the serial spend the canon reason and the invented reason as though they were the same thing.**

---

## 🔴 #26 STATUS UPDATE — CHAPTER ELEVEN EXECUTED ALL THREE AGAIN (2026-09-20)

```
(a) FACE      ✅ LIN XIMENG — THE DETECTOR, on page and inside his own head. He wants an
              explanation. He never raises his voice either. Plus Su Wan, Lan He, Lan Yue,
              Na'er, the man with the key.
(b) NUMBER    ✅ his name into a column with SIXTEEN HOURS against it · the black book's
              six-month hole starts filling · the fee becomes formal · the garden count
              resumes and rises 19,400 → 19,600 · 468 weeks / 1,870 hours done at a pump in
              four seconds.
(c) REGISTER  ✅ Other POV again (Lin Ximeng, italics). Two chapters running. Five registers.
(d) BUTTERFLY ✅ pre-drafted. TWO ANOMALIES IN ONE SMALL CLASS — canon 012's solo
              investigation becomes a comparative one.
```

🔴 **Two consecutive chapters have now satisfied all three. The five-chapter run of abstract
threats (ch5-9) is closed. #26 is no longer aspirational; it is the serial's operating method.**
Re-audit still due after ch12, per the ruling.

## 🔴 #20 UPDATE — NA'ER'S SCHOOLING IS SETTLED, AND IT IS NOT WHAT #20 ASSUMED

`#20` was staged on the assumption that Na'er goes quiet and eventually leaves (canon 015).
Ch11 adds a fact that changes the shape of it:

> 🔴 **She is not in the Soul Master class and never will be. She starts next year in the
> ordinary one, a year behind Wulin.** R2 holds — schooling is nine years, free and compulsory,
> so she is not out of school, only behind, and she has worked out what behind means by herself:
> *"I'll be the biggest one in it, because I'll be six and three quarters and they'll be six."*

**Consequence for #20:** a child who is a year behind, in the ordinary class, with no martial
soul, in a city where her brother is being watched for going too fast — **leaves sooner and for
a better reason than canon supplies.** 🔴 Do not spend the canon reason and the invented reason
as though they were the same thing.

## 🔴🔴 #27 — NEW, ch11 — THE THING HE COULD NOT FIND

Lan Yue asked her brother for one fact about himself that was not the jar thing, the garden
thing, or the count. **He could not find one.** He offered the canteen soup.

> *He sat there with a bowl going cold in front of him and searched for a single fact about
> himself that was not a measurement or a plan or a lie, and he could not find one, and the
> not-finding was so fast and so total that it felt less like a failure of memory than like an
> answer to a question he had not known he was being asked.*

🔴🔴 **This is the most serious thing in eleven chapters and nobody in the serial noticed it.**
*(Ch12 update: it has now been noticed by exactly one person, from the outside, and she has
started writing his answers down. See "#27 — CH12 UPDATE" below.)*

**What it is:** a man who died and was reborn, who has spent a year converting himself
entirely into instrument, discovering that the conversion is complete. He is not hiding a self.
There is increasingly no self there to hide — which is a different problem from concealment and
cannot be solved by concealment.

**Ruled:**

- **Do not resolve it.** Not in ch12, not soon. It is a condition, not a plot.
- **Do not let him become self-aware about it.** The horror is that he noticed and then answered
  with soup. A chapter where he agonises over it turns a finding into a mood.
- **Lan Yue's standing demand is the instrument.** Next Wednesday he owes a second one and she
  does not expect to get it. That is a metronome, like Su Wan's holiday walk, and it should
  recur and should keep not being satisfied.
- 🔴 **Track 8 is the eventual answer and the serial already knows it.** A man with nothing
  about himself can still make things up — that is what an author is. The mountain story was
  not a fact about him either. **He is better at inventing selves than at having one, and that
  is why Track 8 exists.** Do not state this. Earn it.


---

## 🔴🔴 #27 — CH12 UPDATE: THE LIST IS NOW A PHYSICAL OBJECT

**Ruling stands, unchanged: do not resolve it, do not let him agonise.**

Ch11 established the not-finding. Ch12 gave it an instrument and an owner.

Lan Yue has now rejected four substitutes — the canteen soup (rejected: *"that's about work"*),
the smell of the storeroom in the morning before anybody has opened the window, a way of walking
home two streets longer than the short way that he has never once taken the short way on — and
has written all of them **on the back of a noodle ticket, in a hand worse than his.**

> *"Because you're not going to say the real one, so I'm going to write down all the ones you
> say instead, and one day there'll be enough of them that it'll add up to a person, and I
> won't have to ask."*

He is seven. She is eleven. He went to bed and worked out whether that was a threat, decided it
was not, **and then decided that the reason it was not a threat was worse.**

🔴 **THREE BINDING CONSEQUENCES:**

1. **The Wednesday is a metronome, not a crisis.** It recurs. It keeps not being satisfied.
   Do not escalate it into a confrontation.
2. 🔴 **The ticket is an object in the house.** It can be found. By Lan He, by Su Wan, by
   Yan Song's people, by anybody. Banked, unspent. Do not spend it without a reason.
3. 🔴 **Su Wan is now collecting him too, by a different route, and neither woman knows about
   the other.** *"You can hold still for longer than four minutes"* — she had never been told
   four. Two patient collectors, one subject, no communication between them.

🔴 **TRACK 8 REMAINS THE EVENTUAL ANSWER AND MUST STILL BE EARNED, NEVER STATED.** A man with
nothing about himself can still make things up. He is better at inventing selves than at having
one. Ch12 did not touch Track 8 and correctly so — the chapter was about the measurement, not
the escape.

---

## 🔴🔴 #26 — RE-AUDIT NOW FALLS DUE. EXECUTED A THIRD TIME IN CH12; CH13 MUST RE-RUN IT.

Ch12 execution:

```
(a) FACE      Lin Ximeng escalated from observer to instrument — a watch, a narrow column, a
              control. Also on page: Su Wan, Lan Yue, Wulin, Na'er, Jiang Ning, the boy at
              the back. ✅
(b) NUMBER    🔴🔴 THE FLAT LINE. Four minutes x ten weeks, eighth of fifteen. Real ceiling
              nine, told to nobody. Bank peak 41,200. Academy grounds sixty thousand strands,
              untouched once. ✅
(c) REGISTER  Other POV, THIRD CONSECUTIVE CHAPTER (ch10 Qin Wu, ch11 Lin Ximeng, ch12 Lin
              Ximeng). Legal — #26(c) requires it once per three and does not cap it — but
              🔴 **it is now the DEFAULT, and a default register is not a register.**
(d) BUTTERFLY Ran, and caught thirteen defects the gates could not. ✅
```

🔴🔴 **DEVIATION RECORDED: `PREWRITE_ch12.md` ruled Other POV deliberately OUT of this chapter.
It was written anyway**, because the flat line is only visible from inside the man keeping it —
from Lan Shen's side, four minutes looks like success. Cutting the section would have cut the
chapter's only dramatic irony and left *"why is this straight"* with nothing to be ironic
against. Recorded in SERIAL_LOG and in `PREWRITE_ch12.md`. Not excused.

🔴🔴 **BINDING ON CH13: Lan Shen's own register, unless a stated reason exists why it cannot
be.** The prewrite must rule on this explicitly, before drafting, not after.

---

## 🔴 #28 — NEW, ch12 — THE OTHER-POV DEFAULT (a standing hazard, not a chapter note)

Three consecutive chapters in another character's head has produced something the serial did
not plan for: **the reader now knows more than Lan Shen, reliably, every chapter.**

That is dramatic irony, and it is good — but it is only good while it is rationed. If every
chapter ends in Lin Ximeng's head, then:

- Lan Shen's own register atrophies (he has had none since ch9).
- The reader stops fearing for him, because a man watching from outside always explains him.
- 🔴 **The serial's central engine — that nobody knows what he is — gets quietly retired by
  the person narrating.**

**Ruled:**

- Other POV is a **spice, at most once per three chapters**, from ch13 onward. Stricter than
  #26(c), deliberately, because #26(c) set a floor and this sets a ceiling.
- The prewrite must state which register the chapter uses, and if it is Other POV it must state
  **why Lan Shen's own register cannot carry the discovery.**
- 🔴 **Ch13 uses Lan Shen's own register.** This is binding and was set at ch12's ship.
- Available Other-POV holders, ranked by remaining value: **Qin Wu** (three forms, one drawer,
  the far spine, and he noticed something behind Na'er's eyes) · **Yan Song** (has started
  looking at him; the near spine, unspent since ch10) · **Na'er** (canon 024 is titled
  "Na'er Leaves" — 🔴 **she is saying goodbye nine chapters early and nobody hears her**) ·
  Zhao · the man with the key.
- 🔴 **Lin Ximeng has now been used twice running. He is the least valuable Other-POV holder
  left, because he has already been given his interior.**


---

## 🔴🔴 #26 — EXECUTED A FOURTH TIME IN CH13. ALL FOUR. NO DEVIATION.

```
(a) FACE      ✅ 🔴 NEW FACE DELIVERED — MADAM ZHOU. Ch12 had passed on a returning one and Lin
              Ximeng had carried three chapters running; ch13's board ruled a new face mandatory
              and got one. She is not a villain, has no backstory, and wants an answer rather
              than a fight. Tang Ziran also got his best scene.
(b) NUMBER    ✅ 🔴 AND IT MOVED THE WRONG WAY, WHICH WAS THE POINT. Ch12's trick was a number
              that did not move; that could not be repeated. Ch13's is a number that turns out
              to have been the floor all along: thirty thousand stopped being the price of a
              spirit soul and became the price of the cheapest one. Plus bank 20,100 → 42,600,
              ten pages of manuscript, and Lan Yue's list four → five.
(c) REGISTER  ✅ 🔴🔴 #28 SATISFIED. LAN SHEN'S OWN REGISTER. NO OTHER POV. First time since
              ch9. Four of five registers used. **No deviation, no exception, nothing to log.**
(d) BUTTERFLY ✅ Run pre-draft AND post-draft. Twenty-two defects. 🔴 Four were stale year
              counts — the dominant class — and one was an entire promised scene missing.
```

---

## 🔴🔴 #27 — CH13 UPDATE: THE MECHANISM HAS NOW BEEN EARNED. IT HAS NOT BEEN STATED.

**Ruling stands, unchanged: do not resolve it, do not let him agonise.**

Ch11: he could not find one fact about himself that was not a measurement, a plan or a lie.
Ch12: Lan Yue started keeping a list of his substitutes.
🔴🔴 **Ch13: he gave her a story instead of a fact — and the story contained the only true
sentence he has written in two lives.**

The mechanism `#27` predicted, from the day it was opened:

> *A man with nothing about himself can still make things up — that is what an author is. He is
> better at inventing selves than at having one, and that is why Track 8 exists. Do not state
> this. Earn it.*

**It has now been earned.** The steps, exactly as they happened on the page:

1. He could not produce a fact. So he produced a thing instead: *"It's not a saying one. It's a
   giving one."*
2. Lan Yue asked the only question that mattered: *"So how do you know about the doorways."*
3. He found he was not reaching for an answer, and the not-reaching was so unfamiliar he had to
   look at it before he could speak.
4. *"I made it up." — "That's not an answer." — "It's the only one I've got."*
5. She filed it on the ticket as the fifth one, under the soup. 🔴 **A category error: a list of
   facts about a person is not a list of things a person has done.** He did not tell her so.

🔴🔴 **WHAT CH14 MUST NOT DO:** explain any of this. Nobody in the serial has said "he can invent
selves because he has none." Not the narrator, not Lan Yue, not Su Wan, not Lin Ximeng. If ch14
states it, three chapters of earning are void.

🔴 **What ch14 MAY do:** let him do it again, better, and let it cost something. The story is on
the second row of the shelf where his mother can reach it, in the same book as the counts and
`#23`'s falsehood and the column of fours. **It is the only thing in that book that is not a
record, and it is the most dangerous object in the house.**

🔴 **The noodle ticket now has five entries and a category error in it. It remains a findable
physical object. Unspent.**

---

## 🔴🔴 #28 — SATISFIED IN CH13. THE CEILING NOW HOLDS.

Ch13 used Lan Shen's own register, four of five registers, no Other POV. ✅

🔴 **The ration from here:** Other POV at most once per three chapters, combined with `#26(c)`'s
floor of at least once per three — which together mean **exactly once per three.** Ch13 was the
zero. Ch14 should be a zero. **Ch15 is the slot.**

🔴 **Ranked by remaining value for the ch15 slot:**

1. 🔴🔴 **NA'ER.** Canon 024 is titled "Na'er Leaves." She has just said *"Right"* to being
   recognised in a story and gone back to the third page. **She is the most valuable unread
   interior in the serial and she has five chapters of serial time left in it.**
2. 🔴🔴 **TANG ZIRAN.** He has asked "how long have you had it" and been told "a while," and he
   has put his hand on the back of that boy's neck. Canon 011's investigating-his-son fuse is
   live and now has two children in its field of view.
3. 🔴 **YAN SONG.** The near spine, unspent since ch10. He has started looking at him.
4. 🔴 **QIN Wu.** Three forms, one drawer, and something behind Na'er's eyes he had no business
   noticing.
5. **MADAM ZHOU — NEW, AND ALREADY PARTLY SPENT.** She has an interior implied but not given,
   and a pencil line she has not decided to keep. 🔴 **Hold her. She is worth more unseen.**
6. 🔴 **LIN XIMENG — LOWEST VALUE.** Used twice running, already given his interior, and ch13
   proved he changes chapters better from offstage.

---

## 🔴 #29 — NEW, ch13 — THE PRICE FOLLOWS THE AGE, NOT THE QUALITY

Canon 016's table: random selection 30,000 FC · ten-year WHITE 70,000 (73 in stock) ·
hundred-year YELLOW 1,000,000 (11 in stock).

Canon 019's outcome: **30,000 FC bought a defective Grass Snake from position one hundred of
exactly one hundred.**

🔴🔴 **Ch13 has now put the mechanism on the page, in-world, through Lin Ximeng's mouth:**

> *quality matters more than age · the price follows the age and not the quality · this is a
> fact about markets rather than a fact about souls · a man who could not tell the two apart
> would end up paying for a number.*

**Ruled:**

- 🔴 **Lan Shen knows the DIRECTION, not the numbers.** He knows thirty thousand is the cheapest
  thing there is. He does NOT know 70,000, does NOT know 1,000,000, does NOT know the inventory
  counts (73 and 11), and 🔴🔴 **DOES NOT KNOW ABOUT THE GRASS SNAKE.** There is no Spirit Pagoda
  branch in Glorybound City and no case-carrying man in the second term to ask.
- 🔴 **He must not foresee canon 018/019.** He read the novel in the other life and remembers
  parts; the parts he remembers must stay vague, and the serial must never let him act on
  foreknowledge of a specific outcome. He has never done so in thirteen chapters. Do not start.
- 🔴 **The target has moved and it moved AWAY.** This is the first time the serial has made a
  number worse instead of better, and it should be the shape of Book One's second half: the
  further he gets, the further the goal recedes. `#25` compression is what lets that happen
  without stalling.
- 🔴 **2,727 days of Lan Yue's mornings bought the snake.** The white is 6,364 days — seventeen
  and a half years of her mornings. 🔴 **Nobody in the serial has done that second sum. Do not
  let anybody do it out loud before Year 3.**
- 🔴 **Track 8 is now the only route with no capital requirement, and it has no market.** Nobody
  in Glorybound City buys stories. The infrastructure that exists is: a paper shop on the long
  street, a quire price, and a man with a case who comes twice a year. 🔴 **The next Track 8
  question is not "can he write" — it is "who buys."**

