# Background Reader: Global Workspace Theory

Background for the talk on Gurnee et al. (2026) [Verbalizable Representations Form a Global Workspace in Language Models](https://scholar.google.com/scholar?q=Verbalizable+Representations+Form+a+Global+Workspace+in+Language+Models+Gurnee+2026). The paper frames its results in the language of global workspace theory (GWT), "because it is the account whose functional predictions our experiments were designed to test". This reader covers what the theory says, where it came from, what it explains and what it leaves open, how it compares with its competitors, and how it has been carried over to AI. The last section maps the theory onto the paper.

## Contents

- [1. The theory in one page](#1-the-theory-in-one-page)
- [2. What the theory reacts to](#2-what-the-theory-reacts-to)
- [3. History](#3-history)
  - [3.1 Blackboards and pandemonium](#31-blackboards-and-pandemonium)
  - [3.2 Baars 1988: the cognitive theory](#32-baars-1988-the-cognitive-theory)
  - [3.3 Dehaene and Changeux: the global neuronal workspace](#33-dehaene-and-changeux-the-global-neuronal-workspace)
  - [3.4 Ignition and the experimental programme](#34-ignition-and-the-experimental-programme)
  - [3.5 Computational and robotic versions](#35-computational-and-robotic-versions)
- [4. Which problems it solves](#4-which-problems-it-solves)
- [5. Which problems it does not solve](#5-which-problems-it-does-not-solve)
- [6. Competitors](#6-competitors)
  - [6.1 Higher-order theories](#61-higher-order-theories)
  - [6.2 Recurrent processing theory](#62-recurrent-processing-theory)
  - [6.3 Integrated information theory](#63-integrated-information-theory)
  - [6.4 Attention schema theory](#64-attention-schema-theory)
  - [6.5 Predictive processing and multiple drafts](#65-predictive-processing-and-multiple-drafts)
  - [6.6 Comparison table](#66-comparison-table)
  - [6.7 The adversarial collaboration](#67-the-adversarial-collaboration)
- [7. Global workspace theory and AI](#7-global-workspace-theory-and-ai)
- [8. How Gurnee et al. use the theory](#8-how-gurnee-et-al-use-the-theory)
- [9. Reading list](#9-reading-list)

---

## 1. The theory in one page

Global workspace theory is a functional theory of conscious access. Its claims, in the form most authors share:

1. **Specialist processors.** The brain contains many specialised processors (for vision, language, motor control, memory retrieval, and so on). They run in parallel, they are fast and efficient within their domain, and their work is unconscious.
2. **Workspace.** There is a shared **global workspace**: a limited-capacity medium that many processors can write to and, more importantly, read from.
3. **Broadcast.** A content becomes conscious when it enters the workspace and is broadcast to all the processors at once. Broadcast is what makes the content available for verbal report, for reasoning, for planning, for memory storage and for control of action.
4. **Limited capacity and competition.** The workspace holds only a little at a time. Contents compete for entry; attention is the gatekeeper that decides which content wins.
5. **Serial over parallel.** Unconscious processing is massively parallel; conscious processing is serial, one content after another. The serial stream is the price of making each content globally available.

The notion of consciousness at stake is **access consciousness**, which Block (1995) defined as a state whose content is "poised" for use in reasoning and in the rational control of action and speech. Access consciousness is a functional notion. It is distinct from **phenomenal consciousness**, the "what it is like" of experience. GWT is a theory of the first. Whether it is also a theory of the second is one of the main points of dispute (Section 5).

**Slogan.** Baars's own metaphor is a theatre: the workspace is a lit stage, attention is the spotlight, and the unconscious processors are the audience in the dark, each of which sees whatever is on stage. Dennett's version is "fame in the brain": a content is conscious when it is influential across the whole system. Neither metaphor is the theory; the theory is claims 1–5.

---

## 2. What the theory reacts to

GWT was built in the 1980s, when cognitive psychology had made consciousness respectable again after behaviourism, but had no theory of what it is for. Several bodies of evidence pressed the question.

**Most processing is unconscious.** Subliminal priming, implicit memory and implicit learning showed that complex processing (including word meaning) can happen without awareness. The striking clinical case was **blindsight** (Weiskrantz, [Blindsight: A Case Study and Implications](https://scholar.google.com/scholar?q=Blindsight+A+Case+Study+and+Implications+Weiskrantz+1986)): patients with damage to primary visual cortex deny seeing stimuli in part of the visual field, yet point to them or discriminate them well above chance. If so much can be done without consciousness, what does consciousness add?

**Automaticity.** Shiffrin and Schneider, [Controlled and Automatic Human Information Processing](https://scholar.google.com/scholar?q=Controlled+and+automatic+human+information+processing+Shiffrin+Schneider+1977), separated fast, parallel, practised, effortless processing from slow, serial, effortful, flexible processing. Practice moves a skill from the second kind to the first, and it drops out of awareness as it does.

**Capacity limits.** Broadbent's [Perception and Communication](https://scholar.google.com/scholar?q=Perception+and+Communication+Broadbent+1958) introduced the idea of a limited-capacity channel with an attentional filter in front of it. Later work fixed working memory capacity at a handful of items (Cowan, [The magical number 4 in short-term memory](https://scholar.google.com/scholar?q=The+magical+number+4+in+short-term+memory+Cowan+2001)). A theory of consciousness has to explain why such a powerful brain is so narrow at the point of awareness.

**Modularity.** Fodor's [The Modularity of Mind](https://scholar.google.com/scholar?q=The+Modularity+of+Mind+Fodor+1983) argued that input systems are fast, domain-specific and informationally encapsulated, while "central" thought is slow, global and unencapsulated. Fodor thought the central system was beyond the reach of cognitive science. GWT can be read as an answer: the central system is a broadcast medium that lets encapsulated modules share results.

**Integration and the frame problem.** A system of specialists needs a way to bring the right specialists to bear on a novel problem without consulting all of them at all times. Shanahan and Baars, [Applying global workspace theory to the frame problem](https://scholar.google.com/scholar?q=Applying+global+workspace+theory+to+the+frame+problem+Shanahan+Baars+2005), argue that broadcast plus competition does this: every specialist sees the current content, and only those with something relevant to contribute respond.

**Method.** Baars's key methodological move was **contrastive analysis**: compare pairs of cases that are as similar as possible except that in one the content is conscious and in the other it is not (a masked vs. an unmasked word, an attended vs. an unattended message, a novel vs. a practised skill). Whatever differs systematically between the members of each pair is a candidate for what consciousness does. Crick and Koch, [Towards a neurobiological theory of consciousness](https://scholar.google.com/scholar?q=Towards+a+neurobiological+theory+of+consciousness+Crick+Koch+1990), later made the same move the programme for neuroscience: the search for neural correlates of consciousness.

---

## 3. History

### 3.1 Blackboards and pandemonium

The architecture of GWT comes from AI. Selfridge's [Pandemonium: A paradigm for learning](https://scholar.google.com/scholar?q=Pandemonium+A+paradigm+for+learning+Selfridge+1959) had many independent "demons", each shouting in proportion to how well its pattern matched, with a decision demon listening to the loudest. The Hearsay-II speech understanding system (Erman, Hayes-Roth, Lesser and Reddy, [The Hearsay-II speech-understanding system: Integrating knowledge to resolve uncertainty](https://scholar.google.com/scholar?q=The+Hearsay-II+speech-understanding+system+Integrating+knowledge+to+resolve+uncertainty+Erman+1980)) introduced the **blackboard architecture**: independent knowledge sources (acoustic, phonetic, lexical, syntactic, semantic) read from and write hypotheses to a shared data structure, the blackboard, under a scheduler that decides which source acts next. Baars acknowledged blackboard systems as the direct model for the workspace. The difference is emphasis: a blackboard is a software engineering pattern; the workspace is a claim about which states of a brain are conscious.

### 3.2 Baars 1988: the cognitive theory

Bernard Baars stated the theory in [A Cognitive Theory of Consciousness](https://scholar.google.com/scholar?q=A+Cognitive+Theory+of+Consciousness+Baars+1988). The book works through contrastive analysis case by case and builds up the architecture of Section 1, together with additional machinery: **contexts** (unconscious coalitions of processors that shape what enters the workspace, for example goals and expectations), a role for the workspace in learning (novel material must be conscious to be learned; practised material can drop out), and a role in voluntary control. The popular version is [In the Theater of Consciousness](https://scholar.google.com/scholar?q=In+the+Theater+of+Consciousness+The+Workspace+of+the+Mind+Baars+1997). Baars's later review, [Global workspace theory of consciousness: toward a cognitive neuroscience of human experience](https://scholar.google.com/scholar?q=Global+workspace+theory+of+consciousness+toward+a+cognitive+neuroscience+of+human+experience+Baars+2005), connects the cognitive theory to the brain imaging results of the 1990s and early 2000s.

### 3.3 Dehaene and Changeux: the global neuronal workspace

Stanislas Dehaene, Michel Kerszberg and Jean-Pierre Changeux turned the cognitive theory into a neural one in [A neuronal model of a global workspace in effortful cognitive tasks](https://scholar.google.com/scholar?q=A+neuronal+model+of+a+global+workspace+in+effortful+cognitive+tasks+Dehaene+Kerszberg+Changeux+1998). The **global neuronal workspace** (GNW) hypothesis says that the workspace is implemented by a distributed set of cortical neurons with long-range axons, especially pyramidal cells in layers II/III, densest in prefrontal, parietal and cingulate cortex. These neurons connect distant areas reciprocally. When a content is amplified by top-down attention, these connections can lock a set of areas into a self-sustaining, reverberating state that makes the content available everywhere at once.

Dehaene and Naccache, [Towards a cognitive neuroscience of consciousness: basic evidence and a workspace framework](https://scholar.google.com/scholar?q=Towards+a+cognitive+neuroscience+of+consciousness+basic+evidence+and+a+workspace+framework+Dehaene+Naccache+2001), set out the framework and its empirical basis. Dehaene, Changeux, Naccache, Sackur and Sergent, [Conscious, preconscious, and subliminal processing: a testable taxonomy](https://scholar.google.com/scholar?q=Conscious+preconscious+and+subliminal+processing+a+testable+taxonomy+Dehaene+2006), distinguish three states:

- **Subliminal**: bottom-up activation too weak to trigger ignition, whatever attention does.
- **Preconscious**: activation strong enough, but not attended (so it does not enter the workspace now, though it could).
- **Conscious**: strong activation plus attention, giving ignition and broadcast.

The book-length statement is Dehaene's [Consciousness and the Brain](https://scholar.google.com/scholar?q=Consciousness+and+the+Brain+Deciphering+How+the+Brain+Codes+Our+Thoughts+Dehaene+2014). The most recent overview from the core group is Mashour, Roelfsema, Changeux and Dehaene, [Conscious processing and the global neuronal workspace hypothesis](https://scholar.google.com/scholar?q=Conscious+processing+and+the+global+neuronal+workspace+hypothesis+Mashour+Roelfsema+Changeux+Dehaene+2020).

### 3.4 Ignition and the experimental programme

The GNW's most distinctive prediction is **ignition**: entry into the workspace is a sudden, nonlinear, all-or-none transition. Below threshold, activation stays local and decays; above it, activation jumps to a sustained, global state. The prediction has three observable parts.

- **Bimodality at threshold.** If a stimulus is presented right at the threshold of visibility, trials should split into two classes (seen and unseen) rather than form a continuum. Sergent and Dehaene, [Is consciousness a gradual phenomenon? Evidence for an all-or-none bifurcation during the attentional blink](https://scholar.google.com/scholar?q=Is+consciousness+a+gradual+phenomenon+Evidence+for+an+all-or-none+bifurcation+during+the+attentional+blink+Sergent+Dehaene+2004), report such a split in subjective visibility ratings.
- **Late, nonlinear brain signals.** Early sensory responses grow smoothly with stimulus strength; from about 300 ms, activity diverges sharply between seen and unseen trials. Del Cul, Baillet and Dehaene, [Brain dynamics underlying the nonlinear threshold for access to consciousness](https://scholar.google.com/scholar?q=Brain+dynamics+underlying+the+nonlinear+threshold+for+access+to+consciousness+Del+Cul+Baillet+Dehaene+2007), and Sergent, Baillet and Dehaene, [Timing of the brain events underlying access to consciousness during the attentional blink](https://scholar.google.com/scholar?q=Timing+of+the+brain+events+underlying+access+to+consciousness+during+the+attentional+blink+Sergent+Baillet+Dehaene+2005), are the standard references. The EEG component most often cited is the P3b, a late positive wave over parietal cortex.
- **Global signatures.** Conscious trials show widespread activation including prefrontal and parietal cortex, long-distance synchronisation, and the ability to decode the content from many areas (reviewed in Dehaene and Changeux, [Experimental and theoretical approaches to conscious processing](https://scholar.google.com/scholar?q=Experimental+and+theoretical+approaches+to+conscious+processing+Dehaene+Changeux+2011)).

The paradigms are minimal contrasts in the sense of Section 2: visual masking, the attentional blink (a second target in a rapid stream is often missed if it follows the first within about half a second), inattentional blindness, and binocular rivalry.

**Remark.** Ignition is the part of GWT that Gurnee et al. test most directly in a language model (Section 8). They feed the model a mixture of two concept embeddings and ask whether its commitment to one reading jumps sharply at the layer where the workspace starts.

### 3.5 Computational and robotic versions

GWT has had a parallel life as a design for artificial agents.

- Franklin's IDA and LIDA architectures (Franklin, Madl, D'Mello and Snaider, [LIDA: A systems-level architecture for cognition, emotion, and learning](https://scholar.google.com/scholar?q=LIDA+A+systems-level+architecture+for+cognition+emotion+and+learning+Franklin+2014)) implement a cognitive cycle with a workspace, coalitions competing for attention, and broadcast.
- Shanahan, [A cognitive architecture that combines internal simulation with a global workspace](https://scholar.google.com/scholar?q=A+cognitive+architecture+that+combines+internal+simulation+with+a+global+workspace+Shanahan+2006), and the book [Embodiment and the Inner Life](https://scholar.google.com/scholar?q=Embodiment+and+the+Inner+Life+Cognition+and+Consciousness+in+the+Space+of+Possible+Minds+Shanahan+2010) use a workspace for a robot that simulates actions before taking them.

Section 7 covers the deep learning era.

---

## 4. Which problems it solves

GWT's strength is that it accounts for a cluster of functional facts with one architecture. "Accounts for" needs care, because the architecture was built from those facts by contrastive analysis (Section 2). Some items below are built into the theory and only unified by it; others are derived from something further, or predicted in advance.

1. **Limited capacity: stipulated in the cognitive theory, given a mechanism in the neural one.** Baars took the capacity limit from the experimental literature and wrote it into the architecture (claim 4 in Section 1). What the theory adds is a rationale: if a content is to be sent to every consumer at once, the medium can carry only one coherent content at a time, or the consumers would receive a mixture. This is an argument that a broadcast system should have a bottleneck, not a derivation of the limit from independent principles, and it does not predict its size (why about four items, not one or forty). The GNW goes further. In network simulations (Dehaene, Sergent and Changeux, [A neuronal network model linking subjective reports and objective physiological data during conscious perception](https://scholar.google.com/scholar?q=A+neuronal+network+model+linking+subjective+reports+and+objective+physiological+data+during+conscious+perception+Dehaene+Sergent+Changeux+2003)), a reverberating coalition that has ignited suppresses competing coalitions through inhibition, so one content at a time falls out of the dynamics, and the model reproduces the attentional blink. But the inhibition was put into the model, so this explains the limit by a mechanism that was chosen to produce it.
2. **Seriality: follows from the bottleneck.** Given claim 4, one content after another is a consequence. It inherits the status of item 1.
3. **Why conscious contents are reportable and usable in reasoning.** Report, reasoning, planning and memory are all specialist consumers of the broadcast. Being in the workspace is being available to all of them, which is what Block's "poised for use" means.
4. **Why consciousness matters for novelty and learning.** Practised tasks can run inside one specialist or a fixed coalition. Novel tasks need specialists that do not normally talk to each other; the workspace is where they meet. This matches the automaticity findings of Section 2.
5. **Why so much is unconscious.** Most work is done locally and never needs to be broadcast.
6. **Why attention and consciousness are linked.** Attention is the mechanism of selection for the workspace. GNW's preconscious category also explains why attention and consciousness can come apart in one direction: a strong stimulus can be ready for access without being accessed.
7. **Testable neural predictions.** GNW makes predictions about timing (late), dynamics (nonlinear, bimodal), anatomy (frontoparietal involvement) and information (content decodable broadly on conscious trials). This made it the most productive theory in the experimental literature of the 2000s.

**Remark.** Items 3 and 5 are close to definitional: being in the workspace is being available for report and reasoning, and whatever is not broadcast is unconscious. The real explanatory content of GWT lies in items 4, 6 and 7: the link to novelty, the role of attention, and the neural predictions, which could have failed and have sometimes partly failed (Section 6.7).

**Remark.** For the talk, the logic runs in the opposite direction in a language model. Nobody built a capacity limit into a transformer. The residual stream is thousands of dimensions wide, and attention can read from the whole context. Gurnee et al. find empirically that the J-space holds only tens of concepts and a small fraction of activation variance (Section 8). If that holds up, the bottleneck is something that emerged in training rather than a design choice. This is a better test of the claim that a broadcast system needs a bottleneck than the brain can give, since in the brain capacity limits were part of the evidence the theory was built from.

---

## 5. Which problems it does not solve

**The hard problem.** Chalmers, [Facing up to the problem of consciousness](https://scholar.google.com/scholar?q=Facing+up+to+the+problem+of+consciousness+Chalmers+1995), separated the "easy problems" (explaining functions such as report, integration and control) from the hard problem (why any of this is accompanied by experience). GWT is, by design, an answer to easy problems. Dehaene's position is that once the easy problems are solved, nothing is left over; critics reply that the theory explains access and is silent on experience.

**Access vs. phenomenal consciousness.** Block, [On a confusion about a function of consciousness](https://scholar.google.com/scholar?q=On+a+confusion+about+a+function+of+consciousness+Block+1995), argued that the two concepts are distinct and that functional theories run them together. Block, [Consciousness, accessibility, and the mesh between psychology and neuroscience](https://scholar.google.com/scholar?q=Consciousness+accessibility+and+the+mesh+between+psychology+and+neuroscience+Block+2007), went further and argued for **overflow**: phenomenal consciousness has a larger capacity than access. His evidence is Sperling-style partial report: subjects shown a brief array of 12 letters can report only about 4, but can report any row that is cued after the array is gone, and they say they saw all of them. If experience outruns access, GWT, a theory of access, cannot be the whole theory of consciousness. Cohen and Dennett, [Consciousness cannot be separated from function](https://scholar.google.com/scholar?q=Consciousness+cannot+be+separated+from+function+Cohen+Dennett+2011), reply that a notion of experience with no functional consequences cannot be studied empirically at all. The debate is unresolved.

**The report confound.** Most evidence for GNW compares seen and unseen trials on which the subject reports. Late frontoparietal activity might then reflect the report, or the task, rather than consciousness itself. Aru, Bachmann, Singer and Melloni, [Distilling the neural correlates of consciousness](https://scholar.google.com/scholar?q=Distilling+the+neural+correlates+of+consciousness+Aru+Bachmann+Singer+Melloni+2012), make the general point. Tsuchiya, Wilke, Frässle and Lamme, [No-report paradigms: extracting the true neural correlates of consciousness](https://scholar.google.com/scholar?q=No-report+paradigms+extracting+the+true+neural+correlates+of+consciousness+Tsuchiya+2015), propose experiments without report. In one such experiment (Pitts, Metzler and Hillyard, [Isolating neural correlates of conscious perception from neural correlates of reporting one's perception](https://scholar.google.com/scholar?q=Isolating+neural+correlates+of+conscious+perception+from+neural+correlates+of+reporting+one%27s+perception+Pitts+2014)), the P3b disappeared when a consciously seen stimulus was irrelevant to the task. That is a problem for treating the P3b as a signature of access.

**The role of prefrontal cortex.** GNW gives prefrontal cortex a central role. Boly et al., [Are the neural correlates of consciousness in the front or in the back of the cerebral cortex? Clinical and neuroimaging evidence](https://scholar.google.com/scholar?q=Are+the+neural+correlates+of+consciousness+in+the+front+or+in+the+back+of+the+cerebral+cortex+Boly+2017), argue for a posterior "hot zone" instead. Odegaard, Knight and Lau, [Should a few null findings falsify prefrontal theories of conscious perception?](https://scholar.google.com/scholar?q=Should+a+few+null+findings+falsify+prefrontal+theories+of+conscious+perception+Odegaard+Knight+Lau+2017), argue the opposite in the same issue of the Journal of Neuroscience.

**Vagueness about "global".** How many processors must receive a broadcast, and how strongly, for a content to count as conscious? The cognitive version does not say. GNW answers in neural terms (ignition), but this makes the theory's application to non-brains uncertain: is it the function (availability to many consumers) or the mechanism (reverberant long-range recurrence) that matters? This question is central for AI (Section 7).

**Dependence on functionalism.** GWT assumes that consciousness is a matter of functional organisation. Theories that tie consciousness to physical causal structure (IIT) or biological substrate reject the premise, and GWT has no argument against them beyond the general case for functionalism. Gurnee et al. say explicitly that their results are "not relevant to assessing consciousness according to such theories".

**Phenomenal content.** Even granting that a content is conscious because it is broadcast, GWT does not explain why a red experience feels the way it does rather than some other way. The theory says which contents are conscious, not what their conscious character is.

---

## 6. Competitors

Seth and Bayne, [Theories of consciousness](https://scholar.google.com/scholar?q=Theories+of+consciousness+Seth+Bayne+2022+Nature+Reviews+Neuroscience), is the standard recent survey. They group theories into higher-order, global workspace, integrated information, re-entry and predictive processing families. The sections below follow roughly that grouping, adding attention schema theory because Gurnee et al. discuss it.

### 6.1 Higher-order theories

**Claim.** A mental state is conscious when the system has a suitable representation of being in that state. A first-order representation of red is unconscious on its own; it is conscious when accompanied by a higher-order representation that I am seeing red. Rosenthal's [Consciousness and Mind](https://scholar.google.com/scholar?q=Consciousness+and+Mind+Rosenthal+2005) is the classic philosophical version. Lau and Rosenthal, [Empirical support for higher-order theories of conscious awareness](https://scholar.google.com/scholar?q=Empirical+support+for+higher-order+theories+of+conscious+awareness+Lau+Rosenthal+2011), and Brown, Lau and LeDoux, [Understanding the higher-order approach to consciousness](https://scholar.google.com/scholar?q=Understanding+the+higher-order+approach+to+consciousness+Brown+Lau+LeDoux+2019), connect it to neuroscience. Lau's [In Consciousness We Trust](https://scholar.google.com/scholar?q=In+Consciousness+We+Trust+The+Cognitive+Neuroscience+of+Subjective+Experience+Lau+2022) develops perceptual reality monitoring: a higher-order mechanism tags first-order perceptual states as reliable reflections of the world, as opposed to noise or imagination.

**Contrast with GWT.** GWT locates the difference between conscious and unconscious in how a representation is used (broadcast); higher-order theories locate it in whether the representation is itself represented. Both give prefrontal cortex a role. Blindsight is the favourite case of higher-order theorists: first-order visual information guides behaviour, but there is no higher-order representation and so no awareness. GWT reads the same case as visual information that does not reach the workspace.

**Relevance.** Gurnee et al. observe the same structure as blindsight in the model: information that affects behaviour (for example, line length triggering a line break) without being represented in the J-space. They leave open whether J-space representations are higher-order or merely more accessible first-order representations.

### 6.2 Recurrent processing theory

**Claim.** Lamme, [Towards a true neural stance on consciousness](https://scholar.google.com/scholar?q=Towards+a+true+neural+stance+on+consciousness+Lamme+2006), building on Lamme and Roelfsema, [The distinct modes of vision offered by feedforward and recurrent processing](https://scholar.google.com/scholar?q=The+distinct+modes+of+vision+offered+by+feedforward+and+recurrent+processing+Lamme+Roelfsema+2000), distinguishes a fast feedforward sweep through the visual hierarchy, which is unconscious, from local recurrent processing within sensory cortex (feedback from higher to lower visual areas), which is sufficient for phenomenal consciousness. Global recurrent processing that reaches frontoparietal areas corresponds to access and report.

**Contrast with GWT.** Recurrent processing theory accepts something like the GNW as a theory of access but says that phenomenal consciousness arises earlier and more locally. It sides with Block on overflow and with Boly et al. on the posterior cortex.

**Relevance.** Transformers have no recurrence within a forward pass: each layer feeds only later layers. On recurrent processing theory, a single forward pass is all feedforward sweep. Gurnee et al. list recurrence among their acknowledged gaps, and two papers in this folder take it up: Wang and Reid, [Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?](https://scholar.google.com/scholar?q=Looped+Transformers+under+the+Jacobian+Lens+Does+the+Global+Workspace+Survive+Recurrence), and Titov, Ushakov and Berdinsky, [J-Space in Claude: Three Unanswered Questions and an Architectural Solution via Reentry](https://scholar.google.com/scholar?q=J-Space+in+Claude+Three+Unanswered+Questions+and+an+Architectural+Solution+via+Reentry).

### 6.3 Integrated information theory

**Claim.** Tononi's integrated information theory (IIT) starts from axioms about experience (it exists, is structured, specific, unified and definite) and derives requirements on its physical substrate. Consciousness is identified with maximally irreducible integrated cause-effect structure, measured by a quantity Φ. Key references: Tononi, [An information integration theory of consciousness](https://scholar.google.com/scholar?q=An+information+integration+theory+of+consciousness+Tononi+2004); Tononi, Boly, Massimini and Koch, [Integrated information theory: from consciousness to its physical substrate](https://scholar.google.com/scholar?q=Integrated+information+theory+from+consciousness+to+its+physical+substrate+Tononi+Boly+Massimini+Koch+2016).

**Contrast with GWT.** IIT is not a functional theory. Two systems that compute the same input-output function can differ in Φ, and a purely feedforward system has Φ = 0 whatever it computes. IIT therefore predicts that conscious machines would need specific hardware, not just specific software, and it makes the question of LLM consciousness one about chips rather than models. IIT places consciousness in posterior cortex and does not require report or broadcast.

**Controversy.** IIT is highly contested. In 2023 a group of researchers published an open letter calling it pseudoscience (Fleming et al., [The Integrated Information Theory of Consciousness as Pseudoscience](https://scholar.google.com/scholar?q=The+Integrated+Information+Theory+of+Consciousness+as+Pseudoscience+Fleming+2023)), which drew replies defending it as a scientific theory. The dispute is mostly about testability and about IIT's panpsychist consequences.

### 6.4 Attention schema theory

**Claim.** Graziano's attention schema theory (Graziano and Webb, [The attention schema theory: a mechanistic account of subjective awareness](https://scholar.google.com/scholar?q=The+attention+schema+theory+a+mechanistic+account+of+subjective+awareness+Graziano+Webb+2015); Graziano, [Consciousness and the Social Brain](https://scholar.google.com/scholar?q=Consciousness+and+the+Social+Brain+Graziano+2013)) says that the brain builds a simplified internal model of its own attention, for the same reason it builds a body schema: to control it. The model depicts attention as a kind of inner experience. When we report being conscious, we report the content of this model.

**Contrast with GWT.** The two are compatible: attention schema theory can be read as an account of why a workspace system would claim to have experiences. It explains the reports, not the access. Graziano describes it as a theory of why we believe we are conscious.

**Relevance.** Gurnee et al. find that during the model's narrations of its own experience, the J-space is dominated by tokens such as thinking, thoughts, feeling and conscious, and that ablating the J-space removes the experiential character of these reports. In directed-modulation experiments, tokens describing the mental operation (thinking, imagine, focused) appear at earlier layers than the content itself. They present these results as sitting "at the edge of what attention schema theory predicts".

### 6.5 Predictive processing and multiple drafts

**Predictive processing.** The brain as a prediction machine that minimises prediction error (Clark, [Whatever next? Predictive brains, situated agents, and the future of cognitive science](https://scholar.google.com/scholar?q=Whatever+next+Predictive+brains+situated+agents+and+the+future+of+cognitive+science+Clark+2013)). Applied to consciousness, perceptual experience is the brain's best prediction of the causes of its inputs (Seth, [Being You: A New Science of Consciousness](https://scholar.google.com/scholar?q=Being+You+A+New+Science+of+Consciousness+Seth+2021)). Predictive processing is a framework more than a rival theory of access; it can be combined with a workspace.

**Multiple drafts.** Dennett's [Consciousness Explained](https://scholar.google.com/scholar?q=Consciousness+Explained+Dennett+1991) attacks the "Cartesian theatre", the idea of a place in the brain where everything comes together for an inner observer. Parallel processes produce many "drafts" of content, none of which is the definitive conscious version. Baars's theatre metaphor looks like exactly what Dennett rejects, but Dennett later endorsed workspace theories as accounts of "fame in the brain" ([Sweet Dreams](https://scholar.google.com/scholar?q=Sweet+Dreams+Philosophical+Obstacles+to+a+Science+of+Consciousness+Dennett+2005)), on the condition that there is no audience over and above the specialist consumers themselves.

### 6.6 Comparison table

| | Global workspace | Higher-order | Recurrent processing | Integrated information | Attention schema |
| :--- | :--- | :--- | :--- | :--- | :--- |
| What makes a state conscious | broadcast to many consumers | being represented by a higher-order state | local recurrence in sensory cortex | maximal integrated cause-effect structure (Φ) | being represented in the model of attention |
| Theory of | access (claims to cover all) | awareness / subjective character | phenomenal (access = global recurrence) | phenomenal | reports of awareness |
| Functionalist? | yes | yes | mostly | no | yes |
| Brain locus | frontoparietal network | prefrontal | posterior sensory cortex | posterior "hot zone" | temporoparietal junction and attention networks |
| Report needed? | access implies reportability | no | no | no | reports are the explanandum |
| Signature | late, all-or-none ignition | metacognitive mismatch with first-order performance | feedback within sensory areas | sustained integration, perturbational complexity | self-model of attention |
| Feedforward network conscious? | unclear: depends on function vs. mechanism | possible in principle | no | no | possible in principle |

The last row is the one that matters for LLMs, and it is the place where GWT is least definite.

### 6.7 The adversarial collaboration

In an **adversarial collaboration**, proponents of rival theories agree in advance on experiments and on which outcomes would count against each theory. The Cogitate Consortium tested GNW against IIT with preregistered predictions, using fMRI, MEG and intracranial recordings (Cogitate Consortium et al., [Adversarial testing of global neuronal workspace and integrated information theories of consciousness](https://scholar.google.com/scholar?q=Adversarial+testing+of+global+neuronal+workspace+and+integrated+information+theories+of+consciousness+Cogitate+2025), Nature 2025). Neither theory came through cleanly. Against GNW: the predicted ignition at stimulus offset was largely absent, and prefrontal cortex carried information about the category of a stimulus but not all of the conscious content. Against IIT: the predicted sustained synchronisation within posterior cortex was not found. The result is widely read as a sign that the field's leading theories are underconstrained, and as a model for how to test theories of consciousness at all.

---

## 7. Global workspace theory and AI

GWT is the theory most often carried over to AI, for two reasons. It is functionalist, so it makes no reference to biology. And its architecture (specialists plus a shared medium plus broadcast) is easy to state in computational terms.

**Workspace as an architecture.** Bengio, [The consciousness prior](https://scholar.google.com/scholar?q=The+consciousness+prior+Bengio+2017), proposes that a low-dimensional "conscious state" selected by attention from a high-dimensional representation is a useful inductive bias. VanRullen and Kanai, [Deep learning and the global workspace theory](https://scholar.google.com/scholar?q=Deep+learning+and+the+global+workspace+theory+VanRullen+Kanai+2021), sketch a workspace built from pretrained modality-specific latent spaces linked through a shared latent space. Goyal et al., [Coordination among neural modules through a shared global workspace](https://scholar.google.com/scholar?q=Coordination+among+neural+modules+through+a+shared+global+workspace+Goyal+2022), replace pairwise attention between modules with a limited-capacity shared memory that modules compete to write to and that is broadcast to all. Juliani, Arulkumaran, Sasai and Kanai, [On the link between conscious function and general intelligence in humans and machines](https://scholar.google.com/scholar?q=On+the+link+between+conscious+function+and+general+intelligence+in+humans+and+machines+Juliani+2022), relate workspace functions to general intelligence.

**Workspace as an indicator.** Butlin, Long et al., [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness](https://scholar.google.com/scholar?q=Consciousness+in+Artificial+Intelligence+Insights+from+the+Science+of+Consciousness+Butlin+Long+2023), derive "indicator properties" from several theories, on the assumption of computational functionalism. A system that has more of them is more likely to be conscious. The four GWT indicators are:

- GWT-1: multiple specialised systems capable of operating in parallel (modules).
- GWT-2: a limited-capacity workspace, entailing a bottleneck in information flow and a selective attention mechanism.
- GWT-3: global broadcast: availability of information in the workspace to all modules.
- GWT-4: state-dependent attention, giving rise to the capacity to use the workspace to query modules in succession to perform complex tasks.

The report concluded that no then-current AI system was a strong candidate, but that there were no obvious technical barriers to building systems that satisfy the indicators.

**Do LLMs have a workspace?** Chalmers, [Could a Large Language Model be Conscious?](https://scholar.google.com/scholar?q=Could+a+Large+Language+Model+be+Conscious+Chalmers+2023), lists the lack of a global workspace, together with the lack of recurrent processing and unified agency, among the main obstacles to LLM consciousness, while noting that the residual stream might be read as a candidate. Goldstein and Kirk-Giannini, [A Case for AI Consciousness: Language Agents and Global Workspace Theory](https://scholar.google.com/scholar?q=A+Case+for+AI+Consciousness+Language+Agents+and+Global+Workspace+Theory+Goldstein+Kirk-Giannini+2024), argue that language agents (LLMs wrapped in architectures with memory, planning and tool modules) come close to satisfying GWT, if GWT is correct. Both arguments work at the level of architecture diagrams. Neither looks inside a trained model to ask whether something workspace-like has emerged in its internal representations.

**Remark.** That is the gap Gurnee et al. fill. Their question is not "does the transformer's architecture match GWT's diagram?" but "does a trained model contain a subset of its representations that behaves, functionally and structurally, the way GWT says conscious contents behave?"

---

## 8. How Gurnee et al. use the theory

This section maps the paper onto the reader. Details go in the main background reader for the talk.

**What they take from GWT.** Five functional properties commonly held to distinguish consciously accessible information: it is reportable, subject to top-down control, the medium of deliberate reasoning, flexibly generalisable, and selective. These are the claims of Sections 1 and 4. The Jacobian lens is used to identify the representations a model is "poised to verbalize"; the J-space is the subspace those representations span. The paper then tests whether the J-space has each property.

**Structural signatures.** They document three properties GWT associates with a workspace:

1. **Intermediate layers.** J-space content has workspace-like properties only in a band of middle layers, between an early regime where it is empty and a late regime where it is aligned with the imminent output.
2. **Limited capacity.** It holds on the order of tens of concepts at a time, accounts for a small fraction of activation variance, and excludes most of the model's representational features.
3. **Broadcast.** J-lens vectors compose with the input weights of downstream attention and MLP components far more broadly than other directions in the residual stream do.

They also test ignition (Section 3.4) by giving the model an input embedding that is a weighted mixture of two concepts and measuring how its commitment to one reading evolves over layers.

**What they do not claim.** In their words, they "do not claim that language models reproduce the full architecture global workspace theory ascribes to the brain". The gaps they list:

- no clearly separable, encapsulated input processors (GWT-1 is not demonstrated);
- broadcast happens over the model's depth within a single forward pass, not through recurrent loops;
- some competition for access, but it is unclear whether it is the sharp ignition seen in brains.

Their summary: the J-space "achieves many of the functional properties of the global workspace in the brain, while sharing only some of its architectural properties." This is the function-vs-mechanism question of Section 5, answered in favour of function.

**Consciousness.** They adopt the access/phenomenal distinction of Section 1 and "take no position" on phenomenal consciousness. They note that their results bear only on functionalist theories, not on IIT or substrate-based views.

**Other theories.** The discussion relates the results to Butlin et al.'s indicator framework (the J-space as "a concrete, inspectable candidate structure against which several of these indicators can be checked directly"), to higher-order theories (blindsight-like dissociations; J-space tokens such as fake, dangerous, imagined and hidden that may tag other representations), and to attention schema theory (self-descriptive and metacognitive tokens in the J-space). They also suggest the influence may run the other way: a working system with some properties of conscious access, built from different mechanisms, may change the theories themselves.

**Questions for the talk.**

- Is depth a substitute for recurrence? GWT in its neural form says broadcast is reverberation; a transformer's broadcast is one-way. Chain-of-thought, where the model reads its own output, is the closest thing a transformer has to a loop.
- Which property carries the weight: verbalisability or broadcast? GWT defines the workspace by broadcast and treats reportability as a consequence. The paper finds the J-space by verbalisability and then shows it is broadcast. Those are different directions of argument.
- Does the J-space answer Chalmers's objection that LLMs lack a global workspace, or does it only show that a workspace-like structure exists without the modules GWT says it serves?
- What would ignition look like in a feedforward network, and is a sharp change over a narrow band of layers the right analogue of a late, all-or-none transition in time?

---

## 9. Reading list

A short path through the literature, in reading order.

1. Baars, [Global workspace theory of consciousness: toward a cognitive neuroscience of human experience](https://scholar.google.com/scholar?q=Global+workspace+theory+of+consciousness+toward+a+cognitive+neuroscience+of+human+experience+Baars+2005): the theory by its author, in one paper.
2. Dehaene and Changeux, [Experimental and theoretical approaches to conscious processing](https://scholar.google.com/scholar?q=Experimental+and+theoretical+approaches+to+conscious+processing+Dehaene+Changeux+2011): the neural version and the evidence for ignition.
3. Block, [On a confusion about a function of consciousness](https://scholar.google.com/scholar?q=On+a+confusion+about+a+function+of+consciousness+Block+1995): access vs. phenomenal consciousness.
4. Seth and Bayne, [Theories of consciousness](https://scholar.google.com/scholar?q=Theories+of+consciousness+Seth+Bayne+2022+Nature+Reviews+Neuroscience): the competitors side by side.
5. Cogitate Consortium et al., [Adversarial testing of global neuronal workspace and integrated information theories of consciousness](https://scholar.google.com/scholar?q=Adversarial+testing+of+global+neuronal+workspace+and+integrated+information+theories+of+consciousness+Cogitate+2025): how GNW fared in a preregistered test.
6. Butlin, Long et al., [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness](https://scholar.google.com/scholar?q=Consciousness+in+Artificial+Intelligence+Insights+from+the+Science+of+Consciousness+Butlin+Long+2023): GWT as indicator properties for AI.
7. Chalmers, [Could a Large Language Model be Conscious?](https://scholar.google.com/scholar?q=Could+a+Large+Language+Model+be+Conscious+Chalmers+2023): the objection Gurnee et al. can be read as answering.
8. Gurnee et al., [Verbalizable Representations Form a Global Workspace in Language Models](https://scholar.google.com/scholar?q=Verbalizable+Representations+Form+a+Global+Workspace+in+Language+Models+Gurnee+2026): the paper.
