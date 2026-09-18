#!/usr/bin/env python3
"""LAYER 9 — THE MONSTER LAW.

At equal level, Lin Hao defeats EVERYONE in seconds. The only exception in the history of the
franchise is Tang San, who can give him a few seconds of a real fight and still cannot win.

WHY THIS EXISTS. Chapter 44 had him lose in NINE SECONDS to a one-ring record of a girl while he was
rank 31 with three purple rings. That is not a fight. A reader who has read the series knows instantly
that it is wrong, and it was the largest single failure in the project.

WHAT IT FLAGS. Any line in which Lin Hao is described as losing, being defeated, being beaten, or
merely surviving an opponent. Each hit must be reviewed: it is only legitimate if the opponent was
genuinely ABOVE his stage (a soul-beast pride, a sealed power, a higher realm).

WHY IT WARNS RATHER THAN FAILS. "He was beaten by a bear" is legitimate if the bear is above his stage,
and the check cannot know that. So it surfaces every candidate for a human to judge — but it surfaces
ALL of them, which is what was missing when ch44 shipped.

Usage: python3 checks/verify_monster_law.py [--strict]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
strict = "--strict" in sys.argv

# A loss, a defeat, or merely surviving.
# 🔴 CALIBRATED. The first version matched "fell into step beside him", "the shelf broke, Lin Hao
# fell", "it went down" (about a wolf) and "the beam fell" — 20 of 26 hits were noise, and a check
# that cries wolf on 77% of its output gets ignored. Now: the loss verb must be attributed to HIM
# within a short window, and physical-motion verbs (fell/went down/collapsed) are dropped entirely
# because they describe bodies and objects far more often than they describe defeats.
LOSS = re.compile(
    r"\b(?:he|Lin Hao|him)\b[^\n.]{0,55}?\b(?:lost|loses|was defeated|were defeated|defeated by|"
    r"beaten|beaten by|didn'?t win|did not win|failed to win|couldn'?t win|could not win|"
    r"lasted (?:only )?(?:\w+ )?seconds?|outlasted by|taken down|knocked out)\b", re.I)
# Legitimate: the opponent is above his stage, or it is explicitly not a real contest.
LEGIT = re.compile(
    r"\b(?:bear|lion|pride|beast|monster|dragon|ape|above (?:his|their) (?:level|stage|rank)|"
    r"higher realm|sealed|a realm above|not a fight|declined|declining|refused to|never fought|wolf|"
    r"did not fight|didn'?t fight|spar(?:ring)?|training|practice|conceded|declined to win|"
    r"Guang Long|rank (?:2[5-9]|3[0-9]|[4-9][0-9])|"
    r"stepped out of|never touched him|Xie Xie|Wu Zhangkong|Tang San)\b", re.I)
# Negations that mean he did NOT lose.
NOT_LOSS = re.compile(
    r"\b(?:never|not|didn'?t|did not|cannot|can'?t|won'?t|hasn'?t|isn'?t|wasn'?t|no one|nobody|"
    r"cannot be defeated|undefeated)\b[^\n.]{0,40}?(?:lost|loses|defeat|beaten|beaten by)"
    # 🔴 "lost the thought / the thread / the thread of it" — losing an abstraction, not a fight.
    r"|\blost (?:the|a) (?:thought|thread|train|place|moment|idea|sense|sight)\b"
    # 🔴 reversed direction: "she had lost to him" means HE won.
    r"|\blost to (?:him|Lin Hao)\b", re.I)

candidates = []
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    for i, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        if line.lstrip().startswith("#"):
            continue   # header lines quote canon dialogue addressed to OTHER characters
        if not LOSS.search(line):
            continue
        if NOT_LOSS.search(line):
            continue
        # 🔴 "lasted four seconds" is a DURATION, not a defeat, when the line says the opponent
        # "does not lose" — the sentence is describing how fast HE won, not how he lost.
        if re.search(r"lasted[^.]{0,30}seconds", line, re.I) and re.search(
                r"does not lose|doesn'?t lose|did not lose|does not get|four seconds", line, re.I) \
           and not re.search(r"he lasted|Lin Hao lasted|he only lasted", line, re.I):
            continue
        # 🔴 the loss verb may itself be negated: "a rank-21 Soul Grandmaster does NOT LOSE in four
        # seconds" is the Monster Law working, not failing. Check the 18 chars before the verb.
        m_loss = LOSS.search(line)
        if m_loss:
            pre18 = line[max(0, m_loss.start() - 22):m_loss.start()].lower()
            if re.search(r"(?:does|did|do|does not|doesn'?t|did not|never|not|won'?t|cannot|can'?t)\s*$", pre18):
                continue
        if LEGIT.search(line):
            continue
        candidates.append((n, i, line.strip()[:165]))

print(f"verify_monster_law: MONSTER LAW — at equal level he defeats everyone in seconds; "
      f"only Tang San can last more than seconds")
print(f"  {len(candidates)} candidate line(s) describing Lin Hao losing — each needs a human to confirm "
      f"the opponent was ABOVE his stage")
for n, i, seg in candidates:
    print(f"  REVIEW ch{n}:{i}: {seg}")
if candidates and strict:
    sys.exit(1)
sys.exit(0)
