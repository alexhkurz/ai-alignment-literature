# Distributed Representations of Words and Phrases and their Compositionality

**Authors:** Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S. Corrado, Jeff Dean  
**Year:** 2013  
**Venue:** NeurIPS 2013  
**Citation key:** `mikolov2013_word2vec`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/1310.4546.pdf)  
**arXiv:** 1310.4546  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Mikolov+Distributed+Representations+Words+Phrases+Compositionality+2013)

## Summary

Introduces **word2vec** — shallow neural models (skip-gram, CBOW) that learn dense word embeddings from co-occurrence prediction. Famous for **linear analogies** (e.g. king − man + woman ≈ queen), showing that semantic relations can appear as directions in embedding space without explicit supervision.

## Key concepts

- **Skip-gram / CBOW** — predict context from word or vice versa.  
- **Linear structure** — relational semantics as vector offsets.  
- **Compositionality** — phrase embeddings via additive composition.

## Notes

- Foundational for the “concepts as directions” hypothesis cited in activation steering.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
