# Why instruction following works (a background reader)

A map of what is actually known about **in-context learning** and **instruction fine-tuning**, at three levels of explanation. Paper titles link to Google Scholar queries. Local curated notes, when they exist in this tree, are linked by citation key.

This is not a claim that the circuit-level story is solved. The bulk of the literature is training recipes and behavioral analysis; mechanistic accounts of post-SFT chat are still thin.

## The three questions

| Question | Status |
|----------|--------|
| Does instruction fine-tuning work, and how do you do it? | Well studied (InstructGPT, FLAN, LIMA, …). |
| Does it teach new skills, or elicit capabilities already in pretraining? | Actively studied; elicitation + format is a leading story. |
| Which internal mechanism implements “follow this instruction”? | Incomplete — pieces for ICL, refusal, persona; no full account for SFT/RLHF. |

Three different behaviors get lumped together as “instruction following”:

1. **In-context learning (ICL)** — few-shot examples in the prompt; no weight update. GPT-3 made this famous.
2. **Instruction fine-tuning (IFT / SFT)** — supervised updates on `(instruction, response)` pairs.
3. **Preference / RL stage** — RLHF, RLAIF, DPO: further shift toward preferred replies.

A base model can already do a surprising amount of (1). Chat models add (2) and usually (3). Mechanistic work is strongest on (1) and on a few alignment-adjacent behaviors (refusal, persona), not on “the instruction module” after SFT.

---

## 0. Historical path (2017–2021): one objective, then prompts

The decoder-only stack of [Attention is all you need](https://scholar.google.com/scholar?q=Attention+is+all+you+need) (Vaswani et al., 2017) [`vaswani2017_attention`](../interpretability/vaswani2017_attention.md) was reused as a language model in [Improving language understanding by generative pre-training](https://scholar.google.com/scholar?q=Improving+language+understanding+by+generative+pre-training) (Radford et al., 2018, GPT-1) and [Language models are unsupervised multitask learners](https://scholar.google.com/scholar?q=Language+models+are+unsupervised+multitask+learners) (Radford et al., 2019, GPT-2). The training objective is next-token prediction on a single stream — not “encode source, decode target.”

[Language models are few-shot learners](https://scholar.google.com/scholar?q=Language+models+are+few-shot+learners) (Brown et al., 2020, GPT-3) showed that at enough scale, the *prompt* can stand in for a task specification: give examples, then a query, and the model continues in the demonstrated format. That is ICL. It is not instruction fine-tuning.

Before full IFT, people already treated the prompt as a program:

- [Exploiting cloze questions for few-shot text classification and natural language inference](https://scholar.google.com/scholar?q=Exploiting+cloze+questions+for+few-shot+text+classification+and+natural+language+inference) (Schick & Schütze, 2021, PET)
- [Making pre-trained language models better few-shot learners](https://scholar.google.com/scholar?q=Making+pre-trained+language+models+better+few-shot+learners) (Gao et al., 2021, LM-BFF)
- [Prefix-tuning: optimizing continuous prompts for generation](https://scholar.google.com/scholar?q=Prefix-tuning+optimizing+continuous+prompts+for+generation) (Li & Liang, 2021)
- [The power of scale for parameter-efficient prompt tuning](https://scholar.google.com/scholar?q=The+power+of+scale+for+parameter-efficient+prompt+tuning) (Lester et al., 2021)
- [Prompt programming for large language models: beyond the few-shot paradigm](https://scholar.google.com/scholar?q=Prompt+programming+for+large+language+models+beyond+the+few-shot+paradigm) (Reynolds & McDonell, 2021)

[Scaling laws for neural language models](https://scholar.google.com/scholar?q=Scaling+laws+for+neural+language+models) (Kaplan et al., 2020) and later [Training compute-optimal large language models](https://scholar.google.com/scholar?q=Training+compute-optimal+large+language+models) (Hoffmann et al., 2022) framed *why* “just scale next-token prediction” was a serious research program. [On the opportunities and risks of foundation models](https://scholar.google.com/scholar?q=On+the+opportunities+and+risks+of+foundation+models) (Bommasani et al., 2021) named the resulting objects.

Fine-tuning itself was already known to be cheap in parameter space: [Intrinsic dimensionality explains the effectiveness of language model fine-tuning](https://scholar.google.com/scholar?q=Intrinsic+dimensionality+explains+the+effectiveness+of+language+model+fine-tuning) (Aghajanyan et al., 2021) [`aghajanyan2021_intrinsic_dimensionality`](../interpretability/aghajanyan2021_intrinsic_dimensionality.md), and [LoRA: low-rank adaptation of large language models](https://scholar.google.com/scholar?q=LoRA+low-rank+adaptation+of+large+language+models) (Hu et al., 2021) [`hu2021loralowrankadaptation`](../interpretability/hu2021loralowrankadaptation.md).

---

## 1. Empirical / training recipe (most of the literature)

**Question:** what data, objective, and scale make instruction following *good*?

This level explains *that* IFT works and *what* to train on. It does not say which circuits implement obedience.

### Multi-task instruction tuning (zero-shot transfer)

- [Finetuned language models are zero-shot learners](https://scholar.google.com/scholar?q=Finetuned+language+models+are+zero-shot+learners) (Wei et al., 2022, FLAN)
- [Multitask prompted training enables zero-shot task generalization](https://scholar.google.com/scholar?q=Multitask+prompted+training+enables+zero-shot+task+generalization) (Sanh et al., 2022, T0)
- [Super-NaturalInstructions: generalization via declarative instructions on 1600+ NLP tasks](https://scholar.google.com/scholar?q=Super-NaturalInstructions+generalization+via+declarative+instructions) (Wang et al., 2022)
- [Cross-task generalization via natural language crowdsourcing instructions](https://scholar.google.com/scholar?q=Cross-task+generalization+via+natural+language+crowdsourcing+instructions) (Mishra et al., 2022)
- [Scaling instruction-finetuned language models](https://scholar.google.com/scholar?q=Scaling+instruction-finetuned+language+models) (Chung et al., 2024, FLAN-T5)
- [The Flan collection: designing data and methods for effective instruction tuning](https://scholar.google.com/scholar?q=The+Flan+collection+designing+data+and+methods+for+effective+instruction+tuning) (Longpre et al., 2023)

The FLAN/T0 result: train on many tasks phrased as instructions, and zero-shot performance on *held-out* tasks rises. That is the first systematic “instruction following by fine-tuning” result, still without a human preference loop.

Related reasoning prompts (not IFT, but they changed how people write instructions): [Chain-of-thought prompting elicits reasoning in large language models](https://scholar.google.com/scholar?q=Chain-of-thought+prompting+elicits+reasoning+in+large+language+models) (Wei et al., 2022) and [Large language models are zero-shot reasoners](https://scholar.google.com/scholar?q=Large+language+models+are+zero-shot+reasoners) (Kojima et al., 2022).

### Human feedback (InstructGPT → chat)

RL from human preferences predates chat: [Deep reinforcement learning from human preferences](https://scholar.google.com/scholar?q=Deep+reinforcement+learning+from+human+preferences) (Christiano et al., 2017) and [Learning to summarize with human feedback](https://scholar.google.com/scholar?q=Learning+to+summarize+with+human+feedback) (Stiennon et al., 2020).

The chat stack is:

- [Training language models to follow instructions with human feedback](https://scholar.google.com/scholar?q=Training+language+models+to+follow+instructions+with+human+feedback) (Ouyang et al., 2022, InstructGPT) — SFT on demonstrations, then RLHF
- [Training a helpful and harmless assistant with reinforcement learning from human feedback](https://scholar.google.com/scholar?q=Training+a+helpful+and+harmless+assistant+with+reinforcement+learning+from+human+feedback) (Bai et al., 2022)
- [Constitutional AI: harmlessness from AI feedback](https://scholar.google.com/scholar?q=Constitutional+AI+harmlessness+from+AI+feedback) (Bai et al., 2022)
- [RLAIF: scaling reinforcement learning from human feedback with AI feedback](https://scholar.google.com/scholar?q=RLAIF+scaling+reinforcement+learning+from+human+feedback+with+AI+feedback) (Lee et al., 2024)
- [Direct preference optimization: your language model is secretly a reward model](https://scholar.google.com/scholar?q=Direct+preference+optimization+your+language+model+is+secretly+a+reward+model) (Rafailov et al., 2023)

Limitations of the RLHF *process* (not circuits): [Open problems and fundamental limitations of reinforcement learning from human feedback](https://scholar.google.com/scholar?q=Open+problems+and+fundamental+limitations+of+reinforcement+learning+from+human+feedback) (Casper et al., 2023). LLM-as-judge evals: [Judging LLM-as-a-judge with MT-bench and chatbot arena](https://scholar.google.com/scholar?q=Judging+LLM-as-a-judge+with+MT-bench+and+chatbot+arena) (Zheng et al., 2023) and [`li2024llmsasjudgescomprehensivesurveyllmbased`](../interpretability/li2024llmsasjudgescomprehensivesurveyllmbased.md).

### Cheap IFT, distillation, data scaling

- [Stanford Alpaca: an instruction-following LLaMA model](https://scholar.google.com/scholar?q=Stanford+Alpaca+instruction-following+LLaMA) (Taori et al., 2023)
- [Vicuna: an open-source chatbot impressing GPT-4 with 90% ChatGPT quality](https://scholar.google.com/scholar?q=Vicuna+an+open-source+chatbot+impressing+GPT-4) (Chiang et al., 2023)
- [Self-Instruct: aligning language models with self-generated instructions](https://scholar.google.com/scholar?q=Self-Instruct+aligning+language+models+with+self-generated+instructions) (Wang et al., 2023)
- [Unnatural Instructions: tuning language models with (almost) no human labor](https://scholar.google.com/scholar?q=Unnatural+Instructions+tuning+language+models+with+almost+no+human+labor) (Honovich et al., 2023)
- [Orca: progressive learning from complex explanation traces of GPT-4](https://scholar.google.com/scholar?q=Orca+progressive+learning+from+complex+explanation+traces+of+GPT-4) (Mukherjee et al., 2023)
- [Enhancing chat language models by scaling high-quality instructional conversations](https://scholar.google.com/scholar?q=Enhancing+chat+language+models+by+scaling+high-quality+instructional+conversations) (Ding et al., 2023) [`ding2023enhancingchatlanguagemodels`](../interpretability/ding2023enhancingchatlanguagemodels.md)
- Survey: [Instruction tuning for large language models: a survey](https://scholar.google.com/scholar?q=Instruction+tuning+for+large+language+models+a+survey) (Zhang et al., 2023)

A caution on distillation: [The false promise of imitating proprietary LLMs](https://scholar.google.com/scholar?q=The+false+promise+of+imitating+proprietary+LLMs) (Gudibande et al., 2023) — imitating ChatGPT style is easier than imitating its capabilities.

**What this level explains:** SFT + (optional) preference optimization, on the right mixture of tasks or conversations, produces models that look like they follow instructions. It does not identify an “instruction circuit.”

---

## 2. Representational / behavioral analysis (some “why”)

**Question:** does SFT add new skills, or reshape how existing knowledge is accessed?

### Superficial alignment / elicitation

[LIMA: less is more for alignment](https://scholar.google.com/scholar?q=LIMA+less+is+more+for+alignment) (Zhou et al., 2023) is the landmark here. A few thousand high-quality demonstration examples, and no RLHF, already produce strong chat behavior on many prompts. Their **superficial alignment** hypothesis: pretraining already contains most capabilities; SFT mainly teaches the *format, tone, and distribution* of a helpful assistant.

That is an explanation of *kind*, not of mechanism: IFT is closer to **elicitation + surface form** than to teaching facts from scratch. Related “unlocking / latent capability” lines include the FLAN zero-shot transfer results above, and later work on whether fine-tuning injects knowledge or just changes when it is produced — e.g. [Does fine-tuning LLMs on new knowledge encourage hallucinations?](https://scholar.google.com/scholar?q=Does+fine-tuning+LLMs+on+new+knowledge+encourage+hallucinations) (Gekhman et al., 2024).

[The reversal curse: LLMs trained on “A is B” fail to learn “B is A”](https://scholar.google.com/scholar?q=The+reversal+curse+LLMs+trained+on+A+is+B+fail+to+learn+B+is+A) (Berglund et al., 2024) is a reminder that even “learning from text” is not a general reasoner being filled in; direction of association matters.

### Scale, emergence, and ICL that is not magic

[Emergent abilities of large language models](https://scholar.google.com/scholar?q=Emergent+abilities+of+large+language+models) (Wei et al., 2022) documented sharp jumps with scale, including ICL-like tasks. [Are emergent abilities of large language models a mirage?](https://scholar.google.com/scholar?q=Are+emergent+abilities+of+large+language+models+a+mirage) (Schaeffer et al., 2023) argued that some jumps are metric/threshold artifacts. Both papers matter for “why does size help ICL?”: scale helps, but “emergence” is not a mechanism.

On ICL as *pattern matching* rather than task learning: [Rethinking the role of demonstrations: what makes in-context learning work?](https://scholar.google.com/scholar?q=Rethinking+the+role+of+demonstrations+what+makes+in-context+learning+work) (Min et al., 2022) — even gold labels in the prompt can be less important than format. Later: [Larger language models do in-context learning differently](https://scholar.google.com/scholar?q=Larger+language+models+do+in-context+learning+differently) (Wei, Wei, et al., 2023).

### Decision boundaries: refusal, sycophancy, persona

SFT/RLHF shift *when* the model complies or refuses, not only *what* it knows:

- [Discovering language model behaviors with model-written evaluations](https://scholar.google.com/scholar?q=Discovering+language+model+behaviors+with+model-written+evaluations) (Perez et al., 2022)
- [Towards understanding sycophancy in language models](https://scholar.google.com/scholar?q=Towards+understanding+sycophancy+in+language+models) (Sharma et al., 2024)
- Steering / representation work that treats those shifts as directions: [Representation engineering: a top-down approach to AI transparency](https://scholar.google.com/scholar?q=Representation+engineering+a+top-down+approach+to+AI+transparency) (Zou et al., 2023) [`zou2023representationengineeringtopdownapproach`](../interpretability/zou2023representationengineeringtopdownapproach.md); [Steering Llama 2 via contrastive activation addition](https://scholar.google.com/scholar?q=Steering+Llama+2+via+contrastive+activation+addition) (Panickssery et al., 2024) [`panickssery2024steeringllama2contrastive`](../interpretability/panickssery2024steeringllama2contrastive.md)

### Distortion and forgetting

Fine-tuning can *hurt* pretrained behavior if overdone: [An empirical study of catastrophic forgetting in large language models during continual fine-tuning](https://scholar.google.com/scholar?q=An+empirical+study+of+catastrophic+forgetting+in+large+language+models+during+continual+fine-tuning) (Luo et al., 2023); [LoRA learns less and forgets less](https://scholar.google.com/scholar?q=LoRA+learns+less+and+forgets+less) (Biderman et al., 2024).

**What this level explains:** a leading picture is that IFT mostly **reweights access** to pretrained abilities (format, helpfulness register, refusal policy) rather than installing a new general problem-solver. Evidence is behavioral, correlational, and from activation interventions — not a complete internal map.

---

## 3. Mechanistic circuits (thinnest for post-SFT chat)

**Question:** which heads/layers implement “follow this instruction”?

### ICL: the part with actual circuits

The strongest mechanistic story is about **in-context copying / pattern completion**, not chat SFT.

- [A mathematical framework for transformer circuits](https://scholar.google.com/scholar?q=A+mathematical+framework+for+transformer+circuits) (Elhage et al., 2021) [`elhage2021_transformer_circuits`](../interpretability-anthropic/elhage2021_transformer_circuits.md)
- [In-context learning and induction heads](https://scholar.google.com/scholar?q=In-context+learning+and+induction+heads) (Olsson et al., 2022) [`olsson2022_induction_heads`](../interpretability-anthropic/olsson2022_induction_heads.md) — previous-token heads + induction heads; a training-time phase change correlated with ICL
- [Interpretability in the wild: a circuit for indirect object identification in GPT-2 small](https://scholar.google.com/scholar?q=Interpretability+in+the+wild+a+circuit+for+indirect+object+identification+in+GPT-2+small) (Wang et al., 2022) [`wang2022_ioi`](../interpretability/wang2022_ioi.md) — a full-ish circuit in a small model, showing the method
- [Toy models of superposition](https://scholar.google.com/scholar?q=Toy+models+of+superposition) (Elhage et al., 2022) [`elhage2022_superposition`](../interpretability-anthropic/elhage2022_superposition.md)

Theory and toy experiments treat ICL as an *inner algorithm* implemented by the forward pass (this is a hypothesis, not a proof about GPT-4):

- [An explanation of in-context learning as implicit Bayesian inference](https://scholar.google.com/scholar?q=An+explanation+of+in-context+learning+as+implicit+Bayesian+inference) (Xie et al., 2022)
- [What can transformers learn in-context? A case study of simple function classes](https://scholar.google.com/scholar?q=What+can+transformers+learn+in-context+a+case+study+of+simple+function+classes) (Garg et al., 2022)
- [What learning algorithm is in-context learning? Investigations with linear models](https://scholar.google.com/scholar?q=What+learning+algorithm+is+in-context+learning+investigations+with+linear+models) (Akyürek et al., 2023)
- [Transformers learn in-context by gradient descent](https://scholar.google.com/scholar?q=Transformers+learn+in-context+by+gradient+descent) (von Oswald et al., 2023)
- [Why can GPT learn in-context? Language models implicitly perform gradient descent as meta-optimizers](https://scholar.google.com/scholar?q=Why+can+GPT+learn+in-context+language+models+implicitly+perform+gradient+descent+as+meta-optimizers) (Dai et al., 2023)

[Model-agnostic meta-learning for fast adaptation of deep networks](https://scholar.google.com/scholar?q=Model-agnostic+meta-learning+for+fast+adaptation+of+deep+networks) (Finn et al., 2017) is the *explicit* meta-learning baseline people analogize to. Pretraining is **not** MAML; “pretraining is meta-learning” is a research frame (transformers *can* implement inner-loop-like updates in toys), not an established identity.

Task-level vectors in activation space (still not “the instruction head”):

- [In-context learning creates task vectors](https://scholar.google.com/scholar?q=In-context+learning+creates+task+vectors) (Hendel, Geva & Globerson, 2023)
- [Function vectors in large language models](https://scholar.google.com/scholar?q=Function+vectors+in+large+language+models) (Todd et al., 2024)

Early activation-level control, from a frozen decoder rather than SFT: [Extracting latent steering vectors from pretrained language models](https://scholar.google.com/scholar?q=Extracting+latent+steering+vectors+from+pretrained+language+models) (Subramani et al., 2022) [`subramani2022_extracting_steering_vectors`](../interpretability/subramani2022_extracting_steering_vectors.md); later [Steering language models with activation engineering](https://scholar.google.com/scholar?q=Steering+language+models+with+activation+engineering) (Turner et al., 2024) [`turner2024steeringlanguagemodelsactivation`](../interpretability/turner2024steeringlanguagemodelsactivation.md).

### Alignment-ish behaviors, not a general IF module

These papers localize *pieces* of post-training behavior:

- [Refusal in language models is mediated by a single direction](https://scholar.google.com/scholar?q=Refusal+in+language+models+is+mediated+by+a+single+direction) (Arditi et al., 2024)
- [A mechanistic understanding of alignment algorithms: a case study on DPO and refusal](https://scholar.google.com/scholar?q=A+mechanistic+understanding+of+alignment+algorithms+a+case+study+on+DPO+and+refusal) (Lee et al., 2024)
- [Fine-tuning enhances existing mechanisms: a case study on entity tracking](https://scholar.google.com/scholar?q=Fine-tuning+enhances+existing+mechanisms+a+case+study+on+entity+tracking) (Prakash et al., 2024) — SFT often **amplifies** circuits that already exist, rather than building new ones
- [Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks](https://scholar.google.com/scholar?q=Mechanistically+analyzing+the+effects+of+fine-tuning+on+procedurally+defined+tasks) (Jain et al., 2024)
- Sparse features / production-scale traces: [Scaling monosemanticity: extracting interpretable features from Claude 3 Sonnet](https://scholar.google.com/scholar?q=Scaling+monosemanticity+extracting+interpretable+features+from+Claude+3+Sonnet) (Templeton et al., 2024) [`templeton2024_scaling_monosemanticity`](../interpretability-anthropic/templeton2024_scaling_monosemanticity.md); [On the biology of a large language model](https://scholar.google.com/scholar?q=On+the+biology+of+a+large+language+model) (Lindsey et al., 2025) [`lindsey2025_biology_language_model`](../interpretability-anthropic/lindsey2025_biology_language_model.md)

Open-problem framing: [Open problems in mechanistic interpretability](https://scholar.google.com/scholar?q=Open+problems+in+mechanistic+interpretability) (Sharkey et al., 2025) [`sharkey2025openproblemsmechanisticinterpretability`](../interpretability/sharkey2025openproblemsmechanisticinterpretability.md).

**What this level does not yet give:** a story of the form “instruction tokens activate circuit X, which gates logits on Y, therefore the model obeys.” Production chat models stack pretrain + SFT + RLHF + system prompt; the field has fragments (induction, task vectors, refusal directions, some SAE features), not one instruction-following module.

---

## Suggested reading order

1. Brown et al. 2020 (what ICL is) → Wei et al. 2022 FLAN (what IFT is empirically).
2. Ouyang et al. 2022 InstructGPT → Zhou et al. 2023 LIMA (recipe vs elicitation hypothesis).
3. Olsson et al. 2022 induction heads → Xie / Garg / von Oswald (ICL mechanisms and toy theory).
4. Prakash et al. 2024 and Lee et al. 2024 (what SFT/DPO do to *existing* circuits) → Arditi et al. 2024 (refusal as a direction).
5. Casper et al. 2023 if the interest is the RLHF *process* rather than internals.

---

## One-line synthesis

Instruction following is **real as behavior** and **well engineered as a training stack**. The best current *why* is mixed: ICL uses identifiable circuits (especially induction) plus format matching that improves with scale; SFT/RLHF mostly **elicit and reweight** pretrained capabilities (LIMA-style), with mechanistic localization so far for **narrow** post-training behaviors (refusal, some personas), not for instruction following as a whole.

---

## Appendix: Could HeRD-Merging study which mechanism implements “follow this instruction”?

Speculation only. HeRD-Merging (Kunda, Kurz, Dominik & Maoz, ICLR 2027 draft) is not a circuit-discovery method. It is a **weights → activation** bridge: given LoRA adapters on distinct behavioral axes, first-order steering reads Jacobian columns \(\partial \mathbf{h}_\ell / \partial s_j\) as composable residual-stream directions, and Hessian-regularized merging tries to make that first-order picture accurate. Paper reader: [`hera/readers/14-herd.md`](https://github.com/alexhkurz/hera/blob/main/readers/14-herd.md). Draft: [`hera/latex/main.tex`](https://github.com/alexhkurz/hera/blob/main/latex/main.tex).

The question on the table above is about *internal mechanism*. HeRD can at most answer a nearby question: **where in activation space does a LoRA-style instruction adaptation live, how linear it is, and how it factors across axes.** That is useful for Level 2 (elicitation vs new skills) and as a *target* for Level 3 (circuits), not as a substitute for induction-head-style analysis.

### What HeRD actually gives you

Train \(J\) LoRA adapters on a frozen decoder, merge them with a strength vector \(\mathbf{s}\), and expand \(\mathbf{h}_\ell(\mathbf{x}, \mathbf{s})\) around the base model \(\mathbf{s} = \mathbf{0}\). Column \(j\) of \(J_{\mathbf{s}}\mathbf{h}_\ell(\mathbf{x}, 0)\) is the first-order change in layer \(\ell\) when you turn on axis \(j\). Averaging over prompts yields a fixed steering vector \(\mathbf{v}^*\) that approximates what the weight update does to the residual stream.

HeRD-Merging then (i) adds polynomial interaction corrections so simultaneous axes do not just interfere, and (ii) regularizes Hessian blocks \(H_{\mathbf{ss}}\) (Taylor remainder) and \(H_{\mathbf{xs}}\) (prompt variance of the Jacobian). Small Hessians mean the linear picture is trustworthy; large Hessians mean a single vector is a bad summary of the adaptation.

The paper’s own experiments use three *stylistic* axes (analogies, bullet points, sophisticated language), not instruction following. The method is axis-agnostic; the speculation is whether instruction-related LoRAs are a legitimate family of axes.

### A possible experimental sketch

Pick a base model (pretrained, not chat). Train LoRA adapters that isolate pieces of “follow this instruction,” then read first-order directions instead of only looking at generated text.

Candidate axes (orthogonal enough to be interesting, not claimed to be the true factorization):

| Axis | Endpoint 0 | Endpoint 1 | Why |
|------|------------|------------|-----|
| Format / scaffolding | Completions as LM | User/Assistant (or FLAN-style) wrappers | LIMA: SFT teaches surface form |
| Compliance with the query | Ignore / continue the prefix | Answer the instruction | Core “obey” behavior |
| Refusal / policy | Helpful-only | Helpful + refuse disallowed | Already localized as a direction ([Arditi et al., 2024](https://scholar.google.com/scholar?q=Refusal+in+language+models+is+mediated+by+a+single+direction)) |
| Few-shot ICL | Zero-shot | Demonstrations in context | Mechanistic side is stronger ([Olsson et al., 2022](https://scholar.google.com/scholar?q=In-context+learning+and+induction+heads); [`olsson2022_induction_heads`](../interpretability-anthropic/olsson2022_induction_heads.md)) |

Then:

1. **Layer profile.** The Jacobian exists at every adapted layer. A peak in \(\|\partial \mathbf{h}_\ell / \partial s_{\mathrm{IF}}\|\) is a cheap localization of *where* the instruction adapter writes — not which heads, but which residual-stream stages. Compare to CAA/RepE on the same prompts ([`zou2023representationengineeringtopdownapproach`](../interpretability/zou2023representationengineeringtopdownapproach.md), [`panickssery2024steeringllama2contrastive`](../interpretability/panickssery2024steeringllama2contrastive.md)).
2. **Hessian as a test of LIMA.** If instruction SFT is mostly elicitation of a linear format/policy direction, \(H_{\mathbf{ss}}\) and \(H_{\mathbf{xs}}\) should be small and \(\mathbf{v}^*\) should transfer across prompts. If following is a new, prompt-dependent computation, the mixed Hessian \(H_{\mathbf{xs}}\) should stay large and a single vector should fail — HeRD’s own reliability diagnostics, used as a scientific instrument rather than only a merging regularizer.
3. **Composability vs one blob.** Merge format, compliance, and refusal with HeRD. If exact-combination behavior tracks \(\mathbf{s}\) (as in the paper’s style experiments), “instruction following” is a *bundle of directions*, not one module. If interaction corrections dominate, the axes are not independent in weight space.
4. **SFT vs DPO vs RLHF as different \(\mathbf{s}\)-families.** Train adapters on demonstration SFT, on DPO/refusal data, and (if feasible) on a preference stage. First-order directions plus Prakash et al. (2024) / Lee et al. (2024) ([fine-tuning enhances existing mechanisms](https://scholar.google.com/scholar?q=Fine-tuning+enhances+existing+mechanisms+a+case+study+on+entity+tracking); [mechanistic understanding of DPO and refusal](https://scholar.google.com/scholar?q=A+mechanistic+understanding+of+alignment+algorithms+a+case+study+on+DPO+and+refusal)) would test whether later stages *rotate the same vector* or *add new columns*.
5. **Hand the vector to circuit tools.** Once \(\mathbf{v}^*\) is stable, treat it as the thing to explain: which heads write into it, does it overlap induction / IOI / refusal features, do SAEs isolate it ([`templeton2024_scaling_monosemanticity`](../interpretability-anthropic/templeton2024_scaling_monosemanticity.md)). HeRD proposes the direction; circuits still have to account for it.

### Why this is not an answer to the table row

HeRD does not identify heads, MLPs, or an “instruction circuit.” A Jacobian column is a *summary of a LoRA update at a layer*, averaged over prompts. If instruction following is not well modeled as a few LoRA axes — e.g. it is mostly ICL circuits already in the base model, only elicited by prompts — then training an “IF adapter” may just rediscover format/refusal, and the method will look successful while missing the mechanism.

Further limits, already visible in the draft:

- Experiments used lexically loud style labels and DeBERTa classifiers. “Did the model follow the instruction?” is a messier eval than “did it use bullet points?”
- Interaction terms scale as \(2^J\); a rich factorization of IF is expensive unless you restrict to pairwise corrections.
- First-order steering approximates *small* \(\mathbf{s}\). Chat SFT is a large distributional shift; the Taylor remainder may be the scientifically interesting part, not an error to kill.
- \(H_{\mathbf{xx}}\) (sensitivity to prompt wording) is not controlled. Instruction following is exactly the regime where the same adapter should behave differently on “Summarize this” vs “Ignore previous instructions.”

### Tentative bet

HeRD is a plausible tool for **splitting instruction-related SFT into linear residual-stream directions and measuring whether that split is faithful**. That would sharpen Level 2 (elicitation vs new nonlinear computation) and give circuit work a better target than “the chat model minus the base.” It would not, by itself, complete Level 3. The honest use is: train IF-related LoRAs, read \(J_{\mathbf{s}}\mathbf{h}_\ell\) and the Hessians, and treat large \(H_{\mathbf{xs}}\) as evidence that “follow this instruction” is not one steering vector.
