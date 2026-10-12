#!/usr/bin/env python3
"""Static governance and supply-chain checks for the private Fire Phoenix GitHub repository."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/validate.yml"

REQUIRED_FILES = (
    "CODEOWNERS",
    ".editorconfig",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/continuity-correction.yml",
    ".github/ISSUE_TEMPLATE/source-claim-correction.yml",
    ".github/ISSUE_TEMPLATE/publication-decision.yml",
    "CHANGELOG.md",
    "NOTICE.md",
    "PUBLICATION_AND_DATA_CLASSIFICATION.md",
    "BACKUP_AND_RECOVERY.md",
    "GITHUB_ADMIN_SETTINGS_CHECKLIST.md",
    "GITHUB_PROJECT_SETUP.md",
    "tools/create_git_bundle_backup.sh",
    "tools/install_local_hooks.sh",
    "LOCAL_DEVELOPER_SETUP.md",
    "GITHUB_UPGRADE_AUDIT_2026-10-03.md",
    "GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md",
)

REQUIRED_VALIDATORS = (
    "tools/validate_github_governance.py",
    "tools/verify_public_recovery.py",
    "tools/validate_workshop.py",
    "tools/validate_replacement_line_48_60.py",
    "tools/validate_current_v2_line.py",
    "validate_option_a_staging.py",
    "tools/validate_local_accepted_v2_release.py",
)

SECRET_PATTERNS = {
    "GitHub classic PAT": re.compile(rb"ghp_[A-Za-z0-9]{36}"),
    "GitHub fine-grained PAT": re.compile(rb"github_pat_[A-Za-z0-9_]{30,}"),
    "AWS access key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "private-key marker": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Bearer credential": re.compile(rb"Authorization:\s*Bearer\s+[A-Za-z0-9._-]{20,}", re.I),
}


def repository_files() -> list[Path]:
    """Return tracked plus nonignored pending files so pre-commit scans are meaningful."""
    try:
        result = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"unable to enumerate repository files: {exc}") from exc
    return [ROOT / raw.decode("utf-8", "surrogateescape") for raw in result.split(b"\0") if raw]


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing governance artifact: {relative}")

    if not WORKFLOW.is_file():
        failures.append("missing GitHub validation workflow")
        text = ""
    else:
        text = WORKFLOW.read_text(encoding="utf-8")

    workflow_checks = {
        "push trigger": "  push:" in text,
        "pull-request trigger": "  pull_request:" in text,
        "manual trigger": "  workflow_dispatch:" in text,
        "read-only default token": "permissions:\n  contents: read" in text,
        "concurrency control": "concurrency:" in text and "cancel-in-progress: true" in text,
        "no pull_request_target": "pull_request_target" not in text,
        "checkout credentials disabled": "persist-credentials: false" in text,
    }
    for label, ok in workflow_checks.items():
        if not ok:
            failures.append(f"workflow policy missing: {label}")

    uses = re.findall(r"^\s*uses:\s*([^\s@]+)@([^\s#]+)", text, flags=re.M)
    if not uses:
        failures.append("workflow has no actions to inspect")
    for action, revision in uses:
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            failures.append(f"action is not pinned to immutable commit SHA: {action}@{revision}")

    for validator in REQUIRED_VALIDATORS:
        if validator not in text:
            failures.append(f"workflow does not run required validator: {validator}")

    dependabot = ROOT / ".github/dependabot.yml"
    if dependabot.is_file() and "package-ecosystem: github-actions" not in dependabot.read_text(encoding="utf-8"):
        failures.append("Dependabot does not monitor GitHub Actions")

    codeowners = ROOT / "CODEOWNERS"
    if codeowners.is_file() and "@gm5206663-bit" not in codeowners.read_text(encoding="utf-8"):
        failures.append("CODEOWNERS lacks the repository owner")

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    if "publicly mirrored on GitHub" not in readme or "not a public StoryOS application" not in readme:
        failures.append("README does not clearly distinguish public repository visibility from StoryOS publication")

    for path in repository_files():
        try:
            content = path.read_bytes()
        except OSError as exc:
            failures.append(f"cannot scan tracked file {path.relative_to(ROOT)}: {exc}")
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"possible {label} in tracked file: {path.relative_to(ROOT)}")

    if failures:
        print("GITHUB_GOVERNANCE_VALIDATION: FAIL")
        print(*[f"- {failure}" for failure in failures], sep="\n")
        return 1

    print("GITHUB_GOVERNANCE_VALIDATION: PASS")
    print("- GitHub workflow is least-privilege, concurrency-controlled, and SHA-pinned")
    print("- governance, issue-form, backup, publication, and update-management artifacts are present")
    print("- no high-confidence credential pattern appears in tracked or pending nonignored content")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
