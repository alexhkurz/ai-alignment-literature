---
# https://hackmd.io/s/how-to-create-slide-deck
title: Language Models Can Control Their Own Attention (Slides)
slideOptions:
  theme:  white # league #https://revealjs.com/themes/
  transition: fade # none/fade/slide/convex/concave/zoom
  transitionSpeed: slow # default/fast/slow
  spotlight:
    enabled: false
  controls: false
---

## Language Models Can Control Their Own Attention

###### Ho, Ahmad, Koh, Yun, Schuster, dos Santos (2026)

<br>

###### presented by Alexander Kurz

###### Chapman University

<br>

###### AI Journal Club, Oct 14 2026

<br>

---

<style type="text/css">
  .reveal p {
    text-align: left;
  }
  .reveal ul {
    display: block;
  }
  .reveal ol {
    display: block;
  }
  .reveal {
    font-size: 24px;
  }
</style>

## Introduction

> "wouldn't the model already know which parts of the context are relevant?" (Ho et al., abstract)

- **General Idea:** Only pay attention to what is important.
- **Engineering View:** Optimize the KV cache: read less of it for each new token.
- **Method View:** Allow the LLM to program the inference engine.
- **Metacognition View:** What does the LLM know about itself?

---

## The Problem

Generating one token = one pass through the network.

- Every global attention layer re-reads all previous tokens.
- At long context this read dominates decoding time (73–86% in the paper's estimates).
- But the model only attends to a small part of its context.

---

## From Chain-of-Thought to Declarative Attention

Chain-of-thought text is a scratchpad. Declarative Attention extends CoT.

| | Chain-of-thought | Declarative Attention |
| :--- | :--- | :--- |
| Text is read by | the model | the model and the inference engine |
| Text changes | what the model computes next | what the model computes and what it attends to |

The inference engine reads DA and changes the input to the attention mechanism.

---

## Idea

**Attention Mechanism:**

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

**Idea:**

Inference engine reads DA and changes $QK^\top$ (setting masked tokens to $-\infty$).

---

## A Simple Example

![Acme example](images/example-acme.png)

- `<global>`: the model sees the whole document and decides where to look next (similar to CoT).
- `<focus>`: the model sees only the named chunk and copies out what it needs.
- `<local>`: the model sees no chunks, only its own notes, and reasons to the answer.

---

## The Attention Mask

![Figure 1](images/fig1-protocol.png)

R1 global (0% saved), R2 focus on chunk B1 (86.5% saved), R3 local (95.6% saved).

---

## On Focus vs Local

The following quote from the prompt explains the rationale behind focus and local:

![DA instruction, soft requirements](images/prompt-soft-requirements.png)


---

## Models

| | Gemma-4-31B | Qwen-3.6-27B |
| :--- | :--- | :--- |
| Full-attention layers | 10 of 60 | 16 of 64 |
| Other layers | 50 sliding-window (1,024 tokens) | 48 Gated DeltaNet |
| Context | 256K tokens | 256K tokens |

Plus smaller models for scaling: Gemma-4-12B, Gemma-4-E4B, Qwen-3.5-9B, Qwen-3.5-4B.

---

## Tasks

15 tasks from 5 benchmark suites (RULER, LongBench v1/v2, LooGLE, ZeroScrolls), up to 244K tokens. Three running examples:

| Task | Category | What it asks |
| :--- | :--- | :--- |
| passkey (RULER) | single-span | find a 7-digit number hidden in ~9K tokens of filler |
| code_repo (LongBench v2) | single-span | answer a question about a software repository |
| space_digest (ZeroScrolls) | multi-span | aggregate sentiment over ~7K tokens of hotel reviews |

---

## Results

![Table 2](images/table2-main-results.png)

- Left: accuracy (%). Right: tokens read per answer (millions).
- Per model: Vanilla, DA^nm (DA prompt, no mask), DA.
- Running examples: `niah_single_1` (passkey), `code_repo`, `space_digest`.

---

## The Saving Comes from the Mask

![Figure 2](images/fig2-masking-vs-length.png)

- DA generates *more* tokens (+35% / +31% decode steps), yet reads less.
- Without the mask (DA no-mask) the cost goes *up*: the saving comes from masking.

---

## By Model Size

![Figure 3](images/fig3-model-scale.png)

- Relative accuracy: Gemma-4 E4B 29%, 12B 91%, 31B 99%.
- Much of the small model's collapse is failure to *follow the protocol*: only 58% of its focus calls parse (99% at 31B).
- The 12B model attends to *more* tokens than vanilla (183%): ~6% of its responses do not finish within the 8K-token budget.

---

## Conclusion

> a model can control its own attention span in text a person can also read, turning selective attention from a pattern inferred inside the network into one the model states out loud, enabling long-context inference that is at once legible and more efficient. (Ho et al., conclusion)

**Questions:** 
- Does the successful engineering optimization of the attention mechanism tell us sth about what the LLM knows about itself?
- Can one think about other ways of the LLM programming the inference engine?
- What about agents modifying the attention of other agents?

