# How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model

**Authors:** Michael Hanna, Ollie Liu, Alexandre Variengien  
**Year:** 2023  
**Venue:** NeurIPS 2023 Workshop (Mechanistic Interpretability) / arXiv  
**Citation key:** `hanna2023_greater_than`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2305.00586.pdf)  
**arXiv:** 2305.00586  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Hanna+GPT2+Compute+Greater+Than+2023)

## Summary

Mechanistically analyzes how GPT-2 small implements **greater-than** comparisons on numeric tokens: identifies a small set of attention and MLP components, validates with ablations and **activation patching**, and shows a human-interpretable algorithm (extract digits, compare, route).

## Key concepts

- **Algorithm recovery** — from behavior to circuit-level steps.  
- **Activation patching** — swap activations between clean/corrupt runs.  
- **Numeric reasoning** — interpretability beyond linguistic templates.

## Notes

- Representative “circuit for a crisp algorithm” paper alongside IOI.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
