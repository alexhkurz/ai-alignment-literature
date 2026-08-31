# Setup — ai-alignment-literature

Canonical paper summaries, text extracts, and `bib.bib` for the AI alignment / alignment-faking research cluster.

Consumer repositories treat this tree as a sister checkout at the same directory level — not a git submodule. See each consumer’s `LITERATURE.md`.

## Clone (with a consumer)

```bash
cd <parent>
git clone <consumer-repo-url>
git clone https://github.com/alexhkurz/ai-alignment-literature.git
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
| [hera](https://github.com/alexhkurz/hera) | HeRD-Merging LaTeX; bibliography mirrored under `interpretability/` |

## Editing

Edit only this repository for shared summaries. Consumer notes link here with relative `../` paths; they do not vendor a nested copy.

## Ingesting a new paper (here)

1. Append `bib.bib` — include `eprint` / open `url` when a downloadable PDF exists.
2. Write `{citationkey}-notes.md` with metadata, summary, key concepts (no project relevance).
3. Fetch or place `{citationkey}.pdf` locally (gitignored); run `./scripts/ensure-extract.sh {citationkey}` for `{citationkey}.txt`.
4. Run `./scripts/sync-txt-gitignore.sh` so regenerable `.txt` files are not committed.
5. Update theme `README.md`, root `README.md` master index (when curated), `CHANGELOG.md`.
6. Do not add `## Relevance` sections here — put relevance in each consumer repo (`literature-relevance/`).

See [AGENTS.md](AGENTS.md), [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md), and [`docs/bibliography-project.md`](docs/bibliography-project.md).

## Text extracts (`.txt`)

Aligned with [ai-math-formal-methods](https://github.com/alexhkurz/ai-math-formal-methods) bibliography policy:

| Source | In git? | How to obtain locally |
|--------|---------|------------------------|
| Public PDF URL in `bib.bib` (`eprint`, arXiv/open `url`) | **No** (regenerable cache) | `./scripts/ensure-extract.sh {citationkey}` or `pdftotext` |
| No stable public PDF (paywall, print-only, private scan) | **Yes** (`git add -f`) | `pdftotext` during ingest; stays pinned |

```bash
./scripts/ensure-extract.sh {citationkey}    # one paper
./scripts/ensure-extract.sh --missing        # all keys with notes but no .txt
./scripts/sync-txt-gitignore.sh              # refresh theme .gitignore after bib/ingest changes
```

From a consumer (sibling layout): `../ai-alignment-literature/scripts/ensure-extract.sh {citationkey}`.

Requires `pdftotext` (poppler) and network unless a local PDF already exists.

**Legacy note:** older clones may still have tracked `.txt` files; pull this change and run `ensure-extract.sh` locally to rebuild cache.

## PDFs

PDFs stay local (gitignored). Filenames must be `{citationkey}.pdf`.
