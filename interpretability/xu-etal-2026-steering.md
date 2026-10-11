# Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics

**Authors:** Ziwen Xu, Chenyan Wu, Hengyu Sun, Haiwen Hong, Mengru Wang, Yunzhi Yao, Longtao Huang, Hui Xue, Shumin Deng, Zhixuan Chu, Huajun Chen, Ningyu Zhang  
**Year:** 2026  
**Venue:** ACL 2026 (Long Papers)  
**Citation key:** `xu-etal-2026-steering`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [ACL Anthology](https://aclanthology.org/2026.acl-long.1463.pdf)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Why+Steering+Works+Unified+View+Language+Model+Parameter+Dynamics)

## Summary

Unifies weight fine-tuning, LoRA, and activation interventions as *dynamic weight updates* induced by a control signal. Introduces a preference–utility decomposition measured on a shared log-odds scale using polarity-paired examples: stronger control raises preference for a target concept but predictably reduces utility (coherent, valid generation), especially when interventions push activations off the model's valid-generation manifold. Proposes a steering method guided by this analysis.

## Key concepts

- **Unified control framework** — weight vs activation methods as one family.  
- **Preference vs utility** — log-odds trade-off under steering.  
- **Activation manifold** — geometric view of steering side effects.

## Notes

HeRA bibliography; connects merging, LoRA, and activation steering theoretically.
