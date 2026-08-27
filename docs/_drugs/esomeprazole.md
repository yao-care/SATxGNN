---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Esomeprazole: From Acid-Related Disorders (GERD) to Duodenal Ulcer

## One-Sentence Summary

> Esomeprazole (DrugBank DB00736) is the S-isomer proton pump inhibitor originally developed for gastro-oesophageal reflux disease (GERD) and other acid-related conditions.
> Within this evidence pack, the TxGNN model surfaces three candidate indications; the one with genuine actionable evidence is **Duodenal Ulcer**,
> supported by **50 registered clinical trials** (multiple completed Phase 3 RCTs) and **20 relevant publications**.
> The other two predicted indications (duodenogastric reflux, duodenal obstruction) carry only weak or no supporting evidence and are flagged separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastro-oesophageal reflux disease (GERD) / acid-related disorders¹ |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

¹ *Note: `taiwan_regulatory.licenses` and `drug.original_indications` are both empty in this pack (no formal license record exists because esomeprazole is not currently marketed in Saudi Arabia). The original indication above is inferred from supporting literature in this same evidence pack (e.g., PMID 18627213), not from a license record.*

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data (`original_moa`) is flagged as a data gap (DG002) in this pack. However, the evidence pack's own repurposing rationale supplies a clear mechanistic explanation: **Esomeprazole is a proton pump inhibitor (PPI) that directly inhibits the H⁺/K⁺-ATPase enzyme on gastric parietal cells, reducing gastric acid secretion.** This is the standard, first-line mechanism for treating acid-related mucosal disease.

Duodenal ulcer is itself an acid-related, often *H. pylori*-associated condition whose healing and recurrence prevention depend heavily on acid suppression. The mechanistic link here is **direct and strong** — unlike the other two candidates in this pack, this is not a speculative cross-disease inference from the knowledge graph, but a pharmacologically expected use of the PPI class. In fact, the evidence pack's own rationale notes that this may represent an "already-known but not formally registered" indication rather than a true novel repurposing hypothesis — consistent with the fact that esomeprazole (as Nexium®) is approved in other markets for duodenal ulcer healing, *H. pylori* eradication regimens, and NSAID-associated ulcer prevention, but has no current license record in Saudi Arabia.

By contrast, the mechanistic case for the other two predicted indications is weak: duodenogastric reflux involves bile/pancreatic reflux pathology that PPIs do not directly address (indirect/adjunctive at best), and duodenal obstruction is a mechanical/structural condition with no plausible pharmacological pathway for acid suppression to resolve. Both are discussed further under "Other Predicted Indications" below.

---

## Clinical Trial Evidence

*(Duodenal Ulcer — top 10 trials by assigned relevance grade)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03553563](https://clinicaltrials.gov/study/NCT03553563) | Phase 3 | Completed | 50 | Maintenance therapy in Japanese paediatric patients with reflux esophagitis; prevention of gastric/duodenal ulcer recurrence with NSAIDs or low-dose aspirin |
| [NCT00542789](https://clinicaltrials.gov/study/NCT00542789) | Phase 3 | Completed | 343 | Esomeprazole 20 mg qd vs placebo for prevention of gastric and/or duodenal ulcers in daily NSAID users |
| [NCT00595517](https://clinicaltrials.gov/study/NCT00595517) | Phase 3 | Completed | 395 | Long-term (52-week) safety/efficacy of esomeprazole 20 mg qd for prevention of NSAID-associated gastric/duodenal ulcers |
| [NCT00251966](https://clinicaltrials.gov/study/NCT00251966) | Phase 3 | Completed | 960 | Large RCT: esomeprazole 20 mg qd vs placebo for prevention of low-dose aspirin-associated gastroduodenal lesions |
| [NCT05813561](https://clinicaltrials.gov/study/NCT05813561) | Phase 3 | Completed | 332 | Head-to-head comparator trial: DWP14012 vs esomeprazole magnesium enteric-coated tablets for reflux esophagitis |
| [NCT01538849](https://clinicaltrials.gov/study/NCT01538849) | Phase 2 | Completed | 154 | Randomized double-blind active-controlled trial establishing optimal dose/administration referencing esomeprazole |
| [NCT01142245](https://clinicaltrials.gov/study/NCT01142245) | Phase 3 | Completed | 263 | IV + oral esomeprazole for prevention of recurrent bleeding after endoscopic therapy for peptic ulcers |
| [NCT01199328](https://clinicaltrials.gov/study/NCT01199328) | Phase 1 | Completed | 34 | Drug-drug interaction study: effect of esomeprazole on aspirin pharmacodynamics |
| [NCT00325715](https://clinicaltrials.gov/study/NCT00325715) | Phase 1 | Completed | 150 | AGN201904 vs esomeprazole for prevention of aspirin-induced upper GI damage in healthy volunteers |
| [NCT00594854](https://clinicaltrials.gov/study/NCT00594854) | Phase 3 | Terminated | 20 | PN400 (esomeprazole/naproxen) vs diclofenac/misoprostol for gastric ulcer incidence — terminated early, small sample |

*(40 additional trials in this indication are registered but not yet graded for relevance; see raw evidence pack for the complete list.)*

---

## Literature Evidence

*(Duodenal Ulcer — prioritized by RCT/meta-analysis > cohort > review)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11121908](https://pubmed.ncbi.nlm.nih.gov/11121908/) | 2000 | RCT | Alimentary Pharmacology & Therapeutics | One-week esomeprazole-based triple therapy effectively eradicates *H. pylori* in duodenal ulcer disease |
| [11742194](https://pubmed.ncbi.nlm.nih.gov/11742194/) | 2001 | RCT | European Journal of Gastroenterology & Hepatology | One week of esomeprazole-based triple therapy eradicates *H. pylori* and heals duodenal ulcer |
| [21181319](https://pubmed.ncbi.nlm.nih.gov/21181319/) | 2011 | RCT | Advances in Therapy | Safety and tolerability of high-dose IV esomeprazole for prevention of peptic ulcer rebleeding |
| [18350637](https://pubmed.ncbi.nlm.nih.gov/18350637/) | 2008 | RCT | World Journal of Gastroenterology | Randomized double-blind comparison of esomeprazole formulations in healing active duodenal ulcer |
| [39412166](https://pubmed.ncbi.nlm.nih.gov/39412166/) | 2024 | Network Meta-Analysis | Clinical and Translational Gastroenterology | Compares dosing of potassium-competitive acid blockers vs PPIs (incl. esomeprazole) across acid-related disorders |
| [16109574](https://pubmed.ncbi.nlm.nih.gov/16109574/) | 2005 | RCT/Comparative | Academic Journal of the First Medical College of PLA | Compares esomeprazole- vs omeprazole-based triple therapy for *H. pylori*-associated duodenal ulcer |
| [39319279](https://pubmed.ncbi.nlm.nih.gov/39319279/) | 2024 | Cohort (long-term paediatric) | Pediatric Gastroenterology, Hepatology & Nutrition | Long-term esomeprazole use in Japanese paediatric patients with chronic gastric acid-related disease |
| [40168383](https://pubmed.ncbi.nlm.nih.gov/40168383/) | 2025 | Cohort/Trial | Journal of Infection in Developing Countries | High-dose dual therapy (esomeprazole + amoxicillin) for *H. pylori* in a high-resistance region |
| [10983736](https://pubmed.ncbi.nlm.nih.gov/10983736/) | 2000 | Review | Drugs | Overview of esomeprazole's superior intragastric pH control vs omeprazole/lansoprazole/pantoprazole |
| [12072608](https://pubmed.ncbi.nlm.nih.gov/12072608/) | 2002 | Review/Commentary | European Journal of Gastroenterology & Hepatology | Commentary on esomeprazole-based triple therapy for duodenal ulcer and *H. pylori* |

*(An additional 10 publications are registered but not yet classified for study type/tier; see raw evidence pack.)*

---

## Saudi Arabia Market Information

Esomeprazole currently has **no marketing authorization on record in Saudi Arabia** (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No authorization table can be produced.

---

## Other Predicted Indications (Lower Priority — Not Recommended to Advance)

For completeness, this evidence pack also scored two additional indications for esomeprazole, both substantially weaker than duodenal ulcer:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Duodenogastric reflux | 99.53% | L4 | Research Question | Only 1 review-level publication, no clinical trials; mechanistic link is indirect (PPI does not act on bile reflux or duodenogastric motility) |
| Duodenal obstruction | 99.45% | L5 | **Hold** | No clinical trials or literature; duodenal obstruction is a mechanical/structural condition with no pharmacological pathway for acid suppression — likely a knowledge-graph embedding artifact ("duodenal" term proximity), not a real signal |

These two indications should **not** be advanced for further evaluation absent new evidence.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this pack — see DG001, a **Blocking** severity gap requiring TFDA/regulatory package insert retrieval before any S1 safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- For **duodenal ulcer**, evidence is strong (L1: multiple completed Phase 3 RCTs plus supportive literature including RCTs and a network meta-analysis), and the mechanism of action is direct and well established for the PPI class — this is effectively confirming an already-plausible use rather than a speculative repurposing hypothesis.
- However, the drug has **zero market authorizations in Saudi Arabia** and a **Blocking** safety data gap (no TFDA package insert warnings/contraindications available), so this cannot move past initial safety screening (S1) until that gap is closed.
- The other two predicted indications (duodenogastric reflux, duodenal obstruction) lack sufficient evidence and should be put on **Hold** / treated as low-priority research questions only.

**To proceed, the following is needed:**
- Retrieve and parse the official package insert (warnings, precautions, contraindications) — currently Blocking (DG001)
- Obtain detailed mechanism-of-action documentation from DrugBank to close the High-severity MOA gap (DG002)
- Run a formal drug-drug interaction (DDI) query (current query status: not found)
- Confirm regulatory pathway for market entry in Saudi Arabia given zero existing authorizations
- Do not allocate further resources to duodenogastric reflux or duodenal obstruction without new supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

