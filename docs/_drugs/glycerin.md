---
layout: default
title: Glycerin
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Glycerin
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

# Glycerin: Original Indication Not Available → Cauda Equina Syndrome (Predicted)

## One-Sentence Summary

Glycerin (DrugBank DB09462) has no recorded original indication or approved license in this evidence pack — it is currently **not marketed in Saudi Arabia** (0 authorizations). The TxGNN model's top-ranked prediction is **Cauda Equina Syndrome** (score 99.60%), but this is a **pure model prediction with zero supporting clinical trials or literature** in the evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (drug is unmarketed in Saudi Arabia; `original_indications` and `licenses` are both empty) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available for glycerin in this evidence pack (`original_moa` is a data gap), and no original indication is on record — the drug has no marketing history or license text in Saudi Arabia to anchor a mechanistic comparison.

For the top-ranked prediction, cauda equina syndrome, the evidence pack itself states the rationale plainly: *"無任何試驗或文獻證據，僅 TxGNN 預測分數，無可驗證機轉關聯"* (no trial or literature evidence exists; only the TxGNN prediction score is available, with no verifiable mechanistic link). No plausibility argument can be constructed from the data on hand.

For context, other lower-ranked predictions in this evidence pack describe glycerin/glycerol's known pharmacology as a classic hyperosmotic agent (e.g., used to acutely lower intraocular pressure, and as an osmotic laxative) — but that context applies to those other candidates (open-angle glaucoma, irritable bowel syndrome), not to cauda equina syndrome, and should not be read as support for the rank-1 prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Glycerin currently holds no marketing authorization in Saudi Arabia (market status: 未上市 / Not marketed; total authorizations: 0). No license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.60%), the cauda equina syndrome indication has zero supporting clinical trials or literature (L5, decision stage S0) — this is a model-only signal with no verifiable mechanistic or clinical basis. Combined with the drug's unmarketed status in Saudi Arabia and missing safety/MOA data, there is no basis to advance this indication.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001); requires downloading and parsing the official PDF before any safety pre-assessment (S1) can begin
- Mechanism of action (MOA) data — High-severity data gap (DG002); query DrugBank API
- Independent literature/trial search specifically targeting cauda equina syndrome, since current queries returned zero results and should be periodically re-run
- If continued repurposing interest exists, consider evaluating the pack's better-evidenced candidates instead — notably **open-angle glaucoma** (L3, S2, Research Question) and **irritable bowel syndrome** (L4, S1, Research Question) — as separate candidate reports, since they have actual trial/literature support that cauda equina syndrome lacks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

