---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin Glargine (DB00047) is a long-acting basal insulin analog established for diabetes mellitus management. The TxGNN model's top-ranked prediction is **Autoimmune Oophoritis**, but this candidate has **zero clinical trials, zero publications**, and its own mechanistic rationale flags it as likely graph-embedding noise rather than a genuine treatment signal. This is one of 10 low-confidence predictions in this evidence pack; none reach a strong evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1/Type 2) — based on known drug identity; no approved-indication text was returned by this evidence pack (see Data Gaps below) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known information, insulin glargine is a long-acting insulin analog used to achieve basal glycemic control in diabetes mellitus; its efficacy in that indication is well established.

For autoimmune oophoritis specifically, the evidence pack's own rationale is skeptical: there is no known mechanism linking exogenous insulin to autoimmune ovarian inflammation. The high TxGNN score is more plausibly explained by graph-embedding proximity — autoimmune oophoritis frequently co-occurs with other autoimmune endocrinopathies (e.g., autoimmune polyglandular syndrome, which can include type 1 diabetes) — rather than a direct causal or therapeutic relationship. No clinical trial or literature evidence was retrieved to support this link, and the pack itself scores this as L5 (model prediction only) with a "Hold" recommendation.

Two other candidates in this batch (thiamine-responsive dysfunction syndrome / TRMA, and stiff-person spectrum disorders) have a more coherent — though still indirect — mechanistic story: both conditions frequently present with comorbid diabetes mellitus that insulin treats as a complication, not as the disease itself. Several other candidates (drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced lipoatrophy, idiopathic localized lipodystrophy) are explicitly flagged as probable **reverse-causation artifacts** — subcutaneous insulin injection is a known *cause* of localized lipodystrophy, so the model may have learned the co-occurrence backwards.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No license records are available in this evidence pack. `taiwan_regulatory.market_status` indicates the product is **未上市 (not marketed)** with **0 registered authorizations**.

---

## Safety Considerations

TFDA package insert data (warnings/contraindications) is marked as a **Blocking** data gap (DG001) — this evidence pack could not retrieve label-level safety information, which by itself prevents this candidate from clearing the S1 safety-review stage. No drug interaction records were found (`ddi.query_status = not_found`).

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (autoimmune oophoritis) has no clinical trial or literature support and is explicitly flagged by its own rationale as likely a graph-embedding artifact rather than a real mechanistic link. Combined with a Blocking data gap on TFDA safety labeling (DG001) and the drug's not-marketed status in Taiwan, there is no basis to advance this candidate beyond S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required before any S1 safety review (DG001, Blocking)
- DrugBank-confirmed mechanism of action (DG002, High)
- Targeted literature/trial search specifically for "insulin glargine" + "autoimmune oophoritis" using expanded synonyms, since the current PubMed/ClinicalTrials/ICTRP queries returned zero hits
- If prioritizing this batch further, the pancreatic agenesis candidate (rank 6, L3/S2, "Proceed with Guardrails") warrants separate evaluation — it reflects an already-established clinical use pattern (insulin for secondary diabetes from pancreatic developmental defects) rather than a novel repurposing hypothesis, and should be scoped as such rather than folded into this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

