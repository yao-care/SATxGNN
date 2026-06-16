---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

# Duvelisib: From CLL/SLL to Hodgkin's Lymphoma

## One-Sentence Summary

Duvelisib (Copiktra) is an FDA-approved oral dual inhibitor of PI3K-δ and PI3K-γ, originally indicated for relapsed/refractory chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) and follicular lymphoma, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma**, with **11 clinical trials** and **16 publications** retrieved in evidence search — the majority of which pertain to related non-Hodgkin's lymphoma subtypes rather than classical Hodgkin's lymphoma specifically.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory CLL/SLL and follicular lymphoma (FDA-approved 2018; not registered in Saudi Arabia) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Duvelisib is the first FDA-approved oral dual inhibitor of phosphatidylinositol-3-kinase delta (PI3K-δ) and gamma (PI3K-γ). PI3K-δ is selectively and highly expressed in hematopoietic cells and serves as a critical downstream mediator of B-cell receptor (BCR) signaling, driving proliferation, survival, and tissue homing of malignant B cells. PI3K-γ acts within the tumor microenvironment, promoting immunosuppressive conditions by sustaining regulatory T cells (Tregs) and myeloid-derived suppressor cells (MDSCs). The dual inhibition strategy simultaneously targets tumor cell intrinsic survival signaling and the immunosuppressive milieu — a mechanistic profile with broad relevance across lymphoid malignancies.

Hodgkin's lymphoma (HL) is characterized by rare malignant Reed-Sternberg (RS) cells of germinal center B-cell origin, embedded in an extensive immunosuppressive inflammatory infiltrate. The PI3K/AKT/mTOR pathway is constitutively activated in RS cells and contributes to their survival and immune evasion. In approximately 40% of classical HL cases, RS cells harbor Epstein-Barr virus (EBV), which activates PI3K signaling as part of its oncogenic program. Preclinical evidence demonstrates that duvelisib has antitumor activity in EBV-associated B-cell lymphoma models (PMID 29522278, included in the B-cell neoplasm evidence set), providing a mechanistic bridge from the established hematologic indications to HL.

However, a critical caveat must be stated: **all 11 clinical trials retrieved under the Hodgkin's lymphoma query are for non-Hodgkin's lymphoma (NHL) subtypes** — including indolent NHL (follicular lymphoma, marginal zone lymphoma, SLL), T-cell lymphoma, and CLL — not classical Hodgkin's lymphoma. No dedicated clinical trials of duvelisib specifically in HL have been identified. The TxGNN prediction likely reflects shared lymphoid biology and PI3K pathway activation across the lymphoma spectrum, but the clinical translational gap from NHL/CLL to HL remains undemonstrated. Additionally, duvelisib was voluntarily withdrawn from the US market in 2023 for commercial reasons, affecting global supply.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Duvelisib monotherapy in refractory indolent NHL (follicular lymphoma, MZL, SLL); evaluated safety and efficacy in patients refractory to rituximab and prior chemo or radioimmunotherapy |
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Randomized comparison of two intermittent duvelisib dosing schedules in iNHL; assessed whether 2-week dose holidays reduce toxicity while maintaining tumor response |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Duvelisib in combination with BMS-986345 in lymphoid malignancy; dose escalation safety and tolerability study |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | IPI-145 (duvelisib) combined with rituximab or bendamustine/rituximab in relapsed/refractory lymphoma and CLL; characterized MTD and preliminary efficacy profile |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Duvelisib following CAR-T cell therapy in B-cell malignancies; hypothesis that PI3K inhibition enhances CAR-T persistence by promoting less-exhausted T-cell phenotypes |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Randomized study of CHO(E)P vs duvelisib-CHO(E)P vs CC-486-CHO(E)P in untreated CD30-negative peripheral T-cell lymphomas; currently suspended |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A | Not yet recruiting | 200 | CHANT: multicenter non-interventional real-world prospective study of duvelisib in NHL; efficacy and safety in routine clinical practice |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | YY-20394 (a separate PI3K-δ inhibitor, not duvelisib) in relapsed/refractory follicular NHL; indirect class reference only |
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Withdrawn | 0 | Duvelisib + bendamustine/rituximab vs placebo + BR in previously-treated iNHL; withdrawn before enrollment began |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Duvelisib + acalabrutinib (DUAL Trial) in relapsed/refractory iNHL; withdrawn before enrollment |

> ⚠️ **Important**: All trials above are for non-Hodgkin's lymphoma, CLL/SLL, or T-cell lymphoma. None specifically target classical Hodgkin's lymphoma.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic Review & Meta-analysis | Frontiers in Immunology | Pooled safety and efficacy analysis of duvelisib across prospective trials in relapsed/refractory lymphoid neoplasms; quantified response rates and grade 3–4 toxicity profiles |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 Trial | Blood | Phase 1 dose-escalation study in 210 patients with advanced hematologic malignancies; MTD 75 mg BID; clinical activity observed across NHL, CLL, and T-cell lymphoma subtypes |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Phase 1 Trial | American Journal of Hematology | Combination trial of duvelisib with rituximab or BR in relapsed/refractory NHL and CLL; evaluated response rates and remission durability of the combination strategy |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Clinical Commentary | The Lancet Oncology | Expert commentary on the clinical significance of duvelisib approval and activity in indolent NHL |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Current Treatment Options in Oncology | Comprehensive review of PI3K inhibitor mechanisms, clinical efficacy across NHL subtypes, and on-target immune-mediated toxicities |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | American Journal of Health-System Pharmacy | Summary of approved targeted therapies in B- and T-cell lymphomas, including duvelisib's regulatory approval context |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Novel therapeutic approaches to follicular lymphoma with focus on PI3K inhibitors and emerging combination strategies |
| [33132100](https://pubmed.ncbi.nlm.nih.gov/33132100/) | 2021 | Review | Clinical Lymphoma, Myeloma & Leukemia | Next-generation PI3K inhibitors for relapsed/refractory NHL; discussed approaches to reduce toxicity while maintaining efficacy |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical | Scientific Reports | Demonstrated PI3Kγ and PI3Kδ roles in mantle cell lymphoma cell proliferation and migration; duvelisib showed preclinical efficacy in lymph-node-resident MCL models |
| [41920459](https://pubmed.ncbi.nlm.nih.gov/41920459/) | 2026 | Review | American Journal of Clinical Dermatology | Emerging therapies in cutaneous T-cell lymphoma including PI3K inhibition; provides context on the broader lymphoma application landscape |

## Saudi Arabia Market Information

Duvelisib is **not registered in Saudi Arabia**. No marketing authorizations have been issued. The drug is currently unavailable through licensed commercial channels in the Kingdom.

> For reference: Duvelisib (brand name Copiktra) was approved by the US FDA in September 2018 for relapsed/refractory CLL/SLL (after ≥2 prior therapies) and received accelerated approval for follicular lymphoma (after ≥2 prior systemic therapies). The manufacturer voluntarily withdrew the product from the US market in 2023 for commercial reasons unrelated to new safety signals.

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — PI3K-δ/γ dual inhibitor (small molecule kinase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Moderate — neutropenia is the most common hematologic toxicity; thrombocytopenia reported at lower frequency |
| Emetogenicity Classification | Low (oral targeted agent; not classified as a conventional emetogenic chemotherapy) |
| Monitoring Items | CBC with differential (neutropenia), ALT/AST (hepatotoxicity), pulmonary symptoms (pneumonitis/pneumonia), stool frequency and consistency (immune-mediated colitis), skin examination (rash) |
| Handling Protection | Standard antineoplastic oral agent precautions apply; healthcare providers should follow institutional cytotoxic drug handling protocols |

## Safety Considerations

Please refer to the package insert for safety information.

> Based on published clinical trial data, duvelisib carries class-specific immune-mediated toxicities including pneumonitis/Pneumocystis pneumonia (requiring prophylaxis), immune-mediated colitis/diarrhea (the leading cause of dose reduction and discontinuation), skin rash, and neutropenia. Infectious complications — particularly opportunistic infections — are a clinically significant concern. These toxicities contributed to limitations on duvelisib's use even in its approved indications, where better-tolerated alternatives (ibrutinib, venetoclax) became preferred.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although duvelisib has a mechanistically plausible connection to Hodgkin's lymphoma via PI3K pathway activation in Reed-Sternberg cells and EBV-associated oncogenesis, no clinical trials specifically addressing HL with duvelisib have been identified. The retrieved evidence base is entirely from non-Hodgkin's lymphoma subtypes, representing an unvalidated clinical extrapolation. The 2023 US market withdrawal further restricts commercial supply and limits the practical pathway for clinical investigation.

**To proceed, the following is needed:**
- Dedicated preclinical studies confirming duvelisib activity in classical Hodgkin's lymphoma cell lines or patient-derived xenograft models
- Review of PI3K inhibitor class evidence in HL (e.g., idelalisib or copanlisib, which remain available) to establish class-level proof-of-concept before committing to duvelisib specifically
- Assessment of supply chain feasibility given the 2023 voluntary US market withdrawal — identify whether duvelisib is accessible through named-patient programs, compassionate use, or alternative manufacturers
- Acquisition of full safety data: SFDA package insert review (currently a data gap) and assessment of the pneumonitis and colitis risk profile in the intended HL patient population
- Determination of whether a dedicated Phase 1/2 basket trial or HL-specific expansion cohort can be designed using available drug supply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

