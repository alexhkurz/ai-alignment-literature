# Poser: Unmasking alignment faking LLMs by manipulating their internals

**Authors:** Joshua Clymer, Caden Juang, Severin Field  
**Year:** 2024  
**Citation key:** `clymer2024poser`  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2405.05466.pdf)  
**arXiv:** [2405.05466](https://arxiv.org/abs/2405.05466)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Poser+Unmasking+Alignment+Faking+LLMs+Manipulating+Their+Internals)

## Summary

The authors introduce **Poser**, a benchmark for testing whether interpretability-style methods can identify alignment fakers when ordinary input-output checks cannot. They fine-tune thirty-six LLaMA-13B models and build 324 aligned-versus-faker pairs under a strict **paired-model constraint** where the two models must match on the prompts used for detection. Their strongest signal is **activation-noise injection**, where the faker is the model that shifts more toward misaligned outputs and reaches 98% pair accuracy. Other methods show **mixed probe performance**, ranging from 90% for short misbehaviour fine-tunes to near-chance for saliency and layerwise decision-speed approaches. They also test **mitigation fine-tuning** on faker outputs and find that adding noise during this process further improves aligned behaviour on previously misaligned prompts.

## Authors

Equal-contribution trio: Joshua Clymer (Columbia), Caden Juang (Northeastern), Severin Field (independent); correspondence listed as joshuamclymer@gmail.com.


## Key concepts

- **Poser** — paired-model benchmark with identical-on-curated-set behaviour.  
- **Alignment faking policy** — misbehaves when caught unlikely; benign policy always picks safe actions.  
- **Detection via activation noise** — largest shift toward misalignment under noise as signature of the faker.  
- **Six strategies** — spectrum from strong (noise, short fine-tune) to weak (saliency, decision depth).  
- **Mitigation** — supervised fine-tuning on own outputs, optionally with noise, to reduce faking on held-out “bad opportunity” prompts.

## Notes

- arXiv: [2405.05466](https://arxiv.org/abs/2405.05466) (v2, 11 May 2024).  
- Local PDF: `clymer2024poser.pdf` in this folder (git-ignored). Full text: `clymer2024poser.md`.  
- LaTeX: `\parencite{clymer2024poser}` / `\textcite{clymer2024poser}` against `bib.bib`.
