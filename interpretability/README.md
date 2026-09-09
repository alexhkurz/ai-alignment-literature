# Interpretability

Mechanistic interpretability, activation steering, sparse autoencoders, LoRA / PEFT, and model merging — seeded from the [hera](https://github.com/alexhkurz/hera) (HeRD-Merging) paper bibliography.

PDFs are local (gitignored). Text extracts (`{citationkey}.txt`) are **local cache** when `bib.bib` records a public PDF (arXiv, OpenReview, ACL Anthology, …) — regenerate with `../scripts/ensure-extract.sh {citationkey}`. Only **pinned** extracts without a public PDF stay in git (e.g. `bricken2023towards`).

## Reader background (Tier A — curated notes)

HeRA / HeRD-Merging reader prerequisites ([`hera/readers/`](https://github.com/alexhkurz/hera/tree/main/readers)).

- Rumelhart & Hinton & Williams - [Learning representations by back-propagating errors](https://scholar.google.com/scholar?q=Learning+representations+by+back-propagating+errors) (1986) - [PDF](https://doi.org/10.1038/323533a0) - [`rumelhart1986_backprop`](rumelhart1986_backprop.md)
- Pearlmutter - [Fast exact multiplication by the Hessian](https://scholar.google.com/scholar?q=Pearlmutter+Fast+Exact+Multiplication+Hessian) (1994) - [PDF](https://mural.maynoothuniversity.ie/5501/1/BP_fast%20exact.pdf) - [`pearlmutter1994_fast_hessian`](pearlmutter1994_fast_hessian.md)
- Martens - [Deep learning via Hessian-free optimization](https://scholar.google.com/scholar?q=Deep+Learning+via+Hessian-Free+Optimization+Martens) (2010) - [PDF](https://icml.cc/Conferences/2010/papers/458.pdf) - [`martens2010_hessian_free`](martens2010_hessian_free.md)
- He & Zhang & Ren & Sun - [Deep residual learning for image recognition](https://scholar.google.com/scholar?q=Deep+Residual+Learning+Image+Recognition) (2016) - [PDF](https://arxiv.org/pdf/1512.03385.pdf) - [`he2016_deep_residual`](he2016_deep_residual.md)
- Vaswani et al. - [Attention is all you need](https://scholar.google.com/scholar?q=Attention+Is+All+You+Need) (2017) - [PDF](https://arxiv.org/pdf/1706.03762.pdf) - [`vaswani2017_attention`](vaswani2017_attention.md)
- Elhage et al. - [A mathematical framework for transformer circuits](https://scholar.google.com/scholar?q=Mathematical+Framework+Transformer+Circuits+Elhage) (2021) - [thread](https://transformer-circuits.pub/2021/framework/index.html) - [`elhage2021_transformer_circuits`](elhage2021_transformer_circuits.md)
- Aghajanyan & Zettlemoyer & Gupta - [Intrinsic dimensionality explains the effectiveness of language model fine-tuning](https://scholar.google.com/scholar?q=Intrinsic+Dimensionality+Explains+Effectiveness+Language+Model+Fine-Tuning) (2021) - [PDF](https://arxiv.org/pdf/2012.13255.pdf) - [`aghajanyan2021_intrinsic_dimensionality`](aghajanyan2021_intrinsic_dimensionality.md)
- Geva et al. - [Transformer feed-forward layers are key-value memories](https://scholar.google.com/scholar?q=Transformer+Feed+Forward+Layers+Key+Value+Memories) (2021) - [PDF](https://arxiv.org/pdf/2012.14913.pdf) - [`geva2021_key_value_memories`](geva2021_key_value_memories.md)
- Dar et al. - [Analyzing transformers in embedding space](https://scholar.google.com/scholar?q=Analyzing+Transformers+in+Embedding+Space) (2023) - [PDF](https://arxiv.org/pdf/2209.02535.pdf) - [`dar2022_analyzing_transformers`](dar2022_analyzing_transformers.md)

## Activation steering reader (curated notes)

HeRA reader [`04-activation-steering`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md) — linear representation, probing, causal interpretability, steering baselines.

- Mikolov et al. - [Distributed representations of words and phrases](https://scholar.google.com/scholar?q=Mikolov+Distributed+Representations+Words+Phrases+Compositionality+2013) (2013) - [PDF](https://arxiv.org/pdf/1310.4546.pdf) - [`mikolov2013_word2vec`](mikolov2013_word2vec.md)
- Tenney et al. - [What do you learn from context? (edge probing)](https://scholar.google.com/scholar?q=What+do+you+learn+from+context+Tenney+probing+sentence+structure+2019) (2019) - [PDF](https://arxiv.org/pdf/1905.06316.pdf) - [`tenney2019_edge_probing`](tenney2019_edge_probing.md)
- Tenney et al. - [BERT rediscovers the classical NLP pipeline](https://scholar.google.com/scholar?q=Tenney+BERT+Rediscovers+Classical+NLP+Pipeline+2019) (2019) - [PDF](https://aclanthology.org/P19-1452.pdf) - [`tenney2019_bert_pipeline`](tenney2019_bert_pipeline.md)
- Belinkov & Glass - [Analysis methods in neural NLP](https://scholar.google.com/scholar?q=Belinkov+Glass+Analysis+Methods+Neural+NLP+2019) (2019) - [PDF](https://arxiv.org/pdf/1812.08951.pdf) - [`belinkov2019_analysis_methods`](belinkov2019_analysis_methods.md)
- Kim et al. - [TCAV](https://scholar.google.com/scholar?q=Kim+Interpretability+Beyond+Classification+Accuracy+TCAV+2018) (2018) - [PDF](https://openreview.net/pdf?id=SyEnZ-W0b) - [`kim2018tcav`](kim2018tcav.md)
- Meng et al. - [ROME: locating and editing factual associations in GPT](https://scholar.google.com/scholar?q=Meng+Locating+Editing+Factual+Associations+GPT+ROME+2022) (2022) - [PDF](https://arxiv.org/pdf/2202.05262.pdf) - [`meng2022_rome`](meng2022_rome.md)
- Wang et al. - [IOI circuit in GPT-2 small](https://scholar.google.com/scholar?q=Wang+Interpretability+Wild+Circuit+IOI+GPT2+2022) (2022) - [PDF](https://arxiv.org/pdf/2211.00593.pdf) - [`wang2022_ioi`](wang2022_ioi.md)
- Olsson et al. - [In-context learning and induction heads](https://scholar.google.com/scholar?q=Olsson+In+Context+Learning+Induction+Heads+2022) (2022) - [PDF](https://arxiv.org/pdf/2209.11895.pdf) - [`olsson2022_induction_heads`](olsson2022_induction_heads.md)
- Elhage et al. - [Toy models of superposition](https://scholar.google.com/scholar?q=Elhage+Toy+Models+Superposition+2022) (2022) - [PDF](https://arxiv.org/pdf/2209.10652.pdf) - [`elhage2022_superposition`](elhage2022_superposition.md)
- Hanna et al. - [How does GPT-2 compute greater-than?](https://scholar.google.com/scholar?q=Hanna+GPT2+Compute+Greater+Than+2023) (2023) - [PDF](https://arxiv.org/pdf/2305.00586.pdf) - [`hanna2023_greater_than`](hanna2023_greater_than.md)

## Other curated notes

- Cunningham et al. - [Sparse autoencoders find highly interpretable features in language models](https://scholar.google.com/scholar?q=Sparse+Autoencoders+Highly+Interpretable+Features+Cunningham) (2023) - [PDF](https://arxiv.org/pdf/2309.08600) - [`cunningham2023sparseautoencodershighlyinterpretable`](cunningham2023sparseautoencodershighlyinterpretable.md)
- Ding et al. - [Enhancing chat language models by scaling high-quality instructional conversations](https://scholar.google.com/scholar?q=Enhancing+Chat+Language+Models+Scaling+UltraChat) (2023) - [PDF](https://arxiv.org/pdf/2305.14233) - [`ding2023enhancingchatlanguagemodels`](ding2023enhancingchatlanguagemodels.md)
- He, Gao & Chen - [DeBERTaV3: Improving DeBERTa using ELECTRA-style pre-training](https://scholar.google.com/scholar?q=DeBERTaV3) (2023) - [PDF](https://arxiv.org/pdf/2111.09543) - [`he2023debertav`](he2023debertav.md)
- Bai (Qwen Team) - [Qwen2.5-VL technical report](https://scholar.google.com/scholar?q=Qwen2.5-VL+Technical+Report) (2025) - [PDF](https://arxiv.org/pdf/2502.13923) - [`bai2025qwen25vltechnicalreport`](bai2025qwen25vltechnicalreport.md)
- Braun et al. - [Understanding (un)reliability of steering vectors in language models](https://scholar.google.com/scholar?q=Understanding+Unreliability+Steering+Vectors) (2025) - [PDF](https://arxiv.org/pdf/2505.22637) - [`braun2025understanding`](braun2025understanding.md)
- Dunefsky & Cohan - [One-shot optimized steering vectors mediate safety-relevant behaviors in LLMs](https://scholar.google.com/scholar?q=One-shot+Optimized+Steering+Vectors) (2025) - [PDF](https://arxiv.org/pdf/2502.18862) - [`dunefsky2025oneshot`](dunefsky2025oneshot.md)
- Apolinario & Roy - [LANCE: Low-rank activation compression for efficient on-device continual learning](https://scholar.google.com/scholar?q=LANCE+Low+Rank+Activation+Compression) (2026) - [PDF](https://arxiv.org/pdf/2509.21617) - [`apolinario2026lancelowrankactivation`](apolinario2026lancelowrankactivation.md)
- Fang et al. - [Controllable LLM reasoning via sparse autoencoder-based steering](https://scholar.google.com/scholar?q=Controllable+LLM+Reasoning+SAE+Steering) (2026) - [PDF](https://arxiv.org/pdf/2507.06261) - [`fang-etal-2026-controllable`](fang-etal-2026-controllable.md)
- Gemma Team - [Gemma 4 technical report](https://scholar.google.com/scholar?q=Gemma+4+Technical+Report) (2026) - [PDF](https://arxiv.org/pdf/2607.02770) - [`gemmateam2026gemma4technicalreport`](gemmateam2026gemma4technicalreport.md)
- Heyman & Vandeputte - [Steer like the LLM: activation steering that mimics prompting](https://scholar.google.com/scholar?q=Steer+Like+the+LLM+Activation+Steering) (2026) - [PDF](https://arxiv.org/pdf/2605.03907) - [`heyman2026steer`](heyman2026steer.md)
- Ho et al. - [Language models can control their own attention](https://scholar.google.com/scholar?q=Language+Models+Can+Control+Their+Own+Attention+Ho+2026) (2026) - [PDF](https://arxiv.org/pdf/2609.02737) - [`ho2026declarative_attention`](ho2026declarative_attention.md)

## Papers with local extract (regenerate; not in git)

- `apolinario2026lancelowrankactivation`
- `bai2025qwen25vltechnicalreport`
- `braun2025understanding`
- `bricken2023towards` (HTML extract; no PDF)
- `cunningham2023sparseautoencodershighlyinterpretable`
- `ding2023enhancingchatlanguagemodels`
- `dunefsky2025oneshot`
- `fang-etal-2026-controllable`
- `gemmateam2026gemma4technicalreport`
- `he2023debertav`
- `heyman2026steer`
- `hu2021loralowrankadaptation`
- `ilharco2023editingmodelstaskarithmetic`
- `kangaslahti2025continuous`
- `kim2018tcav`
- `kingma2017adammethodstochasticoptimization`
- `koike-akino2025quantumpeft`
- `kong2024aligning`
- `leask2025inferencetimedecompositionactivationsitda`
- `li2024llmsasjudgescomprehensivesurveyllmbased`
- `menon-etal-2025-analyzing`
- `nelwan2026deployableperinstancemultilayeractivation`
- `panickssery2024steeringllama2contrastive`
- `pham-nguyen-2024-householder`
- `pmlr-v235-singh24d`
- `prabhakar2024lorasoupsmergingloras`
- `rodriguez2024controllinglanguagediffusionmodels`
- `sharkey2025openproblemsmechanisticinterpretability`
- `sharma2026coldsteer`
- `shu2025surveysparseautoencodersinterpreting`
- `soo2025interpretable`
- `stoica2024modelmergingsvdtie`
- `tan2024analysing`
- `turner2024steeringlanguagemodelsactivation`
- `wortsman2021_neural_subspaces`
- `xu-etal-2026-steering`
- `yadav2023tiesmerging`
- `yu2024language`
- `zhao2026odesteer`
- `zou2023representationengineeringtopdownapproach`

## Bibliography-only (no local PDF yet)

- `sun2025layernavigator` — OpenReview only (bot challenge)
- `11224465` — IEEE Access (paywalled)
- `levenbergmarquardt` — book chapter
- `ramsay2005functional` — book

Consumer: [`hera`](https://github.com/alexhkurz/hera).
