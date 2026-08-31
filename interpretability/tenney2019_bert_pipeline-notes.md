# BERT Rediscovers the Classical NLP Pipeline

**Authors:** Ian Tenney, Dipanjan Das, Ellie Pavlick  
**Year:** 2019  
**Venue:** ACL 2019  
**Citation key:** `tenney2019_bert_pipeline`  
**BibTeX entry:** [entry](../../bib.bib)  
**PDF:** [ACL Anthology](https://aclanthology.org/P19-1452.pdf)  
**Google Scholar:** [Search](https://scholar.google.com/scholar?q=Tenney+BERT+Rediscovers+Classical+NLP+Pipeline+2019)

## Summary

Uses **probing classifiers** on BERT layer representations to show that linguistic tasks (POS, parsing, NER, etc.) emerge in a **layered pipeline** reminiscent of classical NLP stacks — shallow syntax early, semantics later.

## Key concepts

- **Probing** — train a small classifier on frozen hidden states to test what information is linearly decodable.  
- **Layer-wise specialization** — different layers encode different linguistic levels.  
- **Pipeline hypothesis** — depth mirrors processing stages.

## Notes

- Canonical entry point for the probing literature in the activation-steering reader.  
- HeRA reader: [`hera/readers/04-activation-steering.md`](https://github.com/alexhkurz/hera/blob/main/readers/04-activation-steering.md).
