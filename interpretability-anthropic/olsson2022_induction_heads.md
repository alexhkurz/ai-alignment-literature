# In-context Learning and Induction Heads

**Authors:** Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah  
**Year:** 2022  
**Venue:** Transformer Circuits Thread / arXiv  
**Citation key:** `olsson2022_induction_heads`  
**BibTeX entry:** [entry](../../bib.bib)  
**URL:** [transformer-circuits.pub](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)  
**PDF:** [arXiv](https://arxiv.org/pdf/2209.11895.pdf)  
**arXiv:** 2209.11895  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Olsson+In+Context+Learning+Induction+Heads+2022)

## Summary

Identifies **induction heads** — attention heads that implement in-context copying / pattern completion — and argues they are central to **in-context learning** emergence during training. Combines mechanistic analysis with scaling and training dynamics.

## Details

Olsson et al. (2022) — "In-context Learning and Induction Heads"
The most concrete example of Q, K, V with a specific, traceable function. They identify induction heads — a two-layer circuit:


Layer 1, "previous token head": $W_Q$ and $W_K$ shaped so token $i$ attends strongly to token $i-1$. Mechanically: $q_i \cdot k_{i-1}$ is large because $W_Q$ and $W_K$ project positional information into aligned directions. The value $v_{i-1}$ (content of the previous token) gets written into position $i$'s residual stream.


Layer 2, "induction head": Now position $i$'s residual stream contains information about itself and about what came before it (written by layer 1). The $W_Q$ and $W_K$ of this head use that compound representation to look back in the sequence for a previous occurrence of the same pattern. If the sequence contains $[A][B] \ldots [A]$, the second $[A]$ attends back to the first $[B]$ — because the layer-1 output at the first $[B]$ encodes "I follow $[A]$", which matches the current query.


This is the clearest extant example of Q, K, V doing something interpretable that you can trace all the way through the math.

## Key concepts

- **Induction head** — attends to previous token occurrences to predict repeats.  
- **In-context learning (ICL)** — few-shot behavior without weight updates.  
- **Phase change** — induction heads appear during training.

## Notes

- Key mechanistic motif linking attention circuits to ICL; background for activation patching discussions.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
