---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Undocumented Original Indication to Pseudoachondroplasia

## One-Sentence Summary

Lithium Carbonate (DrugBank DB14509) is not currently marketed in Saudi Arabia, and its original approved indication and mechanism of action are not documented in this evidence pack. The TxGNN model predicts it may be effective for **Pseudoachondroplasia**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, with the evidence pack's own rationale stating there is no known pharmacological pathway linking lithium to this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lithium carbonate is not available in this evidence pack (flagged as a High-severity data gap, DG002). No original indication is recorded either, so a mechanistic comparison between the original and predicted use cannot be constructed from the supplied data.

For the top-ranked prediction itself, the evidence pack's own rationale is explicit that there is **no mechanistic support**: pseudoachondroplasia arises from COMP gene mutations causing misfolded cartilage oligomeric matrix protein to accumulate in the endoplasmic reticulum, and no known lithium pharmacology (e.g., GSK-3β inhibition) is described as correcting protein misfolding or ER stress. The TxGNN score is very high (99.98%), but this reflects graph-embedding similarity in the model's knowledge graph, not a validated or even hypothesized biological pathway.

Worth noting for context: several lower-ranked predictions in this same evidence pack (notably WHIM syndrome, rank 9, L4/S1) reference lithium's **established** psychiatric-care pharmacology — its known effect of stimulating granulocyte production and raising peripheral neutrophil counts — as a plausible mechanistic bridge. That established, sourced pharmacological signal is absent from the rationale for pseudoachondroplasia, reinforcing that this top-ranked candidate is a pure model artifact rather than a mechanism-supported hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Lithium carbonate is not marketed in Saudi Arabia (0 authorizations on record); no license or product data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA package insert warnings and contraindications are flagged as a Blocking data gap, DG001 — this prevents the candidate from entering the S1 safety pre-assessment stage regardless of predicted-indication evidence strength. Drug interaction query also returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pseudoachondroplasia) has evidence level L5 (model prediction only) and decision stage S0, with the evidence pack itself stating no mechanistic pathway supports the link. Independently, a Blocking data gap (missing SFDA package insert) prevents this candidate from reaching safety pre-assessment regardless of indication-level evidence.

**To proceed, the following is needed:**
- SFDA/TFDA package insert (warnings, contraindications) to clear the Blocking gap (DG001) and unblock S1 safety review
- Verified mechanism of action data (DG002) for lithium carbonate
- If pursuing repurposing further, consider redirecting attention within this same evidence pack toward **WHIM syndrome** (rank 9, evidence level L4, decision stage S1, "Research Question"), which has a sourced mechanistic rationale (lithium's known granulocyte-stimulating effect via GSK-3β/CXCR4-CXCL12 pathway) — a materially stronger starting point than the top TxGNN-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

