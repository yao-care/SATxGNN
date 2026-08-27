---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

> Orlistat is a gastric/pancreatic lipase inhibitor generally used for obesity and weight management (original indication/MOA fields are a data gap in this Evidence Pack, so this framing relies on general drug identity, not Evidence Pack data).
> The TxGNN model predicts it may be relevant to **Hypervitaminosis**,
> but **0 clinical trials** and **0 publications** currently support this direction — this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not returned by Evidence Pack (`original_indications` empty; general knowledge suggests obesity/weight management — unverified against source data) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` = Data Gap, DG002). Based on the rationale text captured for this prediction, Orlistat inhibits gastric/pancreatic lipase, reducing intestinal absorption of dietary fat. Because absorption of the fat-soluble vitamins (A, D, E, K) depends on co-absorption with dietary fat, the same mechanism would theoretically also reduce their uptake.

In current clinical practice, this effect is treated as an **adverse effect** of Orlistat — fat-soluble vitamin deficiency is a known risk of therapy — rather than as a therapeutic mechanism. The prediction here reverses that logic, proposing the same fat-malabsorption effect as a way to *lower* excess fat-soluble vitamin levels (hypervitaminosis A/D/E/K). This is mechanistically self-consistent but has **no supporting clinical or preclinical data** in this Evidence Pack.

A further gap: "hypervitaminosis" is not restricted to fat-soluble vitamins — water-soluble vitamin excess (e.g., B6, niacin) would not be affected by this mechanism at all, and the disease term in this prediction is not specified as fat-soluble-only. Until the target sub-type is clarified, the mechanistic link cannot be considered validated even in principle.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) in this Evidence Pack — this must be resolved before any S1 safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature. The drug is not marketed in Saudi Arabia (0 licenses), and safety data required for even an initial S1 review (TFDA warnings/contraindications) is a Blocking gap.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — Blocking, DG001
- Confirmed mechanism of action (MOA) from DrugBank or equivalent — High priority, DG002
- Confirmation of Orlistat's original approved indication(s), currently absent from the Evidence Pack
- Clarification of which hypervitaminosis subtype is targeted (fat-soluble vs. water-soluble), since the proposed mechanism only plausibly applies to fat-soluble vitamin excess
- At minimum, preclinical/mechanistic or case-level evidence before this candidate can move beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

