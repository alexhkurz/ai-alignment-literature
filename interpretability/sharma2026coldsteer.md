# COLD-Steer: Steering Large Language Models via In-Context One-Step Learning Dynamics

**Authors:** Kartik Sharma, Rakshit S. Trivedi  
**Year:** 2026  
**Venue:** ICLR 2026  
**Citation key:** `sharma2026coldsteer`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2603.06495)  
**arXiv:** 2603.06495  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=COLD-Steer+Steering+Large+Language+Models+In-Context+One-Step)

## Summary

Proposes COLD-Steer, a training-free activation-steering method that approximates the representational changes that would result from gradient descent on in-context examples. The method uses either a unit-kernel approximation based on gradients with respect to activations or a two-forward-pass finite-difference approximation. COLD-Steer reaches up to 95% steering effectiveness while using 50× fewer samples than the best existing contrast-based methods, addressing the trade-off between sample efficiency and steering quality.

## Key concepts

- **COLD-Steer** — approximate one-step learning dynamics for in-context steering.  
- **In-context learning dynamics** — infer update direction from a few examples.  
- **Unit-kernel and finite-difference approximations** — two inference-time estimators.  
- **Sample-efficient steering** — reduce the number of contrast examples needed.
