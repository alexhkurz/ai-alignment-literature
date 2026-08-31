# Locating and Editing Factual Associations in GPT

**Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov  
**Year:** 2022  
**Venue:** NeurIPS 2022  
**Citation key:** `meng2022_rome`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2202.05262.pdf)  
**arXiv:** 2202.05262  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Meng+Locating+Editing+Factual+Associations+GPT+ROME+2022)

## Summary

**ROME** (Rank-One Model Editing) locates factual associations (e.g. “Eiffel Tower is in Paris”) at specific MLP layers and edits them with a **rank-one weight update** while preserving unrelated behavior — causal evidence that facts live in interpretable weight–activation structure.

## Key concepts

- **Causal tracing / activation patching** — identify components mediating a fact.  
- **Rank-one edit** — minimal weight change for targeted knowledge update.  
- **Factual recall** — MLP key–value memory view.

## Notes

- Exemplar of **causal** mechanistic interpretability (not just probing).  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
