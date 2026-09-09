# DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

**Authors:** Pengcheng He, Jianfeng Gao, Weizhu Chen  
**Year:** 2023  
**Venue:** ICLR 2023  
**Citation key:** `he2023debertav`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2111.09543)  
**arXiv:** 2111.09543  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=DeBERTaV3+ELECTRA+Gradient-Disentangled+Embedding+Sharing)

## Summary

Presents DeBERTaV3, which improves DeBERTa by replacing masked language modeling (MLM) with replaced token detection (RTD), and introduces gradient-disentangled embedding sharing (GDES) to solve the tug-of-war between the discriminator and generator embeddings in ELECTRA. GDES lets the discriminator and generator share embeddings without their opposing gradients pulling token vectors in conflicting directions. DeBERTaV3 sets a new GLUE SOTA for its model size (91.37% Large), and the multilingual mDeBERTaV3 also improves XLM-R on XNLI.

## Key concepts

- **Replaced token detection (RTD)** — ELECTRA-style pre-training as an alternative to MLM.  
- **Gradient-disentangled embedding sharing (GDES)** — shared embeddings despite opposing generator/discriminator losses.  
- **Tug-of-war dynamics** — vanilla ELECTRA embedding sharing hurts because the two losses pull embeddings apart.  
- **Multilingual extension** — mDeBERTaV3 improves cross-lingual transfer on XNLI.
