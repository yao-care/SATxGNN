---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 3
---

# Lincomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lincomycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Lincomycin is a lincosamide-class antibacterial agent; detailed approved-indication and mechanism-of-action data for this candidate are not available in the current dataset. The TxGNN model predicts a possible association with **Hyperamylasemia**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-score signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in current dataset (Lincomycin is a lincosamide antibacterial per available rationale text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lincomycin is not currently available in this dataset. Based on the information available, lincomycin is a lincosamide-class antibiotic that acts by binding the bacterial 50S ribosomal subunit to inhibit bacterial protein synthesis — a purely antimicrobial mechanism directed at bacterial cells.

Hyperamylasemia is typically associated with pancreatic inflammation, salivary gland disease, or renal impairment — physiological processes unrelated to bacterial ribosomal protein synthesis. No biologically plausible pathway currently links lincomycin's antibacterial mechanism to amylase regulation, and the underlying MOA data itself is incomplete, which further limits any mechanistic argument.

Two other candidate indications were also flagged at nearly identical TxGNN scores — polyclonal hyperviscosity syndrome (immunoglobulin-driven plasma viscosity) and congenital analbuminemia (an *ALB* gene defect in albumin synthesis). Both share the same pattern: no known mechanistic overlap with lincomycin's antibacterial action, and no supporting trials or literature. Taken together, this indicates the ranking is currently driven by the TxGNN network's learned associations rather than by any identifiable pharmacological rationale — consistent with an L5 (model-prediction-only) evidence level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Lincomycin is not currently marketed in Saudi Arabia (0 authorizations on file), so no product/license table is available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package-insert warnings/contraindications are flagged as a Blocking data gap (DG001) in this evidence pack — a full safety review cannot be completed until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia) sit at evidence level L5 — model score only, with zero clinical trials, zero ICTRP records, and zero literature support, and no biologically plausible mechanistic link to lincomycin's known antibacterial action. The drug is also not currently marketed in Saudi Arabia, and core safety data (TFDA warnings/contraindications) is missing.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (Blocking gap, DG001)
- Verified mechanism-of-action data for lincomycin (High-priority gap, DG002)
- Any preclinical or mechanistic literature that could establish biological plausibility for hyperamylasemia (or the other two candidates) before further evaluation
- Re-screening of clinical trial/literature databases once a plausible mechanistic hypothesis is available, since current searches (2026-04-21) returned no hits
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

