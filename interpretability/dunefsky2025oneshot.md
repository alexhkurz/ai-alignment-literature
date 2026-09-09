# One-shot Optimized Steering Vectors Mediate Safety-relevant Behaviors in LLMs

**Authors:** Jacob Dunefsky, Arman Cohan  
**Year:** 2025  
**Venue:** COLM 2025  
**Citation key:** `dunefsky2025oneshot`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2502.18862)  
**arXiv:** 2502.18862  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=One-shot+Optimized+Steering+Vectors+Safety+LLMs+Dunefsky)

## Summary

Shows that steering vectors can be optimized with gradient descent on a single training example and still generalize to mediate safety-relevant behaviors. One-shot optimized steering vectors can induce harmful behavior on benign inputs and suppress harmful behavior on malign inputs, with transfer across inputs and models. In a HarmBench refusal-suppression task, one-shot SVs achieve 96.9% attack success rate. The work also links one-shot steering to emergent misalignment, where SVs optimized for narrow bad behavior generalize to unrelated harmful responses.

## Key concepts

- **One-shot optimized steering vectors** — gradient descent over a single contrastive example.  
- **Refusal suppression** — SVs that break safety guardrails on otherwise benign queries.  
- **Generalization of narrow misalignment** — steering for one bad behavior spreads to unrelated harmful outputs.  
- **Steering-vector safety** — lightweight intervention that can mediate alignment-relevant behavior.
