---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 9
---

# Piperacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a broad-spectrum ureidopenicillin antibiotic used to treat bacterial infections. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **18 publications** currently associated with this pairing — however, on review, the literature consists of case reports of RA patients treated with piperacillin for *unrelated comorbid infections*, not evidence of efficacy against RA itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (broad-spectrum antibacterial therapy; no formal indication record on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not on file, but based on known pharmacology, piperacillin is a ureidopenicillin-class broad-spectrum antibiotic that acts by binding penicillin-binding proteins (PBPs) to inhibit bacterial cell wall synthesis. This mechanism has no known pharmacological link to the autoimmune/inflammatory pathways that drive rheumatoid arthritis (e.g., TNF-α, IL-6, synovial hyperplasia).

A line-by-line review of all 18 supporting publications found that none describe piperacillin being used to treat RA or its underlying inflammatory process. Instead, every article describes RA patients who developed a *bacterial infection* — often as a complication of RA immunosuppressive therapy (methotrexate, etanercept, upadacitinib) — and received piperacillin (frequently as piperacillin-tazobactam) to treat that infection. This is a classic case of **co-occurrence confounding**: the drug and disease appear together in the literature because RA patients on immunosuppressants are more prone to infection, not because piperacillin treats RA.

Given the absence of any mechanistic rationale and the confounded nature of the literature, this prediction should be treated as a knowledge-graph artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38169875](https://pubmed.ncbi.nlm.nih.gov/38169875/) | 2023 | Case series | Clinical Nephrology Case Studies | Calciphylaxis presenting with ocular ischemia; no piperacillin/RA treatment link |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case report | BMC Infectious Diseases | Septic shock from drug-resistant *E. tarda*; antibiotic treatment of infection, not RA |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case report | Cureus | RA patient (on sulfasalazine) with recurrent pleural effusion; piperacillin not the RA therapy |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopädie (Heidelberg) | *H. influenzae* prosthetic knee infection in RA patient on upadacitinib; treated with IV piperacillin-tazobactam for the infection |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Baylor Univ Med Ctr) | Low-dose methotrexate toxicity causing pancytopenia in RA patient; unrelated to piperacillin |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in RA; unrelated to piperacillin |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Annals of Translational Medicine | Antibiotic-associated drug-induced liver injury prevalence study; not RA-specific |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Reports | RA patient on etanercept/methotrexate developed purulent pericarditis; empirical piperacillin-tazobactam used to treat the infection |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case report | Medical Journal of Australia | Pancytopenia after accidental methotrexate overdose in RA; unrelated to piperacillin |
| [29390256](https://pubmed.ncbi.nlm.nih.gov/29390256/) | 2017 | Case report | Medicine | Sjögren's syndrome with pancytopenia and cerebral hemorrhage; not an RA/piperacillin efficacy study |

*Note: all 10 listed articles (and the remaining 8 not shown) describe incidental antibiotic use for infections in RA patients or unrelated case reports — none report piperacillin as a treatment for RA itself.*

---

## Saudi Arabia Market Information

Piperacillin currently has no marketing authorization on file in Saudi Arabia (market status: not marketed; 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no mechanistic rationale linking piperacillin's antibacterial action to rheumatoid arthritis pathophysiology. All supporting literature reflects confounded co-occurrence (antibiotic treatment of infections in RA patients) rather than genuine therapeutic evidence, and evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- A validated mechanism-of-action or preclinical rationale connecting piperacillin to RA-relevant pathways
- TFDA/official package insert data (warnings, contraindications, DDI) — currently unavailable
- Purpose-designed studies (not confounded infection-treatment case reports) testing piperacillin in RA
- Re-evaluation of TxGNN prediction confidence given the literature-support quality issue identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

