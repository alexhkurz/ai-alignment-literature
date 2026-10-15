# Slides narrative

The full story behind [slides.md](slides.md), one section per slide. The slides carry one idea each; everything else lives here: what to say, the numbers behind it, the caveats, and the transition to the next slide. Questions about the slides and their answers are in [slides-commentary.md](slides-commentary.md).

Sources: the paper is Ho et al. (2026), arXiv:2609.02737 (section, table and figure numbers below refer to it). Fact-checked against the paper; see [background-reader-factcheck.md](background-reader-factcheck.md).

---

## Title

The paper is from KAIST AI and Google DeepMind (Google co-authors advisory). It appeared on arXiv on 2 September 2026. I am not an author; I present it because it sits where engineering and questions about machine self-knowledge meet, and because it connects to our own work on steering ("Connection: First-Order Steering" and "Bridges").

---

## Big Questions

**Story.** Start with the question the authors start with: wouldn't the model already know which parts of the context are relevant? There are two ways to hear it.

- The **engineering** question: long conversations are expensive because the model re-reads everything for every word it writes. If the model knows where the relevant part is, we can let it skip the rest.
- The **metacognition** question: does a language model know something about its own knowledge, here about *where* in its context the information it needs is? Can it say so, and is what it says true?

The talk takes the engineering result seriously and asks what it tells us about the second question.

**For later.** Inside the metacognition question sits a further one ("Discussion"): if the model's statements about where to look are good, is that because of something like metacognition, or because of pattern matching on surface cues? The engineering result is neutral between these two; it only needs the statements to be good enough (commentary Q2).

**Question for this talk.** Is the efficiency result a behavioural test of a metacognitive claim? The case for yes: because the system *acts* on what the model says, wrong statements would cost accuracy. Pose it as a question, not a claim: the authors make no metacognitive claim, so this is our reading, to be examined. "Efficiency as a Measure of Self-Knowledge" makes the test precise; the conclusion answers the question.

**Transition.** First the engineering problem.

---

## The Problem

**Story.** A language model writes one token (roughly, a word piece) at a time. For each new token, every attention layer compares the new token with all previous tokens. To avoid recomputing, the model stores two vectors per previous token and layer, the keys and values: the **KV cache**. Each new token reads the whole cache.

At long context this read is the bottleneck. In the paper's cost model for one decode step, reading the cache is 73% (Gemma) and 86% (Qwen) of decoding time (Table 3, a roofline estimate on a B200 accelerator, not a measurement). The arithmetic is cheap; moving memory is expensive.

Yet attention is sparse: most of the weight lands on a few tokens. **Sparse attention** methods try to read only those. Their problem: you do not know which tokens matter until you have looked. Static rules (keep recent tokens, keep tokens that were important before) are cheap but miss what a later question needs. Query-dependent methods (QUEST, SparQ, DeepSeek's indexer) scan a cheap summary of the whole cache at every step, so the cost per token stays proportional to context length, $O(N)$, with a smaller constant. The paper calls this **system-1** masking: inferred from activations, implicit, at every step.

**Details.**

- "Global attention layer" is the paper's term for a full-attention layer. Modern models are hybrids: Gemma-4-31B has 10 full-attention layers and 50 sliding-window layers (each token sees only the last 1,024 tokens); Qwen-3.6-27B has 16 full-attention layers and 48 Gated DeltaNet layers (a fixed-size recurrent memory). Only the full-attention layers have a cost that grows with context, so only they are masked (§2.3). See commentary Q1.
- Name clash to warn about: the DA *mode* `<local>` has nothing to do with *local* (sliding-window) layers.
- Size: Gemma-4-31B stores 81,920 bytes of KV cache per token; at 1M tokens that is about 82 GB, read in full for every new token.

**Transition.** The paper's alternative uses something models already do: think out loud.

---

## From Chain-of-Thought to Declarative Attention

**Story.** Chain-of-thought (CoT): the model writes intermediate reasoning before the answer. Two facts about CoT tokens matter here. They are ordinary tokens, so each costs a forward pass. And they enter the KV cache, so every later token can read them: the written trace is a scratchpad, an external memory.

Why writing helps, precisely: the cache also keeps internal results for earlier tokens, but a later token can read them only at the same depth (layer). A result written out as a token is read again from the first layer on, so the whole network can build on it.

DA adds one step. Explain the table row by row.

- **Who reads the text.** In CoT the only reader of the trace is the model itself (and us). In DA a second reader is added: a small program in the inference engine that scans the output for tags.
- **What the text changes.** A CoT sentence such as "the answer is in the section on fine-tuning" changes what the model computes next, but only *inside* the network: it is one more piece of context, and the next token still reads the whole KV cache; attention may weigh the fine-tuning section more, but nothing is skipped. The same statement written as `<focus magic_chunks="1">` is acted on *outside* the network: the engine removes all other chunks from the set of cache blocks the next token reads. The model cannot attend to what is not loaded. So DA text does both: as context it changes what the model computes, like any CoT; as a command it changes what the model *sees* at all. CoT shifts the soft attention weights, at best; DA also changes the hard set of what is read.
- **Visible vs. executable** (say it; not on the slide). "Visible": CoT lets us read the reasoning, but the text has no effect except through the model, and it need not be faithful to what the model actually computed. "Executable": DA's text works like an instruction in a program. It has a fixed meaning to an interpreter (the engine), and it has that effect whether or not it reflects anything inside the model. This is what makes the efficiency result a test (the question on Big Questions): a declaration that is acted on can be wrong in a way that costs accuracy.

The analogy for the mathematicians and software engineers: CoT is a comment, DA is code.

**Details.**

- Wei et al. (2022) elicited CoT with worked examples in the prompt; Kojima et al. (2022) showed "Let's think step by step" works without examples (zero-shot). DA is zero-shot in Kojima's sense: no training, no examples, one instruction.
- The paper's own framing (§1): CoT surfaces latent computation as text; DA extends this "from dictating what to think to where to attend".
- CoT traces are not always faithful to the model's actual computation: models can give reasons that did not drive their answer (Turpin et al., 2023). DA's declarations are faithful in one limited sense: they determine what is read. Whether they reflect why the model chose that chunk is a separate question.

**Transition.** How the declaration works.

---

## Idea

**Story.** The famous formula (Vaswani et al., 2017):

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

Each token $i$ is turned, at each layer and head, into three vectors by learned linear maps: a **query** $q_i$ (what am I looking for?), a **key** $k_i$ (what do I offer?), and a **value** $v_i$ (what do I pass on?). $Q$, $K$, $V$ stack these as rows; $d_k$ is the key dimension, and dividing by $\sqrt{d_k}$ keeps the dot products in a range where softmax is not saturated.

During generation only one row matters: the newest token $t$. Its output is a weighted average of the values of all earlier tokens,

$$o_t = \sum_{i \le t} \alpha_{ti}\, v_i, \qquad \alpha_{ti} = \frac{\exp(q_t \cdot k_i / \sqrt{d_k})}{\sum_{j \le t} \exp(q_t \cdot k_j / \sqrt{d_k})},$$

where the weights $\alpha_{ti}$ are positive and sum to 1. The restriction $i \le t$ is the causal mask: a token never sees the future.

Three points for the talk:

- **The KV cache** is the list of all $k_i, v_i$ for $i < t$, stored so they need not be recomputed. To compute $o_t$, every one of them must be read from memory: two dot-product-sized operations per stored token, so the arithmetic is cheap and the memory traffic is the cost (The Problem).
- **Sparsity** means that most $\alpha_{ti}$ are tiny: a few tokens carry almost all the weight.
- **DA restricts both sums** to a declared set $S_t \subseteq \{1, \dots, t\}$ (scaffold, declared chunks, response so far). Equivalently, the scores $q_t \cdot k_i$ for $i \notin S_t$ are set to $-\infty$ before the softmax. In matrix form: $\mathrm{softmax}(QK^\top/\sqrt{d_k} + M)\,V$ with $M_{ti} = 0$ for declared $i$ and $-\infty$ otherwise. Causal attention already has a mask of exactly this form ($M_{ti} = -\infty$ for $i > t$: no looking ahead); DA makes the mask depend on what the model writes. The cache entries outside $S_t$ are never read, which is the saving; the softmax renormalizes over $S_t$.

**A bound for the mathematicians.** If the dropped tokens carry total weight $\varepsilon = \sum_{i \notin S_t} \alpha_{ti}$ and $\|v_i\| \le M$, then the masked output $o_t^{S} = \frac{1}{1-\varepsilon}\sum_{i \in S_t} \alpha_{ti} v_i$ satisfies

$$\|o_t - o_t^{S}\| \le 2\varepsilon M.$$

(Split $o_t - o_t^S$ into the dropped terms, of norm at most $\varepsilon M$, and the renormalization error $\frac{\varepsilon}{1-\varepsilon}\sum_{i \in S_t}\alpha_{ti} v_i$, also of norm at most $\varepsilon M$.) So masking is harmless exactly when the declared set captures almost all the attention weight. This holds per head and per layer; errors can compound through the layers, and the bound says nothing about whether the model *chose* $S_t$ well. That is what the accuracy numbers test.

**Details.**

- Multi-head: each layer runs several heads with their own $q, k, v$ in parallel and concatenates the outputs. The masks in DA are the same for all heads and all full-attention layers.
- Grouped-query attention: several query heads share one key–value head, which shrinks the cache. Gemma-4-31B's full-attention layers have 4 KV heads of dimension 512 (81,920 bytes per token over its 10 layers in bf16, App. C.9).

**Transition.** How the model chooses $S_t$: an example.

---

## A Simple Example

**Story.** The paper's own illustration (§2), shown as plain text so the audience meets the tags before any figure. The question needs two facts from two places in a long document. Explain the modes first, as an open-book exam: each tag says what the model will be able to *see* while writing the next passage. `<global>`: the whole book is open; decide where to look. `<focus>`: the book is open at one page; copy out what is needed. `<local>`: the book is closed, only the notebook (everything written so far) remains; reason and commit. ("Global" is not skimming: the model attends to every chunk in full; the analogy is about what is available.) Then read the response top to bottom:

- `<global>`: the model, seeing the whole document, says what it needs and where it expects it: "Magic Chunk 2 should state the founding."
- `<focus magic_chunks="2">`: now it sees only chunk 2 and copies out one sentence.
- `<global>` again: it notes what is still missing and names the next chunk.
- `<focus magic_chunks="7">`: sees only chunk 7, copies the IPO sentence.
- `<local>`: sees no chunks, only its own notes, and computes 2011 − 2003 = 8.
- `<answer>`.

Point out three things: the model alternates navigation and reading as often as it needs; focus text is a short excerpt, not reasoning; the final calculation happens with the document out of sight, using only what was copied out. The engine hides every chunk the model has not named.

This is an illustration written by the authors ("a response … could look like", §2), not a logged model response. The paper does not say whether Fig. 1 is a logged response either.

**Transition.** The same protocol on a longer document, with the mask made visible.

---

## The Attention Mask

**Story.** Recall the three modes from the Acme example, pointing at R1–R3 in the figure. The model splits its reasoning into spans, each tagged with a mode:

- `<global>`: reads everything; used to find where to look.
- `<focus magic_chunks="K">`: reads only chunk K (plus the question and instructions); used to read one region closely.
- `<local>`: reads only the question, instructions and its own notes so far; used to reason about what it already extracted.

The inference engine reads the tags as they are generated and hides everything outside the declared scope. No training: one fixed prompt, off-the-shelf models.

The paper calls this **system-2** sparse attention: the mask is reasoned about, in words.

Then walk through Fig. 1. The prompt: a system instruction (A), a long document cut into 12 chunks (B1–B12), the question (C), the DA instruction (D). The question: how many instruction–response pairs are in the final fine-tuning corpus?

- R1, `<global>`: "Magic Chunks 1 contains the 'Supervised fine-tuning' section." Reads all 25,466 prompt tokens.
- R2, `<focus magic_chunks="1">`: extracts "15K regenerated math answers and 1.5k open-domain conversations". Reads 3,435 prompt tokens: 86.5% saved.
- R3, `<local>`: adds 15,000 + 1,500 = 16,500. Reads 1,124 prompt tokens: 95.6% saved.

The mask at the bottom shows which blocks each step reads: everything, then A + B1 + C + D, then A + C + D. The response so far (R1, R2, …) is always readable.

**How to read the figure** (say this first; most of the audience has not seen such a diagram). Top left: the prompt, as labelled boxes: system instruction A, the document in 12 chunks B1–B12, the question C, the DA instruction D. Top right: the model's answer, which is one continuous text; the labels R1–R3 and the headings are the authors' annotations, not model output. Bottom: the mask. Rows are the three passages the model writes, i.e. who is reading; columns are what can be read. Solid boxes are read, dashed boxes hidden; blue is the always-visible scaffold, green the document, grey the model's own text. The staircase on the right is the ordinary rule that a passage cannot read text written after it.

**Why the savings line matters.** Global steps cost full price; only focus and local save, so the total saving depends on how much the model writes in each mode (global: 23–45% of written tokens, but over 80% of attended tokens; Fig. 5a, §8.2). The scaffold is a floor: local mode still reads about 1,100 tokens, mostly the DA instruction. And the per-step saving grows with context: a focus step always reads the scaffold plus one ~2K chunk, so 86.5% here becomes 98–99% beyond 128K (Fig. 5b).

**Details on the protocol.**

- **Magic chunks.** The context is cut into segments of about 2,048 tokens at natural boundaries (paragraphs, then lines, sentences, clauses). They are presented as results of earlier tool calls ("get_magic_chunk"), so the chunk boundaries fall on special tokens the model already knows from tool-use training. The deliberately odd name keeps the model from confusing chunks with the document's own sections.
- **Scaffold**, always visible: a short system instruction ("You are a helpful assistant.") that absorbs the attention sink (the first tokens receive disproportionate attention), the question, and the DA instruction (1,068 tokens in Fig. 1).
- **Switching.** The engine switches on the closing ">" of `<focus …>` or `<local>`, and back to global on `</focus>` / `</local>`. Global is the default; the `<global>` tag only helps the model keep track (§2.3).
- **Reversible.** Masked blocks stay in memory; a later global step can read everything again. This is unlike eviction methods, which delete cache entries for good.
- **Block-aligned.** The mask is rounded outward to the cache's 16–32-token blocks, so standard attention kernels (FlashAttention) run unchanged.
- **System-2.** The paper calls this system-2 sparse attention (§8.4): the mask is reasoned about, in words, instead of inferred from activations. The term follows System 2 Attention (Weston & Sukhbaatar, 2023), which in turn borrows from dual-process theory.

**Caveat to mention.** The declaration in R1 is made in global mode, i.e. while reading everything. Knowing where to look comes after a full read, and here it looks like matching the question to a section heading.

**Transition.** On which models and tasks was this tested?

---

## Models and Tasks

**Story.** Two headline models, Gemma-4-31B and Qwen-3.6-27B, chosen because they are hybrids of different kinds (sliding-window vs. Gated DeltaNet). Four smaller models for the scaling question: Gemma-4-12B, Gemma-4-E4B, Qwen-3.5-9B, Qwen-3.5-4B.

Fifteen task sources from five benchmark suites (RULER, LongBench v1 and v2, LooGLE, ZeroScrolls), in two categories: **single-span** (the answer is in one place) and **multi-span** (it must be combined from several places). Contexts from about 6K to 244K tokens.

Three running examples, used for every number in the talk:

- **passkey** (RULER `niah_single_1`): a 7-digit "special magic number", attached to a key such as an adjective–noun pair, hidden in about 9K tokens of repeated filler sentences. The simplest retrieval test; explains the mechanism.
- **code_repo** (LongBench v2): questions about a software repository. Shows the stakes: the largest contexts and the largest savings.
- **space_digest** (ZeroScrolls): hotel reviews, about 7K tokens; the answer aggregates sentiment over all reviews, so no single chunk contains it. Shows the limits.

**Details.**

- Both headline models handle 256K tokens (Gemma-4-E4B: 128K). Examples longer than 244K (116K) tokens were excluded, leaving room for the prompt template and the answer (App. D.1). code_repo repositories average 1.07M tokens as a source, but only examples up to 244K were evaluated.
- Four of the 15 sources use questions generated with Gemini-3-Flash (qmsum, multidoc_qa, LooGLE summarization, singledoc_qa; Table 1).
- space_digest: the original ZeroScrolls task asks what percentage of the reviews are positive. Check the exact question format before presenting it.
- Scoring: an LLM judge (Qwen-3.5-4B) applies a pass/fail rubric written by Gemini-3-Flash from the reference answer; on a sample of 2,993 responses it agrees with Gemini-3.1-Pro on 98.5% of verdicts (App. D.2).
- Three arms per task: **vanilla** (plain prompt, full attention), **DA** (DA prompt and mask), **DA no-mask** (DA prompt, full attention).

**Transition.** The results.

---

## Results

**Story.** First explain how to read the table (Table 2 of the paper), then follow the three running examples.

How to read it:

- **Two halves.** Left: accuracy, the percentage of answers judged correct. Right: attended tokens, in millions per answer: how many earlier tokens the model read, added up over every token it wrote (roughly document length × answer length; e.g. passkey: ~9K-token document, 1.89M read, so about 210 tokens written).
- **Three columns per model.** Vanilla (plain prompt, full reading), DA^nm (the DA prompt and tags, but no mask: the model still reads everything), DA (prompt and mask). Comparing Vanilla with DA^nm shows the effect of the prompt; DA^nm with DA the effect of the mask.
- **Two blocks of rows.** Single-span tasks (the answer is in one place) and multi-span tasks (it must be combined from several places), each with a category average; the last row averages all 15.
- **Colours** (right half, average rows only): green = fewest tokens read, red = most. DA is always green, DA^nm always red: the next slide's story in one glance.

Then ask two questions of each running example: did it get worse, and did it read less?

- passkey: no accuracy change on either model; Gemma reads 53% less, Qwen 18% less.
- code_repo: no change on Gemma, Qwen even improves by 5.6 points; reads 64% and 39% less. In absolute terms this is the largest saving: 41.8M fewer attended tokens per answer on Gemma, 52.0M on Qwen.
- space_digest: the limit case. Accuracy drops 2.4 points (Gemma) and 4.7 points (Qwen). This task is hard for everyone (vanilla accuracy only 43–45%).
- Over all 15 tasks: Gemma loses 1.3 points and reads 52% less; Qwen loses 2.8 points and reads 31% less.

**Details.**

- Absolute numbers (accuracy %, attended tokens in millions per response, vanilla → DA): all 15 Gemma 87.01 → 85.74, 13.43 → 6.45; Qwen 85.31 → 82.56, 22.54 → 15.52 (Table 2).
- DA matches or beats vanilla on 7 of 15 tasks on Gemma and 5 of 15 on Qwen, many of them at the ceiling on retrieval tasks.
- Category averages: single-span −0.8 (Gemma) / −2.3 (Qwen); multi-span −2.3 / −3.6.
- "Attended tokens" = number of cache positions read, summed over all decoding steps of an answer.

**Transition.** Where does the saving come from?

---

## The Saving Comes from the Mask

**Story.** Fig. 2, three panels, each relative to vanilla (= 100).

- (a) Accuracy: DA 99 and 97, DA no-mask 100 and 99.
- (b) Decoding steps: DA writes *more*: 135 and 131, i.e. 35% and 31% longer answers, because of the extra navigation text.
- (c) Tokens read: DA 48 and 69. DA no-mask 166 and 129: with the same prompt but without the mask, DA costs *more* than vanilla, because the longer answers each read the full context.

So the format alone is free in accuracy but costs efficiency; the mask turns it into a saving.

**Details.**

- Relative to DA no-mask, the mask cuts tokens read by 71% (Gemma) and 47% (Qwen).
- Estimated decoding time relative to vanilla: 0.71 (Gemma) and 0.77 (Qwen) (Table 3). These are roofline estimates on a B200 accelerator at assumed utilizations, not measured times, and exclude reading the prompt (prefill). The saving is smaller on Gemma because its sliding-window layers, which DA cannot mask, take 42% of DA's attention time (5% for Qwen's DeltaNet layers).

**Transition.** Now read the same numbers as psychology.

---

## Efficiency as a Measure of Self-Knowledge

**Story.** The key fact: the engine *enforces* the declaration. In focus mode the model cannot peek at other chunks. So every number on the engineering side is also a behavioural measurement:

- **Tokens saved** measure how narrow the model's declared focus is.
- **The accuracy cost of the mask** (DA no-mask minus DA: 1.3 points on Gemma, 2.1 on Qwen) measures what it costs to hold the model to its own plan. Since DA no-mask uses the same prompt and the same tags, this difference isolates the enforcement.
- **Focus calls that parse** (the declaration names a valid chunk) measure whether the model follows its own protocol.

The argument: if the model's statements about where to look were poor, enforcing them would cost a lot of accuracy. It costs one to two points.

For the psychologists: in Nelson & Narens' (1990) terms, the declaration is a *control* signal (it steers what happens next) that we can also *monitor* (read). And it is a commitment, not a self-report: the model has to live with it. The discussion question is whether a commitment is a better test of self-knowledge than a report.

**Limits of the argument.**

- It is one-directional. A small cost shows the declarations are good enough; it does not show how they are produced. Pattern matching on headings would pass the same test (commentary Q2).
- The declarations are made in global mode, after reading everything.
- Hidden is not gone. The mask blocks direct access to chunk tokens, but the question, the instruction and the model's own earlier notes were processed while all chunks were visible, so their cached states can carry document information into focus and local mode. "No peeking" means "no direct reading" (commentary Q19).
- The model can recover from a bad declaration by going back to global mode (1.4–1.9 focus attempts per answer), so individual declarations are not tested one by one.

**Transition.** Can all models do this?

---

## Scale: Who Can Do This?

**Story.** Fig. 3a: accuracy relative to vanilla grows with model size in both families: Gemma-4 E4B 29%, 12B 91%, 31B 99%; Qwen 4B 64%, 9B 89%, 27B 97%.

Much of the small models' failure is not about knowing where to look but about following the protocol: only 58% of Gemma-4-E4B's focus calls name a valid chunk, against 99% for the largest models (Fig. 6a).

Fig. 3b: tokens read show no clear size trend (Gemma 46–48% of vanilla, Qwen 50–69%), with one outlier: Gemma-4-12B reads 183% of vanilla because about 6% of its answers do not finish within the 8K-token budget; without those it is at 98%.

**Discussion.** Is there a capacity threshold for metacognitive control, or only for instruction-following? The data cannot separate the two.

**Transition.** A framework from psychology for when self-directed judgment works.

---

## When Does Self-Knowledge Work?

**Story.** Kahneman and Klein (2009) settled a long dispute about expert intuition: it is reliable when the environment is regular (cues predict outcomes) and when there is adequate feedback to learn from. Chess players and firefighters qualify; stock pickers and political forecasters do not.

Applied to DA, as a hypothesis:

- **Regularity.** Declarations should work when the answer lives in one place. The paper's two task categories, fixed in advance, show this: the mask costs 0.8 points on single-span tasks and 2.3 on multi-span tasks (Gemma; Qwen 2.3 vs. 3.6). But per task the picture scatters: long-dependency QA, a multi-span task, *improves* on Gemma by 3.2 points.
- **Feedback.** Zero-shot DA gets none: the model never learns from its declarations. The paper's proposed next step, reinforcement learning that rewards accuracy and efficiency (§8.2, §8.4), would supply exactly this. Kahneman–Klein predicts that this is where reliability should grow.

**Framing.** Say "structurally analogous", not "machines show the same bias". The model has no experience, no feedback history, no causal model of its domain.

**Details for questions.** Human introspective reports are unreliable: people confabulate reasons for their choices (Nisbett & Wilson, 1977). DA's declarations differ in that they are prospective and enforced, but they are never checked against the model's actual attention.

**Transition.** Connection to our own work.

---

## Connection: First-Order Steering

**Story.** Our paper (Kunda, Kurz, Dominik, Maoz, *First-Order Steering: Translating Weight Adaptation into Activation Steering*, draft 2026) and DA are two ways of controlling a model at inference time, and they are opposite in almost every respect:

- **Who controls:** in DA, the model itself; in steering, the experimenter.
- **Channel:** DA uses text in the chain-of-thought; steering adds a vector to the residual stream (the internal activations).
- **What changes:** DA changes what the model *reads*; steering changes what it *writes* (its behaviour, e.g. bullet points, analogies, sophisticated language).
- **Legibility:** DA's control is written in words; steering's is read off the Jacobian $J_{\vec s}\, h_\ell$ of a hidden layer with respect to the steering strengths $\vec s$.

**Details.**

- Composition: DA composes by switching modes over time; first-order steering composes behaviours by adding steering vectors, with strengths $\vec s \in [0,1]^n$.
- Training: DA needs none; first-order steering derives its vectors from LoRA adapters merged with HeRD-Merging, which controls the Hessian terms that bound the first-order error.
- The DA paper itself draws the same line: its mask is "read from text rather than inferred from activations" (App. A.5).

**Transition.** Where the two could meet.

---

## Bridges

**Story.** Three research questions:

- **Does the model's real attention follow its declaration?** In the no-mask arm the model writes declarations but attends to everything. Measuring where its attention actually goes, and whether that matches the declared chunk, is a probe-style check of the kind we use for steering vectors. The paper does not do this.
- **Is there a "focus" direction we could steer?** If mode choice is represented in the residual stream, first-order steering could push the model towards more focus and less global mode, i.e. towards more efficiency.
- **Can a prompt be read as a weight update?** Our conclusion suggests relating $J_{\vec s}\, h_\ell$ to the influence of a system prompt. DA's 1,068-token instruction is exactly such a prompt: it changes behaviour without changing weights.

**Details.**

- Attention steering already exists: PASTA (Zhang et al., 2024) reweights attention towards highlighted spans; AutoPASTA lets the model choose them. Both reweight a fully loaded cache and save no memory reads.
- Small Gemma-4 models are the weak spot in both papers: DA collapses at Gemma-4-E4B; first-order steering gains least on Gemma-4-E2B (32.0% vs. 31.3% for the best baseline).

**Transition.** Taking stock.

---

## What the Prompt Reveals

**Story.** The DA instruction (App. F) ends with three "soft requirements". The paper says the instruction gives "usage guidance derived from failure modes observed during prompt development" (§2.1). So each rule tells us what models did before the rule was added:

1. "Skipping focus and guessing from memory is the most common failure mode." Models answered from what they thought they knew instead of looking it up.
2. "Without it, the model often retrieves multiple values and forgets which one the question actually asks for." Models lost track of the goal.
3. "Anything you 'remember' about a magic chunk you didn't focus on is a guess." Models treated vague impressions of unread text as knowledge.

For the psychologists, rules 1 and 3 read like reports of overconfidence: acting as if one knows, without checking. Rule 2 is a commitment device, the "commitment step" in the authors' words.

**Why it matters for the question of the talk.** Part of what looks like self-knowledge in DA is supplied by the prompt: the authors observed the failures and wrote the corrections into the instruction. The model does not discover that its memory is unreliable; it is told. This is the strongest single piece of evidence for "instruction-following rather than metacognition", and also an honest one: the authors document it themselves.

**Connection to local mode.** Opening `<local>` means closing the book, a judgement that one has copied out enough (commentary Q34). Rule 3 exists because models made that judgement badly.

**Caveat.** The paper gives no numbers for these failures, only the rules; "most common failure mode" is the authors' summary of their prompt development, not a measured result.

**Transition.** Taking stock.

---

## Conclusion: One Result, Two Readings

**Story.** Recap by reading the table top to bottom; every row points back to a slide the audience has seen: a way to read less memory (The Problem, Results); an implementation in a standard serving system (The Idea); an evaluation on 15 tasks (Models and Tasks); a conceptual move, choosing what to attend to becomes part of the model's reasoning, which the authors call "system-2 sparse attention"; and, in our reading, evidence about what models know.

Be explicit that the last row is ours: the paper never uses the words "metacognition", "introspection" or "self-knowledge". Its own one-sentence summary (conclusion) is that selective attention turns "from a pattern inferred inside the network into one the model states out loud".

**Answer to the question.** Is the efficiency result a behavioural test of a metacognitive claim? Yes, but a weak one. What it shows: the model's statements about where to look are good enough to be enforced, at a cost of one to two accuracy points. What it does not show: how the statements are produced (pattern matching or metacognition), or whether the model's internal attention follows them.

**Transition.** Now the caveats.

---

## Skeptical Points

**Story.** Five points, one sentence each.

- **"Attention" ≠ attention.** Transformer attention is a weighted lookup over stored tokens, not a capacity-limited spotlight. The psychological word invites more than the mechanism delivers.
- **Instruction-following rather than metacognition?** "Zero-shot" means no training, not no teaching: a 1,068-token instruction teaches the protocol. Small models fail mainly at following it.
- **Declared ≠ verified, and declared after reading everything.** Nobody checks that the model's internal attention matches its declaration; the 99% "focus success" is a parse rate. Declarations are made in global mode, after a full read ("Example"). Humans, too, confabulate reasons (Nisbett & Wilson, 1977).
- **Selected tasks.** The 15 sources are tasks "where selective attention is particularly relevant" (§4). On six further sources DA fails: two lose accuracy (84 → 59% on average), four read more tokens than vanilla (App. D.4, Gemma only). Some sources were skipped because their prompts forbid intermediate reasoning.
- **Projected speed-up, not measured.** 0.71 and 0.77 are roofline estimates; DA writes 31–35% more tokens.

**Further points if time allows.**

- Who is in control? The model proposes; a parser in the engine enforces.
- Artificial segments: static documents are cut into manufactured chunks; the claim that agentic settings (tool calls, conversation turns) give natural segments is argued, not tested.

**Transition.** Open questions.

---

## Discussion

- **Pattern matching or metacognition?** What evidence would distinguish them? Candidates: remove surface cues (headings, shared keywords) and see whether declarations stay accurate; compare declared and actual attention; probe for "where the answer is" before the model writes its declaration.
- **Training.** Prompting is a floor. What would reinforcement learning on accuracy and efficiency add, and would the declarations stay honest, or drift towards whatever the reward favours?
- **Oversight.** The attention plan is legible text: "the tokens that make it auditable are the same tokens that drive the KV reads" (§8.4). Chain-of-thought monitorability is valuable but fragile (Korbak et al., 2025); does enforcement make it less fragile?

---

## References

On the slide. Additional references used in this narrative:

- Kojima, Gu, Reid, Matsuo, Iwasawa: [Large Language Models are Zero-Shot Reasoners](https://scholar.google.com/scholar?q=Large+Language+Models+are+Zero-Shot+Reasoners), 2022.
- Tang et al.: [Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://scholar.google.com/scholar?q=Quest+Query-Aware+Sparsity+for+Efficient+Long-Context+LLM+Inference), 2024.
- Ribar et al.: [SparQ Attention: Bandwidth-Efficient LLM Inference](https://scholar.google.com/scholar?q=SparQ+Attention+Bandwidth-Efficient+LLM+Inference), 2024.
- Zhang et al.: [Model Tells Itself Where to Attend: Faithfulness Meets Automatic Attention Steering](https://scholar.google.com/scholar?q=Model+Tells+Itself+Where+to+Attend+Faithfulness+Meets+Automatic+Attention+Steering), 2024. - - - AutoPASTA.
- Vaswani et al.: [Attention Is All You Need](https://scholar.google.com/scholar?q=Attention+Is+All+You+Need+Vaswani+2017), 2017.
- Turpin, Michael, Perez, Bowman: [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://scholar.google.com/scholar?q=Language+Models+Don%27t+Always+Say+What+They+Think+Unfaithful+Explanations+in+Chain-of-Thought+Prompting), 2023.
- Dao et al.: [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://scholar.google.com/scholar?q=FlashAttention+Fast+and+Memory-Efficient+Exact+Attention+with+IO-Awareness), 2022.
