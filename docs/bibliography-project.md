# Bibliography — project rules (ai-alignment-literature)

Portable project rules. Shared mechanics: [`bibliography-styleguide.md`](bibliography-styleguide.md). Agent index: [`../AGENTS.md`](../AGENTS.md).

---

## Scope

AI alignment, alignment faking, sleeper / deceptive agents, lie detection, auditing, semantic vulnerabilities of RLHF, mechanistic interpretability / steering / merging (HeRA), adjacent popular press and philosophy-of-consciousness sources.

**Paper summaries here are factual only** (metadata, Summary, key concepts).

**Do not** add `## Relevance to …` in `{citationkey}-notes.md`. Project-specific relevance lives in **consumer repos** (`literature-relevance/`, reader docs, milestones).

---

## `bib.bib`

- **Location:** repository root.
- **Keys:** `{lastname}{year}_{memorable_snake}` per the styleguide.
- Keep **`bib.bib`** in sync with filenames and notes when adding or completing a paper.

---

## Themes (extend before creating new top-level folders)

- `alignment-faking/`
- `sleeper-agents/`
- `lie-detection/`
- `alignment-auditing/`
- `semantic-vulnerabilities/`
- `popular-press/`
- `philosophy_of_consciousness/`
- `interpretability/` — steering, SAEs, LoRA/PEFT, model merging (HeRA cluster)

---

## Per-paper artefacts

In the correct theme folder:

- `{citationkey}.pdf` — local only (gitignored)
- `{citationkey}.txt` — local extract (git policy in styleguide)
- `{citationkey}-notes.md` — curated summary (**commit**)
- optional `{citationkey}.md` — full-text markdown when used

### Git (what goes on the remote)

- **Commit:** `-notes.md`, optional `.md`, `bib.bib`, theme `README.md`, root `CHANGELOG.md`, theme `.gitignore` after `sync-txt-gitignore.sh`.
- **Do not commit:** `*.pdf`.
- **Do not commit `*.txt`** when reproducible from a public PDF in `bib.bib` — regenerate with `./scripts/ensure-extract.sh {citationkey}`.
- **Exception:** `git add -f <theme>/{citationkey}.txt` when no stable public PDF exists.

### README line (authors first)

Sort theme `README.md` bullets by **publication year ascending** (oldest first).

```markdown
- {Author1} & {Author2} - [{Title}](https://scholar.google.com/scholar?q={query}) ({Year}) - [PDF]({url}) - [`{citationkey}`]({citationkey}-notes.md)
```

For **partial ingest** (extract only, no `-notes.md` yet), list the key in a “partial / no notes yet” subsection — see `interpretability/README.md`.

---

## Ingestion checklist (definition of done)

1. Citation key — matches all filenames.
2. **`bib.bib`** entry — include `eprint` / open `url` when a public PDF exists.
3. Theme folder.
4. **`{citationkey}-notes.md`** — metadata, summary, key concepts (**no relevance**).
5. PDF — `{citationkey}.pdf` (gitignored); fetch via `ensure-extract.sh` when possible.
6. Text — `./scripts/ensure-extract.sh {citationkey}` or `pdftotext` (local; do not commit if regenerable).
7. **`./scripts/sync-txt-gitignore.sh`** — refresh theme `.gitignore` for `.txt` policy.
8. Theme **`README.md`**.
9. Root **`README.md`** master index (when note is curated).
10. **`CHANGELOG.md`** — prepend bullet under `## YYYY-MM-DD`.

**Not** part of default ingest: Marker — only when the user explicitly requests it.

---

## Consumer repositories

See [SETUP.md](../SETUP.md). Consumers link with filesystem relatives (`../ai-alignment-literature/…`) and keep their own `latex/references.bib` or `LITERATURE.md` pointers in sync when adding keys.

---

## Backlog / partial ingest

When only an extract exists (common in `interpretability/`):

1. Ensure **`bib.bib`** entry with open `url` / `eprint`.
2. Regenerate **`{citationkey}.txt`** locally — do not commit if public PDF exists.
3. Add theme `README.md` line.
4. When promoting to full ingest: add **`{citationkey}-notes.md`**, root `README.md` link, `CHANGELOG.md`.

Do not treat tracked legacy `.txt` files as policy — prefer `sync-txt-gitignore.sh` and stop committing new regenerable extracts.
