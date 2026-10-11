# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

**Authors:** Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nicholas L. Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E. Burke, Tristan Hume, Shan Carter, Tom Henighan, Chris Olah  
**Year:** 2023  
**Venue:** Anthropic Transformer Circuits thread  
**Citation key:** `bricken2023towards`  
**BibTeX entry:** [entry](../../bib.bib)  
**URL:** [transformer-circuits.pub](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## Summary

Presents a large-scale demonstration that sparse autoencoders can extract interpretable, monosemantic features from a one-layer transformer. The authors train sparse autoencoders on MLP activations from 8 billion tokens, with expansion factors up to 256× (131,072 features). They introduce a suite of methods for evaluating feature interpretability, including automated explanations with Claude, human scoring rubrics, and feature-density analysis. The work argues that dictionary learning can overcome polysemanticity in real language models and provides practical training advice for sparse autoencoders.

## Key concepts

- **Monosemanticity** — learning features that correspond to single, human-understandable concepts.  
- **Sparse autoencoders for interpretability** — overcomplete dictionary learning on MLP activations.  
- **Feature interpretability rubric** — human and automated scoring of feature descriptions against behavior.  
- **Resampling and decoder normalization** — practical techniques for training sparse autoencoders.  
- **Phenomenology** — feature motifs, splitting, and universality patterns across learned dictionaries.
