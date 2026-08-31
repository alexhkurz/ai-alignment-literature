# Bibliography styleguide (ai-alignment-literature)

Shared mechanics for **`bib.bib`**, theme folders, citation keys, ingestion, and Git. Project themes and the no-relevance rule live in [`bibliography-project.md`](bibliography-project.md).

**Rule stack for AI assistants:** [`AGENTS.md`](../AGENTS.md) → this file → [`bibliography-project.md`](bibliography-project.md).

---

## Citation keys

**Default:** `{lastname}{year}_{memorable_snake}` — all **lowercase**, underscore **immediately after** the four-digit year.

**Filenames** (same basename `{citationkey}`):

| File | Role |
|------|------|
| `{citationkey}.pdf` | Local PDF (gitignored) |
| `{citationkey}.txt` | `pdftotext` extract (see [Git](#git)) |
| `{citationkey}-notes.md` | **Curated** summary (commit) |
| `{citationkey}.md` | Optional full-text / extract markdown (commit when used) |
| `{citationkey}.marker.md` | Optional Marker output (opt-in only) |

**Examples:** `greenblatt2024alignment_faking` · `hu2021loralowrankadaptation` · `pacchiardi2023catch_a_liar`

### Link keys in markdown

When a citation key appears as a navigational handle (theme `README`, root `README`, `CHANGELOG`), link the key to the curated note:

```markdown
[`{citationkey}`]({citationkey}-notes.md)
```

Use a path relative to the linking file. Do **not** add a separate `[Summary](…)` next to a bare key.

---

## BibTeX hygiene

- **Authors:** `Lastname, Firstname and Lastname, Firstname`.
- **Titles:** sentence case in prose; `title = {{Title}}` when BibTeX must preserve capitals.
- Include **`doi`** when available.
- **One hyperlink destination:** do not duplicate the same link in `doi` + `url`, or `eprint` + `url` to the same arXiv record. For arXiv: keep `eprint`, `archivePrefix`, optional `primaryClass`; **omit** redundant `url`.
- **Append** new `@…{key,` entries at the **end** of `bib.bib`; edit existing entries in place.

Record **`eprint`** and/or an open **`url`** when a downloadable PDF exists — this drives the `.txt` Git policy below.

---

## Theme folder layout

- Theme folders live at the **repository root** (`alignment-faking/`, `interpretability/`, …).
- Every theme folder that may hold PDFs needs **`.gitignore`** with at least `*.pdf`.
- Run **`./scripts/sync-txt-gitignore.sh`** after ingestion so regenerable `{citationkey}.txt` files are gitignored per theme (see [Git](#git)).

---

## PDF to text

Pandoc does **not** take PDF as input. Default pipeline:

1. Place or fetch `{citationkey}.pdf` (local, gitignored).
2. Run **`./scripts/ensure-extract.sh {citationkey}`** — or manually:
   ```bash
   pdftotext <theme>/{citationkey}.pdf <theme>/{citationkey}.txt
   ```
3. Write or update **`{citationkey}-notes.md`** from the extract (curated; not a raw dump).

**Do not** run Marker unless the user explicitly asks. Default ingestion is **`pdftotext` → `.txt`** plus curated **`-notes.md`**.

For EPUB/HTML sources, pandoc to `{citationkey}.md` where appropriate.

---

## Note file template (`{citationkey}-notes.md`)

Factual only — **no** `## Relevance to …` (consumer repos).

```markdown
# {Title}

**Authors:** …
**Year:** …
**Venue:** … (peer-review status when known)
**Citation key:** `{citationkey}`
**BibTeX entry:** [entry](../../bib.bib#L{line})
**PDF:** [link](url)
**arXiv:** … (if applicable)
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=…)

## Summary
…

## Key concepts
…

## Notes
…
```

List authors once in the metadata block; do not add a separate `## Authors` section.

---

## Git

| Commit | Do not commit (default) |
|--------|-------------------------|
| `{citationkey}-notes.md`, optional `{citationkey}.md`, `bib.bib`, theme `README.md`, `CHANGELOG.md` | `*.pdf` (gitignored in theme folders) |
| | **`*.txt`** when reproducible from a **public** PDF (typical arXiv / open `url` in `bib.bib`) |

### `{citationkey}.txt` — local by default

Same policy as [ai-math-formal-methods `docs/bibliography-styleguide.md`](../../ai-math-formal-methods/docs/bibliography-styleguide.md) § Git:

- If `bib.bib` (or the note) records a **stable public PDF** (`eprint`, arXiv/open `url`, etc.), treat `.txt` as a **regenerable local cache**. Collaborators run `./scripts/ensure-extract.sh {citationkey}`; **do not push** those `.txt` files.
- **`./scripts/sync-txt-gitignore.sh`** rewrites each theme folder’s `.gitignore` so regenerable keys are ignored explicitly; **pinned** keys (local-PDF-only) stay tracked.
- **Exception — commit `.txt`:** only when there is **no** stable public PDF. Then `git add -f <theme>/{citationkey}.txt`.

Requires **`pdftotext`** (poppler). Fetch + extract logic: `scripts/ensure-extract.py`, `scripts/literature_extract.py`.

### Marker

Opt-in only. Output as `{citationkey}.marker.md`; keep separate from curated `-notes.md`.

---

## Adding a paper (mechanics)

1. Citation key.
2. Append **`bib.bib`** (with `eprint` / open `url` when available).
3. Theme folder.
4. **`{citationkey}-notes.md`**.
5. Local PDF → **`ensure-extract.sh`** or `pdftotext`.
6. Theme **`README.md`** line.
7. Root **`README.md`** master index (when curated note exists).
8. **`CHANGELOG.md`** — mandatory bullet under `## YYYY-MM-DD`.

See [`bibliography-project.md`](bibliography-project.md) for theme choice and scope.
