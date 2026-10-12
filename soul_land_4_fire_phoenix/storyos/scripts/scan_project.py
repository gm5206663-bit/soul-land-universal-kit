#!/usr/bin/env python3
"""
scan_project.py — rebuild the StoryOS manifest + cards from whatever the project files say.

This is the anti-drift engine: no number is typed by hand. Point it at a corpus of
audit/validation/status markdown and it produces:
    foundation/CURRENT_STATE_MANIFEST.json   machine state, validator's input
    foundation/canon/characters/*.card.md    per-character locked state (human + machine)
    foundation/canon/locks/*.card.md         each lock, with its source receipt
    canon_coverage/CANON_LEDGER.md           fic <-> canon table
    canon_coverage/BRANCH_LEDGER.md          active vs superseded branches

    python3 scan_project.py <corpus_dir> <project_dir>
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

SCHEMA = "storyos-manifest/3"

RE_DATE = re.compile(r"(20\d\d-\d\d-\d\d)")
RE_EDGE = re.compile(r"Live edge:\s*\*\*after Chapter(\d+),\s*`([^`]+)`\*\*")
RE_CANON = re.compile(r"Canon consumed through(?: verified)? Chapter(\d+)\s*`?([^`\n.]+)`?")
RE_NEXT = re.compile(r"Next (?:source(?: boundary)?|source):\s*Chapter(\d+)\s*`([^`]+)`")
RE_LOCK_PATH = re.compile(r"`(foundation/[A-Za-z0-9_./-]+\.md)`")
RE_LOCK_HEAD = re.compile(r"^#{1,4}[^\n]*[Ll]ock[^\n]*$", re.M)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def date_of(name: str, text: str) -> str:
    m = RE_DATE.search(name) or RE_DATE.search(text)
    return m.group(1) if m else "0000-00-00"



NUM = re.compile(r"(SP\d{2,6}|(?:Dawnflame|Dawn-Iron)\s[\d,]{3,9})")
OR_TAIL = re.compile(r"((?:Dawnflame|Dawn-Iron)\s[\d,]+\s+or\s+[\d,]+)")

def nums_in(t: str) -> list[str]:
    """Expand "Dawnflame 960 or 1,120" into BOTH tokens — the naive matcher kept only
    the first value, leaving 1,120 and 2,040 unguarded."""
    out = [m.group(1) for m in NUM.finditer(t)]
    for m in OR_TAIL.finditer(t):
        label = m.group(1).split()[0]
        for v in re.findall(r"[\d][\d,]*", m.group(1).split(label, 1)[1]):
            out.append(f"{label} {v}")
    return sorted(set(out))
def native_manifest(proj: Path) -> dict:
    """A project may already keep an authoritative machine manifest (schema 2.x).
    If so we adopt its registries verbatim rather than heuristically re-deriving them —
    the project's own declaration beats our guess about what it meant."""
    for rel in ("foundation/CURRENT_STATE_MANIFEST.json", "CURRENT_STATE_MANIFEST.json"):
        f = proj / rel
        if f.exists():
            try:
                return json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return {}
    return {}


CHARS = ("Lan Xuanyu", "Qian Lei", "Liu Feng", "Yan Shuo", "Song Yichen",
             "Luo Haoran", "Lu Qianxun", "Ye Lingtong", "Jin Xiang")


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    corpus = Path(sys.argv[1]).resolve()
    proj = Path(sys.argv[2]).resolve()
    # StoryOS is a CONTROL LAYER, not an editor. Generated state goes to a separate install
    # directory so it can never overwrite a project's own authoritative files.
    inst = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else proj / "storyos"
    if inst == proj:
        inst = proj / "storyos"
    files = sorted(corpus.glob("*.md"))       # top level = live receipts
    (inst / "canon" / "characters").mkdir(parents=True, exist_ok=True)
    (inst / "canon" / "locks").mkdir(parents=True, exist_ok=True)
    all_md = sorted(corpus.rglob("*.md"))     # + dated pre-repair backup dirs
    raw = {p.name: read(p) for p in files}
    snapshots = [p for p in all_md if p.parent != corpus]
    if not raw:
        print(f"scan_project: no .md files in {corpus}")
        return 2

    # Precedence: the PROJECT'S OWN foundation/ beats any mirror found in the corpus.
    # Receipts are evidence about the past, not authority over the present.
    NAT = native_manifest(proj)

    def first_existing(*paths):
        for q in paths:
            if q.exists():
                return read(q), q.name if not str(q).startswith(str(proj)) else str(q.relative_to(proj))
        return "", None

    status, status_name = first_existing(proj / "foundation/STATUS_PANEL.md",
                                         proj / "STATUS_PANEL.md",
                                         corpus / "STATUS_PANEL.md",
                                         corpus / "YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md",
                                         corpus / "YAN_SHUO_CURRENT_STATUS_PANEL.md")
    if not status:
        status_name = next((n for n in ("YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md",
                                        "YAN_SHUO_CURRENT_STATUS_PANEL.md") if n in raw), None)
        status = raw.get(status_name, "")
    bible = (read(proj / "bible/PROJECT_BIBLE.md") or read(proj / "MASTER_PROJECT_BIBLE.md")
             or raw.get("MASTER_PROJECT_BIBLE.md", ""))
    handoff = read(proj / "HANDOFF.md") or raw.get("HANDOFF.md", "")
    cls = (read(proj / "PROJECT_FILE_CLASSIFICATION_AND_SOURCE_OF_TRUTH.md")
           or raw.get("PROJECT_FILE_CLASSIFICATION_AND_SOURCE_OF_TRUTH.md", ""))
    rejection = (read(proj / "USER_REJECTION_REPAIR_MODE.md")
                 or raw.get("USER_REJECTION_REPAIR_MODE_2026-09-17.md", ""))

    # Priority: (1) the project's own native manifest, (2) its foundation/STATUS_PANEL.md,
    # (3) the newest dated claim in the audit receipts. Receipts describe the past; they must
    # never outrank a live declaration — that is how a stale branch becomes "current".
    claims = []
    for name, blob in raw.items():
        for m in RE_EDGE.finditer(blob):
            claims.append((date_of(name, blob), int(m.group(1)), m.group(2), name))
    claims.sort(key=lambda t: t[0])
    if not claims:
        print("scan_project: no 'Live edge' claim found in corpus")
        return 2
    edge_day, edge_ch, edge_title, edge_src = claims[-1]

    consumed = consumed_title = nxt = nxt_title = None
    panel = RE_EDGE.search(status)
    if panel:
        edge_day, edge_ch, edge_title = date_of("panel", status), int(panel.group(1)), panel.group(2)
        edge_src = f"{status_name} (project foundation)"
        mc = RE_CANON.search(status)
        if mc:
            consumed, consumed_title = int(mc.group(1)), mc.group(2).strip()
        mn = RE_NEXT.search(status)
        if mn:
            nxt, nxt_title = int(mn.group(1)), mn.group(2)

    if NAT.get("latest_fic_chapter") is not None:
        cc = NAT.get("canon_consumed_through") or {}
        ns = NAT.get("next_source") or {}
        edge_day = NAT.get("updated", edge_day) or edge_day
        edge_ch = int(NAT["latest_fic_chapter"])
        edge_title = NAT.get("latest_fic_title", edge_title)
        edge_src = "foundation/CURRENT_STATE_MANIFEST.json (native, authoritative)"
        consumed = cc.get("chapter", consumed)
        consumed_title = (cc.get("title") or consumed_title or "").strip()
        nxt = ns.get("chapter", nxt)
        nxt_title = ns.get("title") or nxt_title or ""
    # ---------- ledger: chapter -> newest validation / sync ----------
    def indexed(prefix: str, suffix: str) -> dict[int, tuple[str, str]]:
        out: dict[int, tuple[str, str]] = {}
        for name in raw:
            m = re.match(rf"{prefix}_(\d+)_{suffix}_(20\d\d-\d\d-\d\d)\.md$", name)
            if m:
                n, d = int(m.group(1)), m.group(2)
                if n not in out or d > out[n][0]:
                    out[n] = (d, name)
        return out

    val = indexed("CHAPTER", "VALIDATION")
    sync = indexed("CHAPTER", "SUPPORT_SYNC")

    # A receipt marked SUPERSEDED / DO NOT USE is quarantined by declaration, independent of
    # date arithmetic — humans assert intent better than heuristics infer it.
    marked: set[int] = set()
    for name, blob in raw.items():
        if not re.match(r"CHAPTER_\d+_", name):
            continue
        # only a marker in the leading notice counts — historical receipts discuss supersession
        head = blob[:600]
        if re.search(r"SUPERSEDED[^\n]*DO NOT USE|DO NOT USE AS LIVE STATE", head, re.I):
            marked.add(int(re.match(r"CHAPTER_(\d+)_", name).group(1)))

    # chapters asserted as superseded by the rejection notice / newer rebuild
    superseded: set[int] = set()
    branch_note = ""
    if rejection:
        m = re.search(r"specifically objecting that", rejection)
        branch_note = ("post-Chapter48 direction rejected on 2026-09-17; repair rebuilt "
                       "Chapter46-51 and superseded that branch's receipts")
        for n in sorted(val):
            d = val[n][0]
            if d < edge_day and n > edge_ch:      # receipt older than live edge but ahead of it
                superseded.add(n)
    for n in sorted(val):
        if n > edge_ch or n in marked:
            superseded.add(n)          # beyond live edge, or explicitly marked superseded

    cover_map: dict[int, str] = {}
    for row in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", bible, re.M):
        try:
            n = int(row.group(1))
        except ValueError:
            continue
        if 20 <= n <= 400:
            cover_map.setdefault(n, row.group(2).strip())

    ledger = []
    for n in sorted(set(val) | set(sync) | set(cover_map)):
        status_txt = ("accepted" if n <= edge_ch else
                      "quarantined-superseded" if n in superseded else "drafted-not-live")
        ledger.append({
            "fic": n,
            "canon": cover_map.get(n, "—"),
            "status": status_txt,
            "validation": val.get(n, (None, None))[1],
            "validation_date": val.get(n, (None, ""))[0],
            "support_sync": sync.get(n, (None, None))[1],
        })

    # ---------- locks ----------
    lock_paths, seen = [], set()
    for blob in (status, handoff, cls, bible):
        for m in RE_LOCK_PATH.finditer(blob):
            path = m.group(1)
            if path not in seen:
                seen.add(path)
                lock_paths.append(path)

    lock_cards = []
    for p in files:
        txt = raw[p.name]
        for m in RE_LOCK_HEAD.finditer(txt):
            head = m.group(0).lstrip("#").strip()
            body = txt[m.end():m.end() + 1200]
            lines = [x.strip() for x in body.splitlines() if x.strip()]
            stmt = next((x for x in lines if re.match(r"^[A-Z].{25,}", x) and not x.startswith("#")),
                        "")
            if not stmt:
                continue
            lock_cards.append({"title": head, "source": p.name, "source_date": date_of(p.name, txt),
                               "statement": re.sub(r"\s+", " ", stmt)[:600]})
    # dedupe by normalised statement prefix, keep newest
    uniq: dict[str, dict] = {}
    for c in lock_cards:
        key = re.sub(r"[^a-z]", "", c["statement"].lower())[:70]
        if key not in uniq or c["source_date"] > uniq[key]["source_date"]:
            uniq[key] = c
    lock_cards = sorted(uniq.values(), key=lambda c: c["statement"])

    # ---------- banned tokens: the drift registry ----------
    banned: dict[str, list[str]] = {"deleted_mistake_route": [], "forbidden_future_power": [],
                                    "forbidden_currentization": [], "stale_stat_drift": [],
                                    "banned_pacing": []}
    # Read the whole forbidden section and re-join wrapped bullets, so a value sitting on a
    # continuation line can never be silently dropped (that was the SP526 bug).
    fb = re.search(r"## 9\. Not current / forbidden\n(.+?)\n## 10\.", status, re.S)
    items: list[str] = []
    if fb:
        for line in fb.group(1).splitlines():
            t = line.strip()
            if t.startswith("- "):
                items.append(t[2:])
            elif t and items and not re.match(r"(Do not|Allowed)", t) and not t.startswith("#"):
                items[-1] += " " + t
            elif re.match(r"(Do not|Allowed)", t):
                items.append(t)

    for t in items:
        t = re.sub(r"\s+", " ", t).strip().rstrip(".").strip()
        if not t:
            continue
        banned["stale_stat_drift"].extend(nums_in(t))
        if re.search(r"authority|Domain|Nirvana|resurrection|True Body|invincible"
                     r"|perfect .{0,18}mastery|battle armor|Spiritual attribute"
                     r"|coloured|Glacial|Black Phoenix|Halcyon", t, re.I):
            banned["forbidden_future_power"].append(t)
        if re.search(r"reveal|fourth ring|Emerald Demon Bird|external soul bone|necklace"
                     r"|Rainbow Dragon|auction|wind attribute", t, re.I):
            banned["forbidden_currentization"].append(t)
    for line in re.findall(r"^- (?:No|Do not|any|second) (.+)", handoff, re.M):
        banned["deleted_mistake_route"].append(re.sub(r"\s+", " ", line.strip()))
    for line in re.findall(r"^- (?:any|second|deleted) (.+)", status, re.M):
        banned["deleted_mistake_route"].append(re.sub(r"\s+", " ", line.strip()))
    for t in re.findall(r"Do not ([^\n]{8,90})", status):
        banned["banned_pacing"].append("do not " + re.sub(r"\s+", " ", t).strip().rstrip("."))
    banned = {k: sorted(set(x for x in v if x)) for k, v in banned.items()}

    # ---- adopt the project's own registries when present (authoritative) ----
    NAT = native_manifest(proj)
    native = bool(NAT)
    if native:
        lit = NAT.get("latest_story_body_forbidden_literals") or []
        reg = NAT.get("latest_story_body_forbidden_regexes") or []
        fut = NAT.get("future_bans") or []
        banned["authoritative_literals"] = lit
        banned["authorative_regexes"] = reg
        banned["authoritative_future_bans"] = fut
        for t in lit:
            if re.fullmatch(r"[A-Za-z0-9,.'’\-]{3,40}", t):
                banned["stale_stat_drift"].append(t)
        banned = {k: sorted(set(x for x in v if x)) for k, v in banned.items()}

    # Grep-able tokens: numbers + short proper-noun phrases. Long sentences stay as context.
    flat_bans: dict[str, list[str]] = {}
    GREP_SAFE = [k for k in banned if k != "counts" and k != "phrasal_note"
                 and k != "banned_pacing"]
    for k in GREP_SAFE:
        v = banned[k]
        toks: set[str] = set()
        for t in v:
            toks.update(nums_in(t))
            for phrase in re.findall(r"([A-Z][A-Za-z]*(?: [A-Z][A-Za-z]*){1,3})", t):
                if 6 <= len(phrase) <= 34 and not phrase.startswith(("Do ", "Not ")):
                    toks.add(phrase)
        if k == "forbidden_future_power":
            for t in v:
                m = re.search(r"(Phoenix God authority|Phoenix Domain|Nirvana[^,;]*"
                              r"|Martial Soul True Body|invincible defense[^,;]*"
                              r"|completed battle armor|perfect Ultimate Fire mastery"
                              r"|perfect combat flight mastery|Ultimate Spiritual attribute)", t)
                if m:
                    toks.add(m.group(1).strip().rstrip(".")[:40])
            toks.discard("")
        if k == "forbidden_currentization":
            for t in v:
                m = re.search(r"(public Yan Shuo'er reveal|Yan current fourth ring"
                              r"|Emerald Demon Bird|external soul bone|five-coloured Phoenix"
                              r"|Rainbow Dragon[^,;]*|Dragon Queen necklace[^,;]*)", t)
                if m:
                    toks.add(m.group(1).strip().rstrip(".")[:40])
            toks.discard("")
        flat_bans[k] = sorted(toks)[:48]
    banned["counts"] = {k: len(v) for k, v in banned.items()}

    # ---------- characters ----------
    def sec(title):
        hits = list(re.finditer(r"^## \d+\. (.+)$", status, re.M))
        for i, h in enumerate(hits):
            if re.search(title, h.group(1)):
                end = hits[i + 1].start() if i + 1 < len(hits) else len(status)
                return status[h.end():end]
        return ""
    characters: dict[str, dict] = {}
    for body, dorm in ((sec(r"Dorm333 current status"), "Dorm333"),
                        (sec(r"Dorm336 current status"), "Dorm336"),
                        (sec(r"Other teams"), "Other")):
        for line in body.splitlines():
            if not re.match(r"^- \S", line):
                continue
            m = re.match(r"^- ([^:]+):\s*(.*)$", line.strip())
            if not m:
                continue
            label, rest = m.group(1).strip(), re.sub(r"\s+", " ", m.group(2).strip())
            who = next((c for c in CHARS if label.startswith(c)), None)
            if not who or who in characters:
                continue
            characters[who] = {"dorm": "Dorm336" if who == "Yan Shuo" else dorm,
                              "state": rest,
                              "rank": (int(re.search(r"Rank(\d+)", rest).group(1))
                                       if re.search(r"Rank(\d+)", rest) else None),
                              "sp": (int(re.search(r"SP(\d{2,5})", rest).group(1))
                                    if re.search(r"SP(\d{2,5})", rest) else None)}
    yan_sheet = {}
    d336 = sec(r"Dorm336 current status")
    for line in d336.splitlines():
        if re.match(r"^- [A-Za-z][A-Za-z /'-]+:", line):
            k, v = line.strip()[2:].split(":", 1)
            if k.strip() in ("Martial soul", "Rings", "Fire", "Wings/flight",
                             "No-fusion serious baseline", "Soul Spirit mechanics audit result"):
                yan_sheet[k.strip()] = re.sub(r"\s+", " ", v.strip())
    if "Yan Shuo" in characters:
        characters["Yan Shuo"].update({
            "public_identity": "Yan Shuo / he",
            "reveal_status": "none",
            "power_floor": "low Soul King-class effective threat floor in serious no-full-fusion release",
            "power_ceiling": "no perfect Ultimate Fire mastery; no combat-flight perfection",
            "sheet": yan_sheet})

    # ---------- firewalls (structured, enforceable) ----------
    firewalls = []
    fws = re.search(r"## 7\. Current relationship/firewall state\n(.*?)## 8\.", status, re.S)
    for line in (fws.group(1).splitlines() if fws else []):
        t = line.strip()
        if not t.startswith("- "):
            continue
        t = t[2:]
        # A firewall gates a FACT, not a feeling — skip pure relationship prose.
        if not re.search(r"reveal|knows|private|hidden|secret|not in|may know|identity", t, re.I):
            continue
        if re.search(r"not ordinary friendship|not a ranked list|safety|not distrust"
                     r"|emotional weight|changed a lot|Rebuilt Chapter|among each other"
                     r"|is not a reward", t, re.I):
            continue
        if re.search(r"no confession|no mature romance|no identity reveal|no secret dump", t, re.I):
            state = "HIDDEN"
        elif re.search("may know|public clues|without demanding|not private", t, re.I):
            state = "KNOWN PARTLY"
        elif re.search(r"no reveal|not reveal|remains private|not in private", t, re.I):
            state = "HIDDEN"
        else:
            state = "KNOWN PARTLY"
        firewalls.append({"character": "Lan Xuanyu / Yan Shuo" if "Lan" in t and "Yan" in t
                          else "Yan Shuo" if "Yan" in t else "Lan Xuanyu",
                          "topic": re.split(r"[,.;]", t)[0][:58],
                          "state": state,
                          "earliest_valid_change": "explicit author-authorized reveal scene",
                          "rule": t})
    secrets = re.search(r"Lan secrets still hidden: ([^.]+)\.", status)
    if secrets:
        for s in re.split(r",\s*(?=[A-Z])", secrets.group(1).strip()):
            firewalls.append({"character": "Lan Xuanyu", "topic": s.strip()[:60],
                              "state": "HIDDEN",
                              "earliest_valid_change": "on-page disclosure to that character",
                              "rule": f"Not known to any other character: {s.strip()}."})
    # The codex is the authoritative firewall register when present: each section is a gated
    # topic; each bullet a rule. Receipt-derived gates are only a fallback.
    fw_path = proj / "codex/KNOWLEDGE_FIREWALLS.md"
    if fw_path.exists():
        fwtxt = read(fw_path)
        heads = list(re.finditer(r"^## \d+\. (.+)$", fwtxt, re.M))
        codex_fw = []
        for i, hm in enumerate(heads):
            topic = hm.group(1).strip()
            end = heads[i + 1].start() if i + 1 < len(heads) else len(fwtxt)
            body = fwtxt[hm.end():end]
            bullets = [x.strip()[2:] for x in body.splitlines() if x.strip().startswith("- ")]
            gated = [x for x in bullets
                     if re.search(r"\bnot\b|never|must not|unrevealed|hidden|does not know"
                                  r"|without learning|only when", x, re.I)]
            if not gated:
                continue
            who = next((c for c in CHARS if c.lower()[:5] in topic.lower()), "multiple")
            codex_fw.append({"character": who, "topic": topic[:70],
                             "state": "HIDDEN" if re.search(r"reveal|identity|secret", topic, re.I)
                             else "KNOWN PARTLY",
                             "earliest_valid_change":
                                 "explicit on-page disclosure in a verified source chapter",
                             "rule": f"{len(gated)} gate rules; strongest — {gated[0][:170]}"})
        if codex_fw:
            firewalls = codex_fw
    knows = re.search(r"Yan may know (.+?)\.\n", status, re.S)
    if knows:
        body = re.sub(r"\s+", " ", knows.group(1))
        cut = body.split("but not")[0].strip().rstrip(",")
        firewalls.append({"character": "Yan Shuo", "topic": "Dorm333 / Lan public results",
                          "state": "KNOWN PARTLY",
                          "earliest_valid_change": "official academy channel publishes it",
                          "rule": f"May know: {cut}. May NOT know: "
                                  f"{body.split('but not')[-1].strip().rstrip('.')}"})

    # ---------- branches ----------
    branches = {}
    for name in ("archive/rejected_post48_2026-09-17/", "archive/rejected_overcorrection_2026-09-17/"):
        branches[name.rstrip("/").split("/")[-1]] = {
            "status": "superseded", "chapters": sorted(superseded), "note": branch_note,
            "authority": "none — historical evidence only"}
    qm = re.search(r"## 9\. Historical/audit quarantine\n(.*?)(?:\n## |\Z)",
                   raw.get("FULL_PROJECT_DEEP_AUDIT_AND_CLASSIFICATION_2026-09-13.md", ""), re.S)
    quarantine_notes = [x.strip()[2:] for x in qm.group(1).splitlines() if x.strip().startswith("- ")] \
        if qm else []

    stale_claims = []
    for name, blob in raw.items():
        if "SKILL_CHECK" not in name.upper():
            continue
        m = re.search(r"Latest fic chapter:\s*Chapter(\d+)", blob)
        if m and int(m.group(1)) != edge_ch:
            stale_claims.append(f"{name} claims latest fic Chapter{m.group(1)}; live edge is "
                                f"Chapter{edge_ch} (per {edge_src}, {edge_day}). Stale.")

    manifest = {
        "schema": SCHEMA,
        "project": "Soul Land 4 — Fire Phoenix OC Fic",
        "generated": date.today().isoformat(),
        "generator": "scan_project.py",
        "source_corpus": {"dir": str(corpus), "files": len(files),
                          "snapshot_files_excluded": len(snapshots),
                          "newest_receipt_date": edge_day},
        "edge_authority": edge_src,
        "status_panel_mirror": status_name,
        "edge": {"fic_chapter": edge_ch, "fic_title": edge_title, "declared_by": edge_src,
                 "declared_on": edge_day, "canon_consumed": consumed,
                 "canon_consumed_title": consumed_title, "next_source": nxt,
                 "next_source_title": nxt_title,
                 "accepted_chapters": sorted(l["fic"] for l in ledger
                                             if l["status"] == "accepted")},
        "canon_numbering": [{"fic": l["fic"], "canon": l["canon"], "status": l["status"],
                             "validation": l["validation"]} for l in ledger],
        "characters": characters,
        "knowledge_firewalls": firewalls,
        "banned_tokens": flat_bans,
        "banned_sentences": {k: v for k, v in banned.items() if k != "counts"},
        "enforce": (sorted(set(NAT.get("latest_story_body_forbidden_literals") or []))
                    if native else
                    sorted({t for t in (flat_bans.get("stale_stat_drift") or [])
                            if re.search(r"\d", t)})),
        "enforce_regexes": (NAT.get("latest_story_body_forbidden_regexes") or []) if native else [],
        "required_patterns": (NAT.get("latest_story_body_required_patterns") or []) if native else [],
        "provenance": ("native manifest adopted (schema %s)" % NAT.get("schema_version")
                       if native else "derived from audit corpus"),
        "advisory_review": sorted({t for k in ("forbidden_future_power", "forbidden_currentization")
                                   for t in (flat_bans.get(k) or [])}),
        "pacing": {"mode": "compressed",
                   "rule": "compress routine canon beats; expand only meaningful "
                           "character/system/butterfly/relationship/tactical change",
                   "banned_mode": "one canon chapter = one fic chapter"},
        "information_discipline": "ACTIVE",
        "branches": branches,
        "quarantine_notes": quarantine_notes,
        "stale_claims": stale_claims,
        "edge_authority": edge_src,
        "foundation_paths": sorted(set(lock_paths)),
        "metrics": {"PASS_tokens": sum(len(re.findall(r"\bPASS\b", t)) for t in raw.values()),
                    "receipt_files": len(files),
                    "chapters_validated": len(val), "chapters_synced": len(sync),
                    "quarantined_chapters": sorted(superseded)},
    }
    (inst / "foundation").mkdir(parents=True, exist_ok=True)
    (inst / "STORYOS_STATE.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ---------- cards ----------
    for sub, items, render in (
        ("characters", list(characters.items()), render_char),
        ("locks", lock_cards, render_lock),
    ):
        d = inst / "canon" / sub
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.card.md"):
            old.unlink()
        for it in items:
            fname, text = render(it)
            (d / fname).write_text(text, encoding="utf-8")

    # ---------- ledgers ----------
    (inst / "ledgers").mkdir(parents=True, exist_ok=True)
    (inst / "ledgers" / "CANON_LEDGER.md").write_text(ledger_md(ledger), encoding="utf-8")
    (inst / "ledgers" / "BRANCH_LEDGER.md").write_text(
        branch_md(branches, stale_claims, edge_ch, edge_src, edge_day, quarantine_notes),
        encoding="utf-8")
    (inst / "BANNED_TOKENS.json").write_text(
        json.dumps({"note": "regression tokens — grep chapters for these; any hit is a drift bug",
                    "generated": date.today().isoformat(), "banned_tokens": flat_bans},
                   indent=2), encoding="utf-8")

    m = manifest["metrics"]
    print(f"install dir       : {inst}")
    print(f"corpus            : {corpus}  ({m['receipt_files']} files, newest {edge_day})")
    print(f"live edge         : after Chapter{edge_ch} \"{edge_title}\"  [from {edge_src}]")
    print(f"canon             : consumed {consumed} → next {nxt} {nxt_title}")
    print(f"ledger            : {len(ledger)} chapters · {m['chapters_validated']} validated · "
          f"{m['chapters_synced']} synced")
    print(f"accepted          : {len(manifest['edge']['accepted_chapters'])}   "
          f"quarantined: {len(m['quarantined_chapters'])} {m['quarantined_chapters']}")
    print(f"locks extracted   : {len(lock_cards)}   banned tokens: "
          f"{sum(len(v) for v in flat_bans.values())}")
    print(f"provenance        : {manifest['provenance']}   enforce={len(manifest['enforce'])} "
          f"regex-bans={len(manifest['enforce_regexes'])}")
    print(f"characters        : {len(characters)}   firewalls: {len(firewalls)}")
    print(f"stale claims      : {len(stale_claims)}")
    for s in stale_claims:
        print(f"   ! {s}")
    print(f"wrote             : foundation/STORYOS_STATE.json + "
          f"{len(characters)+len(lock_cards)} cards + 2 ledgers")
    return 0


def slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:52] or "item"


def render_char(item):
    name, st = item
    meta = {"card": "character", "id": slug(name), "dorm": st.get("dorm"),
            "rank": st.get("rank"), "sp": st.get("sp"),
            "public_identity": st.get("public_identity"),
            "reveal_status": st.get("reveal_status"),
            "power_floor": st.get("power_floor"), "power_ceiling": st.get("power_ceiling")}
    body = ["```storyos-meta", json.dumps({k: v for k, v in meta.items() if v is not None},
                                          indent=2), "```", "",
            "## Current state", st.get("state", ""), ""]
    for k, v in (st.get("sheet") or {}).items():
        body += [f"### {k}", v, ""]
    return f"{slug(name)}.card.md", card_doc(f"Character — {name}", body)


def render_lock(c):
    meta = {"card": "lock", "id": slug(c["title"]), "source": c["source"],
            "source_date": c["source_date"], "authority": "user-locked decision",
            "status": "active"}
    return (f"{slug(c['title'])}-{c['source_date']}.card.md",
            card_doc(f"Lock — {c['title']}",
                     ["```storyos-meta", json.dumps(meta, indent=2), "```", "", c["statement"], ""]))


def card_doc(title: str, body: list[str]) -> str:
    return (f"# {title}\n\nGenerated by scan_project.py — edit canon, then re-scan. "
            f"Do not hand-edit this card as a source of truth.\n\n" + "\n".join(body) + "\n")


def ledger_md(ledger) -> str:
    rows = "\n".join(
        f"| Ch{l['fic']} | {l['canon']} | {l['status']} | {l['validation'] or '—'} | "
        f"{l['support_sync'] or '—'} |" for l in ledger)
    return ("# Canon Ledger\n\nFic chapter ↔ consumed canon source, with the receipt that proved it.\n"
            "\n| Fic | Canon source | Status | Validation | Support sync |\n|---|---|---|---|---|\n"
            + rows + "\n\nStatus `quarantined-superseded` = evidence of a rejected attempt. Never a\n"
            "starting point. See `BRANCH_LEDGER.md`.\n")


def branch_md(branches, stale, edge_ch, edge_src, edge_day, notes) -> str:
    bl = "\n".join(f"- **{k}** — status `{v['status']}`, chapters {v['chapters']}, "
                   f"authority: {v['authority']}" for k, v in branches.items())
    sl = "\n".join(f"- {s}" for s in stale) or "- none detected"
    ql = "\n".join(f"- {n}" for n in notes) or "- none"
    return (f"# Branch Ledger\n\n"
            f"## Live branch\n- edge: after **Chapter{edge_ch}** — declared by `{edge_src}` on {edge_day}\n\n"
            f"## Superseded branches\n{bl}\n\n"
            f"## Stale/contradicting claims detected\n{sl}\n\n"
            f"## Quarantine policy\n{ql}\n\n"
            f"Any agent reading a superseded receipt as live state will continue from rejected work.\n"
            f"Rule: **newest dated receipt on the ACTIVE branch wins.**\n")


if __name__ == "__main__":
    sys.exit(main())
