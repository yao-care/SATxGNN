---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Selpercatinib: From RET-Driven Cancers to Pulmonary Hypertension

## One-Sentence Summary

> Selpercatinib is a RET kinase inhibitor; this evidence pack does not include its formal approved-indication text, but the cited literature references its use in RET fusion-positive NSCLC and RET-mutant medullary thyroid carcinoma.
> The TxGNN model predicts a possible signal for **Pulmonary Hypertension**, but this is supported by **0 clinical trials** and only **3 tangentially related publications** (none specific to pulmonary hypertension outcomes).
> Given that other kinase inhibitors are known to *cause* pulmonary hypertension rather than treat it, this prediction should be treated as a signal requiring mechanistic clarification, not a repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in this evidence pack (`original_indications` empty, MOA flagged as Data Gap). Cited literature refers to use in RET fusion-positive NSCLC and RET M918T-mutant medullary thyroid carcinoma. |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% (rank 11,589) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). What is known from the cited literature is that selpercatinib is a highly selective RET tyrosine kinase inhibitor, used in RET fusion/mutation-driven cancers such as NSCLC and medullary thyroid carcinoma.

There is no established mechanistic link between RET/GDNF signaling and pulmonary vascular remodeling — the pathway underlying pulmonary hypertension. By contrast, several other tyrosine kinase inhibitors (e.g., dasatinib) are well documented to **cause** pulmonary hypertension as an adverse drug reaction. This raises the possibility that the TxGNN network has picked up a class-level "TKI ↔ pulmonary vascular effect" association that reflects a safety signal rather than a therapeutic opportunity — the direction of the relationship needs to be clarified before this is treated as a repurposing candidate.

No clinical trials or disease-specific literature currently support a therapeutic hypothesis. The two supporting publications identified are largely unrelated in focus (a pharmacovigilance comparison of RET inhibitors' adverse events, a real-world NSCLC outcomes study, and a medullary thyroid carcinoma case report) — none evaluate selpercatinib in the context of treating pulmonary hypertension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Pharmacovigilance | Frontiers in Pharmacology | FDA FAERS-based comparison of adverse event profiles between pralsetinib and selpercatinib — relevant to safety signal detection, not treatment efficacy for pulmonary hypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective analysis | Therapeutic Advances in Medical Oncology | Real-world efficacy of selpercatinib in RET fusion-positive NSCLC via an access program (SIREN study) — establishes original oncology use, not pulmonary hypertension relevance |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report | Cureus | Long-term management of RET M918T-mutant metastatic medullary thyroid carcinoma (MEN2B) with targeted therapy — again oncology context, not pulmonary hypertension |

---

## Saudi Arabia Market Information

No authorizations on record — the drug is not currently marketed (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: DG001 — TFDA/local package insert warnings and contraindications are flagged as a Blocking-severity data gap; safety data could not be pulled into this evidence pack, and no DDI records were found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension signal is TxGNN-prediction-only (L5), with zero supporting clinical trials and no literature directly evaluating this indication. The mechanistic rationale is inconclusive and may even point in the opposite direction (TKI-induced pulmonary hypertension as an adverse effect), so this should not proceed as a repurposing candidate without further clarification. The other two candidates in this pack (migraine disorder, migraine with brainstem aura) have no clinical trial or literature support at all and no plausible mechanistic link to RET inhibition — both are also Hold/L5.

**To proceed, the following is needed:**
- TFDA/local package insert (safety warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data via DrugBank — currently a High-severity data gap
- A directional analysis clarifying whether the RET inhibitor ↔ pulmonary hypertension association reflects a therapeutic effect or an adverse drug reaction signal
- Preclinical or mechanistic studies linking RET/GDNF signaling to pulmonary vascular remodeling
- Any prospective clinical evidence in pulmonary hypertension populations (currently none registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

