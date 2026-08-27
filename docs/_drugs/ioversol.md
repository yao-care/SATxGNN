---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# IOVERSOL: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

> IOVERSOL (DrugBank DB09134) is a non-ionic, low-osmolar iodinated contrast medium used for diagnostic radiographic imaging; no original indication or MOA data was returned from the source registries used to build this pack.
> The TxGNN model's top-ranked prediction is **Osteoarthritis Susceptibility**, but **0 clinical trials** and **0 publications** currently support this specific prediction directly.
> A related, lower-ranked prediction (osteoarthritis itself) does have 4 trials and 1 publication, but that evidence concerns arterial embolization with a *different* iodinated agent (ethiodized oil/Lipiodol), not IOVERSOL — so overall evidentiary support for this candidate is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in registry data; IOVERSOL is generically classified as a diagnostic radiographic/CT contrast agent |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature for this specific indication) |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, IOVERSOL is a non-ionic, low-osmolar iodinated contrast agent used to opacify tissue during radiographic and CT imaging; its established clinical role has been as a diagnostic aid rather than a therapeutic agent, so there is no confirmed original therapeutic indication on file for this evaluation.

The TxGNN model's top prediction, "osteoarthritis susceptibility," is a disease-risk/predisposition node in the knowledge graph rather than a treatable clinical endpoint, and no clinical trial or literature evidence was retrieved to connect IOVERSOL to it. A mechanistic rationale linking an imaging contrast agent to osteoarthritis risk modification is not established in the data provided.

It is worth noting that the model's second-ranked prediction, osteoarthritis itself (score 99.63%), is supported by several trials and one publication — but that evidence describes genicular/digital artery embolization using an *ethiodized oil-based emulsion* (Lipiodol), a structurally distinct iodinated compound, not IOVERSOL. This is a related but indirect signal at best, and should not be read as direct support for IOVERSOL's efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

IOVERSOL is not currently marketed in Saudi Arabia (0 licenses on file); no product registration data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (osteoarthritis susceptibility) has zero supporting clinical trials or literature — this is a pure model prediction (L5). Combined with a blocking data gap on TFDA/package-insert warnings and contraindications (DG001), the candidate cannot yet clear an initial safety review, and IOVERSOL is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/package insert warnings and contraindications (blocking gap DG001)
- Confirmed mechanism of action data from DrugBank or another authoritative source (DG002)
- Clarification of whether the osteoarthritis-related trial/literature evidence (rank 2) is genuinely attributable to IOVERSOL or to a distinct iodinated compound (Lipiodol/ethiodized oil), before treating it as supporting evidence
- Confirmation of IOVERSOL's original approved indication(s) for a valid before/after comparison
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

