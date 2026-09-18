#!/usr/bin/env python3
"""Rewrite the authoritative ensemble block in every chapter footer from ensemble_schedule.py.

Design decision: ONE authoritative block per chapter. Any older per-character ensemble line in the
footer is REMOVED, so the story can never contradict itself about a canon character's rank.
Prose is never touched.

Usage:  python3 checks/apply_ensemble.py
"""
import re, os, sys, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ensemble_schedule as ES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
ORDER = ["wulin", "xiexie", "guyue", "xiaoyan", "yangzi", "jinxi", "weixf"]
MARK = "### Ensemble — canon-verified state"

# footer lines carrying an ensemble member's state (replaced by the block)
ENSEMBLE_LINE = re.compile(
    r"^\s*-\s+\*\*(Tang Wulin|Xie Xie|Gu Yue|Xu Xiaoyan|Zhang Yangzi|Wang Jinxi|Wei Xiaofeng):\*\*")
# Lin Hao's own line and the adult-cast lines are kept
KEEP_LINE = re.compile(
    r"^\s*-\s+\*\*(Lin Hao|Wu Zhangkong|Mu Xi|Shen Yi|Elder Duan|Ye Xinglan|Xu Lizhi|Long Bing)")

ANCHOR = (
    "Canon position anchors for this point in the story: everyone in class zero is **10 years old** "
    "through the tournament arc (canon c221: *\"They're so young though, only ten years old!\"*); "
    "the Shrek working-student dorm holds **four** — Tang Wulin, Xie Xie, Gu Yue, Xu Xiaoyan "
    "(canon c288; + Lin Hao, AU = five invitees). Departure order: **Wei Xiaofeng left class zero "
    "first** (canon), then **Wang Jinxi transferred to another academy** (canon ch 153, staged in "
    "our ch43). **AU divergence:** in canon Zhang Yangzi transfers out with him; in this story "
    "Zhang Yangzi embraces Wang Jinxi on the steps and **stays at Eastsea Academy**, out of class "
    "zero.\n\n🔴 **REALM GAP LAW (v2.90):** every ten ranks is a wall, not a step. Lin Hao is a "
    "**Soul Elder with three purple rings**; everyone else here is rank 17–23 with two. None of "
    "them can defeat him — they can outlast him, survive him, cost him. Gu Yue does exactly that, "
    "because she is the one he cannot read."
)


def render_block(n):
    s = ES.SCHEDULE.get(n)
    if not s:
        return None
    out = [MARK, "",
           "_Single source of truth: `CHARACTER_STATS.md` §1 (canon citations) and §3 (schedule)._",
           "_Every number below traces to a canon line or is labelled AU._", ""]
    for k in ORDER:
        if k in s:
            out.append(f"- {s[k][1]}")
    out += ["", ANCHOR, ""]
    return "\n".join(out)


def main():
    report = []
    for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                       key=lambda p: int(re.search(r"(\d+)", os.path.basename(p)).group(1))):
        n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
        raw = open(path, encoding="utf-8", errors="replace").read()

        i = raw.find("### Character States:")
        if i < 0:
            report.append((n, "no footer", 0))
            continue
        head, foot = raw[:i], raw[i:]

        # 1. drop any previous authoritative block
        if MARK in foot:
            foot = foot[:foot.find(MARK)].rstrip("\n")

        # 2. strip stale per-character ensemble lines
        kept, removed = [], 0
        for line in foot.split("\n"):
            if ENSEMBLE_LINE.match(line) and not KEEP_LINE.match(line):
                removed += 1
                continue
            kept.append(line)
        foot = "\n".join(kept).rstrip("\n")

        # 3. strip orphaned continuation lines that only held ensemble ranks
        foot = re.sub(
            r"\n  \*\*(Tang Wulin|Xie Xie|Gu Yue|Xu Xiaoyan|Zhang Yangzi|Wang Jinxi|Wei Xiaofeng):\*\*[^\n]*",
            "", foot)

        blk = render_block(n)
        if blk:
            foot = foot + "\n\n" + blk + "\n"

        open(path, "w", encoding="utf-8").write(head + foot)
        report.append((n, "ok", removed))

    print(f"rewrote {len(report)} chapters; stale ensemble lines removed: {sum(r[2] for r in report)}")
    for n, st, rm in report:
        if st != "ok":
            print(f"  ch{n}: {st}")


if __name__ == "__main__":
    main()
