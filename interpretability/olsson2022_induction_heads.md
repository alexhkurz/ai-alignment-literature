# In-context Learning and Induction Heads

**Authors:** Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah  
**Year:** 2022  
**Venue:** Transformer Circuits Thread / arXiv  
**Citation key:** `olsson2022_induction_heads`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2209.11895.pdf)  
**arXiv:** 2209.11895  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Olsson+In+Context+Learning+Induction+Heads+2022)

## Summary

Identifies **induction heads** — attention heads that implement in-context copying / pattern completion — and argues they are central to **in-context learning** emergence during training. Combines mechanistic analysis with scaling and training dynamics.

## Key concepts

- **Induction head** — attends to previous token occurrences to predict repeats.  
- **In-context learning (ICL)** — few-shot behavior without weight updates.  
- **Phase change** — induction heads appear during training.

## Notes

- Key mechanistic motif linking attention circuits to ICL; background for activation patching discussions.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
