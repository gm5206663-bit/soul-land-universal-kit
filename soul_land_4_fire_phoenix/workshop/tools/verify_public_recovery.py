#!/usr/bin/env python3
"""Verify all recovered blobs against the provenance manifest without network access."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "provenance" / "PUBLIC_RECOVERY_MANIFEST.json"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures: list[str] = []
    count = 0
    byte_count = 0
    for result in manifest["results"]:
        if not result["ok"]:
            failures.append(f"source recovery failed: {result['local_path']}")
            continue
        path = ROOT / result["local_path"]
        if not path.is_file():
            failures.append(f"missing: {result['local_path']}")
            continue
        data = path.read_bytes()
        sha = git_blob_sha(data)
        if sha != result["git_blob_sha"]:
            failures.append(f"SHA mismatch: {result['local_path']}")
            continue
        count += 1
        byte_count += len(data)
    if failures:
        print("FIRE_PHOENIX_PUBLIC_WORKSHOP: FAIL")
        for failure in failures[:30]:
            print("-", failure)
        if len(failures) > 30:
            print(f"- … {len(failures) - 30} additional failures")
        return 1
    print("FIRE_PHOENIX_PUBLIC_WORKSHOP: PASS")
    print(f"- files verified: {count}")
    print(f"- bytes verified: {byte_count}")
    print("- all files match the recorded public Git blob SHA values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
