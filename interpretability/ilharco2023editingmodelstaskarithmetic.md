# Editing Models with Task Arithmetic

**Authors:** Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Wortsman, Suchin Gururangan, Ludwig Schmidt, Hannaneh Hajishirzi, Ali Farhadi  
**Year:** 2023  
**Venue:** ICLR 2023  
**Citation key:** `ilharco2023editingmodelstaskarithmetic`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2212.04089)  
**arXiv:** 2212.04089  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Editing+Models+Task+Arithmetic+Ilharco)

## Summary

Proposes *task vectors*: the difference in model weights between a fine-tuned model and its pre-trained base. These vectors define a direction in weight space that improves performance on a target task. The paper shows that task vectors can be manipulated with arithmetic operations — negation, addition, and weighted combination — to erase, combine, or bias model behavior. Task arithmetic enables steering model performance on novel tasks, zero-shot task composition, and bias mitigation without re-training.

## Key concepts

- **Task vectors** — weight-space direction between pre-trained and fine-tuned model.  
- **Task arithmetic** — add, subtract, or interpolate task vectors to edit or combine behaviors.  
- **Erasure and bias mitigation** — negate a task vector to reduce an unwanted capability.  
- **Zero-shot composition** — combine vectors from related tasks to obtain new task behavior.
