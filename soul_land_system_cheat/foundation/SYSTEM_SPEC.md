# THE SYSTEM — complete design spec

Design stage v1.0 · 2026-09-24 · status: AUTHOR REVIEW
Author spec and session rulings: see `../README.md`. Numbers marked **[DIAL]**
are proposed defaults — tunable by the author without breaking anything. The
slot schedule (§3) is settled by the author's word (the unified slot law).
Author-gated decisions live in `OPEN_RULINGS.md`; nothing there is settled
until the author's word.

---

## 0. WHAT IT IS (one paragraph)

The System is a cheat attached to one holder: a **real-time simulation
engine** that runs, 24 hours a day, perfect simulations of the holder
training what he has placed in its slots — techniques, soul rings, soul
bones. It is not a martial soul, not a spirit, not a living thing. It has no
voice, no quests, no shop. It does one thing: **it trains, endlessly, at the
holder's own best speed, and the gains are real from the first percent.**
The holder of the System is, in effect, many men training in parallel —
while he lives one life, the others never sleep.

## 1. THE CORE LAW — real time, real gains (author ruling, verbatim)

> "System acutely progress in real time, it's like simulation happening so
> you don't need to reach 100% to get"

1. Every slot runs a perfect simulation of THE HOLDER doing that one thing
   at his absolute best: perfect form, perfect focus, no fatigue, no injury,
   no distraction, no bad-practice plateaus.
2. The simulation runs 24 hours a day — waking or sleeping, eating,
   travelling, fighting. It never pauses on its own.
3. **The gains are real from the first percent.** This is the heart of the
   design. A technique at 34% means he genuinely holds 34% of that stage's
   skill, in his real body and mind, right now. The meter is not a countdown
   to an unlock — **the meter IS his mastery.** The System is not a timer;
   it is another him, training, and what that him learns, he has.
4. **One true meter.** Gains he earns alive (real practice, real sparring)
   add to the same percentage the slot fills. Nothing is double-counted;
   nothing is lost. The slot's contribution is simply the part that never
   sleeps.
5. **What the meter cannot hold** (live experience): combat instinct,
   adaptation under pressure, killing intent, reading a live enemy, pain,
   fear, and everything else that only exists when something can cut you.
   The simulation has never bled. These are earned alive, or not at all.

## 2. THE ARCHITECTURE — categories, lists, slots

The System is organized into **CATEGORIES**. Each category has:

- a **LIST** — the catalogue of everything the holder has acquired or
  genuinely learned in that category. Listed items keep their progress
  forever, but only slotted items advance.
- **SLOTS** — the active bays. Anything from the list can occupy a slot;
  slots are generic within their category. What occupies a slot progresses
  24/7. Unslotting pauses progress (keeps it, never loses it); re-slotting
  resumes exactly where it stopped.

**Three categories exist (author spec):**

### 2.1 TECHNIQUE & METHOD

Anything learnable: swordsmanship, spear, dagger, footwork, body
conditioning, cultivation methods (the Mysterious Heaven Method and its kin
slot here — cultivation itself can be slotted), forging, poison craft,
theory, languages, anything that is a skill or a method.

- Slot a technique → its meter runs 1% → 100% at his best speed, 24/7.
- **The 100% upgrade (author spec):** at 100%, the stage is mastered —
  permanently — and the technique upgrades to the next stage at 0%, training
  on unless he pulls it. *Basic Swordsmanship* → *Advanced Swordsmanship* →
  … The ladder (proposed) **[DIAL]**: Basic → Advanced → Master →
  Grandmaster → Perfection → Origin.
- Mastery stacks: a Master-stage 40% swordsman is Basic 100% + Advanced
  100% + Master 40%, all of it real, all of it his.
- Slotting requirement (proposed, OPEN S4): the technique must be genuinely
  his to train — learned once, understood at least in its basics. The System
  trains what exists; it invents nothing.

### 2.2 SOUL RING

- A soul ring placed in a ring slot **ages** — its year-count climbs 24/7
  (author spec: "automatically age increase accordingly to user").
- Aging speed is a function of the holder (the user-scaling law, §4);
  proposed ladder **[DIAL]**: 1 year/day at Spirit Scholar, doubling each
  rank-up (2/day at Spirit Master, 4 at Grandmaster … 512/day at Titled
  Douluo).
- The ring's color and class re-evaluate as thresholds cross: 99→100 (white
  → yellow), 999→1,000 (yellow → purple), 9,999→10,000 (purple → black),
  99,999→100,000 (black → red), 999,999→1,000,000 (red → gold).
- Aging deepens the ring's skill — more power, longer sustain, lower cost —
  but never changes WHAT the skill is **[DIAL, OPEN S9]**.
- **System ring slots are not body ring slots.** The System can hold and age
  rings he has not fused — spares for future ranks, trade stock, or strategy.
  His body still bears at most the canon nine.
- Aging works on stored rings by default; whether FUSED rings can be aged is
  an author ruling (OPEN S3).
- **The absorption law stands (canon):** a ring beyond the body's capacity
  can kill him. The System ages the ring; it does not strengthen his
  capacity to take it. Capacity is still earned — by rank, by cultivation,
  by the technique slots he points at it.

### 2.3 SOUL BONE

- Bones placed in bone slots **age** like rings — year-count climbing,
  effect and skill strength scaling with the years **[DIAL: aging proposed;
  refinement alternative in OPEN S8]**.
- Canon positions stand: head, torso, right arm, left arm, right leg, left
  leg — six, non-overlapping; external bones exist in canon and follow their
  own rules (OPEN S3 covers fused-bone aging with fused rings).
- As with rings: system slots can age bones not yet fused; the body still
  caps at its six.

### Future categories

The architecture is extensible (physique, item refinement, spiritual power,
…), but **nothing is added without the author's word** (OPEN S13).

## 3. SLOT GROWTH — THE UNIFIED SLOT LAW (author's correction, SC2-R2)

The author's word, verbatim: **"No, slots number's always same in every
list not different."** One number governs every category — the count is
always the same in every list. One rank-up = crossing into a new title
(levels 11, 21, 31, 41, 51, 61, 71, 81, 91), and every rank-up grants
**+1 slot to ALL lists alike**.

- **Base at system start (Spirit Scholar): 1 / 1 / 1** (confirmed by the
  author, SC2-R3).
- Growth: +1 to every list at every rank-up — no category ever outpaces
  another.

| Rank-up (title) | Every list holds |
|---|---|
| Spirit Scholar (1–10) — base | 1 / 1 / 1 |
| Spirit Master (11) | 2 / 2 / 2 |
| Spirit Grandmaster (21) | 3 / 3 / 3 |
| Spirit Elder (31) | 4 / 4 / 4 |
| Spirit Ancestor (41) | 5 / 5 / 5 |
| Spirit King (51) | **6 / 6 / 6** |
| Spirit Emperor (61) | 7 / 7 / 7 |
| Spirit Sage (71) | 8 / 8 / 8 |
| Spirit Douluo (81) | 9 / 9 / 9 |
| Titled Douluo (91) | 10 / 10 / 10 |

Notes:
- The author's original example — "one who have 6 slots" — lands at Spirit
  King (levels 51–60): deep mid-story.
- At the top: 10 ring slots to the body's nine (one spare aging at all
  times); 10 bone slots to the body's six positions (four spares); 10
  technique slots — the whole man, compounded.

## 4. THE SPEED LAW — "according to user best speed" (author spec)

1. Every slot runs at **the holder's own best speed**: the pace HE could
   sustain at his personal peak — his perfect day, his full focus, his body
   healthy. Not a genius's pace (unless he is one); not a fixed number.
2. The System measures his current best speed exactly, because it simulates
   him and nothing else. As his real body, talent, and rank grow, **every
   slot speeds up with him.** The cheat compounds with the man.
3. What the System sells is **perfect consistency**, not talent: 24/7 at
   best-speed — never tired, never sick, never sloppy, no off-days, no
   plateaus from bad practice.
4. Scale, honestly stated: against a hard trainer's six focused hours a
   day, one slot ≈ four of his schedules — running on top of the holder's
   own live practice, and across every slotted thing at once.

## 5. THE INTERFACE (proposed) **[DIAL, OPEN S6]**

A quiet readout only the holder can open: categories, lists, slots, meters,
aging counts, the rank-up schedule, and the current best-speed the System
measures. Opens and closes at will; invisible to everyone and everything
else (spirit sense, soul pressure, inspection — OPEN S10 for god-level
exceptions). No sound unless he allows it. **The System is silent — no
voice, no praise, no notifications beyond the plain numbers.** It is a
readout, not a personality.

## 6. THE BALANCE LOCKS (what keeps it honest)

1. **TIME, NOT TALENT.** Slots run at HIS best speed. Geniuses still exist
   above him; effort still has a ceiling he must raise alive.
2. **THE METER IS HONEST.** 34% means 34%. No mastery arrives early.
3. **SCARCITY IS THE GAME.** Few slots, many wants. What he slots is who he
   becomes; unslotting pauses, never refunds.
4. **LIVE EXPERIENCE IS EARNED ALIVE.** Instinct, adaptation, killing
   intent — outside the meter. The simulation has never bled.
5. **NO CREATION FROM NOTHING.** The System trains, ages, and refines only
   what EXISTS and is genuinely his: a technique learned, a ring taken, a
   bone owned. It spawns nothing, invents nothing, knows nothing he does not.
6. **CANON CAPS STAND.** Nine rings on the body, six bones, absorption
   limits, rank requirements. The System bypasses none of them.
7. **ONE OF A KIND.** A given thing occupies at most one slot. No stacking.
8. **HIDDEN BY NATURE.** It is not a martial soul; nothing in the world
   reads it in him.
9. **THE CHOICE IS THE COST.** Every hour a slot trains one thing is an
   hour it did not train another. Opportunity cost is real and permanent.
10. **IT NEVER STOPS.** The System does not sleep, wait, or forgive. What he
    slots grows — forever. There is no pause button except his own choice of
    what deserves the slots.

## 7. WHAT THE SYSTEM IS NOT

- **Not a martial soul** (author ruling) — nothing about his awakening
  changes because of it.
- **Not a shop, not a quest-giver, not a points economy** (author ruling:
  slots come from spirit rank).
- **Not an item factory** — no spawning, no buying, no repairing.
- **Not a knowledge download** — it trains what he knows; it does not teach
  what he has never learned.
- **Not a second self** — the simulation is a training simulation, not a
  mind, not a person, not a voice.
- **Not a time machine** — everything happens in real time, in his one life.
