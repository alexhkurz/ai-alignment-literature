# AI alignment literature

Canonical paper summaries, text extracts, and `bib.bib` for the AI alignment / alignment-faking research cluster. Consumer repos (Chapman alignment faking, planning docs, …) use this repository as a sister checkout (same parent directory) — see [SETUP.md](SETUP.md) and each consumer’s `LITERATURE.md`.

**Setup:** [SETUP.md](SETUP.md) · **Ingestion rules:** `.cursor/rules/bibliography.mdc`

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

Curated summaries (`{citationkey}-notes.md` when present; otherwise partial extract only).

- [Clymer, Juang & Field — *Poser: Unmasking alignment faking LLMs…* (2024)](alignment-faking/clymer2024poser-notes.md)
- [Frenkel, Mozur & Satariano — *The escalating global A.I. arms race* (2026)](popular-press/frenkel2026global_ai_arms-notes.md)
- [Greenblatt et al. — *Alignment faking in large language models* (2024)](alignment-faking/greenblatt2024alignment_faking-notes.md)
- [Hubinger et al. — *Sleeper agents…* (2024)](sleeper-agents/hubinger2024sleeper_agents-notes.md)
- [MacDiarmid et al. — *Natural emergent misalignment from reward hacking…* (2025)](alignment-faking/macdiarmid2025emergent_misalignment-notes.md)
- [Metzinger — *The Ego Tunnel* (2009)](philosophy_of_consciousness/metzinger2009_ego_tunnel-notes.md)
- [Pacchiardi et al. — *How to catch an AI liar…* (2023)](lie-detection/pacchiardi2023catch_a_liar-notes.md)
- [Scoles — *You have no choice in reading this article—maybe* (2026)](popular-press/scoles2026free_will_maoz-notes.md)
- [Seth — *Being You* (2021)](philosophy_of_consciousness/seth2021_being_you-notes.md)
- [Wang — *Self-awareness, a singularity of AI* (2023)](philosophy_of_consciousness/wang2023_singularity-notes.md)
- [Whang — *We don't really know how A.I. works…* (2026)](popular-press/whang2026ai_black_box-notes.md)

### Partial / no notes yet

- `koorndijk2025alignment_faking_small_llm` — extract in `alignment-faking/`
- `taylor2025school_reward_hacks` — extract in `alignment-faking/`
- `sheshadri2026auditbench` — extract in `alignment-auditing/`
- `mcintosh2024rlhf_semantic_vulnerabilities` — extract in `semantic-vulnerabilities/`
- HeRA bibliography (~40 extracts) — see [interpretability/README.md](interpretability/README.md)
