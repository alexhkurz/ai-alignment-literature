# Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures

**Authors:** SiYuan Ma, Yiqin Luo, Zhangji, Canran Xiao, Albert Gao, Wei Wang, Qiwei Wu, Xinran Li, Jinfeng Wei, Qixin Zhang  
**Year:** 2026  
**Venue:** ICLR 2026 (conference paper; arXiv:2607.27617v2)  
**Citation key:** `ma2026_hidden_apis`  
**BibTeX entry:** [entry](../bib.bib#L1262)  
**PDF:** [arXiv](https://arxiv.org/pdf/2607.27617)  
**arXiv:** [2607.27617](https://arxiv.org/abs/2607.27617)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Hidden+APIs+in+Language+Models+Forked+Futures)

## Summary

Identical current answers can arise from hidden states that support different future computations, so answer probes do not certify a reusable internal interface. The paper introduces forked futures: after a prefix state forms, future operations are sampled and states are compared by the response distributions those operations induce, yielding an empirical causal quotient without researcher-chosen latent labels. Candidate interface classes (Shared, Local, Mixture, Distributed) compete under prequential causal description length with fidelity and capacity constraints. Shared interfaces win on held-out description length (gains reported on Qwen2.5-1.5B and Llama-3-8B) and transplantation metrics; API-aligned paths mediate most of the target effect versus null paths. A blind four-class model-organism test recovers most planted architectures.

## Key concepts

- Forked futures / future-signature fidelity
- Shared vs local/mixture/distributed causal interfaces
- Prequential causal description length for interface selection
- Transplantation and mediation tests for reusable internal APIs

## Notes

Mechanistic / causal-interface paper downloaded with the J-space batch; complementary to Jacobian-lens workspace audits rather than a direct J-space extension.
