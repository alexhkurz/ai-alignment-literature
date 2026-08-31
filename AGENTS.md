# Agent instructions (ai-alignment-literature)

Canonical shared literature tree for the AI alignment / alignment-faking research cluster. Human overview: [README.md](README.md). Sister-repo layout: [SETUP.md](SETUP.md).

---

## Rule stack

When you touch **`bib.bib`**, theme folders, or paper notes:

1. [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md) — keys, `.bib` hygiene, folder workflow, note template, **Git / `.txt` policy**.
2. [`docs/bibliography-project.md`](docs/bibliography-project.md) — themes, README lines, ingestion checklist, **no relevance sections here**.
3. [`.cursor/rules/references.mdc`](.cursor/rules/references.mdc) — `bib.bib` path and key examples.

Global mechanics not duplicated locally: [`../bib-mcp/docs/styleguide.md`](../bib-mcp/docs/styleguide.md) (when **bib-mcp** is in the workspace).

---

## Repository shape

- **`bib.bib`** at repo root.
- **Theme folders** at repo root (`alignment-faking/`, `interpretability/`, …) — not a nested `bibliography/`.
- **Curated notes:** `{citationkey}-notes.md` (factual summary only; no project relevance).
- **Per paper:** `{citationkey}.pdf` (local), `{citationkey}.txt` (local extract), optional `{citationkey}.md`.

---

## Text extracts (essentials)

- **Default:** `{citationkey}.txt` is **local** — do **not** commit when reproducible from a **public** PDF (`eprint` / open `url` in `bib.bib`).
- **Regenerate:** `./scripts/ensure-extract.sh {citationkey}` (needs `pdftotext`; downloads arXiv/open URLs when needed).
- **Exception:** `git add -f <theme>/{citationkey}.txt` only when **no** stable public PDF exists (paywall, print-only, private scan).
- After bulk ingest or bib changes: `./scripts/sync-txt-gitignore.sh` refreshes theme-folder `.gitignore` files for regenerable vs pinned `.txt`.

---

## Ingestion done when

`bib.bib` + `{citationkey}-notes.md` (or completed partial ingest) + theme `README.md` + root **`CHANGELOG.md`** bullet (prepend under `## YYYY-MM-DD`).

**Do not** add `## Relevance to …` in this repo — consumer repos hold `literature-relevance/`.

---

## Tool-specific loaders

| Tool | Reads |
|------|--------|
| **Any** | This file (`AGENTS.md`) |
| **Cursor** | Also `.cursor/rules/*.mdc` |
| **bib-mcp** | `bib-mcp/.cursor/rules/cursor-bibliography-rules.mdc` when present |

Do not duplicate long prose in `.cursor/rules/` — update `docs/` first, then refresh thin Cursor wrappers.
