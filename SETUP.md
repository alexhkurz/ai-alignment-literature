# Setup — ai-alignment-literature

Canonical paper summaries, text extracts, and `bib.bib` for the AI alignment / alignment-faking research cluster.

Consumer repositories treat this tree as a sister checkout at the same directory level — not a git submodule. See each consumer’s `LITERATURE.md`.

## Clone (with a consumer)

```bash
cd <parent>
git clone <consumer-repo-url>
git clone <this-repo-url> ai-alignment-literature
```

Required layout (fixed sibling name):

```text
<parent>/
  chapman-alignment-faking/          # or Alignment-Faking-Chapman/literature-review-and-docs
  ai-alignment-literature/           # this repo
```

Open both in a multi-root Cursor workspace (e.g. `ai-repos.code-workspace`).

## Consumer repositories

| Repo | Notes |
|------|-------|
| [chapman-alignment-faking](https://github.com/alexhkurz/chapman-alignment-faking) | milestones / onboarding; relevance in `literature-relevance/` |
| [planning-and-literature-review](https://github.com/Alignment-Faking-Chapman/planning-and-literature-review) | org planning docs under `Alignment-Faking-Chapman/literature-review-and-docs` |

## Editing

Edit only this repository for shared summaries. Consumer notes link here with relative `../` paths; they do not vendor a nested copy.

## Ingesting a new paper (here)

1. Append `bib.bib` — include `eprint` / open `url` when a downloadable PDF exists.
2. Write `{citationkey}-notes.md` with metadata, summary, key concepts (no project relevance).
3. If a public PDF URL exists, prefer regenerable `{citationkey}.txt` via `pdftotext`; keep `{citationkey}.pdf` local (gitignored).
4. Optional full-text `{citationkey}.md` from the extract pipeline.
5. Update theme `README.md`, root `README.md` master index, `CHANGELOG.md`.
6. Do not add `## Relevance` sections here — put relevance in each consumer repo (`literature-relevance/`).

See `.cursor/rules/bibliography.mdc` and [`bib-mcp/docs/styleguide.md`](../bib-mcp/docs/styleguide.md).

## Text extracts (`.txt`)

| Source | In git? | How to obtain locally |
|--------|---------|------------------------|
| Public PDF URL in bib / note | Prefer cache (may be tracked until sync scripts are wired) | `pdftotext` or `./scripts/ensure-extract.sh {citationkey}` |
| User-provided PDF only | Yes (pinned) | `pdftotext` during ingest; stays tracked |

```bash
./scripts/ensure-extract.sh {citationkey}
```

From a consumer (sibling layout): `../ai-alignment-literature/scripts/ensure-extract.sh {citationkey}`.

Requires `pdftotext` (poppler) and network unless a local PDF already exists.

## PDFs

PDFs stay local (gitignored). Filenames must be `{citationkey}.pdf`.
