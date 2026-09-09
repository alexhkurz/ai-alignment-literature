# Deep learning via Hessian-free optimization

**Authors:** James Martens  
**Year:** 2010  
**Venue:** ICML 2010 (peer-reviewed)  
**Citation key:** `martens2010_hessian_free`  
**BibTeX entry:** [entry](../../bib.bib#L704)  
**PDF:** [ICML 2010](https://icml.cc/Conferences/2010/papers/458.pdf)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Deep+Learning+via+Hessian-Free+Optimization+Martens)

## Summary

Martens adapts **Hessian-free optimization** (truncated conjugate gradient on HVPs) to deep autoencoders and recurrent networks, showing that careful curvature-aware updates can train architectures that were difficult for plain SGD at the time. The method never materialises the full Hessian; it relies on Pearlmutter-style HVPs and conjugate-gradient solves. The paper is a bridge between classical second-order numerical optimisation and modern large-scale deep learning practice.

## Key concepts

- **Hessian-free / truncated Newton** — solve **H p ≈ −∇f** using only HVPs.  
- **Conjugate gradients** — Krylov subspace search without explicit **H**.  
- **Deep autoencoders / RNNs** — demonstration that curvature information helps training.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh martens2010_hessian_free`.  
- HeRA reader: [`hera/readers/07-hessian.md`](https://github.com/alexhkurz/hera/blob/main/readers/07-hessian.md).
