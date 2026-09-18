#!/usr/bin/env python3
"""LAYER 13 — THE CLOCK. No chapter may claim more time has passed than has passed.

WHY THIS EXISTS. The user asked, of ch62: *"gu Yue said three years so what three years passed."*
Nothing had passed. Gu Yue arrives in **ch8, week 6 at Eastsea**, and ch62 is roughly **week 50** —
she has known him about **ten months**. The prose said three years. ch57 said it twice more, and put
the same false number in **Wu Zhangkong's mouth**, a man who has taught him since ch20.

Nine separate duration claims in ch62 were wrong, and nothing caught any of them, because every
existing check reads **facts** (ranks, rings, canon quotes) and none of them read **time**.

THE CLOCK (derived from the `## Timeline:` headers, which are the authority)

    t0  ch1     Awakening Day, age 6
    +4y ch4     age 10 — leaves Glorybound for Eastsea
    +4y ch5-7   weeks 1-5 at Eastsea
    +4y ch8     week 6 — 🔴 GU YUE ARRIVES
    +4y ch9-19  weeks 7-40 — the tournament
    +4y ch20    🔴 WU ZHANGKONG BEGINS TEACHING CLASS ZERO
    +4y ch52    the new semester
    +4y ch55-60 the Skysea tournament, nine days
    +4y ch61-62 the week after

So at ch62: **4 years 11 months** since Awakening · **11 months** at Eastsea ·
**Gu Yue 10 months** · **Wu Zhangkong 8 months** · Wulin **his whole life**.

RULES ENFORCED
  1. No chapter may claim a tenure longer than the story's total elapsed time at that point.
  2. A tenure attached to **Gu Yue** may not exceed her arrival (ch8).
  3. A tenure attached to **Wu Zhangkong as teacher** may not exceed ch20.
  4. 🔴 The header timeline must stay **monotonic in age** — a chapter may not be younger than the
     one before it.

Usage:  python3 checks/verify_timeline.py [--strict]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
strict = "--strict" in sys.argv

# ---- the clock, in years from Awakening Day --------------------------------
AGE_AT = {}          # chapter -> age in years (float)
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    # 🔴 2026-08-30: this used to read the first 4,000 chars only, and the header block is
    # hand-written with no length limit — ch25's Timeline line sits at offset 5,461 and ch29's at
    # 4,075, so BOTH CHAPTERS WERE SILENTLY EXEMPT from the clock check. It reported "69
    # chapters" for a 71-chapter story and nobody noticed, because the number looked plausible.
    # A parser that returns the wrong value quietly is worse than one that crashes.
    head = open(path, encoding="utf-8", errors="replace").read(24000)
    m = re.search(r"(?im)^## Timeline:.*?\bage (\d{1,2})(?:\s*(?:→|->|to)\s*(\d{1,2}))?", head)
    if m:
        AGE_AT[n] = float(m.group(2) or m.group(1))

# ---- relationship tiers: how long each character can have been in Lin Hao's life ----
# 🔴 Lin Hao is 10. He has known Wulin and his family since before he could read (call it his
#     whole life). He met everybody at Eastsea at age 10 — under ONE year before ch62. So a
#     "for N years" relationship claim is impossible for an Eastsea character at N>=2, and
#     impossible for anybody at N>=8 (longer than a ten-year-old has been alive).
LIFELONG = {"Wulin", "Tang Wulin", "Lin Wei", "Lin Mei", "Na'er"}          # known since ~age 3
GLOWSBOUND = {"Mang Tian"}                                                  # forge master, age 7+
EASTSEA = {"Gu Yue", "Wu Zhangkong", "Xie Xie", "Xu Xiaoyan", "Zhang Yangzi", "Wang Jinxi",
           "Wei Xiaofeng", "Mu Chen", "Mu Xi", "Shen Yi", "Long Hengxu"}    # met at age 10
ROSTER = LIFELONG | GLOWSBOUND | EASTSEA
MAX_YEARS = {}
for _n in LIFELONG:   MAX_YEARS[_n] = 8      # a ten-year-old's whole life, minus infancy
for _n in GLOWSBOUND: MAX_YEARS[_n] = 4      # age 7 -> 10
for _n in EASTSEA:    MAX_YEARS[_n] = 1      # age 10 -> 10; under a year

# 🔴 Attribution by NEAREST NAME, not pronoun guessing. The first three attempts each failed a
#     different way: whole-context pronoun matching (40 false positives), name-in-line (missed
#     "she had given him nothing"), whole-body name (blamed Wulin's lifelong "watched me forge
#     for four years" on Gu Yue because her name was somewhere in the chapter). The signal that
#     actually separates them is WHICH CHARACTER stands nearest the number.
REL_MAX_DIST = 120
# a relationship-tenure verb takes an object: "known HIM", "given HIM nothing", "asked ANYBODY",
# "since I have HAD him". "known for four years" (intransitive, his own knowledge) does NOT match,
# which is exactly what keeps the adult-teacher and personal-practice false positives out.
RELATIONSHIP = re.compile(
    r"\b(?:known?|given|gave|asked|taught|told|owed|watched)\s+(?:him|her|me|you|anybody|anyone)\b|"
    r"\bsince I have had\b|\bhave had (?:him|her)\b|\bhad (?:him|her) for\b", re.I)

# a tenure phrase -> years it claims
TENURE = [
    (re.compile(r"\b(\w+?) years?\b", re.I), None),
]
WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}

fails, notes = [], []

# 🔴 CALIBRATION — measured on the first run: 40 false positives before it found anything real.
# Each class is named here because a check that cries wolf gets ignored.
#   (a) AGES ARE NOT TENURES. "six years old", "a six-year-old boy", "he was ten".
#   (b) SOUL-BEAST AND RING AGES. "a ten-year ring", "nine years of a soul", "seven hundred
#       and thirty-five years" — these are canon mechanics and routinely exceed the story clock.
#   (c) BARE COUNTS are not tenures. "three years of story time", "every three years",
#       "layered three years deep", "three years ago and who remembered" — narrative furniture.
# A TENURE is a claim that a PERSON has spent N years WITH somebody or somewhere. That requires
# the "for/in N years" construction, which is exactly the construction that broke in ch57/ch62.
# 🔴 SPLIT 2026-08-29 after the check FAILED to catch a re-inserted bug. The single 110-char
# NOT_TENURE window meant that "In three years she had given him nothing. Not one element, not
# one RING released..." was exempted by the word "ring" sitting 60 characters away in unrelated
# prose. A beast/ring AGE is a noun attached directly to the number ("a ten-year ring", "nine
# years of a soul"); it must be tested in a TIGHT window, not the whole sentence.
NOUN_AGE = re.compile(   # tested within ~18 chars of the number: what is being counted
    r"\bhawk\b|\bsoul\b|\bbeast\b|\bdragon\b|\bbird\b|\bdead\b|\bring\b|\bdagger\b|\bblade\b|"
    r"\bmetal\b|\bsteel\b|\byears? old\b|\bage \d|\b\d+[- ]years?[- ]old\b|\bwas \d+\b", re.I)
CONSTRUCTION = re.compile(   # tested wider: the shape of the phrase, not a nearby noun
    r"\bevery \w+ years?\b|\bonce every\b|\blayered\b|\bago\b|\bnotice-board\b|"
    r"\bstory time\b|\bcompressed\b|\bcanon\b|\bSpirit Pagoda\b|\bAssociation\b|\bacademy\b|"
    r"\bcity\b|\bcontinent\b|\bTang Sect\b|\bShrek\b|\bwar\b|\blegend\b|\brecord\b|\bhistory\b|"
    r"\bgrudge\b|\bpaperwork\b", re.I)

# the construction that actually broke: "<for|in> N years"
TENURE_RE = re.compile(r"\b(?:for|in)\s+(one|two|three|four|five|six|seven|eight|nine|ten|\d+)"
                       r"[- ]years?\b", re.I)

ages = [AGE_AT[n] for n in sorted(AGE_AT)]
if any(b < a for a, b in zip(ages, ages[1:])):
    bad = [(n, AGE_AT[n]) for n in sorted(AGE_AT)
           if n - 1 in AGE_AT and AGE_AT[n] < AGE_AT[n - 1]]
    fails.append(f"the Timeline headers go BACKWARD in age: {bad}")
else:
    notes.append(f"timeline headers monotonic in age across {len(AGE_AT)} chapters")

for n in sorted(AGE_AT):
    age = AGE_AT[n]
    p = open(os.path.join(CH, f"chapter_{n:02d}.md"), encoding="utf-8", errors="replace").read()
    body = p.split("## End of Chapter")[0]
    if "## Part 1" in body:
        body = body.split("## Part 1", 1)[1]

    body_offset = 0
    for line in body.split("\n"):
        for m in TENURE_RE.finditer(line):
            raw = m.group(1)
            yrs = float(raw) if raw.isdigit() else WORDS[raw.lower()]

            # 🔴 (c) FUTURE / HYPOTHETICAL is not a tenure: "you will, in ten years or twenty",
            #     "she would not find out for two years", "cheap in ten years". These describe
            #     time that has NOT passed and cannot be checked against the clock.
            tail = line[m.end():m.end() + 30]
            head = line[max(0, m.start() - 40):m.start()]
            if re.search(r"\bor (twenty|thirty|so)\b", tail) or \
               re.search(r"\b(will|would|going to|shall|before|until|next|another)\b", head, re.I):
                continue

            tight = line[max(0, m.start() - 18):m.end() + 18]   # what the number counts
            wide = line[max(0, m.start() - 60):m.end() + 60]     # the shape of the phrase
            if NOUN_AGE.search(tight) or CONSTRUCTION.search(wide):
                continue

            # 🔴 (b) GLOBAL RULE — nobody can have done anything longer than they have been alive.
            #     Everyone in class zero is 10. This replaces the old "years since Awakening" test,
            #     which fired on legitimate retrospective narration ("in four years" at age 10).
            if yrs > age + 0.5:
                fails.append(
                    f"ch{n}: \"{m.group(0).strip()}\" exceeds the character's age ({age:.0f}) — "
                    f"{ctx.strip()[:110]}")
                continue

            # 🔴 (a) PER-CHARACTER RULE — a RELATIONSHIP-tenure claim about a late arrival.
            #     The bug the user caught was "In three years she had given him nothing" and
            #     "never in three years asked Gu Yue" — claims about how long a character has
            #     been IN A RELATIONSHIP, not about that character's own lifetime. Wu Zhangkong
            #     "had known for four years" (his own knowledge, he is an adult) and Gu Yue
            #     "doing X with her eyes closed for two years" (her own practice since age 8)
            #     are NOT the bug and must not fire. So the rule needs a RELATIONSHIP verb with
            #     an object (known/given/asked/taught + him/her/me), OR the name in the clause.
            # 🔴 the RELATIONSHIP verb is MANDATORY — it is what separates the bug
            #     ("she had GIVEN HIM nothing for three years") from an adult's own knowledge
            #     ("Wu Zhangkong had KNOWN for four years") and a prodigy's own practice
            #     ("Gu Yue had been DOING X with her eyes closed for two years").
            near = line[max(0, m.start() - 45):m.end() + 25]
            if not RELATIONSHIP.search(near):
                continue
            # whose relationship is it? the nearest roster name to the number, within 120 chars
            best, bestd = None, REL_MAX_DIST + 1
            for name in ROSTER:
                for nm in re.finditer(re.escape(name), body):
                    d = abs(nm.start() - (m.start() + body_offset))
                    if d < bestd:
                        bestd, best = d, name
            if best is None or bestd > REL_MAX_DIST:
                continue
            if yrs > MAX_YEARS[best] + 0.5:
                fails.append(
                    f"ch{n}: \"{m.group(0).strip()}\" about {best}, who can have been in his life "
                    f"at most {MAX_YEARS[best]} year(s) — {near.strip()[:90]}")
        body_offset += len(line) + 1

print("verify_timeline: no chapter may claim more time has passed than has passed")
for x in notes:
    print("  ok   " + x)
for f in fails:
    print("  FAIL " + f)
if not fails:
    print(f"  0 impossible duration claims across {len(AGE_AT)} chapters")
print(f"  clock at the latest chapter: age {max(AGE_AT.values()):.0f}, "
      f"{max(AGE_AT.values()) - 6:.0f} years since Awakening")
if fails and strict:
    sys.exit(1)
sys.exit(0)
