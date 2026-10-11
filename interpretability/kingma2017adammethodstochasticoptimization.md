# Adam: A Method for Stochastic Optimization

**Authors:** Diederik P. Kingma, Jimmy Lei Ba  
**Year:** 2017  
**Venue:** ICLR 2015  
**Citation key:** `kingma2017adammethodstochasticoptimization`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/1412.6980)  
**arXiv:** 1412.6980  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Adam+Method+Stochastic+Optimization)

## Summary

Introduces Adam, a first-order gradient-based optimization algorithm that maintains adaptive estimates of lower-order moments (mean and variance) of the gradients. Adam is straightforward to implement, memory-efficient, invariant to diagonal rescaling, and well-suited to large-scale, non-stationary, or noisy objectives. The paper provides theoretical convergence analysis and a regret bound comparable to best-known online convex optimization results.

## Key concepts

- **Adaptive moment estimation** — exponentially decaying averages of gradients and squared gradients.  
- **Bias correction** — accounting for zero initialization of moving averages.  
- **Invariance to gradient rescaling** — adapts per-parameter step sizes.  
- **Stochastic optimization** — suitable for sparse, noisy, and high-dimensional objectives.
