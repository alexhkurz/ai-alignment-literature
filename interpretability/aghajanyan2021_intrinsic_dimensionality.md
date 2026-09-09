# Intrinsic dimensionality explains the effectiveness of language model fine-tuning

**Authors:** Armen Aghajanyan, Luke Zettlemoyer, Sonal Gupta  
**Year:** 2021  
**Venue:** ACL 2021 (peer-reviewed)  
**Citation key:** `aghajanyan2021_intrinsic_dimensionality`  
**BibTeX entry:** [entry](../../bib.bib#L641)  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2012.13255.pdf)  
**arXiv:** [2012.13255](https://arxiv.org/abs/2012.13255)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Intrinsic+Dimensionality+Explains+Effectiveness+Language+Model+Fine-Tuning)

## Summary

The paper measures the **intrinsic dimension** of fine-tuning objectives: how many degrees of freedom are actually needed to reach most of the full fine-tune’s performance when optimising in a random low-dimensional subspace of parameter space. For many NLP tasks the intrinsic dimension is **far smaller** than the parameter count, explaining why low-rank methods like **LoRA** work well — behavioural adaptation lives in a thin subspace of weight space. This motivates HeRA’s low-rank adapters and merging literature.

## Key concepts

- **Intrinsic dimension** — minimal subspace dimension for near-full fine-tune quality.  
- **Random subspace training** — empirical probe of effective degrees of freedom.  
- **Low-rank adaptation** — structural prior matching empirical findings.

## Notes

- Regenerate local text: `./scripts/ensure-extract.sh aghajanyan2021_intrinsic_dimensionality`.  
- HeRA reader: [`hera/readers/02-lora.md`](https://github.com/alexhkurz/hera/blob/main/readers/02-lora.md).
