---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibrate-class lipid-regulating agent, historically used to manage hypertriglyceridemia and mixed dyslipidemia. The TxGNN model's top-ranked prediction is that it may be effective for **Rheumatoid Arthritis**, but this direction is currently supported only by **preclinical/mechanistic literature (4 publications)** and **no clinical trials**, so the evidence remains weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Saudi Arabia regulatory data (drug is unmarketed there); globally known as a fibrate for hypertriglyceridemia/mixed dyslipidemia |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for gemfibrozil is not available (Data Gap DG002). Based on known information, gemfibrozil belongs to the fibric acid derivative (fibrate) class, and its efficacy in hypertriglyceridemia/dyslipidemia is well established via PPAR-α agonism.

The proposed link to rheumatoid arthritis (RA) rests on a class-level mechanistic hypothesis: PPAR-α/pan-PPAR agonism has anti-inflammatory and T-cell-regulatory (Foxp3) effects, and a related pan-PPAR agonist, bezafibrate, showed benefit in an experimental RA model in 2026. However, no literature in this evidence pack demonstrates a direct anti-arthritic effect of gemfibrozil itself in humans — the closest data point is a rat adjuvant-induced arthritis model where gemfibrozil was combined with prednisolone, and the remaining publications (palmar erythema description, an EAE/multiple sclerosis model) are only tangentially related to RA. This makes the prediction a research hypothesis rather than an evidence-backed repurposing candidate at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal study (rat AIA model) | Modern Rheumatology | Gemfibrozil + reduced-dose prednisolone produced a disease-management profile similar to full-dose prednisolone in a rat adjuvant-induced arthritis model |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (different drug: bezafibrate) | International Immunopharmacology | Bezafibrate, a pan-PPAR agonist, attenuated experimental RA via PPAR-γ-dependent modulation of inflammatory pathways — supports the fibrate-class mechanistic rationale, not gemfibrozil-specific data |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (EAE model, indirect) | Journal of Immunology | Studied nitric oxide–mediated Foxp3 regulation in a myelin basic protein-primed EAE (MS) model, not RA; only indirectly relevant via immune-regulatory mechanism |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review/case description | American Journal of Clinical Dermatology | Describes palmar erythema as a physical finding across systemic conditions; not a treatment study and not RA-specific |

## Saudi Arabia Market Information

Gemfibrozil is currently not marketed in Saudi Arabia (0 authorizations on record); no product license data is available.

## Safety Considerations

Please refer to the package insert for safety information. (SFDA package insert warnings/contraindications and DDI data are marked as Blocking Data Gap — DG001 — and were not available in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for gemfibrozil in RA is limited to preclinical/animal studies and one indirectly related, mechanistically-analogous fibrate (bezafibrate); there is no human clinical trial or direct RA efficacy data for gemfibrozil itself, placing this at L4 (preclinical/mechanism only) — insufficient to justify proceeding.

**To proceed, the following is needed:**
- SFDA official package insert (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- DrugBank-confirmed mechanism of action for gemfibrozil (DG002)
- A gemfibrozil-specific preclinical or early clinical study directly targeting RA (not just class-level fibrate data)
- Clarification of whether Saudi Arabia market entry is planned, given the drug is currently unmarketed there

*Note: This evidence pack also contains 9 other TxGNN-predicted indications for gemfibrozil. Of these, hypoalphalipoproteinemia (rank 4, L2 evidence, multiple comparative clinical studies) and HIV-associated hypertriglyceridemia (rank 3, L2 evidence, including one RCT) are substantially better supported than rheumatoid arthritis and may warrant a separate evaluation report if a stronger repurposing candidate is desired.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

