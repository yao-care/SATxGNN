---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor originally developed for ALK-positive non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **Gingival Fibromatosis** (fibromatosis, gingival), but currently **0 clinical trials** and **0 publications** support this specific link — the model's own rationale states no known pathological relationship exists between ALK/ROS1 inhibition and this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive Non-Small Cell Lung Cancer (NSCLC) — not locally registered; local (SFDA) indication text unavailable since the drug is not marketed in Saudi Arabia |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap). Based on the literature retained in this evidence pack, lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor (TKI), and its efficacy in ALK-positive NSCLC is well established (see the CROWN trial data cited under other candidate indications in this pack).

However, for the top-ranked prediction — gingival fibromatosis — the evidence pack's own mechanistic assessment is explicit: **"No clinical or mechanistic evidence; no trials, no literature; ALK/ROS1 inhibition has no known pathological association with gingival fibromatosis."** No PubMed or clinical trial hits were returned for this drug-disease pair (query log IDs 5–7, all zero results). This means the prediction rests entirely on the TxGNN network embedding score, with no biological rationale currently identified. It should be treated as a low-confidence, model-only hypothesis rather than a mechanistically supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Lorlatinib is not currently marketed in Saudi Arabia (0 authorizations on record); no license data is available.

---

## Cytotoxicity

Lorlatinib is an antineoplastic agent (ALK/ROS1-targeted therapy used in NSCLC), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no myelosuppression data in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Lipid panel (cholesterol, triglycerides) and weight — literature elsewhere in this pack (PMID 40287137, 40157899, 39537504, 33789526) documents lorlatinib-associated hyperlipidemia/metabolic syndrome; CNS/neurocognitive assessment and pulmonary symptoms are also reported adverse effects (PMID 31985497 ARDS case, PMID 38554546 AE management review) |
| Handling Protection | Not specified in this evidence pack; refer to institutional hazardous-drug handling policy and the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack, and the DDI database query returned "not found").

*Supplementary note:* literature attached to other, unrelated candidate indications in this same pack (not part of the formal safety dataset) documents real-world lorlatinib adverse-event signals, including ARDS (PMID 31985497), hyperlipidemia/metabolic syndrome (PMID 40287137, 40157899, 39537504, 33789526), and paraneoplastic leukemoid reaction (PMID 38344203). These are worth flagging to a reviewer even though they fall outside the formal `safety` fields.

---

## Additional Notes: Other Predicted Indications in This Evidence Pack

This candidate record (`TW-DB12130-multi`) scored 10 indications. Only the top-ranked one is used for the formal report above per the standard template, but the full set is summarized here because several entries reveal a **disease-ontology labeling problem** that materially affects interpretation:

| Rank | Predicted Disease | Score | Evidence Level | Recommendation | Note |
|------|-------------------|-------|-----------------|-----------------|------|
| 1 | Fibromatosis, gingival | 99.81% | L5 | Hold | No evidence; no known mechanistic link |
| 2 | Fibroma of lung | 99.75% | L5 | Hold | No evidence |
| 3 | Hamartoma of lung | 99.75% | L5 | Hold | No evidence; benign, non-ALK-driven |
| 4 | Lung hilum carcinoma | 99.74% | L4 | Hold | Only 1 case report; anatomical subtype, not a distinct disease entity |
| 5 | Lung benign neoplasm | 99.74% | **L1** | Proceed with Guardrails | **Mislabeled** — all 20 cited papers (incl. CROWN phase 3 RCT) are about ALK-positive *malignant* NSCLC, an already-approved indication, not a benign neoplasm |
| 6 | Pulmonary sulcus neoplasm | 99.73% | L5 | Hold | No evidence |
| 7 | Lung germ cell tumor | 99.73% | L2 | Hold | **Mislabeled** — all 15 papers concern ALK-driven neuroblastoma, not germ cell tumors |
| 8 | IBMPFD/FTD spectrum disease | 99.72% | L5 | Hold | **Mislabeled** — 20 papers are generic FTD reviews with no lorlatinib/ALK connection |
| 9 | Junctional epidermolysis bullosa | 99.72% | L5 | Hold | No evidence |
| 10 | Leukomelanoderma... syndrome | 99.69% | L4 | Hold | **Mislabeled** — 8 papers are lorlatinib adverse-event case reports, unrelated to this syndrome |

**Key finding:** across ranks 4, 5, 7, 8, and 10, the literature returned by the pipeline does not match the assigned disease label — the underlying documents are real and relevant to lorlatinib, but tagged to the wrong disease entity. This suggests a disease-name mapping/ontology issue upstream of this evidence pack, and should be corrected before any of these candidates (especially rank 5, which otherwise looks like strong L1 evidence) are reassessed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (gingival fibromatosis) has no clinical trials, no literature, and an explicit statement in the evidence pack that no mechanistic relationship is known — this is a pure model-score artifact (L5). Separately, this evidence pack shows systemic disease-label mismatches affecting several other candidates, which need correction before any can be responsibly evaluated.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (blocking data gap DG001) to establish baseline safety/contraindication information
- DrugBank MOA data (data gap DG002) to properly assess mechanistic plausibility
- Correction of the disease-ontology mapping errors identified in ranks 4, 5, 7, 8, and 10 — particularly rank 5 ("lung benign neoplasm"), where the underlying CROWN-trial evidence actually supports the *already-approved* ALK+ NSCLC indication, not a new one
- If gingival fibromatosis is to be pursued further, preclinical/mechanistic studies establishing any biological link to ALK/ROS1 signaling, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

