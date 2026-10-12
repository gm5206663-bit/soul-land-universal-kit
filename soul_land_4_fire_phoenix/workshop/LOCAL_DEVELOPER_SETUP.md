# Local Developer Setup

## One-time setup

```bash
git config user.name "Your Name"
git config user.email "you@example.invalid"
bash tools/install_local_hooks.sh
```

The optional hooks run `python3 tools/validate_all.py` before every commit and push. They do not store a GitHub token or bypass authority controls.

## Daily workflow

```bash
make validate
bash tools/configure_github_remote.sh   # only if this sandbox reset .git/config
git status
git diff
git add <intentionally reviewed files>
git commit -m "type: narrow description"
```

Before a separately authorized push, confirm that `origin` is the private Fire Phoenix repository, run the full validation suite, and read `PROJECT_CONTROL.md`.

## Offline preservation

```bash
make backup
```

This creates a verified, ignored local Git bundle in `backups/`; copy it to an encrypted/offline location if the project needs independent disaster recovery.
