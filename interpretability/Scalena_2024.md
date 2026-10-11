# Multi-property Steering of Large Language Models with Dynamic Activation Composition

**Authors:** Daniel Scalena, Gabriele Sarti, Malvina Nissim  
**Year:** 2024  
**Venue:** BlackboxNLP 2024 (ACL workshop)  
**Citation key:** `Scalena_2024`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [ACL Anthology](https://aclanthology.org/2024.blackboxnlp-1.34.pdf)  
**DOI:** [10.18653/v1/2024.blackboxnlp-1.34](https://doi.org/10.18653/v1/2024.blackboxnlp-1.34)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Multi-property+Steering+Dynamic+Activation+Composition+Scalena)

## Summary

Evaluates activation steering beyond single-property, short-generation settings. Contrastive in-context demonstrations yield steering vectors for safety, formality, and language; optimal injection settings are highly property-dependent, and strong fixed-intensity steering over longer generations harms fluency. The authors propose Dynamic Activation Composition: an information-theoretic (KL / probability-shift) schedule that adapts each property’s steering intensity at every generation step, boosting under-conditioned properties and damping already-conditioned ones. On multi-property steering with Mistral 7B, the method maintains high conditioning accuracy while better preserving fluency than static composition baselines.

## Key concepts

- **Multi-property steering** — simultaneous conditioning on several attributes (e.g. safety + formality + language).  
- **Property-dependent optima** — best layer / intensity settings differ across properties.  
- **Conditioning–fluency trade-off** — fixed high intensity over long generations degrades fluency.  
- **Dynamic Activation Composition** — per-step adaptive intensities from the expected steering effect (prediction shift), rather than a constant coefficient.
