#!/usr/bin/env python3
"""CONSEQUENCE — a mechanical aid to logical thinking on a long story.

WHAT IT IS FOR
  Every serious error on this project was the same shape: a fact entered the story and its mechanical
  consequence was never followed through.
      both rings turned purple (ch40)  ->  soul skills upgrade too   ->  found 21 chapters late
      Wulin reached peak rank 15       ->  canon moves him 15->16->17 ->  found 49 chapters late
      the rank-30 wall opened          ->  every "hard wall" doc wrong ->  found 21 chapters late
  Imagination was never the problem. Consequence-tracking was. So this tool tracks consequences.

WHAT IT DOES
  brief    -- the thing to read before writing: current state, open premises, owed items, next events
  premise  -- register a premise: something happened, here is what must follow
  check    -- for every OPEN premise, grep the chapters for each consequence and report what has
              not landed yet
  rules    -- print the rule library
  done     -- close a premise
  impact   -- given an event type, list which rules fire (so you don't have to remember them)

LIMITATION — READ THIS BEFORE TRUSTING A GREEN RESULT
  This tool does PRESENCE checks: "is there a chapter containing X?" It CANNOT do absence checks
  ("no chapter says Y"), because a checker can prove false presence but never false absence. A
  consequence of the form "nothing may still say Z" must be enforced by a dedicated checker with a
  regex for Z, not by this tool. Framing such a rule as a scan here produces a permanently-red line
  that gets ignored, which is worse than not having it.

REGISTRY: CODEX/CONSEQUENCE_REGISTRY.md (markdown tables, one block per premise)
JOURNAL:  CODEX/DECISION_JOURNAL.md -- every AU decision, with its reason and its cost. A decision
          that is not written down gets re-decided differently later, and that is how a story
          contradicts itself.
RULES:    CODEX/CONSEQUENCE_RULES.md

Usage:
  python3 CODEX/consequence.py brief
  python3 CODEX/consequence.py premise --id P007 --event "Xie Xie builds the Twin Dragon Storm" \
      --ch 53 --follows "it costs him: three weeks, two vomits" --follows "Wu Zhangkong reacts"
  python3 CODEX/consequence.py impact --event "a ring changes colour"
  python3 CODEX/consequence.py check
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(ROOT)
REG = os.path.join(ROOT, "CONSEQUENCE_REGISTRY.md")

# ---------------------------------------------------------------------------
# the rule library, in code so `impact` can answer without me remembering
# ---------------------------------------------------------------------------
RULES = [
    ("R01", "A RING CHANGES COLOUR",
     ["soul ring changes colour", "ring re-forms", "ring turns purple", "ring turns black",
      "rings re-form"],
     ["Their soul skills upgrade with it (canon: upgraded spirit soul => upgraded soul skills)",
      "The new tier must be SHOWN, not assumed",
      "The cost of the skill changes too"]),
    ("R02", "A SPIRIT SOUL CROSSES A THRESHOLD",
     ["spirit soul crosses", "hawk crosses", "crosses 1,000", "crosses 10,000", "thousand-year crossing"],
     ["Rings it produced re-form in the new colour",
      "R01 fires for every one of those rings",
      "A new ring may be bestowed (a thousand-year soul bestows up to three)",
      "Count the soul skills — canon says a thousand-year soul gives THREE",
      "The rank ceiling moves: N rings => ranks N*10+1 .. (N+1)*10",
      "Every document stating the old ceiling is now wrong"]),
    ("R03", "A CHARACTER CROSSES A REALM BOUNDARY",
     ["rank 10", "rank 20", "rank 30", "rank 40", "rank 50", "becomes a Soul", "breakthrough to"],
     ["Their title changes — check every use of the old title",
      "They may now reach things the lower realm cannot",
      "Everyone who compares themselves to them must re-compare"]),
    ("R04", "A NEW FACT INVALIDATES A STANDING STATEMENT",
     ["no longer", "instead", "superseded", "was wrong", "opened", "ended", "cancelled"],
     ["Grep every tracking document for the old claim",
      "Grep the chapters for the old claim in present tense",
      "Update the generated docs, don't hand-patch them"]),
    ("R05", "A CHARACTER IS ABSENT FOR AN ARC",
     ["leaves", "absent", "does not appear", "is not present", "transfers out"],
     ["Their progression lines must still be decided off-page",
      "Someone must notice the absence",
      "Their return must cost something"]),
    ("R06", "A POWER IS USED FOR THE FIRST TIME ON-PAGE",
     ["first use", "uses it for the first time", "unleashes", "finally uses"],
     ["It must cost something countable",
      "Witnesses must recalibrate",
      "It cannot be un-used — every later chapter knows it exists"]),
    ("R07", "A NUMBER IS MEASURED IN-WORLD",
     ["measured", "the machine reads", "tested at", "kilograms"],
     ["It becomes a hard floor, never under-performed",
      "Every earlier estimate of the same quantity must be reconciled",
      "Comparison targets update"]),
    ("R08", "A CHARACTER LEAVES OR JOINS A GROUP",
     ["joins", "leaves the group", "roster", "transfers", "arrives"],
     ["Recount the group — every 'all six' / 'the five of us' must be right",
      "The reason must be stated and consistent with who they are",
      "If canon disagrees, record the AU divergence in writing"]),
    ("R09", "A PLAN IS CANCELLED",
     ["cancelled", "canceled", "will not happen", "plan is dead"],
     ["Nothing may foreshadow it again",
      "Add a checker that fails if the cancelled thing's name reappears"]),
]

JRN = os.path.join(ROOT, "DECISION_JOURNAL.md")
JRN_HEADER = """# DECISION JOURNAL

Every AU decision, with the reason it was made and what it costs.

**Why this file exists.** A decision that is not written down gets re-decided differently later, and
that is how a story contradicts itself. Most of the contradictions found in this project were not
bad decisions — they were *unrecorded* ones. Example: "Zhang Yangzi stays at Eastsea while canon has
him transfer out" was decided in ch43 and never recorded, so ch60 cheerfully sent him to Shrek.

Search it before deciding anything: `python3 CODEX/consequence.py decide --find "keyword"`

| ID | Decision | Reason | Cost / what it forbids | Canon diverges? |
|---|---|---|---|---|
"""


def _jrn_rows():
    if not os.path.exists(JRN):
        return []
    out = []
    for l in open(JRN, encoding="utf-8").read().split("\n"):
        m = re.match(r"^\|\s*(D\d+)\s*\|(.*)$", l)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            out.append([m.group(1)] + cells)
    return out


def cmd_decide(a):
    if a.find:
        rows = _jrn_rows()
        q = a.find.lower()
        hits = [r for r in rows if q in " ".join(r).lower()]
        if not hits:
            print(f"no recorded decision matches \"{a.find}\".")
            print("If you are about to decide this, that is fine — but record it:")
            print("  python3 CODEX/consequence.py decide --decision \"...\" --reason \"...\" "
                  "--cost \"...\" [--diverges \"...\"]")
            return
        for r in hits:
            print(f"\n{r[0]}: {r[1]}")
            print(f"   reason:   {r[2] if len(r) > 2 else ''}")
            print(f"   cost:     {r[3] if len(r) > 3 else ''}")
            print(f"   diverges: {r[4] if len(r) > 4 else 'no'}")
        return
    if not a.decision:
        sys.exit("need --decision, or use --find")
    rows = _jrn_rows()
    nid = f"D{len(rows) + 1:03d}"
    cells = [a.decision, a.reason or "", a.cost or "", a.diverges or "no"]
    line = "| " + nid + " | " + " | ".join(c.replace("|", "/").replace("\n", " ") for c in cells) + " |"
    txt = open(JRN, encoding="utf-8").read() if os.path.exists(JRN) else JRN_HEADER
    open(JRN, "w", encoding="utf-8").write(txt.rstrip("\n") + "\n" + line + "\n")
    print(f"recorded {nid}: {a.decision[:80]}")


HEADER = """# CONSEQUENCE REGISTRY

Every premise that has entered the story, and what must follow from it.

**A premise stays OPEN until every one of its consequences has either landed on-page or been
explicitly decided against.** Silence is not a decision.

`python3 CODEX/consequence.py check` greps the chapters for each open consequence and reports what
has not landed.

---

"""


# ---------------------------------------------------------------------------
# registry I/O
# ---------------------------------------------------------------------------
def load():
    if not os.path.exists(REG):
        return []
    txt = open(REG, encoding="utf-8").read()
    out = []
    for block in txt.split("\n## ")[1:]:
        lines = block.strip().split("\n")
        head = lines[0]
        m = re.match(r"(P\d+)\s*—\s*(.*)", head)
        if not m:
            continue
        p = {"id": m.group(1), "event": m.group(2).strip(), "ch": None,
             "status": "OPEN", "follows": [], "scan": []}
        def val(line, key):
            # "- **follows:** the text" -> "the text". Splitting on the first ":" returns the
            # markdown "**" instead of the value, which silently produced an empty registry.
            rest = line.split(":", 1)[1] if ":" in line else ""
            return rest.lstrip("* ").strip()

        for l in lines[1:]:
            l = l.strip()
            if l.startswith("- **chapter:**"):
                p["ch"] = val(l, "chapter")
            elif l.startswith("- **status:**"):
                p["status"] = val(l, "status").upper()
            elif l.startswith("- **follows:**"):
                p["follows"].append(val(l, "follows"))
            elif l.startswith("- **scan:**"):
                p["scan"].append(val(l, "scan"))
        out.append(p)
    return out


def save(premises):
    lines = [HEADER]
    for p in premises:
        lines.append(f"## {p['id']} — {p['event']}")
        lines.append("")
        if p.get("ch"):
            lines.append(f"- **chapter:** {p['ch']}")
        lines.append(f"- **status:** {p['status']}")
        for f in p["follows"]:
            lines.append(f"- **follows:** {f}")
        for s in p["scan"]:
            lines.append(f"- **scan:** {s}")
        lines.append("")
    open(REG, "w", encoding="utf-8").write("\n".join(lines))


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------
def chapters():
    paths = sorted(glob.glob(os.path.join(WS, "Soul_Land_3_Project", "chapters", "chapter_*.md")))
    return [(int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1)), p) for p in paths]


def latest_chapter():
    ch = chapters()
    return ch[-1][0] if ch else 0


def cmd_rules(_a):
    txt = os.path.join(ROOT, "CONSEQUENCE_RULES.md")
    print(open(txt, encoding="utf-8").read() if os.path.exists(txt) else "(rule library missing)")


def _norm(t):
    """Lowercase, collapse whitespace, and fold the inflections that break naive substring
    matching. The first version of this matched literal phrases and therefore MISSED
    "both of his soul rings change colour to purple" — the exact case it was written for.
    A thinking aid that fails on its own founding example is worse than none."""
    t = re.sub(r"\s+", " ", t.lower().strip())
    for a, b in (("changes", "change"), ("crosses", "cross"), ("re-forms", "reform"),
                 ("reforms", "reform"), ("leaves", "leave"), ("joins", "join"),
                 ("arrives", "arrive"), ("turns", "turn"), ("becomes", "become"),
                 ("uses", "use"), ("cancelled", "cancel"), ("canceled", "cancel"),
                 ("colours", "color"), ("colour", "color"), ("kilograms", "kilogram")):
        t = re.sub(r"\b" + a + r"\b", b, t)
    return t


def cmd_impact(a):
    ev = _norm(a.event)
    hits = []
    for rid, name, keys, cons in RULES:
        scored = [k for k in keys if _norm(k) in ev or any(
            w in ev for w in _norm(k).split() if len(w) > 4)]
        if scored:
            hits.append((rid, name, cons, len(scored)))
    hits.sort(key=lambda h: -h[3])
    if not hits:
        print(f"No rule matched \"{a.event}\".")
        print("That is worth noticing: either the event is genuinely novel, or the rule library")
        print("has a gap. If it is novel, add a rule — the next person to write this story is you.")
        return
    print(f"Rules that fire on \"{a.event}\":\n")
    for rid, name, cons, _score in hits:
        print(f"  {rid} — {name}")
        for c in cons:
            print(f"        → {c}")
        print()
    print("Now register it:  python3 CODEX/consequence.py premise --id P### --event \"...\" "
          "--follows \"...\"")


def cmd_premise(a):
    ps = load()
    if any(p["id"] == a.id for p in ps):
        sys.exit(f"{a.id} already exists")
    ps.append({"id": a.id, "event": a.event, "ch": a.ch or str(latest_chapter()),
               "status": "OPEN", "follows": list(a.follows or []), "scan": list(a.scan or [])})
    ps.sort(key=lambda p: p["id"])
    save(ps)
    print(f"registered {a.id} — {a.event} (OPEN, {len(a.follows or [])} consequences)")


def cmd_done(a):
    ps = load()
    for p in ps:
        if p["id"] == a.id:
            p["status"] = "CLOSED"
            save(ps)
            print(f"closed {a.id}")
            return
    sys.exit(f"no premise {a.id}")


def docs_corpus():
    """The tracking documents, keyed by a synthetic 'chapter' of -1 so they always fall
    inside the scan window. Some consequences land in the docs and not in the prose -- the
    first version of this tool could only see chapters, so it flagged the ceiling move and
    the wall correction as unlanded when they were in fact done."""
    proj = os.path.join(WS, "Soul_Land_3_Project")
    out = {-1: ""}
    names = ["THE_CODEX.md", "POWER_MODEL.md", "LIN_HAO_STATUS.md", "LIN_HAO_PANELS.md",
             "CHARACTER_STATS.md", "PROBLEM_INVENTORY.md", "CONTINUATION_PROMPT.md"]
    for n in names:
        f = os.path.join(proj, n)
        if os.path.exists(f):
            out[-1] += f"\n\n===== {n} =====\n" + open(f, encoding="utf-8", errors="replace").read()
    return out


def cmd_check(a):
    ps = [p for p in load() if p["status"] == "OPEN"]
    if not ps:
        print("consequence: no open premises")
        return
    blob = {}
    if a.scope in ("chapters", "both"):
        for n, path in chapters():
            blob[n] = open(path, encoding="utf-8", errors="replace").read()
    if a.scope in ("docs", "both"):
        blob.update(docs_corpus())
    failures = 0
    for p in ps:
        start = int(p["ch"]) if (p.get("ch") or "0").isdigit() else 0
        window = {n: t for n, t in blob.items() if n >= start or n == -1}
        print(f"\n{p['id']} (ch{p['ch']}, OPEN) — {p['event']}")
        if not p["scan"]:
            print("   (no scan patterns registered — cannot verify; add --scan)")
            continue
        for pat, note in zip(p["scan"], p["follows"]):
            # Per-consequence scope, marked in the consequence text as [chapters] / [docs].
            # Default is CHAPTERS, because a consequence is normally a thing that must happen
            # IN THE STORY. A blanket --scope docs "found" every consequence in the rule text
            # itself, which is a false positive: the docs saying "the skills must upgrade" is
            # not the skills upgrading.
            sm = re.match(r"^\[(chapters|docs|both)\]\s*(.*)$", note, re.I)
            scope = (sm.group(1).lower() if sm else "chapters")
            clean = sm.group(2) if sm else note
            if scope == "docs":
                pool = {n: t for n, t in window.items() if n == -1}
            elif scope == "both":
                pool = window
            else:
                pool = {n: t for n, t in window.items() if n != -1}
            try:
                hit = [n for n, t in sorted(pool.items()) if re.search(pat, t, re.I)]
            except re.error:
                print(f"   !! bad regex: {pat}")
                failures += 1
                continue
            if hit:
                where = "the docs" if hit[0] == -1 else f"ch{hit[0]}"
                print(f"   ok    landed in {where}{'+' if len(hit) > 1 else ''}: {clean[:68]}")
            else:
                where = "docs" if scope == "docs" else ("chapters+docs" if scope == "both" else "the chapters")
                print(f"   OPEN  not found in {where} from ch{start}: {clean[:60]}")
                print(f"         (scan: {pat})")
                failures += 1
    print(f"\nconsequence: {failures} unlanded consequence(s) across {len(ps)} open premise(s)")
    if failures:
        print("         This is DEBT, not a broken build. It warns rather than fails, because a")
        print("         permanently-red check trains you to ignore the check. Use --strict to make")
        print("         it a hard failure, e.g. before delivering an arc.")
    sys.exit(1 if (failures and a.strict) else 0)


def _read_open_block(path):
    """Read the OPEN-PROBLEMS block. Returns [(id, problem, status)] or None if absent.

    🔴 WHY A BLOCK AND NOT A SCRAPE. Three attempts to scrape PROBLEM_INVENTORY.md's free-text
    tables produced three different wrong answers: the tables mix open and closed rows across ten
    id series, rows are written as "✅ FIXED — the problem text" as well as "problem | FIXED", and
    the cells contain literal `|` characters. So the file now carries one unambiguous block and
    both readers use it. Layer 5 checks the block against the table.
    """
    if not os.path.exists(path):
        return None
    t = open(path, encoding="utf-8").read()
    m = re.search(r"<!--\s*OPEN-PROBLEMS-BEGIN(.*?)OPEN-PROBLEMS-END\s*-->", t, re.S)
    if not m:
        return None
    out = []
    for line in m.group(1).strip().split("\n"):
        parts = [x.strip() for x in line.split("|")]
        if len(parts) == 3 and re.match(r"^[A-Z]\d{1,2}$", parts[0]):
            out.append((parts[0], parts[1], parts[2]))
    return out


def cmd_brief(_a):
    proj = os.path.join(WS, "Soul_Land_3_Project")
    sj = os.path.join(proj, "checks", "state.json")
    st = json.load(open(sj, encoding="utf-8")) if os.path.exists(sj) else {}

    print("=" * 74)
    print("BEFORE YOU WRITE — READ THIS FIRST")
    print("=" * 74)

    if st:
        print(f"\nCURRENT (derived from the footers, ch{st.get('latest_chapter')})")
        print(f"  rank {st.get('current_rank')} — {st.get('current_realm')}   "
              f"ceiling {st.get('rank_ceiling')}")
        print(f"  EFFECTIVE: {st.get('effective_realm')} {st.get('effective_rank_band')}  "
              f"(+{st.get('effective_rank_delta')} ranks above his number)")
        print(f"  rings {st.get('rings', {}).get('count')} "
              f"{st.get('rings', {}).get('colour')}   "
              f"spiritual power {st.get('current_spiritual_power')}   "
              f"hawk {st.get('current_hawk_years'):,}")
        print(f"  ledger {st.get('current_ledger')}   smith "
              f"{st.get('current_smith_rank')} ({st.get('current_smith_title')})")

    pinv = os.path.join(proj, "PROBLEM_INVENTORY.md")
    owed = _read_open_block(pinv)
    if owed is None:
        print("\nOWED: ⚠️ PROBLEM_INVENTORY.md has no OPEN-PROBLEMS block, or the file is "
              "missing. This tool will not scrape the free-text tables — three attempts at "
              "that produced three different wrong answers. Go read the file by hand.")
    elif not owed:
        print("\nOWED: the OPEN-PROBLEMS block is empty — nothing is owed.")
    else:
        print(f"\nOWED ({len(owed)} open problem(s), from the OPEN-PROBLEMS block):")
        for pid, problem, status in owed:
            print(f"  {pid}: {problem[:96]}")
            print(f"       [{status}]")

    ps = [p for p in load() if p["status"] == "OPEN"]
    print(f"\nOPEN PREMISES ({len(ps)}) — consequences that have not landed")
    if not ps:
        print("  none registered. If something happened recently, register it:")
        print("  python3 CODEX/consequence.py premise --id P001 --event \"...\" --follows \"...\"")
    for p in ps:
        print(f"  {p['id']} (ch{p['ch']}) {p['event']}")
        for f in p["follows"][:4]:
            print(f"        → {f[:78]}")

    print("\nTHE THREE QUESTIONS")
    print("  1. What changed since the last chapter? (what DID change, not what you plan)")
    print("  2. Which rules fire on it?   python3 CODEX/consequence.py impact --event \"...\"")
    print("  3. What does the reader know that the characters don't — and the reverse?")

    print("\nTHEN")
    print("  cd Soul_Land_3_Project && sh checks/run_all.sh     # must exit 0")
    print("  python3 CODEX/consequence.py check                  # consequences landed?")
    print("=" * 74)


def main():
    ap = argparse.ArgumentParser(description="consequence tracking for long fiction")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("brief").set_defaults(fn=cmd_brief)
    sub.add_parser("rules").set_defaults(fn=cmd_rules)

    p = sub.add_parser("premise")
    p.add_argument("--id", required=True)
    p.add_argument("--event", required=True)
    p.add_argument("--ch")
    p.add_argument("--follows", action="append")
    p.add_argument("--scan", action="append")
    p.set_defaults(fn=cmd_premise)

    c = sub.add_parser("check")
    c.add_argument("--scope", choices=["chapters", "docs", "both"], default="both")
    c.add_argument("--strict", action="store_true",
                   help="exit non-zero on any unlanded consequence")
    c.set_defaults(fn=cmd_check)

    d = sub.add_parser("done")
    d.add_argument("--id", required=True)
    d.set_defaults(fn=cmd_done)

    dc = sub.add_parser("decide")
    dc.add_argument("--decision")
    dc.add_argument("--reason")
    dc.add_argument("--cost")
    dc.add_argument("--diverges")
    dc.add_argument("--find")
    dc.set_defaults(fn=cmd_decide)

    i = sub.add_parser("impact")
    i.add_argument("--event", required=True)
    i.set_defaults(fn=cmd_impact)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
