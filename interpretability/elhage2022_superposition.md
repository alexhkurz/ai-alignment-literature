# Toy Models of Superposition

**Authors:** Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, Christopher Olah  
**Year:** 2022  
**Venue:** Transformer Circuits Thread / arXiv  
**Citation key:** `elhage2022_superposition`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2209.10652.pdf)  
**arXiv:** 2209.10652  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Elhage+Toy+Models+Superposition+2022)

## Summary

Uses **toy sparse-feature models** to explain **superposition** — networks represent more features than dimensions by encoding them as nearly orthogonal directions, with interference tradeoffs. Clarifies why linear probes and sparse autoencoders matter for interpretability.

## Key concepts

- **Superposition** — $m$ features in $n \ll m$ dimensions.  
- **Feature geometry** — interference vs sparsity.  
- **Implications for monosemanticity** — why single neurons are often polysemantic.

## Notes

- Theoretical backbone for why “one direction = one concept” is approximate, not guaranteed.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
