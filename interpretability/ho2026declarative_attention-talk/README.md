# Talk: *Language Models Can Control Their Own Attention*

Presentation materials for [`ho2026declarative_attention`](../ho2026declarative_attention.md) (Ho et al., 2026, [arXiv:2609.02737](https://arxiv.org/abs/2609.02737)).

Slides are written in HackMD Markdown (reveal.js) here and pasted into HackMD; images are uploaded to HackMD by hand.

## Contents

- `slides.md` — HackMD slide deck
- `example-niah_single_1.md` — one RULER `niah_single_1` (passkey) item, as a plain prompt and under DA
- `slides-narrative.md` — the full story behind each slide (what to say, numbers, caveats, transitions)
- `slides-commentary.md` — questions on the slides, with answers and references
- `background-reader.md` — background reader, Sections 1–7 (extracted from the chat transcript below)
- `background-reader-factcheck.md` — fact check of the reader against the paper and literature
- `Declarative_Attention_Protocol_Explained.md` — (local only, gitignored) exported chat (claude-sonnet-4-6): abstract line by line, Q&A, reader drafting
- `images/` — figure and table crops from the paper (local only, gitignored; regenerate with `./make-images.sh`)
- `make-images.sh` — renders paper pages at 200 dpi and crops the figures

## Images

| File | Source in paper |
|------|-----------------|
| `example-acme.png` | §2 — the Acme Corp example response (global → focus → global → focus → local → answer) |
| `fig1-protocol.png` | Fig. 1 — global / focus / local example and the resulting attention mask |
| `table2-main-results.png` | Table 2 — accuracy and attended tokens, 15 tasks, Gemma-4-31B and Qwen-3.6-27B |
| `fig2-masking-vs-length.png` | Fig. 2 — savings come from masking, not shorter generation |
| `fig3-model-scale.png` | Fig. 3 — accuracy and attended tokens by model size |
| `fig4-context-length.png` | Fig. 4 — accuracy and token delta by context length |
| `table3-wall-time.png` | Table 3 — roofline decode wall-time estimate |
| `fig5-mode-share.png` | Fig. 5 — token share per mode; per-token savings of focus and local |
| `fig6-focus-adherence.png` | Fig. 6 — focus success rate and attempts by model size |
| `prompt-soft-requirements.png` | App. F — the DA instruction's three "soft requirements", written from observed failure modes |
