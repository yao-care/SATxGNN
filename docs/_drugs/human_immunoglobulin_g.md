---
layout: default
title: Human Immunoglobulin G
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 3
---

# Human Immunoglobulin G
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

# Human Immunoglobulin G: From (Original Indication Not on File) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Human Immunoglobulin G (DB00028)'s original approved indication and mechanism of action are not recorded in this evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, with a **99.75%** prediction score,
> but this is currently supported by only **1 correlational biomarker publication** and **no clinical trials** — evidence is weak and likely reflects a spurious graph connection rather than a therapeutic mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licenses or indications on file for this evidence pack) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no actual therapeutic studies) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Human Immunoglobulin G is not available in this evidence pack (data gap), and no original approved indication is on file, so a mechanistic comparison between an original and new indication cannot be constructed.

More importantly, the single literature source behind this prediction (PMID 40204274) is an observational biomarker study: it measured serum IgG Fc N-glycosylation patterns to distinguish stages of diabetic retinopathy in existing patients. This is a **disease-state association finding** — a diagnostic signature — not evidence that administering exogenous human immunoglobulin G treats or prevents diabetic retinopathy. The TxGNN high score most likely arises because the knowledge graph links the "IgG" node to the "diabetic retinopathy" node through this biomarker literature, rather than through a validated pharmacological or causal pathway. There is no clinical trial, animal treatment model, or dose-response data supporting a therapeutic effect.

Given the absence of MOA data, the absence of an original indication, and a supporting literature base that is correlational rather than interventional, this prediction should be treated as a low-confidence signal requiring substantial further validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40204274](https://pubmed.ncbi.nlm.nih.gov/40204274/) | 2025 | Cohort/Biomarker | Molecular & Cellular Proteomics | Serum IgG Fc N-glycosylation was tested as a diagnostic biomarker to distinguish nonproliferative vs. proliferative diabetic retinopathy in 160 patients (47 non-DR, 51 NPDR, 62 PDR) — a diagnostic association study, not a treatment study of IVIG. |

---

## Saudi Arabia Market Information

Human Immunoglobulin G is not marketed in Saudi Arabia; no authorizations are on file in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single correlational biomarker study, with no clinical trials, no MOA data, and no original indication on record. The TxGNN score likely reflects a graph artifact from biomarker literature rather than a genuine therapeutic hypothesis, so this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank query pending — currently a High-severity data gap)
- TFDA/SFDA package insert warnings and contraindications (Blocking data gap — required before any S1 safety screening)
- Interventional (treatment) studies of IVIG in diabetic retinopathy, distinct from the existing biomarker/association literature
- Confirmation of the drug's original approved indication(s) for mechanistic comparison

---

### Other Candidate Indications Reviewed (Same Evidence Pack)

Two additional TxGNN-predicted indications were evaluated for this drug and are also rated **Hold**, for transparency:

- **Diabetic Retinopathy** (score 99.63%, L4): The 3 retrieved clinical trials all involve unrelated drugs (adalimumab, an investigational agent + liraglutide, aflibercept vs. bevacizumab) matched only by shared indication, not by drug. Literature is dominated by IgG N-glycosylation association/Mendelian-randomization studies — again correlational, not interventional for IVIG itself.
- **Drug-Induced Osteoporosis** (score 99.37%, L5): No supporting literature; the 2 retrieved trials study unrelated anti-osteoporotic agents, not IVIG. No mechanistic rationale can be built due to the MOA data gap.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

