#!/usr/bin/env python3
"""chapter_gate.py — the chapter gate for soul-land-1-fire-dragon-lizard.

Rulings it enforces (foundation/RULINGS_LOG.md):
  R13 — band: 3600–5000 words (corrected 2026-10-03 against the author's
  own chapters; see BAND_MIN/BAND_MAX below — the 2400–3400 default was an
  unchecked agent guess the author never typed).
  PRE4 — NO SYSTEM anywhere (banned tokens below).
  R11 — figures belong to STATUS/panels, never prose (informational checks).
  Stage-0 lock — if foundation/OPEN_RULINGS.md still carries a red-lane
  marker, no chapter may pass (drafting unlocked only when every lane is
  ruled; STATUS is the truth for that state).

Usage:
  python3 tools/chapter_gate.py chapters/Chapter_01.md
  python3 tools/chapter_gate.py --selftest

Exit 0 = PASS, 1 = FAIL. Never weaken a check to make a chapter pass —
fix the chapter (house law).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# R13 default corrected 2026-10-03 against the AUTHOR'S REAL chapters:
# his Chapter_01/02/03 = 4622 / 4154 / 3776 words (receipts: raw fetch
# that date). The original 2400-3400 was an unchecked agent default the
# author never typed; 'everything was wrong' + his practice corrected it.
BAND_MIN, BAND_MAX = 3600, 5000
# Paragraph advisory calibrated to the AUTHOR'S OWN STYLE, 2026-10-03:
# his Chapter 1 (soul_land_4_fire_phoenix/chapters/Chapter_01.md) runs 272
# non-empty blocks; the old 14-18 guess was never his voice. Warn-only —
# never gates pass/fail.
PARA_MIN, PARA_MAX = 60, 300              # R13 band's paragraph advisory

# PRE4 + house bans: System vocabulary and cheat-story tokens.
BANNED_FAIL = [
    (r"\bSystem\b", "capital-S 'System' — banned (PRE4)"),
    (r"\blevel up\b", "level-up chrome — banned (PRE4)"),
    (r"\[\[", "'[[' game-bracket — banned (PRE4)"),
    (r"\]\]", "']]' game-bracket — banned (PRE4)"),
    (r"宿主", "System-novel host token — banned"),
    (r"签到", "check-in-system token — banned"),
    (r"开挂", "cheat token — banned"),
    (r"外挂", "cheat token — banned"),
    (r"金手指", "golden-finger token — banned"),
    (r"面板", "System-panel token — banned"),
]
BANNED_WARN = [
    (r"\bsystem\b", "lowercase 'system' — review context (PRE4)"),
]

CH_NAME = re.compile(r"^Chapter_\d{2,3}\.md$")
PANEL = re.compile(r"^\s*【")


def words(text: str) -> int:
    return len(re.findall(r"\S+", re.sub(r"【[^】]*】", "", text)))


def paragraphs(text: str) -> int:
    return len([b for b in re.split(r"\n\s*\n", text) if re.search(r"\S", b)])


def check_stage0(root: Path) -> tuple[list[str], list[str], list[str]]:
    errs: list[str] = []
    open_file = root / "foundation" / "OPEN_RULINGS.md"
    if not open_file.exists():
        errs.append("foundation/OPEN_RULINGS.md missing — no foundation, no chapters")
        return errs, [], []
    text = open_file.read_text(encoding="utf-8")
    if "🔴" in text:
        errs.append("foundation/OPEN_RULINGS.md still carries a red-lane marker — drafting locked (Stage 0)")
    return errs, [], []


def check_chapter(path: Path) -> tuple[list[str], list[str], list[str]]:
    errs, warns, infos = [], [], []
    if not path.exists():
        return [f"{path}: not found"], warns, infos
    if path.parent.name == "chapters" and not CH_NAME.match(path.name):
        errs.append(f"{path.name}: name must match Chapter_NN.md (house pattern)")
    text = path.read_text(encoding="utf-8")
    w = words(text)
    if w < BAND_MIN:
        errs.append(f"word count {w} < band minimum {BAND_MIN} (R13)")
    elif w > BAND_MAX:
        errs.append(f"word count {w} > band maximum {BAND_MAX} (R13)")
    else:
        infos.append(f"word count {w} — inside band {BAND_MIN}-{BAND_MAX}")
    p = paragraphs(text)
    if p < PARA_MIN or p > PARA_MAX:
        warns.append(f"paragraph blocks {p} — target {PARA_MIN}-{PARA_MAX} (R13 avg)")
    for pat, why in BANNED_FAIL:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            errs.append(f"line {line}: banned token — {why}")
    for pat, why in BANNED_WARN:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            warns.append(f"line {line}: {why}")
    panels = sum(1 for ln in text.splitlines() if PANEL.match(ln))
    infos.append(f"panel lines: {panels} — F22: update/gain beats only, human review")
    if "the OC" in text:
        warns.append("'the OC' appears in prose — placeholder never ships; the name rule stands (STATUS)")
    infos.append("no invented-name scan possible — STATUS is the name authority")
    return errs, warns, infos


def selftest() -> int:
    import tempfile
    passed = failed = 0

    def t(name: bool, expect: bool):
        nonlocal passed, failed
        if bool(name) == expect:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL selftest: {name}")

    t(BAND_MIN == 3600 and BAND_MAX == 5000, True)          # R13 band (corrected)
    t(words("one two three") == 3, True)
    t(words("【hello world】 kept now") == 2, True)          # panel stripped
    t(bool(re.search(BANNED_FAIL[0][0], "The System spoke")), True)
    t(not bool(re.search(BANNED_FAIL[0][0], "the political system")), True)  # case-sensitive
    t(bool(re.search(BANNED_WARN[0][0], "the system of rivers")), True)
    t(CH_NAME.match("Chapter_07.md") is not None, True)
    t(CH_NAME.match("chapter7.md") is None, True)
    t(paragraphs("a\n\nb\n\n\nc") == 3, True)
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "foundation").mkdir()
        (root / "foundation" / "OPEN_RULINGS.md").write_text("all ruled ✅")
        t(check_stage0(root)[0] == [], True)                # no red marker
        (root / "foundation" / "OPEN_RULINGS.md").write_text("🔴 OPEN lane")
        t(len(check_stage0(root)[0]) == 1, True)            # red marker locks
    good = "word\n\n" * 17                                   # ~17 short blocks
    good = " ".join(["filler"] * 2600).join(["\n\n"]) if False else ("filler " * 3700)
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "Chapter_01.md"
        p.write_text(good, encoding="utf-8")
        errs, _, _ = check_chapter(p)
        t(len(errs) == 0, True)                              # 3700 words in band
        p.write_text("too short", encoding="utf-8")
        errs, _, _ = check_chapter(p)
        t(len(errs) >= 1, True)                              # under band fails
        p.write_text(("System " * 3000), encoding="utf-8")
        errs, _, _ = check_chapter(p)
        t(any("banned" in e for e in errs), True)           # banned token fails
    print(f"chapter_gate selftest: {passed}/{passed + failed} passed")
    return 0 if failed == 0 else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if len(argv) != 2:
        print(__doc__)
        return 1
    root = Path(__file__).resolve().parent.parent
    errs, warns, infos = check_stage0(root)
    c_errs, c_warns, c_infos = check_chapter(Path(argv[1]))
    errs += c_errs
    warns += c_warns
    infos += c_infos
    for i in infos:
        print(f"  info  {i}")
    for w in warns:
        print(f"  warn  {w}")
    for e in errs:
        print(f"  FAIL  {e}")
    if errs:
        print(f"FAIL  chapter gate: {len(errs)} error(s), {len(warns)} warning(s) [{argv[1]}]")
        return 1
    print(f"PASS  chapter gate: 0 error(s), {len(warns)} warning(s) [{argv[1]}]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
