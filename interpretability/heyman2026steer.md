# Steer Like the LLM: Activation Steering that Mimics Prompting

**Authors:** Geert Heyman, Frederik Vandeputte  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `heyman2026steer`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2605.03907)  
**arXiv:** 2605.03907  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Steer+Like+the+LLM+Activation+Steering+Mimics+Prompting)

## Summary

Frames prompt steering as a form of activation steering and asks why popular activation-steering methods underperform prompting. The key difference: prompt steering applies strong, token-specific interventions, whereas standard steering often uses a uniform or single vector. The paper introduces Prompt Steering Replacement (PSR) models, which learn token-specific steering coefficients from activations to imitate prompt-based behavior. On three steering benchmarks, PSR outperforms existing activation-steering methods and competes with prompting on AxBench and persona steering.

## Key concepts

- **Prompt as activation steering** — in-context prompting is itself a steering mechanism the model performs on itself.  
- **Token-specific steering coefficients** — prompt steering varies in strength per token and position.  
- **Prompt Steering Replacement (PSR)** — a learned module that estimates per-token activation-steering coefficients.  
- **Prompting vs. activation steering** — comparing and distilling prompting into interpretable interventions.
