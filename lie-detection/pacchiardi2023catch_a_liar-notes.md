# How to catch an AI liar: lie detection in black-box LLMs by asking unrelated questions

**Authors:** Lorenzo Pacchiardi, Alex J. Chan, Sören Mindermann, Ilan Moscovitz, Alexa Y. Pan, Yarin Gal, Owain Evans, Jan Brauner  
**Year:** 2023  
**Citation key:** `pacchiardi2023catch_a_liar`  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2309.15840.pdf)  
**arXiv:** [2309.15840](https://arxiv.org/abs/2309.15840)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=How+to+Catch+an+AI+Liar+Lie+Detection+in+Black-Box+LLMs)

## Summary

The paper defines an LLM **lie** as producing a false statement while still representing the truth in a demonstrable way (for example, after being instructed to misreport a fact). The authors then build a **black-box detector** that uses no internal activations and no external ground truth for the specific target fact. After a suspected lie, the method asks a fixed set of unrelated follow-up questions and fits a **logistic regression** classifier on the model’s yes/no responses.

Despite this simplicity, the detector shows strong **generalisation** beyond its training setup. Trained in one setting (GPT-3.5 lying on factual prompts), it transfers across **model families** and behavioural regimes, including fine-tuned liars, sycophancy, and more realistic sales-like scenarios. The authors argue this reflects **stable behavioural signatures** of lying that may support broader auditing when direct trust in model statements is unsafe.

## Authors

Mixed affiliation (Oxford / OATML-style line-up); first author Lorenzo Pacchiardi; senior names include Yarin Gal, Owain Evans, Jan Brauner.


## Key concepts

- **Black-box** detection (no gradients, no activations).  
- **Unrelated questions** as a behavioural fingerprint of lying.  
- **Logistic regression** on yes/no outputs.  
- **Out-of-distribution generalisation** (architecture, fine-tuning, sycophancy, applied settings).  
- Operational definition of **lying** vs mere error.

## Notes

- Local PDF should live at `pacchiardi2023catch_a_liar.pdf` in this folder (git-ignored).  
- Cite with `\parencite{pacchiardi2023catch_a_liar}` / `\textcite{pacchiardi2023catch_a_liar}` in LaTeX.
