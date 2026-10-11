# Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models

**Authors:** Patrick Leask, Neel Nanda, Noura Al Moubayed  
**Year:** 2025  
**Venue:** arXiv preprint  
**Citation key:** `leask2025inferencetimedecompositionactivationsitda`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2505.17769)  
**arXiv:** 2505.17769  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Inference-Time+Decomposition+Activations+ITDA)

## Summary

Proposes ITDA as a lightweight alternative to training sparse autoencoders (SAEs) for decomposing LLM activations. ITDAs build dictionaries greedily via matching pursuit, selecting a small set of activating examples based on a reconstruction error threshold. They can be trained in about 1% of the time of SAEs and scaled to Llama-3.1 70B/405B. The resulting dictionaries enable cross-model representation comparison and outperform CKA, SVCCA, and other relative-representation baselines.

## Key concepts

- **ITDA** — inference-time activation decomposition using matching-pursuit over a small dictionary.  
- **Scalability** — 1% of SAE training time, works on 70B/405B models.  
- **Cross-model comparison** — dictionaries let different models be compared in a shared feature space.  
- **Relative representation similarity** — alternative to CKA / SVCCA for comparing LLM internals.
