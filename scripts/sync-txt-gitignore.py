#!/usr/bin/env python3
"""Update theme-folder .gitignore files for .txt cache vs pinned policy.

Regenerable .txt (public PDF URL in bib.bib / note) → gitignored via *.txt.
Pinned .txt (local PDF only) → negated with !{key}.txt so they stay in git.

Usage:
  sync-txt-gitignore.py
  sync-txt-gitignore.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from literature_extract import classify_txt_policy, repo_root, sync_folder_gitignores


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root(),
        help="Literature tree root (default: repo root)",
    )
    parser.add_argument(
        "--bib",
        type=Path,
        default=None,
        help="Path to bib.bib (default: ROOT/bib.bib)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report folders without writing .gitignore files",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    root = args.root.resolve()
    bib_path = (args.bib or root / "bib.bib").resolve()
    if not bib_path.is_file():
        raise SystemExit(f"Missing bib file: {bib_path}")

    bib_text = bib_path.read_text(encoding="utf-8", errors="replace")
    policy = classify_txt_policy(root, bib_text)
    regenerable = sum(1 for _, reg in policy.values() if reg)
    pinned = len(policy) - regenerable

    for line in sync_folder_gitignores(root, bib_text, dry_run=args.dry_run):
        print(line)

    print(f"Total: {regenerable} regenerable, {pinned} pinned (commit .txt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
