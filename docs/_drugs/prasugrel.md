---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Antiplatelet Therapy after Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine-class P2Y12 antiplatelet agent used in dual antiplatelet therapy following acute coronary syndrome (ACS) and PCI. The TxGNN model predicts a possible link to **Pulmonary Hypertension** with a very high score (99.88%), but the retrieved **2 clinical trials** and **2 publications** are both graded low relevance and do not directly support this indication — this is flagged in the evidence pack itself as a likely score/evidence mismatch.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiplatelet therapy following acute coronary syndrome (ACS) managed with PCI (drug not marketed in Saudi Arabia — no local label text available; inferred from background context in retrieved literature) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prasugrel is a thienopyridine-class P2Y12 receptor antagonist used as part of dual antiplatelet therapy; its efficacy in reducing thrombotic cardiovascular events after ACS/PCI has been established. Mechanistically, one could hypothesize that platelet activation and release of serotonin/thromboxane — factors with a theoretical role in pulmonary hypertension (PH) pathophysiology — might be modulated by antiplatelet therapy, providing a loose rationale for the TxGNN association.

However, the evidence retrieved for this candidate does not support the prediction. Both clinical trials returned (cancer-associated thrombosis eligibility criteria; NOAC management in elderly atrial fibrillation) were graded **C (low relevance)** and have no direct bearing on PH or prasugrel's antiplatelet mechanism. Both literature items (a COVID-19 comorbidity registry analysis and a study of clopidogrel/prasugrel adherence after PCI) likewise do not address PH.

The evidence pack's own repurposing rationale explicitly characterizes this as a case where the TxGNN score and the retrieved evidence content do not match — the mechanistic link is theoretical only, with no direct study of prasugrel in PH.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility criteria for cancer-associated venous thromboembolism trials; not related to PH or prasugrel (relevance grade C) |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Cross-sectional observational study of NOAC management in elderly atrial fibrillation patients in Spain; not a PH or antiplatelet drug study (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | ACTIV COVID-19 registry analysis of background comorbidity therapy effects on COVID-19 outcome severity; not specific to PH or prasugrel |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Factors associated with clopidogrel/prasugrel adherence after PCI in ACS patients; confirms prasugrel's established ACS/PCI use but does not address PH |

---

## Saudi Arabia Market Information

Prasugrel is currently not marketed in Saudi Arabia (0 authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the TFDA package insert/label data required for initial safety screening (S1) is currently a blocking data gap, and MOA data is a high-priority gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, none of the retrieved clinical trials or literature directly support prasugrel's use in pulmonary hypertension — all evidence items are graded low relevance, and the evidence pack itself identifies this as a likely score/content mismatch. Combined with a blocking data gap in TFDA label/safety data (DG001) and a high-priority gap in MOA data (DG002), this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking
- Mechanism of action data via DrugBank API
- Targeted preclinical or mechanistic studies linking P2Y12 inhibition to pulmonary vascular remodeling/thrombosis
- PH-specific clinical trials or case series involving prasugrel

*For reference: among the other candidates in this evidence pack, migraine disorder (rank 2, L3, decision stage S1, "Research Question") has comparatively stronger class-level human evidence — thienopyridines (clopidogrel/prasugrel) and PFO-associated migraine — and may warrant separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

