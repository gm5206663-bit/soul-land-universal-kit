#!/usr/bin/env python3
"""Recover every publicly accessible Fire Phoenix project artifact into this workshop.

No git clone and no credential are used. Each file is written with a source URL, Git blob
SHA verification where available, and group provenance in the generated manifest.

This cannot retrieve the private canonical repository; see ACTIVE_START_HERE.md.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
HEADERS = {"User-Agent": "Arena-FirePhoenix-Workshop-Recovery"}
KIT = "gm5206663-bit/soul-land-universal-kit"
STORYOS = "gm5206663-bit/storyos-site"
UNIVERSAL = "gm5206663-bit/the-universal-storyline-creation"
SNAPSHOT_REF = "3d54b4e0d5eb"
SNAPSHOT_PREFIX = (
    "arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/"
    "soul_land_4_fire_phoenix/"
)


def get_json(url: str) -> dict:
    with urlopen(Request(url, headers=HEADERS), timeout=120) as response:
        return json.load(response)


def tree(repo: str, ref: str) -> list[dict]:
    payload = get_json(f"https://api.github.com/repos/{repo}/git/trees/{quote(ref, safe='')}?recursive=1")
    if payload.get("truncated"):
        raise RuntimeError(f"tree was truncated: {repo}@{ref}")
    return payload["tree"]


def kit_main_related(path: str) -> bool:
    lower = path.lower()
    return path in {
        "SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md",
        "WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md",
    } or "fire_phoenix" in lower or "sl4_fire_phoenix" in lower or "sl4-canon" in lower


def plans() -> list[dict]:
    snapshot = [entry for entry in tree(KIT, SNAPSHOT_REF)
                if entry["type"] == "blob" and entry["path"].startswith(SNAPSHOT_PREFIX)]
    kit_main = [entry for entry in tree(KIT, "main")
                if entry["type"] == "blob" and kit_main_related(entry["path"])]
    storyos = [entry for entry in tree(STORYOS, "main") if entry["type"] == "blob" and (
        entry["path"].startswith("published-site/soul_land_4/")
        or entry["path"] in {
            "framework/foundation/canon/characters/yan-shuo.card.md",
            "framework/archive/quarantine/CHAPTER_52_VALIDATION_2026-09-17.md",
            "framework/archive/quarantine/CHAPTER_53_VALIDATION_2026-09-17.md",
        }
    )]
    # The project-specific state record is small but essential; avoid collecting unrelated projects.
    universal_tree = tree(UNIVERSAL, "main")
    universal = [entry for entry in universal_tree if entry["type"] == "blob" and entry["path"] == "state/projects/sl4_fire_phoenix.json"]
    return [
        {
            "id": "chapter51_managed_snapshot",
            "description": "Complete public project snapshot at the Chapter-51 edge; all original project files including its internal archives and audits.",
            "repo": KIT,
            "ref": SNAPSHOT_REF,
            "entries": snapshot,
            "destination": "sources/chapter51_managed_snapshot/soul_land_4_fire_phoenix",
            "relpath": lambda path: path[len(SNAPSHOT_PREFIX):],
        },
        {
            "id": "current_kit_related_public_history",
            "description": "All currently public Fire-Phoenix-related paths in soul-land-universal-kit, including stale archives and legacy foundation exports. Historical/quarantine status is retained, not erased.",
            "repo": KIT,
            "ref": "main",
            "entries": kit_main,
            "destination": "sources/soul_land_universal_kit_main_related",
            "relpath": lambda path: path,
        },
        {
            "id": "storyos_current_public_layer",
            "description": "Published Chapter 1–52 prose, Chapter-52 current state/gate/rules, generated cards, and explicitly marked quarantine receipts.",
            "repo": STORYOS,
            "ref": "main",
            "entries": storyos,
            "destination": "sources/storyos_current_public_layer",
            "relpath": lambda path: path,
        },
        {
            "id": "universal_storyline_project_record",
            "description": "Project-map record; its embedded Chapter-31 values are retained as explicitly stale evidence only.",
            "repo": UNIVERSAL,
            "ref": "main",
            "entries": universal,
            "destination": "sources/the_universal_storyline_creation",
            "relpath": lambda path: path,
        },
    ]


def raw_url(repo: str, ref: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{repo}/{quote(ref, safe='')}/{quote(path, safe='/')}"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def download_one(job: dict) -> dict:
    target: Path = job["target"]
    target.parent.mkdir(parents=True, exist_ok=True)
    url = raw_url(job["repo"], job["ref"], job["source_path"])
    # Retries protect against transient GitHub raw-host responses without using auth.
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urlopen(Request(url, headers=HEADERS), timeout=120) as response:
                data = response.read()
            actual = git_blob_sha(data)
            if actual != job["expected_git_blob_sha"]:
                raise RuntimeError(f"Git blob SHA mismatch: expected {job['expected_git_blob_sha']}, got {actual}")
            temporary = target.with_name(target.name + ".part")
            temporary.write_bytes(data)
            os.replace(temporary, target)
            return {
                "ok": True,
                "group": job["group"],
                "source_path": job["source_path"],
                "local_path": str(target.relative_to(ROOT)),
                "url": url,
                "bytes": len(data),
                "git_blob_sha": actual,
            }
        except Exception as exc:  # retry only temporary or external errors
            last_error = exc
            time.sleep(0.6 * (attempt + 1))
    return {
        "ok": False,
        "group": job["group"],
        "source_path": job["source_path"],
        "local_path": str(target.relative_to(ROOT)),
        "url": url,
        "error": repr(last_error),
    }


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    all_plans = plans()
    jobs: list[dict] = []
    group_metadata = []
    for plan in all_plans:
        destination = ROOT / plan["destination"]
        destination.mkdir(parents=True, exist_ok=True)
        group_metadata.append({
            key: value for key, value in plan.items() if key not in {"entries", "relpath"}
        } | {"file_count_expected": len(plan["entries"]), "bytes_expected": sum(e.get("size", 0) for e in plan["entries"])})
        for entry in plan["entries"]:
            relpath = plan["relpath"](entry["path"])
            jobs.append({
                "group": plan["id"],
                "repo": plan["repo"],
                "ref": plan["ref"],
                "source_path": entry["path"],
                "target": destination / relpath,
                "expected_git_blob_sha": entry["sha"],
            })

    results: list[dict] = []
    # Raw GitHub host requests, not API requests: concurrency keeps recovery practical.
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(download_one, job) for job in jobs]
        for number, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            results.append(result)
            if number % 100 == 0 or not result["ok"]:
                print(f"[{number}/{len(jobs)}] {'OK' if result['ok'] else 'ERROR'} {result['local_path']}", flush=True)

    results.sort(key=lambda item: (item["group"], item["local_path"]))
    manifest = {
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": "public GitHub tree + raw-blob recovery; no credential; Git blob SHA verified",
        "private_repository_note": "The canonical private repository is not publicly readable. This workshop retains all identified public project artifacts, not an invented private export.",
        "groups": group_metadata,
        "results": results,
        "summary": {
            "files_expected": len(jobs),
            "files_recovered": sum(1 for result in results if result["ok"]),
            "files_failed": sum(1 for result in results if not result["ok"]),
            "bytes_recovered": sum(result.get("bytes", 0) for result in results if result["ok"]),
        },
    }
    provenance = ROOT / "provenance"
    provenance.mkdir(exist_ok=True)
    (provenance / "PUBLIC_RECOVERY_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (provenance / "PUBLIC_RECOVERY_SUMMARY.txt").write_text(
        "\n".join([
            f"expected={manifest['summary']['files_expected']}",
            f"recovered={manifest['summary']['files_recovered']}",
            f"failed={manifest['summary']['files_failed']}",
            f"bytes={manifest['summary']['bytes_recovered']}",
        ]) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest["summary"], ensure_ascii=False))
    return 0 if manifest["summary"]["files_failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
