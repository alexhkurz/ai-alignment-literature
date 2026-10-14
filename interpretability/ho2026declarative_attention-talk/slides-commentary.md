# Commentary on the slides

Questions raised while building [slides.md](slides.md), with answers. Newest at the bottom.

---

## Contents

- [Q1. What is "global attention"?](#q1-what-is-global-attention)
- [Q2. Shouldn't View A be about optimizing the KV cache?](#q2-shouldnt-view-a-be-about-optimizing-the-kv-cache)
- [Q3. Would "One Result, Two Readings" work better as a conclusion slide?](#q3-would-one-result-two-readings-work-better-as-a-conclusion-slide)
- [Q4. Are slides 1–4 good so far?](#q4-are-slides-14-good-so-far)
- [Q5. Does the narrative explain "what is computed next" vs. "what is read next", and "visible" vs. "executable"?](#q5-does-the-narrative-explain-what-is-computed-next-vs-what-is-read-next-and-visible-vs-executable)
- [Q6. Does the revised CoT → DA table work?](#q6-does-the-revised-cot--da-table-work)
- [Q7. Is "the inference engine reads DA and changes $QK^\top$" correct?](#q7-is-the-inference-engine-reads-da-and-changes-qktop-correct)
- [Q8. Isn't adding a mask the same as setting entries of $QK^\top$ to $0$ or $-\infty$?](#q8-isnt-adding-a-mask-the-same-as-setting-entries-of-qktop-to-0-or--infty)
- [Q9. On an "Idea" slide, is "the engine changes $QK^\top$" acceptable, since implementation comes later?](#q9-on-an-idea-slide-is-the-engine-changes-qktop-acceptable-since-implementation-comes-later)
- [Q10. Can I avoid the KV cache, or downplay it to a technical detail?](#q10-can-i-avoid-the-kv-cache-or-downplay-it-to-a-technical-detail)
- [Q11. Are the CoT and Idea slides ok now? And is the thesis mine or the paper's?](#q11-are-the-cot-and-idea-slides-ok-now-and-is-the-thesis-mine-or-the-papers)
- [Q12. Understanding the example (Fig. 1)](#q12-understanding-the-example-fig-1)
- [Q13. Who breaks the context into magic chunks?](#q13-who-breaks-the-context-into-magic-chunks)
- [Q14. Are magic chunks essential, or just for reporting? How would DA work in practice?](#q14-are-magic-chunks-essential-or-just-for-reporting-how-would-da-work-in-practice)
- [Q15. Is the segmenter part of DA, and DA part of a modified vLLM?](#q15-is-the-segmenter-part-of-da-and-da-part-of-a-modified-vllm)
- [Q16. What should I call the side of DA that is not the state machine?](#q16-what-should-i-call-the-side-of-da-that-is-not-the-state-machine)
- [Q17. How should I explain the meaning of global, focus and local?](#q17-how-should-i-explain-the-meaning-of-global-focus-and-local)
- [Q18. Is global ordinary CoT, focus a tool call that erases data from the KV cache, and what is the difference between focus and local?](#q18-is-global-ordinary-cot-focus-a-tool-call-that-erases-data-from-the-kv-cache-and-what-is-the-difference-between-focus-and-local)
- [Q19. How does focus "hide" chunks, and what does "no chunks visible" mean for `<local>2011 - 2003 = 8 years.</local>`?](#q19-how-does-focus-hide-chunks-and-what-does-no-chunks-visible-mean-for-local2011---2003--8-yearslocal)
- [Q20. How do I read and explain the Results slide?](#q20-how-do-i-read-and-explain-the-results-slide)
- [Q21. Where do I see how many tokens were saved? An example.](#q21-where-do-i-see-how-many-tokens-were-saved-an-example)
- [Q22. What is DA^nm vs. DA?](#q22-what-is-danm-vs-da)
- [Q23. What is the difference between single-span and multi-span?](#q23-what-is-the-difference-between-single-span-and-multi-span)
- [Q24. Does the paper have single-span and multi-span examples to inspect?](#q24-does-the-paper-have-single-span-and-multi-span-examples-to-inspect)
- [Q25. What do the three charts of Fig. 2 show?](#q25-what-do-the-three-charts-of-fig-2-show)
- [Q26. What does "relative" mean in "relative decode steps", and why does it matter?](#q26-what-does-relative-mean-in-relative-decode-steps-and-why-does-it-matter)
- [Q27. Is the estimated decode time (0.71× / 0.77×) visible in the charts?](#q27-is-the-estimated-decode-time-071--077-visible-in-the-charts)
- [Q28. What does the Scale slide (Fig. 3) show?](#q28-what-does-the-scale-slide-fig-3-show)
- [Q29. Why does Gemma-4-12B read more than vanilla (183%), more than the 4B and 31B models?](#q29-why-does-gemma-4-12b-read-more-than-vanilla-183-more-than-the-4b-and-31b-models)
- [Q30. What does "only its own notes" mean for `<local>`?](#q30-what-does-only-its-own-notes-mean-for-local)
- [Q31. What is the difference between global and local, if both are added to the context? Are no new KV values computed in local mode?](#q31-what-is-the-difference-between-global-and-local-if-both-are-added-to-the-context-are-no-new-kv-values-computed-in-local-mode)
- [Q32. Should I read the mask in Fig. 1 as a picture of what can attend to what?](#q32-should-i-read-the-mask-in-fig-1-as-a-picture-of-what-can-attend-to-what)
- [Q33. Where do the results show the difference between focus and local?](#q33-where-do-the-results-show-the-difference-between-focus-and-local)
- [Q34. For my message the focus/local difference seems unimportant. Is there something I should say?](#q34-for-my-message-the-focuslocal-difference-seems-unimportant-is-there-something-i-should-say)

---

## Q1. What is "global attention"?

*Slide: The Problem.*

**Short answer.** It is a term of art, used by the paper and by the model architectures it runs on. A **global attention layer** is an ordinary full (causal) self-attention layer: each new token attends to *every* earlier token, so the layer must read the whole KV cache at every decode step. "Global" contrasts it with the cheaper layer types that modern models mix in.

**Why the qualifier is needed.** Recent models are *hybrid*: most layers no longer attend to the full context.

| Layer type | Each new token reads | Per-step cost grows with context? |
| :--- | :--- | :--- |
| Global (full) attention | all earlier tokens | yes |
| Sliding-window attention (SWA), "local" layers | the last $w$ tokens only | no (bounded by $w$) |
| Linear attention / recurrent (e.g. Gated DeltaNet) | a fixed-size state summarising the past | no |

The two models in the paper:

- **Gemma-4-31B**: 50 of 60 layers are sliding-window with a 1,024-token window; the other 10 are global.
- **Qwen-3.6-27B**: the non-global layers are Gated DeltaNet (GDN), a linear-attention variant with a recurrent state.

**What Gated DeltaNet is.** Gated DeltaNet (Yang, Kautz & Hatamizadeh, 2025) is a linear-attention layer: instead of storing one key–value pair per past token, it keeps a single fixed-size matrix $S_t$ (a "fast-weight" associative memory, $d_k \times d_v$) and reads it with the query, $o_t = S_t^\top q_t$. Each new token writes its value $v_t$ under its key $k_t$ by the **delta rule**, $S_t = \alpha_t\,(I - \beta_t k_t k_t^\top)\,S_{t-1} + \beta_t\, k_t v_t^\top$: the term $-\beta_t k_t k_t^\top S_{t-1}$ first erases what was stored under $k_t$, so the memory corrects its prediction for that key instead of piling up entries; $\beta_t \in (0,1)$ is a learned write strength, and the **gate** $\alpha_t \in (0,1)$ is a learned decay (taken from Mamba2) that lets the layer forget quickly when the context changes. The delta rule is the Widrow–Hoff error-correcting update, i.e. Rescorla–Wagner learning in psychology, and reading DeltaNet as a fast-weight programmer goes back to Schlag, Irie & Schmidhuber (2021). For DA the point is cost: each step reads a state of fixed size, however long the context, so there is no KV cache to mask, but also no exact recall of a token far back; that is why hybrids keep a few global layers.

DA masks only the global layers, because only they have a per-step cost that grows with context length (paper, §2.3 "Scope and tradeoffs" and Appendix B). The SWA and GDN layers are untouched. This is also why the wall-time saving is smaller on Gemma: the SWA reads that DA cannot reduce account for 42% of DA's attention time there, against 5% for GDN on Qwen (paper, §5.4).

**Where the vocabulary comes from.** The global vs. local (sliding-window) terminology is standard in model reports, e.g. Gemma 3's interleaving of local and global attention layers (Gemma Team, 2025). One older usage differs: in Longformer (Beltagy et al., 2020), "global attention" means a few *selected tokens* (such as a classification token) that attend to, and are attended by, all tokens, inside an otherwise sliding-window layer. In the DA paper, "global" is a property of a *layer*, not of individual tokens.

**A name clash in the DA paper.** The DA *mode* names reuse these words with a different meaning:

- `<global>` mode: the model reads the whole context (inside the global layers).
- `<local>` mode: the model reads only the scaffold and its own response so far.

The `<local>` *mode* has nothing to do with *local (sliding-window) layers*. Both kinds of "local" occur in the same paper, e.g. Table 3's "Local Memory" column means the SWA/GDN read, not `<local>` mode.

**For the slides.** Say "full-attention layers (the paper: *global* attention layers)" once, and warn the audience that the `<global>` / `<local>` modes are a different use of the same words. For a mixed audience, "full attention" is the clearer term.

**References (Q1)**

- Ho, Ahmad, Koh, Yun, Schuster, dos Santos: [Language Models Can Control Their Own Attention](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026), 2026. - - - §2.3 (scope: global layers only), §5.4 and Table 3 (wall time), Appendix B.
- Beltagy, Peters, Cohan: [Longformer: The Long-Document Transformer](https://scholar.google.com/scholar?q=Longformer+The+Long-Document+Transformer+Beltagy+2020), 2020. - - - Sliding-window attention; "global attention" on selected tokens.
- Gemma Team: [Gemma 3 Technical Report](https://scholar.google.com/scholar?q=Gemma+3+Technical+Report+2025), 2025. - - - Interleaved local (sliding-window) and global attention layers.
- Gemma Team: [Gemma 4 Technical Report](https://scholar.google.com/scholar?q=Gemma+4+Technical+Report+2026), 2026. - - - The Gemma-4 models used in the paper.
- Yang, Kautz, Hatamizadeh: [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://scholar.google.com/scholar?q=Gated+Delta+Networks+Improving+Mamba2+with+Delta+Rule), 2025. - - - Gated DeltaNet.
- Yang, Wang, Zhang, Shen, Kim: [Parallelizing Linear Transformers with the Delta Rule over Sequence Length](https://scholar.google.com/scholar?q=Parallelizing+Linear+Transformers+with+the+Delta+Rule+over+Sequence+Length), 2024. - - - DeltaNet, trainable at scale.
- Schlag, Irie, Schmidhuber: [Linear Transformers Are Secretly Fast Weight Programmers](https://scholar.google.com/scholar?q=Linear+Transformers+Are+Secretly+Fast+Weight+Programmers), 2021. - - - Linear attention as fast-weight memory; the delta-rule update.
- Gu, Dao: [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://scholar.google.com/scholar?q=Transformers+are+SSMs+Generalized+Models+and+Efficient+Algorithms+Through+Structured+State+Space+Duality), 2024. - - - Mamba2, source of the decay gate.
- Widrow, Hoff: [Adaptive Switching Circuits](https://scholar.google.com/scholar?q=Widrow+Hoff+Adaptive+Switching+Circuits+1960), 1960. - - - The delta (LMS) rule.
- Rescorla, Wagner: [A Theory of Pavlovian Conditioning: Variations in the Effectiveness of Reinforcement and Nonreinforcement](https://scholar.google.com/scholar?q=Rescorla+Wagner+A+theory+of+Pavlovian+conditioning+1972), 1972. - - - The same error-correcting update in learning theory.

---

## Q2. Shouldn't View A be about optimizing the KV cache?

*Slide: Big Questions.*

**Short answer.** No. The slide puts two different distinctions next to each other, and they are easy to merge:

| Distinction | About | The two sides |
| :--- | :--- | :--- |
| Two **readings** of the paper | what kind of contribution the paper makes | engineering (fewer KV-cache reads) vs. metacognitive (what models know about where information is) |
| Two **views** of the model | how the model produces its declarations | View A: pattern matching on surface cues vs. View B: something like metacognition |

The first is the slide "One Result, Two Readings". The second is a general debate about language models that came up in the earlier chat as an answer to "is this paper about optimization or about the nature of thinking?", which is why the two got paired.

**How they relate.** The engineering reading is *neutral* between View A and View B. The KV-cache saving needs only that the declarations are good enough; it does not care how they were produced. A model that picks chunk 1 because the question says "supervised fine-tuning" and chunk 1 contains a section headed "Supervised fine-tuning" saves exactly as many tokens as a model with a representation of its own knowledge state. View A vs. View B is a question *inside* the metacognitive reading: given that the declarations work, what kind of process produces them?

**A subtlety that favours View A.** The declarations are not made blind. In Fig. 1 the model declares "Magic Chunks 1 contains the 'Supervised fine-tuning' section" while in `<global>` mode, i.e. while attending to the *whole* context. So "knowing where to look" happens after a full read; the declaration is prospective only relative to the later `<focus>` and `<local>` steps, not relative to reading the document. The Fig. 1 example is, on its face, header matching. This weakens the "prospective self-knowledge" framing of the background reader (§3.4) and belongs on the Skeptical Points slide.

**What would separate View A from View B.** Experiments the paper does not run:

- remove surface cues (strip headers, paraphrase the question so it shares no keywords with the relevant chunk) and see whether declarations stay accurate;
- in the no-mask arm, compare the declared chunks with where the model's attention actually goes;
- probe the residual stream for "which chunk holds the answer" *before* the model writes its declaration (see the Bridges slide).

**Suggested change to the slide.** Ask the two questions in order: first "optimization or nature of thinking?" (the two readings), then, for the second reading, "pattern matching or metacognition?" (View A / View B). And add the global-mode point to Skeptical Points.

---

## Q3. Would "One Result, Two Readings" work better as a conclusion slide?

*Slide: One Result, Two Readings.*

**Short answer.** Yes, the table and the quote; but keep the thesis up front.

**Why the table belongs at the end.**

- **Cognitive load.** At slide 3 most rows use words the audience has not met yet: KV cache, vLLM, block-aligned masking, system-2 sparse attention, 15 tasks. A table of unfamiliar terms is read as noise. At the end every row points back to a slide they have seen, so the table becomes a recap that costs nothing to read.
- **It is a summary.** "What the paper is, at five levels" is a verdict on the paper. Verdicts come after the evidence.
- **The quote is the paper's own conclusion** ("from a pattern inferred inside the network into one the model states out loud"). It reads as a punchline only once the audience has seen Fig. 1 and the mask.
- **The Scientific row can be stated honestly** at the end, after the self-knowledge slides, as "evidence, with the caveats on the next slide".

**Why the thesis stays at the start.** The thesis tells the audience what to listen for: watch the efficiency numbers, because they will be read as a test of a metacognitive claim. Without it, the engineering slides look like a detour for the psychologists and philosophers. It fits as one line on the Big Questions slide, under the two views.

**Where to put the conclusion.** Before Skeptical Points:

… → Bridges → **Conclusion** (table + quote) → Skeptical Points → Discussion

Claims first, then caveats, then open questions; the skeptical points stay near the end, as planned. Restating the thesis on the conclusion slide closes the loop: "the efficiency result was a behavioural test; here is what it does and does not show".

---

## Q4. Are slides 1–4 good so far?

*Slides: Title, Big Questions, One Result, Two Readings, The Problem (state of 2026-10-14).*

**Title, Big Questions.** Good. The two views are short and concrete, and the abstract's question frames them. If the table moves to the conclusion (Q3), add the thesis as one line here: "Thesis: the efficiency result is a behavioural test of a metacognitive claim."

**One Result, Two Readings.** Fine as it stands, but see Q3: it works better as the conclusion.

**The Problem.** Three fixes:

1. **"(sparse attention)" names the wrong thing.** That the model attends to a small part of its context is *attention sparsity* ("attention is sparse"). *Sparse attention* is the family of methods that exploit it. Suggest: "But the model only attends to a small part of its context: attention is **sparse**."
2. **The punchline is missing.** The problem DA solves is not only that reading is expensive, but that existing sparse-attention methods still pay for it: to know what to skip, they scan a summary of the whole cache at every step. Without this bullet the audience will ask "why not just use sparse attention?" Suggest a fourth bullet: "Existing sparse-attention methods guess what to skip, but the guess itself scans everything."
3. **"KV cache" is no longer introduced,** but the next two slides use it. Suggest: "reads the stored keys and values of all previous tokens (the **KV cache**)."

Minor: double space after "global attention layer".

---

## Q5. Does the narrative explain "what is computed next" vs. "what is read next", and "visible" vs. "executable"?

*Slide: From Chain-of-Thought to Declarative Attention.*

It did not; it only restated the table. The narrative section now explains both rows. In short:

- **Computed vs. read.** CoT text acts *inside* the network: it is more context, the next token still reads the whole KV cache, and at most the soft attention weights shift. DA text is acted on *outside* the network: the engine removes the other chunks from what the next token reads. CoT changes weights; DA changes the hard set of what is read at all.
- **Visible vs. executable.** CoT text lets us read the reasoning, but has no effect except through the model and need not be faithful (Turpin et al., 2023). DA text has a fixed meaning to an interpreter, the engine, and takes effect whether or not it reflects anything inside the model. CoT is a comment; DA is code. That is why the efficiency result can serve as a test: a declaration that is executed can be wrong in a way that costs accuracy.

---

## Q6. Does the revised CoT → DA table work?

*Slide: From Chain-of-Thought to Declarative Attention, with the rows "Text is read by" and "Text changes: what the model computes next | what the model computes and what it sees".*

**Yes, and the new second row is more accurate than the earlier "computed vs. read".** DA text still acts as context, so it changes what the model computes, exactly like CoT; the mask adds a second effect on what the model sees. "Computes and sees" says that DA is CoT *plus* something, which is the right picture. "Sees" is also clearer for a mixed audience than "reads" or "attends to".

Two small suggestions:

- **Keep one word.** The Idea slide's table has the column "Attends to"; the narrative mostly says "reads". Pick "sees" or "reads" and use it on both slides, so the audience does not wonder whether these are different things. (The psychologists may hear "sees" as perception; that is acceptable here, and the Skeptical Points slide covers "attention ≠ attention".)
- **The dropped slogan row** carried the "visible vs. executable" point, which is what makes the efficiency result a test. If you want it on the slide, one line under the table does it: "CoT is a comment; DA is code." Otherwise say it; the narrative now marks it as spoken.

---

## Q7. Is "the inference engine reads DA and changes $QK^\top$" correct?

*Slides: From Chain-of-Thought to Declarative Attention (last line), Idea.*

**Almost.** The engine does not change $Q$, $K$ or their product. It adds a **mask** to the scores before the softmax:

$$\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right)V, \qquad M_{ti} = \begin{cases} 0 & \text{if token } i \text{ is declared visible} \\ -\infty & \text{otherwise.} \end{cases}$$

Since $e^{-\infty} = 0$, masked tokens get weight 0 and the softmax renormalizes over the rest. Two remarks make this the right formulation:

- **It is the standard form.** Causal attention already uses such a mask ($M_{ti} = -\infty$ for $i > t$: no looking ahead). DA makes the mask depend on what the model writes. For the audience: "DA doesn't change the formula; it changes the mask."
- **It is where the saving comes from.** The engine implements the mask by not loading the masked rows of $K$ and $V$ at all; equivalently, it restricts $K$ and $V$ to the declared rows. Changing $QK^\top$ after computing it would save nothing, since all of $K$ would already have been read.

The same applies to the line on the CoT slide: the engine does not change the attention mechanism, it changes what the mechanism reads (its mask).

**Suggested Idea slide:**

```markdown
## Idea

**Attention:** $\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$

**Declarative Attention:** the engine reads the declarations and adds a mask $M$:

$$\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right)V, \qquad M_{ti} = \begin{cases} 0 & i \text{ declared} \\ -\infty & \text{otherwise} \end{cases}$$

Masked keys and values are never read.
```

---

## Q8. Isn't adding a mask the same as setting entries of $QK^\top$ to $0$ or $-\infty$?

*Follow-up to Q7.*

**Yes for $-\infty$, no for $0$.**

- **Setting masked entries of $QK^\top/\sqrt{d_k}$ to $-\infty$** is exactly the same as adding $M$: same softmax, same output. So "the engine changes $QK^\top$" is mathematically correct if it means "sets the undeclared entries to $-\infty$". Q7 overstated the difference.
- **Setting them to $0$ is not the same.** A score of $0$ gives weight proportional to $e^0 = 1$, the same as any other token with score $0$; the token still contributes. Zeroing is right only *after* the softmax: set the masked weights $\alpha_{ti}$ to $0$ and renormalize the rest, which again equals the $-\infty$ version.

What remains of Q7 is about implementation, not mathematics: if the engine first computed all of $QK^\top$ and then overwrote entries, it would already have read every key, and nothing would be saved. DA's saving comes from never loading the masked keys and values. One formula, two implementations, only one of them cheap.

For the slide, either wording works: "sets undeclared entries of $QK^\top$ to $-\infty$" or "adds a mask $M$". The mask form has the advantage that the audience can compare it to the causal mask.

---

## Q9. On an "Idea" slide, is "the engine changes $QK^\top$" acceptable, since implementation comes later?

*Slide: Idea.*

**Yes.** At the level of the idea, the mathematics is what matters, and setting entries of $QK^\top$ to $-\infty$ is the mask. Two small points:

- **Say how it changes.** "Changes $QK^\top$" alone could mean anything. "Sets the entries of undeclared tokens to $-\infty$" (or "masks them") costs a few words and makes the idea precise, which matters for the mathematicians.
- **The saving still needs saying once.** The audience has just heard that reading the KV cache is the cost; an idea that only overwrites scores would not reduce it. One sentence on the next slide or in the spoken narrative closes the gap: "masked keys and values are never loaded".

---

## Q10. Can I avoid the KV cache, or downplay it to a technical detail?

**Yes, as a term; no, as an idea.**

**What the talk needs.** One fact: *for every new token, the model re-reads everything before it, and that reading is what makes long contexts slow.* Without it, "reads 52% less" means nothing and the engineering view has no problem to solve. The name "KV cache" and what it stores (keys and values per token and layer) are implementation detail; the AI experts know them, the rest of the audience does not need them.

**What the metacognition view needs.** Not the cache at all, only that the engine *enforces* the declaration: in focus mode the model cannot see the other chunks. The thesis rests on enforcement, not on memory traffic.

**Suggested wording.** Say once, in passing: "this memory of past tokens is called the KV cache", then never use the term again. Replacements for the current slides:

| Slide | Now | Instead |
| :--- | :--- | :--- |
| The Problem | "reads the stored keys and values of all previous tokens" | "re-reads all previous tokens" |
| The Idea | "masks the KV cache accordingly" | "hides the undeclared chunks" |
| Connection: First-Order Steering | "what the model *reads* (KV mask)" | "what the model *reads*" |
| Conclusion | "a way to read less of the KV cache during decoding" | "a way to read less of the context while generating" |

The Attention Mechanism slide can keep $k_i, v_i$: there they are just symbols in the formula, and the mathematicians will see that re-reading them for every $t$ is the cost.

The narrative keeps the KV cache in its Details paragraphs, for questions from the AI experts.

---

## Q11. Are the CoT and Idea slides ok now? And is the thesis mine or the paper's?

*Slides: From Chain-of-Thought to Declarative Attention, Idea, Big Questions.*

**CoT and Idea slides: yes.** "Changes the input to the attention mechanism" is accurate, and "changes $QK^\top$ (setting masked tokens to $-\infty$)" is the mask. One word: it is the *scores* of masked tokens, the entries of $QK^\top$, that are set to $-\infty$, not the tokens. Suggest "(setting the entries of masked tokens to $-\infty$)". Optionally "reads the declarations" instead of "reads DA".

**The thesis is yours.** The paper never claims anything about metacognition. Its own thesis (conclusion): a model "can control its own attention span in text a person can also read", turning selective attention "from a pattern inferred inside the network into one the model states out loud", with large savings at a small accuracy cost. That is an engineering claim with a legibility bonus.

Your thesis is a claim about how to *read* that result: because the engine enforces the declarations, the accuracy numbers test whether the model's statements about where to look are good. "Thesis of this talk" labels it correctly as yours. Two options to make the distinction visible to the audience:

- put both on the slide: **Paper:** a model can control its own attention, in text we can read. **This talk:** the efficiency result is a behavioural test of a metacognitive claim.
- or say it: "This is not the authors' claim; it is how I propose to read their result."

Keep in mind how strong the thesis is: the test is passed in a weak sense (the declarations are good enough to be enforced at a cost of 1–2 points). It does not show how the declarations are produced (Q2). The conclusion slide's "thesis revisited" in the narrative says this.

---

## Q12. Understanding the example (Fig. 1)

*Slide: Example.*

### What was in the context segments, and what does the question refer to?

The paper does not say which document Fig. 1 uses. The 12 segments (about 25K tokens) are evidently a technical report on training a language model: the question asks how many instruction–response pairs the final supervised fine-tuning (SFT) corpus contained after merging regenerated math solutions with open-domain conversations, and chunk 1 holds a section headed "Supervised fine-tuning". (A guess: it resembles the arXiv-paper source used for LooGLE/summarization, mean 21K tokens; not confirmed.) The audience needs only: "a long ML paper, cut into 12 chunks; a question about one number in it".

### Are R1, R2, R3 part of the model's response?

The *text* is; the *labels* are not. The model writes one continuous response containing the tags: `<global>…</global><focus magic_chunks="1">…</focus><local>…</local><answer>16,500</answer>`. "R1", "R2", "R3" and the bold headings ("Global mode for navigation", …) are the authors' annotations, naming the three passages so they can be rows of the mask.

### What does the Declarative Attention mask illustrate?

A table of who may read what:

- **Rows** are the three passages the model writes (R1, R2, R3): the "queries", i.e. the tokens doing the reading.
- **Columns** are the blocks that can be read: the system instruction A, the chunks B1–B12, the question C, the DA instruction D, and the model's own passages R1–R3.
- **Solid** boxes are read, **dashed** boxes are hidden. Blue = scaffold (always read), green = document chunks, grey = the response.

Read row by row: R1 (global) reads everything up to itself; R2 (focus) reads only A, B1 (marked F), C, D and the response so far; R3 (local) reads A, C, D and the response, no chunks. The staircase on the right is the ordinary causal rule: R1 cannot read R2, which does not exist yet.

### How should I understand what the model writes in each mode?

The prompt tells it (Appendix F, "DA Instruction Prompt"):

- **global:** "identify the next magic chunk to examine. Briefly explain why the magic chunk is relevant. Do not reason about the answer itself in global mode." So global text is a navigation note: *where* and *why*.
- **focus:** `<focus magic_chunks="K">VALUE</focus>`, where VALUE is "a name, number, date, or short noun phrase (typically 1 to 12 words)", pulled out verbatim. So focus text is an excerpt, not reasoning.
- **local:** reasoning over values already extracted, ending with "the single value … you will put inside `<answer>`". So local text is the calculation and the commitment.

The prompt also gives "soft requirements" (use at least one focus block, end with a local block, never recall chunk content in local mode) and lists typical orders, e.g. local → global → focus → local → answer ("plan, locate, extract, conclude"). For the metacognition question this matters: the *strategy* is spelled out in the prompt; what the model contributes is the choice of chunk.

A cleaner example from the paper (§2), worth showing as text before Fig. 1, because it has two navigation steps:

```
<global>I need the founding year and the IPO year. The company history
in Magic Chunk 2 should state the founding.</global>
<focus magic_chunks="2">"Acme Corp was founded in 2003 in San Jose."</focus>
<global>The IPO year is still missing. Magic Chunk 7 covers Acme's
financial milestones.</global>
<focus magic_chunks="7">"Acme Corp went public on the NYSE in 2011."</focus>
<local>2011 - 2003 = 8 years.</local>
<answer>8 years</answer>
```

### What is a magic chunk?

A piece of the long input, about 2,048 tokens (hard cap 2,560), cut at the most natural boundary available (paragraph, then line, sentence, clause, word). Chunks are numbered 1 to N and delivered as a *simulated tool-use conversation*: a user turn asks the assistant to retrieve the document one chunk at a time; each chunk then appears as an assistant call `get_magic_chunk` followed by a tool response headed "Magic Chunk N". No tool actually runs. Two reasons: the chunk boundaries fall on the special tokens that delimit tool messages, which the model tracks well from training; and the odd name, declared as "arbitrary retrieval splits", keeps the model from confusing chunks with the document's own sections (App. F).

### How does the DA state machine work?

A small program next to the inference engine that watches the model's output, token by token (§2.3):

1. It starts in global mode: all chunks visible.
2. When the model completes an opening tag, at the closing ">" of `<focus magic_chunks="K">` or `<local>`, it switches: from the next token on, only the scaffold, chunk K (or no chunk) and the response are read.
3. At `</focus>` or `</local>` it switches back to global.
4. `<global>` triggers nothing; global is the default, and the tag only helps the model keep track.

"Switching" means changing the list of memory blocks the next token reads, rounded to whole blocks, so standard attention code runs unchanged. Hidden blocks stay in memory, so going back to global is free.

### Do I need to explain all this?

Not all of it. For the Example slide the audience needs three things: what the prompt contains (the labelled boxes), that R1–R3 are three successive passages the model writes, and how to read the mask (rows read, columns are read). Magic chunks and the state machine get one spoken sentence each; the details are in the narrative for questions. Consider showing the Acme example as a text-only slide before Fig. 1: it introduces the tags with no figure to decode, and Fig. 1 then adds the mask.

### Why is the note "R1 0%, R2 86.5%, R3 95.6% saved" interesting?

Four reasons:

- **The saving is per step and depends on the mode.** Global steps cost full price; only focus and local steps save. So the total saving depends on how much the model writes in each mode. In the experiments, global steps are 23–45% of the written tokens (rising with context length) but over 80% of the attended tokens (Fig. 5a, §8.2).
- **The scaffold is the floor.** Local mode still reads the system instruction, question and DA instruction, about 1,100 tokens here, most of it the instruction itself. The protocol's own prompt is a fixed cost.
- **The saving grows with context.** A focus step reads the scaffold plus one ~2K chunk, whatever the document length; in this 25K-token example that is 86.5% saved, at contexts beyond 128K focus and local save 98–99% per step (Fig. 5b).
- **The numbers check out:** 3,435 − 1,124 = 2,311, exactly the size of chunk B1. (The box labels A + C + D add up to 1,291, not 1,124; a small inconsistency in the figure, probably template tokens counted differently. Not worth mentioning in the talk.)

---

## Q13. Who breaks the context into magic chunks?

*Slides: A Simple Example, Example.*

**The authors' preprocessing code, before the model sees anything.** A "tokenizer-aware semantic segmenter" (App. F) cuts the input document into segments of about 2,048 tokens at the most natural boundary available, numbers them, and builds the prompt around them: the system instruction, the simulated `get_magic_chunk` tool conversation with one "Magic Chunk N" per segment, then the question and the DA instruction. It is a fixed rule applied to the text, not a decision of the model, and not part of the state machine.

So the division of labour is:

| Who | Does what | When |
| :--- | :--- | :--- |
| Segmenter (authors' code) | cuts the document into numbered chunks, builds the prompt | once, before the model runs |
| Model | *names* chunks in its declarations | while writing |
| State machine (in the inference engine) | hides the chunks not named | at every generated token |

**Why this matters for the talk.**

- **The model never chooses the boundaries, only the labels.** If the answer straddles two chunks, or a table is split, the model can only focus on both or lose part of it. This is one of the two failure modes in App. D.4 ("evidence destroyed by segmentation", e.g. split tables), and the paper's proposed fix is again on the authors' side: structure-aware segmentation.
- **The chunks are artificial for static documents.** The paper argues that agentic settings provide natural segments (tool results, conversation turns) that need no segmenter; this is argued, not tested (Skeptical Points).
- **The model has read every chunk before it declares anything.** DA's mask acts only while the model generates its answer (decoding). The prompt, including all chunks, is first processed in full, as usual (prefill), so every chunk is already in the model's memory when it writes its first `<global>` note. This strengthens the point from Q2: "knowing where to look" comes after a complete read.

---

## Q14. Are magic chunks essential, or just for reporting? How would DA work in practice?

**Essential.** Focus mode needs something to name. The mask is defined over segments: `<focus magic_chunks="K">` means "keep chunk K", so without numbered chunks there is nothing to focus on. The DA instruction says so itself: when the document is delivered without chunks, "this tag is unavailable" (App. F). Only global and local mode would remain, and local alone saves little. The chunks are not a measuring device; the attended-token counts are measured by the engine regardless.

**Who does what in the paper's setup.**

1. **Prompt construction, before any call to the model** (the authors' evaluation code, outside vLLM): the segmenter cuts the document into ~2K-token chunks and builds the simulated tool conversation, "Magic Chunk 1" … "Magic Chunk N", followed by the question and the DA instruction. "No tool is ever executed: every segment is in place before generation begins" (§2.2).
2. **Prefill** (vLLM, unmodified): the whole prompt is read once, as usual.
3. **Decoding** (vLLM, modified): a hook on vLLM's attention metadata builder runs the state machine. At each generated token it checks the mode and rewrites the request's list of KV-cache blocks so that only the scaffold, the named chunks and the response stay visible (§2.3, App. B). No changes to vLLM's kernels or scheduler.

So the answer to "has vLLM been modified to chunk the input before calling the model?" is no: chunking is prompt preparation; the vLLM change acts only during generation. The engine must, however, know which token positions belong to which chunk in order to translate "chunk 7" into blocks. The paper does not spell out how this information reaches the engine (passed with the request, or found from the tool-message boundary tokens); App. B describes only the mask side.

**In practice.** Three requirements:

- **Segments.** For a static document someone must chunk it, as in the paper. The authors' target is different: agentic systems, where context already arrives in pieces (tool results, retrieved passages, conversation turns) that can serve as chunks directly, with no segmenter (§2.2, §8.2). This is argued, not tested.
- **A serving system with the state machine.** DA needs control over the inference engine, so it is something a model provider or a self-hosted open-weight deployment would build in; it cannot be added from the outside to a commercial API.
- **A model that follows the protocol.** Here, by a long instruction prompt; the paper expects post-training to make it native (§8.2), and suggests exposing the modes as tool declarations so they also work inside thinking traces.

**For the talk.** One sentence suffices: "the document is cut into numbered pieces when the prompt is built; the model names pieces, the serving system hides the rest." The practicality question (who chunks, who runs the engine) belongs to Skeptical Points under "Artificial segments".

---

## Q15. Is the segmenter part of DA, and DA part of a modified vLLM?

**The first yes, the second only partly.** The paper calls DA a *protocol*: an agreement between parties, each doing its part. It has three parts:

| Part of DA | What it does | Where it runs |
| :--- | :--- | :--- |
| Prompt construction: segmenter, magic-chunk transcript, DA instruction | turns a document and a question into a DA prompt | the application, before calling the model |
| The model | writes the tags and names chunks | the model itself, unchanged |
| State machine | reads the tags, hides undeclared chunks | the modified vLLM, during generation |

So the segmenter is part of DA (the prompt side), but it is not part of vLLM; only the state machine is. The two sides must agree on the chunk numbering: the prompt side defines "Magic Chunk 7", the engine side has to know which tokens that is.

A good mental model: DA is like a network protocol, with a client side (prompt construction), a server side (the engine) and a shared vocabulary (the tags and chunk numbers); the model is what speaks it. Nothing prevents packaging everything in the server, so that the user sends a plain document and the server chunks it, but that is a deployment choice the paper does not make.

---

## Q16. What should I call the side of DA that is not the state machine?

**The paper's own terms:** **prompt construction** (title of App. F; it includes the segmenter, the magic-chunk delivery and the DA instruction) versus **decode-time interventions** (title of §2.3; the state machine). §2 is organized the same way: prompt structure, context delivery, decode-time interventions.

**For the talk:** the **prompt side** and the **engine side**. Short, symmetric, and self-explanatory:

- *prompt side:* cut the document into numbered chunks, explain the three modes to the model;
- *engine side:* watch the model's tags, hide the chunks it did not name.

**On "modifies vLLM"** (clarified after a follow-up). The distinction is between a change to the *code*, made once, and what happens at *run time*:

- **Once, by the authors:** they modify vLLM by adding a piece of code, a hook. That added code *is* the state machine. In this sense "the engine side of DA is a modification of vLLM" is exactly right.
- **At every generated token, at run time:** the state machine does not change vLLM again; it changes vLLM's *data*, namely the list of memory blocks the next token will read.

So both phrasings are fine as long as they are not mixed: "DA's engine side is a modified vLLM", or "the state machine changes what the attention reads". The earlier wording here made a distinction that matters little for the talk.

---

## Q17. How should I explain the meaning of global, focus and local?

*Slide: A Simple Example.*

**One sentence first:** each tag says what the model will be able to *see* while it writes the next passage, and the engine holds it to that.

**Then the three modes, as an open-book exam:**

| Mode | Analogy | What the model sees | What it writes (per the prompt) |
| :--- | :--- | :--- | :--- |
| `<global>` | the whole book open | every chunk, plus the question and its notes | where to look next, and why; no answering |
| `<focus magic_chunks="K">` | the book open at one page | chunk K only, plus the question and its notes | the exact sentence or value, copied out |
| `<local>` | the book closed, only your notebook | no chunks; just the question and its notes | the reasoning: combine, calculate, commit |

**Then walk the slide line by line:** global, "I need two years; chunk 2 should have the founding"; focus on 2, copy the sentence; global again, "IPO still missing, try chunk 7"; focus on 7, copy; local, with the book closed, 2011 − 2003 = 8; answer.

**Two points to make explicit:**

- **"Its notes" are everything it has written so far.** That is why local mode works: the two copied sentences are on the page, so the book can be closed. Copy first, then reason.
- **The modes cost differently.** Global reads everything and costs full price; focus and local read almost nothing. The saving comes from spending most of the writing in focus and local.

**Caveat for the psychologists.** "Global" is not skimming: in global mode the model attends to every chunk at full resolution. The analogy is about what is *available*, not about how carefully it is read.

---

## Q18. Is global ordinary CoT, focus a tool call that erases data from the KV cache, and what is the difference between focus and local?

**Global ≈ ordinary CoT: yes.** In global mode the model sees everything, exactly as in plain chain-of-thought, and the engine does nothing (the `<global>` tag triggers no transition). The only differences come from the prompt: global text is supposed to be navigation only ("which chunk next, and why"), not reasoning about the answer.

**Focus as a tool call that erases data: two corrections.**

- **It looks like a tool call but is not one.** The engine parses the tag as it would a tool call, but nothing is executed and nothing is returned: no new text enters the context. The only effect is on what the model can see.
- **Nothing is erased.** All chunks stay in the KV cache. Focus *hides* every chunk except K for the duration of the focus passage; at `</focus>` everything is visible again. Hiding is reversible and free; erasing (as eviction methods do) is not.

**Focus vs. local.** The three modes differ in one parameter, which chunks are visible:

| Mode | Visible chunks | Always visible |
| :--- | :--- | :--- |
| global | all | question, instructions, everything written so far |
| focus K | only chunk K | same |
| local | none | same |

So the visible sets are nested: global ⊇ focus ⊇ local. Focus keeps one window onto the source, for copying out a fact; local closes it, for reasoning over what was already copied. Local is the cheapest mode and the one where the model must rely entirely on its own notes. For the talk: "Focus: look at one page. Local: look at no page, only at your notes."

---

## Q19. How does focus "hide" chunks, and what does "no chunks visible" mean for `<local>2011 - 2003 = 8 years.</local>`?

**How hiding works.** Mathematically, yes, as in Q7–Q8: for every token the model writes, the attention scores $q_t \cdot k_i$ of all tokens $i$ in hidden chunks are set to $-\infty$, so they get weight 0. In the implementation the engine does something equivalent but cheaper: it leaves those chunks' memory blocks out of the list the attention kernel reads, so they are never loaded. Same output; that is where the saving comes from.

**The local example, token by token.** The model writes "2011", " -", " 2003", " =", " 8", … one token at a time. Each of these tokens is a query $q_t$ that attends to:

- the scaffold: system instruction, question, DA instruction;
- everything written so far: the two global notes and the two focus excerpts, "Acme Corp was founded in 2003 in San Jose." and "Acme Corp went public on the NYSE in 2011.";

and to **no token of any document chunk**, chunks 2 and 7 included. So the numbers 2011 and 2003 have to come from the copied sentences in the response, not from the document. That is the point of the prompt's rule "copy first, then reason": a value not copied out during focus is not directly readable in local mode.

**A subtlety: hidden is not the same as gone.** The mask blocks *direct* access to chunk tokens. It is not an information barrier, because other cached entries were computed while the chunks were visible:

- The question and DA instruction come *after* the chunks in the prompt. During prefill they attended to the whole document, so their cached keys and values (beyond the first layer) can carry information from every chunk.
- The model's own earlier passages, especially the global notes, were written with all chunks visible; their cached states can also carry document information beyond their literal words.

So in local mode the model can, in principle, still draw on the document indirectly, through these states. Whether it does is an empirical question the paper does not address.

**Consequences for the talk.**

- The slide "Efficiency as a Measure of Self-Knowledge" says "no peeking". More precise: "the model cannot *read* other chunks directly". The behavioural-test argument weakens accordingly: the accuracy cost of the mask measures the cost of losing direct access, not of losing all information.
- This belongs with "Declared ≠ verified" on the Skeptical Points slide, and it is a natural experiment for the Bridges slide: probe the cached states in local mode for document facts that were never copied out.

---

## Q20. How do I read and explain the Results slide?

*Slide: Results.*

### What the numbers are

- **Each cell is "vanilla → DA"**: the same model on the same questions, without and with Declarative Attention.
- **Accuracy (%)**: share of answers judged correct.
- **Tokens (millions per answer)**: how much the model *read* while writing one answer, i.e. the number of earlier tokens attended to, added up over every token it wrote. Roughly: document length × answer length. Sanity check for passkey: a ~9K-token document and 1.89M tokens read means about 210 tokens written. This is why the numbers are in millions, and why they differ between models on the same task (different answer lengths).
- **Rows**: the three running examples, then the average over all 15 tasks.

### How to tell it

Ask the audience to read each row with two questions: *Did it get worse? Did it read less?*

- **passkey**: no loss; Gemma reads half as much, Qwen a fifth less. The easy case: the answer sits in one place.
- **code_repo**: no loss on Gemma, and Qwen even improves (72.2 → 77.8). Reads 64% (Gemma) and 39% (Qwen) less. The biggest documents, so the biggest absolute saving: about 42M and 52M fewer tokens read per answer.
- **space_digest**: the limit case. The answer is spread over all the reviews, so no single chunk contains it; accuracy drops 2.4 and 4.7 points. Note that vanilla is only 43–45% here: hard for everyone.
- **all 15**: about 1–3 points of accuracy lost, a third to a half of the reading saved.

One-sentence summary: *small accuracy cost, large saving, largest where documents are long, smallest gain where the answer is spread out.*

### Fig. 2 and the bullets

Three panels, each relative to vanilla = 100, with three bars: vanilla (grey), DA (blue), DA without the mask (light blue, same prompt but full reading).

- **(a) accuracy:** all close to 100.
- **(b) decode steps:** DA writes *more*, 31–35% longer answers, because of the navigation text.
- **(c) tokens read:** with the mask, DA reads 48% / 69% of vanilla; without the mask, the same longer answers read 166% / 129%.

The story: DA does not save by writing less; it writes more. The saving comes entirely from the mask. The decode-time estimate (0.71× / 0.77× of vanilla) is a calculation from these counts, not a measurement.

### Cognitive load

The slide has two visuals, three bullets and a note: too much for one slide. Suggest splitting:

1. **Results**: the table only, ideally as relative changes (±0 / −53%, …), which are easier to read than pairs of numbers;
2. **The Saving Comes from the Mask**: Fig. 2 with one line, "DA writes more but reads less; without the mask it reads more than vanilla."

Both texts are already in the narrative.

---

## Q21. Where do I see how many tokens were saved? An example.

*Slides: Results, The Saving Comes from the Mask.*

**In Table 2, right half ("Attended Tokens, M / sample"):** compare the **Vanilla** and **DA** columns of the same model in the same row. The saving is the difference; the relative saving is one minus the ratio. The table does not print the savings; you compute them.

**Example: code_repo on Gemma-4-31B** (row `LBv2/code_repo`, Gemma columns):

- Vanilla: **64.86** million tokens read per answer.
- DA: **23.08** million.
- Saved: 64.86 − 23.08 = **41.78 million** tokens per answer, i.e. 1 − 23.08 / 64.86 = **64%**.
- Accuracy in the same row: 72.2 → 72.2, no loss.

**The headline numbers come from the last row**, "Total Average": Gemma 13.43 → 6.45, saving 6.98M per answer = **52%**; Qwen 22.54 → 15.52, saving 7.02M = **31%**. These are the 52% and 31% of the abstract.

**On the next slide**, Fig. 2c shows the same totals relative to vanilla = 100: DA bars at 48 and 69, i.e. 52% and 31% saved; the DA no-mask bars at 166 and 129 read *more* than vanilla.

**What 42 million tokens means physically** (for the AI experts). Gemma-4-31B reads 81,920 bytes per token across its 10 full-attention layers (App. C.9). 41.78M tokens × 81,920 B ≈ **3.4 TB** of memory traffic avoided for one answer: at the paper's assumed effective bandwidth (8 TB/s × 70%), about 0.6 seconds of pure memory reading.

**For the slide**, one line under the table makes it concrete: "Example: code_repo on Gemma reads 64.9M → 23.1M tokens per answer: 42M (64%) saved, same accuracy."

---

## Q22. What is DA^nm vs. DA?

**DA^nm = "DA, no mask".** Same prompt as DA (document in magic chunks, the DA instruction), and the model writes the same kind of tagged response, but the engine ignores the tags: nothing is hidden, every token reads the whole context, as in vanilla. **DA** is the full method: same prompt, and the engine enforces the tags.

It is the paper's control condition (an ablation): it separates the effect of the *prompt* from the effect of the *mask*.

| | Vanilla | DA^nm | DA |
| :--- | :---: | :---: | :---: |
| DA prompt and tags | no | yes | yes |
| Mask enforced | no | no | yes |
| Gemma: accuracy | 87.01 | 87.01 | 85.74 |
| Gemma: tokens read (M) | 13.43 | 22.31 | 6.45 |
| Qwen: accuracy | 85.31 | 84.62 | 82.56 |
| Qwen: tokens read (M) | 22.54 | 29.02 | 15.52 |

Two comparisons:

- **Vanilla → DA^nm, the prompt alone:** accuracy unchanged (Gemma) or −0.7 points (Qwen), but reading goes *up* by 66% / 29%, because the tagged answers are longer and every token still reads everything.
- **DA^nm → DA, the mask alone:** accuracy −1.3 (Gemma) / −2.1 (Qwen) points, reading *down* by 71% / 47%.

So the prompt costs nothing in accuracy but makes reading more expensive; the mask makes it cheap and costs the 1–2 points. For the talk's question this is the key comparison: DA^nm minus DA is the accuracy cost of *holding the model to its declarations* (slide "Efficiency as a Measure of Self-Knowledge").

---

## Q23. What is the difference between single-span and multi-span?

**The idea.** A *span* is a contiguous stretch of the document. In a **single-span** task the evidence for the answer sits in one place: find it, read it, answer. In a **multi-span** task the answer has to be put together from several places: two facts in different sections, or an aggregate over the whole text.

**The paper's definition is only by name.** It sorts its 15 sources into "single-span retrieval/reasoning" and "multi-span reasoning" (Table 1, §4) without a formal criterion, and it sorts whole sources, not individual questions:

| Single-span (10) | Multi-span (5) |
| :--- | :--- |
| the five RULER needle tasks (incl. passkey), qmsum, multidoc_qa, LooGLE summarization, code_repo, quality | singledoc_qa, dialogue_history, longdep_qa, shortdep_cloze, space_digest |

Some placements are surprising: *multi-document* QA is single-span (presumably each question is answered from one document), while *single-document* QA is multi-span (questions combine sections of one long document). The names refer to where the evidence lies, not to the number of documents.

**Why it matters for DA.** Single-span fits the protocol's simplest shape: global → focus on one chunk → local → answer. Multi-span needs several navigation rounds, or a focus on several chunks at once (`<focus magic_chunks="2,7">` is allowed), or, for aggregates like space_digest, information from every chunk, which no focus on a few chunks can supply. The paper's Acme example is in fact a small multi-span question: two facts from chunks 2 and 7.

**Results by category** (Table 2, §5.1):

| | Accuracy cost, single / multi | Reading saved, single / multi |
| :--- | :---: | :---: |
| Gemma-4-31B | −0.8 / −2.3 points | 55% / 49% |
| Qwen-3.6-27B | −2.3 / −3.6 points | 30% / 33% |

The accuracy cost is higher on multi-span tasks for both models; the saving in reading is similar. This is the basis of the "When Does Self-Knowledge Work?" slide: declaring where to look works best when the answer lives somewhere.

---

## Q24. Does the paper have single-span and multi-span examples to inspect?

**No real model responses beyond Fig. 1.** I searched the paper: the only responses shown are

| Example | Where | Real or illustrative | Shape |
| :--- | :--- | :--- | :--- |
| SFT corpus question | Fig. 1 | not stated | single-span: global → focus on one chunk → local |
| Acme Corp | §2 | illustrative ("could look like") | multi-span: global → focus chunk 2 → global → focus chunk 7 → local |

Beyond that, the paper gives only schematic shapes and aggregate numbers:

- **The DA instruction (App. F) lists typical orders**, which are effectively the two categories as the authors expect them:
  - "Short factual / needle-in-haystack: the target magic chunk is obvious from the question": global → focus → local → answer (single-span).
  - "Multi-fact, separate magic chunks": global → focus → global → focus → local → answer (multi-span).
  - "Extract, sanity-check, fetch what's still missing, commit": global → focus → local → global → focus → local → answer.
- **Answer formats per question type** (multiple choice, cloze, short factual, summary), with one example answer each, no responses.
- **Failure cases** (Table 10, App. D.4): numbers per source, no responses.
- **Mode statistics** (Fig. 5): how many tokens are written in each mode, by context length, no responses.

No code or traces are released with the paper as far as the text says (no repository link).

**Options for the talk.**

1. **Use what exists:** Fig. 1 as the single-span case, Acme as the multi-span case. They already sit next to each other in the deck (A Simple Example, Example). Saying so explicitly gives the audience the contrast: "one chunk suffices" vs. "two chunks, two rounds".
2. **Show real task questions** from the benchmarks, without model responses: e.g. a passkey needle (single-span) and a space_digest question (multi-span: every review counts). These come from the public datasets, not from the paper.
3. **Generate examples ourselves.** The DA prompt is printed in full in App. F, so the prompt side can be reproduced exactly. Running it on a small open model (e.g. Qwen-3.5-4B, used in the paper) gives real tagged responses for a single-span and a multi-span question. Without a modified engine this is the no-mask condition (DA^nm): the model writes the tags but reads everything. That is enough to *show* the behaviour, not to measure savings. Effort: a few hours, mostly building the magic-chunk prompt.

---

## Q25. What do the three charts of Fig. 2 show?

*Slide: The Saving Comes from the Mask.*

**Common layout.** Each panel has two groups, Gemma-4-31B and Qwen-3.6-27B, with three bars each: **Vanilla** (grey), **DA** (blue), **DA no-mask** (light blue). Everything is relative to vanilla = 100, averaged over the 15 tasks.

**(a) Relative accuracy: does it get worse?**
Gemma: 100 / 99 / 100. Qwen: 100 / 97 / 99. The DA prompt alone (no-mask) costs almost nothing; the mask costs 1–3%.

**(b) Relative decode steps: how much does it write?**
Gemma: 100 / 135 / 128. Qwen: 100 / 131 / 116. Decode steps = tokens written, the length of the answer. DA answers are 31–35% longer than vanilla, because of the navigation notes, the copied excerpts and the tags. With the mask they are even a bit longer than without it; the paper does not discuss why.

**(c) Relative attended tokens: how much does it read?**
Gemma: 100 / 48 / 166. Qwen: 100 / 69 / 129. Without the mask, the longer answers read *more* than vanilla, since every written token still reads the whole context. With the mask, DA reads about half (Gemma) or two thirds (Qwen) of vanilla.

**How (b) and (c) fit together.** Reading = number of tokens written × how much each token reads. Dividing (c) by (b):

| | written (b) | read (c) | read per written token |
| :--- | :---: | :---: | :---: |
| Gemma, DA | 1.35 | 0.48 | 0.36 |
| Qwen, DA | 1.31 | 0.69 | 0.53 |
| Gemma, no-mask | 1.28 | 1.66 | 1.30 |
| Qwen, no-mask | 1.16 | 1.29 | 1.11 |

So with the mask each written token reads about a third (Gemma) or half (Qwen) of what a vanilla token reads, which more than pays for the longer answers. Without the mask each token reads *more* than in vanilla (1.1–1.3), because the DA prompt itself is longer (chunk transcript plus a ~1K-token instruction) and so is the response read back.

**One sentence for the audience:** "DA writes a third more, but each word reads only a third to a half as much, and that is entirely the mask: the same prompt without the mask costs more than doing nothing."

---

## Q26. What does "relative" mean in "relative decode steps", and why does it matter?

*Slide: The Saving Comes from the Mask (Fig. 2b).*

**Relative = divided by the same model's vanilla value, times 100.** A decode step is one forward pass, which produces one token, so the number of decode steps is the length of the answer in tokens. "Relative decode steps 135" for Gemma's DA means: DA answers are 1.35 times as long as Gemma's vanilla answers on the same questions, averaged over the 15 tasks. Vanilla is 100 by definition.

**Why relative.** Absolute answer lengths differ between models (Qwen tends to write more) and between tasks (a passkey answer is short, a summary long). Dividing by each model's own vanilla removes this, so the bars show only the effect of DA, and the two models can be compared side by side.

**Why decode steps matter at all.** Three reasons:

1. **Steps are time.** Each step is one pass through the whole network, and only part of its cost is reading the context. The rest (multiplying by all the model's weights, and on Gemma the sliding-window layers) is the same with or without the mask. So every extra step costs time the mask cannot save. This is why the estimated decode time falls only to 0.71× and 0.77× of vanilla, while reading falls to 0.48× and 0.69×: the 31–35% extra steps eat part of the saving (Table 3: on Gemma the weight multiplications go from 22.9 to 30.9 ms, the sliding-window reads from 49.7 to 67.1 ms).
2. **It rules out the trivial explanation.** One might suspect DA saves by writing less. Panel (b) shows the opposite: DA writes more, so the saving in (c) must come from reading less per token.
3. **It is the overhead of navigating.** The extra third is the text the model writes to say where to look and to copy things out. In the talk's terms: the cost of thinking about one's own attention. The paper expects training to cut it (§8.2: "DA runs about a third more decode steps than vanilla").

---

## Q27. Is the estimated decode time (0.71× / 0.77×) visible in the charts?

*Slide: The Saving Comes from the Mask.*

**No.** Fig. 2 shows accuracy, decode steps and tokens read. The decode-time figures come from **Table 3**, a separate calculation: the authors take the measured step counts (Fig. 2b) and tokens read (Fig. 2c), and charge each a cost per operation on an assumed accelerator (one B200 at assumed utilizations, a "roofline" model). The result is an estimate, not a timing.

| ms per answer (Table 3) | weight multiplications | full-attention reading | other layers | total |
| :--- | :---: | :---: | :---: | :---: |
| Gemma, vanilla → DA | 22.9 → 30.9 | 196.5 → 94.4 | 49.7 → 67.1 | 269.1 → 192.3 (**0.71×**) |
| Qwen, vanilla → DA | 34.4 → 45.1 | 263.8 → 181.6 | 8.0 → 10.5 | 306.2 → 237.3 (**0.77×**) |

Reading the context is the big term and falls by half (Gemma) or a third (Qwen); the other two grow with the 31–35% extra steps.

**For the slide.** The bullet refers to something the audience cannot see. Options:

- drop it from this slide and say the number aloud, with "estimate";
- or give it its own slide with the Table 3 screenshot (`images/table3-wall-time.png`, already cropped) and one line: "Estimated decode time: 0.71× (Gemma), 0.77× (Qwen) of vanilla; a calculation, not a measurement."

Given that "efficiency is projected" is one of the Skeptical Points, the second option has the advantage that the audience sees where the number comes from.

---

## Q28. What does the Scale slide (Fig. 3) show?

*Slide: Scale: Who Can Do This?*

**The question:** does DA work only for large models? Fig. 3 runs it on six models, three per family, and plots each relative to the *same model's* vanilla run (= 100).

**Layout.** x-axis: model size. Blue: Gemma-4 E4B (about 4B; "E" for "effective" parameters, an on-device design), 12B, 31B. Red: Qwen-3.5 4B, 9B and Qwen-3.6 27B. The dashed line is vanilla.

**(a) Relative accuracy: how much of its own accuracy does a model keep under DA?**

| | small | medium | large |
| :--- | :---: | :---: | :---: |
| Gemma | 29 | 91 | 99 |
| Qwen | 64 | 89 | 97 |

The smaller the model, the more DA hurts; the largest models are almost at vanilla. Smallest Gemma keeps less than a third of its accuracy: the protocol breaks it.

**(b) Relative tokens read: how much does it save?**

| | small | medium | large |
| :--- | :---: | :---: | :---: |
| Gemma | 46 | 183 (98) | 48 |
| Qwen | 50 (38) | 68 | 69 |

The saving does not grow with size: Gemma reads about half of vanilla at every size, Qwen half to two thirds. The outlier, Gemma-12B at 183%, is an artefact: about 6% of its answers never finish within the 8K-token output limit, and these endless answers keep reading. The black marks on the bars show the values without such non-terminating answers (98% for Gemma-12B, 38% for Qwen-4B).

**Why the small models fail.** Fig. 6a gives part of the answer: the share of `<focus>` declarations that name a valid chunk is 58% for Gemma-E4B, 90% for Gemma-12B, 99% for Gemma-31B; for Qwen 89%, 95%, 99%. So much of Gemma-E4B's collapse is failing to *follow the protocol*, not failing to know where to look. But not all of it: Qwen-4B follows the protocol 89% of the time and still keeps only 64% of its accuracy, so for that model something beyond the syntax goes wrong (bad choice of chunk, or reasoning with too little in local mode). The paper does not break this down.

**What it means.**

- **For the engineering view:** the method improves as models grow, which supports the paper's claim that zero-shot results are a floor.
- **For the metacognition view:** ability to declare usefully appears with scale. Whether that is a threshold for something like metacognition or simply for following a 1,000-token instruction, these data cannot tell (the slide's discussion question).

**Possible simplification of the slide:** keep the figure and one line, "Bigger models lose less; small ones fail mostly at following the protocol"; move the three numeric bullets to the narrative.

---

## Q29. Why does Gemma-4-12B read more than vanilla (183%), more than the 4B and 31B models?

*Slide: Scale: Who Can Do This? (Fig. 3b).*

**Because a few answers never end.** About 6% of Gemma-12B's DA answers do not terminate: the model keeps writing until it hits the 8K-token output limit. Each of these runaway answers reads the context thousands of times, and since the bar is an *average*, these few answers dominate it. The paper (§5.2, Fig. 3 caption): "Gemma-4-12B sits above vanilla only because about 6% of its DA responses fail to terminate, a decode-length artifact rather than a property of the mask: excluding them brings it just below vanilla (98%)." The black mark on its bar is that 98%.

**But even 98% is not a saving.** The 4B and 31B models read 46–48% of vanilla; the 12B model, without the runaway answers, still reads 98%. The paper's own decomposition explains why: the saving *per written token* is about the same on five of the six models (each token reads about half of what a vanilla token reads, §5.2), so the difference is in *how much* they write. Reading = tokens written × reading per token, so 98% at about 0.5 per token means Gemma-12B's DA answers are roughly twice as long as its vanilla answers. The mask works; this model just writes a lot under the protocol.

**How to put it in the talk.**

- The paper calls it an "artifact rather than a property of the mask". That is fair about the mask, but the total saving is what an engineer gets, and for this model it is zero. The paper itself says the per-token ratio measures the mechanism, "while the total reflects the elicitation" (§5.2): how well the prompt gets this model to use the protocol economically.
- The smallest Gemma's low 46% is not a success story either: it keeps only 29% of its accuracy.
- A milder version of the runaway effect appears in Qwen-4B (50%, or 38% without non-terminating answers), and there it happens in vanilla too: "a small-model trait".

One sentence: "The mask saves about half per word for every model; whether that becomes a total saving depends on how much the model writes, and Gemma-12B writes too much."

---

## Q30. What does "only its own notes" mean for `<local>`?

*Slide: A Simple Example.*

**"Its own notes" = everything the model has written so far in this answer.** In the Acme example, when the model reaches `<local>`, its notes are:

- the first global passage ("I need the founding year and the IPO year… Magic Chunk 2…"),
- the first focus excerpt ("Acme Corp was founded in 2003 in San Jose."),
- the second global passage ("The IPO year is still missing… Magic Chunk 7…"),
- the second focus excerpt ("Acme Corp went public on the NYSE in 2011.").

It reads these as ordinary text, with the tags. Not meant: notes from other conversations, or any hidden memory beyond this answer.

**Two precisions:**

- **Also visible in local mode:** the scaffold, i.e. the question, the DA instruction and the system instruction. Strictly, local mode sees "the question, the instructions, and its own notes, but none of the document".
- **Hidden is not gone** (Q19): the question, the instructions and the notes were processed while the document was visible, so their internal states can still carry some document information. "Sees" means what it can read directly.

**Suggested wording for the bullet**, if you want it exact: "`<local>`: the model sees no chunks, only the question and what it has written so far, and reasons to the answer."

---

## Q31. What is the difference between global and local, if both are added to the context? Are no new KV values computed in local mode?

**Both are written, both are stored; they differ only in what they read.**

Every token the model writes, in any mode, is appended to the context, and its keys and values are computed and stored in the KV cache. Local tokens are no exception: their keys and values are computed and kept, and every later token can read them, since the response so far is always visible (App. B: "the entire response generated so far" is always attended).

What differs is the *reading* done while each token is written, i.e. which earlier tokens its query $q_t$ may attend to:

| Mode of the token being written | It may attend to ($S_t$) |
| :--- | :--- |
| global | everything before it: scaffold, all chunks, response so far |
| focus K | scaffold, chunk K, response so far |
| local | scaffold, response so far |

In the formula of the Idea slide, the mode decides only the set $S_t$ in $o_t = \sum_{i \in S_t} \alpha_{ti} v_i$: the row of the mask. The keys and values of the new token itself are computed the same way in every mode.

**In a picture:** the mode is a property of the *reader*, not of what is written. A local passage is written with the document hidden, but once written it is part of the notes, visible to everything that follows, including a later global passage.

**One consequence:** the keys and values of a local token are computed from a state that saw no document chunk directly, only the scaffold and the notes. So local passages contain what the model could work out from its notes, which is the point of "copy first, then reason" (with the caveat of Q19 that the notes themselves may carry indirect document information).

---

## Q32. Should I read the mask in Fig. 1 as a picture of what can attend to what?

*Slide: Example.*

**Yes, exactly.** Rows are the readers, columns what can be read:

- **Row** = the tokens of one passage the model writes (R1 global, R2 focus, R3 local): the queries.
- **Column** = a block that could be read: system instruction A, chunks B1–B12, question C, DA instruction D, and the passages R1–R3: the keys and values.
- **Solid box** = this row may attend to this column; **dashed** = masked.

Each row is the set $S_t$ of Q31 for the tokens of that passage. Read across:

- R1 (global): A, B1–B12, C, D, R1: everything up to itself.
- R2 (focus on B1, marked F): A, B1, C, D, R1, R2.
- R3 (local): A, C, D, R1, R2, R3: no chunks, but all earlier passages.

**Three things the picture shows at a glance:**

- **The blue scaffold columns are solid in every row:** the question and instructions are always visible.
- **The grey response columns are solid wherever they exist:** a passage, once written, is visible to all later ones (Q31). R3 reads the excerpt copied in R2.
- **The staircase on the right is the ordinary causal rule:** R1 cannot attend to R2 or R3, which do not exist yet.

**One simplification in the figure:** it draws one box per segment. The real mask is per token, rounded to memory blocks of 16–32 tokens, and within a passage each token also reads the earlier tokens of the same passage.

---

## Q33. Where do the results show the difference between focus and local?

**Not in the headline results.** Table 2 and Fig. 2 count all tokens of an answer together, whatever the mode. The modes are separated in **Fig. 5** (§6.1, Gemma-4-31B; the Qwen counterpart is Fig. 9 in App. E). The crop is already in `images/fig5-mode-share.png`.

**Fig. 5a: how much of the answer is written in each mode**, by context length (% of written tokens):

| Context length | global | focus | local |
| :--- | :---: | :---: | :---: |
| < 32K | 27 | 38 | 35 |
| 32–64K | 26 | 32 | 42 |
| 64–128K | 23 | 19 | 58 |
| > 128K | 45 | 22 | 34 |

Overall about 27% global and 73% focus + local. At the longest contexts the global share jumps to 45%, which caps the saving there.

**Fig. 5b: how much a token saves in each mode**, relative to a vanilla token (% of reading saved):

| Context length | focus | local |
| :--- | :---: | :---: |
| < 32K | 76 | 88 |
| 32–64K | 90 | 95 |
| 64–128K | 96 | 97 |
| > 128K | 98 | 99 |

On average a focus token reads about 12% and a local token about 6% of what a vanilla token reads (§6.1).

**How to read the difference.**

- **Local always saves more than focus,** because it reads no chunk at all; focus reads one.
- **The gap closes as documents grow.** A focus token reads the scaffold plus one ~2K chunk, a local token only the scaffold; that one chunk is a sizeable part of a 30K document but negligible in a 200K one. Hence focus improves sharply with length (76 → 98%) and local only a little (88 → 99%).
- **Neither saves 100%,** because both still read the scaffold (about 1K tokens of instructions) and the growing response.
- **Global is the expensive mode:** it saves nothing, and although it is only a quarter to a half of the written tokens, it accounts for over 80% of all tokens read by DA (§8.2).

**For the talk.** If you want the focus/local distinction in the results, Fig. 5 fits as one slide after "The Saving Comes from the Mask", with one line: "Most of the answer is written in the cheap modes; local saves the most, focus nearly as much on long documents; the global steps are where the remaining cost lies."

---

## Q34. For my message the focus/local difference seems unimportant. Is there something I should say?

**Right: as an efficiency detail, skip it.** That local saves a little more than focus, and that the gap closes on long documents, does not bear on the question of the talk. No Fig. 5 slide needed.

**But the transition *into* local mode is worth one or two sentences**, because it is the most metacognitive moment of the protocol:

- **Opening `<local>` is a judgement of sufficiency.** The model closes the book: it commits to having copied out everything it needs. That is a "do I know enough to answer?" decision, close to what psychologists study as feeling-of-knowing or confidence judgements before answering. In your earlier list, "know when they have enough information to stop looking" was one of the abilities DA seems to require.
- **The prompt documents that models get this wrong.** The DA instruction (App. F) was written "from failure modes observed during prompt development" (§2.1), and two of its rules read like reports of overconfidence: "Skipping focus and guessing from memory is the most common failure mode", and "Anything you 'remember' about a magic chunk you didn't focus on is a guess." So before the authors added these warnings, models tended to answer from what they thought they knew instead of looking. That is a nice point for the psychologists, and it fits the Skeptical Points: part of the "self-knowledge" is supplied by the prompt's warnings.
- **The data cannot separate the two cases.** When local mode produces a wrong answer, the paper does not tell us whether the model closed the book too early (a sufficiency error) or chose the wrong chunk earlier (a navigation error).

**Where to put it.** One sentence on the A Simple Example slide when introducing `<local>` ("closing the book is a judgement that you have enough"), and the prompt's warnings as a bullet in the narrative of "When Does Self-Knowledge Work?" or Skeptical Points.
