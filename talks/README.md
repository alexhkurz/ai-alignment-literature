# Talks

This folder holds slide decks and summary notes for talks. Slide binaries are local only and **not committed**.

## Conventions

- **Slide file** — `{speaker}_{date}.{ext}` or `{event}_{speaker}_{date}.{ext}` (e.g. `JC__Sep_09_2026.pptx`). Gitignored.
- **Summary file** — same basename with `.md`: `{base}.md`. **Committed.**
- **No `bib.bib` entry** and no `CHANGELOG.md` bullet for talks.
- **No `citationkey`**. Link to relevant ingested paper notes with relative paths.

## Ingesting a talk

1. Copy the slide file into `talks/` (it will be ignored by Git).
2. Create `{base}.md` with:
   - Speaker, date, source slide link
   - Short summary
   - Key concepts
   - **Related paper summaries** — link to relevant `{citationkey}.md` notes
3. Add a line to this `README.md` (sorted by date, newest last).

## Talks

- 2026-09-09 — [Verbalizable Representations Form a Global Workspace in Language Models](JC__Sep_09_2026.md)
