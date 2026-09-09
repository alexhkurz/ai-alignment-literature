# Bibliography changelog

Newest first. Full ToC in the [README.md](README.md).

---

## 2026-09-08

- [`ho2026declarative_attention`](interpretability/ho2026declarative_attention.md) — Declarative Attention (DA): zero-shot protocol where the model declares its attention scope (`<global>` / `<focus>` / `<local>` tags) in its chain-of-thought; inference engine masks the KV cache accordingly (arXiv:2609.02737).
- Backfilled `bib.bib` entries and `alignment-faking/README.md` "Partial / no notes yet" lines for `koorndijk2025alignment_faking_small_llm` (arXiv:2506.21584) and `taylor2025school_reward_hacks` (arXiv:2508.17511); both `.txt` extracts are regenerable and gitignored.
- Promoted 10 `interpretability/` partial extracts to curated `.md` notes: [`apolinario2026lancelowrankactivation`](interpretability/apolinario2026lancelowrankactivation.md), [`bai2025qwen25vltechnicalreport`](interpretability/bai2025qwen25vltechnicalreport.md), [`braun2025understanding`](interpretability/braun2025understanding.md), [`cunningham2023sparseautoencodershighlyinterpretable`](interpretability/cunningham2023sparseautoencodershighlyinterpretable.md), [`ding2023enhancingchatlanguagemodels`](interpretability/ding2023enhancingchatlanguagemodels.md), [`dunefsky2025oneshot`](interpretability/dunefsky2025oneshot.md), [`fang-etal-2026-controllable`](interpretability/fang-etal-2026-controllable.md), [`gemmateam2026gemma4technicalreport`](interpretability/gemmateam2026gemma4technicalreport.md), [`he2023debertav`](interpretability/he2023debertav.md), [`heyman2026steer`](interpretability/heyman2026steer.md); added `braun2025understanding`, `dunefsky2025oneshot`, `he2023debertav`, and `heyman2026steer` to `bib.bib`.
- Standardized on `{citationkey}.md` as the canonical curated-note filename: renamed all `*-notes.md` files, deleted full-text/extract `.md` files, and updated `README.md`, theme `README.md`, `AGENTS.md`, `docs/bibliography-styleguide.md`, `docs/bibliography-project.md`, and `.cursor/rules/workspace.mdc` to use `.md` only.

## 2026-08-31

- [`tenney2019_edge_probing`](interpretability/tenney2019_edge_probing.md) — ICLR 2019 edge-probing method paper (prerequisite to [`tenney2019_bert_pipeline`](interpretability/tenney2019_bert_pipeline.md)).
- Activation steering reader (9 papers) in [`interpretability/`](interpretability/README.md#activation-steering-reader-curated-notes): [`mikolov2013_word2vec`](interpretability/mikolov2013_word2vec.md), [`tenney2019_bert_pipeline`](interpretability/tenney2019_bert_pipeline.md), [`belinkov2019_analysis_methods`](interpretability/belinkov2019_analysis_methods.md), [`kim2018tcav`](interpretability/kim2018tcav.md), [`meng2022_rome`](interpretability/meng2022_rome.md), [`wang2022_ioi`](interpretability/wang2022_ioi.md), [`olsson2022_induction_heads`](interpretability/olsson2022_induction_heads.md), [`elhage2022_superposition`](interpretability/elhage2022_superposition.md), [`hanna2023_greater_than`](interpretability/hanna2023_greater_than.md).
- Tier A reader background (9 papers) in [`interpretability/`](interpretability/README.md#reader-background-tier-a--curated-notes): [`vaswani2017_attention`](interpretability/vaswani2017_attention.md), [`elhage2021_transformer_circuits`](interpretability/elhage2021_transformer_circuits.md), [`aghajanyan2021_intrinsic_dimensionality`](interpretability/aghajanyan2021_intrinsic_dimensionality.md), [`pearlmutter1994_fast_hessian`](interpretability/pearlmutter1994_fast_hessian.md), [`rumelhart1986_backprop`](interpretability/rumelhart1986_backprop.md), [`geva2021_key_value_memories`](interpretability/geva2021_key_value_memories.md), [`dar2022_analyzing_transformers`](interpretability/dar2022_analyzing_transformers.md), [`he2016_deep_residual`](interpretability/he2016_deep_residual.md), [`martens2010_hessian_free`](interpretability/martens2010_hessian_free.md).
- Fixed `scripts/literature_extract.py` `download_pdf` to write fetched bytes to disk.
- Stopped tracking regenerable `{citationkey}.txt` files (47 removed from git; arXiv / OpenReview / ACL Anthology / similar public PDFs in `bib.bib`). Pinned extracts kept for books, popular press, paywalled HTML (`bricken2023towards`), and `mcintosh2024rlhf_semantic_vulnerabilities`.
- [`AGENTS.md`](AGENTS.md), [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md), [`docs/bibliography-project.md`](docs/bibliography-project.md) — bibliography rules aligned with ai-math-formal-methods (`.txt` local-by-default).
- [`scripts/literature_extract.py`](scripts/literature_extract.py) — fixed `bib.bib` key parsing; classify keys from theme `.txt` artefacts; OpenReview / ACL / PMLR PDF URL helpers.

## 2026-08-24

- Ingested HeRA / HeRD-Merging bibliography into [`interpretability/`](interpretability/README.md): ~40 PDFs (local) + `.txt` extracts, entries appended to `bib.bib`. Consumer: [hera](https://github.com/alexhkurz/hera). Still missing notes; OpenReview-only `sun2025layernavigator`, IEEE `11224465`, and two books without PDFs.
- Migrated thematic folders and `bib.bib` from `literature-review-and-docs` / `chapman-alignment-faking` into this standalone sister repo (quantale-enriched-literature pattern). Project relevance moved to each consumer’s `literature-relevance/`.

## 2026-05-20

- [The Ego Tunnel: The Science of the Mind and the Myth of the Self](philosophy_of_consciousness/metzinger2009_ego_tunnel.md) — `metzinger2009_ego_tunnel`
- [Being You: A New Science of Consciousness](philosophy_of_consciousness/seth2021_being_you.md) — `seth2021_being_you`
- [Self-awareness, a singularity of AI](philosophy_of_consciousness/wang2023_singularity.md) — `wang2023_singularity`

## 2026-05-04


## 2026-04-20

- [The escalating global A.I. arms race](popular-press/frenkel2026global_ai_arms.md) — `frenkel2026global_ai_arms`
- [We don't really know how A.I. works. That's a problem](popular-press/whang2026ai_black_box.md) — `whang2026ai_black_box`
- [You have no choice in reading this article—maybe](popular-press/scoles2026free_will_maoz.md) — `scoles2026free_will_maoz`

## Initial Papers

- [Poser: Unmasking alignment faking LLMs by manipulating their internals](alignment-faking/clymer2024poser.md) — `clymer2024poser`
- [Alignment faking in large language models](alignment-faking/greenblatt2024alignment_faking.md) — `greenblatt2024alignment_faking`
- [Natural emergent misalignment from reward hacking in production RL](alignment-faking/macdiarmid2025emergent_misalignment.md) — `macdiarmid2025emergent_misalignment`
- [How to catch an AI liar: lie detection in black-box LLMs by asking unrelated questions](lie-detection/pacchiardi2023catch_a_liar.md) — `pacchiardi2023catch_a_liar`
- [Sleeper agents: training deceptive LLMs that persist through safety training](sleeper-agents/hubinger2024sleeper_agents.md) — `hubinger2024sleeper_agents`
