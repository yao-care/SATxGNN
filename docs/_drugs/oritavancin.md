---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: From Gram-Positive Bacterial Infections to Bacteroidaceae Infectious Disease

## One-Sentence Summary

> Oritavancin is a lipoglycopeptide antibiotic whose established spectrum covers Gram-positive organisms, including MRSA.
> The TxGNN model assigns its highest-ranked new-indication signal to **Bacteroidaceae infectious disease**,
> but this prediction is currently backed by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in this evidence pack (drug not marketed locally); known spectrum is Gram-positive bacterial infections, including MRSA |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Oritavancin is a lipoglycopeptide antibiotic. Its mechanism of action inhibits bacterial cell-wall synthesis by binding the D-Ala-D-Ala terminus of peptidoglycan precursors, combined with membrane-disrupting activity. This mechanism is effective against **Gram-positive** organisms, including MRSA, which is consistent with oritavancin's known clinical role in skin and soft-tissue infections.

The top-ranked prediction, Bacteroidaceae infectious disease, targets a **Gram-negative anaerobic** family. Gram-negative organisms have an outer membrane that typically excludes glycopeptide-class drugs, meaning oritavancin's mechanism does not naturally extend to this target. The evidence pack's own mechanistic rationale explicitly notes this mismatch and attributes the high TxGNN score to likely over-generalization of a broad "antibiotic–infectious disease" association pattern rather than a species-specific signal.

The two lower-ranked candidates in this evidence pack (ophthalmic herpes zoster, rank 2; Mycoplasma pneumoniae pneumonia, rank 3) are mechanistically even weaker: herpes zoster is a viral infection with no plausible link to a cell-wall-targeting antibacterial, and Mycoplasma species lack a cell wall entirely, making them intrinsically insensitive to oritavancin's mechanism. All three candidates in this pack are therefore assessed as low-confidence, model-only signals rather than mechanistically supported repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No product authorizations are on record — oritavancin is currently not marketed in this jurisdiction (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (Bacteroidaceae infectious disease) has no clinical trial or literature support and is L5 (model prediction only); the evidence pack's own mechanistic analysis argues the signal is likely spurious given oritavancin's Gram-positive-restricted mechanism versus Bacteroidaceae's Gram-negative anaerobic biology. The two other candidates in this pack are mechanistically even less defensible and do not change this conclusion.

**To proceed, the following is needed:**
- TFDA/regional package insert data (warnings, contraindications — currently a blocking data gap)
- Verified mechanism-of-action source documentation
- Confirmed original approved indication(s) for this drug in the target market
- If pursued further, in vitro susceptibility data for oritavancin against Bacteroidaceae specifically, since no existing evidence supports Gram-negative anaerobic coverage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

