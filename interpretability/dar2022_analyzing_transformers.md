# Analyzing transformers in embedding space

**Authors:** Guy Dar, Mor Geva, Ankit Gupta, Jonathan Berant  
**Year:** 2023  
**Venue:** AAAI 2023 (peer-reviewed)  
**Citation key:** `dar2022_analyzing_transformers`  
**BibTeX entry:** [entry](../../bib.bib#L684)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2209.02535.pdf)  
**arXiv:** [2209.02535](https://arxiv.org/abs/2209.02535)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Analyzing+Transformers+in+Embedding+Space)

## Summary

The paper studies how transformer layers transform **token embeddings** in embedding space, decomposing updates into interpretable components and relating attention and FFN contributions to geometric operations on embeddings. It complements the circuits view by emphasising **where** in representation space computation happens — useful background for thinking about **activation steering** as shifts in the residual stream versus weight edits in embedding/projection maps.

## Key concepts

- **Embedding-space analysis** — geometry of layer-wise updates.  
- **Attention vs FFN contributions** — separate transformation modes.  
- **Interpretability via decomposition** — not single-scalar probing alone.

## Notes

- Citation key uses arXiv year **2022**; AAAI publication **2023**.  
- Regenerate local text: `./scripts/ensure-extract.sh dar2022_analyzing_transformers`.  
- HeRA reader: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md).
