---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Hematologic Disease to Autosomal Recessive Severe Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

Ravulizumab is a terminal complement (C5) inhibitor; its original approved indications are not recorded in this evidence pack, and no Saudi Arabia market authorization exists for the drug. The TxGNN model predicts a possible effect in **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags the biological link as unconfirmed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` and Saudi Arabia license records are empty in this evidence pack |
| Predicted New Indication | Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency |
| TxGNN Prediction Score | 99.96% (rank 1178) |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on publicly known drug-class information, ravulizumab is a humanized monoclonal antibody that binds complement protein C5, blocking its cleavage into C5a and C5b and thereby preventing formation of the terminal membrane attack complex (C5b-9). This class is generally used in complement-mediated diseases; note this is background context, not data confirmed within this evidence pack.

The predicted indication, G6PC3-deficient congenital neutropenia, is caused by a defect in the glucose-6-phosphatase catalytic subunit, which drives endoplasmic reticulum stress and increased apoptosis in neutrophil precursors — a metabolic/intracellular signaling disorder. The evidence pack's own mechanistic rationale is explicit that this pathway has **no known direct relationship** to the terminal complement (C5) pathway, and states that the high TxGNN score may instead reflect proximity between "rare hematologic disease" nodes in the knowledge graph rather than a genuine mechanistic connection.

Given this, the prediction should be treated as a hypothesis-generating signal only, not as one backed by a plausible, disease-specific biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/SFDA package insert warnings and contraindications are flagged in this evidence pack as a **Blocking** data gap (DG001), meaning a formal safety review (S1) cannot proceed until this is resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence level L5 — supported only by the TxGNN model score, with zero clinical trials or publications, and the evidence pack's own mechanistic analysis casts doubt on a genuine biological link between C5 inhibition and G6PC3-related neutropenia. Combined with a Blocking safety data gap, this candidate is not ready to advance.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank/primary literature (DG002)
- Preclinical or case-level evidence testing whether complement activation contributes to G6PC3-deficient neutropenia pathology
- Re-evaluation of lower-ranked candidates (e.g., primary hyperoxaluria, rank 3) whose rationale shows a comparatively stronger, if still indirect, mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

