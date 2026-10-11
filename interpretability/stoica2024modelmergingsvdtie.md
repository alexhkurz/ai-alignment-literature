# Model Merging with SVD to Tie the Knots

**Authors:** George Stoica, Pratik Ramesh, Boglarka Ecsedi, Leshem Choshen, Judy Hoffman  
**Year:** 2024  
**Venue:** arXiv preprint  
**Citation key:** `stoica2024modelmergingsvdtie`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2410.19735)  
**arXiv:** 2410.19735  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Model+Merging+SVD+Tie+Knots+Stoica)

## Summary

Studies why existing model-merging methods work for fully fine-tuned models but not as well for LoRA fine-tuned models. The authors observe that LoRA-adapted weights are less aligned across tasks and propose KnOTS, which uses SVD to jointly transform the weights of different LoRA modules into a shared aligned space before applying existing merging methods. KnOTS improves LoRA merging by up to 4.3% across vision and language benchmarks and is accompanied by a new benchmark for evaluating whether merged models remain generalists.

## Key concepts

- **KnOTS** — SVD-based alignment for LoRA model merging.  
- **LoRA merging** — combining task-specific low-rank adapters.  
- **Weight-space alignment** — rotate parameters into a shared basis before merging.  
- **Generalist vs. specialist benchmark** — evaluate whether merges preserve breadth.
