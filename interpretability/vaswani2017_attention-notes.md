# Attention is all you need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin  
**Year:** 2017  
**Venue:** NeurIPS 2017 (peer-reviewed)  
**Citation key:** `vaswani2017_attention`  
**BibTeX entry:** [entry](../../bib.bib#L623)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/1706.03762.pdf)  
**arXiv:** [1706.03762](https://arxiv.org/abs/1706.03762)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Attention+Is+All+You+Need)

## Summary

Introduces the **Transformer**: a sequence model built from stacked **self-attention** and position-wise feedforward blocks, without recurrence or convolution. Each position attends to all others via learned **query, key, value** projections; **multi-head** attention runs several attention patterns in parallel. The architecture is the template for modern LLMs and the object of HeRA’s projection-head adapters (**W_Q, W_K, W_V, W_O**).

## Key concepts

- **Scaled dot-product attention** — softmax(**QK**ᵀ/√d_k)**V**.  
- **Multi-head attention** — parallel heads with separate projections.  
- **Encoder–decoder stack** — basis for later decoder-only language models.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh vaswani2017_attention`.  
- HeRA reader: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md).
