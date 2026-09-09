# AI alignment literature

Canonical paper summaries, text extracts, and `bib.bib` for the AI alignment / alignment-faking research cluster. Consumer repos (Chapman alignment faking, planning docs, …) use this repository as a sister checkout (same parent directory) — see [SETUP.md](SETUP.md) and each consumer’s `LITERATURE.md`.

**Setup:** [SETUP.md](SETUP.md) · **Agent rules:** [AGENTS.md](AGENTS.md) · **Ingestion:** [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md), [`docs/bibliography-project.md`](docs/bibliography-project.md)

**Ingestion log:** every new or completed paper must get a bullet in [CHANGELOG.md](CHANGELOG.md) and an entry in **Papers (A–Z by first author)** below, at the same time as the note / `bib.bib` / subfolder `README` updates.

**Relevance:** do not add project-specific `## Relevance` sections here — keep those in each consumer repo (`literature-relevance/`).

## Subfolders

- [alignment-faking](alignment-faking/README.md) — core alignment-faking and related empirical work.
- [sleeper-agents](sleeper-agents/README.md) — deceptive / backdoored LLMs and resistance to safety training.
- [lie-detection](lie-detection/README.md) — detecting deceptive or false LLM outputs (black-box methods, evaluation).
- [alignment-auditing](alignment-auditing/README.md) — auditing benchmarks and related evaluation tooling (partial ingest).
- [semantic-vulnerabilities](semantic-vulnerabilities/README.md) — RLHF / semantic vulnerability work (partial ingest).
- [popular-press](popular-press/README.md) — reporting on AI capabilities, interpretability, and adjacent themes.
- [philosophy_of_consciousness](philosophy_of_consciousness/README.md) — consciousness, subjective experience, and self-consciousness in humans and AI.
- [interpretability](interpretability/README.md) — steering, SAEs, LoRA/PEFT, model merging (HeRA bibliography; partial ingest).

## Papers (A–Z by first author)

Curated summaries (`{citationkey}.md`).

- [David E. Rumelhart et al. — *Learning representations by back-propagating errors* (1986)](./interpretability/rumelhart1986_backprop.md)
- [Tomas Mikolov et al. — *Distributed Representations of Words and Phrases and their Compositionality* (2013)](./interpretability/mikolov2013_word2vec.md)
- [Kaiming He et al. — *Deep residual learning for image recognition* (2016)](./interpretability/he2016_deep_residual.md)
- [Ashish Vaswani et al. — *Attention is all you need* (2017)](./interpretability/vaswani2017_attention.md)
- [Been Kim et al. — *TCAV: Relative Concept Importance Testing with Linear Concept Activation Vectors* (2018)](./interpretability/kim2018tcav.md)
- [Ian Tenney et al. — *BERT Rediscovers the Classical NLP Pipeline* (2019)](./interpretability/tenney2019_bert_pipeline.md)
- [Ian Tenney et al. — *What do you learn from context? Probing for sentence structure in contextualized word representations* (2019)](./interpretability/tenney2019_edge_probing.md)
- [Yonatan Belinkov et al. — *Analysis Methods in Neural Language Processing: A Survey* (2019)](./interpretability/belinkov2019_analysis_methods.md)
- [Armen Aghajanyan et al. — *Intrinsic dimensionality explains the effectiveness of language model fine-tuning* (2021)](./interpretability/aghajanyan2021_intrinsic_dimensionality.md)
- [Mor Geva et al. — *Transformer feed-forward layers are key-value memories* (2021)](./interpretability/geva2021_key_value_memories.md)
- [Nelson Elhage et al. — *A mathematical framework for transformer circuits* (2021)](./interpretability/elhage2021_transformer_circuits.md)
- [Catherine Olsson et al. — *In-context Learning and Induction Heads* (2022)](./interpretability/olsson2022_induction_heads.md)
- [Kevin Meng et al. — *Locating and Editing Factual Associations in GPT* (2022)](./interpretability/meng2022_rome.md)
- [Kevin Wang et al. — *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small* (2022)](./interpretability/wang2022_ioi.md)
- [Nelson Elhage et al. — *Toy Models of Superposition* (2022)](./interpretability/elhage2022_superposition.md)
- [Guy Dar et al. — *Analyzing transformers in embedding space* (2023)](./interpretability/dar2022_analyzing_transformers.md)
- [Hoagy Cunningham et al. — *Sparse Autoencoders Find Highly Interpretable Features in Language Models* (2023)](./interpretability/cunningham2023sparseautoencodershighlyinterpretable.md)
- [Lorenzo Pacchiardi et al. — *How to catch an AI liar: lie detection in black-box LLMs by asking unrelated questions* (2023)](./lie-detection/pacchiardi2023catch_a_liar.md)
- [Michael Hanna et al. — *How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model* (2023)](./interpretability/hanna2023_greater_than.md)
- [Ning Ding et al. — *Enhancing Chat Language Models by Scaling High-quality Instructional Conversations* (2023)](./interpretability/ding2023enhancingchatlanguagemodels.md)
- [Pengcheng He et al. — *DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing* (2023)](./interpretability/he2023debertav.md)
- [Evan Hubinger et al. — *Sleeper agents: training deceptive LLMs that persist through safety training* (2024)](./sleeper-agents/hubinger2024sleeper_agents.md)
- [Joshua Clymer et al. — *Poser: Unmasking alignment faking LLMs by manipulating their internals* (2024)](./alignment-faking/clymer2024poser.md)
- [Ryan Greenblatt et al. — *Alignment faking in large language models* (2024)](./alignment-faking/greenblatt2024alignment_faking.md)
- [Jacob Dunefsky et al. — *One-shot Optimized Steering Vectors Mediate Safety-relevant Behaviors in LLMs* (2025)](./interpretability/dunefsky2025oneshot.md)
- [Joschka Braun et al. — *Understanding (Un)Reliability of Steering Vectors in Language Models* (2025)](./interpretability/braun2025understanding.md)
- [Monte MacDiarmid et al. — *Natural emergent misalignment from reward hacking in production RL* (2025)](./alignment-faking/macdiarmid2025emergent_misalignment.md)
- [Qwen Team et al. — *Qwen2.5-VL Technical Report* (2025)](./interpretability/bai2025qwen25vltechnicalreport.md)
- [Geert Heyman et al. — *Steer Like the LLM: Activation Steering that Mimics Prompting* (2026)](./interpretability/heyman2026steer.md)
- [Gemma Team et al. — *Gemma 4 Technical Report* (2026)](./interpretability/gemmateam2026gemma4technicalreport.md)
- [Marco P. Apolinario et al. — *LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning* (2026)](./interpretability/apolinario2026lancelowrankactivation.md)
- [Namgyu Ho et al. — *Language Models Can Control Their Own Attention* (2026)](./interpretability/ho2026declarative_attention.md)
- [Sheera Frenkel et al. — *The escalating global A.I. arms race* (2026)](./popular-press/frenkel2026global_ai_arms.md)
- [Yi Fang et al. — *Controllable LLM Reasoning via Sparse Autoencoder-Based Steering* (2026)](./interpretability/fang-etal-2026-controllable.md)
- [James Martens — *Deep learning via Hessian-free optimization* (2010)](./interpretability/martens2010_hessian_free.md)
- [Thomas Metzinger — *The Ego Tunnel: The Science of the Mind and the Myth of the Self* (2009)](./philosophy_of_consciousness/metzinger2009_ego_tunnel.md)
- [Barak A. Pearlmutter — *Fast exact multiplication by the Hessian* (1994)](./interpretability/pearlmutter1994_fast_hessian.md)
- [Sarah Scoles — *You have no choice in reading this article—maybe* (2026)](./popular-press/scoles2026free_will_maoz.md)
- [Anil Seth — *Being You: A New Science of Consciousness* (2021)](./philosophy_of_consciousness/seth2021_being_you.md)
- [Jinchang Wang — *Self-awareness, a singularity of AI* (2023)](./philosophy_of_consciousness/wang2023_singularity.md)
- [Oliver Whang — *We don't really know how A.I. works. That's a problem* (2026)](./popular-press/whang2026ai_black_box.md)

### Partial / no notes yet

- `koorndijk2025alignment_faking_small_llm` — extract in `alignment-faking/`
- `taylor2025school_reward_hacks` — extract in `alignment-faking/`
- `sheshadri2026auditbench` — extract in `alignment-auditing/`
- `mcintosh2024rlhf_semantic_vulnerabilities` — extract in `semantic-vulnerabilities/`
- HeRA bibliography (~40 extracts) — see [interpretability/README.md](interpretability/README.md)

