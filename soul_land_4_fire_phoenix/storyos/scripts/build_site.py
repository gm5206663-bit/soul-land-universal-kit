#!/usr/bin/env python3
"""
build_site.py — StoryOS Control Centre, built FROM the foundation layer.

    python3 scripts/build_site.py [project_dir] [out_dir]

State comes from foundation/CURRENT_STATE_MANIFEST.json + the generated docs, so the
dashboard cannot disagree with the files. Run scan_project.py first if canon changed.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

FIREWALL_STATES = ("KNOWN", "SUSPECTED", "UNKNOWN", "FALSE BELIEF",
                   "KNOWN PARTLY", "DISBELIEF", "HIDDEN")


def parse_cards(d: Path) -> list[dict]:
    out = []
    for p in sorted(d.glob("*.card.md")) if d.is_dir() else []:
        m = re.search(r"```storyos-meta\n(.*?)\n```", p.read_text(encoding="utf-8"), re.S)
        meta = json.loads(m.group(1)) if m else {}
        meta["_file"] = p.name
        body = re.sub(r"^# .*?\n", "", p.read_text(encoding="utf-8"), count=1, flags=re.S)
        body = re.sub(r"```storyos-meta\n.*?\n```", "", body, flags=re.S)
        meta["_body"] = re.sub(r"\n{3,}", "\n\n", body).strip()
        out.append(meta)
    return out


def main() -> int:
    proj = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else proj / "site"
    # Prefer the generated v3 state (full derived picture); fall back to a native manifest.
    cands = [out / "STORYOS_STATE.json", out.parent / "STORYOS_STATE.json",
             proj / "storyos" / "STORYOS_STATE.json",
             proj / "foundation" / "CURRENT_STATE_MANIFEST.json"]
    mf = next((c for c in cands if c.exists()), None)
    if mf is None:
        print("build_site: no state found — run scripts/scan_project.py first")
        return 2
    install = out.parent if out.parent.exists() else out
    M = json.loads(mf.read_text(encoding="utf-8"))

    # validator status is embedded so Overview shows the real gate, not a hope
    import subprocess
    tool = proj / "tools" / "storyos_validate.py"
    if not tool.exists():
        tool = Path(__file__).resolve().parent.parent / "tools" / "storyos_validate.py"
    try:
        v = subprocess.run([sys.executable, str(tool), "--project", str(proj),
                            "--phase", "full"], capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.SubprocessError) as e:
        class _R: stdout = f"validator unavailable: {e}"; returncode = 2
        v = _R()
    vtext = v.stdout.strip()
    vm = re.search(r"STORYOS_VALIDATE: (\w+)\s+\(phase=\w+, errors=(\d+), warnings=(\d+)\)", vtext)
    validation = {
        "result": vm.group(1) if vm else "UNKNOWN",
        "errors": int(vm.group(2)) if vm else None,
        "warnings": int(vm.group(3)) if vm else None,
        "findings": [l.strip() for l in vtext.splitlines()
                     if re.match(r"\[(FAIL|WARN|info)\]", l.strip())],
        "gate": next((l.replace("GATE:", "").strip() for l in vtext.splitlines()
                      if l.strip().startswith("GATE:")), ""),
        "raw": vtext,
    }

    ledgers = {}
    for name in ("CANON_LEDGER", "BRANCH_LEDGER"):
        p = next((q for q in (install / "ledgers" / f"{name}.md",
                             proj / "canon_coverage" / f"{name}.md") if q.exists()), None)
        if p is None:
            ledgers[name] = ""
            continue
        ledgers[name] = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""

    locks = parse_cards(install / "canon" / "locks") or parse_cards(proj / "foundation" / "canon" / "locks")
    charcards = (parse_cards(install / "canon" / "characters")
                 or parse_cards(proj / "foundation" / "canon" / "characters"))
    audits = sorted(p.name for p in (proj / "audits").glob("*.md")) if (proj / "audits").is_dir() else []

    data = {
        "project": M.get("project"),
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "schema": M.get("schema"),
        "edge": M.get("edge", {}),
        "metrics": M.get("metrics", {}),
        "ledger": M.get("canon_numbering", []),
        "characters": M.get("characters", {}),
        "character_cards": charcards,
        "locks": locks,
        "foundation_paths": M.get("foundation_paths", []),
        "firewalls": M.get("knowledge_firewalls", []),
        "firewall_states": list(FIREWALL_STATES),
        "bans": M.get("banned_tokens", {}),
        "enforce": M.get("enforce", []),
        "advisory": M.get("advisory_review", []),
        "pacing": M.get("pacing", {}),
        "branches": M.get("branches", {}),
        "quarantine_notes": M.get("quarantine_notes", []),
        "stale_claims": M.get("stale_claims", []),
        "validation": validation,
        "ledgers": ledgers,
        "audit_files": audits,
        "files": {"corpus_files": M.get("source_corpus", {}).get("files"),
                  "information_discipline": M.get("information_discipline"),
                  "card_count": len(locks) + len(charcards)},
        "control_centre": {
            "url": "https://storyos-control-centre.gm5206663.chatgpt.site/",
            "verified_http_status": 401,
            "note": "ChatGPT Sites auth gate — unreadable externally. This local build is "
                    "the mirror that can actually be verified.",
        },
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / "STATE.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tpl = Path(__file__).with_name("site_template.html").read_text(encoding="utf-8")
    (out / "index.html").write_text(tpl.replace("/*__STATE__*/null",
                                                 json.dumps(data, ensure_ascii=False)),
                                    encoding="utf-8")
    e = data["edge"]
    print(f"project         : {data['project']}  ({data['schema']})")
    print(f"live edge       : after Chapter{e.get('fic_chapter')} \"{e.get('fic_title')}\"")
    print(f"canon           : consumed {e.get('canon_consumed')} → next {e.get('next_source')}")
    print(f"ledger          : {len(data['ledger'])} rows · accepted "
          f"{len(e.get('accepted_chapters', []))} · quarantined {data['metrics'].get('quarantined_chapters')}")
    print(f"cards           : {len(locks)} locks + {len(charcards)} characters")
    print(f"firewalls       : {len(data['firewalls'])}   enforce tokens: {len(data['enforce'])}")
    print(f"validator       : {validation['result']} — errors={validation['errors']} "
          f"warnings={validation['warnings']}  ({validation['gate']})")
    print(f"wrote           : {out/'index.html'} ({(out/'index.html').stat().st_size/1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
