# Language Models Can Control Their Own Attention

**Authors:** Namgyu Ho, Huzama Ahmad, Woosung Koh, Se-Young Yun, Tal Schuster, Cicero Nogueira dos Santos  
**Year:** 2026  
**Venue:** arXiv preprint (KAIST AI, Google DeepMind; Google co-authors advisory only)  
**Citation key:** `ho2026declarative_attention`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [arXiv](https://arxiv.org/pdf/2609.02737)  
**arXiv:** 2609.02737  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026)

## Summary

Introduces **Declarative Attention (DA)**, an inference-time protocol in which the model declares — inside its own chain-of-thought — which parts of the context it will attend to. Generation is partitioned into three tagged modes: `<global>` (attends to all context segments, used for navigation), `<focus magic_chunks="K">` (attends only to named segments), and `<local>` (attends only to its own output so far). A **DA state machine** running alongside the inference engine parses these tags like tool calls and rewrites the KV-cache block table at each decode step, so most of the KV cache is never read. Because the attention mask is read off the model's generated text rather than approximated from activations, the per-step `O(N)` selection cost of prior sparse-attention methods is eliminated entirely; `O(N)` reads remain only during declared global phases.

Evaluated zero-shot (no training) on off-the-shelf Gemma-4-31B and Qwen-3.6-27B across 15 long-context tasks drawn from RULER, LongBench v1/v2, LooGLE, and ZeroScrolls: DA reduces average attended tokens during decoding by 52.0% / 31.1% with accuracy drops of 1.27pp / 2.75pp, shrinking with model scale (4B → 31B) and growing in absolute terms with context length (up to ~21M tokens saved per response; up to 98–99% per-step attention read saved at >128K contexts in focus/local steps). A vLLM integration with block-aligned, in-place masking (compatible with FlashAttention, no kernel changes) yields a roofline-projected decode wall-time of 0.71× (Gemma) and 0.77× (Qwen) vs. vanilla.

## Key concepts

- **Declarative Attention (DA)** — attention scope declared in text via `<global>` / `<focus>` / `<local>` tags; the mask is legible, human-readable structure rather than an inferred activation pattern.  
- **Magic chunks** — addressable ~2K-token context segments delivered in a simulated `get_magic_chunk` tool-use transcript, so segment boundaries land on special tokens the model already tracks from post-training.  
- **Intrinsic vs. extrinsic sparsity** — prior sparse attention predicts attention-heavy tokens via proxy scores (`O(N)` per step); DA has the model state its attention plan, removing the selection cost.  
- **DA state machine** — decode-time parser that transitions on tag closings and applies a block-aligned attention mask (rounded outward to KV-cache block boundaries) by rewriting the request's block table in vLLM.  
- **Roofline wall-time analysis** — global-attention KV reads dominate decode time (73–86% of roofline decode time on benchmark traces; up to 94–97% on recent architectures at 1M-token contexts); DA trades ~1/3 more decode steps for lower per-step cost.  
- **Zero-shot as a floor** — all results are prompting-only; authors argue post-training on the protocol itself and naturally addressable agentic segments (tool calls, turns) are the headroom.

## Notes

- Closest prior work: Jin et al. 2024 trained the behavior per-task within 2K contexts; DA elicits it zero-shot across ~100K-token tasks under one fixed prompt.  
- Applies only to global-attention layers; sliding-window and linear-attention layers are untouched.  
- Conceptually adjacent to tool-use / CoT-as-interface work: turns "where to attend" into an explicit, inspectable declaration — relevant to legibility of reasoning traces.  
- Limitations acknowledged: suboptimal zero-shot decomposition, manufactured segments for static benchmarks, and thinking-tag protocol adherence.
