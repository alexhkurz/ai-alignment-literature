# Aligning Large Language Models with Representation Editing: A Control Perspective

**Authors:** Lingkai Kong, Haorui Wang, Wenhao Mu, Yuanqi Du, Yuchen Zhuang, Yifei Zhou, Yue Song, Rongzhi Zhang, Kai Wang, Chao Zhang  
**Year:** 2024  
**Venue:** arXiv preprint  
**Citation key:** `kong2024aligning`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2406.05954)  
**arXiv:** 2406.05954  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Aligning+Large+Language+Models+Representation+Editing+Control)

## Summary

Reframes LLM alignment as a control problem over a discrete-time stochastic dynamical system. Instead of fine-tuning the model, the authors introduce external control signals into the hidden-state space of an autoregressive LLM. A value function is trained on hidden states via the Bellman equation, and gradient-based optimization obtains the optimal control signals at test time. This representation-editing approach aims to be more stable and compute-efficient than fine-tuning while modifying the underlying model more deeply than prompting or guided decoding.

## Key concepts

- **Representation editing for alignment** — modify hidden states rather than weights or prompts.  
- **LLM as a dynamical system** — autoregressive model viewed as discrete-time stochastic process.  
- **Bellman value function on hidden states** — learn a value function over internal representations.  
- **Test-time control signals** — optimized and injected at inference to steer behavior.
