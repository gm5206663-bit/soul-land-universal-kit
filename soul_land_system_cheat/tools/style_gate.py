#!/usr/bin/env python3
"""STYLE GATE — the serial's style laws, self-enforcing.

HARD FAILURES (exit 1):
  1. a prose sentence over 60 words;
  2. the banned "the way [clause]" simile construction;
  3. a bare (unquoted) panel line;
  4. DIALOGUE FLOOR — fewer than 3 spoken lines in a chapter.
  5. SCOPE — an author edition with no reader edition (never published) or a
     reader edition with no author edition (published, never gated);
  6. STALE COPY — a reader edition that is not the current author edition.

WARNINGS (the author's call, they do not stop the build):
  outside the 2,400-3,400 working band; dialogue below the 8-10 per 1,000
  word bar; speech written as reported speech (said/asked with no quotes);
  a sentence repeated inside one chapter.

SCOPE — this is the law this gate was rebuilt for (2026-10-11):
  a check must declare the scope it actually covered, and must fail loudly
  when it could not cover its full scope. The gate used to read `chapters/`
  only — while `manuscript/` shipped. In the sister project four chapters
  were published with no author edition at all and no gate had ever read
  them. So the gate now audits both ends of the pipeline, prints a
  COVERAGE line, and treats every unaccounted-for chapter as a failure.

Run:  python3 tools/style_gate.py                 # the whole book, both ends
      python3 tools/style_gate.py path/to/file.md  # explicit files
"""
import re, sys, glob, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
SERIAL = os.path.dirname(HERE)

AUTHOR_DIR = os.path.join(SERIAL, "chapters")
READER_DIR = os.path.join(SERIAL, "manuscript")

DIALOGUE_FLOOR = 3          # absolute, hard  — house law
DIALOGUE_BAR = 8.0          # per 1,000 words, advisory
WORD_BAND = (2400, 3400)
FOOT = re.compile(r"\n---\n\n## Footer|\n## Footer")

IDIOM_OK = ("all the way", "on the way", "opens the way", "the way of", "by the way")


def _exceptions():
    ex = os.path.join(HERE, "style_gate_exceptions.txt")
    if not os.path.exists(ex):
        return []
    return [l.split("#")[0].strip() for l in open(ex, encoding="utf-8").read().splitlines()
            if l.split("#")[0].strip()]


def the_way_hits(body):
    hits = []
    for m in re.finditer(r".{0,40}\bthe way\b.{0,40}", body):
        s = m.group(0); low = s.lower()
        if any(i in low for i in IDIOM_OK):
            continue
        if any(e.lower() in low for e in _exceptions()):
            continue
        hits.append(s.strip())
    return hits


def author_body(text):
    """The reader-facing prose inside an author edition (footer stripped)."""
    return FOOT.split(text)[0].rstrip() + "\n"


def measure(body):
    lines = [l for l in body.split("\n") if l.strip() and not l.startswith("# ")]
    prose = [l for l in lines if not l.startswith(">")]
    words = len("\n".join(lines).split())
    sent = [s for l in prose for s in re.split(r"(?<=[.!?])\s+", l.strip()) if s]
    sl = [len(s.split()) for s in sent]
    over = [(n, s) for n, s in zip(sl, sent) if n > 60]
    bare = [l for l in body.split("\n") if l.strip().startswith("「")]
    dlgs = re.findall(r'"([^"\n]+)"', prose_text(prose))
    unmarked = [l.strip() for l in prose
                if not l.startswith((">", "#"))
                and re.search(r"\b(said|asked|answered|replied)\b", l)
                and '"' not in l]
    band = "IN" if WORD_BAND[0] <= words <= WORD_BAND[1] else ("OVER" if words > WORD_BAND[1] else "UNDER")
    return dict(words=words, sl=sl, over=over, bare=bare, dlg=len(dlgs), dlgs=dlgs,
                unmarked=unmarked, band=band,
                avg=statistics.mean(sl) if sl else 0.0,
                med=statistics.median(sl) if sl else 0,
                mx=max(sl) if sl else 0)


def prose_text(prose_lines):
    return "\n".join(prose_lines)


def repeats(body):
    """Sentences of 6+ words repeated inside this chapter."""
    out = []
    seen = {}
    for l in body.split("\n"):
        l = l.strip()
        if not l or l.startswith(("#", ">")) or l == "---":
            continue
        for s in re.split(r"(?<=[.!?])\s+", l):
            s = s.strip()
            if len(s.split()) >= 6:
                seen[s] = seen.get(s, 0) + 1
    for s, n in seen.items():
        if n > 1:
            out.append((n, s))
    return sorted(out, key=lambda x: -x[0])


def check(path, kind, problems, warnings):
    text = open(path, encoding="utf-8").read()
    body = author_body(text) if kind == "author" else text
    m = measure(body)
    name = os.path.basename(path)
    tw = the_way_hits(body)
    hard = bool(m["over"] or tw or m["bare"] or m["dlg"] < DIALOGUE_FLOOR)
    per_k = m["dlg"] / m["words"] * 1000 if m["words"] else 0.0
    if hard:
        problems.append(f"{name}: " + ", ".join(filter(None, [
            f"{len(m['over'])} sentence(s) over 60 words" if m["over"] else "",
            f"{len(tw)} banned 'the way' construction(s)" if tw else "",
            f"{len(m['bare'])} bare panel line(s)" if m["bare"] else "",
            f"dialogue {m['dlg']} < floor {DIALOGUE_FLOOR}" if m["dlg"] < DIALOGUE_FLOOR else "",
        ])))
    if m["dlg"] < DIALOGUE_FLOOR or per_k < DIALOGUE_BAR:
        warnings.append(f"{name} [{kind}]: dialogue {m['dlg']} line(s), {per_k:.1f}/1k — bar is {DIALOGUE_BAR:.0f}/1k")
    if m["band"] != "IN":
        warnings.append(f"{name} [{kind}]: band:{m['band']} — {m['words']}w outside 2400-3400")
    if m["unmarked"] and m["dlg"] < DIALOGUE_FLOOR:
        warnings.append(f"{name} [{kind}]: {len(m['unmarked'])} line(s) of reported speech, unquoted — quotes may be missing")
    rp = repeats(body)
    if rp:
        warnings.append(f"{name} [{kind}]: {len(rp)} sentence(s) repeated inside the chapter — worst x{rp[0][0]}: {rp[0][1][:70]}...")
    print(f"{name:38s} {kind:6s} {m['words']:5d}w band:{m['band']:5s} avg:{m['avg']:4.1f} "
          f"med:{m['med']:3.0f} max:{m['mx']:2d} dlg:{m['dlg']:3d} ({per_k:4.1f}/1k) "
          f"over60:{len(m['over'])} the-way:{len(tw)} bare:{len(m['bare'])}")
    for n, s in m["over"]:
        print(f"    OVER60 [{n}w]: {s[:100]}...")
    for s in tw:
        print(f"    THE-WAY: ...{s}...")
    return m


def main():
    args = sys.argv[1:]
    problems, warnings = [], []
    print("THE SYSTEM CHEAT — STYLE GATE\n" + "=" * 86)

    if args:
        paths = args
        print(f"COVERAGE: explicit paths — {len(paths)} file(s), no book scope claimed")
        for p in paths:
            check(p, "file", problems, warnings)
    else:
        authors = sorted(glob.glob(os.path.join(AUTHOR_DIR, "Chapter_*.md")))
        readers = [p for p in sorted(glob.glob(os.path.join(READER_DIR, "Chapter_*.md")))]
        an = {os.path.basename(p): p for p in authors}
        rn = {os.path.basename(p): p for p in readers}

        # ── SCOPE: both ends of the pipeline must account for every chapter ──
        print("AUTHOR EDITIONS  chapters/")
        for n in sorted(an):
            check(an[n], "author", problems, warnings)
        print("\nREADER EDITIONS  manuscript/")
        for n in sorted(rn):
            check(rn[n], "reader", problems, warnings)

        fulls = sorted(glob.glob(os.path.join(READER_DIR, "*FULL*.md")))
        full = fulls[0] if fulls else None
        full_ch = 0
        if full:
            full_ch = len(re.findall(r"(?m)^# Chapter \d+", open(full, encoding="utf-8").read()))

        print("\n" + "-" * 86)
        print(f"COVERAGE: chapters/ {len(an)} of {len(an)} author editions · "
              f"manuscript/ {len(rn)} of {len(rn)} reader editions · "
              f"{(os.path.basename(full) if full else 'FULL edition')} {full_ch} of {len(an)} chapters")

        if not an and not rn:
            problems.append("SCOPE: 0 files found — a check that executes nothing verifies nothing")

        for name in sorted(set(an) - set(rn)):
            problems.append(f"SCOPE: {name} — author edition exists but no reader edition was ever published")
        for name in sorted(set(rn) - set(an)):
            problems.append(f"SCOPE: {name} — PUBLISHED with no author edition, so no gate has ever seen it")
        for name in sorted(set(an) & set(rn)):
            a, r = author_body(open(an[name], encoding="utf-8").read()), open(rn[name], encoding="utf-8").read()
            if re.sub(r"\s+$", "", a) != re.sub(r"\s+$", "", r):
                problems.append(f"SCOPE: {name} — reader edition is not the author edition it claims "
                                f"(what ships is not what was gated — run tools/run_all.py)")
        if an and full_ch != len(an):
            problems.append(f"SCOPE: the FULL edition holds {full_ch} of {len(an)} chapters")

    print("=" * 86)
    for w in warnings:
        print("WARN  " + w)
    for p in problems:
        print("FAIL  " + p)
    print("=" * 86)
    print(f"COVERAGE: {len(problems)} hard failure(s), {len(warnings)} warning(s). "
          f"Band, dialogue bar and repetition are the author's call; scope, the floor, "
          f"over60, the-way and bare panels are not.")
    print("FAIL" if problems else "ALL HARD CHECKS PASS")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
