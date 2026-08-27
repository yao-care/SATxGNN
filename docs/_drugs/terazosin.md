---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Benign Prostatic Hyperplasia/Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is a selective α1-adrenergic receptor antagonist historically used for benign prostatic hyperplasia (BPH) and hypertension. The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the score most likely reflects embedding proximity rather than an established biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH) / Hypertension (based on known pharmacology of terazosin; not confirmed in the Saudi regulatory data, as the drug is unmarketed there) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (marked as a data gap in this evidence pack). Based on known pharmacology, terazosin is a quinazoline-derived, selective α1-adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck (useful in BPH) and reduces peripheral vascular resistance (useful in hypertension).

Hypotrichosis simplex of the scalp is a monogenic hereditary hair-development disorder most commonly associated with genes such as *APCDD1*, involving Wnt-signaling dysregulation in the hair follicle — a pathway with no established connection to α1-adrenergic blockade. No mechanistic, preclinical, or clinical literature links terazosin to this condition.

Given the absence of any supporting mechanism, trial, or publication, this prediction should be treated as a high TxGNN-score artifact likely driven by knowledge-graph embedding proximity (e.g., shared neighbors with other hair-related nodes) rather than genuine pharmacological plausibility. It should not be interpreted as a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Terazosin is not currently marketed in Saudi Arabia — no authorizations are on file (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.97%), there is no mechanistic rationale, no preclinical data, no clinical trials, and no literature supporting terazosin's use in hypotrichosis simplex of the scalp. This pattern — a top-ranked score with zero corroborating evidence, while lower-ranked candidates for the same drug (e.g., Raynaud disease at rank 7, migraine at rank 5) have direct mechanistic plausibility and small clinical studies — suggests the top score reflects embedding artifact rather than biological signal.

**To proceed, the following is needed:**
- Confirmed DrugBank/MOA data (currently a data gap)
- TFDA/SFDA package insert with warnings and contraindications (currently a blocking data gap)
- Preclinical evidence connecting α1-adrenergic blockade to hair follicle biology in *APCDD1*-related hypotrichosis
- If repurposing evaluation continues for this drug, consider prioritizing **Raynaud disease** (rank 7, L3, direct α1-mediated vasospasm mechanism, small clinical study) and **migraine disorder** (rank 5, L3) instead, as they carry materially stronger mechanistic and literature support than this top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

