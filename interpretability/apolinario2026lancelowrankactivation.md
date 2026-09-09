# LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning

**Authors:** Marco P. Apolinario, Kaushik Roy  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `apolinario2026lancelowrankactivation`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2509.21617)  
**arXiv:** 2509.21617  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=LANCE+Low+Rank+Activation+Compression+On-Device+Continual+Learning)

## Summary

Proposes LANCE, a low-rank activation compression framework for on-device fine-tuning and continual learning. A one-shot higher-order SVD produces a reusable low-rank subspace for activation projection, removing repeated decompositions and cutting memory/compute costs. Fixed subspaces also support continual learning by assigning tasks to orthogonal subspaces without storing large task-specific matrices. On image benchmarks and continual learning suites, LANCE reduces activation storage up to 250× while maintaining accuracy comparable to full backpropagation.

## Key concepts

- **Low-rank activation compression** — one-shot higher-order SVD for a reusable projection subspace.  
- **On-device continual learning** — task-specific orthogonal subspaces avoid large task-specific matrices.  
- **Activation memory** — reduction up to 250× with comparable accuracy.  
- **Catastrophic forgetting mitigation** — via orthogonal subspace allocation.
