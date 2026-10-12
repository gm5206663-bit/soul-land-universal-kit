#!/usr/bin/env bash
# Install opt-in local Git hooks that run the complete Fire Phoenix validation suite.
# Invoke with: bash tools/install_local_hooks.sh
set -euo pipefail

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
HOOK_DIR="$ROOT/.git/hooks"

if [ ! -d "$ROOT/.git" ]; then
  echo "No Git repository found at $ROOT" >&2
  exit 1
fi
mkdir -p "$HOOK_DIR"

for hook in pre-commit pre-push; do
  cat > "$HOOK_DIR/$hook" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
python3 tools/validate_all.py
HOOK
  chmod 755 "$HOOK_DIR/$hook"
  echo "Installed $HOOK_DIR/$hook"
done

echo "Hooks run the full validator before commits and pushes."
echo "They do not store credentials or change publication authority."
