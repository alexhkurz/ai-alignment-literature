# Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning

**Authors:** Zirui Song, Huaxing Liu, Xiang Wang, Shuai Li, Xinye Li, Lang Gao, Jinghui Zhang, Zheng Lu, Fengxian Ji, Xiaojun Chang, Xiuying Chen  
**Year:** 2026  
**Venue:** arXiv preprint (AAAI copyright line in PDF)  
**Citation key:** `song2026_j_access`  
**BibTeX entry:** [entry](../bib.bib#L1253)  
**PDF:** [arXiv](https://arxiv.org/pdf/2608.11408)  
**arXiv:** [2608.11408](https://arxiv.org/abs/2608.11408)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Measure+Don%27t+Optimize+Forecasting+Recovery+LLM+Unlearning+J-Access)

## Summary

Introduces J-Access, an inference-time audit that applies the Jacobian lens to map intermediate representations into vocabulary space and scores how often “forgotten” target concepts remain accessible along the output pathway. Across 398 public unlearned models and eight methods: most retain accessibility above a retain-only gold baseline; pre-attack J-Access predicts model-level recovery speed/extent under relearning, but not which specific facts recover; directly minimizing J-Access during unlearning does not delete knowledge—models learn to hide from the audit and then recover more after attack. Positions J-Access as a diagnostic, not an optimization target.

## Key concepts

- J-Access score (Jacobian-lens residual accessibility)
- Recovery forecasting vs item-level prediction failure
- Goodharting when the audit becomes a training objective
- White-box unlearning evaluation beyond behavioral refusal

## Notes

Builds directly on the Jacobian lens / J-space readout pathway from [`gurnee2026_global_workspace`](gurnee2026_global_workspace.md).
