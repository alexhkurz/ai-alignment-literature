# Fast exact multiplication by the Hessian

**Authors:** Barak A. Pearlmutter  
**Year:** 1994  
**Venue:** Neural Computation (peer-reviewed)  
**Citation key:** `pearlmutter1994_fast_hessian`  
**BibTeX entry:** [entry](../../bib.bib#L651)  
**PDF:** [open copy](https://mural.maynoothuniversity.ie/5501/1/BP_fast%20exact.pdf)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Pearlmutter+Fast+Exact+Multiplication+Hessian)

## Summary

Pearlmutter shows how to compute the product **Hv** of a network Hessian **H** with an arbitrary vector **v** without ever forming **H**. The trick is a differential operator **R_v** applied to the backprop equations that compute gradients: one forward/backward pass yields an **Hessian–vector product (HVP)** at the same asymptotic cost as a gradient. This is the foundation of practical second-order methods in deep learning and of modern **forward-mode / reverse-mode** tricks for higher-order derivatives (including JVPs used in HeRD-Merging curvature probes).

## Key concepts

- **Hessian–vector product (HVP)** — curvature along direction **v** without storing **H**.  
- **R-operator** — directional derivative of the gradient map.  
- **Same cost as backprop** — feasible inside large networks.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh pearlmutter1994_fast_hessian` from the open PDF URL.  
- HeRA reader: [`hera/readers/07-hessian.md`](https://github.com/alexhkurz/hera/blob/main/readers/07-hessian.md).
