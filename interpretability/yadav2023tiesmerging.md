# TIES-Merging: Resolving Interference When Merging Models

**Authors:** Prateek Yadav, Derek Tam, Leshem Choshen, Colin Raffel, Mohit Bansal  
**Year:** 2023  
**Venue:** NeurIPS 2023  
**Citation key:** `yadav2023tiesmerging`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2306.01708)  
**arXiv:** 2306.01708  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=TIES-Merging+Resolving+Interference+Merging+Models)

## Summary

Addresses interference when merging task-specific fine-tuned models into one multi-task model without extra training. **TIES-Merging** (Trim, Elect Sign, Merge) resets small-magnitude delta parameters, resolves sign conflicts across models, and merges the surviving task vectors—reducing destructive interference vs. naive averaging.

## Key concepts

- **Model merging** — combine fine-tuned checkpoints.  
- **Parameter interference** — redundant deltas and sign disagreement.  
- **Trim–Elect–Sign–Merge** — three-step merge pipeline.

## Notes

HeRD-Merging comparison baseline for weight-space merging.
