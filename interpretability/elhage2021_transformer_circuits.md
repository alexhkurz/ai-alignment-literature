# A mathematical framework for transformer circuits

**Authors:** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah  
**Year:** 2021  
**Venue:** Transformer Circuits Thread (not peer-reviewed as a journal paper)  
**Citation key:** `elhage2021_transformer_circuits`  
**BibTeX entry:** [entry](../../bib.bib#L633)  
**PDF:** [thread](https://transformer-circuits.pub/2021/framework/index.html)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Mathematical+Framework+Transformer+Circuits+Elhage)

## Summary

Anthropic’s **transformer circuits** framework gives a mechanistic vocabulary for small transformers: the **residual stream** as a shared workspace, **Q/K/V** attention as bilinear routing plus value aggregation, and **MLP** layers as key–value memories writing to the stream. The essay connects attention heads and MLP neurons to interpretable **circuits** (e.g. induction heads) and distinguishes **residual dimensions** from classical “neurons.” It is the interpretability backbone cited throughout the HeRA transformer reader.

## Key concepts

- **Residual stream** — additive communication channel across layers.  
- **Attention head** — reads/writes via Q/K/V projections.  
- **Circuits** — compositional subcomputations built from heads and MLPs.  
- **Induction heads** — exemplar mechanistic motif.

## Notes

- Web article (HTML), not arXiv; no `ensure-extract.sh` PDF pipeline by default.  
- HeRA reader: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md).
