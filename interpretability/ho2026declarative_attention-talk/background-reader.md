# Background Reader: Language Models Can Control Their Own Attention

---

## Section 1: The Problem — Why Long Contexts Are Expensive

---

### 1.1 Tokens and the Forward Pass

A language model operates on **tokens** — subword units produced by a fixed tokenizer. Common words are single tokens; rare words are split into several. A rough conversion is one token ≈ 0.75 words, so a 1M-token context is approximately 750,000 words, or roughly ten novels.

At each generation step the model computes a single forward pass: a function from the current sequence of tokens to a probability distribution over the vocabulary. The next token is sampled from this distribution and appended to the sequence. Generation is therefore **autoregressive** — each token is conditioned on all previous tokens, including those the model has itself generated. This creates an irreducibly sequential process: token $n$ cannot be generated until tokens $1, \ldots, n-1$ exist.

The forward pass itself has two computationally distinct components that will matter throughout this reader: the **attention layers** and the **feed-forward layers** (FFN). Their cost structures differ, and understanding the difference is prerequisite to understanding what Declarative Attention does and does not save.

---

### 1.2 The Two Phases of Inference

Modern LLM serving separates inference into two phases with different computational characters.

**Prefill** processes the input prompt. All prompt tokens are available simultaneously, so attention over the prompt is computed as a single large matrix operation — every token attending to every preceding token in parallel. Prefill is **compute-bound**: the limiting resource is floating-point throughput (FLOPS), and the GPU's arithmetic units are the bottleneck.

**Decode** generates the response, one token per forward pass. At decode step $t$, only one new token exists — the one just sampled. Attention for this token must be computed against all $t-1$ preceding tokens, but those tokens' intermediate representations have already been computed during prefill (and earlier decode steps). Recomputing them at every step would be wasteful. They are instead cached.

This cache is the central object of the paper.

---

### 1.3 The KV Cache

In the transformer attention mechanism, each token $i$ at each layer $\ell$ produces three vectors: a **query** $q_i^\ell$, a **key** $k_i^\ell$, and a **value** $v_i^\ell$, each computed by a learned linear projection of the token's hidden state. The attention output for token $i$ is:

$$\text{Attn}(q_i, K, V) = \text{softmax}\!\left(\frac{q_i K^\top}{\sqrt{d}}\right) V$$

where $K$ and $V$ are matrices stacking the keys and values of all preceding tokens, and $d$ is the head dimension.

During decode, the query $q_t$ belongs to the new token. The keys and values $k_1, \ldots, k_{t-1}$ and $v_1, \ldots, v_{t-1}$ were computed in previous steps. Rather than recompute them, the inference engine stores them in the **KV cache** — a buffer in GPU memory (specifically High Bandwidth Memory, HBM) that grows by one entry per token per layer as generation proceeds.

The KV cache is purely an optimization: it trades memory for computation, storing intermediate results to avoid recomputing them. Without it, each decode step would require a full forward pass over the entire sequence — $O(t^2)$ total work over a $t$-step generation. With it, the per-step computation is $O(t)$ — one new token's projections plus one attention pass over the cached keys and values.

The cache size for a single sequence scales as:

$$\text{cache size} = 2 \times L_{\text{global}} \times n_{kv} \times d_{\text{head}} \times t \times \text{bytes per element}$$

where $L_{\text{global}}$ is the number of attention layers, $n_{kv}$ is the number of KV heads, $d_{\text{head}}$ is the head dimension, and $t$ is the current sequence length. For Gemma-4-31B at 1M tokens this evaluates to approximately 82 GB — comparable to loading the model's active parameters.

---

### 1.4 Why Decode Is Memory-Bound

The cost asymmetry between prefill and decode is worth stating precisely.

At prefill, the GPU computes attention over a large token matrix simultaneously. The arithmetic intensity — FLOPs per byte of memory traffic — is high. The GPU's compute units are saturated. Time is set by peak FLOPS.

At decode, only one new query vector exists per step. The arithmetic is minimal: one dot product between $q_t$ and each cached key, one weighted sum over cached values. But to compute these, the entire KV cache must be loaded from HBM. The arithmetic intensity is low — a small amount of arithmetic per byte transferred. The GPU's compute units sit mostly idle while the memory bus is saturated. Time is set by peak memory bandwidth.

This is the **roofline model** characterization: an operation is memory-bound when its arithmetic intensity falls below the machine's compute-to-bandwidth ratio, and compute-bound above it. Decode attention is firmly in the memory-bound regime.

A concrete illustration from the paper: Qwen-3.5-397B-A17B at 1M-token context requires loading approximately 15 GB of KV cache per sequence at every decode step — a memory bandwidth requirement comparable to loading the model's 17B active parameters, repeated for every token of the response.

The critical observation is that this cost is **per-sequence and non-amortizable**. FFN parameter loads are shared across all sequences in a batch — doubling the batch size halves the per-sequence FFN cost. KV cache loads are not shared: each sequence has its own cache, loaded independently at every step regardless of batch size. In large-batch long-context serving, attention KV reads therefore dominate total decode time. The paper estimates this at 73% of decode wall-clock time on Gemma-4-31B and 86% on Qwen-3.6-27B, at the context lengths and hardware utilizations they study.

---

### 1.5 The Sparsity Observation and Its Consequences

The expensive full-cache read would be justified if every cached token materially influenced every decode step. Empirically, it does not.

Weston and Sukhbaatar (2019) [Generating Long Sequences with Sparse Transformers](https://scholar.google.com/scholar?q=Generating+Long+Sequences+with+Sparse+Transformers+Child+2019), Zhang et al. (2023) [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://scholar.google.com/scholar?q=H2O+Heavy+Hitter+Oracle+Efficient+Generative+Inference+Large+Language+Models+Zhang+2023), and Tang et al. (2024) [QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://scholar.google.com/scholar?q=QUEST+Query+Aware+Sparsity+Efficient+Long+Context+LLM+Inference+Tang+2024) all demonstrate that after softmax, attention weights concentrate on a small subset of tokens. Most weights are negligibly small. The model is, in effect, attending to a sparse subset of its context at each step.

This motivates **sparse attention**: load and compute only the high-weight subset, skipping the rest. The memory bandwidth and the attention FLOPs both reduce in proportion to the fraction of tokens kept.

The fundamental obstacle is that the sparse subset is unknown before computing full attention. The softmax weights are the output of attending to everything — you cannot know which weights are large without first computing them all. This creates a circularity: to identify which tokens to skip, you must first do the computation you are trying to skip.

---

### 1.6 The Prior Art and Its Shared Limitation

The literature has addressed this circularity through **proxy scoring**: approximate the attention weights without computing them exactly, use the approximation to select a subset, and compute exact attention only over that subset.

The main approaches:

**Static heuristics.** Xiao et al. (2024) [Efficient Streaming Language Models with Attention Sinks](https://scholar.google.com/scholar?q=Efficient+Streaming+Language+Models+Attention+Sinks+Xiao+2024) (StreamingLLM) retains a fixed window of recent tokens plus a small set of "attention sink" tokens at the start of the sequence. Zhang et al. (2023) [H2O: Heavy-Hitter Oracle for Efficient Generative Inference](https://scholar.google.com/scholar?q=H2O+Heavy+Hitter+Oracle+Efficient+Generative+Inference+Large+Language+Models+Zhang+2023) retains tokens with historically high accumulated attention weight. Both are $O(1)$ per step — no scan required — but their fixed rules cannot anticipate which tokens future queries will need, leading to accuracy degradation on tasks requiring access to non-recent, non-prominent tokens.

**Dynamic query-dependent scoring.** Tang et al. (2024) [QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://scholar.google.com/scholar?q=QUEST+Query+Aware+Sparsity+Efficient+Long+Context+LLM+Inference+Tang+2024) scores KV pages by per-page key bounds. Ribar et al. (2024) [SparQ Attention: Bandwidth-Efficient LLM Inference](https://scholar.google.com/scholar?q=SparQ+Attention+Bandwidth+Efficient+LLM+Inference+Ribar+2024) reads a low-rank surrogate of every key. Yang et al. (2025) [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://scholar.google.com/scholar?q=TidalDecode+Fast+Accurate+LLM+Decoding+Position+Persistent+Sparse+Attention+Yang+2025) amortizes the scan across layers. At industry scale, DeepSeek-AI (2025) [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://scholar.google.com/scholar?q=DeepSeek+V3.2+Pushing+Frontier+Open+Large+Language+Models+2025) trains a lightweight indexer that scores and selects tokens at every step. These methods adapt to the query and therefore handle diverse tasks better than static approaches. But they all scan a surrogate of the full context at every decode step. The per-step cost is $O(N)$ with a smaller constant factor — not $O(1)$.

**The shared limitation** across all proxy approaches is that they are **extrinsic**: an external mechanism, separate from the model's reasoning, decides what to attend to. The model has no voice in the selection. The proxy may be wrong, and when it is wrong, the error is silent — the model simply does not see the tokens it needed, and generates a wrong answer with no indication of what happened.

Ho et al. (2026) [Language Models Can Control Their Own Attention](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026) take a different starting point. Rather than asking how to build a better external proxy, they ask whether the model itself already knows which tokens it needs — and whether it can be made to say so.

---

*Section 1 established the engineering problem: at long context, decode is dominated by KV cache memory reads, most of which carry negligible attention weight, yet existing approaches to skipping them still require an O(N) scan by an external proxy at every step. Section 2 introduces the technical mechanism — chain-of-thought reasoning — that DA uses to replace the external proxy with the model's own declarations.*


## Section 2: Chain-of-Thought — Making Reasoning Visible and Executable

---

### 2.1 The Basic Finding

Wei et al. (2022) [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://scholar.google.com/scholar?q=Chain+of+Thought+Prompting+Elicits+Reasoning+Large+Language+Models+Wei+2022) reported a finding that was, at the time, surprising: simply instructing a language model to write out its reasoning before giving an answer dramatically improved accuracy on arithmetic, symbolic reasoning, and commonsense inference tasks. The prompt addition was minimal — something as simple as "let's think step by step" — and the improvement was large, sometimes turning near-random performance into near-human performance on multi-step problems.

The finding was surprising because nothing about the model changed. The same weights, the same architecture, the same training. Only the prompt changed. This implied that the capability was already latent in the model and that the prompt was surfacing it — a point we will return to in Section 3, because the same logic applies to Declarative Attention.

---

### 2.2 What Chain-of-Thought Tokens Actually Are

The first thing to establish precisely is that chain-of-thought tokens are mechanically identical to any other generated tokens. There is no special mode, no separate computation, no architectural change. The model generates reasoning tokens the same way it generates answer tokens: one forward pass per token, sampling from the output distribution, appending to the sequence.

This has two immediate consequences.

**Consequence 1: CoT tokens cost inference time.** Each reasoning token requires a full forward pass. A response with 500 tokens of reasoning before a 50-token answer costs ten times as many forward passes as the answer alone. This is not free. The DA paper explicitly measures this cost — DA generates approximately 35% more tokens than vanilla generation, which is a real overhead that must be weighed against the attention savings.

**Consequence 2: CoT tokens enter the KV cache.** Every generated token has its key and value vectors computed and stored, exactly like prompt tokens. Future tokens attend to reasoning tokens through the same attention mechanism they use to attend to the original prompt. The reasoning trace is not ephemeral — it is a permanent part of the attended context for all subsequent tokens.

Both consequences matter for understanding DA. The first is a cost. The second is the mechanism by which DA works.

---

### 2.3 Three Reasons Chain-of-Thought Works

**Reason 1: Computation budget**

Each decode step — one forward pass — provides a fixed amount of computation. The model cannot think more deeply by using more computation per token; the architecture is fixed. What it can do is use more tokens.

A complex multi-step problem requires more computation than a simple lookup. Without CoT, all of that computation must happen in the forward passes that generate the answer tokens directly. The model gets, say, five forward passes to multiply two three-digit numbers and write the result. With CoT, it gets as many forward passes as it needs to write out the intermediate steps, each step requiring only a small increment of work. The total computation scales with the difficulty of the problem rather than being capped by the length of the answer.

This is a precise computational claim, not a metaphor. The transformer has a fixed depth and width. The only way to increase total computation on a problem is to generate more tokens.

**Reason 2: The context window as external memory**

This is the mechanism most relevant to DA and deserves careful treatment.

A transformer has no persistent internal memory across forward passes. The hidden states computed during step $t$ — the residual stream vectors, the attention outputs, the FFN activations — are used to generate token $t+1$ and then discarded. They do not carry forward. The only information that persists across steps is what appears in the token sequence, because that sequence is what gets attended to.

This means the context window is the model's only working memory. Anything not written into the sequence is lost at the end of the step that computed it.

Without CoT:

```
Step 1: read problem → compute intermediate result → 
        result lives in activations → used to generate answer token
Step 2: activations from step 1 are gone
        only the answer token survives
```

With CoT:

```
Step 1: read problem → compute intermediate result →
        WRITE intermediate result as a token
Step 2: intermediate result is in the sequence
        step 2's attention can read it directly
        step 2 does not need to recompute it
Step 3: same — each step reads from all prior written steps
```

The context window is functioning as a scratchpad in the most literal sense: intermediate computations are written to it and read back from it via attention. The "external memory" framing is not an analogy — the written tokens are genuinely external to the forward pass that reads them, stored in the KV cache and accessed through the attention mechanism.

This has a direct implication for DA. When the model writes:

```
<focus magic_chunks="4">Revenue was $2.4B in Q3</focus>
```

that extracted value enters the KV cache as part of the response. A subsequent `<local>` block can attend to it without touching the document at all. The extraction is durable. The document segment that contained it can be masked away entirely, and the value remains accessible. This is not a special DA feature — it is the standard behavior of the context window as external memory, applied to attention planning.

**Reason 3: Self-conditioning**

The model's own prior output shifts the probability distribution over its next output. Writing "this requires multiplication" makes arithmetic-related continuations more probable. Writing "I need to check section 3" makes section-3-referencing continuations more probable.

This is not an independent mechanism — it follows directly from the attention over prior tokens — but its effect on generation is distinctive. The reasoning trace steers itself forward. Each reasoning step creates the context that makes the next step more likely to be coherent and relevant. A model asked to answer directly must find the right answer in a single distributional step from the question; a model asked to reason can take many small distributional steps, each conditioned on the previous ones.

---

### 2.4 Self-Consistency — Correctness as Convergence

Wei et al.'s original finding established that CoT improves accuracy on average. Wang et al. (2023) [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://scholar.google.com/scholar?q=Self+Consistency+Improves+Chain+of+Thought+Reasoning+Language+Models+Wang+2023) identified a further improvement by exploiting a structural property of reasoning errors.

The observation is simple: there is one correct answer to a well-posed problem, but many possible wrong answers. A reasoning path that makes an error introduces a deviation that is, in some sense, arbitrary — there is no particular reason for the error to take one form rather than another. Correct reasoning paths, by contrast, are constrained — they must all arrive at the same value.

This asymmetry suggests an aggregation strategy. Sample $N$ independent reasoning paths by running generation with nonzero temperature $N$ times. Take the majority answer across paths.

```
Sample 10 paths for "47 × 83 = ?":

Path 1:  47 × 80 = 3760, 47 × 3 = 141, total = 3901  → 3901
Path 2:  47 × 83: 40×83=3320, 7×83=581, total=3901   → 3901
Path 3:  47 × 83 = 120 (error)                        → 120
Path 4:  47 × 83 = 3901                               → 3901
...

Majority answer: 3901 (correct)
```

The correct answer accumulates votes across paths because all correct paths converge to it. Errors are diverse — path 3's error is unlikely to be exactly replicated by other paths — so no wrong answer accumulates enough votes to win the majority.

This principle is structurally identical to several other aggregation mechanisms in mathematics and statistics:

- **Condorcet's Jury Theorem (1785)**: if each voter is independently correct with probability $p > \frac{1}{2}$, majority vote is correct with probability approaching 1 as the number of voters grows.
- **Ensemble methods in machine learning**: Breiman (2001) [Random Forests](https://scholar.google.com/scholar?q=Random+Forests+Breiman+2001) — randomized trees make uncorrelated errors; majority vote over the ensemble outperforms any single tree.
- **Error-correcting codes**: Shannon (1948) showed that redundant transmission over a noisy channel can recover the original message with arbitrary reliability, because noise is random (errors diverse) while the signal is fixed (correct answer consistent).

Self-consistency applies this principle to language model reasoning by using temperature sampling to generate approximately independent paths. The key assumption — that errors are diverse — holds when the model has no systematic bias toward a particular wrong answer. When it does have such a bias (a misconception baked into its weights), all paths make the same error and majority voting fails.

Self-consistency is computationally expensive: $N$ independent generations cost $N$ times a single generation. It is therefore used selectively, for high-stakes problems where accuracy dominates cost. The DA paper does not use self-consistency, but the underlying principle — that consistency across independent instantiations is a signal of correctness — appears in a different form in DA's results, as we discuss in Section 3.

---

### 2.5 From Zero-Shot CoT to Trained Reasoning

The Wei et al. (2022) result was zero-shot: no examples of CoT were shown to the model. The capability was elicited through a single prompt instruction. Subsequent work trained models to produce reasoning traces:

Zelikman et al. (2024) [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://scholar.google.com/scholar?q=Quiet+STaR+Language+Models+Teach+Themselves+Think+Before+Speaking+Zelikman+2024) trained models to generate hidden reasoning tokens between every pair of consecutive tokens, learning to think before speaking at a fine-grained level.

Lightman et al. (2023) [Let's Verify Step by Step](https://scholar.google.com/scholar?q=Let%27s+Verify+Step+by+Step+Lightman+OpenAI+2023) trained process reward models — verifiers that score individual reasoning steps rather than final answers. Models trained against step-level feedback produce better-calibrated reasoning traces than those trained only on final answer correctness.

DeepSeek-AI (2025) [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://scholar.google.com/scholar?q=DeepSeek+R1+Incentivizing+Reasoning+Capability+LLMs+Reinforcement+Learning+2025) and OpenAI (2024) [OpenAI o1 System Card](https://scholar.google.com/scholar?q=OpenAI+o1+System+Card+2024) applied reinforcement learning to reward accurate final answers, allowing models to develop their own reasoning strategies. The resulting models generate long, structured reasoning traces and dramatically outperform their base versions on complex tasks.

The trajectory from Wei et al. (2022) to DeepSeek-R1 is the relevant precedent for DA:

```
Wei et al. 2022:    zero-shot CoT elicited by prompting
                    → significant accuracy improvement
                    → proof of concept for latent capability

DeepSeek-R1 2025:   CoT optimized through RL training
                    → dramatically larger improvements
                    → optimal reasoning strategies learned

Ho et al. 2026:     zero-shot DA elicited by prompting
                    → significant efficiency improvement
                    → proof of concept for latent capability
                    → trained DA is future work
```

The paper explicitly positions its zero-shot results as a lower bound, with trained DA representing the ceiling that future work can approach. Section 8.2 of the paper describes this trajectory in detail.

---

### 2.6 The Extension DA Makes

Standard CoT makes the model's **reasoning** visible as text. The model writes what it thinks. The inference engine does not act on this text — it is just tokens.

DA extends this in one precise direction: it makes the model's **attention plan** visible as parseable text, and the inference engine acts on it.

```
Standard CoT:
Model writes: "The answer involves Q3 revenue figures."
Engine:       generates this text, adds it to KV cache, continues
              nothing changes about what the model attends to

DA:
Model writes: <focus magic_chunks="4">
Engine:       intercepts the closing tag
              rewrites the KV cache block table
              next forward pass loads only segment 4's blocks
              the model literally sees less context
```

The reasoning token has been given **operational semantics** with respect to the attention mechanism. It does not merely express a plan — it executes one.

This is the technical contribution of DA, built entirely on the infrastructure of CoT. The reasoning trace was already there. The KV cache was already there. The PagedAttention block table was already there. DA connects them: it makes the text of the reasoning trace drive the structure of the cache read.

---

*Section 2 established chain-of-thought as the technical substrate of DA: reasoning tokens are mechanically real, they persist in the KV cache, they function as external memory, and they can be given operational semantics that the inference engine acts on. Section 3 turns to the scientific question this raises: for DA to work, the model must already know where to attend — and this is a claim about LLM self-knowledge that connects to a broader literature on machine and human introspection.*


## Section 3: LLM Self-Knowledge — What Do Models Know About Themselves?

---

### 3.1 The Double Nature of the Paper

Ho et al. (2026) [Language Models Can Control Their Own Attention](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026) can be read in two ways simultaneously, and understanding both readings is necessary for understanding what the paper actually establishes.

The **engineering reading**: DA is a technique for reducing KV cache memory reads during decode. It achieves 52% and 31% reductions in attended tokens on two frontier models, translating to estimated wall-clock speedups of 0.71× and 0.77× on optimized hardware. It fits into a specific literature on long-context inference efficiency. The result is an engineering contribution.

The **metacognitive reading**: DA works only if the model already knows, before attending to a segment in focus mode, that the segment contains the information it needs. The efficiency gain is contingent on this self-knowledge being accurate. The accuracy numbers — 98.5% and 96.8% retention of vanilla performance — are not just efficiency metrics. They are the empirical verification that the model's attention declarations are reliable. The result is evidence about LLM self-knowledge.

These readings are not independent. The optimization is the **consequence** of the metacognitive claim being true. If the claim were false — if the model's declarations were no better than random guesses about where relevant information lives — the mask would cut off needed context, accuracy would collapse, and DA would be useless. The fact that accuracy is nearly preserved is what proves the declarations are meaningful.

This section develops the background for the metacognitive reading. It proceeds through three bodies of literature: calibration research, which asks whether models know what they know; introspection research in psychology, which asks whether humans can accurately report their own mental states; and expert intuition research, which identifies the conditions under which self-directed attention is reliable. All three converge on the same conditions that predict where DA succeeds and where it fails.

---

### 3.2 Calibration — The History of Machine Self-Knowledge

**Calibration in general** refers to the alignment between a probabilistic predictor's stated probabilities and empirical frequencies. A forecaster is well-calibrated if, across all instances where they say "70% probability," the event occurs approximately 70% of the time. Calibration is a property of any probabilistic system — weather models, medical diagnostic tools, sports betting odds — and has nothing inherently to do with introspection.

In the context of neural networks, calibration has a specific meaning: does the softmax output probability assigned to the predicted class reflect the model's actual accuracy on examples where it assigns that probability? This is measured with a **reliability diagram**.

**The reliability diagram.** Given a large test set with known ground truth:

1. Collect all predictions with their confidence scores (softmax probabilities)
2. Bin predictions by confidence: $[0.5, 0.6)$, $[0.6, 0.7)$, $\ldots$, $[0.9, 1.0]$
3. Within each bin, compute the fraction of predictions that were correct
4. Plot stated confidence (x-axis) against actual accuracy (y-axis)

A perfectly calibrated model produces points on the diagonal: stated confidence equals actual accuracy at every level. An overconfident model produces points below the diagonal — it says 90% confident when it is actually right only 70% of the time. An underconfident model produces points above the diagonal.

```
Actual
Accuracy
  1.0 │                              ╱ ← perfect calibration
      │                         ╱
      │                    ╱
  0.8 │               ╱
      │    ●──────────────────────────── overconfident model
      │  ●        ╱
  0.6 │●      ╱
      │    ╱     ← gap at high confidence
      │ ╱           (says 0.95, right only 0.74)
  0.4 │
      └──────────────────────────────────
         0.5   0.6   0.7   0.8   0.9   1.0
                              Stated Confidence
```

**The Guo et al. finding.** Guo et al. (2017) [On Calibration of Modern Neural Networks](https://scholar.google.com/scholar?q=On+Calibration+of+Modern+Neural+Networks+Guo+2017) compared shallow networks from the 1990s and early 2000s against modern deep networks (ResNet, VGG, DenseNet) on image classification. The older networks were approximately well-calibrated. The modern networks were severely overconfident, particularly at high confidence values — a model saying 95% confident was right only around 74% of the time.

The gap grew with model depth, model size, and training duration. More accurate models were more miscalibrated. The properties that made networks perform better — depth, width, batch normalization, weight decay, extended training — simultaneously made their confidence scores less trustworthy.

The mechanism is the cross-entropy training objective. This loss rewards pushing the correct class probability toward 1.0 and all others toward 0.0. Given sufficient capacity and training time, the network learns to output extreme probabilities, because extreme outputs minimize the loss on the training distribution. Accuracy saturates; confidence continues to inflate.

**Why this matters: wrong confidently.** The practical consequence is a failure of legibility. A well-calibrated model's confidence score is a useful signal: predictions above 90% confidence can be trusted; predictions below 60% should be checked. Downstream systems can use this signal to route low-confidence predictions for human review.

An overconfident model's confidence score loses this utility. Its errors arrive wearing the same costume as its correct predictions — high confidence scores — and are therefore invisible to any threshold-based review mechanism. The safety valve that confidence was supposed to provide is disabled. The model gets better at the task while getting worse at knowing when it is wrong.

This is not merely a statistical nuisance. In deployed systems — medical diagnosis, legal document review, financial analysis — the failure mode is that errors accumulate silently, dressed in high confidence, while the review mechanism that would catch them has been turned off by the model's own overconfidence.

**Temperature scaling.** Guo et al.'s practical contribution was showing that a single scalar post-hoc fix largely corrects this. Dividing the logits by a temperature parameter $T > 1$ before softmax flattens the output distribution, reducing confidence without changing rankings. Fitting $T$ on a small validation set and applying it at test time substantially improves calibration while leaving accuracy unchanged. The model's ability to discriminate (rank correct answers above wrong ones) is unaffected; only the sharpness of the probability outputs changes.

---

### 3.3 Introspective Calibration in Language Models

The Guo et al. result concerns the calibration of softmax output probabilities. For language models, a different and more interesting question arises: when a model writes "I am fairly confident the answer is Paris" or "I think it was around 1850, though I am not certain," do these verbal expressions of confidence track actual accuracy?

This is **introspective calibration** — distinct from token probability calibration. The two can come apart, and the direction of the discrepancy reverses with scale.

**Token probability calibration** in LLMs follows the Guo et al. pattern: larger models assign more extreme probabilities and are more overconfident in this sense. This worsens with scale.

**Verbal introspective calibration** shows the opposite pattern. Kadavath et al. (2022) [Language Models (Mostly) Know What They Know](https://scholar.google.com/scholar?q=Language+Models+Mostly+Know+What+They+Know+Kadavath+2022) found that large language models, when asked to evaluate whether their own answers are correct, are surprisingly accurate at this self-assessment — and the accuracy improves with model scale. A large model that writes "I'm not sure about this" is genuinely more likely to be wrong than when it writes "I'm confident." The verbal signal, unlike the token probability, becomes more reliable as models grow.

The mechanism is indirect. During pretraining, the model processes vast amounts of text in which confident language ("X is definitely Y," "the capital is certainly Z") tends to appear around reliably true facts, while hedged language ("I think," "approximately," "around") tends to appear around uncertain or contested facts. The model learns statistical associations between linguistic confidence markers and factual reliability. When generating text, it reproduces these associations — not through any explicit computation of its own uncertainty, but through pattern matching on the distributions it was trained on.

This indirect mechanism has clear limits. It works for facts that appear frequently and consistently in training data, where the linguistic confidence pattern is reliable. It fails for rare facts (weak training signal), contested facts (mixed linguistic patterns), and precise numerical details (dates, measurements, statistics) where confident-sounding approximations are common even when wrong.

**Attempts to improve introspective calibration through training.** Several approaches have been explored:

Zhang et al. (2024) [R-Tuning: Instructing Large Language Models to Refuse Unknown Questions](https://scholar.google.com/scholar?q=R+Tuning+Instructing+Large+Language+Models+Refuse+Unknown+Questions+Zhang+2024) fine-tune models on data labeled for whether the question falls within the model's knowledge, training the model to say "I don't know" on out-of-distribution questions. This works for the binary known/unknown distinction but does not produce graded calibrated confidence.

Lightman et al. (2023) [Let's Verify Step by Step](https://scholar.google.com/scholar?q=Let%27s+Verify+Step+by+Step+Lightman+2023) train process reward models that evaluate individual reasoning steps. Models trained with step-level feedback produce better-calibrated reasoning, because the training signal connects specific intermediate claims to their downstream correctness.

CoT-based uncertainty elicitation asks the model to reason explicitly about the basis of its confidence before stating it — not just "how confident am I?" but "have I seen this fact directly? Am I inferring or remembering? What could go wrong?" Band et al. (2024) [Linguistic Calibration of Long-Form Generations](https://scholar.google.com/scholar?q=Linguistic+Calibration+Long+Form+Generations+Band+2024) show this improves calibration on long-form answers. The mechanism is that reasoning about uncertainty forces the model to represent the basis of its confidence rather than simply reproducing a confidence-level pattern.

The honest state of the art: introspective calibration can be improved through training, but the improvement is domain-dependent, does not generalize reliably to out-of-distribution question types, and the mechanism remains indirect — training on outputs, not on internal states.

---

### 3.4 Retrospective vs Prospective Self-Knowledge

The calibration literature is concerned with **retrospective** self-knowledge: given that the model has already produced an answer, how accurately can it assess whether that answer is correct? This is self-knowledge looking backward — evaluating a completed act.

DA requires a different kind of self-knowledge: **prospective** self-knowledge. Before attending to any specific segment, the model must declare which segment contains the relevant information. It must know, in advance, where to look — not evaluate, after the fact, whether it looked in the right place.

Prospective self-knowledge is harder to study and less studied. It requires the model to have a representation not just of what it knows, but of where in its context the information it needs is located — a spatial or structural representation of its own knowledge state.

The verification is also different in kind. Retrospective calibration is measured statistically: across many instances where the model expresses 80% confidence, is it correct 80% of the time? The signal is aggregated over many examples. Prospective DA declarations are verified operationally: the model declares segment 4, the engine masks everything else, and the model either answers correctly or not. Each declaration is individually testable. Wrong declarations immediately produce wrong answers, with no aggregation required.

This makes DA's accuracy numbers a cleaner test of self-knowledge than calibration results. The 98.5% accuracy retention on Gemma-4-31B means that on 98.5% of questions, the model's prospective declaration — this is where I need to look — was correct enough to produce a right answer. The declaration was not merely correlated with correctness; it was causally necessary for it, since the engine masked everything the declaration excluded.

---

### 3.5 Human Introspection — A Cautionary Parallel

Before concluding that DA demonstrates genuine model self-knowledge, it is worth noting that human introspective reports are themselves unreliable in ways that psychologists have documented carefully.

Nisbett and Wilson (1977) [Telling More Than We Can Know: Verbal Reports on Mental Processes](https://scholar.google.com/scholar?q=Telling+More+Than+We+Can+Know+Verbal+Reports+Mental+Processes+Nisbett+Wilson+1977) showed that people routinely confabulate reasons for their choices and judgments. When asked why they preferred one object over another, subjects produced confident verbal explanations that bore no causal relationship to the actual determinants of their choice — which Nisbett and Wilson identified through experimental manipulation. The verbal report was not a readout of the underlying process but a post-hoc reconstruction that felt accurate but was not.

This is the risk for DA as well. When a model writes `<global>Magic Chunk 4 contains the SFT section</global>`, is this a genuine readout of some internal representation of document structure? Or is it a plausible-sounding declaration constructed from surface cues in the question and document headers, which happens to be correct often enough to maintain accuracy?

The paper cannot definitively resolve this question, and does not claim to. What it does establish is the operational fact: the declarations are correct at a rate (97-99% at the largest scales) that is far above chance and sufficient to maintain near-vanilla accuracy. Whether the mechanism is genuine introspection or sophisticated pattern matching on document structure cues is an open question — and arguably not the most important one for the engineering application. But it is the right question for the scientific reading of the paper.

---

### 3.6 Expert Intuition and the Conditions of Reliable Self-Direction

The most useful framework for understanding where DA works and where it fails comes not from the calibration literature but from the psychology of expert intuition.

Kahneman and Klein (2009) [Conditions for Intuitive Expertise: A Failure to Disagree](https://scholar.google.com/scholar?q=Conditions+Intuitive+Expertise+Failure+Disagree+Kahneman+Klein+2009) synthesized two research traditions that had reached apparently opposite conclusions about expert judgment. Klein's naturalistic decision-making research found that experienced practitioners — firefighters, chess players, intensive care nurses — make remarkably accurate rapid judgments that outperform formal analysis. Kahneman's heuristics and biases research found that experts are systematically overconfident and make predictable errors. Both were right, because they were studying different domains.

Their resolution: the reliability of expert intuition depends on two properties of the domain.

**Condition 1: Environmental regularity.** The environment must be sufficiently regular that cues reliably predict outcomes. Chess is maximally regular — the same position always has the same optimal continuation. Weather is moderately regular — atmospheric physics is consistent even if chaotic. Political outcomes are irregular — historical cues have weak and unstable predictive relationships to outcomes.

**Condition 2: Feedback quality.** The expert must receive rapid, clear, unambiguous feedback that allows learning. A chess player knows immediately whether a move was good (the game's outcome) or bad (losing material). A radiologist learns within days or weeks whether a diagnosis was correct (biopsy results). A political forecaster may wait years for feedback, and even then can reinterpret the outcome as consistent with the prediction.

Domains meeting both conditions — chess, weather forecasting, radiology, firefighting — produce experts whose intuitions are well-calibrated and reliable. Domains meeting neither — political forecasting, clinical psychology, financial prediction — produce experts who are confidently wrong, often more so than novices because expertise brought confidence without bringing accurate calibration.

**The mapping onto DA tasks.** The Kahneman-Klein framework predicts the pattern of DA results almost exactly.

Tasks with regular environments and clear feedback:

```
Passkey retrieval:
  Environment: maximally regular — one target in uniform noise
  Feedback: binary, immediate — model finds it or doesn't
  DA result: 0pp accuracy drop, perfect performance maintained

Code repository QA:
  Environment: regular — functions have names, files have structure
  Feedback: clear — function behavior is deterministic
  DA result: 0pp accuracy drop on Gemma, +5.6pp improvement on Qwen

Meeting transcript QA:
  Environment: moderately regular — statements are attributed to speakers
  Feedback: reasonably clear — specific decisions are on record
  DA result: 0pp accuracy drop
```

Tasks with irregular environments or diffuse information:

```
Sentiment aggregation (space_digest):
  Environment: irregular — relevant information distributed across all reviews
  No single location to declare
  DA result: 2.4pp accuracy drop, largest in the study

Multi-span reasoning:
  Environment: irregular — answer requires combining distant passages
  Declaring one segment is structurally incomplete
  DA result: 2.28pp category-average drop on Gemma

Long-dependency QA:
  Environment: irregular — connection between passages is implicit
  DA result: 1.8pp accuracy drop
```

The correlation between environment regularity and DA accuracy retention is not incidental. It reflects the same underlying condition: self-directed attention is reliable when the environment has a structure that maps onto the available attention modes. DA's three modes — global survey, focused extraction, local synthesis — fit tasks where the answer lives in a locatable region. They fit poorly when the answer is synthesized from a distribution over the entire context.

**The scale parallel.** Kahneman and Klein note that expertise improves calibration, but only in regular environments with good feedback. In irregular environments, more experience brings more confidence without improving accuracy — the expert overconfidence finding.

DA shows an analogous pattern. Larger models retain more vanilla accuracy under DA, with the gap closing monotonically from 29% retention at Gemma-4-E4B to 99% at Gemma-4-31B. This improvement is most pronounced on regular-environment tasks; irregular-environment tasks show less improvement with scale. Larger models have better-developed representations of document structure — more "expertise" at navigation — and this translates to better attention declarations on tasks where document structure is the relevant cue.

**The legibility fix.** The most direct parallel between the Kahneman-Klein framework and DA concerns the role of legibility in error detection.

The overconfident expert — the political forecaster, the overconfident physician — fails silently. Their errors arrive with high confidence and are invisible until the outcome reveals them, often too late. The confidence score, even if nominally present, does not discriminate errors from correct predictions.

DA replaces the confidence score with a legible declaration. When the model writes `<global>Magic Chunk 4 contains the founding date</global>` and focuses on chunk 4, the declaration is auditable. If chunk 4 does not contain the founding date, the error is traceable — not to a miscalibrated probability score, but to a specific, readable claim that was wrong. The paper notes this explicitly in Section 8.4: "The attention plan is also legible by construction: the tokens that make it auditable are the same tokens that drive the KV reads, a property that serves oversight as much as efficiency."

This is what calibration research has sought and failed to fully achieve — a mechanism by which model errors are legible rather than dressed in confident-looking outputs. DA achieves it not by improving calibration but by replacing the calibration problem with a different architecture: explicit declarations whose correctness is operationally verifiable rather than statistically estimated.

Fischhoff et al. (1977) [Knowing with Certainty: The Appropriateness of Extreme Confidence](https://scholar.google.com/scholar?q=Knowing+with+Certainty+Appropriateness+Extreme+Confidence+Fischhoff+Slovic+Lichtenstein+1977) documented that human confidence intervals are systematically too narrow — people say 90% confident when they should say 60%. Tetlock (2005) [Expert Political Judgment: How Good Is It? How Can We Know?](https://scholar.google.com/scholar?q=Expert+Political+Judgment+How+Good+Is+It+How+Can+We+Know+Tetlock+2005) showed that political experts barely outperform chance on long-horizon predictions while expressing strong confidence. Both findings turn on the same structural problem: the confidence score is not verifiable at the time it is expressed, so it is never properly corrected.

DA's declarations are verifiable at the time they are acted on. The engine focuses on the declared segment. The model answers correctly or not. The feedback is immediate. This is the feedback structure that Kahneman and Klein identified as necessary for calibration — and it is built into DA's architecture by construction.

---

*Section 3 established the scientific context for DA's results: the paper is simultaneously an engineering contribution and evidence about LLM self-knowledge. The accuracy numbers verify that model attention declarations are prospectively reliable at a rate that existing calibration methods for retrospective self-assessment have not achieved. The pattern of results — where DA works and where it fails — follows the Kahneman-Klein conditions for reliable self-directed attention. Section 4 turns to the technical implementation: how declarations become executable, how the inference engine intercepts them, and how the KV cache is modified in real time.*


## Section 4: Declarative Attention — How It Works

---

### 4.1 The Protocol

Declarative Attention is a **protocol** — a structured convention governing how the model reasons and how the inference engine responds to that reasoning. It has two sides: a prompting side that elicits structured declarations from the model, and an execution side that intercepts those declarations and modifies the attention computation accordingly.

The protocol partitions generation into three modes, each with a distinct attention scope and a distinct reasoning purpose.

**Global mode** (`<global>`) attends to all context segments simultaneously. It is the default mode, used for navigation: surveying the full context to locate which segment contains the information needed for the next reasoning step. The model uses global mode to orient itself — identifying where to look next, briefly noting why a particular segment is relevant — without extracting specific values or performing synthesis.

**Focus mode** (`<focus magic_chunks="K">`) attends only to the named segment(s) plus a set of always-attended scaffold regions described below. It is the mode for extraction: reading a specific segment to pull out a verbatim value, date, name, or short phrase that the question requires. The model commits to a specific region and reasons within it.

**Local mode** (`<local>`) attends to none of the context segments — only the scaffold and the model's own response generated so far. It is the mode for synthesis: planning over the question, performing arithmetic, combining previously extracted values, and committing to a final answer. In local mode the model cannot see the document at all; it works entirely from what it has already written into its response.

A response to a question about an SFT training corpus (taken directly from Figure 1 of the paper) illustrates the three modes in sequence:

```
<global>
I need to find the number of instruction-response pairs 
used in the Supervised Fine-Tuning (SFT) stage. 
Magic Chunks 1 contains the "Supervised fine-tuning" section.
</global>

<focus magic_chunks="1">
The SFT stage uses 15K regenerated math answers 
and 1.5k open-domain conversations.
</focus>

<local>
The final SFT training corpus was created by merging 
the regenerated math solutions (15k) with the 
open-domain conversations (1.5k). 
Total = 15,000 + 1,500 = 16,500.
</local>

<answer>16,500</answer>
```

The global step navigates to the right segment. The focus step extracts the two numbers verbatim. The local step performs the arithmetic and commits to the answer. At each step, the inference engine has modified the KV cache to match the declared scope — the global step loads all segments, the focus step loads only segment 1, the local step loads no segments.

---

### 4.2 The Prompt Structure

DA requires a specific prompt structure that makes the context addressable. The prompt has two regions with different visibility properties.

**The scaffold** is always attended in every mode. It contains three components:

- A short fixed **system instruction** at the very start of the prompt ("You are a helpful assistant."). Its role is to occupy the attention sink — the first few tokens of a sequence, which empirically receive disproportionate attention weight regardless of content. Placing content-free scaffolding here ensures that context never enters the attention sink, which would make it permanently attended and therefore un-maskable.

- The **question** — the user's query. Always visible so the model never loses sight of what it is answering.

- The **DA instruction** — a structured prompt (reproduced in full in Appendix F of the paper) that defines the three modes, their syntax, and guidance on when to use each. Always visible so the model can refer to the protocol at any point.

**The context** is the long input the model reasons over. This is the variable region — the part whose visibility the DA state machine controls step by step. It holds the vast majority of tokens in long-context tasks.

---

### 4.3 Context Delivery as Magic Chunks

For focus mode to work, the model must be able to name specific regions of the context. This requires dividing the context into addressable segments with stable, trackable names.

The paper calls these segments **magic chunks** — deliberately arbitrary names chosen so the model does not conflate them with the document's own structural divisions (chapters, sections, parts). The context is delivered as a simulated tool-use conversation: for each segment, an assistant turn appears to call a `get_magic_chunk` tool, and a tool response returns the segment text headed "Magic Chunk N." The full document is present from the start — no tool is actually executed — but the formatting places segment boundaries on the special tokens that delimit tool messages, which are boundaries the model encountered throughout instruction-tuning and tracks reliably.

**Segmentation** targets 2048-token units, splitting only at semantic boundaries to avoid cutting mid-sentence or mid-argument. The segmenter descends a hierarchy of delimiters: paragraph breaks first, then single newlines, then sentence boundaries, then clause boundaries, then word boundaries. A segment edge never falls inside a word. The result is an exact partition of the context — concatenating all segments reproduces the original text without loss.

The choice of 2048 tokens is not arbitrary. It is large enough that most questions require only one or two focus steps (the answer is likely contained within a single segment), and small enough that focusing on one segment provides substantial masking of the rest (a 10-segment context masks 90% of tokens in focus mode).

---

### 4.4 The State Machine

The execution side of DA is a **state machine** — a persistent software component running alongside the inference engine that watches the model's output stream and updates the attention mask at mode transitions.

A state machine is defined by a set of states, a set of transition triggers, and the actions taken on each transition. DA's state machine has three states corresponding to the three modes:

```
States: GLOBAL (default), FOCUS(K), LOCAL

Transitions:
  Any state → FOCUS(K):  on closing ">" of <focus magic_chunks="K">
  Any state → LOCAL:     on closing ">" of <local>
  FOCUS or LOCAL → GLOBAL: on closing tag </focus> or </local>

Actions on transition:
  → FOCUS(K): rewrite block table to keep only segment K blocks
               plus always-attended regions
  → LOCAL:    rewrite block table to keep only always-attended regions
               (no context segments)
  → GLOBAL:   restore full block table (all segments)
```

The state machine is initialized in GLOBAL mode. It reads the token stream one token at a time. When it detects a transition token sequence — specifically the closing `>` character of an opening tag — it fires the corresponding transition and rewrites the block table before the next forward pass begins.

**Timing is critical.** The block table rewrite happens **between** forward passes, not during one. When the model generates the closing `>` of `<focus magic_chunks="4">`, that token is the output of one forward pass (which ran under whatever mask was previously active). The state machine then rewrites the block table. The next forward pass — which generates the first token of the focused content — runs under the new, reduced mask. There is no mid-pass intervention; the mask is always consistent within a single forward pass.

**Always-attended regions.** Three regions remain in the block table regardless of mode:

1. The first 16 tokens of the prompt (the attention sink / system instruction)
2. The question and DA instruction at the end of the prompt
3. The entire response generated so far

The third region is what makes local mode useful. When the model is in local mode — attending to no context segments — it can still read back everything it has written into its response, including the verbatim values extracted in prior focus steps. The external memory function of CoT (Section 2.3) is what enables local mode to do real work.

---

### 4.5 PagedAttention and the Block Table

To understand precisely what the state machine does when it "rewrites the block table," it is necessary to understand how vLLM manages KV cache memory.

Kwon et al. (2023) [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://scholar.google.com/scholar?q=Efficient+Memory+Management+Large+Language+Model+Serving+PagedAttention+Kwon+2023) introduced PagedAttention, now the standard approach in production LLM serving. The central observation is that naive KV cache management wastes memory through fragmentation and over-allocation: if you reserve a contiguous memory region large enough for the maximum possible sequence length, most of it sits empty for shorter sequences.

PagedAttention addresses this by treating KV cache memory like virtual memory in an operating system. Physical GPU memory is divided into fixed-size **blocks**, typically 16 to 32 tokens' worth of key and value vectors. Each sequence is assigned a **block table** — a list of pointers to the physical blocks that hold its tokens. Blocks need not be contiguous; they are linked through the table.

```
Physical memory:
  Block 3:  [tokens 32-47 of sequence A]
  Block 7:  [tokens 0-15  of sequence A]
  Block 11: [tokens 16-31 of sequence A]
  Block 2:  [tokens 0-15  of sequence B]
  ...

Block table for sequence A:
  [ptr→Block 7, ptr→Block 11, ptr→Block 3]
  (logical order: 0-15, 16-31, 32-47)
```

The attention kernel follows the block table to load key and value vectors. It does not know or care about physical layout — it reads whatever blocks the table points to, in order.

**DA's masking operation** is a rewrite of this block table. When the state machine transitions to focus mode on segment 4, it rewrites sequence A's block table to contain only the blocks belonging to segment 4, the scaffold blocks, and the response blocks. The blocks for segments 1, 2, 3, 5, 6, ... remain in physical memory — they are not evicted or deleted. They simply do not appear in the block table that the attention kernel reads.

```
Full block table (GLOBAL mode):
  [scaffold_blocks | seg1_blocks | seg2_blocks | seg3_blocks |
   seg4_blocks | seg5_blocks | ... | response_blocks]

Rewritten block table (FOCUS on segment 4):
  [scaffold_blocks | seg4_blocks | response_blocks]

Blocks for segments 1,2,3,5,... still exist in memory.
They are hidden, not deleted.
```

The kernel loads whatever is in the table and computes attention over exactly those blocks. Since fewer blocks are listed, fewer bytes are transferred from HBM. The memory bandwidth saving is proportional to the fraction of blocks removed from the table.

**Reversibility** is an important property that distinguishes DA from eviction-based methods. Because masked blocks are never deleted, returning to global mode requires only restoring the full block table — an $O(1)$ operation. Eviction-based methods (H2O, SnapKV) permanently remove KV cache entries. If a later decode step needs an evicted token, it must be recomputed from the original text — a re-prefill operation that is expensive and disrupts serving. DA never incurs this cost.

---

### 4.6 Block Alignment

vLLM's attention kernels read entire blocks. A block is the minimum unit of memory access — the kernel cannot load half a block. This means masking only saves bandwidth if it removes entire blocks. Dropping scattered individual tokens while keeping their blocks would leave memory reads unchanged; only the arithmetic would be skipped, and attention is memory-bound, not compute-bound.

The state machine therefore rounds the mask to **block boundaries**. When a segment boundary does not coincide with a block boundary, the state machine keeps the full block containing the boundary, even if some tokens in that block belong to an adjacent (masked) segment. This is a conservative choice: it guarantees that no declared token is ever dropped, at the cost of loading a few extra tokens at each segment edge.

The overhead is small. A block is 16-32 tokens; a segment is 2048 tokens. At most two extra blocks are kept per segment edge (one at each end), adding at most 64 tokens against a 2048-token segment — approximately 3% overhead on the kept content, and zero effect on the masked content.

Block alignment means the kernel receives a standard, legal block table and runs without modification. Dao et al. (2022) [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://scholar.google.com/scholar?q=FlashAttention+Fast+Memory+Efficient+Exact+Attention+IO+Awareness+Dao+2022) and its successors run unchanged. DA does not require custom attention kernels.

---

### 4.7 The Autoregressive Loop With DA

Putting the pieces together, here is the complete decode loop with DA active:

```
Initialize:
  State machine: mode = GLOBAL
  Block table: all blocks (full context)

LOOP at each decode step t:

  1. Build attention metadata:
     DA hook intercepts metadata construction
     Reads current state machine mode
     Rewrites block table accordingly
     Passes modified metadata to kernel

  2. Run forward pass:
     Query q_t computed for the new token
     Keys and values loaded from blocks in (modified) block table
     Attention computed over loaded blocks only
     FFN computed
     Logits produced

  3. Sample token from logits → token_t

  4. State machine inspects token_t:
     Is token_t part of a transition sequence?
     If yes and transition complete:
       Update mode
       Rewrite block table for new mode
     If no: leave block table unchanged

  5. Append token_t to sequence
     Compute and store k_t, v_t in KV cache
     (always stored, regardless of current mode)

  6. Go to step 1
```

Note step 5: key and value vectors for every generated token are always stored in the KV cache, regardless of mode. DA never prevents a token's KV from being cached — it only controls which cached tokens are loaded by the attention kernel in subsequent steps. A token generated in local mode is still cached and will be attended to by all future tokens (it is in the response region, which is always attended).

**A concrete trace.** Following the SFT example from Section 4.1:

```
Steps 1-6:   Generate "<global>" 
             State: GLOBAL, full block table
             
Steps 7-40:  Generate "I need to find..."
             State: GLOBAL, full block table
             All 12 context segments visible

Steps 41-43: Generate "</global>"
             State: GLOBAL (closing tag reverts to default)
             
Steps 44-50: Generate "<focus magic_chunks="1">"
             On closing ">": TRANSITION to FOCUS(1)
             Block table rewritten: only segment 1 blocks kept
             
Steps 51-80: Generate "The SFT stage uses 15K..."
             State: FOCUS(1), only segment 1 visible
             86.5% reduction in attended tokens per step

Steps 81-88: Generate "</focus>"
             TRANSITION back to GLOBAL
             
Steps 89-95: Generate "<local>"
             On closing ">": TRANSITION to LOCAL
             Block table rewritten: no context segments
             Only scaffold + response visible
             
Steps 96-130: Generate "The final SFT training corpus..."
              State: LOCAL, no context segments
              95.6% reduction in attended tokens per step
              Model reads back extracted values from response

Step 131:    Generate "<answer>16,500</answer>"
             Final answer produced
```

The reduction figures in the paper (86.5% and 95.6% for the focus and local steps respectively) are exact for this example: the prompt is 25,466 tokens total, segment 1 is approximately 2,311 tokens plus scaffold, and local mode sees only the scaffold and response.

---

### 4.8 Scope and What DA Does Not Touch

DA's mask applies only to **global attention layers** — the layers whose per-step KV read grows with context length. Both headline models also contain efficient attention layers whose per-step cost is bounded independently of context length:

- **Gemma-4-31B**: 10 global attention layers and 50 sliding window attention (SWA) layers. SWA at each layer attends only to a fixed window of 1,024 tokens. Its per-step cost is constant regardless of total context length. DA leaves SWA layers unmodified.

- **Qwen-3.6-27B**: 16 global attention layers and 48 Gated DeltaNet (GDN) layers. GDN is a linear attention variant that maintains a fixed-size recurrent state. Its per-step cost is constant. DA leaves GDN layers unmodified.

The always-on cost of these efficient layers — 838.9 MB per step for Gemma's SWA cache, 78.45 MB per step for Qwen's GDN state — is why the attended-token savings do not translate one-for-one into wall-clock savings. On Gemma, the SWA floor is 42% of DA's total attention time; reducing the global read by half leaves the SWA cost unchanged, limiting the net speedup. On Qwen, the GDN state is only 5% of attention time, so the global saving passes through with little dilution.

This scope limitation is a property of current hybrid architectures, not of the DA protocol. A purely global attention model would see larger proportional savings. Conversely, as architectures shift more layers to efficient attention, the share of decode time that DA can affect will shrink — unless context windows and batch sizes grow proportionally, which recent trends suggest they will.

---

*Section 4 established the complete technical picture of DA: the three-mode protocol, the prompt structure that makes context addressable, the state machine that intercepts mode declarations and rewrites the block table, the PagedAttention substrate that makes block-level masking efficient, and the scope limitations imposed by hybrid architectures. Section 5 turns to the experimental validation: which models were tested, which tasks, how accuracy was measured, and what the results show.*


## Section 5: Experiments and Results

---

### 5.1 Models

The paper evaluates DA on six models across two families, chosen to represent the current frontier of publicly available instruction-tuned models with long-context support.

**The Gemma 4 family** — Gemma Team et al. (2026) [Gemma 4 Technical Report](https://scholar.google.com/scholar?q=Gemma+4+Technical+Report+Gemma+Team+2026):

- **Gemma-4-31B** — 31 billion parameters, the primary headline model. Hybrid architecture: 10 global attention layers and 50 sliding window attention layers (1,024-token window). Supports 256K input tokens natively. Per-token global KV cache: 81,920 bytes in bf16.

- **Gemma-4-12B** — 12 billion parameters. Same architectural family, intermediate scale.

- **Gemma-4-E4B** — approximately 4 billion active parameters. The smallest model in the study. Supports 128K tokens (half the others). Used in the scaling analysis to establish the lower end of the capability range.

**The Qwen 3 family** — Qwen Team (2026) [Qwen3.5: Towards Native Multimodal Agents](https://scholar.google.com/scholar?q=Qwen3.5+Towards+Native+Multimodal+Agents+Qwen+Team+2026):

- **Qwen-3.6-27B** — 27 billion parameters, the primary headline model from this family. Hybrid architecture: 16 global attention layers and 48 Gated DeltaNet linear attention layers. Supports 256K tokens. Per-token global KV cache: 65,536 bytes in bf16.

- **Qwen-3.5-9B** — 9 billion parameters. Intermediate scale in the Qwen family.

- **Qwen-3.5-4B** — 4 billion parameters. The smallest Qwen model, used to anchor the lower end of the Qwen scaling curve.

The two families were chosen deliberately to represent different architectural approaches to hybrid attention — SWA on Gemma, GDN on Qwen — ensuring that DA's results are not an artifact of one particular efficient-layer design.

All models are served in non-thinking mode. Preliminary experiments showed that models fail to follow the DA protocol within thinking traces — the free-associative reasoning style of thinking mode overrides the structured tag syntax DA requires. The paper flags this as a limitation and discusses it in Section 8.2: models trained to use tool calls within thinking traces (as several frontier models now do) should be able to integrate DA tags naturally.

All models are served on NVIDIA B200 GPUs via vLLM with the custom DA integration described in Section 4. Sampling follows each model family's recommended parameters: temperature 1.0, top-$p$ 0.95, top-$k$ 64 for Gemma; temperature 0.7, top-$p$ 0.80, top-$k$ 20, presence penalty 1.5 for Qwen.

---

### 5.2 The Three Experimental Arms

Every task and model combination is evaluated under three conditions, allowing the contribution of each component to be isolated.

**Vanilla** serves the raw context inline with the question and a brief instruction to wrap the final answer in `<answer>` tags, with full causal attention. This is the baseline: no chunking, no DA protocol, no masking. It represents standard long-context inference.

**DA-no-mask (DAnm)** uses the full DA prompt template — magic chunk formatting, three-mode instructions, the complete DA protocol — but with full causal attention. The model generates global, focus, and local blocks, but the inference engine does not intercept mode transitions or modify the block table. Every forward pass reads the full KV cache regardless of what mode the model declared.

DAnm is the critical ablation. The gap between Vanilla and DAnm isolates the effect of the chunked prompt format alone. The gap between DAnm and DA isolates the effect of the attention mask alone.

**DA** uses both the DA prompt and the DA state machine with block table rewriting. This is the full method.

The three arms share the same final-answer specification and `<answer>` tag convention, so the evaluation judge scores them on identical criteria.

---

### 5.3 Benchmarks

The evaluation spans 15 long-context sources drawn from five benchmark suites, chosen to cover a wide range of context lengths, domains, and task structures. The history and character of each suite matters for interpreting where DA succeeds and where it does not.

**RULER** — Hsieh et al. (2024) [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://scholar.google.com/scholar?q=RULER+What%27s+Real+Context+Size+Long+Context+Language+Models+Hsieh+2024)

RULER was introduced in response to a specific problem: existing long-context benchmarks had become too easy. Frontier models were scoring near-ceiling on them while clearly failing on real long-document tasks. RULER introduced controlled synthetic tasks where difficulty can be dialed precisely by varying context length, the number of distractors, and the type of retrieval target. This allows clean measurement of whether a model is genuinely using its full context window or relying on shortcuts.

The five RULER tasks in the paper are all needle-in-a-haystack (NIAH) variants — a format that has become the standard diagnostic for long-context models. A target (the needle) is hidden inside irrelevant text (the haystack). The model must find and return it.

Three tasks used in the paper, illustrating the range:

*`niah_single_1` — Passkey retrieval*
- **Setup:** Pages of repeated filler sentences ("The grass is green. The sky is blue. The sun is yellow.") with one sentence hidden at a random position: "The secret passkey is 47832."
- **Task:** What is the passkey?
- **What makes it hard:** Pure length. The needle is one sentence in thousands of identical-looking filler lines. The model must not lose it.
- **What makes it tractable:** No ambiguity once found. No reasoning required. The answer is a verbatim copy of five digits.
- **DA result:** 100% accuracy on both models, 53% token reduction on Gemma. The clearest demonstration that DA's navigation declarations are reliable — the model correctly identifies the location of the passkey and focuses there.

*`niah_single_3` — UUID value retrieval*
- **Setup:** A UUID key-value pair (`key-7f3a2b: value-9c1d4e`) injected into Paul Graham essays about startups.
- **Task:** Given the key, return the value.
- **What makes it harder:** UUIDs are semantically meaningless — the model cannot guess or infer the value. It must locate the exact pair. Paul Graham essays are semantically coherent, making the injected pair harder to distinguish from the surrounding text than filler sentences.
- **DA result:** 100% accuracy on Gemma, 96.1% on Qwen. Slightly larger token savings than niah_single_1 because the essays are longer.

*`niah_multikey_3` — Key-value retrieval*
- **Setup:** A large lookup table of UUID key-value pairs fills the context.
- **Task:** Given a specific key, return its value.
- **What makes it hard:** All entries look structurally identical. With many pairs, the model must locate one specific entry without confusing it with adjacent entries. The pairs have no semantic content to distinguish them.
- **DA result:** 99.2% accuracy on Gemma (0.8pp drop), 94.5% on Qwen (5.5pp drop). The Qwen drop reflects the model occasionally focusing on an adjacent or similar key rather than the exact target — an instance of the protocol adherence failure at non-trivial retrieval difficulty.

---

**LongBench v1** — Bai et al. (2024) [LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding](https://scholar.google.com/scholar?q=LongBench+Bilingual+Multitask+Benchmark+Long+Context+Understanding+Bai+2024)

LongBench was one of the first comprehensive real-task long-context benchmarks, published in early 2024. It moved the field from synthetic retrieval tasks to realistic tasks across diverse domains, and introduced bilingual (English and Chinese) evaluation. Its most distinctive feature was the inclusion of tasks requiring different types of long-context processing: summarization, QA, few-shot learning, code completion, and synthetic tasks.

One LongBench v1 task appears in the paper:

*`LBv1/qmsum` — Meeting transcript QA (~14K tokens)*
- **Setup:** A full transcript of a real meeting — academic committee discussions, product reviews, parliamentary proceedings — approximately 14,000 tokens.
- **Task:** Answer a specific question about what was decided, said, or proposed. Example: "What did the project manager say about the timeline for the user interface redesign?"
- **What makes it hard:** Real meeting transcripts are digressive and repetitive. The relevant statement may be brief and embedded in extended tangential discussion. There is no injection — the answer is genuinely present somewhere in the transcript.
- **DA result:** 97.7% accuracy on both models (no drop), 45.7% token reduction on Gemma.

---

**LongBench v2** — Bai et al. (2025) [LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-Context Multitasks](https://scholar.google.com/scholar?q=LongBench+v2+Towards+Deeper+Understanding+Reasoning+Realistic+Long+Context+Multitasks+Bai+2025)

LongBench v2 was published in 2025 as a substantially harder successor to v1. The motivation was the same as RULER's: frontier models had approached ceiling performance on v1. v2 features much longer contexts (up to 1M+ tokens), harder reasoning requirements that demand combining information from multiple locations rather than finding a single fact, and more careful annotation quality control.

Four LongBench v2 tasks appear in the paper, two in each category:

*`LBv2/code_repo` — Code repository QA (~1M tokens)*
- **Setup:** An entire software repository — all source files, configuration, documentation — concatenated, averaging 1,071,100 tokens.
- **Task:** Answer questions about the codebase. Example: "What function handles authentication in the API module?" or "What is the default timeout for database connections?"
- **What makes it hard:** Everything. 1M tokens of code, most irrelevant to any question. The relevant function definition may be 50 lines in a million.
- **DA result:** No accuracy drop on Gemma (72.2% → 72.2%), +5.6pp improvement on Qwen (72.2% → 77.8%). Largest absolute token savings: 41.8M tokens per response on Gemma, 52.0M on Qwen. The improvement on Qwen is notable — at 1M tokens, vanilla attention may be failing due to the model getting lost in context, while DA's structured navigation keeps it focused.

*`LBv2/dialogue_history` — Dialogue history QA (~76K tokens)*
- **Setup:** Long conversations between LLM agents and users, averaging 76,000 tokens.
- **Task:** Answer questions about what was said, decided, or requested at specific points in the conversation. Example: "What file did the user ask to modify in the third request?" or "Did the user change their formatting preference?"
- **What makes it hard:** Conversations are repetitive and evolving. Decisions may be overridden later. The model must track state changes across the full history, not just find a single fact.
- **DA result:** 71.8% accuracy on Gemma (5.1pp drop from 76.9%), 69.2% on Qwen (no drop from 69.2%). Second largest absolute token savings: 22.1M tokens per response on Gemma.

---

**LooGLE** — Li et al. (2024) [LooGLE: Can Long-Context Language Models Understand Long Contexts?](https://scholar.google.com/scholar?q=LooGLE+Long+Context+Language+Models+Understand+Long+Contexts+Li+2024)

LooGLE was published in 2024 with a specific focus that distinguishes it from RULER and LongBench: it explicitly targets **long-dependency** understanding — tasks where the answer requires connecting information from passages that are far apart in the document, not merely finding a single fact. The title's implicit answer ("can they?") was, at the time, largely "not reliably."

Three LooGLE tasks appear in the paper:

*`LooGLE/longdep_qa` — Long-dependency QA (~31K tokens)*
- **Setup:** Wikipedia articles averaging 31,000 tokens.
- **Task:** Answer questions where the answer requires connecting facts from distant parts of the article. Example: "Given the founding date mentioned in the introduction and the acquisition described in the later history section, how many years passed between them?"
- **What makes it hard:** The two relevant facts may be 20,000 tokens apart with no explicit connection. The model must read both, hold them in memory (or context), and reason about their relationship.
- **DA result:** 68.8% accuracy on Gemma (+3.2pp improvement from 65.6%), 64.1% on Qwen (1.5pp drop). The Gemma improvement is one of the clearest gains in the study.

*`LooGLE/shortdep_cloze` — Cloze completion (~35K tokens)*
- **Setup:** Movie and television scripts averaging 35,000 tokens with one word or phrase blanked out.
- **Task:** Fill in the blank. Example: "CHARACTER_A: I told you not to open the [MASK]. CHARACTER_B: But I had no choice."
- **What makes it hard:** Requires understanding character relationships, plot context, and dialogue conventions across the full script. The right word must fit both grammatically and narratively within the story's logic.
- **DA result:** 86.7% accuracy on Gemma (4.7pp drop from 91.4%), 68.8% on Qwen (4.6pp drop). One of the larger drops in the study, reflecting the difficulty of locating which scene provides context for the blank.

---

**ZeroScrolls** — Shaham et al. (2023) [ZeroScrolls: A Zero-Shot Benchmark for Long Text Understanding](https://scholar.google.com/scholar?q=ZeroScrolls+Zero+Shot+Benchmark+Long+Text+Understanding+Shaham+2023)

ZeroScrolls was published in late 2023, among the earliest comprehensive long-context benchmarks. Its distinguishing feature is in the name: zero-shot evaluation, with no few-shot examples provided to the model. This tests raw generalization capability rather than the ability to learn from demonstrations. The benchmark covers summarization, QA, and aggregation tasks across literary texts, legal documents, and review collections.

Two ZeroScrolls tasks appear in the paper:

*`ZS/quality` — Multiple choice QA (~6K tokens)*
- **Setup:** Short stories and articles from Project Gutenberg and news sources, approximately 6,000 tokens, followed by a four-choice question.
- **Task:** Select the correct answer from A, B, C, D. Example: "Why did the protagonist leave the city? A) Financial trouble B) Family obligation C) Romantic rejection D) Political exile"
- **What makes it hard:** Literary reasoning. The answer may not be stated explicitly — it must be inferred from character motivation, plot logic, or thematic content. The distractors are plausible.
- **DA result:** 88.9% accuracy on both models (no drop on Gemma, no drop on Qwen). At 6K tokens — the shortest context in the study — DA's savings are smaller in absolute terms but the accuracy is perfectly preserved.

*`ZS/space_digest` — Sentiment aggregation (~7K tokens)*
- **Setup:** A collection of hotel reviews from multiple guests, totaling approximately 7,000 tokens.
- **Task:** Answer aggregate sentiment questions. Example: "What aspect of the hotel did reviewers most consistently praise?" or "Was room cleanliness generally rated positively or negatively?"
- **What makes it hard:** No single review contains the answer. The model must read all reviews, aggregate sentiment across them, and synthesize a conclusion. This is structurally the most demanding task for DA — every segment is relevant, and focusing on any one segment gives an incomplete picture.
- **DA result:** 40.6% accuracy on Gemma (2.4pp drop from 43.0%), 40.6% on Qwen (4.7pp drop from 45.3%). The largest proportional accuracy drop in the study, and the clearest illustration of DA's structural limits. This task is important for credibility: including it shows the paper is honest about where DA's decomposition does not fit the task.

---

### 5.4 Evaluation Method

Free-form generation makes exact string matching unreliable as an accuracy metric. A correct answer expressed differently from the reference would be scored as wrong. The paper uses LLM-as-judge, a now-standard approach.

Zheng et al. (2023) [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://scholar.google.com/scholar?q=Judging+LLM+as+a+Judge+MT+Bench+Chatbot+Arena+Zheng+2023) established that large language models can serve as reliable evaluators of other language models' outputs, with agreement rates approaching human inter-annotator agreement on many task types.

The paper implements a two-stage judge pipeline:

**Stage 1: Rubric generation.** For each question, Gemini-3-Flash generates a strict binary acceptance rubric conditioned on the ground-truth answer. The rubric specifies exactly what counts as correct, identifies common wrong answers and distractors, and is designed so that an evaluator without access to the original context can apply it consistently.

**Stage 2: Scoring.** Qwen-3.5-4B with thinking enabled applies the rubric to each model response. Responses that fail to produce a parseable `<answer>` tag are counted as incorrect. The judge outputs a binary verdict: correct or incorrect.

**Validation.** The paper re-judges a stratified sample of 2,993 responses with Gemini-3.1-Pro as a frontier reference judge. The local Qwen-3.5-4B judge agrees with Gemini-3.1-Pro on 98.53% of individual verdicts, with Cohen's $\kappa = 0.940$ and Pearson $r = 0.992$ on per-cell accuracy. Disagreements are symmetric (McNemar $p = 0.65$, 24 false positives vs 20 false negatives), supporting the use of the local judge for all reported results.

---

### 5.5 Metrics

**Accuracy** is the fraction of responses judged correct, with format failures counted as incorrect. It is averaged within each of the 15 sources, then averaged equally across sources — each source counts once regardless of how many examples it contributed. This macro-averaging prevents large sources from dominating the aggregate.

**Attended tokens** is the total number of KV cache positions attended during decoding, summed across all decode steps of a response:

$$A = \sum_{t=1}^{T} |\text{attended positions at step } t|$$

averaged per response within each source and then equally across sources. Percent reduction relative to vanilla is the primary efficiency metric. This directly measures the bandwidth saving: fewer attended tokens means fewer bytes transferred from HBM.

**Roofline wall-time** is an estimated decode time derived from the roofline performance model. Each operation is charged at its hardware ceiling: compute-bound operations at peak FLOPS × MFU (Model FLOPs Utilization, 40%), memory-bound operations at peak bandwidth × MBU (Model Bandwidth Utilization, 70%), on a single B200 accelerator in bf16. The three components — matmul, global memory (KV reads), and local memory (efficient layer reads) — are computed separately and summed over the full generation, averaged across tasks.

Roofline wall-time is a theoretical ceiling at the stated utilizations, not a measured time. It excludes prefill, which in phase-disaggregated serving runs on a separate pool. It provides a principled basis for comparing the efficiency of different arms on the same hardware target without committing to a specific batch size or serving configuration.

---

### 5.6 Main Results

**The ablation first: format versus mask.** The DA-no-mask condition isolates the contribution of each component. The chunked prompt format alone — magic chunks, three-mode instructions, tool-use formatting — is nearly lossless: DAnm matches vanilla accuracy exactly on Gemma (87.01% vs 87.01%) and drops only 0.69pp on Qwen. The format does not harm accuracy.

However, DAnm's attended-token count is 66.2% higher than vanilla on Gemma and 28.8% higher on Qwen. This is the cost of the DA protocol's extra tokens: global, focus, and local blocks together make the response approximately 15-35% longer than vanilla. At full causal attention, every extra step reads the full context, so more steps means more total attended tokens.

The mask converts this overhead into a net saving. Relative to DAnm, DA cuts attended tokens by 71.1% on Gemma and 46.5% on Qwen — moving DA from 66.2% above vanilla to 52.0% below on Gemma, and from 28.8% above to 31.1% below on Qwen. The mask is therefore the source of both DA's efficiency gain and essentially all of its accuracy cost: without the mask the format is free; with the mask the format pays for itself many times over in bandwidth savings at the cost of a small accuracy penalty.

**Accuracy.** DA produces average accuracy drops of 1.27pp on Gemma-4-31B (87.01% → 85.74%) and 2.75pp on Qwen-3.6-27B (85.31% → 82.56%) across the 15 tasks. The aggregate conceals substantial per-task variation:

- DA matches or improves on vanilla in 7 of 15 tasks on Gemma and 5 of 15 on Qwen
- Clearest single-task improvements: longdep_qa on Gemma (+3.2pp), code_repo on Qwen (+5.6pp)
- Losses are larger in multi-span reasoning than single-span retrieval (Gemma: 2.28pp vs 0.78pp category average; Qwen: 3.59pp vs 2.34pp)

The category split confirms the Kahneman-Klein prediction from Section 3: DA's declarations are most reliable in regular-environment tasks (single-span retrieval) and least reliable in irregular-environment tasks (multi-span reasoning).

**Attended tokens.** DA reduces average attended tokens by 52.0% on Gemma (13.43M → 6.45M per response) and 31.1% on Qwen (22.54M → 15.52M). The absolute savings are largest at the longest contexts: code_repo saves 41.8M tokens per response on Gemma and 52.0M on Qwen; dialogue_history saves 22.1M and 39.1M respectively. This is the right direction: savings are largest exactly where long-context decoding is most expensive.

**Wall-clock estimate.** The attended-token reductions translate to estimated decode wall-clock times of 0.71× on Gemma-4-31B and 0.77× on Qwen-3.6-27B, decomposed as follows:

```
Gemma-4-31B:
  Matmul:         22.9 ms  → 30.9 ms  (+35% steps)
  Global memory: 196.5 ms  → 94.4 ms  (−52% attended tokens)
  Local memory:   49.7 ms  → 67.1 ms  (+35% steps, SWA floor)
  Total:         269.1 ms  → 192.3 ms  (0.71×)

Qwen-3.6-27B:
  Matmul:         34.4 ms  → 45.1 ms  (+31% steps)
  Global memory: 263.8 ms  → 181.6 ms (−31% attended tokens)
  Local memory:    8.0 ms  → 10.5 ms  (+31% steps, GDN state)
  Total:         306.2 ms  → 237.3 ms  (0.77×)
```

The global memory term dominates under vanilla (73% of decode time on Gemma, 86% on Qwen) and is the only term DA reduces. The matmul and local memory terms increase slightly due to DA's extra decode steps. The net saving survives because the global reduction is larger than the overhead increase.

Qwen's larger global share (86% vs 73%) means a larger fraction of its decode time is attackable by DA in principle. But Qwen's attended-token reduction is smaller (31.1% vs 52.0%), because Qwen uses global mode more frequently under the zero-shot prompt. On Gemma, the SWA local floor (42% of DA's attention time) limits how much of the global saving survives in the total. These are properties of the zero-shot elicitation and the architecture respectively — not fundamental limits of the protocol.

---

### 5.7 Scaling Results

The model-size analysis is the most important result for the metacognitive reading of the paper.

Relative accuracy — DA accuracy as a fraction of vanilla accuracy — increases monotonically with model size in both families:

```
Gemma family:
  Gemma-4-E4B (~4B):  29% of vanilla accuracy retained
  Gemma-4-12B:        91% retained
  Gemma-4-31B:        99% retained

Qwen family:
  Qwen-3.5-4B:        64% retained
  Qwen-3.5-9B:        89% retained
  Qwen-3.6-27B:       97% retained
```

The smallest models fail primarily because they fail to follow the protocol. Gemma-4-E4B's focus success rate — the fraction of `<focus>` calls that resolve to a valid chunk reference — is only 58%, against 99% at the largest models. The model cannot reliably produce parseable tags or valid segment references. This is a protocol adherence failure, not a self-knowledge failure: the model does not have enough capability to follow structured syntax reliably, let alone to make accurate attention declarations.

At the largest scales, protocol adherence is essentially perfect (99% focus success rate on both families), and the residual accuracy gap reflects the quality of the declarations themselves rather than formatting failures.

Token savings show no strong size trend. DA attends roughly 46-50% of vanilla tokens in both families across most model sizes. The per-step masking saving — what fraction of each focus or local step's potential read is saved — is roughly scale-independent. The variation in totals comes from generation length, which different models set differently through their choice of global, focus, and local mix.

The one exception is Gemma-4-12B, which attends 183% of vanilla tokens — more than vanilla. This is a generation-length artifact: approximately 6% of Gemma-4-12B's DA responses fail to terminate within the 8,000-token generation budget, producing very long incomplete responses that inflate the attended-token sum. Excluding non-terminating responses brings Gemma-4-12B to 98% of vanilla, consistent with the family pattern.

---

### 5.8 Context-Length Scaling

Pooling all 15 sources and binning by context length reveals a clean pattern: DA's relative accuracy holds within approximately one percentage point of vanilla up to 32K tokens and declines modestly at longer contexts, reaching approximately 96% of vanilla in the longest bin (64-256K). The maskless DAnm line shows no such decline, confirming that the long-context accuracy cost comes from the mask rather than the chunked prompt format.

In absolute terms, DA's token savings grow sharply with context. At short contexts (below 8K), DA attends approximately 1M fewer tokens per response than vanilla. In the longest bin, this grows to approximately 21M fewer tokens. Since DA's per-step masking saves a roughly constant fraction of tokens (~50%), the absolute saving scales linearly with context length. The benefit is therefore largest exactly where long-context decoding is most expensive — a favorable alignment of savings and need.

---

*Section 5 established the experimental picture: DA maintains near-vanilla accuracy on a diverse 15-task suite while reducing attended tokens by 52% and 31% on two frontier models, with wall-clock savings of 0.71× and 0.77×. The scaling result — accuracy gap closing monotonically from 4B to 31B — is the key empirical support for the metacognitive reading. Section 6 synthesizes these results into the two readings of the paper and situates DA in the broader landscape of sparse attention and LLM self-knowledge research.*


## Section 6: Synthesis — Two Readings of One Result

---

### 6.1 Recapitulation

The preceding sections have established four things:

First, the engineering problem: at long context, decode is dominated by KV cache memory reads that are largely wasted — most attended tokens carry negligible attention weight, yet all must be loaded from HBM at every decode step, because the sparse subset is not known in advance.

Second, the technical substrate: chain-of-thought tokens are mechanically real, persist in the KV cache as external memory, and can be given operational semantics that the inference engine acts on — connecting the model's reasoning trace to the structure of the cache read.

Third, the scientific context: the question of whether language models have reliable self-knowledge about their own states is live and unresolved. Calibration research has shown that verbal introspective confidence improves with scale but remains domain-dependent and indirect. The conditions under which self-directed attention is reliable — identified by Kahneman and Klein for human experts — map cleanly onto the pattern of DA's results.

Fourth, the experimental results: DA reduces attended tokens by 52% and 31% on two frontier models, maintains 98.5% and 96.8% of vanilla accuracy zero-shot, and shows monotonically improving accuracy retention as model scale increases from 4B to 31B parameters.

These four things together support two simultaneous readings of the paper. This section develops each reading fully and then argues that the two are not parallel interpretations of the same facts but causally connected: the engineering result is the consequence of the scientific claim being true.

---

### 6.2 The Engineering Reading

In the engineering reading, DA is a new point in the design space of sparse attention methods. The relevant design space has two axes:

**Axis 1: Selection timing** — static versus dynamic. Static methods (StreamingLLM, H2O) select tokens once based on fixed heuristics and never revise. Dynamic methods (QUEST, TidalDecode, DeepSeek sparse attention) reselect at every decode step based on the current query.

**Axis 2: Selection mechanism** — extrinsic versus intrinsic. Extrinsic methods use a component external to the model's reasoning — a proxy scorer, a learned indexer, a key-vector surrogate — to decide what to attend to. Intrinsic methods would use the model's own reasoning to make this decision.

Prior to DA, the intrinsic quadrant was essentially empty. All dynamic methods are extrinsic. Static methods are extrinsic by definition. Jin et al. (2024) [Self-Selected Attention Span for Accelerating Large Language Model Inference](https://scholar.google.com/scholar?q=Self+Selected+Attention+Span+Accelerating+Large+Language+Model+Inference+Jin+2024) — the closest prior work — trained a model to select its own attention spans, but on hand-designed context partitions, per-task fine-tuning, and contexts up to 2K tokens on 7B models. DA is the first method to populate the dynamic + intrinsic quadrant at scale: zero-shot, task-agnostic, contexts up to 244K tokens, two model families.

The practical advantages of the intrinsic approach follow from the architecture:

**No per-step scan.** Extrinsic dynamic methods pay $O(N)$ per step to score surrogate representations of all $N$ context tokens. Resolving a `<focus>` tag is $O(1)$: the state machine reads the chunk number from a token it has already generated and rewrites the block table directly. The selection cost is zero beyond what the model would spend generating reasoning tokens anyway.

**Contiguous access pattern.** Ribar et al. (2024) [SparQ Attention: Bandwidth-Efficient LLM Inference](https://scholar.google.com/scholar?q=SparQ+Attention+Bandwidth+Efficient+LLM+Inference+Ribar+2024) report that scattered KV reads achieve only 1.3 to 3.0× of their theoretical speedup because non-contiguous memory access patterns defeat hardware prefetching. Yang et al. (2024) [Post-Training Sparse Attention with Double Sparsity](https://scholar.google.com/scholar?q=Post+Training+Sparse+Attention+Double+Sparsity+Yang+2024) find that a contiguous layout accounts for most of the available speedup independently. DA selects whole segments — contiguous blocks of 2,048 tokens — and the block-aligned masking preserves this contiguity at the block-table level. Existing kernels such as Dao et al. (2022) [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://scholar.google.com/scholar?q=FlashAttention+Fast+Memory+Efficient+Exact+Attention+IO+Awareness+Dao+2022) run without modification.

**Reversibility.** Unlike eviction-based methods that permanently delete KV cache entries, DA masks blocks without removing them. Switching back to global mode restores full attention in $O(1)$. A `<focus>` step can be followed by a `<global>` step that re-attends everything, which is why DA preserves accuracy where eviction must accept an unrecoverable error whenever the evicted token later becomes needed.

**Composability.** DA's global mode retains full $O(N)$ attention cost — the model surveys the complete context to navigate. This is where existing extrinsic sparse attention methods apply. A lightweight scan scorer could serve exactly the global steps, replacing full attention there while DA's declarations carry the savings in focus and local modes. The paper discusses this synergy in Section 8.3. Because DA applies its mask by rewriting the block table without modifying the attention kernel, integrating an extrinsic method in global mode requires no additional kernel changes.

**Synergy with speculative decoding.** Speculative decoding — drafting multiple tokens with a smaller model and verifying with the large model — reduces the number of sequential forward passes. DA reduces the cost of each forward pass by masking the KV read. The two savings are complementary and stack: verification passes read only the masked KV, and the attention pattern is fixed within a mode, so drafting proceeds under a single mask and speculation resets only at infrequent mode transitions.

**KV cache offloading potential.** DA changes its attended set only at span boundaries, and each change is announced in plain text before the tokens that read it. This is the access pattern that KV cache offloading needs: out-of-focus segments could spill to CPU memory for the duration of a span and be prefetched back as soon as a declaration names them, overlapping the transfer with decoding. Existing serving-level offloading systems (Sheng et al. 2023 [FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU](https://scholar.google.com/scholar?q=FlexGen+High+Throughput+Generative+Inference+Large+Language+Models+Single+GPU+Sheng+2023)) move KV between memory tiers only at request boundaries. Dynamic sparse attention methods reselect at every step, leaving nothing to prefetch ahead of time. DA's declared spans provide advance notice that neither existing approach offers.

In the engineering reading, the bottom line is a favorable cost-accuracy trade-off at a point in the design space that was previously unoccupied, achieved with no model modifications, using infrastructure (vLLM, PagedAttention, FlashAttention) that is already standard in production serving.

---

### 6.3 The Metacognitive Reading

In the metacognitive reading, DA is an empirical test of whether language models have prospective self-knowledge about their own attention needs — and the accuracy numbers are the result of that test.

The test has a clean structure. The model is given a long document divided into named segments, a question, and instructions to declare where it will attend before attending there. The inference engine then enforces those declarations by masking everything else. If the model's declaration is wrong — if it names segment 4 when the answer is in segment 7 — it will not see segment 7 and will generate a wrong answer. Each declaration is individually and immediately verified by the outcome.

The result: 98.5% accuracy retention on Gemma-4-31B and 96.8% on Qwen-3.6-27B, zero-shot, across 15 tasks spanning six orders of magnitude in content type and three orders of magnitude in context length.

What does this establish?

**The weak claim** — which the results definitively support — is that these models' attention declarations are operationally reliable. The model says "the answer is in segment 4" and is right often enough that masking everything else costs less than 2pp of accuracy. This is a clean empirical fact.

**The stronger claim** — which the results support but do not definitively establish — is that this reliability reflects genuine prospective self-knowledge: an internal representation of document structure, question semantics, and the relationship between them, which the model can access and express in language before attending to the relevant content.

The distinction between the weak and strong claims matters because an alternative explanation is available: the model may be performing sophisticated pattern matching on surface cues — document headers, question keywords, segment numbering — rather than representing anything like "where the answer is." This would produce the same behavior without requiring anything that deserves to be called self-knowledge.

The paper does not resolve this distinction, and is careful not to overclaim. What it does is provide evidence that bears on the stronger claim through three results that are harder to explain by surface pattern matching alone:

**Zero-shot generalization across 15 tasks.** A pure surface-pattern matcher would need to have seen the specific document type, question type, and segment numbering convention during training to match reliably. DA works zero-shot across scientific papers, legal documents, meeting transcripts, code repositories, hotel reviews, and literary fiction, with one fixed prompt. The breadth of generalization suggests the underlying capability is more than task-specific pattern matching.

**Monotonic scaling.** Accuracy retention increases monotonically with model size in both families, from 29% at 4B to 99% at 31B. If the behavior were surface pattern matching, it would be expected to plateau once the model is large enough to recognize the relevant patterns — scaling further would not systematically help. The monotonic improvement suggests that larger models have better-developed representations of the relevant structure, not just better pattern-matching of the protocol syntax.

**Task-structure correspondence.** DA works best on tasks where the answer genuinely lives in a locatable region (single-span retrieval) and worst on tasks where it is distributed across the full context (sentiment aggregation, multi-span reasoning). This is exactly the pattern that would be predicted if the model's declarations reflect something real about information location, and exactly what would not be predicted if the declarations were uniform surface-pattern responses to the protocol.

Together these three results are consistent with — though not proof of — the model having a genuine internal representation of where information is located in its context, accessible before attending to the specific location. This is the prospective self-knowledge claim.

---

### 6.4 Why the Two Readings Are Not Independent

The most important thing to understand about the paper is that the engineering reading and the metacognitive reading are not two alternative interpretations of the same results. They are causally connected: the engineering result is only possible because the metacognitive claim is true.

Consider the counterfactual. Suppose the model's declarations were no better than random guesses about which segment contains the answer. The state machine would mask away a random 90% of the context at each focus step. The masked content would include the answer most of the time. Accuracy would collapse to near zero. DA would be useless as an engineering technique.

The fact that accuracy does not collapse — that it remains within 1-3pp of vanilla — is simultaneously the engineering result (the masking saves bandwidth without destroying accuracy) and the scientific result (the model's self-knowledge is reliable enough to make the masking safe). The two results are the same observation described from two perspectives.

This causal structure distinguishes DA from all prior sparse attention work. In extrinsic methods — QUEST, SparQ, DeepSeek sparse attention — the proxy scorer is a component separate from the model's reasoning. Its accuracy is a property of the proxy, not a property of the model. Improving the proxy improves efficiency without saying anything about the model. In DA, there is no proxy. The model's reasoning trace is the selector. The accuracy of the selection is a property of the model's reasoning. Improving efficiency necessarily involves improving the model's self-knowledge.

This means DA's results are not just an engineering benchmark. They are measurements of a cognitive property — prospective self-knowledge about attention — expressed in units of percentage-point accuracy retention across a 15-task evaluation suite.

---

### 6.5 The System-2 Framing

The paper frames DA as **system-2 sparse attention** in Section 8.4, borrowing the terminology of dual-process theory in psychology. The framing is worth unpacking carefully.

Dual-process theories — associated with Kahneman's [Thinking, Fast and Slow](https://scholar.google.com/scholar?q=Thinking+Fast+and+Slow+Kahneman+2011) and earlier work by Stanovich and West — distinguish two modes of cognition:

**System 1**: fast, automatic, parallel, unconscious, associative. Pattern recognition, intuition, skilled performance. Operates below the level of deliberate reflection.

**System 2**: slow, deliberate, sequential, conscious, rule-governed. Explicit reasoning, planning, verification. Operates at the level of reflective thought.

The paper applies this distinction to sparse attention:

**System-1 sparse attention** (all prior work): the mask is inferred from internal activations — attention magnitudes, key-vector similarities, learned indexer scores. The selection happens automatically, below the level of the model's explicit reasoning, from signals that are not expressed in language and cannot be inspected without probing the model's internals.

**System-2 sparse attention** (DA): the mask is derived from explicit declarations in the model's reasoning trace. The selection is deliberate, sequential, expressed in language, and inspectable by anyone who reads the output.

The consequences of this distinction extend beyond efficiency:

**Steerability.** A system-1 mask is fixed by the model's weights and cannot be changed without retraining. A system-2 mask — expressed in language — can be changed by changing the prompt. Different instructions produce different attention strategies without any weight update.

**Scalability with capability.** System-1 masking quality is fixed once the proxy is trained. System-2 masking quality scales with the model's general language understanding and reasoning capability, because better models produce better declarations. This is why accuracy retention improves monotonically with scale.

**Optimizability.** System-2 reasoning has been dramatically improved through reinforcement learning — DeepSeek-AI (2025) [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://scholar.google.com/scholar?q=DeepSeek+R1+Incentivizing+Reasoning+Capability+LLMs+Reinforcement+Learning+2025) and OpenAI (2024) [OpenAI o1 System Card](https://scholar.google.com/scholar?q=OpenAI+o1+System+Card+2024) show that RL training on reasoning traces produces qualitative improvements in reasoning quality. The same pipeline applied to DA — rewarding both accuracy and attention efficiency — could optimize DA's attention strategies in ways that zero-shot prompting cannot approach.

**Legibility.** System-1 masking is opaque: the selected tokens are chosen by a process internal to the model that produces no human-readable rationale. System-2 masking is transparent: the selected tokens are chosen because the model wrote "Magic Chunk 4 contains the SFT section," and anyone can read and evaluate that claim. The attention plan is auditable because the tokens that make it auditable are the same tokens that drive the KV reads.

This last property connects DA to concerns beyond inference efficiency. As language models are deployed in high-stakes settings — legal analysis, medical literature review, financial document processing — the ability to inspect and verify why a model attended to specific content is valuable independently of any efficiency gain. DA provides this for free, as a byproduct of its architecture: the attention plan is written in the output where it has always been.

---

### 6.6 What Comes Next

The paper's zero-shot results are explicitly positioned as a lower bound. The analogy to Wei et al. (2022) is precise: chain-of-thought was first demonstrated zero-shot, producing significant accuracy improvements from prompting alone. Subsequent training-based methods — process reward models, RLHF, RL on reasoning traces — produced qualitatively better reasoning at much greater scale. DA is at the Wei et al. stage. The training-based stage is future work, and the paper identifies the specific directions:

**Post-training for DA.** Supervised fine-tuning on DA-formatted data, followed by reinforcement learning rewarding both accuracy and attention efficiency, would optimize the model's mode-selection strategy. Currently DA runs approximately 35% more decode steps than vanilla — the model uses global mode more than necessary, and its decomposition does not always fit the task structure. Trained models would learn when one global step suffices versus when multiple are needed, reducing the step overhead and the cases where DA's decomposition fails.

**Natural segments in agentic contexts.** The paper evaluates on static benchmarks where context must be artificially chunked. Agentic systems — where the model interacts with tools, retrieves documents, and accumulates context across turns — provide naturally addressable segments: tool responses, retrieved passages, conversation turns. DA's declarations would be more natural and more accurate in these settings, because the segment boundaries align with semantic content boundaries rather than arbitrary 2048-token splits.

**Thinking mode integration.** All results use non-thinking mode. Models trained to use tool calls within thinking traces — as several frontier models now do — should be able to integrate DA tags as standard tool declarations within reasoning traces. This would extend DA's savings to the regime where reasoning traces are longest and the potential savings are largest.

**Global mode optimization.** Global steps retain full $O(N)$ attention cost and account for over 80% of DA's attended tokens, with their share rising at longer contexts. The model could instead survey an in-context index — a short description of each segment's content, orders of magnitude smaller than the segments themselves — rather than the full context. This would reduce global mode costs and extend DA's savings to the navigation steps that currently retain full attention.

**Reversible KV offloading.** DA's declared spans provide advance notice of which segments will be needed. Out-of-focus segments could be offloaded to CPU memory during focus and local steps and prefetched back when a new global declaration names them. This would enable effective context windows beyond what GPU memory can hold while maintaining the reversibility that distinguishes DA from eviction-based approaches — no re-prefill required, because the KV cache of offloaded segments remains valid in CPU memory.

---

### 6.7 The Honest Boundary

Any honest synthesis must state where DA does not work, and why.

The two structural failure modes (identified in Appendix D.4 of the paper) are not edge cases — they represent classes of tasks that the global/focus/local decomposition does not fit:

**Evidence destroyed by segmentation.** Some tasks require information that does not survive chunking: a global count over all segments (counting word frequencies), or a table that the segmenter splits across two chunks. DA's accuracy collapses on these tasks not because the model's declarations are wrong but because the right answer cannot be extracted from any single segment. The fix is structure-aware segmentation that preserves tables and a map-reduce pattern that accumulates partial results across focus steps — not a fundamental limit of the protocol.

**Output length grows with the document.** Some tasks require emitting one unit of output per segment: per-segment summarization, full-document ordering, per-example in-context learning. Decode steps scale with the document, so attended tokens accumulate regardless of per-step savings. The fix is routing verbose output through focus mode rather than global mode — a training-time optimization that zero-shot prompting cannot achieve.

Both failure modes are addressable. Neither reflects a limit on whether models can know where to attend — they reflect limits on whether the current three-mode decomposition and zero-shot elicitation are sufficient for every task structure. The metacognitive claim survives these failures; the engineering claim is bounded by them.

---

*Section 6 has developed both readings of the paper and argued for their causal connection: the engineering result is the consequence of the metacognitive claim being true. DA occupies a new point in the sparse attention design space — dynamic and intrinsic — whose properties (zero scan cost, contiguous access, reversibility, legibility) follow from this architecture. The zero-shot results are a lower bound; the training-based ceiling is the trajectory the field is already on, applied to a new target. The reader is now equipped to follow the paper's argument in full and to situate it in the surrounding literature.*


## Section 7: References and Further Reading

---

### 7.1 How to Use This Section

The inline citations throughout the reader are the complete reference list. This section reorganizes them thematically and adds brief annotations for a reader who wants to go deeper on specific threads. Papers are grouped by the intellectual lineage they belong to, following the structure of the reader. Within each group, papers are ordered by importance for understanding the DA paper, not by date.

---

### Thread 1: The Engineering Problem — KV Cache and Long-Context Inference

The essential background for understanding why DA addresses a real and growing cost.

Kwon et al. (2023) [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://scholar.google.com/scholar?q=Efficient+Memory+Management+Large+Language+Model+Serving+PagedAttention+Kwon+2023)
The foundational paper for vLLM and PagedAttention — the memory management system DA builds on. Explains why KV cache fragmentation is expensive and how block-based management solves it. Essential reading for understanding what a block table is and why DA can rewrite it without kernel modifications.

Dao et al. (2022) [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://scholar.google.com/scholar?q=FlashAttention+Fast+Memory+Efficient+Exact+Attention+IO+Awareness+Dao+2022)
The paper that made IO-aware attention the standard. Introduces the roofline framing for attention — memory-bound at decode, compute-bound at prefill — that the DA paper uses throughout its efficiency analysis. The roofline wall-time estimates in Section 5 of the DA paper are built directly on this framing.

Williams et al. (2009) [Roofline: An Insightful Visual Performance Model for Multicore Architectures](https://scholar.google.com/scholar?q=Roofline+Insightful+Visual+Performance+Model+Multicore+Architectures+Williams+2009)
The original roofline model paper. Not ML-specific — this is a general computer architecture tool. Worth reading if the distinction between compute-bound and memory-bound operations in Section 1 of the reader felt unclear. The model is simple and the paper is accessible.

---

### Thread 2: The Sparse Attention Literature — Prior Art DA Situates Itself Against

Reading these in order gives the clearest picture of why DA's intrinsic approach is genuinely different.

Zhang et al. (2023) [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://scholar.google.com/scholar?q=H2O+Heavy+Hitter+Oracle+Efficient+Generative+Inference+Large+Language+Models+Zhang+2023)
The representative static sparse attention paper. Keeps tokens with high accumulated attention weight, evicts the rest permanently. The clearest illustration of why static methods fail: they cannot anticipate which tokens future queries will need. Compare directly to DA's reversibility.

Tang et al. (2024) [QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://scholar.google.com/scholar?q=QUEST+Query+Aware+Sparsity+Efficient+Long+Context+LLM+Inference+Tang+2024)
The representative dynamic sparse attention paper. Scores KV pages by per-page key bounds at every decode step. The clearest illustration of why dynamic extrinsic methods still pay O(N): the scoring is query-dependent but still requires scanning the full context. The paper DA most directly competes with on the efficiency axis.

Xiao et al. (2024) [Efficient Streaming Language Models with Attention Sinks](https://scholar.google.com/scholar?q=Efficient+Streaming+Language+Models+Attention+Sinks+Xiao+2024)
Introduces the attention sink observation — the first few tokens receive disproportionate attention regardless of content — and StreamingLLM, which keeps sinks plus a recent window. DA adopts the attention sink insight directly in its prompt design (the fixed system instruction occupying the sink region).

Jin et al. (2024) [Self-Selected Attention Span for Accelerating Large Language Model Inference](https://scholar.google.com/scholar?q=Self+Selected+Attention+Span+Accelerating+Large+Language+Model+Inference+Jin+2024)
The most important prior work for understanding DA's novelty. Demonstrates that a model can be trained to declare its own attention spans — the same core idea as DA — but with per-task fine-tuning, hand-designed context partitions, and 2K-token contexts. Reading this alongside DA clarifies exactly what DA adds: zero-shot elicitation, task-agnostic protocol, 244K-token contexts.

Yuan et al. (2025) [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://scholar.google.com/scholar?q=Native+Sparse+Attention+Hardware+Aligned+Natively+Trainable+Sparse+Attention+Yuan+2025)
The industry-scale learned sparse attention paper, from DeepSeek. Trains block-sparse selection directly into the model. Represents the current state of the art in system-1 sparse attention — the most capable extrinsic approach. Reading this alongside DA clarifies the tradeoff: Native Sparse Attention achieves better per-step efficiency at the cost of architectural changes and retraining; DA achieves good efficiency with no architectural changes and no training.

---

### Thread 3: Chain-of-Thought — The Technical Substrate

These papers establish the CoT lineage that DA extends.

Wei et al. (2022) [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://scholar.google.com/scholar?q=Chain+of+Thought+Prompting+Elicits+Reasoning+Large+Language+Models+Wei+2022)
The foundational CoT paper. Essential reading. The zero-shot elicitation finding — a simple prompt instruction surfaces a latent capability — is the direct precedent for DA's approach. The DA paper explicitly frames its contribution as extending CoT from dictating what to think to where to attend.

Wang et al. (2023) [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://scholar.google.com/scholar?q=Self+Consistency+Improves+Chain+of+Thought+Reasoning+Language+Models+Wang+2023)
The self-consistency paper. Introduces majority voting over sampled reasoning paths. Important for understanding the consistency-as-truth-signal principle that appears throughout Section 3 of the reader, and for understanding why DA's 97-99% accuracy retention across 15 diverse tasks is evidence of genuine self-knowledge rather than task-specific pattern matching.

Lightman et al. (2023) [Let's Verify Step by Step](https://scholar.google.com/scholar?q=Let%27s+Verify+Step+by+Step+Lightman+OpenAI+2023)
Process reward models — verifiers that score individual reasoning steps rather than final answers. Important for understanding how training-based improvements to CoT work, and therefore what training-based DA could look like. The step-level verification idea is directly applicable to DA: reward models could score individual global, focus, and local steps rather than only final answers.

DeepSeek-AI (2025) [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://scholar.google.com/scholar?q=DeepSeek+R1+Incentivizing+Reasoning+Capability+LLMs+Reinforcement+Learning+2025)
The most important trained-reasoning paper for situating DA's future trajectory. Shows that RL training on reasoning traces produces qualitative improvements far beyond what zero-shot CoT achieves. DA is at the zero-shot stage; DeepSeek-R1 is the trained-reasoning stage. The gap between them is the opportunity the paper identifies in Section 8.

---

### Thread 4: LLM Self-Knowledge — The Scientific Context

These papers establish the research context for the metacognitive reading of DA.

Kadavath et al. (2022) [Language Models (Mostly) Know What They Know](https://scholar.google.com/scholar?q=Language+Models+Mostly+Know+What+They+Know+Kadavath+2022)
The foundational paper on LLM introspective calibration. Shows that large models can predict whether their own answers are correct with reasonable accuracy, improving with scale. The direct scientific predecessor to DA's metacognitive claim — DA extends this from "does the model know what it knows?" to "does the model know where to look?"

Guo et al. (2017) [On Calibration of Modern Neural Networks](https://scholar.google.com/scholar?q=On+Calibration+of+Modern+Neural+Networks+Guo+2017)
The foundational paper on neural network miscalibration. Shows that deep networks become more overconfident as they become more accurate. Essential background for understanding the calibration problem that DA sidesteps — rather than improving the calibration of a confidence score, DA replaces the confidence score with an operationally verifiable declaration.

Nisbett and Wilson (1977) [Telling More Than We Can Know: Verbal Reports on Mental Processes](https://scholar.google.com/scholar?q=Telling+More+Than+We+Can+Know+Verbal+Reports+Mental+Processes+Nisbett+Wilson+1977)
The foundational paper on human introspective unreliability. Shows that people confabulate explanations for their choices that bear no causal relationship to the actual determinants. Important as a cautionary note for the metacognitive reading of DA: the fact that a model produces a confident-sounding declaration does not guarantee that the declaration reflects an internal process of the kind it appears to describe.

Korbak et al. (2025) [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://scholar.google.com/scholar?q=Chain+of+Thought+Monitorability+New+Fragile+Opportunity+AI+Safety+Korbak+2025)
Directly cited in the DA paper in the context of legibility. Argues that chain-of-thought reasoning traces provide a monitorable window into model reasoning that is valuable for AI safety — but fragile, because models are not explicitly trained to make their reasoning legible. DA's attention declarations are a specific instance of this monitorability, with the additional property that the declarations are mechanically enforced: the model cannot attend to content it did not declare.

---

### Thread 5: Expert Intuition and Calibration — The Psychological Context

For readers coming from psychology or cognitive science, these are the key papers underlying Section 3.6 of the reader.

Kahneman and Klein (2009) [Conditions for Intuitive Expertise: A Failure to Disagree](https://scholar.google.com/scholar?q=Conditions+Intuitive+Expertise+Failure+Disagree+Kahneman+Klein+2009)
The synthesis paper reconciling two research traditions on expert judgment. The two conditions — environmental regularity and feedback quality — map directly onto the pattern of DA's results across task types. The most important single paper for the psychological framing of the talk.

Tetlock (2005) [Expert Political Judgment: How Good Is It? How Can We Know?](https://scholar.google.com/scholar?q=Expert+Political+Judgment+How+Good+Is+It+How+Can+We+Know+Tetlock+2005)
The most systematic study of expert prediction accuracy. Shows that domain experts barely outperform chance on long-horizon predictions while expressing strong confidence. Illustrates the failure mode — wrong confidently — that DA's legibility property addresses. The contrast between Tetlock's political forecasters (irregular environment, no feedback) and DA on passkey retrieval (regular environment, immediate feedback) is the clearest illustration of the Kahneman-Klein conditions.

Fischhoff et al. (1977) [Knowing with Certainty: The Appropriateness of Extreme Confidence](https://scholar.google.com/scholar?q=Knowing+with+Certainty+Appropriateness+Extreme+Confidence+Fischhoff+Slovic+Lichtenstein+1977)
The foundational paper on confidence interval miscalibration. Shows that stated 90% confidence intervals contain the true value only 40-60% of the time across domains and populations. The earliest systematic documentation of the wrong-confidently failure mode in human judgment.

---

### Thread 6: The Benchmarks

For readers who want to understand the evaluation context in more depth.

Hsieh et al. (2024) [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://scholar.google.com/scholar?q=RULER+What%27s+Real+Context+Size+Long+Context+Language+Models+Hsieh+2024)
The needle-in-a-haystack benchmark suite. Important for understanding what controlled synthetic evaluation adds: the ability to isolate specific retrieval capabilities by varying context length and distractor count independently. The RULER tasks are where DA shows its cleanest results — 100% accuracy at 0pp drop on the simplest tasks.

Bai et al. (2025) [LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-Context Multitasks](https://scholar.google.com/scholar?q=LongBench+v2+Towards+Deeper+Understanding+Reasoning+Realistic+Long+Context+Multitasks+Bai+2025)
The hardest benchmark in the suite and the most practically relevant. The code_repo task at ~1M tokens is where DA's absolute savings are largest and where the practical case for long-context efficiency is strongest. Worth reading the benchmark paper to understand how the tasks were constructed and why they are harder than v1.

Li et al. (2024) [LooGLE: Can Long-Context Language Models Understand Long Contexts?](https://scholar.google.com/scholar?q=LooGLE+Long+Context+Language+Models+Understand+Long+Contexts+Li+2024)
The long-dependency benchmark. Important for understanding the distinction between retrieval (find a fact) and reasoning (connect facts from distant locations). LooGLE's longdep_qa task is where DA shows an unexpected improvement on Gemma (+3.2pp), which is worth examining: structured navigation may help when the task requires deliberately connecting distant passages.

---

### 7.2 Five Papers for a Reader New to This Area

If you read nothing else from the lists above, read these five in this order:

**1.** Wei et al. (2022) [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://scholar.google.com/scholar?q=Chain+of+Thought+Prompting+Elicits+Reasoning+Large+Language+Models+Wei+2022)
— establishes the paradigm DA extends

**2.** Kwon et al. (2023) [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://scholar.google.com/scholar?q=Efficient+Memory+Management+Large+Language+Model+Serving+PagedAttention+Kwon+2023)
— establishes the infrastructure DA uses

**3.** Kadavath et al. (2022) [Language Models (Mostly) Know What They Know](https://scholar.google.com/scholar?q=Language+Models+Mostly+Know+What+They+Know+Kadavath+2022)
— establishes the scientific question DA answers

**4.** Kahneman and Klein (2009) [Conditions for Intuitive Expertise: A Failure to Disagree](https://scholar.google.com/scholar?q=Conditions+Intuitive+Expertise+Failure+Disagree+Kahneman+Klein+2009)
— provides the framework that predicts DA's pattern of results

**5.** Jin et al. (2024) [Self-Selected Attention Span for Accelerating Large Language Model Inference](https://scholar.google.com/scholar?q=Self+Selected+Attention+Span+Accelerating+Large+Language+Model+Inference+Jin+2024)
— the closest prior work, clarifying exactly what DA adds

---

### 7.3 The DA Paper Itself

Ho et al. (2026) [Language Models Can Control Their Own Attention](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026)
Available on arXiv: arXiv:2609.02737v1. The appendices are worth reading in full: Appendix A surveys the complete sparse attention literature; Appendix C derives the roofline wall-time estimates in detail; Appendix D.4 documents the failure cases honestly; Appendix F reproduces the complete prompt templates including the DA instruction prompt and the vanilla baseline prompt.


