#!/usr/bin/env python3
"""Ensure {citationkey}.txt exists by fetching a PDF and running pdftotext.

Text extracts are local cache when a public PDF URL exists (see theme .gitignore).
Run when an agent (or human) needs full text and {key}.txt is missing.

Usage:
  ensure-extract.py KEY [KEY ...]
  ensure-extract.py --missing
  ensure-extract.py --all
  ensure-extract.py --dry-run KEY

Requires: pdftotext (poppler), network for download when no local PDF.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from literature_extract import (
    fetch_pdf,
    find_note,
    iter_note_keys,
    parse_bib_entry,
    repo_root,
)


def run_pdftotext(pdf_path: Path, txt_path: Path) -> None:
    if shutil.which("pdftotext") is None:
        raise SystemExit("pdftotext not found on PATH (install poppler).")
    subprocess.run(
        ["pdftotext", "-enc", "UTF-8", str(pdf_path), str(txt_path)],
        check=True,
    )


def ensure_key(
    root: Path,
    bib_text: str,
    key: str,
    *,
    dry_run: bool = False,
    force: bool = False,
) -> str:
    note = find_note(root, key)
    if note is None:
        raise SystemExit(f"No curated note {key}.md under {root}")

    folder = note.parent
    pdf_path = folder / f"{key}.pdf"
    txt_path = folder / f"{key}.txt"
    note_text = note.read_text(encoding="utf-8", errors="replace")
    fields = parse_bib_entry(bib_text, key)

    if txt_path.is_file() and txt_path.stat().st_size > 0 and not force:
        return f"{key}: cached ({txt_path.relative_to(root)})"

    if dry_run:
        sources = []
        if pdf_path.is_file():
            sources.append("local pdf")
        if fields.get("eprint"):
            sources.append(f"arxiv:{fields['eprint']}")
        if fields.get("url"):
            sources.append(fields["url"])
        source = ", ".join(sources) if sources else "no public URL"
        return f"{key}: would extract ({source}) -> {txt_path.relative_to(root)}"

    source = fetch_pdf(fields, note_text, pdf_path)
    run_pdftotext(pdf_path, txt_path)
    size = txt_path.stat().st_size
    rel = txt_path.relative_to(root)
    if size < 1024:
        return (
            f"{key}: wrote {rel} ({size} bytes; {source}) "
            "[warning: very small extract — scanned PDF?]"
        )
    return f"{key}: wrote {rel} ({size // 1024} KiB; {source})"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("keys", nargs="*", help="Citation key(s)")
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
        "--missing",
        action="store_true",
        help="Process keys with a note but no non-empty .txt",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process every citation key with a curated note",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report actions without downloading or writing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate .txt even when it already exists",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    root = args.root.resolve()
    bib_path = (args.bib or root / "bib.bib").resolve()
    if not bib_path.is_file():
        raise SystemExit(f"Missing bib file: {bib_path}")

    bib_text = bib_path.read_text(encoding="utf-8", errors="replace")

    if args.all:
        keys = list(iter_note_keys(root))
    elif args.missing:
        keys = []
        for key in iter_note_keys(root):
            note = find_note(root, key)
            txt_path = note.parent / f"{key}.txt"
            if not txt_path.is_file() or txt_path.stat().st_size == 0:
                keys.append(key)
    else:
        keys = args.keys

    if not keys:
        parser.error("Provide KEY(s), or use --missing / --all")

    failures = 0
    for key in keys:
        try:
            print(ensure_key(root, bib_text, key, dry_run=args.dry_run, force=args.force))
        except SystemExit as exc:
            failures += 1
            print(f"{key}: FAILED — {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
