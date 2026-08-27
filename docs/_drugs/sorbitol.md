---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sorbitol: From Unrecorded Original Indication to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol's original approved indication is not documented in the available evidence, and it currently holds no marketing authorization in Saudi Arabia.
The TxGNN model predicts a very high association score (**99.40%**) with **Exercise-Induced Malignant Hyperthermia**,
but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely false-positive signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sorbitol is not available in this evidence pack, and no original indication is on record to compare against. This absence of foundational data already limits how much confidence can be placed in the predicted link.

More importantly, the evidence pack's own mechanistic assessment argues against biological plausibility: malignant hyperthermia (exercise-induced) is driven by dysfunction of the RyR1 (ryanodine) receptor, which causes uncontrolled calcium release from the sarcoplasmic reticulum. The current standard of care, dantrolene, works precisely by antagonizing RyR1. Sorbitol's known pharmacological roles — osmotic/laxative activity and sugar-alcohol metabolism — have no established mechanistic overlap with RyR1-mediated calcium dysregulation.

Given the lack of MOA data, the absence of any supporting trials or literature, and the mechanistic mismatch noted above, this high TxGNN score most likely reflects graph-embedding proximity within the knowledge graph rather than genuine pharmacological relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Sorbitol currently holds no marketing authorization in Saudi Arabia (0 licenses on record; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-only prediction with zero corroborating clinical trials or literature, no available MOA data, and a mechanistic rationale that actively argues against plausibility (RyR1-driven pathology vs. sorbitol's known osmotic/metabolic roles). There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for sorbitol (DrugBank query currently blocked/incomplete — DG002)
- TFDA/SFDA package insert data on warnings and contraindications (DG001, marked Blocking)
- Independent pharmacological or preclinical evidence linking sorbitol to RyR1/calcium-release pathology before this candidate is reconsidered
- Ongoing monitoring for any newly registered trials or publications on this drug–disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

