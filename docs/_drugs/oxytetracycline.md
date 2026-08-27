---
layout: default
title: Oxytetracycline
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Oxytetracycline: From Bacterial Infections to Otitis Externa

> **Note on indication selection:** This evidence pack contains 10 TxGNN-predicted indications for oxytetracycline. The top-ranked candidate by TxGNN score alone (chronic rhinosinusitis, score 99.61%) has **zero** supporting trials or literature (Evidence Level L5, Hold). This report instead features **otitis externa** (rank 10, score 99.27%), the only candidate that reached decision stage S3 with actual clinical literature. The other 9 low-evidence candidates are summarized in the appendix at the end of this report.

## One-Sentence Summary

Oxytetracycline is a broad-spectrum tetracycline-class antibiotic historically used to treat bacterial infections. The TxGNN model predicts it may be effective for **otitis externa (external ear infection)**, a use consistent with its long-standing off-label/historical topical application (often combined with hydrocortisone and polymyxin B, e.g. Terra-Cortril). No dedicated repurposing clinical trials exist, but **20 publications**, including multiple randomized comparative studies, support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no DrugBank/regulatory indication text retrieved); by established pharmacological class, oxytetracycline is a broad-spectrum tetracycline antibacterial |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this pack). Based on known pharmacology, oxytetracycline is part of the tetracycline class of antibiotics, which act by inhibiting bacterial protein synthesis via binding to the 30S ribosomal subunit, giving broad-spectrum bacteriostatic activity against common Gram-positive and Gram-negative pathogens.

Otitis externa is most commonly caused by *Staphylococcus aureus* and *Pseudomonas aeruginosa*, both susceptible to topical tetracyclines. This is not a novel biological hypothesis — topical oxytetracycline (often combined with hydrocortisone ± polymyxin B, marketed historically as Terra-Cortril) has been used clinically for external ear infections since the 1950s. The TxGNN prediction therefore recovers a pharmacologically well-established use rather than an untested mechanistic leap, which is consistent with its comparatively strong literature support relative to the other 9 candidates in this pack (all Evidence Level L5, mechanism-only reasoning with no clinical data).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/) | 1985 | RCT | Archives of Oto-Rhino-Laryngology | 55 patients with acute external otitis randomized to framycetin/gramicidin vs. oxytetracycline/hydrocortisone/polymyxin B; 78% cured overall, no significant difference between regimens |
| [1782715](https://pubmed.ncbi.nlm.nih.gov/1782715/) | 1991 | RCT | Clinical Otolaryngology | 10 patients with bilateral otitis externa compared dressing vs. sump-filling administration of the same topical antibiotic/steroid preparation; 9/10 ears improved in each group |
| [2156538](https://pubmed.ncbi.nlm.nih.gov/2156538/) | 1990 | RCT (single-blind) | European Archives of Oto-Rhino-Laryngology | 46 patients with acute external otitis randomized to oxytetracycline/hydrocortisone/polymyxin B vs. hydrocortisone-17-butyrate; overall cure rate 80%, no significant difference |
| [8222746](https://pubmed.ncbi.nlm.nih.gov/8222746/) | 1993 | Cohort (comparative) | Current Medical Research and Opinion | 30 patients randomized to ciprofloxacin drops vs. oxytetracycline/polymyxin B/hydrocortisone; clinical and bacteriological outcomes compared over 8 days |
| [12564664](https://pubmed.ncbi.nlm.nih.gov/12564664/) | 2002 | Cohort (comparative) | Current Medical Research and Opinion | Compared otic powder vs. Dex-Otic drops (antibacterial/anti-inflammatory formulations) for otitis externa treatment |
| [15823803](https://pubmed.ncbi.nlm.nih.gov/15823803/) | 2005 | Animal study | Acta Oto-Laryngologica | Rat model of external otitis (*P. aeruginosa*/*C. albicans*) cured by topical group III steroid alone; questions the added value of the antibiotic component |
| [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/) | 2005 | RCT | The Journal of Laryngology and Otology | 51 patients, open randomized multicentre trial comparing betamethasone alone vs. hydrocortisone/oxytetracycline/polymyxin B; explores whether the antibiotic component is necessary |
| [11583468](https://pubmed.ncbi.nlm.nih.gov/11583468/) | 2001 | Animal study | European Archives of Oto-Rhino-Laryngology | Rat external otitis model comparing steroid alone vs. hydrocortisone+oxytetracycline (± polymyxin B) vs. saline control |
| [14412537](https://pubmed.ncbi.nlm.nih.gov/14412537/) | 1959 | Case series | Monatsschrift für Ohrenheilkunde | Early clinical report on treatment of otitis externa with oxytetracycline and hydrocortisone |
| [13447965](https://pubmed.ncbi.nlm.nih.gov/13447965/) | 1957 | Case series | Eye, Ear, Nose & Throat Monthly | Historical case series on treatment of otitis externa with Terra-Cortril (oxytetracycline/hydrocortisone) suspension |

## Saudi Arabia Market Information

Currently no marketed products in Saudi Arabia (0 authorizations recorded; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple older randomized and comparative studies (1985–2005) support topical oxytetracycline/hydrocortisone±polymyxin B as an effective treatment for otitis externa, and this mirrors decades of real-world off-label/historical use (e.g., Terra-Cortril). However, no trial was designed as a formal TxGNN-repurposing validation, several studies are small or dated, and two more recent studies (PMID 15823803, 15949095) suggest steroid alone may be sufficient without the antibiotic component — evidence is directionally supportive but not conclusive.

**To proceed, the following is needed:**
- TFDA/Saudi regulatory package insert data (currently a Blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action documentation from DrugBank
- A formal DDI and contraindication review (current query returned no data)
- Since the drug is not currently marketed in Saudi Arabia, a registration/import feasibility assessment would be needed before this indication could be operationalized

---

### Appendix: Other Predicted Indications (Low Evidence, Not Actionable)

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|-----------------|----------|
| 1 | Chronic rhinosinusitis | 99.61% | L5 | Hold |
| 2 | Chronic ethmoidal sinusitis | 99.61% | L5 | Hold |
| 3 | Paranasal sinus neoplasm | 99.58% | L5 | Hold |
| 4 | Punctate epithelial keratoconjunctivitis | 99.52% | L5 | Hold |
| 5 | Postinfectious vasculitis | 99.37% | L5 | Hold |
| 6 | Post-bacterial disorder | 99.35% | L3 | Research Question (1 terminated, underpowered osteomyelitis trial, n=11) |
| 7 | Post-infectious syndrome | 99.33% | L5 | Hold |
| 8 | Infective urethral stricture | 99.28% | L5 | Hold |
| 9 | Chagas cardiomyopathy | 99.27% | L5 | Hold (mechanistically implausible — antiparasitic activity not established) |

These candidates have no clinical trial or literature support beyond mechanistic reasoning and are not recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

