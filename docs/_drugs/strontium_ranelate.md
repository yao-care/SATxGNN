---
layout: default
title: Strontium Ranelate
parent: 僅模型預測 (L5)
nav_order: 585
evidence_level: L5
indication_count: 5
---

# Strontium Ranelate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Strontium Ranelate: From Osteoporosis to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Strontium ranelate is a bone-metabolism agent historically used for osteoporosis. The TxGNN model predicts a possible link to **Heparin Cofactor 2 Deficiency**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states there is no known biological connection between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (general pharmacological knowledge; not present in this evidence pack — no `taiwan_regulatory.licenses` entries) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, strontium ranelate acts on bone remodeling — activating calcium-sensing receptors to promote osteoblast activity while inhibiting osteoclast activity — and its established clinical use has been in osteoporosis and fracture risk reduction.

For this candidate, however, the evidence pack's own `repurposing_rationale` explicitly states there is **no known mechanistic link**: heparin cofactor II deficiency is a rare coagulation-regulatory protein disorder, and its biology (thrombin inhibition pathways) does not intersect with strontium ranelate's known bone-metabolism activity. The high TxGNN score appears to reflect embedding-space similarity rather than a biologically grounded relationship, and no clinical or literature evidence currently exists to support the link.

It is also worth noting that all five top-ranked TxGNN predictions for this drug (heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, thrombophilia, severe nonproliferative diabetic retinopathy) fall into this same unsupported category — four of the five are coagulation/thrombosis-related, and the rationale for several notes that strontium ranelate carries a **known venous thromboembolism (VTE) risk**, which would argue against rather than for repurposing into thrombosis-adjacent indications.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Strontium ranelate currently has no marketing authorizations registered in Saudi Arabia (market status: Not Marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting any of the top five TxGNN-predicted indications, and the mechanistic rationale for the top-ranked candidate (heparin cofactor 2 deficiency) explicitly states there is no biological plausibility. Several lower-ranked candidates are thrombosis-related, a direction that conflicts with strontium ranelate's known VTE risk. Combined with the drug's unmarketed status in Saudi Arabia and a Blocking-severity gap in safety/label data, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (DG001, Blocking — required before any S1 safety screening)
- Verified mechanism of action data from DrugBank or equivalent source (DG002, High)
- Independent biological plausibility assessment for heparin cofactor 2 deficiency, since the current score is model-prediction-only (L5)
- A safety re-evaluation of the VTE risk profile before considering any of the four thrombosis-adjacent candidates further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

