#!/usr/bin/env bash
# Ensure {citationkey}.txt from a public PDF (or local {citationkey}.pdf).
#
# Lazy workflow: run when you or an agent need full text and .txt is missing.
# Usage (from repo root or any directory):
#   ./scripts/ensure-extract.sh kurz2024_semiprimal_coalgebra
#   ./scripts/ensure-extract.sh --missing
#   ./scripts/ensure-extract.sh --all
#   ./scripts/ensure-extract.sh --dry-run KEY
#
# Requires: python3, pdftotext (poppler), network unless local PDF exists.
if [ -z "${BASH_VERSION:-}" ]; then
  printf '%s\n' "This script requires bash. Use: bash \"$0\" …" >&2
  exit 1
fi
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/ensure-extract.py" --root "$ROOT" "$@"
