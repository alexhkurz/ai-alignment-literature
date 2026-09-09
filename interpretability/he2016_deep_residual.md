# Deep residual learning for image recognition

**Authors:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun  
**Year:** 2016  
**Venue:** CVPR 2016 (peer-reviewed)  
**Citation key:** `he2016_deep_residual`  
**BibTeX entry:** [entry](../../bib.bib#L694)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/1512.03385.pdf)  
**arXiv:** [1512.03385](https://arxiv.org/abs/1512.03385)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Deep+Residual+Learning+Image+Recognition)

## Summary

ResNets replace each layer’s transformation with a **residual block** that adds the layer’s output to its input: **y = F(x) + x**. This makes very deep networks easier to optimise by giving gradients a shortcut path and by encouraging layers to learn **incremental refinements** rather than full rewrites of the representation. Transformers inherited the same idea as **residual stream** additions around attention and MLP sublayers — the architectural choice that makes activation steering and adapter injection mathematically natural.

## Key concepts

- **Residual / skip connection** — additive path around a sublayer.  
- **Identity baseline** — default is “no change”; **F** learns corrections.  
- **Gradient highways** — easier training of deep stacks.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh he2016_deep_residual`.  
- HeRA reader: [`hera/readers/01-transformers.md`](https://github.com/alexhkurz/hera/blob/main/readers/01-transformers.md).
