---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor (DB06809) is a CXCR4 antagonist internationally used to mobilize hematopoietic stem cells for collection and autologous transplantation in patients with lymphoma or multiple myeloma — this original-use context is background pharmacological knowledge, as the evidence pack itself contains no confirmed original-indication or MOA data. The TxGNN model predicts a possible new application in **Indolent Plasma Cell Myeloma**, with a very high prediction score (**99.97%**), but **zero clinical trials and zero publications** in this dataset currently support that specific link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Saudi Arabia (drug unlicensed, no approved indication text available). Internationally, Plerixafor is approved for peripheral blood stem cell mobilization in non-Hodgkin lymphoma / multiple myeloma patients undergoing autologous transplant (background knowledge, not confirmed within this evidence pack) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap, High severity). Based on known background pharmacology, Plerixafor is a CXCR4 antagonist that disrupts the CXCR4/CXCL12 axis, releasing hematopoietic (and malignant) cells from the bone marrow niche into circulation — this is the basis of its established use as a stem cell mobilizing agent ahead of autologous transplantation in multiple myeloma and lymphoma patients.

Indolent plasma cell myeloma sits within the same plasma cell dyscrasia spectrum as multiple myeloma, so a mechanistic hypothesis is plausible: if CXCR4 blockade dislodges malignant plasma cells from protective marrow niches, it could theoretically sensitize them to therapy or alter disease course, similar to the chemosensitization rationale documented for CXCR4 blockade in leukemia (see Myeloid Leukemia note below).

However, this rationale is extrapolated from general CXCR4 biology, not from any direct study of Plerixafor in indolent plasma cell myeloma. No clinical trial or literature record in this dataset examines this specific pairing, so the prediction should be treated as a model-generated hypothesis only, not an evidence-backed relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Additional Note: Other Candidate Indications in This Evidence Pack

This evidence pack (`TW-DB06809-multi`) contains 7 TxGNN-ranked predictions for Plerixafor. Six of them — including the top-ranked Indolent Plasma Cell Myeloma above — have TxGNN scores above 99% but **no supporting clinical trials or literature** (CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, bronchitis, vulvar melanoma), and are all scored L5/Hold.

One exception stands out: **Myeloid Leukemia** (rank 7, TxGNN score 99.02%) is supported by ~30 registered clinical trials (multiple completed Phase 1/2 studies combining Plerixafor with G-CSF/chemotherapy for AML chemosensitization and stem cell mobilization/transplant) and ~20 PubMed publications on the CXCR4/CXCL12 axis in AML, reaching **evidence level L2** with a "Research Question" designation — a materially stronger signal than the indication covered in the main body of this report. This candidate warrants its own dedicated evaluation report rather than being treated as a secondary note here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for Indolent Plasma Cell Myeloma is very high, but this dataset contains no clinical trials, no publications, and no confirmed MOA data linking Plerixafor to this specific indication — it is a pure model prediction (L5, S0). Core drug-level data needed even to begin safety screening (TFDA/SFDA package insert warnings, DG001) is flagged as a **Blocking** gap.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Confirmed mechanism of action data (DG002, High)
- Targeted literature and clinical trial search specifically for Plerixafor in indolent/plasma cell myeloma populations
- Saudi Arabia market licensing status confirmation (currently unlicensed)
- Consider prioritizing the Myeloid Leukemia candidate (L2, Research Question) from this same evidence pack for a separate, better-supported evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

