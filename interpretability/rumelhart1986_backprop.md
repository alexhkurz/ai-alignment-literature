# Learning representations by back-propagating errors

**Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams  
**Year:** 1986  
**Venue:** Nature (peer-reviewed)  
**Citation key:** `rumelhart1986_backprop`  
**BibTeX entry:** [entry](../../bib.bib#L663)  
**PDF:** [Nature](https://doi.org/10.1038/323533a0)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Learning+representations+by+back-propagating+errors+Rumelhart)

## Summary

This short Nature paper popularised **error backpropagation** for training multi-layer networks: the output error is propagated backward through the network so each weight receives a signal proportional to its contribution to the mistake. The method makes it practical to learn **internal representations** in hidden layers rather than relying on hand-designed features. Although similar ideas appeared earlier, this presentation became the standard reference for reverse-mode automatic differentiation applied to neural networks — the same computational pattern modern transformers use when optimising billions of parameters.

## Key concepts

- **Backpropagation** — efficient gradient computation via the chain rule.  
- **Hidden-layer representations** — learned features, not just linear readouts.  
- **Credit assignment** — distributing error blame across layers.

## Notes

- No stable open PDF in `bib.bib`; local `{citationkey}.txt` may be pinned if added manually.  
- HeRA reader background: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md) Appendix A.
