# Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small

**Authors:** Kevin Wang, Alexandre Variengien, Arthur Conmy, Buck Shlegeris, Jacob Steinhardt  
**Year:** 2022  
**Venue:** arXiv preprint (Redwood Research)  
**Citation key:** `wang2022_ioi`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2211.00593.pdf)  
**arXiv:** 2211.00593  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Wang+Interpretability+Wild+Circuit+IOI+GPT2+2022)

## Summary

Reverse-engineers an end-to-end **circuit** (~26 attention heads in 7 classes) in GPT-2 small for **indirect object identification** (IOI), using path patching, activation patching, and embedding projections. One of the largest “in the wild” mechanistic case studies at the time.

## Key concepts

- **IOI task** — predict the correct indirect object name in a template sentence.  
- **Path patching** — causal intervention tracing information flow.  
- **Circuit faithfulness** — quantitative criteria (faithfulness, completeness, minimality).

## Notes

- Landmark “full circuit” paper in mechanistic interpretability; cited in the activation-steering reader as “Wang et al.”  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
