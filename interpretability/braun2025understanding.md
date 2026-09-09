# Understanding (Un)Reliability of Steering Vectors in Language Models

**Authors:** Joschka Braun, Carsten Eickhoff, David Krueger, Seyed Ali Bahrainian, Dmitrii Krasheninnikov  
**Year:** 2025  
**Venue:** ICLR 2025 Workshop on Foundation Models in the Wild  
**Citation key:** `braun2025understanding`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2505.22637)  
**arXiv:** 2505.22637  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Understanding+Unreliability+Steering+Vectors+Language+Models+Braun)

## Summary

Investigates why steering vectors sometimes work, fail, or backfire. Across seven prompt types, all produce a net positive steering effect but with high sample-level variance, and no single prompt type dominates. Reliability is higher when the training activation-difference vectors are more cosinely similar and when positive/negative examples are better separated. The central takeaway: steering is unreliable when the target behavior is not represented by a coherent direction in activation space.

## Key concepts

- **Steering reliability** — mean effect can be positive while individual samples often backfire.  
- **Activation-difference geometry** — cosine similarity of training vectors predicts transfer success.  
- **Prompt type variance** — different prompts yield vectors that point in different directions.  
- **Coherent behavioral directions** — steering works best when a behavior is a single linear direction.
