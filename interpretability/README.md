# Interpretability

Mechanistic interpretability, activation steering, sparse autoencoders, LoRA / PEFT, and model merging — seeded from the [hera](https://github.com/alexhkurz/hera) (HeRD-Merging) paper bibliography.

PDFs are local (gitignored). Text extracts (`{citationkey}.txt`) are **local cache** when `bib.bib` records a public PDF (arXiv, OpenReview, ACL Anthology, …) — regenerate with `../scripts/ensure-extract.sh {citationkey}`. Only **pinned** extracts without a public PDF stay in git (e.g. `bricken2023towards`).

## Reader background (Tier A — curated notes)

HeRA / HeRD-Merging reader prerequisites ([`hera/readers/`](https://github.com/alexhkurz/hera/tree/main/readers)).

- Rumelhart & Hinton & Williams - [Learning representations by back-propagating errors](https://scholar.google.com/scholar?q=Learning+representations+by+back-propagating+errors) (1986) - [PDF](https://doi.org/10.1038/323533a0) - [`rumelhart1986_backprop`](rumelhart1986_backprop-notes.md)
- Pearlmutter - [Fast exact multiplication by the Hessian](https://scholar.google.com/scholar?q=Pearlmutter+Fast+Exact+Multiplication+Hessian) (1994) - [PDF](https://mural.maynoothuniversity.ie/5501/1/BP_fast%20exact.pdf) - [`pearlmutter1994_fast_hessian`](pearlmutter1994_fast_hessian-notes.md)
- Martens - [Deep learning via Hessian-free optimization](https://scholar.google.com/scholar?q=Deep+Learning+via+Hessian-Free+Optimization+Martens) (2010) - [PDF](https://icml.cc/Conferences/2010/papers/458.pdf) - [`martens2010_hessian_free`](martens2010_hessian_free-notes.md)
- He & Zhang & Ren & Sun - [Deep residual learning for image recognition](https://scholar.google.com/scholar?q=Deep+Residual+Learning+Image+Recognition) (2016) - [PDF](https://arxiv.org/pdf/1512.03385.pdf) - [`he2016_deep_residual`](he2016_deep_residual-notes.md)
- Vaswani et al. - [Attention is all you need](https://scholar.google.com/scholar?q=Attention+Is+All+You+Need) (2017) - [PDF](https://arxiv.org/pdf/1706.03762.pdf) - [`vaswani2017_attention`](vaswani2017_attention-notes.md)
- Elhage et al. - [A mathematical framework for transformer circuits](https://scholar.google.com/scholar?q=Mathematical+Framework+Transformer+Circuits+Elhage) (2021) - [thread](https://transformer-circuits.pub/2021/framework/index.html) - [`elhage2021_transformer_circuits`](elhage2021_transformer_circuits-notes.md)
- Aghajanyan & Zettlemoyer & Gupta - [Intrinsic dimensionality explains the effectiveness of language model fine-tuning](https://scholar.google.com/scholar?q=Intrinsic+Dimensionality+Explains+Effectiveness+Language+Model+Fine-Tuning) (2021) - [PDF](https://arxiv.org/pdf/2012.13255.pdf) - [`aghajanyan2021_intrinsic_dimensionality`](aghajanyan2021_intrinsic_dimensionality-notes.md)
- Geva et al. - [Transformer feed-forward layers are key-value memories](https://scholar.google.com/scholar?q=Transformer+Feed+Forward+Layers+Key+Value+Memories) (2021) - [PDF](https://arxiv.org/pdf/2012.14913.pdf) - [`geva2021_key_value_memories`](geva2021_key_value_memories-notes.md)
- Dar et al. - [Analyzing transformers in embedding space](https://scholar.google.com/scholar?q=Analyzing+Transformers+in+Embedding+Space) (2023) - [PDF](https://arxiv.org/pdf/2209.02535.pdf) - [`dar2022_analyzing_transformers`](dar2022_analyzing_transformers-notes.md)

## Activation steering reader (curated notes)

HeRA reader [`04-activation-steering`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md) — linear representation, probing, causal interpretability, steering baselines.

- Mikolov et al. - [Distributed representations of words and phrases](https://scholar.google.com/scholar?q=Mikolov+Distributed+Representations+Words+Phrases+Compositionality+2013) (2013) - [PDF](https://arxiv.org/pdf/1310.4546.pdf) - [`mikolov2013_word2vec`](mikolov2013_word2vec-notes.md)
- Tenney et al. - [BERT rediscovers the classical NLP pipeline](https://scholar.google.com/scholar?q=Tenney+BERT+Rediscovers+Classical+NLP+Pipeline+2019) (2019) - [PDF](https://aclanthology.org/P19-1452.pdf) - [`tenney2019_bert_pipeline`](tenney2019_bert_pipeline-notes.md)
- Belinkov & Glass - [Analysis methods in neural NLP](https://scholar.google.com/scholar?q=Belinkov+Glass+Analysis+Methods+Neural+NLP+2019) (2019) - [PDF](https://arxiv.org/pdf/1812.08951.pdf) - [`belinkov2019_analysis_methods`](belinkov2019_analysis_methods-notes.md)
- Kim et al. - [TCAV](https://scholar.google.com/scholar?q=Kim+Interpretability+Beyond+Classification+Accuracy+TCAV+2018) (2018) - [PDF](https://openreview.net/pdf?id=SyEnZ-W0b) - [`kim2018tcav`](kim2018tcav-notes.md)
- Meng et al. - [ROME: locating and editing factual associations in GPT](https://scholar.google.com/scholar?q=Meng+Locating+Editing+Factual+Associations+GPT+ROME+2022) (2022) - [PDF](https://arxiv.org/pdf/2202.05262.pdf) - [`meng2022_rome`](meng2022_rome-notes.md)
- Wang et al. - [IOI circuit in GPT-2 small](https://scholar.google.com/scholar?q=Wang+Interpretability+Wild+Circuit+IOI+GPT2+2022) (2022) - [PDF](https://arxiv.org/pdf/2211.00593.pdf) - [`wang2022_ioi`](wang2022_ioi-notes.md)
- Olsson et al. - [In-context learning and induction heads](https://scholar.google.com/scholar?q=Olsson+In+Context+Learning+Induction+Heads+2022) (2022) - [PDF](https://arxiv.org/pdf/2209.11895.pdf) - [`olsson2022_induction_heads`](olsson2022_induction_heads-notes.md)
- Elhage et al. - [Toy models of superposition](https://scholar.google.com/scholar?q=Elhage+Toy+Models+Superposition+2022) (2022) - [PDF](https://arxiv.org/pdf/2209.10652.pdf) - [`elhage2022_superposition`](elhage2022_superposition-notes.md)
- Hanna et al. - [How does GPT-2 compute greater-than?](https://scholar.google.com/scholar?q=Hanna+GPT2+Compute+Greater+Than+2023) (2023) - [PDF](https://arxiv.org/pdf/2305.00586.pdf) - [`hanna2023_greater_than`](hanna2023_greater_than-notes.md)

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
