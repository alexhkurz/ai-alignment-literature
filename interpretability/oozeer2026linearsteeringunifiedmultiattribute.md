# Beyond Linear Steering: Unified Multi-Attribute Control for Language Models

**Authors:** Narmeen Oozeer, Luke Marks, Shreyans Jain, Fazl Barez, Amirali Abdullah  
**Year:** 2026  
**Venue:** arXiv preprint (cs.LG)  
**Citation key:** `oozeer2026linearsteeringunifiedmultiattribute`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2505.24535)  
**arXiv:** 2505.24535  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Beyond+Linear+Steering+Unified+Multi-Attribute+Control+Oozeer)

## Summary

Argues that multi-attribute activation control is poorly served by additive linear steering: composing per-attribute vectors causes interference, and each vector needs its own hyperparameter sweep. K-Steering trains one non-linear multi-label classifier on hidden activations and, at inference, uses classifier gradients to obtain intervention directions for any chosen subset of attributes—without storing separate vectors or assuming linearity. Evaluated on two new compositional benchmarks (ToneBank, DebateMix) across three model families, with both activation classifiers and LLM judges; a single-step, single-layer variant already outperforms strong linear multi-steering baselines. Multi-step / multi-layer variants can help further but cost more compute.

## Key concepts

- **K-Steering** — unified gradient-based multi-attribute steering from one multi-label activation classifier.  
- **Beyond linear additivity** — avoids composing independent steering vectors.  
- **Dynamic composition** — choose target attribute subsets at inference without retraining.  
- **ToneBank / DebateMix** — benchmarks built for compositional behavioral control.
