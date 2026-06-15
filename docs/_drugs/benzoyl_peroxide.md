---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Benzoyl Peroxide: From Acne Vulgaris to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide (BPO) is a topical oxidizing agent widely established for the treatment of acne vulgaris, exerting antibacterial and keratolytic effects on follicular units. The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, yet this prediction is currently supported by **no clinical trials** and **no published literature**. Without biological rationale beyond knowledge-graph node proximity, the overall evidence posture is model prediction only (L5).

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (established use; no formal indication text on record in this dataset) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Benzoyl peroxide acts as a potent oxidizing agent that releases free-radical oxygen species on contact with skin. This leads to direct bactericidal activity against *Cutibacterium acnes* and secondary keratolytic effects — softening and dissolving the keratin plug that obstructs follicular ostia. These two combined actions explain BPO's long-standing role in acne vulgaris management.

Vulvar inverted follicular keratosis is a rare benign epithelial neoplasm arising from the follicular infundibulum. It is characterized histologically by squamous eddies, inverted endophytic growth, and acanthotic epithelial proliferation — features that are mechanistically distinct from the inflammatory follicular obstruction seen in acne. The TxGNN model likely derived its high score from shared "keratosis" and "follicular" ontology nodes in the disease knowledge graph, creating a topological link that does not translate into a meaningful biological one.

In short, while BPO does interact with follicular keratin, the pathological driver of vulvar inverted follicular keratosis is neoplastic epithelial proliferation rather than microbial overgrowth or inflammatory keratinous plugging. BPO has no known anti-proliferative or anti-neoplastic mechanism relevant to this lesion type. This prediction is assessed as a high-risk graph topology false positive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Benzoyl peroxide has no registered authorizations in Saudi Arabia at this time. No license records are available for review.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.92%), but this reflects knowledge-graph structural proximity — not clinical or mechanistic evidence. Vulvar inverted follicular keratosis is a benign neoplastic lesion for which BPO has no plausible therapeutic mechanism, and zero supporting trials or publications exist. Proceeding with repurposing development at this stage is not justified.

**To proceed, the following is needed:**
- Formal MOA documentation for BPO, particularly any evidence of anti-proliferative or lesion-modulating activity beyond keratolysis and antibacterial action
- Systematic literature search broadened to include keratolytic agents (salicylic acid, tretinoin) in inverted follicular keratosis, to assess the class hypothesis
- Pathology consultation to determine whether any keratolytic intervention has biological rationale in benign follicular neoplasms
- Saudi Arabia registration pathway assessment should evidence emerge in the future
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

