---
layout: default
title: Lifitegrast
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 6
---

# Lifitegrast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lifitegrast: From an LFA-1 Antagonist to Diabetic Retinopathy

*Note on candidate selection: this evidence pack contains 6 TxGNN-predicted indications for lifitegrast. The five highest-scoring candidates (penile, palmar, plantar, and infantile digital fibromatosis; severe nonproliferative diabetic retinopathy) are pure model output — evidence_level L5, zero clinical trials or literature, recommendation "Hold." Only **diabetic retinopathy** (rank 6) has actual supporting evidence, so this report focuses on that indication.*

---

## One-Sentence Summary

> Lifitegrast is an LFA-1 (integrin αLβ2) antagonist developed for inflammatory ocular surface disease; this evidence pack does not contain confirmed local (Taiwan) regulatory data on its original approved indication, as the drug is not currently marketed here.
> The TxGNN model predicts it may be effective for **Diabetic Retinopathy**, supported by **1 completed clinical trial** and **2 publications**, including direct Phase 1b safety/PK data on lifitegrast's precursor compound (SAR 1118) in a related retinal disease.
> Evidence is early-stage (L2) — sufficient to justify further targeted investigation, not yet to support a go decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (`original_indications` and `original_moa` are flagged as data gaps; drug is not locally marketed) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is flagged as a data gap in this pack (`DG002`, severity High). Based on information available elsewhere in the evidence pack, lifitegrast is an antagonist of lymphocyte function-associated antigen-1 (LFA-1, integrin αLβ2), which blocks the LFA-1/ICAM-1 interaction that mediates leukocyte adhesion. This is the mechanism cited directly in the literature evidence below (PMID 22538219), which studied lifitegrast under its earlier development code, SAR 1118.

Diabetic retinopathy involves leukostasis — leukocytes adhering to retinal microvascular endothelium via LFA-1/ICAM-1, contributing to capillary occlusion and endothelial injury. Blocking this pathway is therefore mechanistically plausible as an anti-inflammatory strategy for the disease. Notably, this is not a purely theoretical extrapolation: SAR 1118 was directly investigated as a topical treatment in diabetic macular oedema (a closely related diabetic retinal disease) in a Phase 1b safety/PK study, which provides direct pharmacological precedent — though not yet direct efficacy evidence — for use in diabetic retinopathy specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04030962](https://clinicaltrials.gov/study/NCT04030962) | Phase 1/Phase 2 | Completed | 292 | Two-stage, multicenter, vehicle-controlled, double-masked RCT evaluating safety, tolerability, PK, and exploratory efficacy of AGN-242428 and AGN-231868 in dry eye disease. Flagged as "Grade A" relevance in the source data, but note: the trial title lists different compounds (AGN-242428/AGN-231868) and a different indication (dry eye disease) than lifitegrast/diabetic retinopathy — this mismatch should be verified before relying on this trial as direct evidence. No efficacy outcome data reported. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22538219](https://pubmed.ncbi.nlm.nih.gov/22538219/) | 2012 | RCT | Eye (London, England) | Phase 1b study of topical SAR 1118 (lifitegrast), an LFA-1 antagonist; evaluated safety, tolerability, and PK. Cites LFA-1/ICAM-1-mediated inflammation as a driver of diabetic macular oedema pathogenesis — direct mechanistic and pharmacological precedent for retinal disease use. |
| [41158172](https://pubmed.ncbi.nlm.nih.gov/41158172/) | 2025 | Review | International Journal of Ophthalmology | Proteome-wide Mendelian randomization study identifying novel protein and drug targets for retinal neurodegenerative diseases in European populations. General target-discovery context rather than lifitegrast-specific evidence. |

---

## Taiwan Market Information

Lifitegrast is not currently marketed in Taiwan (0 authorizations on file). No local product license or approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack does not contain confirmed data on key warnings, contraindications, or drug-drug interactions for lifitegrast (`DG001`, severity Blocking — TFDA package insert data not yet obtained).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (LFA-1/ICAM-1-mediated leukostasis in diabetic retinopathy, with direct precedent from a related retinal disease) is credible, but the evidence base is early-stage (L2) and thin — one completed trial of uncertain relevance (drug/indication mismatch to verify) and no lifitegrast-specific efficacy data in diabetic retinopathy itself. This supports further investigation, not a market decision.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed original mechanism-of-action and original approved indication data for lifitegrast
- Verification of whether NCT04030962 is genuinely relevant to lifitegrast (the listed compounds differ from the drug under evaluation)
- A lifitegrast-specific efficacy trial in diabetic retinopathy or diabetic macular oedema
- Drug interaction and contraindication data before any safety pre-screen (S1) can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

