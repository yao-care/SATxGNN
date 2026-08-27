---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 620
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab is a monoclonal antibody originally developed for moderate-to-severe plaque psoriasis.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (moderate-to-severe; based on public drug information — not captured in the Saudi Arabia license data, which shows 0 licenses) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on publicly known pharmacology, tildrakizumab is an anti-IL-23p19 monoclonal antibody whose efficacy in moderate-to-severe plaque psoriasis has been clinically proven. Mechanistically, it might be applicable to diabetic retinopathy because the IL-23/Th17 inflammatory axis has been observed in some models to participate in microvascular inflammation.

However, this specific candidate — severe nonproliferative diabetic retinopathy — is a more advanced subtype of diabetic retinopathy, and the underlying mechanistic hypothesis is identical to (not distinct from) the general diabetic retinopathy hypothesis: IL-23/Th17 inflammatory pathway involvement in microvascular disease. There is no drug-specific or disease-stage-specific evidence supporting this link, and no clinical trials or literature have been identified for this indication at all. Because this subtype represents more severe, vision-threatening disease, the safety risk of an unproven immunomodulatory therapy in this population is also higher than for the milder disease stage.

In short, the high TxGNN score (99.63%) reflects strong association strength within the knowledge graph, not a validated biological mechanism — this should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Tildrakizumab is not currently marketed in Saudi Arabia (0 authorizations on record); no license or approved-indication data is available for this market.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently unavailable — TFDA/SFDA package insert retrieval is flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature, no established drug-specific mechanistic link, and the drug is not currently marketed in the target market. A Blocking safety data gap (missing package insert/warnings) also precludes any S1 safety assessment.

**To proceed, the following is needed:**
- SFDA/TFDA package insert data (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism-of-action documentation for tildrakizumab (DG002)
- Preclinical or mechanistic studies directly linking IL-23p19 inhibition to diabetic retinopathy (not just IL-23/Th17 pathway inference)
- Any emerging clinical trial or case-report evidence in diabetic retinopathy populations before advancing beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

