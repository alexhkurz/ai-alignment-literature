# Fact check: background reader

Checked [background-reader.md](background-reader.md) against the paper (`../ho2026declarative_attention.txt`, arXiv:2609.02737v1) and, for background claims, against the cited literature. The reader was distilled from the gitignored chat transcript, so the transcript contains the same errors; it was not checked separately.

Line numbers refer to `background-reader.md` as of 2026-10-14.

## Summary

| Section | Verdict |
| :--- | :--- |
| 1. The problem | Sound. One wrong citation, one complexity slip. |
| 2. Chain-of-thought | **Two substantive errors**: Wei et al. were not zero-shot; hidden state *does* persist via the KV cache. |
| 3. LLM self-knowledge | **Weakest section.** Calibration literature partly misdescribed; the Kahneman–Klein task mapping uses wrong numbers; "declarations correct 97–99%" confuses parse success with correctness. |
| 4. How DA works | Accurate. Every number checked matches the paper. |
| 5. Experiments | Mostly accurate; four wrong numbers (qmsum and quality on Qwen, token share by size, "~1M-token" contexts) and invented task examples. |
| 6. Synthesis | Engineering reading (6.2) accurate. Metacognitive reading (6.3–6.5) presents the reader's own argument as the paper's and repeats Section 3's errors. Omits that the failure cases are outside the 15 headline tasks. |
| 7. References | Fine as a list; several annotations repeat the errors above. |

**The paper never uses the word "metacognition"** (nor "introspection" or "self-knowledge"). Its own framing is *intrinsic vs. extrinsic* selection and *system-2 sparse attention* (§8.4), the latter following System 2 Attention (Weston & Sukhbaatar, 2023; paper footnote 2). Everything in the reader about calibration, introspection, Kahneman–Klein and "prospective self-knowledge" is the reader's interpretation and should be marked as such.

---

## A. Factual errors (fix)

1. **Wrong authors for Sparse Transformers** (l. 71). *Generating Long Sequences with Sparse Transformers* (2019) is by Child, Gray, Radford & Sutskever. "Weston and Sukhbaatar" wrote *System 2 Attention* (2023), the source of the paper's system-2 framing.

2. **Wei et al. (2022) was few-shot, not zero-shot** (l. 104, 216, 1121, 1203). Chain-of-thought prompting used worked exemplars in the prompt. "Let's think step by step" is Kojima et al. (2022), *Large Language Models are Zero-Shot Reasoners*. The analogy "DA is at the Wei et al. stage" should point to Kojima et al. if it is about zero-shot elicitation.

3. **"No persistent internal memory across forward passes"** (l. 138–140). False. The KV cache stores, for every earlier token and every layer, keys and values computed from that token's hidden state at that layer. Later tokens attend to these intermediate representations, not just to the token sequence. What is true: information flows only "upward and forward" (a token at layer ℓ reads earlier tokens' layer-ℓ keys/values; it cannot feed deep results back to shallow layers of earlier positions), which is one reason writing intermediate results as tokens helps. This matters for the talk: "CoT is the model's only working memory" is a stronger claim than the architecture supports.

4. **Decode-step overhead** (l. 116). DA runs 35% more decode steps on Gemma, 31% on Qwen (Fig. 2b), not "approximately 35%" in general.

5. **Guo et al. (2017) on weight decay** (l. 327). Reversed: Guo et al. found that *less* weight decay worsens calibration (the trend towards little or no weight decay is one cause of miscalibration). The "says 95%, right 74%" figure (l. 318, 325) could not be traced to the paper; drop it or cite the exact figure.

6. **Token-probability calibration "worsens with scale"** (l. 347). Contradicts Kadavath et al. (2022), who found larger pretrained models *well calibrated* on multiple-choice token probabilities, improving with scale; post-training (RLHF) is what degrades it (also the GPT-4 Technical Report). Kadavath et al. measured self-evaluation probabilities, P(True) and P(IK), not verbal hedges ("I'm fairly confident…"). Verbalized confidence is studied by Lin, Hilton & Evans (2022) and Xiong et al. (2024), the latter finding it typically *over*confident.

7. **Lightman et al. (2023)** (l. 220, 359). They show process supervision beats outcome supervision for training reward models on MATH. They do not show "better-calibrated reasoning".

8. **Band et al. (2024)** (l. 361). *Linguistic Calibration of Long-Form Generations* is a training method (supervised fine-tuning, then RL with a decision-based reward), not a CoT prompting technique.

9. **"98.5% retention means the declaration was correct on 98.5% of questions"** (l. 377, also l. 375, 1051, 1079). Wrong in two ways. (a) 98.5% is the ratio of DA accuracy to vanilla accuracy (85.74 / 87.01), not a per-question rate. (b) A wrong declaration does not force a wrong answer: the model can return to `<global>` and focus again (1.4–1.9 focus attempts per response, Fig. 6b). Declarations are never scored individually in the paper.

10. **"Declarations correct at a rate of 97–99%"** (l. 389). This is the **focus success rate**: the fraction of `<focus>` calls that *parse to a valid chunk reference* (Fig. 6a: 99% at the largest models). It measures protocol compliance, not whether the declared chunk contains the answer.

11. **Kahneman–Klein task mapping uses wrong numbers** (l. 412–444):
    - "Passkey: 0pp drop": true on Gemma only; Qwen's NIAH tasks drop to 97.7, 96.1 and 94.5.
    - "Meeting transcript QA: 0pp": Gemma only; Qwen drops 5.5pp (96.9 → 91.4).
    - "space_digest: 2.4pp, largest in the study": false. On Gemma, dialogue_history (−5.1), summarization (−4.7) and shortdep_cloze (−4.7) drop more.
    - "Long-dependency QA: 1.8pp drop": false. Gemma *improves* 3.2pp (65.6 → 68.8); Qwen drops 1.5pp.
    - The "feedback" condition (l. 403, 462) does not apply: DA is zero-shot, so the model receives no feedback and learns nothing from its declarations.

12. **qmsum** (l. 820–824). Qwen DA is 91.4%, not 97.7% ("no drop" holds for Gemma only). The QA for this source is synthetic (generated with Gemini-3-Flash, Table 1), not the original QMSum queries.

13. **quality** (l. 878). Qwen DA is 94.4%, not 88.9% (no drop on either model is correct).

14. **space_digest "largest proportional drop in the study"** (l. 884). True on Qwen (−10%), false on Gemma (dialogue_history −6.6% vs space_digest −5.6%).

15. **Token share by model size** (l. 982). Gemma models attend 46–48% of vanilla (excluding the 12B artefact); Qwen models attend 50–69% (Fig. 3b), not "46–50% in both families".

16. **"~1M-token" contexts** (l. 835–837, 1257). Table 1 reports a *source* mean of 1,071.1K tokens for code_repo, but every example longer than 244K tokens is excluded (116K for Gemma-4-E4B; §4, App. D.1). Evaluated contexts are at most 244K.

17. **"Six orders of magnitude in content type and three orders of magnitude in context length"** (l. 1053). Content type has no magnitude; evaluated contexts range from about 6K to 244K tokens, under two orders of magnitude.

18. **FlashAttention and the roofline** (l. 1170). FlashAttention (Dao et al., 2022) is about IO-aware tiling of exact attention; it did not introduce the roofline framing. The roofline model is Williams, Waterman & Patterson (2009), correctly listed next.

19. **System-2 framing source** (l. 1091–1093). The paper's footnote 2 says the framing follows *System 2 Attention* (Weston & Sukhbaatar, 2023), which itself borrows from dual-process theory. Worth citing for the psychologists: it is the direct ML precedent.

## B. Interpretation presented as the paper's claim (mark or soften)

1. **"The engineering result is the consequence of the metacognitive claim being true"** (l. 286, 1077–1085, bridge paragraphs l. 466, 1149). The reader's own argument. The paper claims the model can declare where to attend and that this preserves accuracy; it does not claim self-knowledge or introspection.

2. **"Calibration research has sought and failed … DA achieves it"** (l. 458–462). Overclaim: DA does not measure or improve confidence at all.

3. **"The Kahneman–Klein framework predicts the pattern of DA results almost exactly"** (l. 407, 934, 1239). The single-span vs. multi-span split is the paper's own task taxonomy, chosen in advance; mapping it to "regular vs. irregular environments" is post hoc, and the per-task numbers used to support it are partly wrong (A.11).

4. **"Improvement with scale is most pronounced on regular-environment tasks"** (l. 450). No per-task scaling results appear in the paper; unsupported.

5. **The scaling argument for self-knowledge** (l. 1067, 1109). Section 5.7 of the reader itself attributes the small-model failure largely to protocol adherence (58% focus success at Gemma-4-E4B). Monotone scaling therefore says at least as much about instruction-following as about self-knowledge.

6. **"Accuracy would collapse to near zero" with random declarations** (l. 1079). Untested; the model can re-declare.

7. **"Improving efficiency necessarily involves improving the model's self-knowledge"** (l. 1083). Efficiency can also improve through fewer global steps, better segmentation or an in-context index (all proposed in the paper).

8. **"Frontier models"** (l. 282, 739, 996, 1013). Gemma-4-31B and Qwen-3.6-27B are mid-size open-weight models; the paper's "frontier" refers to larger models used only in the roofline illustrations.

9. **"Wall-clock savings / speedups of 0.71× and 0.77×"** (l. 282, 996). These are roofline *estimates* of decode time relative to vanilla (lower is better), not measured wall-clock times and not speedups. Section 5.5 of the reader states this correctly.

10. **Self-consistency as evidence** (l. 210, 1206). Self-consistency plays no role in the paper, and DA's results across 15 tasks are not evidence of "genuine self-knowledge" by that principle.

11. **Speculative explanations stated as fact**: Qwen's multikey_3 drop "reflects focusing on an adjacent key" (l. 810); "the model uses global mode more than necessary" (l. 1123); agentic segments "would be more accurate" (l. 1125: argued by the paper, not tested).

## C. Omissions worth adding

1. **The failure cases are outside the headline suite** (l. 1139–1145). Appendix D.4 analyses six *further* sources (cwe, structured_data, fwe, summ_screen_fd, book_sum_sort, in_context_learning), on Gemma-4-31B only, where DA either loses accuracy (cluster mean 84.2 → 58.8%) or inflates attended tokens (17.8 → 21.2M). Some sources (ruler_qa_1/2) were skipped entirely because their prompts forbid intermediate reasoning. The 15 headline sources were chosen as tasks "where selective attention is particularly relevant" (§4). This belongs in the skeptical points of the talk.

2. **Four of the 15 sources use synthetic QA** generated by Gemini-3-Flash (qmsum, multidoc_qa, LooGLE summarization, singledoc_qa; Table 1).

3. **Task examples are invented.** The example questions for qmsum, code_repo, dialogue_history, longdep_qa, shortdep_cloze, quality and space_digest (l. 822, 836, 842, 856, 862, 876, 882) are illustrative, not from the datasets; mark them as such. For space_digest, the original ZeroSCROLLS task asks for the percentage of positive reviews (to be checked against the dataset if used on a slide).

## D. Minor

- l. 41: without a cache each step recomputes the whole prefix (quadratic attention per step); with it each step is linear in context. The text mixes per-step and total cost.
- l. 63: 73% / 86% are shares of *roofline* decode time (Table 3), not measured wall-clock time.
- l. 460, 1245: the "90% confidence intervals contain the truth only 40–60% of the time" finding is usually attributed to Alpert & Raiffa (1982) and Lichtenstein, Fischhoff & Phillips (1982); Fischhoff, Slovic & Lichtenstein (1977) studied judgments stated with extreme certainty. Check before citing.
- l. 1027: "the intrinsic quadrant was essentially empty": the paper lists SSAS and AutoPASTA as self-declared attention (App. A.5); "sparsely populated" is fairer.

## What checks out

Section 4 in full (protocol, scaffold, magic chunks, segmentation, state machine transitions, 16-token sink, block alignment, 10/50 and 16/48 layer splits, 81,920 B/token, 838.9 MB and 78.45 MB local reads, 42% / 5% shares); Section 5.2 (three arms); 5.4 (judge: Gemini-3-Flash rubrics, Qwen-3.5-4B judge, 2,993 responses, 98.53% agreement, κ = 0.940, r = 0.992, McNemar p = 0.65, 24/20); 5.5; the DAnm ablation numbers (l. 922–926); the 7/15 and 5/15 counts; category averages; Table 3 decomposition; scaling 29/91/99 and 64/89/97; Gemma-4-12B 183% / 98%; context-length binning; 6.2 (SparQ 1.3–3.0×, Double Sparsity, reversibility, speculative decoding, offloading); appendix pointers in 7.3.

## References (fact check)

- Child, Gray, Radford, Sutskever: [Generating Long Sequences with Sparse Transformers](https://scholar.google.com/scholar?q=Generating+Long+Sequences+with+Sparse+Transformers+Child+2019), 2019.
- Weston, Sukhbaatar: [System 2 Attention (is something you might need too)](https://scholar.google.com/scholar?q=System+2+Attention+is+something+you+might+need+too+Weston+Sukhbaatar+2023), 2023.
- Kojima, Gu, Reid, Matsuo, Iwasawa: [Large Language Models are Zero-Shot Reasoners](https://scholar.google.com/scholar?q=Large+Language+Models+are+Zero-Shot+Reasoners+Kojima+2022), 2022.
- Wei et al.: [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://scholar.google.com/scholar?q=Chain+of+Thought+Prompting+Elicits+Reasoning+Large+Language+Models+Wei+2022), 2022.
- Guo, Pleiss, Sun, Weinberger: [On Calibration of Modern Neural Networks](https://scholar.google.com/scholar?q=On+Calibration+of+Modern+Neural+Networks+Guo+2017), 2017.
- Kadavath et al.: [Language Models (Mostly) Know What They Know](https://scholar.google.com/scholar?q=Language+Models+Mostly+Know+What+They+Know+Kadavath+2022), 2022.
- OpenAI: [GPT-4 Technical Report](https://scholar.google.com/scholar?q=GPT-4+Technical+Report+OpenAI+2023), 2023. - - - Calibration of the pretrained vs. post-trained model.
- Lin, Hilton, Evans: [Teaching Models to Express Their Uncertainty in Words](https://scholar.google.com/scholar?q=Teaching+Models+to+Express+Their+Uncertainty+in+Words+Lin+Hilton+Evans+2022), 2022.
- Xiong et al.: [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://scholar.google.com/scholar?q=Can+LLMs+Express+Their+Uncertainty+Empirical+Evaluation+Confidence+Elicitation+Xiong+2024), 2024.
- Lightman et al.: [Let's Verify Step by Step](https://scholar.google.com/scholar?q=Let%27s+Verify+Step+by+Step+Lightman+2023), 2023.
- Band, Li, Ma, Hashimoto: [Linguistic Calibration of Long-Form Generations](https://scholar.google.com/scholar?q=Linguistic+Calibration+of+Long-Form+Generations+Band+2024), 2024.
- Williams, Waterman, Patterson: [Roofline: An Insightful Visual Performance Model for Multicore Architectures](https://scholar.google.com/scholar?q=Roofline+Insightful+Visual+Performance+Model+Multicore+Architectures+Williams+2009), 2009.
- Alpert, Raiffa: [A Progress Report on the Training of Probability Assessors](https://scholar.google.com/scholar?q=Alpert+Raiffa+A+progress+report+on+the+training+of+probability+assessors), 1982.
- Lichtenstein, Fischhoff, Phillips: [Calibration of Probabilities: The State of the Art to 1980](https://scholar.google.com/scholar?q=Lichtenstein+Fischhoff+Phillips+Calibration+of+probabilities+state+of+the+art+to+1980), 1982.
- Shaham et al.: [ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding](https://scholar.google.com/scholar?q=ZeroSCROLLS+Zero-Shot+Benchmark+Long+Text+Understanding+Shaham+2023), 2023. - - - SpaceDigest task definition.
