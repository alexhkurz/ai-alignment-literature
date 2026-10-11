# J-CoT: Chain-of-Thought in J-Space

**Authors:** Junde Wu, Jiayuan Zhu, Fengling Liu, Minhao Hu, Jiazhen Pan  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `wu2026_j_cot`  
**BibTeX entry:** [entry](../bib.bib#L1271)  
**PDF:** [arXiv](https://arxiv.org/pdf/2607.21981)  
**arXiv:** [2607.21981](https://arxiv.org/abs/2607.21981)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=J-CoT+Chain-of-Thought+in+J-Space+Wu)

## Summary

Proposes J-CoT, a recurrent reasoning interface that uses J-space (vocabulary-indexed coordinates in hidden representations) instead of either fluent natural-language CoT or dense full-hidden-state recurrence. Within each cycle the model computes in its full hidden space; at the cycle boundary it expresses the intermediate state as vocabulary-indexed coefficients (a J-thought), carries those forward, and maps them back into hidden space for the next cycle. Under matched backbone and inference settings, J-CoT-Zero matches or beats strong latent-reasoning baselines; J-CoT-Train leads on the reported math, science, coding, and structured path-reasoning evaluations.

## Key concepts

- J-thought: vocabulary-indexed intermediate state
- Intermediate recurrent interface between text CoT and dense latent recurrence
- J-CoT-Zero vs J-CoT-Train
- Cycle-boundary projection into / out of J-space

## Notes

Method paper that treats J-space as a practical recurrent substrate for reasoning, building on the Jacobian-lens coordinate system of [`gurnee2026_global_workspace`](gurnee2026_global_workspace.md).
