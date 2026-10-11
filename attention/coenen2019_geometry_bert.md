# Visualizing and measuring the geometry of BERT

**Authors:** Andy Coenen, Emily Reif, Ann Yuan, Been Kim, Adam Pearce, Fernanda Viégas, Martin Wattenberg  
**Year:** 2019  
**Venue:** NeurIPS 2019 (peer-reviewed)  
**Citation key:** `coenen2019_geometry_bert`  
**BibTeX entry:** [entry](../../bib.bib#L1184)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/1906.02715.pdf)  
**arXiv:** [1906.02715](https://arxiv.org/abs/1906.02715)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Visualizing+Measuring+Geometry+BERT+Coenen+2019)

## Summary

Qualitative and quantitative study of **internal geometry in BERT**: how syntax and semantics are represented in context embeddings and attention. Two main syntactic lines: (1) **attention probes** — concatenate every layer/head’s scalar attention for an ordered token pair into a **model-wide attention vector** and train linear probes (85.8% binary / 71.9% multiclass dependency-relation accuracy on Penn Treebank); (2) **parse-tree geometry** — after Hewitt–Manning’s structural probe, **PCA projections of context embeddings** (not raw Q/K vectors) visualize dependency trees and deviations from ideal power-2 tree metrics. Semantic section uses activation visualizations suggesting fine-grained word senses in a low-dimensional subspace.

Interactive exploration blog: [Language, trees, and geometry in neural networks](https://pair-code.github.io/interpretability/bert-tree/).

## Key concepts

- **Model-wide attention vector** — all heads’ \(a_{ij}\) values for pair \((i,j)\) stacked; linear probe ⇒ syntax in attention patterns.  
- **Structural probe + PCA** — 2D projection of probed **context embeddings** with tree edges overlaid.  
- **Squared Euclidean tree distance** — mathematical argument for Hewitt–Manning’s \(\|B h_i - B h_j\|^2 \approx d_{\text{tree}}(i,j)\).  
- **Semantic subspace** — sense distinctions visible in activation geometry.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh coenen2019_geometry_bert`.  
- PCA here targets **post-attention context embeddings** after probe transform; direct **Q/K PCA** is a separate later line of work (e.g. positional/content disentangling in later transformer-geometry papers).  
- Complements [`vig2019_multiscale_attention`](vig2019_multiscale_attention.md) (per-head weight visualization) and [`elhage2021_transformer_circuits`](../interpretability-anthropic/elhage2021_transformer_circuits.md) (toy-model \(W_Q W_K^\top\) circuits).
