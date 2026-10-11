# Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models

**Authors:** Muhammad Faishal Adly Nelwan, Alfan Farizki Wicaksono  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `nelwan2026deployableperinstancemultilayeractivation`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2608.08829)  
**arXiv:** 2608.08829  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Deployable+Per-Instance+Multi-Layer+Activation+Steering)

## Summary

Argues that the best layers for activation steering are an instance-level decision, not a global fixed set. The authors propose a deployable recipe with three components: a per-instance layer ranker derived from the prompt embedding, a classifier that infers the steering direction, and an adaptive gate that scores short steered passes and stops when further steering no longer helps. On two 8B open-weight models and six binary persona traits, this per-instance, multi-layer approach recovers most of an oracle's per-instance benefit while avoiding the fluency collapse that strong global multi-layer selection can cause.

## Key concepts

- **Per-instance layer selection** — choose which layers to steer for each input.  
- **Multi-layer activation steering** — steer more than one layer when it helps, but only when it helps.  
- **Adaptive gating** — stop steering once the output is no longer improving.  
- **Deployability at inference** — no gold answer required at test time; all components run from the prompt.
