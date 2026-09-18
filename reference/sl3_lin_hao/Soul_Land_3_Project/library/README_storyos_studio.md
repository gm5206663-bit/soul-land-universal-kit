# StoryOS Studio — Canon-First Fiction Engine

A self-contained Python app that runs the entire StoryOS system: the authority
stack, the **canon-first OC-woven chapter style**, the **Adaptation Talent**
rules, the pre-draft gate, the post-draft audit, the zero-tolerance list, and
every session command — with per-project state that **saves to disk** and
**exports to Markdown**.

**Zero dependencies. Pure Python 3.** Runs anywhere.

---

## Run it

From the workspace root (`/home/user`):

```bash
python3 storyos_app/run.py            # interactive menu
python3 storyos_app/run.py cli        # command-line interface
python3 storyos_app/run.py web        # browser app -> http://localhost:6464
```

---

## Two interfaces

- **CLI** — an interactive REPL (`storyos> ` prompt). Command history, full command set.
- **Web** — a browser app (dark UI): sidebar buttons for every action + a command bar. Served by the built-in HTTP server (no Flask).

---

## What it does

**Project management** — `new`, `open`, `list`. Each project persists to
`storyos_app/storyos_projects/<name>.json`.

**Build the foundation** — `foundation title=.. source_universe=.. canon_version=..` etc.
(fills the Story Identity Card).

**Track everything** — locks, canon scenes (with confidence + owner + OC position),
current-state matrix, knowledge firewall, mysteries (with pressure level), powers
(with phase), relationships, butterflies, chapters, checkpoint, quarantine.

**Enforce the rules** — `style`, `at`, `rules authority`, `rules zero`, `gate`
(pre-draft), `rules audit` (post-draft).

**View maps** — `map butterfly | knowledge | power | relationship`.

**Export** — `export` writes a full **Story Bible & Continuity Vault** (Markdown)
to `storyos_projects/<name>_bible.md`.

---

## Command reference (type `help` in the app)

| Command | What it does |
|---|---|
| `new <name>` / `open <name>` / `list` | manage projects |
| `foundation [k=v..]` | view / set the Story Identity Card |
| `lock <statement>` | add a locked foundation decision |
| `canon beat=".." owner=".." confidence=H oc=absent` | log a canon scene |
| `state <char> location=.. condition=..` | set a character's current state |
| `knowledge <char> knows=.. does_not_know=..` | set the knowledge firewall |
| `mystery name=".." truth=".." pressure=Dormant` | log a mystery |
| `power <holder> name=".." phase=dormant limits=".."` | log a power |
| `relationship <pair> stage=.. next_step=..` | log a relationship |
| `butterfly cause=".." consequence=".." type=A` | log a butterfly |
| `chapter add <n> <title>` / `chapter accept <n>` / `chapter reject <n>` | chapters |
| `audit <n>` | mark a chapter's post-draft audit dimensions |
| `checkpoint <text>` | set / view the accepted checkpoint |
| `quarantine <text>` | mark material permanently rejected |
| `status` | full project dashboard |
| `map <butterfly|knowledge|power|relationship>` | view a ledger |
| `style` / `at` / `rules <name>` / `gate` | rules & checklists |
| `export` | export the Story Bible to Markdown |
| `save` / `exit` | save / quit |

---

## Architecture

```
storyos_app/
├── engine.py     # rules (embedded) + Project + Studio (command dispatcher)
├── cli.py        # interactive REPL
├── web.py        # stdlib HTTP server + browser SPA
├── run.py        # launcher (menu / cli / web)
└── storyos_projects/   # per-project JSON state + exported bibles
```

The **engine** holds the full rule sets as data and all command logic; the
**CLI** and **Web** are thin front-ends over the same `Studio.execute()` — so
both interfaces are always in sync.

---

## Works with the rest of the StoryOS system

The app is the *operational* layer. The full reference documents live alongside:
`storyos_narrative_forge.md`, `storyos_ultra_extension.md`, `universal/`
(the Adaptation Talent master foundation, the writing-corrections v2.1, the
continuity/audit corrections, the drafting-mistake lessons, the canon-first
style), and the project bibles. The app distills and enforces them.
