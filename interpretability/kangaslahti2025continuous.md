# Continuous Language Model Interpolation for Dynamic and Controllable Text Generation

**Authors:** Sara Kangaslahti, David Alvarez-Melis  
**Year:** 2025  
**Venue:** Transactions on Machine Learning Research  
**Citation key:** `kangaslahti2025continuous`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2404.07117)  
**arXiv:** 2404.07117  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Continuous+Language+Model+Interpolation+Dynamic+Controllable+Text+Generation)

## Summary

Studies parameter-space interpolation between language models as a way to build dynamic, controllable generators. Rather than producing a single merged model, the authors formulate *continuous model interpolation* over the trajectory between two model checkpoints, allowing a user to sample from any point along the interpolation path at inference time. The method supports smooth control over style, domain, and safety properties without task-specific fine-tuning or expensive decoding-time steering.

## Key concepts

- **Continuous model interpolation** — generate from any point along a parameter-space path.  
- **Controllable text generation** — trade off style, domain, or safety by choosing the interpolation point.  
- **No task-specific training** — control comes from the pre-trained trajectory, not new data.  
- **Dynamic inference-time selection** — pick the interpolation coefficient per sample.
