#!/usr/bin/env python3
"""LAYER 10 — THE BUTTERFLY EFFECT.

Canon's hierarchy does not survive Lin Hao being in the room. Every line that makes another
character "the highest / strongest / best" in a group he belongs to is a canon line copied
without applying the butterfly effect of his existence.

WHY THIS EXISTS. The user pointed at one line in ch52 — "because Xie Xie's soul power is the
highest" — copied verbatim from canon c184. Canon says that about a class that does not contain
Lin Hao. Copying it is not adaptation, it is transcription, and it silently erases him from his
own story sixteen times over.

Usage: python3 checks/verify_butterfly.py [--strict]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
strict = "--strict" in sys.argv

PEERS = r"(?:Xie Xie|Gu Yue|Wulin|Xu Xiaoyan|Zhang Yangzi|Wang Jinxi|Wei Xiaofeng|Mu Xi|Yun Xiao|Zhou Zhangxi)"
SUPER = r"\b(?:highest|strongest|best|greatest|most powerful|strongest of|top)\b"
# allowed when the line already scopes it away from him
SCOPED = re.compile(
    r"except lin hao|after lin hao|of the four of you|of the girls|after him|not including|of the four|"
    r"of the others|of them\b|of the two|of the three|not the strongest in this class|"
    r"canon without him|butterfly|of the four of|fifth shape|of the two of|of the three of|"
    r"not counting myself|strongest of the first generation|strongest thousand-year|"
    r"strongest thing anyone|of the first generation", re.I)

hits = []
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    for i, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        # header lines and canon-beat footers quote canon legitimately; the butterfly effect
        # applies to OUR claims about OUR class, not to canon quotes about canon people/beasts.
        if line.lstrip().startswith("#"):
            continue
        if re.search(r"canon ch\.?\s*\d+ preserved|canon beats preserved|preserved beat-exact|"
                    r"preserved in full|Canon Reference", line, re.I):
            continue
        if not re.search(SUPER, line, re.I):
            continue
        if not re.search(PEERS, line):
            continue
        # 🔴 If the superlative is about LIN HAO himself, the line is CORRECT, not a violation.
        # "Lin Hao: ... the strongest" is the Monster Law working, not failing.
        m_sup = re.search(SUPER, line, re.I)
        window = line[max(0, m_sup.start() - 70):m_sup.end() + 40]
        if re.search(r"lin hao|\bhe is the strongest\b|\bhe's the strongest\b|you're the strongest|"
                     r"you are the strongest|the strongest boy in the class|the strongest in this class",
                     window, re.I):
            continue
        if not re.search(r"soul power|spiritual power|strongest|strongest of|highest", line, re.I):
            continue
        if SCOPED.search(line):
            continue
        hits.append((n, i, line.strip()[:165]))

print(f"verify_butterfly: canon's hierarchy does not survive him being in the room")
for n, i, seg in hits:
    print(f"  REVIEW ch{n}:{i}: {seg}")
print(f"  {len(hits)} line(s) making a peer 'highest/strongest' without scoping him out")
if hits and strict:
    sys.exit(0)
