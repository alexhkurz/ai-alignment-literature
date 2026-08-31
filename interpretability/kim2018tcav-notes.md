# TCAV: Relative Concept Importance Testing with Linear Concept Activation Vectors

**Authors:** Been Kim, Justin Gilmer, Martin Wattenberg, Fernanda Viégas  
**Year:** 2018  
**Venue:** ICML 2018 (also OpenReview)  
**Citation key:** `kim2018tcav`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [OpenReview](https://openreview.net/pdf?id=SyEnZ-W0b)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Kim+Interpretability+Beyond+Classification+Accuracy+TCAV+2018)

## Summary

**TCAV** (Testing with Concept Activation Vectors) defines a human-labeled concept direction in a network’s activation space and measures how sensitive model predictions are to movement along that direction — bridging human concepts and internal representations.

## Key concepts

- **Concept Activation Vector (CAV)** — direction separating examples with vs without a concept.  
- **TCAV score** — fraction of examples where the concept positively influences the prediction.  
- **User-provided concepts** — exemplar-based concept definition.

## Notes

- Early influential method for concept-level interpretability; precursor to later steering via activation directions.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
