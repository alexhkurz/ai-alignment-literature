# The Illustrated Transformer

**Authors:** Jay Alammar  
**Year:** 2018  
**Venue:** Jay Alammar blog (not peer-reviewed)  
**Citation key:** `alammar2018_illustrated_transformer`  
**BibTeX entry:** [entry](../../bib.bib#L1167)  
**URL:** [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Illustrated+Transformer+Alammar)

## Summary

Widely used **pedagogical walkthrough** of the original encoder–decoder Transformer (Vaswani et al., 2017): encoder/decoder stacks, residual connections, layer norm, feed-forward blocks, and **scaled dot-product self-attention** with explicit **Q, K, V** tensors. Uses a tiny running example (short English→French-style sentence) with concrete matrix dimensions (embedding size 512, multi-head split) and step-by-step arithmetic for one attention head — the “full numerical walkthrough” entry point before reading papers or code.

Later expanded in *Hands-On Large Language Models* (LLM-book.com) with updated variants (MQA, RoPE, etc.).

## Key concepts

- **Q / K / V** — three linear projections; attention scores \(QK^\top/\sqrt{d_k}\), output weighted sum of \(V\).  
- **Multi-head attention** — parallel heads with split dimensions, concatenated and projected.  
- **Encoder vs decoder** — self-attention vs masked self-attention + cross-attention.  
- **Residual stream** — add & norm around each sublayer (precursor vocabulary for circuits work).

## Notes

- HTML blog source; local `{citationkey}.txt` from page extract (untracked).  
- Referenced by BertViz documentation as background reading.  
- Pairs with [`karpathy2022_nanogpt`](karpathy2022_nanogpt.md) for executable minimal GPT once concepts are clear.
