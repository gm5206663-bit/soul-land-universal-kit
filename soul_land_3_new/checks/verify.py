#!/usr/bin/env python3
"""soul_land_3_new — the no-mistake chapter gate. Stdlib only.

Usage:
    python3 checks/verify.py             gate the real serial (chapters/ + STATUS_PANEL)
    python3 checks/verify.py --selftest  prove the gate still catches known defects

Gates (in order):
  1 rulings   no chapters while Ruling R1 or R2 is **OPEN**
  2 sequence  chapters/Chapter_NN_*.md strictly sequential from 01
  3 footer    every chapter ends with the SYNC mirror record (R5)
  4 length    900..3400 words (BUDGET-EXTENDED footer escape, RAILS prose 5)
  5 sentences avg <= 25.5 words; none over 60 (measured house grammar)
  6 dialogue  >= 5 spoken lines per 1000 words (DIALOGUE: SKIP escape, prose 3)
  7 banned    incident tokens + zero-CJK (rail 8)
  8 spine     >= 1 canon anchor per chapter (SPINE: NONE escape, story law 1)
  9 panel     STATUS_PANEL sections + latest-chapter sync (rail 3)
"""
import re, sys, os, tempfile

GATE_NAME = "sl3-new-gate v1.0 (2026-09-22)"
MIN_WORDS, MAX_WORDS = 900, 3400
AVG_SENT_FAIL, AVG_SENT_WARN = 25.5, 25.0
MAX_SENT_WORDS = 60
DIALOGUE_PER_1000 = 5.0

BANNED = [
    "Dawnflame 1,120", "Dawn-Iron 2,040",   # Fire Phoenix stale-edge incident tokens
    "lorem ipsum", "TODO", "FIXME", "XXX",
]
SPINE_ANCHORS = [
    "wulin", "shrek", "spirit pagoda", "pagoda", "eastsea", "spirit soul",
    "battle armor", "mecha", "federation", "holy spirit cult", "star luo",
    "dou spirit", "blacksmith", "fusion forging", "sea god pavilion", "gu yue",
    "xie xie", "blood god legion", "abyss", "soul rank", "rank ", "ring",
]
PANEL_SECTIONS = [
    "## 1. LIVE EDGE", "## 2. POWER & NUMBERS", "## 3. OPEN THREADS",
    "## 4. FIREWALLS", "## 5. NEXT ACTIONS",
]
FOOTER_MARK = "SYNC:"
CJK = re.compile(r"[぀-ヿ一-鿿㐀-䶿]")


def _words(text):
    return re.findall(r"[A-Za-z0-9'\u2019-]+", text)


def _split_prose_footer(text):
    """Return (prose_lines, footer_lines): footer starts at first SYNC: line."""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if ln.strip().startswith(FOOTER_MARK):
            return lines[:i], lines[i:]
    return lines, []


def _sentences(prose_lines):
    body = " ".join(l.strip("#> \t") for l in prose_lines if l.strip())
    raw = re.split(r"(?<=[.!?])\s+", body)
    return [s for s in raw if len(_words(s)) > 0]


def _spoken_lines(prose_lines):
    return sum(1 for l in prose_lines if re.search(r'"[^"\n]*"', l))


def find_chapters(chapters_dir):
    out = []
    if os.path.isdir(chapters_dir):
        for f in sorted(os.listdir(chapters_dir)):
            m = re.match(r"Chapter_(\d+)_.+\.md$", f)
            if m:
                out.append((int(m.group(1)), os.path.join(chapters_dir, f)))
    return out


def check_rulings(root, has_chapters, errors):
    p = os.path.join(root, "foundation", "OPEN_RULINGS.md")
    if not os.path.exists(p):
        errors.append("rulings: foundation/OPEN_RULINGS.md missing")
        return
    if not has_chapters:
        return
    for rid in ("R1", "R2"):
        line = next((l for l in open(p, encoding="utf-8")
                     if l.strip().startswith("| " + rid)), "")
        if "**OPEN**" in line:
            errors.append(
                f"rulings: {rid} still **OPEN** but chapters exist — drafting is locked "
                f"(see OPEN_RULINGS.md + README)")


def check_sequence(chapters, errors):
    nums = [n for n, _ in chapters]
    want = list(range(1, len(nums) + 1))
    if nums != want:
        errors.append(f"sequence: chapter numbers {nums} != sequential {want}")


def check_length(path, prose_lines, footer_lines, errors):
    n = len(_words(" ".join(prose_lines)))
    if n > MAX_WORDS and not any(l.strip().startswith("BUDGET-EXTENDED:") for l in footer_lines):
        errors.append(f"length: {os.path.basename(path)} = {n} words > {MAX_WORDS} "
                      f"(scope law; declare BUDGET-EXTENDED: <reason> in footer)")
    if n < MIN_WORDS:
        errors.append(f"length: {os.path.basename(path)} = {n} words < {MIN_WORDS}")
    return n


def check_sentences(path, prose_lines, errors, warnings):
    sents = _sentences(prose_lines)
    if not sents:
        return
    avg = sum(len(_words(s)) for s in sents) / len(sents)
    over = [len(_words(s)) for s in sents if len(_words(s)) > MAX_SENT_WORDS]
    if avg > AVG_SENT_FAIL:
        errors.append(f"sentences: {os.path.basename(path)} avg {avg:.1f} > {AVG_SENT_FAIL} "
                      f"(canon is plain and fast)")
    elif avg > AVG_SENT_WARN:
        warnings.append(f"sentences: {os.path.basename(path)} avg {avg:.1f} near cap")
    if over:
        errors.append(f"sentences: {os.path.basename(path)} has {len(over)} sentence(s) "
                      f"over {MAX_SENT_WORDS} words (max {max(over)})")


def check_dialogue(path, prose_lines, footer_lines, wc, errors):
    if any(l.strip().startswith("DIALOGUE: SKIP") for l in footer_lines):
        return
    rate = _spoken_lines(prose_lines) / max(wc / 1000.0, 0.001)
    if rate < DIALOGUE_PER_1000:
        errors.append(f"dialogue: {os.path.basename(path)} has {rate:.1f} spoken lines/1000 "
                      f"words < {DIALOGUE_PER_1000} (people talking — or declare "
                      f"DIALOGUE: SKIP — reason)")


def check_banned(path, prose_lines, errors):
    body = "\n".join(prose_lines)
    for tok in BANNED:
        if tok.lower() in body.lower():
            errors.append(f"banned: {os.path.basename(path)} contains '{tok}'")
    if CJK.search(body):
        errors.append(f"banned: {os.path.basename(path)} contains CJK characters "
                      f"(rail 8 zero-CJK)")


def check_spine(path, prose_lines, footer_lines, errors, warnings):
    if any(l.strip().startswith("SPINE: NONE") for l in footer_lines):
        return
    body = " ".join(prose_lines).lower()
    hits = [a for a in SPINE_ANCHORS if a in body]
    if not hits:
        errors.append(f"spine: {os.path.basename(path)} names ZERO canon anchors — "
                      f"failure #1 (canon must happen on the page; else declare "
                      f"SPINE: NONE — reason)")


def check_footer(path, footer_lines, errors):
    if not footer_lines:
        errors.append(f"footer: {os.path.basename(path)} has no SYNC: mirror record "
                      f"(R5/RAILS record law)")
        return
    joined = "\n".join(footer_lines)
    for key in ("Beats:", "Files updated:"):
        if key not in joined:
            errors.append(f"footer: {os.path.basename(path)} SYNC block missing '{key}'")


def check_panel(root, chapters, errors):
    p = os.path.join(root, "foundation", "STATUS_PANEL.md")
    if not os.path.exists(p):
        errors.append("panel: foundation/STATUS_PANEL.md missing"); return
    txt = open(p, encoding="utf-8").read()
    for sec in PANEL_SECTIONS:
        if sec not in txt:
            errors.append(f"panel: STATUS_PANEL.md missing section '{sec}'")
    if chapters:
        hi = max(n for n, _ in chapters)
        if not re.search(r"[Cc]hapter\s+0*%d\b" % hi, txt):
            errors.append(f"panel: STATUS_PANEL.md does not track latest Chapter {hi:02d} "
                          f"(two-copies law: panel syncs in the same turn as the chapter)")


def verify(root):
    errors, warnings = [], []
    chapters = find_chapters(os.path.join(root, "chapters"))
    check_rulings(root, bool(chapters), errors)
    check_sequence(chapters, errors)
    for _, path in chapters:
        prose, footer = _split_prose_footer(open(path, encoding="utf-8").read())
        check_footer(path, footer, errors)
        wc = check_length(path, prose, footer, errors)
        check_sentences(path, prose, errors, warnings)
        check_dialogue(path, prose, footer, wc, errors)
        check_banned(path, prose, errors)
        check_spine(path, prose, footer, errors, warnings)
    check_panel(root, chapters, errors)
    return errors, warnings, chapters


# ----------------------------------------------------------------- selftest
GOOD_CH = ("Chapter 1 — The morning bell at Eastsea gate rang twice, and he was late.\n"
           '"You owe me the gate chit," said the porter. "Pay up or wait outside."\n'
           '"I have two coppers and a broken sandal," he said. "Take the sandal."\n'
           "The porter laughed and waved him through the yard toward the testing hall.\n") * 14 + (
           "Inside, the Spirit Pagoda clerk called his name and set a cheap soul on the counter.\n"
           '"Defective stock," the clerk said. "Still want it?" "It is mine," he said. "Yes."\n'
           "The little soul's light was dim. His rank was low. He paid the coin anyway.\n") * 14 + (
           "\nSYNC: ch01\nBeats: Eastsea gate; Pagoda counter; defective soul taken\n"
           "Files updated: foundation/STATUS_PANEL.md Chapter 01\n")

def _mkroot(tmp, rulings_open):
    os.makedirs(os.path.join(tmp, "chapters")); os.makedirs(os.path.join(tmp, "foundation"))
    state = "**OPEN**" if rulings_open else "**RESOLVED**"
    open(os.path.join(tmp, "foundation", "OPEN_RULINGS.md"), "w").write(
        f"| R1 | q | {state} |\n| R2 | q | {state} |\n")
    open(os.path.join(tmp, "foundation", "STATUS_PANEL.md"), "w").write(
        "\n".join(PANEL_SECTIONS) + "\nlatest: Chapter 01\n")
    return tmp


def selftest():
    print(GATE_NAME + " — selftest")
    cases = []
    def one(name, ch_text=None, rulings_open=False, expect=None, extra=None):
        tmp = tempfile.mkdtemp()
        _mkroot(tmp, rulings_open)
        if ch_text is not None:
            open(os.path.join(tmp, "chapters", "Chapter_01_T.md"), "w").write(ch_text)
        if extra == "gap":
            open(os.path.join(tmp, "chapters", "Chapter_03_T.md"), "w").write(GOOD_CH)
        if extra == "panel_gap":
            p = os.path.join(tmp, "foundation", "STATUS_PANEL.md")
            open(p, "w").write("\n".join(PANEL_SECTIONS) + "\nlatest: none yet\n")
        errors, _, _ = verify(tmp)
        hit = "; ".join(errors)
        ok = bool((expect is None and not errors) or
                  (expect and any(expect in e for e in errors)))
        cases.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  -> got: {hit}"))
        return ok

    one("good chapter passes", GOOD_CH)
    one("short fails", GOOD_CH[:1200], expect="length")
    one("long-sentence fails",
        re.sub(r"[.!?]", ",", GOOD_CH)[:-1] + ".\n\nSYNC: x\nBeats: b\nFiles updated: f\n",
        expect="sentences")
    one("no-footer fails", GOOD_CH.split("\nSYNC:")[0], expect="footer")
    one("banned token fails", GOOD_CH.replace("two coppers", "Dawnflame 1,120"),
        expect="banned")
    one("CJK fails", GOOD_CH.replace("porter", "门房"), expect="banned")
    silent = GOOD_CH.replace(
        '"You owe me the gate chit," said the porter. "Pay up or wait outside."',
        "The porter looked at him and held out one open patient hand for the fee."
    ).replace(
        '"I have two coppers and a broken sandal," he said. "Take the sandal."',
        "He had two coppers and one broken sandal, and he offered both at once."
    ).replace(
        '"Defective stock," the clerk said. "Still want it?" "It is mine," he said. "Yes."',
        "The clerk shrugged and slid the dim soul across the counter without a word."
    )
    one("no-dialogue fails", silent, expect="dialogue")
    one("open-rulings fails", GOOD_CH, rulings_open=True, expect="rulings")
    one("sequence gap fails", GOOD_CH, extra="gap", expect="sequence")
    one("panel desync fails", GOOD_CH, extra="panel_gap", expect="panel")
    n_ok = sum(cases)
    print(f"selftest: {n_ok}/10 defect classes behaved correctly")
    return 0 if n_ok == 10 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors, warnings, chapters = verify(root)
    print(GATE_NAME)
    print(f"chapters: {len(chapters)}")
    for w in warnings:
        print("  WARN " + w)
    if not chapters:
        print("foundation stage: no chapters — narrative gates dormant; "
              "structure gates ran.")
    if errors:
        print(f"GATE FAIL ({len(errors)}):")
        for e in errors:
            print("  FAIL " + e)
        sys.exit(1)
    print("GATE PASS" + (f" ({len(warnings)} warnings)" if warnings else ""))
    sys.exit(0)
