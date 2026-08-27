---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro (DB00046) is a rapid-acting insulin analog used to manage diabetes mellitus. TxGNN's top prediction links it to **Autoimmune Oophoritis** with a **99.78%** score, but currently **0 clinical trials** and **0 publications** support this specific indication, and the model's own rationale flags the signal as likely reflecting disease co-occurrence rather than a genuine treatment mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (not confirmed via Saudi Arabia registry — no local licenses on file) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for insulin lispro is not available in this evidence pack (marked as a data gap). What can be said from general knowledge is that insulin lispro is a rapid-acting insulin analog whose efficacy in glycemic control for diabetes mellitus is well established.

However, the repurposing rationale for autoimmune oophoritis is **not** a proposed treatment mechanism — it is explicitly flagged as a probable confounding signal. Autoimmune oophoritis can occur as part of autoimmune polyglandular syndrome type 2 (APS-2), which frequently co-occurs with type 1 diabetes. TxGNN's knowledge graph likely picked up this pattern because patients with both conditions are commonly co-prescribed insulin, not because insulin lispro has any known biological action on ovarian autoimmune destruction.

In short, this is a comorbidity-driven artifact rather than a mechanistically grounded repurposing hypothesis, and it is corroborated by the complete absence of clinical trials or literature specifically linking insulin lispro to autoimmune oophoritis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries no direct clinical trial or literature support (Evidence Level L5), and the model's own mechanistic rationale describes a comorbidity confound rather than a plausible treatment pathway — this does not meet the bar to advance to safety or clinical screening.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert warnings and contraindications (currently blocking — required before any S1 safety screening)
- Confirmed mechanism of action data via DrugBank API query
- A biologically grounded hypothesis (beyond comorbidity) connecting insulin signaling to ovarian autoimmune pathology, or de-prioritization of this candidate in favor of higher-evidence predictions (e.g., rank 7, pancreatic agenesis, which reflects an established clinical care pattern rather than a novel mechanism)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

