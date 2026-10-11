# Bibliography changelog

Newest first. Full ToC in the [README.md](README.md).

---

## 2026-09-30

- New theme [`j-space/`](j-space/README.md) — Jacobian lens / J-space cluster: moved [`gurnee2026_global_workspace`](j-space/gurnee2026_global_workspace.md) from `interpretability-anthropic/` (pointer left there); ingested [`wu2026_j_cot`](j-space/wu2026_j_cot.md), [`ma2026_hidden_apis`](j-space/ma2026_hidden_apis.md), [`titov2026_jspace_reentry`](j-space/titov2026_jspace_reentry.md), [`oskin2026_off_axis`](j-space/oskin2026_off_axis.md), [`song2026_j_access`](j-space/song2026_j_access.md), [`lange2026_jspace_standpoint`](j-space/lange2026_jspace_standpoint.md) (local PDF; pinned `.txt`), [`wang2026_looped_jacobian`](j-space/wang2026_looped_jacobian.md); `bib.bib`, root [`README.md`](README.md), [`docs/bibliography-project.md`](docs/bibliography-project.md), [`talks/JC__Sep_09_2026.md`](talks/JC__Sep_09_2026.md).

## 2026-09-25

- HeRA literature gaps: [`Scalena_2024`](interpretability/Scalena_2024.md) (BlackboxNLP 2024 Dynamic Activation Composition), [`oozeer2026linearsteeringunifiedmultiattribute`](interpretability/oozeer2026linearsteeringunifiedmultiattribute.md) (K-Steering; arXiv:2505.24535), [`vanderweij2024extendingactivationsteeringbroad`](interpretability/vanderweij2024extendingactivationsteeringbroad.md) (arXiv:2403.05767); `bib.bib`, [`interpretability/README.md`](interpretability/README.md), root [`README.md`](README.md).

## 2026-09-16

- New theme [`attention/`](attention/README.md) — BertViz ([`vig2019_multiscale_attention`](attention/vig2019_multiscale_attention.md)), BERT geometry ([`coenen2019_geometry_bert`](attention/coenen2019_geometry_bert.md)), Illustrated Transformer ([`alammar2018_illustrated_transformer`](attention/alammar2018_illustrated_transformer.md)), nanoGPT ([`karpathy2022_nanogpt`](attention/karpathy2022_nanogpt.md)); cross-link to existing [`elhage2021_transformer_circuits`](interpretability-anthropic/elhage2021_transformer_circuits.md); `bib.bib`, root [`README.md`](README.md).
- [`shafiq2022deep_residual_survey`](interpretability/shafiq2022deep_residual_survey.md) — MDPI 2022 ResNet survey (open challenges §13, post-2022 follow-up in note); [`interpretability/README.md`](interpretability/README.md), root [`README.md`](README.md).
- Ingested Google Scholar corpus [`authors/rimkevicius/`](authors/rimkevicius/README.md) — Paulius Rimkevičius (Chapman; `JEEYxL4AAAAJ`): 16 works (free will, volition/EEG, ISA self-knowledge, cross-cultural cognition, AI moral responsibility talk); `bib.bib` entries; curated `{key}.md` notes; extended `scripts/literature_extract.py` for `authors/<researcher>/` folders.
- [`publications/README.md`](publications/README.md) — index of papers migrated from `literature-review-and-docs` / `chapman-alignment-faking` (links to alignment cluster theme folders; excludes HeRA `interpretability/`).

## 2026-09-15

- [`readers/instruction-following.md`](readers/instruction-following.md) — background reader on why instruction following works (ICL / SFT / RLHF; empirical, representational, and circuit-level literatures); moved from `interpretability/` to new [`readers/`](readers/README.md) folder; appendix speculates on using HeRD-Merging to study the “which mechanism implements follow this instruction” question.

## 2026-09-13

- [`subramani2022_extracting_steering_vectors`](interpretability/subramani2022_extracting_steering_vectors.md) — ACL Findings 2022 paper on extracting steering vectors from frozen GPT-2 decoders (>99 BLEU target recovery, sentiment transfer, STS-B similarity); [`interpretability/README.md`](interpretability/README.md), root [`README.md`](README.md).
- Regenerated [`README.md`](README.md) master index (A–Z by last name): all curated `{citationkey}.md` notes linked; partial-ingest section lists the four remaining `bib.bib`-only extracts.
- Ingested remaining HeRA (`hera/latex/references.bib`) gaps into `interpretability/`: added `bib.bib` entries for [`chatterjee2007fluctuationseigenvaluessecondorder`](interpretability/chatterjee2007fluctuationseigenvaluessecondorder.md), [`jiang2023mistral7b`](interpretability/jiang2023mistral7b.md), [`hörmander2015analysis`](interpretability/hörmander2015analysis.md); promoted 11 partial extracts to curated notes ([`11224465`](interpretability/11224465.md), [`levenbergmarquardt`](interpretability/levenbergmarquardt.md), [`ramsay2005functional`](interpretability/ramsay2005functional.md), [`sun2025layernavigator`](interpretability/sun2025layernavigator.md), [`tan2024analysing`](interpretability/tan2024analysing.md), [`turner2024steeringlanguagemodelsactivation`](interpretability/turner2024steeringlanguagemodelsactivation.md), [`xu-etal-2026-steering`](interpretability/xu-etal-2026-steering.md), [`yadav2023tiesmerging`](interpretability/yadav2023tiesmerging.md), [`yu2024language`](interpretability/yu2024language.md), [`zhao2026odesteer`](interpretability/zhao2026odesteer.md), [`zou2023representationengineeringtopdownapproach`](interpretability/zou2023representationengineeringtopdownapproach.md)); added [`wortsman2021_neural_subspaces`](interpretability/wortsman2021_neural_subspaces.md) for HeRA key `DBLP:journals/corr/abs-2102-10472`; updated [`interpretability/README.md`](interpretability/README.md).

## 2026-09-08

- Promoted 10 more `interpretability/` extracts to curated `.md` notes: [`panickssery2024steeringllama2contrastive`](interpretability/panickssery2024steeringllama2contrastive.md), [`pham-nguyen-2024-householder`](interpretability/pham-nguyen-2024-householder.md), [`pmlr-v235-singh24d`](interpretability/pmlr-v235-singh24d.md), [`prabhakar2024lorasoupsmergingloras`](interpretability/prabhakar2024lorasoupsmergingloras.md), [`rodriguez2024controllinglanguagediffusionmodels`](interpretability/rodriguez2024controllinglanguagediffusionmodels.md), [`sharkey2025openproblemsmechanisticinterpretability`](interpretability/sharkey2025openproblemsmechanisticinterpretability.md), [`sharma2026coldsteer`](interpretability/sharma2026coldsteer.md), [`shu2025surveysparseautoencodersinterpreting`](interpretability/shu2025surveysparseautoencodersinterpreting.md), [`soo2025interpretable`](interpretability/soo2025interpretable.md), [`stoica2024modelmergingsvdtie`](interpretability/stoica2024modelmergingsvdtie.md); added `sharma2026coldsteer` and `soo2025interpretable` to `bib.bib`; regenerated `README.md` A–Z and `interpretability/README.md`.
- Created `interpretability-anthropic/` theme for Anthropic's [Transformer Circuits thread](https://transformer-circuits.pub/); moved [`elhage2021_transformer_circuits`](interpretability-anthropic/elhage2021_transformer_circuits.md), [`olsson2022_induction_heads`](interpretability-anthropic/olsson2022_induction_heads.md), [`elhage2022_superposition`](interpretability-anthropic/elhage2022_superposition.md), and [`bricken2023towards`](interpretability-anthropic/bricken2023towards.md) from `interpretability/`; ingested 10 additional thread research posts with `{citationkey}.md` summaries and untracked `{citationkey}.txt` extracts (no `.pdf`); added `bib.bib` entries; updated `README.md`, `interpretability-anthropic/README.md`, `interpretability/README.md`, and the `ingest` skill's blog/HTML rule.
- [`ho2026declarative_attention`](interpretability/ho2026declarative_attention.md) — Declarative Attention (DA): zero-shot protocol where the model declares its attention scope (`<global>` / `<focus>` / `<local>` tags) in its chain-of-thought; inference engine masks the KV cache accordingly (arXiv:2609.02737).
- Backfilled `bib.bib` entries and `alignment-faking/README.md` "Partial / no notes yet" lines for `koorndijk2025alignment_faking_small_llm` (arXiv:2506.21584) and `taylor2025school_reward_hacks` (arXiv:2508.17511); both `.txt` extracts are regenerable and gitignored.
- Promoted 10 `interpretability/` partial extracts to curated `.md` notes: [`apolinario2026lancelowrankactivation`](interpretability/apolinario2026lancelowrankactivation.md), [`bai2025qwen25vltechnicalreport`](interpretability/bai2025qwen25vltechnicalreport.md), [`braun2025understanding`](interpretability/braun2025understanding.md), [`cunningham2023sparseautoencodershighlyinterpretable`](interpretability/cunningham2023sparseautoencodershighlyinterpretable.md), [`ding2023enhancingchatlanguagemodels`](interpretability/ding2023enhancingchatlanguagemodels.md), [`dunefsky2025oneshot`](interpretability/dunefsky2025oneshot.md), [`fang-etal-2026-controllable`](interpretability/fang-etal-2026-controllable.md), [`gemmateam2026gemma4technicalreport`](interpretability/gemmateam2026gemma4technicalreport.md), [`he2023debertav`](interpretability/he2023debertav.md), [`heyman2026steer`](interpretability/heyman2026steer.md); added `braun2025understanding`, `dunefsky2025oneshot`, `he2023debertav`, and `heyman2026steer` to `bib.bib`.
- Standardized on `{citationkey}.md` as the canonical curated-note filename: renamed all `*-notes.md` files, deleted full-text/extract `.md` files, and updated `README.md`, theme `README.md`, `AGENTS.md`, `docs/bibliography-styleguide.md`, `docs/bibliography-project.md`, and `.cursor/rules/workspace.mdc` to use `.md` only.
- Promoted another 10 `interpretability/` extracts to curated `.md` notes: [`hu2021loralowrankadaptation`](interpretability/hu2021loralowrankadaptation.md), [`ilharco2023editingmodelstaskarithmetic`](interpretability/ilharco2023editingmodelstaskarithmetic.md), [`kangaslahti2025continuous`](interpretability/kangaslahti2025continuous.md), [`kingma2017adammethodstochasticoptimization`](interpretability/kingma2017adammethodstochasticoptimization.md), [`koike-akino2025quantumpeft`](interpretability/koike-akino2025quantumpeft.md), [`kong2024aligning`](interpretability/kong2024aligning.md), [`leask2025inferencetimedecompositionactivationsitda`](interpretability/leask2025inferencetimedecompositionactivationsitda.md), [`li2024llmsasjudgescomprehensivesurveyllmbased`](interpretability/li2024llmsasjudgescomprehensivesurveyllmbased.md), [`menon-etal-2025-analyzing`](interpretability/menon-etal-2025-analyzing.md), [`nelwan2026deployableperinstancemultilayeractivation`](interpretability/nelwan2026deployableperinstancemultilayeractivation.md); added `ilharco2023editingmodelstaskarithmetic`, `kangaslahti2025continuous`, `koike-akino2025quantumpeft`, and `kong2024aligning` to `bib.bib`.

## 2026-08-31

- [`tenney2019_edge_probing`](interpretability/tenney2019_edge_probing.md) — ICLR 2019 edge-probing method paper (prerequisite to [`tenney2019_bert_pipeline`](interpretability/tenney2019_bert_pipeline.md)).
- Activation steering reader (9 papers) in [`interpretability/`](interpretability/README.md#activation-steering-reader-curated-notes): [`mikolov2013_word2vec`](interpretability/mikolov2013_word2vec.md), [`tenney2019_bert_pipeline`](interpretability/tenney2019_bert_pipeline.md), [`belinkov2019_analysis_methods`](interpretability/belinkov2019_analysis_methods.md), [`kim2018tcav`](interpretability/kim2018tcav.md), [`meng2022_rome`](interpretability/meng2022_rome.md), [`wang2022_ioi`](interpretability/wang2022_ioi.md), [`olsson2022_induction_heads`](interpretability-anthropic/olsson2022_induction_heads.md), [`elhage2022_superposition`](interpretability-anthropic/elhage2022_superposition.md), [`hanna2023_greater_than`](interpretability/hanna2023_greater_than.md).
- Tier A reader background (9 papers) in [`interpretability/`](interpretability/README.md#reader-background-tier-a--curated-notes): [`vaswani2017_attention`](interpretability/vaswani2017_attention.md), [`elhage2021_transformer_circuits`](interpretability-anthropic/elhage2021_transformer_circuits.md), [`aghajanyan2021_intrinsic_dimensionality`](interpretability/aghajanyan2021_intrinsic_dimensionality.md), [`pearlmutter1994_fast_hessian`](interpretability/pearlmutter1994_fast_hessian.md), [`rumelhart1986_backprop`](interpretability/rumelhart1986_backprop.md), [`geva2021_key_value_memories`](interpretability/geva2021_key_value_memories.md), [`dar2022_analyzing_transformers`](interpretability/dar2022_analyzing_transformers.md), [`he2016_deep_residual`](interpretability/he2016_deep_residual.md), [`martens2010_hessian_free`](interpretability/martens2010_hessian_free.md).
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
