#!/usr/bin/env python3
"""
SOUL LAND UNIVERSAL KIT — gate self-test.   **v2, 2026-09-20**

Usage:
    python3 tools/selftest.py

Builds throwaway chapters that each contain exactly one known defect, runs
verify.py over them, and confirms every defect is caught. Then builds clean
chapters and confirms they pass.

Why this file exists
    A gate that passes everything verifies nothing. verify.py was once run on a
    proven 33,000-word serial and reported 15 failures, all of them false
    positives from an over-broad rule. Nothing caught that except a hand-built
    negative test. This script is that test, permanently.

Why v2 added the apparatus cases
    v1 classified the chapter's title, metadata head and bookkeeping tail as
    prose, so it failed all 230 chapters in the corpus for digits the story
    never wrote. Fixing that meant teaching the gate where apparatus ends -- and
    an exemption is exactly the kind of edit that silently swallows real
    defects. So the boundary is red-tested in BOTH directions:

        digits in the head or tail   -> must PASS
        digits in the story          -> must still FAIL
        CJK in the head or tail      -> must still FAIL  (whole-file gate)
        emoji in the tail            -> must still FAIL  (whole-file gate)

    A rule that only ever gets tested in the direction that makes it convenient
    is not a rule.

Exits 0 only when every defect is caught AND every clean chapter passes.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.join(HERE, "verify.py")

MARKER = "\u25c6"
ENDASH = "\u2013"
EMDASH = "\u2014"
NL = chr(10)

# A minimal chapter that satisfies all seven gates. Every defect fixture is this
# text with exactly one corruption applied, so a failure can only mean the gate
# missed that corruption.
CLEAN = (
    "# Chapter 1 " + EMDASH + " The Clean One" + NL + NL
    + "```" + NL
    + MARKER + " STATUS " + EMDASH + " Chapter 1: years 0" + ENDASH + "1" + NL
    + "KIND      : a test subject" + NL
    + "AGE       : six" + NL
    + "CLASS     : none" + NL
    + "THREAT    : a recruiter" + NL
    + "```" + NL + NL
    + "---" + NL + NL
    + "The man came to the door." + NL + NL
    + '"Your name," he said.' + NL + NL
    + '"Lin," the boy said.' + NL + NL
    + '"Lin what."' + NL + NL
    + '"Just Lin."' + NL + NL
    + "The man wrote it down. "
    '"Innate soul power four," he said. "That is enough to matter."' + NL + NL
    + '"It is not nothing," the boy said.' + NL + NL
    + '"No," said the man. "It is not nothing."' + NL + NL
    + "---" + NL
)

# A chapter shaped like the real corpus: title + metadata head + story + a
# bookkeeping tail carrying digits, dates and panel-map numbers in the
# apparatus, and NOT ONE digit in the story itself.
REAL_HEAD = (
    "# Chapter 21: Round One" + NL + NL
    + "## Canon Reference: Novel ch 17-2/3 (the dual-control spar continued)"
    + " -- held whole" + NL
    + "## Timeline: Assessment day one, afternoon" + NL + NL
    + "---" + NL + NL
)
REAL_BODY = (
    "Wang Dong at thirty meters, wings lit, one yellow ring and one purple."
    + NL + NL
    + '"Left foot," the boy said.' + NL + NL
    + '"What about it."' + NL + NL
    + '"It leaves its foundation."' + NL + NL
    + "The spar turned on that one sentence." + NL
)
REAL_TAIL = (
    NL + "---" + NL + NL
    + "## End of Chapter 21" + NL + NL
    + "### Chapter Summary:" + NL
    + "- **Panel map (5 panels):** the spar, the room, the stall" + NL
    + "### Canon Preserved / Butterfly Effects:" + NL
    + "- Canon: the monitor switch, held" + NL
    + "### Character States (End of Chapter 21):" + NL
    + "- **Jiang Che:** Rank 25, two rings, 4,500 words audited" + NL
    + "- **Written:** 2026-08-26" + NL
)
REAL = REAL_HEAD + REAL_BODY + REAL_TAIL

# SL4-shaped: no metadata head at all -- title, story, then a "## Footer".
SL4_SHAPED = (
    "# Chapter 4: The Bell" + NL + NL
    + REAL_BODY
    + NL + "---" + NL + NL
    + "## Footer" + NL
    + "- Project state: Chapter 4 written, 4200 words." + NL
    + "- Canon span touched: Soul Land 4 opening, 12 beats held." + NL
)

# blue_silver-shaped: the apparatus is an italic paragraph after the last rule,
# with no heading to find it by.
BS_SHAPED = (
    "# Chapter Two " + EMDASH + " What the Water Teaches" + NL + NL
    + REAL_BODY
    + NL + "---" + NL + NL
    + "*Chapter footer " + EMDASH + " Position: year one of the blade's life; "
    + "deep era (~800 years before the original story). Canon touched: Blue "
    + "Silver Grass is the continent's commonest weed [canon].*" + NL
)

# A story that genuinely ends on a scene-break rule and a closing paragraph.
# There is no apparatus signal, so this paragraph is STORY and a digit in it
# must fail. This is what keeps the keyword rule load-bearing.
# Names are digits that are not measurements: Room 108 (SL2), Dorm333 (SL4).
# These must PASS; a measurement like "rank 29" must still fail.
NAME_OK = (
    "# Chapter 30: The Rooms" + NL + NL
    + "The week that followed found room 108's rhythm, and the rhythm had three beats."
    + NL + NL
    + '"Same bed, every night," the courier said.' + NL + NL
    + '"Same room, every year." Dorm333 had a reputation by then.' + NL + NL
    + "They did not move." + NL
    + '"Why move," the fox said, "when the room fits."' + NL
)
MEASURE_BAD = NAME_OK.replace("Dorm333 had a reputation by then.",
                              "He was rank 29 by then, which was not the point.")
SCENE_CLOSE = (
    "# Chapter 9: The Last Vigil" + NL + NL
    + REAL_BODY
    + NL + "---" + NL + NL
    + "The bell rang 3 times before dawn." + NL
)


def _set_panel(text, lo, hi):
    """Rewrite the panel's year range."""
    return re.sub(
        r"years \d+" + ENDASH + r"\d+",
        "years " + str(lo) + ENDASH + str(hi),
        text,
        count=1,
    )


def d_digits(t):
    return t.replace("The man came to the door.",
                     "The man came to the door in year 163 with 3 others.")


def d_cjk(t):
    return t.replace("The man came to the door.",
                     "The man came to the door " + "\u84dd\u94f6\u8349")


def d_nodialogue(t):
    return t.replace('"', "")


def d_placeholder(t):
    return t.replace("The man came to the door.",
                     "TODO: <fill this in> the man came to the door.")


def d_backslash_n(t):
    return t.replace("The man came to the door.",
                     "The man came to the door." + chr(92) + "nHere.")


def d_marker_in_prose(t):
    return t.replace("The man came to the door.",
                     MARKER + " The man came to the door.")


def d_two_cards(t):
    return (t
            + "```" + NL + MARKER + " END OF BOOK TWO" + NL + "```" + NL + NL
            + "```" + NL + MARKER + " END OF BOOK THREE" + NL + "```" + NL)


# --- v2 apparatus cases -----------------------------------------------------
def d_real_digits_in_story(t):
    """Apparatus digits are fine; a digit in the STORY must still be caught."""
    return t.replace("The spar turned on that one sentence.",
                     "The spar turned in 3 seconds.")


def d_real_cjk_in_head(t):
    """Head is apparatus for gates 3/4/7 -- but gate 1 is whole-file."""
    return t.replace("## Timeline: Assessment day one, afternoon",
                     "## Timeline: Assessment day one, afternoon \u521d\u7aa5")


def d_real_emoji_in_tail(t):
    """The corpus carries marks like these in tails; they are still unreadable."""
    return t.replace("- Canon: the monitor switch, held",
                     "- \u2705 Canon: the monitor switch, held")


def d_real_cjk_in_story(t):
    return t.replace("The spar turned on that one sentence.",
                     "The spar turned on that one sentence \u7075\u529b.")


DEFECTS = [
    ("digits in prose", "d_digits", "digits in prose"),
    ("unreadable script", "d_cjk", "unreadable script"),
    ("no dialogue", "d_nodialogue", "spoken dialogue lines"),
    ("placeholder text", "d_placeholder", "placeholder text"),
    ("literal backslash-n", "d_backslash_n", "backslash-n"),
    ("marker leaked to prose", "d_marker_in_prose", "panel marker in prose"),
    ("two book-end cards", "d_two_cards", "marker cards"),
]

APPARATUS_DEFECTS = [
    ("digits in the STORY of a real-shaped chapter",
     "d_real_digits_in_story", "digits in prose"),
    ("CJK in the metadata head", "d_real_cjk_in_head", "unreadable script"),
    ("emoji mark in the bookkeeping tail", "d_real_emoji_in_tail",
     "unreadable script"),
    ("CJK in the STORY", "d_real_cjk_in_story", "unreadable script"),
]


def run_verify(*args):
    r = subprocess.run(
        [sys.executable, VERIFY] + list(args),
        capture_output=True, text=True,
    )
    return r.returncode, r.stdout + r.stderr


def main():
    if not os.path.exists(VERIFY):
        print("selftest: cannot find verify.py next to this file")
        return 1

    tmp = tempfile.mkdtemp(prefix="sl_selftest_")
    failures = []
    try:
        # ---- 1. the clean chapter must PASS --------------------------------
        d = os.path.join(tmp, "clean")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_01_Clean.md"), "w", encoding="utf-8") as fh:
            fh.write(CLEAN)
        rc, out = run_verify(d)
        if rc != 0:
            failures.append(
                "clean chapter FAILED the gate (false positive)" + NL
                + "".join("    " + l + NL for l in out.splitlines() if "FAIL" in l)
            )
        else:
            print("  ok    clean chapter passes")

        # ---- 2. each defect must be caught, alone --------------------------
        for i, (name, fn_name, needle) in enumerate(DEFECTS):
            mutate = globals()[fn_name]
            d = os.path.join(tmp, "d%d" % i)
            os.makedirs(d)
            bad = mutate(_set_panel(CLEAN, 100 + i, 199 + i))
            with open(os.path.join(d, "Chapter_01_Defect.md"), "w",
                      encoding="utf-8") as fh:
                fh.write(bad)
            rc, out = run_verify(d)
            if rc == 0:
                failures.append("NOT CAUGHT: " + name + " (gate returned PASS)")
            elif needle not in out:
                failures.append(
                    "caught for the wrong reason: " + name
                    + NL + "    expected a complaint containing " + repr(needle)
                )
            else:
                print("  ok    caught: " + name)

        # ---- 3. contiguity: overlap and gap --------------------------------
        d = os.path.join(tmp, "contig")
        os.makedirs(d)
        for n, (lo, hi) in enumerate([(0, 10), (10, 20), (18, 30)]):
            with open(os.path.join(d, "Chapter_%02d_X.md" % (n + 1)), "w",
                      encoding="utf-8") as fh:
                fh.write(_set_panel(CLEAN, lo, hi))
        rc, out = run_verify(d)
        if "OVERLAP" not in out:
            failures.append("panel OVERLAP not detected")
        else:
            print("  ok    caught: panel overlap")

        d = os.path.join(tmp, "gap")
        os.makedirs(d)
        for n, (lo, hi) in enumerate([(0, 10), (25, 30)]):
            with open(os.path.join(d, "Chapter_%02d_X.md" % (n + 1)), "w",
                      encoding="utf-8") as fh:
                fh.write(_set_panel(CLEAN, lo, hi))
        rc, out = run_verify(d)
        if "GAP" not in out:
            failures.append("panel GAP not detected")
        else:
            print("  ok    caught: panel gap")

        # ---- 4. v2: the apparatus boundary, both directions -----------------
        d = os.path.join(tmp, "real_clean")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_21_Round_One.md"), "w",
                  encoding="utf-8") as fh:
            fh.write(REAL)
        rc, out = run_verify(d)
        if rc != 0:
            failures.append(
                "corpus-shaped chapter FAILED (apparatus digits read as prose)"
                + NL + "".join("    " + l + NL for l in out.splitlines()
                               if "FAIL" in l)
            )
        else:
            print("  ok    apparatus digits/tail do not fail (the v1 defect)")

        for i, (name, fn_name, needle) in enumerate(APPARATUS_DEFECTS):
            mutate = globals()[fn_name]
            d = os.path.join(tmp, "r%d" % i)
            os.makedirs(d)
            with open(os.path.join(d, "Chapter_21_X.md"), "w",
                      encoding="utf-8") as fh:
                fh.write(mutate(REAL))
            rc, out = run_verify(d)
            if rc == 0:
                failures.append("NOT CAUGHT: " + name)
            elif needle not in out:
                failures.append(
                    "caught for the wrong reason: " + name
                    + NL + "    expected " + repr(needle)
                )
            else:
                print("  ok    caught: " + name)

        # ---- 5. v2: the two apparatus shapes found in the corpus ------------
        for label, fixture in (("SL4shaped", SL4_SHAPED),
                               ("bluesilver", BS_SHAPED)):
            d = os.path.join(tmp, "shape_" + label)
            os.makedirs(d)
            with open(os.path.join(d, "Chapter_X.md"), "w", encoding="utf-8") as fh:
                fh.write(fixture)
            rc, out = run_verify(d)
            if rc != 0:
                failures.append("apparatus not recognised: " + label
                                + NL + "".join("    " + l + NL
                                               for l in out.splitlines() if "FAIL" in l))
            else:
                print("  ok    apparatus recognised: " + label)

        # the keyword rule must stay load-bearing
        d = os.path.join(tmp, "scene_close")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_09.md"), "w", encoding="utf-8") as fh:
            fh.write(SCENE_CLOSE)
        rc, out = run_verify(d)
        if rc == 0 or "digits in prose" not in out:
            failures.append(
                "a closing paragraph with no apparatus signal was exempted "
                "(digits in the story not caught)")
        else:
            print("  ok    a closing paragraph with no apparatus signal is still story")

        # names pass, measurements still fail
        d = os.path.join(tmp, "names_ok")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_30.md"), "w", encoding="utf-8") as fh:
            fh.write(NAME_OK)
        rc, out = run_verify(d)
        if rc != 0:
            failures.append("name-digits (Room 108 / Dorm333) failed the gate"
                            + NL + "".join("    " + l + NL
                                           for l in out.splitlines() if "FAIL" in l))
        else:
            print("  ok    name-digits (Room 108, Dorm333) pass")

        d = os.path.join(tmp, "measure_bad")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_31.md"), "w", encoding="utf-8") as fh:
            fh.write(MEASURE_BAD)
        rc, out = run_verify(d)
        if rc == 0 or "digits in prose" not in out:
            failures.append("a measurement digit (rank 29) passed the gate")
        else:
            print("  ok    measurement digits (rank 29) still fail")

        # ---- 6. v2: project mode -------------------------------------------
        root = os.path.join(tmp, "proj")
        os.makedirs(os.path.join(root, "chapters"))
        os.makedirs(os.path.join(root, "foundation"))
        with open(os.path.join(root, "chapters", "chapter_01.md"), "w",
                  encoding="utf-8") as fh:
            fh.write(REAL)
        # a doc that legitimately carries CJK glosses and regex escapes
        with open(os.path.join(root, "foundation", "CANON_LEDGER.md"), "w",
                  encoding="utf-8") as fh:
            fh.write("# ledger" + NL + "Jiang Che (\u6c5f\u6f88)" + NL
                     + "banned pattern: `Lan[^" + chr(92) + "n]{0,120}`" + NL)
        rc, out = run_verify("--project", root)
        if rc != 0:
            failures.append("project mode failed on a clean project"
                            + NL + "".join("    " + l + NL
                                           for l in out.splitlines() if "VERDICT" in l))
        else:
            print("  ok    project mode: doc CJK + regex escapes are advisory, not fatal")

        with open(os.path.join(root, "chapters", "chapter_02.md"), "w",
                  encoding="utf-8") as fh:
            fh.write(REAL.replace("Round One", "Round Two")
                     .replace("Wang Dong at thirty meters",
                              "Wang Dong at thirty meters \u7075\u529b"))
        rc, out = run_verify("--project", root)
        if rc == 0 or "cjk in chapters" not in out:
            failures.append("project mode did not fail on CJK in a chapter")
        else:
            print("  ok    project mode: CJK in a chapter is fatal")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("-" * 64)
    if failures:
        print("SELFTEST FAILED " + EMDASH + " verify.py is not trustworthy:")
        for f in failures:
            print("  " + f)
        return 1
    print("SELFTEST PASSED " + EMDASH + " all defects caught, clean chapters pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
