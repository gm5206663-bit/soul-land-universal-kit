#!/usr/bin/env python3
"""tools/method/conformance.py — does this repository actually practise the method?

THE FIVE REQUIREMENTS, TAKEN FROM THE METHOD ITSELF
    Not invented here. Each is quoted from `how-to-write-fanfiction`:

    R1 · A BATTERY            "The battery is one command and must exit 0. A red layer is a
                              stop; a green run with a skipped layer is not green."
                              -> docs/03_gates_and_audits.md, "The gate battery — layers"

    R2 · A SELFTEST           "A gate must selftest… A gate that has never been seen to fail is
                              a gate nobody has tested."
                              -> docs/03, "The contract of a gate", rule 1

    R3 · AN INDEPENDENT PROOF "Never trust only the project's own checker… a project grading its
                              own homework can be consistently wrong." Plus the manifest
                              contract: "a repository that cannot prove its own files are the
                              files it checked cannot prove anything downstream."
                              -> docs/03 rule 3 · tools/check_manifest.py docstring

    R4 · SAME-TURN STATE      "Update everything the same turn… a chapter is not shipped until
                              every state file agrees with it. 'Later' is how state rots."
                              -> README, the big idea, point 4

    R5 · NAMES THE LAW        A fresh agent landing in the repository must be able to find the
                              constitution. The guide is written to be fandom-neutral and is the
                              single source of the method; a repository that reimplements it
                              without citing it becomes a second, drifting copy — which the
                              guide's own point 5 forbids: "One copy of one thing."

WHY R5 IS THE ONE THAT MATTERS MOST HERE
    Measured 2026-10-30: five of twelve repositories cite the method. The kit — 2,400 files, the
    whole Soul Land corpus — cites it zero times, while carrying its own copy of the tools. That
    is exactly the failure R5 exists to catch: not a missing file, a missing *authority*.

USAGE
    python3 tools/method/conformance.py --root /path/to/clones
    python3 tools/method/conformance.py --root /path/to/clones --strict
    python3 tools/method/conformance.py --selftest

    Exit 0 when every repository clears R1–R5 (or, without --strict, when the only failures are
    R5 citations — a missing pointer is a documentation debt, a missing gate is a hole).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

METHOD_REPO = 'how-to-write-fanfiction'
SKIP_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', '_archive'}

# a battery is a single command that invokes several named checks
CHECK_NAMES = ('verify', 'style_gate', 'canon_copy', 'banned_token', 'plain_word',
               'camera_gate', 'claim_gate', 'selftest', 'drift', 'sentinel', 'run_all')
BATTERY_EXT = {'.sh', '.py', '.yml', '.yaml'}

# The method speaks of a repository's OWN battery and of an agent reading AGENTS.md first.
# A sub-project's script deep in the tree is that sub-project's, not the repository's; a passing
# mention in a changelog is not a pointer from the door. Both were false passes on 2026-10-30.
# A serial's battery at <serial>/checks/ is that serial's, which is why depth is 1: the
# kit has ten gated sub-projects and its own root battery was still missing.
MAX_DEPTH = 1          # the repository's OWN level: root, tools/, checks/ — not a serial's folder
ENTRY_DOCS = ('readme.md', 'agents.md', 'index.md')
# what a battery is CALLED matters: a writer, a generator or a renderer that happens to name
# two checks in its source is not a battery. `tools/ship_chapter.py` was credited as one on
# 2026-10-30 before this line existed.
MANIFEST_NAMES = ('manifest.sha256', 'checksums.sha256', 'manifest.sha256sum',
                  'sha256sums.txt', 'hashes.sha256')
BATTERY_NAME = re.compile(r'(run_all|battery|gate|check_all|verify_all|ci_run|run_checks)', re.I)

REQUIREMENTS = {
    'R1': 'a one-command battery that runs several checks',
    'R2': 'a selftest that injects defects and proves the gates can fail',
    'R3': 'independent proof — a manifest or an outside scan',
    'R4': 'same-turn state — a generated status or ledger',
    'R5': 'names the law — cites how-to-write-fanfiction',
}


def repo_files(root: Path, max_depth: int | None = None) -> list[Path]:
    out = []
    for p in root.rglob('*'):
        if not p.is_file() or (set(p.parts) & SKIP_DIRS):
            continue
        if max_depth is not None:
            rel = p.relative_to(root)
            # workflows live at .github/workflows/<f> = depth 2, and a CI job is a legitimate
            # battery; depth 1 alone silently disqualified every repository that uses one.
            in_workflows = '.github' in rel.parts and 'workflows' in rel.parts
            if len(rel.parts) - 1 > max_depth and not in_workflows:
                continue
        out.append(p)
    return out


def text_of(path: Path, limit: int = 400_000) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='replace')[:limit]
    except OSError:
        return ''


def battery(root: Path, files: list[Path]) -> str | None:
    """A script that shells out to two or more checks WHICH EXIST.

    A battery is not a list of names. The first version of this function counted
    `python3 tools/verify.py` as a check whether or not `tools/verify.py` was
    present — so a repository carrying a battery script and none of the tools
    scored as conformant. The selftest fixtures caught it; this is the fix.
    """
    for p in files:
        if p.suffix not in BATTERY_EXT or p.stat().st_size > 200_000:
            continue
        # A CI workflow IS a battery when it runs the checks in one job — the law repo
        # itself does it that way (`.github/workflows/verify.yml`), so excluding workflow
        # files would hold the method to a standard its own repository fails.
        is_workflow = '.github' in p.parts and 'workflows' in p.parts
        if not is_workflow and not BATTERY_NAME.search(p.name):
            continue
        body = text_of(p)
        # Two ways a battery names its checks: the shell way (`python3 tools/x.py`) and the
        # Python way (`subprocess.run([sys.executable, 'tools/x.py'])`, which is how
        # supergirl-adrian-vale/tools/run_all.py does it). Only recognising the shell way
        # reported that repository as having no battery when it has had one all along — a
        # false gap is as damaging as a false pass, because someone then "fixes" a working repo.
        RUNS = re.compile(r'subprocess|os\.system|popen|check_call|check_output|execv|'
                          r'python3?\b|\bsh\b|\bbash\b', re.I)
        lines = body.splitlines()
        near_run = set()
        for i, line in enumerate(lines):
            if RUNS.search(line):
                for j in (i - 1, i, i + 1):
                    if 0 <= j < len(lines):
                        near_run.add(j)
        invoked = set()
        for i in sorted(near_run):
            line = lines[i]
            if 'http' in line:
                continue
            for m in re.finditer(r'[\w./-]+\.(?:py|sh)', line):
                target = m.group(0)
                if target.startswith('.'):
                    continue
                for base in (root, p.parent, p.parent.parent):
                    cand = (base / target)
                    if cand.exists() and cand.resolve() != p.resolve():
                        # distinct FILES, not distinct spellings of one file: pokemon's
                        # style_gate.py mentions "tools/style_gate.py" and "style_gate.py"
                        # in its own docstring, and that counted as a two-check battery.
                        invoked.add(cand.resolve())
                        break
        named = {n for n in CHECK_NAMES if n in body}
        if len(invoked) >= 2 and len(named) >= 2:
            return str(p.relative_to(root))
    return None


def find_selftest(root: Path, files: list[Path]) -> str | None:
    """A test that writes a deliberately broken fixture and requires a failure.

    Two legitimate shapes, both named by the method: a dedicated `*selftest*` file that
    injects defects, OR the battery invoking `--selftest` on the gates themselves. The
    guide's own repository uses the second (`.github/workflows/verify.yml` runs
    `minigate.py --selftest`, `claim_gate.py --selftest`, `camera_gate.py --selftest`),
    so requiring a file *called* selftest would fail the method against itself.
    """
    for p in files:
        if 'selftest' not in str(p).lower():
            continue
        body = text_of(p)
        if re.search(r'tamper|inject|defect|broken|bad\b|mutate|corrupt', body, re.I):
            return str(p.relative_to(root))
    for p in files:
        if p.suffix not in BATTERY_EXT or p.stat().st_size > 200_000:
            continue
        body = text_of(p)
        if re.search(r'\w+\.py\s+--selftest', body) or '--selftest' in body:
            return f'{p.relative_to(root)} (invokes --selftest)'
    return None


def independent(root: Path, files: list[Path]) -> str | None:
    """A hash manifest for THIS tree — not a report about someone else's tree.

    Two false passes on 2026-10-30 forced the `reports/` exclusion: the-authors-desk was
    credited with a manifest because a report archived a *copy* of soul-library's CI file,
    and storyos-site was credited because it has a `scripts/drift.py`. The guide's rule is
    that a repository must prove its own files are the files it checked. A drift detector
    is a check; a manifest is the proof. Only the proof counts here.
    """
    HISTORICAL = ('reports/', 'audits/', 'archive/', '_archive/', 'archive-')
    for p in files:
        rel = p.relative_to(root).as_posix()
        if any(h in rel.lower() for h in HISTORICAL):
            continue
        if p.name.lower() in MANIFEST_NAMES:
            return rel
    return None


def same_turn_state(root: Path, files: list[Path]) -> str | None:
    """The Ship Law needs a state file that is REBUILT from the tree, not a hand-written
    ledger. A mistakes ledger records the past; a status panel is the present, and only the
    present can rot out of agreement with the text."""
    for p in files:
        n = p.name.lower()
        if 'status_panel' in n or n == 'status.md':
            return str(p.relative_to(root))
    for p in files:
        if p.suffix.lower() != '.md' or p.stat().st_size > 200_000:
            continue
        head = text_of(p, 4000).lower()
        if 'generated' in head and ('status' in head or 'inventory' in head or 'live edge' in head):
            return str(p.relative_to(root))
    return None


def names_the_law(root: Path, files: list[Path]) -> str | None:
    """An ENTRY document must carry the pointer — README or AGENTS, the two files the
    method itself says an agent reads first. A mention buried in a changelog does not
    help the agent who lands at the door."""
    for p in files:
        if p.parent != root or p.name.lower() not in ENTRY_DOCS:
            continue
        if p.suffix.lower() not in ('.md', '.html', '.txt'):
            continue
        if p.stat().st_size > 400_000:
            continue
        if METHOD_REPO in text_of(p):
            return str(p.relative_to(root))
        if 'how to write gated fan fiction' in text_of(p).lower():
            return str(p.relative_to(root))
    return None


def audit(root: Path) -> dict:
    files = repo_files(root)
    shallow = repo_files(root, max_depth=MAX_DEPTH)
    found = {
        'R1': battery(root, shallow),
        'R2': find_selftest(root, shallow),
        'R3': independent(root, repo_files(root, max_depth=2)),
        'R4': same_turn_state(root, repo_files(root, max_depth=2)),
        'R5': names_the_law(root, files),
    }
    return {
        'repo': root.name,
        'files': len(files),
        'checks': {k: {'ok': bool(v), 'evidence': v} for k, v in found.items()},
        'score': sum(1 for v in found.values() if v),
    }


def run(root: Path, strict: bool = False, as_json: bool = False) -> int:
    repos = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('.'))
    results = [audit(p) for p in repos]

    if as_json:
        print(json.dumps({'requirements': REQUIREMENTS, 'repos': results}, indent=2))
    else:
        head = f"{'repository':30s} " + ' '.join(f'{k:3s}' for k in REQUIREMENTS) + '  score'
        print(head)
        print('-' * len(head))
        for r in results:
            marks = ' '.join(' ok' if r['checks'][k]['ok'] else '  .' for k in REQUIREMENTS)
            print(f"{r['repo']:30s} {marks}  {r['score']}/5")
        print()
        for k, text in REQUIREMENTS.items():
            passing = [r['repo'] for r in results if r['checks'][k]['ok']]
            failing = [r['repo'] for r in results if not r['checks'][k]['ok']]
            print(f'{k} · {text}')
            print(f'   {len(passing)} of {len(results)} pass' +
                  (f' · missing: {", ".join(failing)}' if failing else ''))
        print()
        for r in results:
            if r['score'] == 5:
                continue
            gaps = [k for k in REQUIREMENTS if not r['checks'][k]['ok']]
            print(f"  {r['repo']}: missing {', '.join(gaps)}")

    hard = [r for r in results if any(not r['checks'][k]['ok'] for k in ('R1', 'R2'))]
    citation = [r for r in results if not r['checks']['R5']['ok']]
    failed = bool(hard) or (strict and bool(citation))
    if not as_json:
        print()
        print(f'{len(results)} repositories · {len(hard)} missing a gate or a selftest · '
              f'{len(citation)} not citing the law')
        print('RESULT:', 'FAIL' if failed else 'PASS')
    return 1 if failed else 0


def _fixture(root: Path, *, battery_file: bool = True, selftest_file: bool = True,
             manifest: bool = False, status: bool = False, cite: bool = False) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / 'tools').mkdir(exist_ok=True)
    if battery_file:
        (root / 'checks').mkdir(exist_ok=True)
        # the battery names three checks, so the three checks must exist — a battery
        # that points at nothing is not a battery, which is what the fixture proves
        for tool in ('verify.py', 'style_gate.py'):
            (root / 'tools' / tool).write_text('# a gate\n', encoding='utf-8')
        (root / 'checks' / 'run_all.sh').write_text(
            '#!/bin/sh\npython3 tools/verify.py chapters\npython3 tools/style_gate.py chapters\n'
            'python3 tools/selftest.py\n', encoding='utf-8')
    if selftest_file:
        (root / 'tools' / 'selftest.py').write_text(
            '# inject a defect and require the gate to fail\ntamper = True\n', encoding='utf-8')
    if manifest:
        (root / 'MANIFEST.sha256').write_text('x  a.md\n', encoding='utf-8')
    if status:
        (root / 'foundation').mkdir(exist_ok=True)
        (root / 'foundation' / 'STATUS_PANEL.md').write_text('# live edge\n', encoding='utf-8')
    (root / 'README.md').write_text(
        ('See how-to-write-fanfiction for the law.\n' if cite else '# a repo\n'), encoding='utf-8')


def selftest() -> int:
    failures = 0

    def expect(label: str, cond: bool) -> None:
        nonlocal failures
        print(f"SELFTEST {'ok:  ' if cond else 'FAIL:'} {label}")
        failures += 0 if cond else 1

    with tempfile.TemporaryDirectory() as tmp:
        box = Path(tmp)
        _fixture(box / 'full', manifest=True, status=True, cite=True)
        r = audit(box / 'full')
        expect('a fully conformant repository scores 5/5', r['score'] == 5)

        _fixture(box / 'nobattery', battery_file=False, cite=True)
        r = audit(box / 'nobattery')
        expect('no battery fails R1', not r['checks']['R1']['ok'])

        _fixture(box / 'noself', selftest_file=False, cite=True)
        r = audit(box / 'noself')
        expect('no selftest fails R2', not r['checks']['R2']['ok'])

        _fixture(box / 'nocite', manifest=True)
        r = audit(box / 'nocite')
        expect('silence about the law fails R5', not r['checks']['R5']['ok'])

        # a file merely NAMED selftest, with nothing injected, must not count
        box_named = box / 'namedonly'
        _fixture(box_named, cite=True)
        (box_named / 'tools' / 'selftest.py').write_text(
            'print("all good")\n', encoding='utf-8')
        expect('a selftest that injects nothing does not count',
               not audit(box_named)['checks']['R2']['ok'])

        # a battery that names one check twice is not a battery
        box_one = box / 'onecheck'
        _fixture(box_one, cite=True)
        (box_one / 'checks' / 'run_all.sh').write_text(
            '#!/bin/sh\npython3 tools/verify.py chapters\n', encoding='utf-8')
        expect('a single-check script is not a battery',
               not audit(box_one)['checks']['R1']['ok'])

        # The Python-style battery: checks launched through sys.executable. Recognising only
        # `python3 tools/x.py` made this shape invisible, and supergirl-adrian-vale was
        # reported as having no battery when it has had one all along.
        box_py = box / 'pybattery'
        _fixture(box_py, battery_file=False, cite=True)
        for tool in ('verify.py', 'style_gate.py'):
            (box_py / 'tools' / tool).write_text('# a gate\n', encoding='utf-8')
        (box_py / 'tools' / 'run_all.py').write_text(
            'import subprocess, sys\n'
            'for c in ([sys.executable, "tools/verify.py"],\n'
            '          [sys.executable, "tools/style_gate.py"]):\n'
            '    subprocess.run(c, check=True)\n', encoding='utf-8')
        expect('a Python-style battery counts (sys.executable + subprocess)',
               audit(box_py)['checks']['R1']['ok'])

        box_docs = box / 'notools'
        _fixture(box_docs, battery_file=False, selftest_file=False, cite=True)
        expect('documentation alone fails R1 and R2',
               not audit(box_docs)['checks']['R1']['ok']
               and not audit(box_docs)['checks']['R2']['ok'])

        expect('run() returns 1 when a repository has no gate',
               run(box, strict=False) == 1)

    print(f'SELFTEST: {failures} failure(s)')
    return 0 if failures == 0 else 2


def main(argv: list[str]) -> int:
    if '--selftest' in argv:
        return selftest()
    root = Path(argv[argv.index('--root') + 1]) if '--root' in argv else Path.cwd()
    if not root.is_dir():
        print(f'not a directory: {root}')
        return 2
    return run(root, strict='--strict' in argv, as_json='--json' in argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
