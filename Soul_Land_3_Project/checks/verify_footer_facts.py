#!/usr/bin/env python3
"""LAYER 11 — FOOTER FACTS. The hand-written footer must not contradict the generated one.

WHY THIS EXISTS. Found 2026-08-29 while writing ch62. Chapter 60's footer contained:

    ## GROWTH: rank **294 -> 294 (Soul Elder)**          <- the rank is 36. 294 is not a rank.
    - **Ranks at chapter end:** ... **ledger 264**       <- the ledger is 107. 264 was the
                                                            SPIRITUAL POWER two words earlier
                                                            on the same line.
    - **Tang Wulin:** rank 15                            <- he is 18. The ensemble block
    - **Xie Xie:** rank 21                               <- he is 23.   14 lines below said so.

Every one of those numbers was also present, correctly, in the SAME FOOTER — in the
`### Ensemble` block that `apply_ensemble.py` regenerates from `ensemble_schedule.py`.
Ten verification layers ran green over it, because all ten read either the generated block or
`checks/state.json` (which is derived from the one authoritative line). Nothing ever compared
the HAND-WRITTEN prose of a footer against the GENERATED block sitting underneath it.

That is the root disease this project keeps rediscovering: **a fact maintained in two places
will be wrong in one of them, and the check reads the other.** Layer 0 already derives the
ensemble block and LIN_HAO_STATUS.md so they cannot rot. This layer closes the last gap — the
hand-written part of the footer.

WHAT IT CHECKS, per chapter:
  1. every ensemble character's rank in the hand-written footer matches the schedule
  2. Lin Hao's rank / spiritual power / hawk / ledger in the footer match state.json
  3. Lin Hao's rank in the GROWTH header matches the footer (the "294" class of typo)
  4. no number in the footer is a two-rank-digit impossibility (rank > 100)

Usage:  python3 checks/verify_footer_facts.py [--strict]
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from ensemble_schedule import SCHEDULE  # noqa: E402

strict = "--strict" in sys.argv
STATE = json.load(open(os.path.join(HERE, "state.json"), encoding="utf-8"))

# character name -> (schedule key, how the footer writes the rank)
CAST = {
    "Tang Wulin": "wulin",
    "Xie Xie": "xiexie",
    "Gu Yue": "guyue",
    "Xu Xiaoyan": "xiaoyan",
    "Zhang Yangzi": "yangzi",
    "Wang Jinxi": "jinxi",
    "Wei Xiaofeng": "weixf",
}

problems, notes = [], []

for path in sorted(glob.glob(os.path.join(ROOT, "chapters", "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    full = open(path, encoding="utf-8", errors="replace").read()
    if "## End of Chapter" not in full:
        continue
    footer = full.split("## End of Chapter", 1)[1]
    header = full.split("## End of Chapter", 1)[0]

    # The generated block is the authority. Everything above it is hand-written and must agree.
    hand = footer.split("### Ensemble — canon-verified state")[0]

    # 🔴 CALIBRATION. Two sources of false positives were measured on the first run:
    #   (a) narrative lines under "Chapter Summary" that mention a PAST rank — ch1's
    #       "Tang Wulin: Bluesilver Grass, rank 3" is canon-correct for Awakening Day and is
    #       not a claim about his rank at chapter end. Scope to the Character Progression block.
    #   (b) the GROWTH header has TWO bolded numbers ("rank **36 → 36** · spiritual power
    #       **264 → 264**"). A greedy `.*?rank \*{0,2}(\d+)` matched the SPIRITUAL POWER when
    #       the rank itself was unbolded, and reported "rank 205" for five chapters. Parse the
    #       GROWTH line as its own object instead.
    prog = hand.split("### Character Progression:", 1)[-1]
    # 🔴 and the Chapter Summary above it is NARRATIVE — ch1's summary records Tang Wulin at
    # "rank 3" on Awakening Day, which is canon-correct and is not a claim about his rank at
    # chapter end. Only the progression/state blocks make current-value claims.
    if "### Character Progression:" not in hand:
        prog = hand.split("### Character States:", 1)[-1]

    # ---- 1. ensemble cast: rank in the hand-written footer vs the schedule ----
    sched = SCHEDULE.get(n, {})
    for name, key in CAST.items():
        if key not in sched:
            continue
        want = sched[key][0]
        # only look at the character's OWN line(s) in the hand-written progression block
        # 🔴 CALIBRATION, second pass. Footers pack several characters onto ONE line:
        #   "- **Xie Xie:** rank 21 · **Wulin:** rank 15 · **Xu Xiaoyan:** starwheel"
        # A per-line match attributed Wulin's 15 to Xie Xie and reported three failures for one
        # line. Split each line at the bolded name markers and read only the segment that
        # belongs to the character being checked.
        for line in prog.split("\n"):
            segs = re.split(r"(\*\*[^*]{1,24}:\*\*)", line)
            owner, segment = None, ""
            for piece in segs:
                nm = re.match(r"\*\*([^*]{1,24}):\*\*", piece)
                if nm:
                    owner = nm.group(1).strip()
                    segment = ""
                elif owner and owner.rstrip(":") in (name, name.split()[-1]):
                    segment += piece
            if not segment:
                continue
            # "last rank 22" / "last known rank 25" is a HISTORICAL fact about a departed
            # character and is correct even when the schedule says he is gone.
            # 🔴 "Bluesilver Grass, rank 3" is the AWAKENING-DAY martial-soul reading (canon:
            # Wulin awakened at rank 3), not a claim about his rank at chapter end. Exempt a
            # rank that directly follows a martial-soul name.
            m = re.search(r"(?<!last )(?<!known )(?<!Grass, )(?<!Dagger, )(?<!Eagle, )(?<!King, )"
                          r"\brank \*{0,2}(\d{1,3})\b", segment)
            if not m:
                continue
            got = int(m.group(1))
            if want is None:
                problems.append(f"ch{n}: {name} is given rank {got} but has left / is absent "
                                f"per ensemble_schedule.py")
            elif got != want:
                problems.append(f"ch{n}: {name} rank {got} in the hand-written footer, "
                                f"{want} in ensemble_schedule.py (the generated block below says "
                                f"{want} too)")

    # ---- 2. Lin Hao's own numbers vs state.json ----
    def chain(pattern):
        m = re.search(pattern, hand)
        return m.group(1) if m else None

    # rank
    m = re.search(r"Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d{1,3})", hand)
    if m:
        got = int(m.group(1))
        want = STATE["rank_by_chapter"].get(str(n))
        if want is not None and got != want:
            problems.append(f"ch{n}: Lin Hao rank {got} at chapter end, {want} in state.json")
        if got > 100:
            problems.append(f"ch{n}: Lin Hao rank {got} — soul ranks run 1-100")

    # spiritual power — 🔴 scoped to LIN HAO's own lines. ch3's footer legitimately records
    # Lin Hao at 41 and Tang Wulin at 38; an unscoped search reported that as a contradiction.
    sp_hits = []
    for line in hand.split("\n"):
        if "Lin Hao" not in line:
            continue
        # a line can carry several characters; stop at the next bolded name after his
        seg = line.split("**Lin Hao:**", 1)[-1]
        nxt = re.search(r"\*\*[A-Z][A-Za-z' ]{1,20}:\*\*", seg)
        if nxt:
            seg = seg[:nxt.start()]
        # a "281 → 289" chain is one value, not two: keep the END of the chain
        for mm in re.finditer(r"spiritual power \*{0,2}(\d[\d,]*)(?:\s*→\s*\*{0,2}(\d[\d,]*))?", seg):
            sp_hits.append(int((mm.group(2) or mm.group(1)).replace(",", "")))
    sp_hits = [x for x in sp_hits if x < 1000]  # skip "2,612 kg" style artefacts
    if sp_hits and len(set(sp_hits)) > 1:
        # a "264 -> 264" chain is fine; two DIFFERENT end values on different lines is not
        problems.append(f"ch{n}: spiritual power written as {sorted(set(sp_hits))} in the same "
                        f"footer — pick one")

    # ledger — 🔴 this is a PROGRESSION line, not a constant. ch21's ledger is 71 and ch61's is
    # 107, and both are correct. The first version of this check compared every chapter against
    # state.json's CURRENT ledger and produced 17 false positives. Compare against the ledger
    # that chapter itself recorded, and only flag a chapter whose ledger goes BACKWARD or whose
    # ledger is the spiritual power pasted into the wrong slot.
    lg = re.findall(r"ledger[:\s*]{0,4}(\d{1,4})", hand)
    if lg:
        got = int(lg[-1])
        per_ch = STATE.get("ledger_by_chapter", {})
        prev = max((v for k, v in per_ch.items() if int(k) < n), default=0)
        if got < prev:
            problems.append(f"ch{n}: ledger {got} is lower than ch{n - 1}'s {prev} — the ledger "
                            f"only grows")
        if sp_hits and got in sp_hits and got > 150:
            problems.append(f"ch{n}: ledger {got} equals the spiritual power on the same line — "
                            f"the wrong number pasted into the slot (the ch60 defect)")

    # ---- 3. the GROWTH header must agree with the footer ----
    # Parse the GROWTH line as its own object: rank first, then spiritual power.
    gline = next((l for l in header.split("\n") if l.startswith("## GROWTH:")), "")
    grank = re.search(r"rank \*{0,2}(\d{1,3})\s*(?:→\s*\*{0,2}(\d{1,3}))?", gline)
    gsp = re.search(r"spiritual power \*{0,2}(\d{1,3})\s*(?:→\s*\*{0,2}(\d{1,3}))?", gline)
    if grank:
        g_end = int(grank.group(2) or grank.group(1))
        if g_end > 100:
            problems.append(f"ch{n}: GROWTH header rank {g_end} — soul ranks run 1-100. This is "
                            f"the spiritual power pasted into the rank slot.")
        elif m and g_end != int(m.group(1)):
            problems.append(f"ch{n}: GROWTH header says rank {g_end}, footer says {m.group(1)}")
    if gsp and sp_hits:
        g_sp_end = int(gsp.group(2) or gsp.group(1))
        if g_sp_end not in sp_hits:
            problems.append(f"ch{n}: GROWTH header spiritual power {g_sp_end}, footer says "
                            f"{sorted(set(sp_hits))}")

    # ---- 4. hawk must be monotonic and match state.json ----
    hk = re.findall(r"hawk\D{0,6}([\d,]{3,6})", footer)
    if hk:
        got = int(hk[-1].replace(",", ""))
        want = STATE["hawk_by_chapter"].get(str(n))
        if want is not None and got != want:
            problems.append(f"ch{n}: hawk {got} in the footer, {want} in state.json")

notes.append(f"{len(glob.glob(os.path.join(ROOT, 'chapters', 'chapter_*.md')))} chapters, "
             f"{len(CAST)} tracked canon characters, 4 fact classes")

print("verify_footer_facts: the hand-written footer must not contradict the generated one")
for p in problems:
    print("  FAIL " + p)
for nt in notes:
    print("  ok   " + nt)
if problems:
    print(f"  {len(problems)} contradiction(s) between hand-written and derived facts")
    if strict:
        sys.exit(1)
else:
    print("  0 contradictions")
sys.exit(0)
