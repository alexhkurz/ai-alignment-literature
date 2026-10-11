# Mistral 7B

**Authors:** Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, et al.  
**Year:** 2023  
**Venue:** arXiv preprint  
**Citation key:** `jiang2023mistral7b`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2310.06825)  
**arXiv:** 2310.06825  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Mistral+7B+Jiang+2023)

## Summary

Introduces Mistral 7B, a 7B-parameter decoder-only LM designed for strong performance at modest scale. Uses grouped-query attention (GQA) for faster inference and sliding-window attention (SWA) for long contexts at lower cost. Reports beating Llama 2 13B on standard benchmarks and competitive math/code vs. much larger models. Releases base and instruction-tuned variants under Apache 2.0.

## Key concepts

- **Grouped-query attention (GQA)** — shared KV heads, faster decoding.  
- **Sliding-window attention (SWA)** — local attention with rolling cache.  
- **Mistral-7B-Instruct** — chat-tuned variant used in HeRA experiments.

## Notes

HeRA evaluation backbone (`mistralai/Mistral-7B-Instruct-v0.3`).
