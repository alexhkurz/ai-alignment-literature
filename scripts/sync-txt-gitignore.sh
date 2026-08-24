#!/usr/bin/env bash
# Rewrite theme-folder .gitignore for .txt cache vs pinned policy.
# Usage: ./scripts/sync-txt-gitignore.sh [--dry-run]
if [ -z "${BASH_VERSION:-}" ]; then
  printf '%s\n' "This script requires bash. Use: bash \"$0\" …" >&2
  exit 1
fi
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/sync-txt-gitignore.py" --root "$ROOT" "$@"
