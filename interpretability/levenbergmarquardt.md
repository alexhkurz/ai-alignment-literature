# The Levenberg–Marquardt algorithm: Implementation and theory

**Authors:** Jorge J. Moré  
**Year:** 1978  
**Venue:** *Numerical Analysis* (Lecture Notes in Mathematics, Springer)  
**Citation key:** `levenbergmarquardt`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [Springer](https://doi.org/10.1007/BFb0067700)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Levenberg+Marquardt+algorithm+Implementation+theory+More)

## Summary

Classic reference on the Levenberg–Marquardt algorithm (LMA) for nonlinear least-squares: interpolates between Gauss–Newton and gradient descent via a damping parameter, with implementation guidance and convergence theory. HeRA uses LMA to fit first-order steering matrices by minimizing residual norms between Jacobian columns and target steering directions.

## Key concepts

- **Nonlinear least squares** — minimize \(\|r(\theta)\|^2\).  
- **Damping / trust-region flavor** — stabilizes Gauss–Newton steps.  
- **Implementation details** — practical numerical analysis chapter.

## Notes

HeRA optimization method for computing steering vectors (Section on first-order steering fitting). Book chapter; no open PDF ingested locally.
