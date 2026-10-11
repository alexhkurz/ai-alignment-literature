# Steering Llama 2 via Contrastive Activation Addition

**Authors:** Nina Panickssery, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner  
**Year:** 2024  
**Venue:** arXiv preprint  
**Citation key:** `panickssery2024steeringllama2contrastive`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2312.06681)  
**arXiv:** 2312.06681  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Steering+Llama+2+via+Contrastive+Activation+Addition)

## Summary

Introduces Contrastive Activation Addition (CAA), an inference-time steering method that computes a steering vector by averaging the difference in residual-stream activations between positive and negative contrast pairs. The vector is added to all token positions after the user prompt with a tunable coefficient, allowing fine-grained control over behaviors such as truthfulness, instruction following, and harmfulness. CAA does not require re-training and is tested on Llama 2, showing that simple contrastive examples can induce precise behavioral control.

## Key concepts

- **Contrastive Activation Addition (CAA)** — steering vector = mean activation difference between contrast pairs.  
- **Inference-time activation steering** — modify hidden states during the forward pass.  
- **Residual-stream additions** — steer at all token positions with a scalar coefficient.  
- **Behavioral control** — target specific properties without fine-tuning.
