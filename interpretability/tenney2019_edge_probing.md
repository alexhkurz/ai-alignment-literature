# What do you learn from context? Probing for sentence structure in contextualized word representations

**Authors:** Ian Tenney, Patrick Xia, Berlin Chen, Alex Wang, Adam Poliak, R. Thomas McCoy, Najoung Kim, Benjamin Van Durme, Samuel R. Bowman, Dipanjan Das, Ellie Pavlick  
**Year:** 2019  
**Venue:** ICLR 2019  
**Citation key:** `tenney2019_edge_probing`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/1905.06316.pdf)  
**arXiv:** 1905.06316  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=What+do+you+learn+from+context+Tenney+probing+sentence+structure+2019)

## Summary

Introduces **edge probing**: a unified format that turns structured NLP tasks into predicting a label for one or two token **spans**, using only the contextual vectors inside those spans (encoder frozen). Probes CoVe, ELMo, GPT, and BERT on a suite drawn from the classical NLP pipeline (syntax through semantics). Main finding: these models are strong on **syntactic** phenomena relative to a non-contextual lexical baseline, but gains on **semantic** tasks are comparatively small.

## Key concepts

- **Edge probing** — common span/edge template for POS, constituents, dependencies, entities, SRL, coreference, SPR, relations.  
- **Frozen encoder** — only span pooling + MLP classifier train; pretrained weights stay fixed.  
- **Lexical baseline** — separates context from word-identity priors.  
- **Cross-model comparison** — CoVe, ELMo, OpenAI GPT, BERT under one metric suite.

## Notes

- Method paper behind the later ACL follow-up [`tenney2019_bert_pipeline`](tenney2019_bert_pipeline.md) (layer-wise “NLP pipeline” analysis of BERT).  
- Public code: [jiant](https://github.com/jsalt18-sentence-repl/jiant) probing suite.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
