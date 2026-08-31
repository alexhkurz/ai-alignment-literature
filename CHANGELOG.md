# Bibliography changelog

Newest first. Full ToC in the [README.md](README.md).

---

## 2026-08-31

- Activation steering reader (9 papers) in [`interpretability/`](interpretability/README.md#activation-steering-reader-curated-notes): [`mikolov2013_word2vec`](interpretability/mikolov2013_word2vec-notes.md), [`tenney2019_bert_pipeline`](interpretability/tenney2019_bert_pipeline-notes.md), [`belinkov2019_analysis_methods`](interpretability/belinkov2019_analysis_methods-notes.md), [`kim2018tcav`](interpretability/kim2018tcav-notes.md), [`meng2022_rome`](interpretability/meng2022_rome-notes.md), [`wang2022_ioi`](interpretability/wang2022_ioi-notes.md), [`olsson2022_induction_heads`](interpretability/olsson2022_induction_heads-notes.md), [`elhage2022_superposition`](interpretability/elhage2022_superposition-notes.md), [`hanna2023_greater_than`](interpretability/hanna2023_greater_than-notes.md).
- Tier A reader background (9 papers) in [`interpretability/`](interpretability/README.md#reader-background-tier-a--curated-notes): [`vaswani2017_attention`](interpretability/vaswani2017_attention-notes.md), [`elhage2021_transformer_circuits`](interpretability/elhage2021_transformer_circuits-notes.md), [`aghajanyan2021_intrinsic_dimensionality`](interpretability/aghajanyan2021_intrinsic_dimensionality-notes.md), [`pearlmutter1994_fast_hessian`](interpretability/pearlmutter1994_fast_hessian-notes.md), [`rumelhart1986_backprop`](interpretability/rumelhart1986_backprop-notes.md), [`geva2021_key_value_memories`](interpretability/geva2021_key_value_memories-notes.md), [`dar2022_analyzing_transformers`](interpretability/dar2022_analyzing_transformers-notes.md), [`he2016_deep_residual`](interpretability/he2016_deep_residual-notes.md), [`martens2010_hessian_free`](interpretability/martens2010_hessian_free-notes.md).
- Fixed `scripts/literature_extract.py` `download_pdf` to write fetched bytes to disk.
- Stopped tracking regenerable `{citationkey}.txt` files (47 removed from git; arXiv / OpenReview / ACL Anthology / similar public PDFs in `bib.bib`). Pinned extracts kept for books, popular press, paywalled HTML (`bricken2023towards`), and `mcintosh2024rlhf_semantic_vulnerabilities`.
- [`AGENTS.md`](AGENTS.md), [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md), [`docs/bibliography-project.md`](docs/bibliography-project.md) — bibliography rules aligned with ai-math-formal-methods (`.txt` local-by-default).
- [`scripts/literature_extract.py`](scripts/literature_extract.py) — fixed `bib.bib` key parsing; classify keys from theme `.txt` artefacts; OpenReview / ACL / PMLR PDF URL helpers.

## 2026-08-24

- Ingested HeRA / HeRD-Merging bibliography into [`interpretability/`](interpretability/README.md): ~40 PDFs (local) + `.txt` extracts, entries appended to `bib.bib`. Consumer: [hera](https://github.com/alexhkurz/hera). Still missing notes; OpenReview-only `sun2025layernavigator`, IEEE `11224465`, and two books without PDFs.
- Migrated thematic folders and `bib.bib` from `literature-review-and-docs` / `chapman-alignment-faking` into this standalone sister repo (quantale-enriched-literature pattern). Project relevance moved to each consumer’s `literature-relevance/`.

## 2026-05-20

- [The Ego Tunnel: The Science of the Mind and the Myth of the Self](philosophy_of_consciousness/metzinger2009_ego_tunnel-notes.md) — `metzinger2009_ego_tunnel`
- [Being You: A New Science of Consciousness](philosophy_of_consciousness/seth2021_being_you-notes.md) — `seth2021_being_you`
- [Self-awareness, a singularity of AI](philosophy_of_consciousness/wang2023_singularity-notes.md) — `wang2023_singularity`

## 2026-05-04


## 2026-04-20

- [The escalating global A.I. arms race](popular-press/frenkel2026global_ai_arms-notes.md) — `frenkel2026global_ai_arms`
- [We don't really know how A.I. works. That's a problem](popular-press/whang2026ai_black_box-notes.md) — `whang2026ai_black_box`
- [You have no choice in reading this article—maybe](popular-press/scoles2026free_will_maoz-notes.md) — `scoles2026free_will_maoz`

## Initial Papers

- [Poser: Unmasking alignment faking LLMs by manipulating their internals](alignment-faking/clymer2024poser-notes.md) — `clymer2024poser`
- [Alignment faking in large language models](alignment-faking/greenblatt2024alignment_faking-notes.md) — `greenblatt2024alignment_faking`
- [Natural emergent misalignment from reward hacking in production RL](alignment-faking/macdiarmid2025emergent_misalignment-notes.md) — `macdiarmid2025emergent_misalignment`
- [How to catch an AI liar: lie detection in black-box LLMs by asking unrelated questions](lie-detection/pacchiardi2023catch_a_liar-notes.md) — `pacchiardi2023catch_a_liar`
- [Sleeper agents: training deceptive LLMs that persist through safety training](sleeper-agents/hubinger2024sleeper_agents-notes.md) — `hubinger2024sleeper_agents`
