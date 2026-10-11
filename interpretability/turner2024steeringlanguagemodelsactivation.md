# Steering Language Models With Activation Engineering

**Authors:** Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J. Vazquez, Ulisse Mini, Monte MacDiarmid  
**Year:** 2024  
**Venue:** arXiv preprint  
**Citation key:** `turner2024steeringlanguagemodelsactivation`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2308.10248)  
**arXiv:** 2308.10248  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Steering+Language+Models+Activation+Engineering+Turner)

## Summary

Introduces *activation engineering*: inference-time edits to internal activations to steer model outputs without weight updates. Presents **Activation Addition (ActAdd)**—contrast activations on prompt pairs (e.g. “Love” vs “Hate”) to form a steering vector added during the forward pass. Reports strong results on sentiment shift and detoxification while largely preserving off-target task performance; lightweight (no optimization, single contrast pair).

## Key concepts

- **Activation Addition (ActAdd)** — pairwise contrast steering vectors.  
- **Activation engineering** — control via residual-stream interventions.  
- **Inference-time steering** — no fine-tuning required.

## Notes

Core activation-steering baseline for HeRA; related to representation engineering and contrastive activation addition literature.
