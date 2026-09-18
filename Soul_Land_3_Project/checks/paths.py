#!/usr/bin/env python3
"""Shared path resolution for the whole check suite.

🔴 WHY THIS EXISTS (2026-09-18). The suite grew 18 hardcoded `/home/user/...` paths across six
files. That is fine on one machine and useless anywhere else: the moment the project is cloned
into a repository subdirectory, every one of those paths is wrong, and the checks either crash
or — worse — silently check nothing. This module makes the layout explicit in one place.

THE EXPECTED LAYOUT (workspace root = the directory holding these four things)::

    <WORKSPACE>/
        CODEX/                       the thinking tools, consequence engine, decision journal
        canon_extract/chapters/      the canon corpus (NOT distributed — copyrighted)
        Soul_Land_3_Project/         the story + this suite
        README.md, FANFICTION_FRAMEWORK.md

OVERRIDES (for when the project is relocated, e.g. inside a git repo)::

    SL3_WORKSPACE   the directory that stands in for <WORKSPACE>
    SL3_CANON       the directory holding canon_NNN.txt files

Nothing else should hardcode an absolute path. If you find one, move it here.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))          # .../Soul_Land_3_Project/checks
PROJECT = os.path.dirname(HERE)                            # .../Soul_Land_3_Project

def _resolve_workspace():
    """Find the directory that stands in for the workspace root.

    Order:
      1. SL3_WORKSPACE, if set.
      2. PROJECT/FRAMEWORK — the layout used when this project is vendored into a larger
         repository and its CODEX/ travels with it.
      3. the project's parent — the original authoring layout (<WS>/CODEX, <WS>/canon_extract).
      4. the parent regardless.

    🔴 2 BEFORE 3, and that ordering is load-bearing — I got it backwards the first time and it
    broke in the vendored repo. The host repository had its OWN unrelated `CODEX/` one level up,
    so "the parent has a CODEX directory" matched the wrong one, and the two-copies guard then
    failed on a mirror file belonging to the host project, not to us. A directory named CODEX is
    not evidence that it is OUR codex. The vendored path is unambiguous, so it wins; and the
    parent is only accepted when it actually holds our marker file (`CODEX/00_MASTER_INDEX.md`).
    """
    env = os.environ.get("SL3_WORKSPACE")
    if env:
        return env
    vendored = os.path.join(PROJECT, "FRAMEWORK")
    if os.path.isdir(os.path.join(vendored, "CODEX")):
        return vendored
    parent = os.path.dirname(PROJECT)
    if os.path.isfile(os.path.join(parent, "CODEX", "00_MASTER_INDEX.md")):
        return parent
    return parent


WORKSPACE = _resolve_workspace()

CODEX = os.path.join(WORKSPACE, "CODEX")
CANON = os.environ.get("SL3_CANON") or os.path.join(WORKSPACE, "canon_extract", "chapters")
FROZEN_QUOTES = os.path.join(CODEX, "CANON_QUOTE_SOURCES_FROZEN.txt")
CONSEQUENCE = os.path.join(CODEX, "consequence.py")

# Workspace-level documents that carry live-state markers and must be scanned for staleness.
WORKSPACE_DOCS = [
    os.path.join(CODEX, "00_MASTER_INDEX.md"),
    os.path.join(WORKSPACE, "README.md"),
    os.path.join(WORKSPACE, "FANFICTION_FRAMEWORK.md"),
]


def has_canon():
    """True when the copyrighted canon corpus is actually present on disk."""
    return os.path.isdir(CANON) and any(
        f.startswith("canon_") and f.endswith(".txt") for f in os.listdir(CANON))
