# Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?

**Authors:** Wenlong Wang, Fergal Reid  
**Year:** 2026  
**Venue:** arXiv preprint  
**Citation key:** `wang2026_looped_jacobian`  
**BibTeX entry:** [entry](../bib.bib#L1235)  
**PDF:** [arXiv](https://arxiv.org/pdf/2609.01924)  
**arXiv:** [2609.01924](https://arxiv.org/abs/2609.01924)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Looped+Transformers+under+the+Jacobian+Lens+Wang+Reid)

## Summary

Extends the Jacobian-lens / J-space workspace suite from feedforward transformers to depth-recurrent (looped) models via a virtual-unrolling adapter. Evaluates Ouro-2.6B (48 layers looped 4×) and Huginn-0125 (4-layer core recurred 16×), with Qwen3.6-27B as an untied-depth baseline. A workspace still forms in the iterated depth of each architecture, but recurrence changes access: Ouro reconstructs workspace content each loop and resists linear transport across loop boundaries (writes/ablations must span remaining loops); Huginn carries content across all sixteen recurrences while reads/writes/ablations act only in a short sliding window. Verbalizability of newly injected content tracks per-iteration supervision; steerability of existing content does not.

## Key concepts

- Jacobian lens on looped / depth-recurrent transformers
- Virtual-unrolling adapter for workspace experiments under weight tying
- Loop-boundary transport failure (Ouro) vs long-horizon carry with local edit windows (Huginn)
- Per-iteration supervision vs steerability dissociation

## Notes

Follow-up to [`gurnee2026_global_workspace`](gurnee2026_global_workspace.md). Eleven causal experiment families from the workspace suite are re-run under recurrence.
