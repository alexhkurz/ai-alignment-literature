# LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks

**Authors:** Akshara Prabhakar, Yuanzhi Li, Karthik Narasimhan, Sham Kakade, Eran Malach, Samy Jelassi  
**Year:** 2024  
**Venue:** arXiv preprint  
**Citation key:** `prabhakar2024lorasoupsmergingloras`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2410.13025)  
**arXiv:** 2410.13025  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=LoRA+Soups+Merging+LoRAs+Skill+Composition)

## Summary

Studies how independently trained LoRA modules can be merged to solve a target task that requires combining their skills. The authors identify practical use cases such as math-word problems with code and domain-specific QA, then propose CAT (Concatenation of LoRAs), an optimal weighting scheme that outperforms both data-merging and existing model-merging methods. On compositional tasks, CAT improves by up to 43% over data merging and 12% over alternative model merging.

## Key concepts

- **LoRA merging** — combine fine-tuned low-rank adapters into one model.  
- **Skill composition** — target task needs capabilities from multiple specialized LoRAs.  
- **CAT (Concatenation of LoRAs)** — optimal linear weighting of LoRA modules.  
- **Compute-efficient multi-task models** — no re-training of the full model.
