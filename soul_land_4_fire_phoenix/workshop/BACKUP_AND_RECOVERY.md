# Backup and Recovery

GitHub is a private mirror, not the only preservation mechanism. Keep an offline copy before major editorial, authority, or repository-setting changes.

## Create an offline Git bundle

From the repository root:

```bash
bash tools/create_git_bundle_backup.sh
```

The script writes a dated `.bundle` and checksum into the ignored `backups/` directory, verifies the bundle, and never uploads it.

To choose another directory:

```bash
bash tools/create_git_bundle_backup.sh /secure/offline/location
```

## Restore or inspect a bundle

```bash
git clone /secure/offline/location/fire-phoenix-YYYYMMDD-HHMMSS.bundle restored-fire-phoenix
git -C restored-fire-phoenix fsck --no-reflogs
python3 restored-fire-phoenix/tools/validate_all.py
```

## Recovery priorities

1. Preserve the original workspace plus at least one offline bundle.
2. Verify recovered public evidence before editing any creative layer.
3. Restore the private remote only with `bash tools/configure_github_remote.sh`; verify the destination before a push.
4. Treat a missing GitHub remote configuration as an operational problem, not permission to reconstruct/replace public source material.
5. The intentionally ignored rejected Chapter 53 draft is not part of Git bundles. Preserve it separately only if the author wants that local quarantine retained.
