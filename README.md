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

Curated summaries (`{citationkey}.md` or `{citationkey}.md`).

- [Apolinario & Roy — *LANCE: Low-rank activation compression for on-device continual learning* (2026)](interpretability/apolinario2026lancelowrankactivation.md)
- [Bai (Qwen Team) — *Qwen2.5-VL technical report* (2025)](interpretability/bai2025qwen25vltechnicalreport.md)
- [Braun et al. — *Understanding (un)reliability of steering vectors in language models* (2025)](interpretability/braun2025understanding.md)
- [Clymer, Juang & Field — *Poser: Unmasking alignment faking LLMs…* (2024)](alignment-faking/clymer2024poser.md)
- [Cunningham et al. — *Sparse autoencoders find highly interpretable features in language models* (2023)](interpretability/cunningham2023sparseautoencodershighlyinterpretable.md)
- [Ding et al. — *Enhancing chat language models by scaling high-quality instructional conversations* (2023)](interpretability/ding2023enhancingchatlanguagemodels.md)
- [Dunefsky & Cohan — *One-shot optimized steering vectors mediate safety-relevant behaviors in LLMs* (2025)](interpretability/dunefsky2025oneshot.md)
- [Fang et al. — *Controllable LLM reasoning via sparse autoencoder-based steering* (2026)](interpretability/fang-etal-2026-controllable.md)
- [Frenkel, Mozur & Satariano — *The escalating global A.I. arms race* (2026)](popular-press/frenkel2026global_ai_arms.md)
- [Gemma Team — *Gemma 4 technical report* (2026)](interpretability/gemmateam2026gemma4technicalreport.md)
- [Greenblatt et al. — *Alignment faking in large language models* (2024)](alignment-faking/greenblatt2024alignment_faking.md)
- [He, Gao & Chen — *DeBERTaV3…* (2023)](interpretability/he2023debertav.md)
- [Heyman & Vandeputte — *Steer like the LLM: activation steering that mimics prompting* (2026)](interpretability/heyman2026steer.md)
- [Ho et al. — *Language models can control their own attention* (2026)](interpretability/ho2026declarative_attention.md)
- [Hubinger et al. — *Sleeper agents…* (2024)](sleeper-agents/hubinger2024sleeper_agents.md)
- [MacDiarmid et al. — *Natural emergent misalignment from reward hacking…* (2025)](alignment-faking/macdiarmid2025emergent_misalignment.md)
- [Metzinger — *The Ego Tunnel* (2009)](philosophy_of_consciousness/metzinger2009_ego_tunnel.md)
- [Pacchiardi et al. — *How to catch an AI liar…* (2023)](lie-detection/pacchiardi2023catch_a_liar.md)
- [Scoles — *You have no choice in reading this article—maybe* (2026)](popular-press/scoles2026free_will_maoz.md)
- [Seth — *Being You* (2021)](philosophy_of_consciousness/seth2021_being_you.md)
- [Wang — *Self-awareness, a singularity of AI* (2023)](philosophy_of_consciousness/wang2023_singularity.md)
- [Whang — *We don't really know how A.I. works…* (2026)](popular-press/whang2026ai_black_box.md)

### Partial / no notes yet

### Partial / no notes yet

- `koorndijk2025alignment_faking_small_llm` — extract in `alignment-faking/`
- `taylor2025school_reward_hacks` — extract in `alignment-faking/`
- `sheshadri2026auditbench` — extract in `alignment-auditing/`
- `mcintosh2024rlhf_semantic_vulnerabilities` — extract in `semantic-vulnerabilities/`
- HeRA bibliography (~40 extracts) — see [interpretability/README.md](interpretability/README.md)
