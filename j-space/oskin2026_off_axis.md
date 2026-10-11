# Off-Axis, On Purpose: Where a Transformer Computes Concepts and Why it Does So

**Authors:** Mark Oskin  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `oskin2026_off_axis`  
**BibTeX entry:** [entry](../bib.bib#L1244)  
**PDF:** [arXiv](https://arxiv.org/pdf/2608.10251)  
**arXiv:** [2608.10251](https://arxiv.org/abs/2608.10251)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Off-Axis+On+Purpose+Oskin+transformer)

## Summary

Argues that intermediate transformer states being off the unembedding (“read-out”) axis is functional rather than a mere obstacle to interpretation. In a 12-layer model, early computation writes into a subspace held near-orthogonal to the vocabulary read-out (attention values ~75–96° off-axis); forcing values onto the read-out harms composition far more than matched random rotations. A single rotation fitted to the token stream (not to concepts) transports the concept constellation layer-to-layer at high \(R^2\), driven by the antisymmetric part of the layer’s linear response. Late layers bring the answer on-axis by addition. The off-axis frame is largely free: many prescribed bases are adopted without hurting quality, so a random basis chosen before training can be used as an interpretability coordinate system through the concept phase.

## Key concepts

- Off-axis residual subspace as insulation for cross-token composition
- Concept-phase frame rotation vs late on-axis answer arrival
- Antisymmetric linear response as the turn that moves concepts
- Prescribable / seed-dependent concept frames with shared read-outs

## Notes

Jacobian / linear-response geometry paper adjacent to the Jacobian-lens literature that defines J-space; not itself a J-space audit paper.
