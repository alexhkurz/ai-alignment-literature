"""Shared helpers for PDF fetch, text extract, and .txt gitignore policy."""

from __future__ import annotations

import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterator

SKIP_MD_NAMES = frozenset({"README.md", "CHANGELOG.md", "SETUP.md"})

# Host/path hints that usually serve a downloadable PDF (not merely an abstract page).
FETCHABLE_URL_MARKERS = (
    "arxiv.org",
    "episciences.org",
    "lmcs.episciences.org",
    "tac.mta.ca",
    "hal.science",
    "hal.archives-ouvertes.fr",
    "ceur-ws.org",
    "drops.dagstuhl.de",
    "openreview.net/pdf",
    "acm.org/doi/pdf",
    "bibliotecadigital.exactas.uba.ar",
    "library.oapen.org",
    "archive.org/download/",
    "research-collection.ethz.ch",
    "orbilu.uni.lu/bitstream",
)

# Pages that are not treated as public PDF sources for gitignore / auto-fetch policy.
NON_FETCHABLE_URL_MARKERS = (
    "scholar.google.com",
    "link.springer.com/article/",
    "sciencedirect.com/science/article/abs",
    "doi.org/",
    "books.google.",
    "worldcat.org",
)

GITIGNORE_HEADER = """*.pdf

# Regenerable text cache — explicit list (public PDF URL in bib.bib / note).
# Run: ../scripts/ensure-extract.sh KEY
# Pinned {key}.txt (local PDF only) are omitted here and stay tracked in git.
"""


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def find_note(root: Path, key: str) -> Path | None:
    matches = [
        p
        for p in root.rglob(f"{key}.md")
        if "_marker-work" not in p.parts and not p.name.endswith(".marker.md")
    ]
    if not matches:
        return None
    if len(matches) > 1:
        paths = "\n".join(f"  {m.relative_to(root)}" for m in matches)
        raise ValueError(f"Ambiguous citation key {key!r}; multiple notes:\n{paths}")
    return matches[0]


def iter_notes(root: Path) -> Iterator[tuple[str, Path]]:
    for path in sorted(root.rglob("*.md")):
        if "_marker-work" in path.parts:
            continue
        name = path.name
        if name in SKIP_MD_NAMES or name.endswith(".marker.md") or name.endswith("-notes.md"):
            continue
        yield path.stem, path


def iter_note_keys(root: Path) -> Iterator[str]:
    yield from (key for key, _ in iter_notes(root))


def parse_bib_entry(bib_text: str, key: str) -> dict[str, str]:
    pattern = rf"@\w+\{{{re.escape(key)}\s*,(.*?)(?=\n@\w+\{{|\Z)"
    match = re.search(pattern, bib_text, re.DOTALL)
    if not match:
        return {}
    body = match.group(1)
    fields: dict[str, str] = {}
    for field_match in re.finditer(
        r"(\w+)\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}|"
        r"(\w+)\s*=\s*\"([^\"]*)\"",
        body,
    ):
        if field_match.group(1):
            fields[field_match.group(1).lower()] = field_match.group(2).strip()
        else:
            fields[field_match.group(3).lower()] = field_match.group(4).strip()
    return fields


def urls_in_note(note_text: str) -> list[str]:
    return re.findall(r"https?://[^\s\)>\]|\"']+", note_text)


def url_looks_fetchable(url: str) -> bool:
    lower = url.strip().lower()
    if not lower.startswith("http"):
        return False
    if any(marker in lower for marker in NON_FETCHABLE_URL_MARKERS):
        return False
    if lower.endswith(".pdf"):
        return True
    # OJS / journal “article/download/…” endpoints (often PDF without .pdf suffix)
    if "/article/download/" in lower:
        return True
    return any(marker in lower for marker in FETCHABLE_URL_MARKERS)


def has_downloadable_pdf_url(fields: dict[str, str], note_text: str = "") -> bool:
    """True when bib or note records a public PDF source (not local-only)."""
    if fields.get("eprint", "").strip():
        return True
    for url in [fields.get("url", ""), *urls_in_note(note_text)]:
        if url and url_looks_fetchable(url):
            return True
    return False


def classify_txt_policy(
    root: Path, bib_text: str
) -> dict[str, tuple[Path, bool]]:
    """Map citation key -> (note path, gitignore_txt)."""
    result: dict[str, tuple[Path, bool]] = {}
    for key, note in iter_notes(root):
        fields = parse_bib_entry(bib_text, key)
        note_text = note.read_text(encoding="utf-8", errors="replace")
        regenerable = has_downloadable_pdf_url(fields, note_text)
        result[key] = (note, regenerable)
    return result


def arxiv_pdf_url(eprint: str) -> str:
    eprint = eprint.strip()
    if eprint.startswith("http"):
        base = eprint.replace("/abs/", "/pdf/")
        return base if base.endswith(".pdf") else base + ".pdf"
    return f"https://arxiv.org/pdf/{eprint}.pdf"


def url_to_pdf_candidates(url: str) -> list[str]:
    url = url.strip()
    candidates = [url]
    lower = url.lower()
    if "arxiv.org/abs/" in lower:
        candidates.insert(0, url.replace("/abs/", "/pdf/") + ".pdf")
    if "episciences.org/" in lower and not lower.endswith(".pdf"):
        candidates.insert(0, url.rstrip("/") + "/pdf")
    if "tac.mta.ca" in lower and lower.endswith("abs.html"):
        candidates.insert(0, url.replace("abs.html", ".pdf"))
    if "hal.science/" in lower and "/document" not in lower:
        candidates.insert(0, url.rstrip("/") + "/document")
    return candidates


def download_pdf(url: str, dest: Path) -> None:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ai-alignment-literature/ensure-extract"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        content_type = response.headers.get("Content-Type", "")
        data = response.read()
    if not data.startswith(b"%PDF") and "pdf" not in content_type.lower():
        raise ValueError(f"URL did not return a PDF ({content_type or 'unknown type'}): {url}")


def fetch_pdf(fields: dict[str, str], note_text: str, pdf_path: Path) -> str:
    if pdf_path.is_file() and pdf_path.stat().st_size > 0:
        return f"local PDF {pdf_path}"

    errors: list[str] = []

    eprint = fields.get("eprint")
    if eprint:
        url = arxiv_pdf_url(eprint)
        try:
            download_pdf(url, pdf_path)
            return f"downloaded arXiv {url}"
        except (urllib.error.URLError, ValueError) as exc:
            errors.append(f"arXiv {url}: {exc}")

    urls: list[str] = []
    bib_url = fields.get("url")
    if bib_url:
        urls.append(bib_url)
    for url in urls_in_note(note_text):
        if url_looks_fetchable(url) and url not in urls:
            urls.append(url)

    for url in urls:
        for candidate in url_to_pdf_candidates(url):
            try:
                download_pdf(candidate, pdf_path)
                return f"downloaded {candidate}"
            except (urllib.error.URLError, ValueError) as exc:
                errors.append(f"{candidate}: {exc}")

    if errors:
        raise SystemExit(
            "Could not fetch PDF.\n"
            + "\n".join(f"  - {line}" for line in errors)
            + "\nPlace a local PDF at "
            + str(pdf_path)
            + " and rerun."
        )
    raise SystemExit(
        f"No downloadable PDF URL in bib.bib or the note.\n"
        f"Place a local PDF at {pdf_path} and rerun."
    )


def render_folder_gitignore(regenerable_keys: list[str]) -> str:
    lines = [GITIGNORE_HEADER.rstrip()]
    for key in sorted(regenerable_keys):
        lines.append(f"{key}.txt")
    return "\n".join(lines) + "\n"


THEME_FOLDER_EXCLUDE = frozenset({"scripts"})


def theme_folders(root: Path) -> list[Path]:
    """Top-level theme directories (every subfolder except scripts and dot dirs)."""
    return sorted(
        p
        for p in root.iterdir()
        if p.is_dir() and p.name not in THEME_FOLDER_EXCLUDE and not p.name.startswith(".")
    )


def sync_folder_gitignores(root: Path, bib_text: str, *, dry_run: bool = False) -> list[str]:
    """Rewrite theme-folder .gitignore files from bib + note URL policy."""
    by_folder: dict[Path, list[tuple[str, bool]]] = {}
    for key, (note, regenerable) in classify_txt_policy(root, bib_text).items():
        by_folder.setdefault(note.parent, []).append((key, regenerable))

    reports: list[str] = []
    for folder in theme_folders(root):
        entries = by_folder.get(folder, [])
        regenerable_keys = [key for key, regenerable in entries if regenerable]
        regenerable_count = len(regenerable_keys)
        pinned_count = len(entries) - regenerable_count
        content = render_folder_gitignore(regenerable_keys)
        gitignore_path = folder / ".gitignore"
        rel = gitignore_path.relative_to(root)
        if dry_run:
            reports.append(
                f"{rel}: {regenerable_count} regenerable, {pinned_count} pinned"
            )
            continue
        gitignore_path.write_text(content, encoding="utf-8")
        reports.append(
            f"wrote {rel}: {regenerable_count} regenerable, {pinned_count} pinned"
        )
    return reports
