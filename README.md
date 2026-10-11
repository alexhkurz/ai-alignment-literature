# AI alignment literature

Canonical paper summaries, text extracts, and `bib.bib` for the AI alignment / alignment-faking research cluster. Consumer repos (Chapman alignment faking, planning docs, …) use this repository as a sister checkout (same parent directory) — see [SETUP.md](SETUP.md) and each consumer’s `LITERATURE.md`.

**Setup:** [SETUP.md](SETUP.md) · **Agent rules:** [AGENTS.md](AGENTS.md) · **Ingestion:** [`docs/bibliography-styleguide.md`](docs/bibliography-styleguide.md), [`docs/bibliography-project.md`](docs/bibliography-project.md)

**Ingestion log:** every new or completed paper must get a bullet in [CHANGELOG.md](CHANGELOG.md) and an entry in **Papers (A–Z by last name)** below, at the same time as the note / `bib.bib` / subfolder `README` updates.

**Relevance:** do not add project-specific `## Relevance` sections here — keep those in each consumer repo (`literature-relevance/`).

## Subfolders

- [alignment-faking](alignment-faking/README.md) — core alignment-faking and related empirical work.
- [sleeper-agents](sleeper-agents/README.md) — deceptive / backdoored LLMs and resistance to safety training.
- [lie-detection](lie-detection/README.md) — detecting deceptive or false LLM outputs (black-box methods, evaluation).
- [alignment-auditing](alignment-auditing/README.md) — auditing benchmarks and related evaluation tooling (partial ingest).
- [semantic-vulnerabilities](semantic-vulnerabilities/README.md) — RLHF / semantic vulnerability work (partial ingest).
- [popular-press](popular-press/README.md) — reporting on AI capabilities, interpretability, and adjacent themes.
- [philosophy_of_consciousness](philosophy_of_consciousness/README.md) — consciousness, subjective experience, and self-consciousness in humans and AI.
- [interpretability](interpretability/README.md) — steering, SAEs, LoRA/PEFT, model merging (HeRA bibliography).
- [interpretability-anthropic](interpretability-anthropic/README.md) — Anthropic Transformer Circuits thread and related posts.
- [attention](attention/README.md) — attention visualization, BERT geometry, toy-model QK/OV factorization, pedagogical and minimal-GPT resources.
- [j-space](j-space/README.md) — Jacobian lens, J-space / global workspace, J-Access, J-CoT, and related follow-ups.
- [readers](readers/README.md) — background synthesis readers (topic maps across papers; not per-paper notes).
- [publications](publications/README.md) — index of papers migrated from `literature-review-and-docs` / `chapman-alignment-faking` (theme folders above; not HeRA `interpretability/`).
- [authors](authors/README.md) — per-researcher corpora (Google Scholar ingest).
- [authors/rimkevicius](authors/rimkevicius/README.md) — Paulius Rimkevičius (Chapman; Google Scholar `JEEYxL4AAAAJ`): free will, volition, self-knowledge, cross-cultural cognition, AI agency.

## Papers (A–Z by last name)

Curated summaries (`{citationkey}.md`). Every entry in `bib.bib` with a curated note appears here; partial ingests (extract only) are listed below.

- [Aghajanyan et al. — *Intrinsic dimensionality explains the effectiveness of language model fine-tuning* (2021)](./interpretability/aghajanyan2021_intrinsic_dimensionality.md)
- [Alammar — *The Illustrated Transformer* (2018)](./attention/alammar2018_illustrated_transformer.md)
- [Ameisen et al. — *Circuit Tracing: Revealing Computational Graphs in Language Models* (2025)](./interpretability-anthropic/ameisen2025_circuit_tracing.md)
- [Apolinario et al. — *LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning* (2026)](./interpretability/apolinario2026lancelowrankactivation.md)
- [Belinkov et al. — *Analysis Methods in Neural Language Processing: A Survey* (2019)](./interpretability/belinkov2019_analysis_methods.md)
- [Braun et al. — *Understanding (Un)Reliability of Steering Vectors in Language Models* (2025)](./interpretability/braun2025understanding.md)
- [Bricken et al. — *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning* (2023)](./interpretability-anthropic/bricken2023towards.md)
- [Chatterjee — *Fluctuations of eigenvalues and second order Poincaré inequalities* (2009)](./interpretability/chatterjee2007fluctuationseigenvaluessecondorder.md)
- [Clymer et al. — *Poser: Unmasking alignment faking LLMs by manipulating their internals* (2024)](./alignment-faking/clymer2024poser.md)
- [Cunningham et al. — *Sparse Autoencoders Find Highly Interpretable Features in Language Models* (2023)](./interpretability/cunningham2023sparseautoencodershighlyinterpretable.md)
- [Coenen et al. — *Visualizing and measuring the geometry of BERT* (2019)](./attention/coenen2019_geometry_bert.md)
- [Dar et al. — *Analyzing transformers in embedding space* (2023)](./interpretability/dar2022_analyzing_transformers.md)
- [Diallo et al. — *The Effectiveness of Style Vectors for Steering Large Language Models: A Human Evaluation* (2025)](./interpretability/11224465.md)
- [Ding et al. — *Enhancing Chat Language Models by Scaling High-quality Instructional Conversations* (2023)](./interpretability/ding2023enhancingchatlanguagemodels.md)
- [Dunefsky et al. — *One-shot Optimized Steering Vectors Mediate Safety-relevant Behaviors in LLMs* (2025)](./interpretability/dunefsky2025oneshot.md)
- [Elhage et al. — *A mathematical framework for transformer circuits* (2021)](./interpretability-anthropic/elhage2021_transformer_circuits.md)
- [Elhage et al. — *Toy Models of Superposition* (2022)](./interpretability-anthropic/elhage2022_superposition.md)
- [Fang et al. — *Controllable LLM Reasoning via Sparse Autoencoder-Based Steering* (2026)](./interpretability/fang-etal-2026-controllable.md)
- [Fraser-Taliente et al. — *Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations* (2026)](./interpretability-anthropic/fraser2026_natural_language_autoencoders.md)
- [Frenkel et al. — *The escalating global A.I. arms race* (2026)](./popular-press/frenkel2026global_ai_arms.md)
- [Gemma Team — *Gemma 4 Technical Report* (2026)](./interpretability/gemmateam2026gemma4technicalreport.md)
- [Geva et al. — *Transformer feed-forward layers are key-value memories* (2021)](./interpretability/geva2021_key_value_memories.md)
- [Greenblatt et al. — *Alignment faking in large language models* (2024)](./alignment-faking/greenblatt2024alignment_faking.md)
- [Gurnee et al. — *When Models Manipulate Manifolds: The Geometry of a Counting Task* (2025)](./interpretability-anthropic/gurnee2025_manipulate_manifolds.md)
- [Gurnee et al. — *Verbalizable Representations Form a Global Workspace in Language Models* (2026)](./j-space/gurnee2026_global_workspace.md)
- [Hanna et al. — *How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model* (2023)](./interpretability/hanna2023_greater_than.md)
- [He et al. — *Deep residual learning for image recognition* (2016)](./interpretability/he2016_deep_residual.md)
- [He et al. — *DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing* (2023)](./interpretability/he2023debertav.md)
- [Henighan et al. — *Superposition, Memorization, and Double Descent* (2023)](./interpretability-anthropic/henighan2023_superposition_memorization.md)
- [Heyman et al. — *Steer Like the LLM: Activation Steering that Mimics Prompting* (2026)](./interpretability/heyman2026steer.md)
- [Ho et al. — *Language Models Can Control Their Own Attention* (2026)](./interpretability/ho2026declarative_attention.md)
- [Hörmander — *The Analysis of Linear Partial Differential Operators I* (2015)](./interpretability/hörmander2015analysis.md)
- [Hu et al. — *LoRA: Low-Rank Adaptation of Large Language Models* (2021)](./interpretability/hu2021loralowrankadaptation.md)
- [Hubinger et al. — *Sleeper agents: training deceptive LLMs that persist through safety training* (2024)](./sleeper-agents/hubinger2024sleeper_agents.md)
- [Ilharco et al. — *Editing Models with Task Arithmetic* (2023)](./interpretability/ilharco2023editingmodelstaskarithmetic.md)
- [Jiang et al. — *Mistral 7B* (2023)](./interpretability/jiang2023mistral7b.md)
- [Kamath et al. — *Tracing Attention Computation Through Feature Interactions* (2025)](./interpretability-anthropic/kamath2025_attention_feature_interactions.md)
- [Karpathy — *nanoGPT* (2022)](./attention/karpathy2022_nanogpt.md)
- [Kangaslahti et al. — *Continuous Language Model Interpolation for Dynamic and Controllable Text Generation* (2025)](./interpretability/kangaslahti2025continuous.md)
- [Kim et al. — *TCAV: Relative Concept Importance Testing with Linear Concept Activation Vectors* (2018)](./interpretability/kim2018tcav.md)
- [Kingma et al. — *Adam: A Method for Stochastic Optimization* (2017)](./interpretability/kingma2017adammethodstochasticoptimization.md)
- [Koike-Akino et al. — *Quantum-PEFT: Ultra Parameter-Efficient Fine-Tuning* (2025)](./interpretability/koike-akino2025quantumpeft.md)
- [Kong et al. — *Aligning Large Language Models with Representation Editing: A Control Perspective* (2024)](./interpretability/kong2024aligning.md)
- [Lange — *Does J-Space Cross the Standpoint Threshold?* (2026)](./j-space/lange2026_jspace_standpoint.md)
- [Leask et al. — *Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models* (2025)](./interpretability/leask2025inferencetimedecompositionactivationsitda.md)
- [Li et al. — *LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods* (2024)](./interpretability/li2024llmsasjudgescomprehensivesurveyllmbased.md)
- [Lindsey — *Emergent Introspective Awareness in Large Language Models* (2025)](./interpretability-anthropic/lindsey2025_introspective_awareness.md)
- [Lindsey et al. — *On the Biology of a Large Language Model* (2025)](./interpretability-anthropic/lindsey2025_biology_language_model.md)
- [MacDiarmid et al. — *Natural emergent misalignment from reward hacking in production RL* (2025)](./alignment-faking/macdiarmid2025emergent_misalignment.md)
- [Ma et al. — *Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures* (2026)](./j-space/ma2026_hidden_apis.md)
- [Martens — *Deep learning via Hessian-free optimization* (2010)](./interpretability/martens2010_hessian_free.md)
- [Meng et al. — *Locating and Editing Factual Associations in GPT* (2022)](./interpretability/meng2022_rome.md)
- [Menon et al. — *Analyzing (In)Abilities of SAEs via Formal Languages* (2025)](./interpretability/menon-etal-2025-analyzing.md)
- [Metzinger — *The Ego Tunnel: The Science of the Mind and the Myth of the Self* (2009)](./philosophy_of_consciousness/metzinger2009_ego_tunnel.md)
- [Mikolov et al. — *Distributed Representations of Words and Phrases and their Compositionality* (2013)](./interpretability/mikolov2013_word2vec.md)
- [Moré — *The Levenberg–Marquardt algorithm: Implementation and theory* (1978)](./interpretability/levenbergmarquardt.md)
- [Nelwan et al. — *Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models* (2026)](./interpretability/nelwan2026deployableperinstancemultilayeractivation.md)
- [Olsson et al. — *In-context Learning and Induction Heads* (2022)](./interpretability-anthropic/olsson2022_induction_heads.md)
- [Oozeer et al. — *Beyond Linear Steering: Unified Multi-Attribute Control for Language Models* (2026)](./interpretability/oozeer2026linearsteeringunifiedmultiattribute.md)
- [Oskin — *Off-Axis, On Purpose: Where a Transformer Computes Concepts and Why it Does So* (2026)](./j-space/oskin2026_off_axis.md)
- [Pacchiardi et al. — *How to catch an AI liar: lie detection in black-box LLMs by asking unrelated questions* (2023)](./lie-detection/pacchiardi2023catch_a_liar.md)
- [Panickssery et al. — *Steering Llama 2 via Contrastive Activation Addition* (2024)](./interpretability/panickssery2024steeringllama2contrastive.md)
- [Pearlmutter — *Fast exact multiplication by the Hessian* (1994)](./interpretability/pearlmutter1994_fast_hessian.md)
- [Pham et al. — *Householder Pseudo-Rotation: A Novel Approach to Activation Editing in LLMs with Direction-Magnitude Perspective* (2024)](./interpretability/pham-nguyen-2024-householder.md)
- [Prabhakar et al. — *LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks* (2024)](./interpretability/prabhakar2024lorasoupsmergingloras.md)
- [Qwen Team — *Qwen2.5-VL Technical Report* (2025)](./interpretability/bai2025qwen25vltechnicalreport.md)
- [Ramsay et al. — *Functional Data Analysis* (2005)](./interpretability/ramsay2005functional.md)
- [Rodríguez et al. — *Controlling Language and Diffusion Models by Transporting Activations* (2024)](./interpretability/rodriguez2024controllinglanguagediffusionmodels.md)
- [Rumelhart et al. — *Learning representations by back-propagating errors* (1986)](./interpretability/rumelhart1986_backprop.md)
- [Scalena et al. — *Multi-property Steering of Large Language Models with Dynamic Activation Composition* (2024)](./interpretability/Scalena_2024.md)
- [Scoles — *You have no choice in reading this article—maybe* (2026)](./popular-press/scoles2026free_will_maoz.md)
- [Seth — *Being You: A New Science of Consciousness* (2021)](./philosophy_of_consciousness/seth2021_being_you.md)
- [Shafiq & Gu — *Deep Residual Learning for Image Recognition: A Survey* (2022)](./interpretability/shafiq2022deep_residual_survey.md)
- [Sharkey et al. — *Open Problems in Mechanistic Interpretability* (2025)](./interpretability/sharkey2025openproblemsmechanisticinterpretability.md)
- [Sharma et al. — *COLD-Steer: Steering Large Language Models via In-Context One-Step Learning Dynamics* (2026)](./interpretability/sharma2026coldsteer.md)
- [Shu et al. — *A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models* (2025)](./interpretability/shu2025surveysparseautoencodersinterpreting.md)
- [Singh et al. — *Representation Surgery: Theory and Practice of Affine Steering* (2024)](./interpretability/pmlr-v235-singh24d.md)
- [Sofroniew et al. — *Emotion Concepts and their Function in a Large Language Model* (2026)](./interpretability-anthropic/sofroniew2026_emotion_concepts.md)
- [Song et al. — *Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning* (2026)](./j-space/song2026_j_access.md)
- [Soo et al. — *Interpretable Steering of Large Language Models with Feature Guided Activation Additions* (2025)](./interpretability/soo2025interpretable.md)
- [Stoica et al. — *Model Merging with SVD to Tie the Knots* (2024)](./interpretability/stoica2024modelmergingsvdtie.md)
- [Subramani et al. — *Extracting Latent Steering Vectors from Pretrained Language Models* (2022)](./interpretability/subramani2022_extracting_steering_vectors.md)
- [Sun et al. — *LayerNavigator: Finding Promising Intervention Layers for Efficient Activation Steering in Large Language Models* (2025)](./interpretability/sun2025layernavigator.md)
- [Tan et al. — *Analysing the Generalisation and Reliability of Steering Vectors* (2024)](./interpretability/tan2024analysing.md)
- [Templeton et al. — *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet* (2024)](./interpretability-anthropic/templeton2024_scaling_monosemanticity.md)
- [Tenney et al. — *BERT Rediscovers the Classical NLP Pipeline* (2019)](./interpretability/tenney2019_bert_pipeline.md)
- [Tenney et al. — *What do you learn from context? Probing for sentence structure in contextualized word representations* (2019)](./interpretability/tenney2019_edge_probing.md)
- [Titov et al. — *J-Space in Claude: Three Unanswered Questions and an Architectural Solution via Reentry* (2026)](./j-space/titov2026_jspace_reentry.md)
- [Turner et al. — *Steering Language Models With Activation Engineering* (2024)](./interpretability/turner2024steeringlanguagemodelsactivation.md)
- [van der Weij et al. — *Extending Activation Steering to Broad Skills and Multiple Behaviours* (2024)](./interpretability/vanderweij2024extendingactivationsteeringbroad.md)
- [Vaswani et al. — *Attention is all you need* (2017)](./interpretability/vaswani2017_attention.md)
- [Vig — *A multiscale visualization of attention in the Transformer model* (2019)](./attention/vig2019_multiscale_attention.md)
- [Wang et al. — *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small* (2022)](./interpretability/wang2022_ioi.md)
- [Wang — *Self-awareness, a singularity of AI* (2023)](./philosophy_of_consciousness/wang2023_singularity.md)
- [Wang & Reid — *Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?* (2026)](./j-space/wang2026_looped_jacobian.md)
- [Whang — *We don't really know how A.I. works. That's a problem* (2026)](./popular-press/whang2026ai_black_box.md)
- [Wortsman et al. — *Learning Neural Network Subspaces* (2021)](./interpretability/wortsman2021_neural_subspaces.md)
- [Wu et al. — *J-CoT: Chain-of-Thought in J-Space* (2026)](./j-space/wu2026_j_cot.md)
- [Xu et al. — *Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics* (2026)](./interpretability/xu-etal-2026-steering.md)
- [Yadav et al. — *TIES-Merging: Resolving Interference When Merging Models* (2023)](./interpretability/yadav2023tiesmerging.md)
- [Yu et al. — *Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch* (2024)](./interpretability/yu2024language.md)
- [Zhao et al. — *ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment* (2026)](./interpretability/zhao2026odesteer.md)
- [Zou et al. — *Representation Engineering: A Top-Down Approach to AI Transparency* (2023)](./interpretability/zou2023representationengineeringtopdownapproach.md)

### Partial / no notes yet

`bib.bib` entries with local `.txt` extracts only (no curated `{citationkey}.md` yet):

- [`koorndijk2025alignment_faking_small_llm`](alignment-faking/) — extract in `alignment-faking/`
- [`taylor2025school_reward_hacks`](alignment-faking/) — extract in `alignment-faking/`
- [`sheshadri2026auditbench`](alignment-auditing/) — extract in `alignment-auditing/`
- [`mcintosh2024rlhf_semantic_vulnerabilities`](semantic-vulnerabilities/) — extract in `semantic-vulnerabilities/`
