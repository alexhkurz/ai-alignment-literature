# nanoGPT

**Authors:** Andrej Karpathy  
**Year:** 2022  
**Venue:** Open-source code repository (not a paper)  
**Citation key:** `karpathy2022_nanogpt`  
**BibTeX entry:** [entry](../../bib.bib#L1195)  
**Repository:** [github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=nanoGPT+Karpathy)

## Summary

Minimal **~300-line GPT training stack** (PyTorch): `model.py` defines causal self-attention, multi-head blocks, and MLP; `train.py` / `sample.py` handle data loading, optimization, and generation. Designed as the simplest readable reference for **instrumenting attention and activations yourself** — hook `CausalSelfAttention`, dump Q/K/V tensors, log attention maps, or swap in analysis code without HuggingFace abstractions.

Supports pretraining and fine-tuning on character-level (Shakespeare) and BPE tokenized corpora; widely forked for teaching and mechanistic experiments.

## Key concepts

- **CausalSelfAttention** — fused QKV projection, scaled softmax attention, output projection.  
- **GPT block** — attention + MLP with residuals (LayerNorm variants in repo history).  
- **Inspectable training loop** — single-process, explicit tensors, easy breakpoints.  
- **Baseline for circuits work** — small models you can train and fully trace.

## Notes

- Code resource, not a PDF paper; cite the repository URL.  
- For visualization after instrumentation, use [`vig2019_multiscale_attention`](vig2019_multiscale_attention.md) (BertViz on HF models) or custom hooks in nanoGPT.  
- Conceptual prerequisite: [`alammar2018_illustrated_transformer`](alammar2018_illustrated_transformer.md). Formal factorization: [`elhage2021_transformer_circuits`](../interpretability-anthropic/elhage2021_transformer_circuits.md).
