# Quantum-PEFT: Ultra Parameter-Efficient Fine-Tuning

**Authors:** Toshiaki Koike-Akino, Francesco Tonin, Yongtao Wu, Frank Zhengqing Wu, Leyla Naz Candogan, Volkan Cevher  
**Year:** 2025  
**Venue:** ICLR 2025  
**Citation key:** `koike-akino2025quantumpeft`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2503.05431)  
**arXiv:** 2503.05431  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Quantum-PEFT+Ultra+Parameter-Efficient+Fine-Tuning)

## Summary

Introduces Quantum-PEFT, a parameter-efficient fine-tuning method built on a quantum unitary parameterization. Unlike low-rank methods such as LoRA, Quantum-PEFT uses Pauli parameterization to represent full-rank updates while scaling the number of trainable parameters logarithmically with ambient dimension. The method is compatible with standard backpropagation and can be applied to any neural network module, not just language models.

## Key concepts

- **Quantum-PEFT** — quantum unitary / Pauli parameterization for PEFT.  
- **Logarithmic parameter scaling** — parameter count grows with log of dimension, not linearly as in LoRA.  
- **Full-rank updates** — expressive adaptation while remaining parameter-efficient.  
- **Pauli parameterization** — quantum-inspired basis for compact, expressive trainable transformations.
