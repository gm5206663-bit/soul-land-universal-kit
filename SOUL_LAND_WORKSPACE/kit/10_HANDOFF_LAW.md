# 10 — HANDOFF LAW [REBUILT from kit references — originals not in this upload]

A fresh agent must be able to orient in one read and produce the next chapter
without asking what happened. The handoff is a file discipline, not a hope.

---

## IF YOU INHERIT AN EXISTING PROJECT (from 00)

Do these four before writing anything:

1. **Find the single status source.** If two files claim current state, one is
   wrong and you don't know which. Fix that first — pick one, make the other
   explicitly derivative, stamp it.
2. **Find the live edge** — the last chapter that counts. Deleted, superseded and
   abandoned drafts will still sit in the tree, readable and wrong.
3. **Run the verification script over everything.** Expect failures. Fix them
   before adding.
4. **Stamp superseded files.** An unstamped stale file is a trap with a
   five-minute fuse. Stamp = a header line: `SUPERSEDED by <file> — <date>`.

## THE HANDOFF BLOCK (bottom of the project README, kept current)

```
## HANDOFF
READ FIRST (in order):
1. <this README>                 — authority order + file map + live edge
2. foundation/NO_MISTAKE_LIVE_RULES.md — the twelve locks
3. foundation/STATUS_PANEL.md    — single status source (LIVE EDGE field)
4. foundation/CONTINUITY.md      — anchor table + forward references
5. the last two chapters
6. foundation/SERIAL_LOG.md (tail only — last 3 entries)
LIVE EDGE: Chapter N — <title>
NEXT BEAT: <one line, author-gated>
```

## STANDING RULES

- Files over memory. If it is not written down, it did not happen.
- Corrections repair the CHAPTERS the same turn, not just the doctrine files.
- After any correction, sweep every file that should carry it before reporting
  done. Then verify by grep, not by assumption.
- The serial log grows every session whatever the project; the self-file too.
