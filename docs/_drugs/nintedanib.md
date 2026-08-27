---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 3
---

# Nintedanib
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

# Nintedanib: From Unspecified Original Indication to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib's original approved indication and mechanism of action are not recorded in this evidence pack, and the drug is not currently marketed in Saudi Arabia (0 licenses on file). The TxGNN model predicts potential efficacy in **Dermatofibrosarcoma Protuberans (DFSP)**, but this is currently supported only by an indirect, class-level mechanism review — **0 clinical trials** and **1 publication** (not disease-specific).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SFDA/KSA market license or indication text on file |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nintedanib is not available at the drug level in this evidence pack (data gap DG002). However, the model's own repurposing rationale identifies nintedanib as a **triple angiokinase inhibitor**, blocking VEGFR1-3, FGFR1-3, and PDGFR-α/β.

DFSP is driven by the COL1A1-PDGFB fusion gene, resulting in constitutive PDGFR-β activation. Because nintedanib inhibits PDGFR-β, it shares a mechanistic target with imatinib — the current standard of care for DFSP, which also acts on PDGFR. This overlap is the basis for the TxGNN association.

That said, the supporting literature is a general pharmacology review of PDGFR-inhibitor drug class (not specific to nintedanib or DFSP), and no case reports, preclinical models, or trials directly test nintedanib in DFSP. The mechanistic plausibility is real, but the evidence remains indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors across neoplastic disorders; establishes class-level rationale for PDGFR blockade in PDGF-driven tumors, but does not evaluate nintedanib in DFSP specifically |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA package insert warnings/contraindications (DG001) are flagged as a **Blocking** data gap in this evidence pack — this alone prevents the candidate from clearing a preliminary (S1) safety screen until resolved.*

---

## Additional Model-Predicted Indications (Lower Confidence, Not Pursued)

Two further indications were flagged by TxGNN for nintedanib but carry no clinical or literature evidence (L5, stage S0) and are recommended **Hold**:

| Disease | TxGNN Score | Evidence | Rationale Summary |
|---------|------------|----------|--------------------|
| Liposarcoma | 99.13% | None | Liposarcoma is a heterogeneous disease group; most subtypes (e.g., myxoid, FUS-DDIT3–driven) lack PDGFR/VEGFR/FGFR pathway dependence, weakening mechanistic fit |
| Ovarian myxoid liposarcoma | 99.12% | None | Ultra-rare tumor driven by FUS-DDIT3/EWSR1-DDIT3 fusion, not an angiogenesis/PDGFR-dependent tumor; no supporting trials or literature |

These are model-driven signals only and are not advanced further at this stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (DFSP) rests on mechanism-only (L4) evidence with no nintedanib-specific trials, case reports, or preclinical data. Critically, TFDA safety data (warnings, contraindications, DDI) are entirely missing — a **Blocking** gap that prevents even a preliminary S1 safety assessment — and the drug is not currently marketed in Saudi Arabia, with no original indication on record to anchor a benefit-risk comparison.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications, drug interactions) — resolves Blocking gap DG001
- Confirmed original indication and regulatory approval history for nintedanib
- DrugBank/verified mechanism-of-action detail — resolves gap DG002
- Preclinical (e.g., PDGFR-driven xenograft) or case-level evidence of nintedanib activity specifically in DFSP before advancing beyond Research Question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

