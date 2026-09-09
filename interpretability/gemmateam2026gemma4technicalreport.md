# Gemma 4 Technical Report

**Authors:** Gemma Team, Google DeepMind  
**Year:** 2026  
**Venue:** arXiv technical report  
**Citation key:** `gemmateam2026gemma4technicalreport`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2607.02770)  
**arXiv:** 2607.02770  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Gemma+4+Technical+Report)

## Summary

Introduces the Gemma 4 open-weight multimodal language model family, ranging from 2.3B to 31B (including MoE variants). Gemma 4 adds native multimodal input (text, image, audio), a thinking/reasoning mode, long-context efficiency, an autoregressive multi-token prediction drafter for speculative decoding, and an encoder-free 12B architecture that projects raw audio and image patches directly into LLM embeddings. Quantization-aware training provides efficient variants. Benchmarks show competitive performance against larger frontier open models across STEM, multimodal, and long-context tasks.

## Key concepts

- **Native multimodal Gemma** — unified text/image/audio processing in open-weight models.  
- **Encoder-free 12B architecture** — raw audio/image patches projected into token space.  
- **Thinking mode** — explicit reasoning traces before final response.  
- **MTP drafter + speculative decoding** — faster autoregressive inference.  
- **Long-context and KV-cache efficiency** — key-value sharing and quantization-aware training.
