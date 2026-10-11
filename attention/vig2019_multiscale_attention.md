# A multiscale visualization of attention in the Transformer model

**Authors:** Jesse Vig  
**Year:** 2019  
**Venue:** ACL 2019 System Demonstrations (peer-reviewed)  
**Citation key:** `vig2019_multiscale_attention`  
**BibTeX entry:** [entry](../../bib.bib#L1175)  
**PDF:** [ACL Anthology](https://aclanthology.org/P19-3007.pdf)  
**arXiv:** [1906.05714](https://arxiv.org/abs/1906.05714)  
**Tool:** [BertViz](https://github.com/jessevig/bertviz)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Multiscale+Visualization+Attention+Transformer+Vig+2019)

## Summary

Introduces **BertViz**, an open-source Jupyter/Colab tool for inspecting Transformer attention at three scales on BERT and GPT-2. The **attention-head view** shows token–token attention weights for a chosen layer/head. The **model view** overlays all layers and heads to locate structurally important heads quickly. The **neuron view** decomposes the softmax input into **query** and **key** vector components and **element-wise Q×K product bars**, linking individual dimensions to attention patterns (e.g. distance-decay heads).

Demonstrated use cases: detecting gender bias in occupation predictions, finding heads that attend across sentence pairs, and identifying neuron positions that drive positional attention decay.

## Key concepts

- **Attention-head view** — heatmap / bipartite graph of attention weights \(\mathrm{softmax}(QK^\top/\sqrt{d})\).  
- **Model view** — bird’s-eye grid of heads × layers.  
- **Neuron view** — per-token **Q** and **K** bars plus **Q⊙K** contribution bars before softmax.  
- **Multiscale interpretability** — same forward pass, three complementary lenses.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh vig2019_multiscale_attention`.  
- Extends Jones (2017) Tensor2Tensor attention visualization to BERT/GPT-2 and adds model + neuron views.  
- Pairs with [`alammar2018_illustrated_transformer`](alammar2018_illustrated_transformer.md) (pedagogy) and [`elhage2021_transformer_circuits`](../interpretability-anthropic/elhage2021_transformer_circuits.md) (formal QK/OV factorization).
