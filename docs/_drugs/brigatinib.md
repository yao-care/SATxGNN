---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib is a next-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor, internationally approved for the treatment of ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is entirely model-driven with no biological or clinical evidence, and should be treated as a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive Non-Small Cell Lung Cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on the extensive literature included in this report, Brigatinib is a potent second-generation ALK tyrosine kinase inhibitor with demonstrated efficacy specifically against ALK gene rearrangements and fusions. Its validated clinical use is in ALK-positive NSCLC, where multiple Phase 3 RCTs — most notably the ALTA-1L trial — have shown superior progression-free survival compared to the first-generation inhibitor crizotinib. Beyond ALK, Brigatinib also inhibits several other kinase targets (including ErbB2/ErbB3 and FAK), which accounts for its observed activity in rare ALK-negative contexts such as NF2-related schwannomatosis.

Gingival fibromatosis is a rare hereditary or idiopathic fibrous overgrowth of the gingiva. Its known genetic drivers include mutations in **SOS1**, **KCNJ13**, and **FAM20A**, none of which intersect with the ALK signaling pathway or any established off-target kinase of Brigatinib. There is no mechanistic link between ALK inhibition and the fibroproliferative pathways underlying this condition.

The high TxGNN prediction score (99.89%) most likely reflects indirect topological proximity within the drug-disease knowledge graph rather than true biological relevance. Without any supporting experimental or clinical data, this prediction cannot be considered actionable and requires biological plausibility investigation before any experimental work is justified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Brigatinib is an antineoplastic targeted therapy approved for ALK-positive lung cancer. The following cytotoxicity profile applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (ALK-TKI) |
| Myelosuppression Risk | Low (TKI class; substantially lower risk than conventional cytotoxics) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST), pulmonary function and chest imaging (early-onset ILD/pneumonitis risk in week 1), blood pressure (hypertension), blood glucose (hyperglycemia), heart rate (bradycardia), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.89%, this indication is classified as L5 evidence — model prediction only — with zero supporting clinical trials or publications and no identifiable mechanistic connection between Brigatinib's primary ALK-inhibitory activity and the known genetic drivers of gingival fibromatosis (SOS1/KCNJ13/FAM20A).

**To proceed, the following is needed:**
- **Biological plausibility analysis**: determine whether ALK or any known Brigatinib off-target kinase plays a role in gingival fibromatosis pathogenesis
- **Mechanism of action data**: DrugBank API query is recommended (flagged as a high-severity data gap in this Evidence Pack)
- **Safety warnings and contraindication data**: package insert retrieval from the SFDA or originator (flagged as a blocking data gap preventing S1 safety screening)
- **Preclinical investigation**: gingival fibromatosis cell line or animal model studies would be required before any clinical hypothesis can be formed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

