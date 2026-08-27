---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea-class oral antidiabetic, pharmacologically known for stimulating insulin secretion via pancreatic β-cell K-ATP channels. The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, but this prediction currently has **0 clinical trials** and **0 publications** directly supporting it — it is a pure model-generated signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (general pharmacological knowledge; not confirmed by this Evidence Pack) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (marked as a High-severity data gap). Based on general pharmacological knowledge, glimepiride is a sulfonylurea that binds SUR1/Kir6.2 (K-ATP) channels on pancreatic β-cells to trigger insulin release — its efficacy in Type 2 Diabetes Mellitus is well established.

Focal stiff limb syndrome (a localized variant of stiff person syndrome) is an autoimmune, anti-GAD65-antibody-mediated disorder of GABAergic neurotransmission — mechanistically unrelated to insulin secretion. Neurons do express K-ATP channels, but no evidence indicates sulfonylureas modulate GABAergic transmission or anti-GAD65 autoimmunity. The TxGNN score is high, but the model appears to be surfacing a graph-proximity signal rather than a validated mechanistic link.

Notably, 8 other diseases in this pack score similarly high (0.995–0.997), most of them ultra-rare conditions (stiff person syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, several lipodystrophies, pancreatic agenesis). Only the thiamine-responsive dysfunction syndrome and pancreatic agenesis candidates have any plausible mechanistic rationale (both involve β-cell dysfunction), and even those are unvalidated analogies with no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Glimepiride is not currently marketed in Saudi Arabia under this dataset — 0 product authorizations are on record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a TxGNN similarity score (L5, S0 stage) with zero supporting clinical trials or literature, and the proposed indication has no plausible mechanistic bridge to glimepiride's known pharmacology. A Blocking data gap on TFDA/regulatory safety labeling also prevents any S1 safety evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank query, currently unresolved)
- TFDA/official package insert with warnings, contraindications, and DDI data (Blocking gap — required before any S1 safety review)
- Preclinical or case-level evidence connecting sulfonylurea pharmacology to GABAergic/autoimmune neurological disease
- Re-evaluation of the higher-plausibility candidates in this pack (e.g., thiamine-responsive dysfunction syndrome, pancreatic agenesis) as alternative leads, given their closer mechanistic overlap with β-cell function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

