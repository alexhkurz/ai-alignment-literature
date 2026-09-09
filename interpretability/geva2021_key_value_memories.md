# Transformer feed-forward layers are key-value memories

**Authors:** Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy  
**Year:** 2021  
**Venue:** EMNLP 2021 (peer-reviewed)  
**Citation key:** `geva2021_key_value_memories`  
**BibTeX entry:** [entry](../../bib.bib#L674)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2012.14913.pdf)  
**arXiv:** [2012.14913](https://arxiv.org/abs/2012.14913)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Transformer+Feed+Forward+Layers+Key+Value+Memories)

## Summary

Geva et al. argue that transformer **FFN blocks** act as **key–value memories**: the first layer detects patterns (keys) and the second layer writes associated vectors (values) into the residual stream. This parallels the attention story but for MLP sublayers and helps explain why FFN parameters store factual associations. The HeRA transformer reader cites this when distinguishing **MLP neurons** from **residual stream dimensions**.

## Key concepts

- **FFN as memory** — pattern detection + content retrieval.  
- **Key–value decomposition** of MLP weights.  
- **Factual / lexical storage** in feedforward layers.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh geva2021_key_value_memories`.  
- HeRA reader: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md).
