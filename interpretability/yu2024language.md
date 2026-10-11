# Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch

**Authors:** Le Yu, Bowen Yu, Haiyang Yu, Fei Huang, Yongbin Li  
**Year:** 2024  
**Venue:** ICML 2024  
**Citation key:** `yu2024language`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [OpenReview](https://openreview.net/pdf?id=fq0NaiU8Ex)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Language+Models+Super+Mario+Absorbing+Abilities+Homologous)

## Summary

Introduces **DARE** (Drop And REscale): randomly zero most fine-tuning delta parameters and rescale survivors to approximate original embeddings, then merge sparse deltas from multiple homologous SFT models. Shows SFT deltas are small and highly redundant; DARE can drop 90–99% of delta weights and still merge multi-task abilities into one model without retraining.

## Key concepts

- **DARE** — sparse delta dropping + rescaling before merge.  
- **Homologous models** — same architecture, different task SFT.  
- **Parameter merging** — compose skills without GPU retraining.

## Notes

HeRA merging baseline; related to task arithmetic and LoRA merging.
