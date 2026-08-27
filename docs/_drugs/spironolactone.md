---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From Diuretic/Antihypertensive Use to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a mineralocorticoid receptor antagonist with well-established use as a potassium-sparing diuretic and antihypertensive agent, though detailed original-indication and mechanism-of-action data are not available in the current evidence pack.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, a hair-thinning disorder, but this prediction is currently supported by **no clinical trials and no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (spironolactone is classically known for edema, hypertension, and primary hyperaldosteronism management) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, spironolactone belongs to the mineralocorticoid receptor antagonist (potassium-sparing diuretic) class, and it is also recognized to have antiandrogenic activity — a property that has led to off-label use in androgen-related dermatologic conditions such as acne and female-pattern hair thinning.

Hypotrichosis simplex of the scalp is a hair-loss disorder that can have an androgen-mediated component in some presentations. Spironolactone's antiandrogenic activity offers a plausible mechanistic rationale for the TxGNN prediction, and a second, closely related indication (congenital hypotrichosis milia, score 99.04%) was also flagged by the model, which may reflect a consistent underlying signal around hair-follicle/androgen pathways rather than an isolated artifact.

However, this rationale is inferred from general pharmacological knowledge rather than the drug's documented original indication or MOA, both of which are marked as data gaps (DG001, DG002) in this evidence pack. The mechanistic link should be treated as hypothesis-generating only until confirmed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5 evidence) with zero clinical trials or literature for either candidate indication. Additionally, a Blocking data gap exists for TFDA package-insert warnings/contraindications (DG001), which prevents the drug from clearing the S1 safety pre-screen, and the drug is currently not marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (resolve DG001 — Blocking)
- Documented mechanism of action data (resolve DG002)
- Confirmed original indication(s) for this drug from a regulatory or DrugBank source
- Preclinical or observational evidence linking spironolactone's antiandrogenic activity to hypotrichosis simplex of the scalp
- Drug interaction (DDI) data, currently unresolved (query status: not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

