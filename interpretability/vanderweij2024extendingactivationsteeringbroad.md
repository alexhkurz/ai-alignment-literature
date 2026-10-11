# Extending Activation Steering to Broad Skills and Multiple Behaviours

**Authors:** Teun van der Weij, Massimo Poesio, Nandi Schoots  
**Year:** 2024  
**Venue:** arXiv preprint (cs.LG)  
**Citation key:** `vanderweij2024extendingactivationsteeringbroad`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2403.05767)  
**arXiv:** 2403.05767  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Extending+Activation+Steering+Broad+Skills+Multiple+Behaviours)

## Summary

Tests whether activation addition (ActAdd / CAA-style) scales from narrow single behaviours to broad skills and to several behaviours at once, on Llama 2 7B Chat, while tracking alignment tax. Steering a broad skill (general coding) is competitive with steering a narrower skill (Python). For multiple behaviours (e.g. myopia, wealth-seeking), summing several steering vectors into one combined vector is largely unsuccessful; injecting separate vectors at different layers simultaneously is more promising. Individual behaviour vectors remain effective, consistent with prior work, but naive multi-vector composition does not transfer cleanly.

## Key concepts

- **Broad-skill steering** — one vector for a wide capability (coding) vs a narrow subskill (Python).  
- **Combined multi-steering** — adding behaviour vectors into a single intervention (mostly fails here).  
- **Simultaneous multi-layer injection** — apply distinct vectors at different layers (more promising).  
- **Alignment tax** — tracking collateral damage to general performance under stronger / broader interventions.
