#!/usr/bin/env python3
"""Build a local searchable metadata index for every recovered workshop file."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {ROOT / "provenance" / "WORKSHOP_FILE_INDEX.json"}


def describe(path: Path) -> dict:
    data = path.read_bytes()
    record = {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "kind": path.suffix.lower().lstrip(".") or "no-extension",
    }
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        record["encoding"] = "binary-or-non-utf8"
        return record
    record["encoding"] = "utf-8"
    title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), None)
    if title:
        record["h1"] = title
    for label, regex in {
        "live_edge": r"(?im)^Live edge:\s*(.+)$",
        "status": r"(?im)^Status:\s*(.+)$",
        "archive_marker": r"(?im)^(?:#\s*)?.{0,30}(?:SUPERSEDED|ARCHIVED|QUARANTINED).{0,90}$",
    }.items():
        match = re.search(regex, text)
        if match:
            value = match.group(1) if match.lastindex else match.group(0)
            record[label] = re.sub(r"\s+", " ", value).strip()
    return record


def main() -> int:
    records = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in SKIP or "__pycache__" in path.parts:
            continue
        records.append(describe(path))
    index = {
        "purpose": "Local metadata index only; original project files remain in their recovered source layers.",
        "file_count": len(records),
        "records": records,
    }
    output = ROOT / "provenance" / "WORKSHOP_FILE_INDEX.json"
    output.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"indexed={len(records)} output={output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
