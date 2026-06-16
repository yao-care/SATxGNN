---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab: From Bone Loss Prevention to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody targeting RANKL, used clinically for the prevention of bone loss associated with osteoporosis and androgen deprivation therapy. The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (severe NPDR)**, with a prediction score of 99.63% — however, **no clinical trials** and **no direct publications** currently support this specific indication, placing this prediction at the earliest evidence stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bone loss prevention (osteoporosis; androgen deprivation therapy-related bone loss in prostate cancer) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Denosumab is a RANKL (Receptor Activator of Nuclear Factor Kappa-B Ligand) inhibitor. By binding RANKL, it prevents osteoclast activation and bone resorption — the mechanism underlying its bone-protective indications. Notably, RANKL signaling is not confined to bone: it has been detected in retinal vascular pericytes and Müller glial cells, raising the hypothesis that Denosumab could attenuate retinal microvascular inflammation through the same pathway.

The proposed link to diabetic retinopathy rests on three indirect mechanistic pathways. First, a 2024 real-world cohort study with meta-analysis (PMID 38899553) found that Denosumab reduces the incidence of type 2 diabetes compared with bisphosphonates, suggesting a metabolic benefit that could indirectly lower cumulative diabetic retinopathy risk. Second, RANKL may promote retinal microvascular inflammation and contribute to new vessel formation in the diabetic retina — blocking it could theoretically slow disease progression. Third, the OPG/RANKL ratio imbalance has been proposed as a shared pathophysiological factor linking diabetic bone loss to diabetic retinopathy severity.

It is essential to underscore that all of these pathways remain mechanistic hypotheses with no direct clinical validation for severe NPDR. The TxGNN prediction score of 99.63% reflects graph-network inference based on molecular similarity and disease-network topology — a strong computational signal, but not a substitute for clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

> **Contextual note:** One Phase 3 trial was retrieved for the related indication "diabetic retinopathy" (Rank 2):
>
> | Trial Number | Phase | Status | Enrollment | Key Findings |
> |-------------|-------|--------|------------|--------------|
> | [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Examined **lens opacification (cataract)** as a safety endpoint in prostate cancer patients on androgen deprivation therapy receiving Denosumab — not a diabetic retinopathy efficacy trial. Relevance grade: C (low). Cannot serve as evidence for the DR repurposing hypothesis. |

---

## Literature Evidence

Currently no related literature directly studying Denosumab in severe nonproliferative diabetic retinopathy.

> **Contextual note:** Two publications retrieved for the broader "diabetic retinopathy" indication (Rank 2) provide indirect biological context:
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observational Cohort + Meta-analysis | Diabetes, Obesity & Metabolism | Denosumab reduces T2D incidence and long-term microvascular complications (including retinopathy) compared with bisphosphonates in real-world data — supports the indirect metabolic pathway hypothesis |
> | [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cross-sectional | Cureus | FRAX fracture risk assessment in T2DM adults; highlights bone-diabetes comorbidity but does not study Denosumab specifically — background context only |

---

## Saudi Arabia Market Information

Denosumab is not currently registered or marketed in Saudi Arabia. No authorization records are available in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. The package insert query (log entry 4) returned a record, but content was not transmitted into this pack. Full safety review is required before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a biologically plausible mechanistic hypothesis linking Denosumab's RANKL-inhibiting mechanism to retinal microvascular pathology in severe NPDR — but there is currently zero direct clinical evidence (no trials, no publications) for this specific indication. With Evidence Level L5 and no Saudi Arabia market footprint, this candidate cannot advance until foundational data gaps are closed.

**To proceed, the following is needed:**

- Retrieve the full package insert content to complete the safety profile (warnings, contraindications, key drug interactions)
- Confirm Denosumab's complete mechanism of action from DrugBank to validate the RANKL–retinal vascular connection
- Commission a structured literature review on RANKL/OPG signaling specifically in diabetic retinal tissue and animal models
- Consider whether the broader **diabetic retinopathy** indication (Rank 2, Evidence Level L4, "Research Question" stage) should be evaluated first as an evidence-building stepping stone
- Clarify route-of-administration compatibility: Denosumab is a subcutaneous injection — suitability and dosing rationale for a retinal indication requires separate pharmacokinetic analysis
- If preclinical evidence is favorable, design a Phase 2 exploratory trial in collaboration with ophthalmology to generate direct efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

