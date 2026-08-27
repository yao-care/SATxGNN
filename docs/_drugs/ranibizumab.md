---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: From Anti-VEGF Ophthalmic Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is a humanized anti-VEGF-A monoclonal antibody fragment; no approved indication is currently on file for the Saudi Arabia market (drug not marketed).
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (severe NPDR)**,
> with **6 clinical trials** (including 3 completed Phase 3 RCTs) and **10+ prioritized publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (drug not currently marketed in Saudi Arabia) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

A formal, sourced mechanism-of-action record (original_moa) is not currently on file for ranibizumab. However, the repurposing evidence itself documents that ranibizumab is a humanized anti-VEGF-A monoclonal antibody fragment. VEGF is a core driver of vascular leakage and pathological neovascularization in diabetic retinopathy (DR), and intravitreal anti-VEGF injection is already an established, guideline-level treatment mechanism for DR and diabetic macular edema (DME).

Because no original indication is on record for this market, the "original-to-new indication" relationship cannot be framed as a shift between two approved uses. Instead, the case rests on ranibizumab's well-validated anti-VEGF pharmacology: this mechanism directly targets the vascular pathology underlying severe NPDR, and multiple completed Phase 3 trials (below) have already tested ranibizumab specifically in NPDR populations rather than only in DME or wet AMD. This makes the mechanistic linkage clinically demonstrated rather than a purely computational (TxGNN-only) association.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | DRCR.net Protocol I-type study comparing laser alone, laser + triamcinolone, laser + ranibizumab, and ranibizumab alone for diabetic macular edema |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Anti-VEGF (PANORAMA-type) treatment for prevention of vision-threatening progression in high-risk diabetic retinopathy |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Completed | 174 | Port Delivery System with ranibizumab vs monitoring in NPDR without center-involved DME |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Intravitreous ranibizumab vs sham injection for prevention of high-risk DR progression |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Single-center pilot study of intravitreal ranibizumab effects on microaneurysm turnover and non-perfused retinal area in NPDR with DME |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy (ranibizumab, aflibercept, conbercept) across exudative AMD, PDR, macular edema, and CNV |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring in NPDR without macular edema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT post-hoc | Ophthalmology Retina | Meta-analysis of time to DME resolution with ranibizumab by baseline DR severity |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT post-hoc (RIDE/RISE) | Clinical Ophthalmology | Predictors of early DR regression with ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | RCT post-hoc (RIDE/RISE) | Ophthalmic Surgery, Lasers & Imaging Retina | DR progression course in untreated fellow eyes |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review/Meta-analysis | Health Technology Assessment | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Overview of ranibizumab for diabetic retinopathy treatment |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Review | Journal of Diabetes and its Complications | Advances in the treatment of diabetic retinopathy |
| [20964459](https://pubmed.ncbi.nlm.nih.gov/20964459/) | 2010 | Review | Drugs | Current approaches to management of DR and diabetic macular oedema |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohort/Imaging | JAMA Ophthalmology | Retinal nonperfusion characteristics on widefield angiography in severe NPDR vs PDR |
| [36580154](https://pubmed.ncbi.nlm.nih.gov/36580154/) | 2023 | Basic/Biomarker | International Ophthalmology | Serum and vitreous VEGF levels in diabetic retinopathy |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Severe NPDR is supported by an L1 evidence level, including three completed Phase 3 RCTs (n=691, n=399, n=174) and a well-established anti-VEGF mechanistic basis; however, ranibizumab is not currently marketed in this jurisdiction and core safety/labeling data are unavailable, so guardrails are needed before advancing further.

**To proceed, the following is needed:**
- Resolve the blocking data gap (DG001): official package insert warnings/contraindications, required for safety pre-assessment (S1)
- Formal, sourced mechanism-of-action documentation (DG002), currently only inferable from repurposing rationale text
- Drug interaction (DDI) data — current query returned no results
- Regulatory registration/filing pathway assessment, since the product holds zero authorizations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

