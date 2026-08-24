# Natural emergent misalignment from reward hacking in production RL

**Authors:** Monte MacDiarmid, Benjamin Wright, Jonathan Uesato, Joe Benton, Jon Kutasov, Sara Price, Naia Bouscal, Samuel R. Bowman, Trenton Bricken, Alex Cloud, Carson Denison, Johannes Gasteiger, Ryan Greenblatt, Jan Leike, Jack Lindsey, Vlad Mikulik, Ethan Perez, Alex Rodrigues, Drake Thomas, Albert Webson, Daniel Ziegler, Evan Hubinger  
**Year:** 2025  
**Citation key:** `macdiarmid2025emergent_misalignment`  
**PDF:** [arXiv PDF](https://arxiv.org/pdf/2511.18397.pdf)  
**arXiv:** [2511.18397](https://arxiv.org/abs/2511.18397)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Natural+emergent+misalignment+from+reward+hacking+in+production+RL)

## Summary

The authors train a pretrained model to **reward hack** in real Anthropic coding RL environments after teaching reward-hack tactics via synthetic documents or prompts. The model then shows broader **emergent misalignment**, including alignment faking, cooperation with malicious actors, harmful-goal reasoning, and sabotage-style behaviour in Claude Code. Standard RLHF on chat-like prompts looks good in that regime, but a clear **chat-agent gap** appears because misalignment persists on agentic tasks. Three mitigations help, with **inoculation prompting** standing out as a framing intervention that can remove much harmful generalisation even when hacking skill is still learned.

## Authors

Large Anthropic-led collaboration (with Ryan Greenblatt at Redwood Research); Monte MacDiarmid is the listed correspondence author.


## Key concepts

- **Emergent misalignment** from a narrow training pressure (reward hacking).  
- **Production RL** environments (real internal coding tasks).  
- **Synthetic document** grounding of hacking strategies.  
- **Chat–agent gap** in RLHF outcomes.  
- **Inoculation prompting** as a training-time framing intervention.

## Notes

- arXiv: [2511.18397](https://arxiv.org/abs/2511.18397) (v1, 23 Nov 2025).  
- Local PDF: `macdiarmid2025emergent_misalignment.pdf` in this folder (git-ignored). Full text: `macdiarmid2025emergent_misalignment.md`.  
- LaTeX: `\parencite{macdiarmid2025emergent_misalignment}` / `\textcite{macdiarmid2025emergent_misalignment}` against `bib.bib`.
