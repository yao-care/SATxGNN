---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 6
---

# Lenalidomide
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

# Lenalidomide: From Deletion 5q Myelodysplastic Syndrome to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide is an immunomodulatory drug (IMiD) with an established approved indication in deletion 5q myelodysplastic syndrome (del(5q) MDS) in other markets, but is currently **not marketed in Saudi Arabia**. The TxGNN model predicts it may also be effective for **Myeloid Leukemia (AML)**, supported by **~50 clinical trials** (led by one completed Phase 2 RCT, NCT01358734, n=88) and **20 publications**, including one systematic review/meta-analysis. However, a **Blocking data gap** in TFDA/SFDA safety labelling currently prevents a formal safety evaluation of this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (drug not marketed in Saudi Arabia; licenses list is empty). The pack's own rank-6 candidate confirms Lenalidomide's established approved mechanism is in **del(5q) myelodysplastic syndrome**. |
| Predicted New Indication | Myeloid Leukemia (AML) |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002, High severity). However, the per-indication analysis in the evidence pack provides substantive mechanistic detail: Lenalidomide is an IMiD (immunomodulatory drug) that binds the cereblon (CRBN)–CUL4A E3 ubiquitin ligase complex, promoting degradation of IKZF1/IKZF3 and producing immunomodulatory and anti-angiogenic effects. This CRBN-dependent mechanism is the same pathway underlying Lenalidomide's approved use in del(5q) MDS, where it selectively degrades CSNK1A1 (a haploinsufficient gene on 5q31) to induce apoptosis in the del(5q) clone — an FDA/EMA-approved targeted mechanism.

Myeloid leukemia (AML) and MDS share overlapping pathophysiology — MDS frequently transforms into AML, and both are clonal myeloid stem-cell disorders. This biological continuity is the basis for the TxGNN prediction and is reflected clinically: Lenalidomide has been extensively studied in combination with hypomethylating agents (notably azacitidine) across the MDS–AML spectrum, including as induction, consolidation, and post-transplant maintenance therapy in AML.

The strongest direct evidence is a completed, randomized, open-label Phase 2 trial (NCT01358734, n=88) comparing lenalidomide-containing regimens against azacitidine alone in older adults with newly diagnosed AML, together with a 2019 systematic review/meta-analysis (PMID 31221030) evaluating azacitidine-plus-lenalidomide across AML/MDS/CMML populations. Evidence specific to AML as a standalone (non-MDS-transformed) entity remains comparatively weaker than for MDS itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Randomized, open-label comparison of lenalidomide, sequential azacitidine+lenalidomide, and azacitidine alone in older adults with newly diagnosed AML — highest-quality randomized evidence in this set. |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | Completed | 37 | Lenalidomide + azacitidine (Revlimid + Vidaza) in advanced MDS/AML; directly relevant and complete. |
| [NCT01442714](https://clinicaltrials.gov/study/NCT01442714) | Phase 2 | Terminated | 33 | Azacitidine + lenalidomide in elderly, previously-treated AML and high-risk MDS; terminated, small sample. |
| [NCT00867308](https://clinicaltrials.gov/study/NCT00867308) | Phase 2 | Terminated | 32 | High-dose lenalidomide in MDS and AML with trilineage dysplasia; terminated, limits evidence strength. |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | Completed | 51 | Sequential idarubicin + cytarabine followed by lenalidomide maintenance in MDS(RAEB-2)/untreated AML. |
| [NCT01578954](https://clinicaltrials.gov/study/NCT01578954) | Phase 1 | Completed | 20 | Dose-finding of lenalidomide as re-induction/consolidation and maintenance in AML ≥60 years after induction response. |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | Lenalidomide + MEC (mitoxantrone/etoposide/cytarabine) in relapsed/refractory AML. |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML in remission. |
| [NCT01016600](https://clinicaltrials.gov/study/NCT01016600) | Phase 1/2 | Completed | 31 | Azacitidine + lenalidomide for AML — toxicity and remission rates. |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | Completed | 48 | Lenalidomide in older, untreated AML patients without chromosome 5q abnormalities. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic Review/Meta-analysis | Hematology (Amsterdam) | Efficacy and adverse events of azacitidine + lenalidomide across AML, high-risk MDS, and CMML. |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib Trial | J Geriatric Oncology | Lenalidomide as post-remission therapy in older AML adults; safety and geriatric functional assessment. |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Cohort | Leukemia | Combination of azacitidine and lenalidomide in MDS/AML — rationale and outcomes review. |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Cohort | Haematologica | Azacitidine + lenalidomide + donor lymphocyte infusion for post-transplant relapse (Azalena trial). |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | Cohort | Frontiers in Immunology | Azacitidine + low-dose lenalidomide as relapse-prophylaxis maintenance after allo-HSCT in AML. |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematology | 2023 update on MDS diagnosis, risk stratification, and management (background context for MDS→AML). |
| [37568631](https://pubmed.ncbi.nlm.nih.gov/37568631/) | 2023 | Review | Cancers | Biology and therapeutic landscape of MDS/MPN overlap neoplasms. |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making and treatment of MDS. |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Overview of MDS pathophysiology and progression to AML. |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide as a novel treatment approach in AML. |

---

## Saudi Arabia Market Information

Currently no authorizations on record — Lenalidomide has 0 registered licenses and a market status of **未上市 (Not Marketed)** in this evidence pack.

---

## Cytotoxicity

Lenalidomide is used across hematologic malignancies (predicted indication: AML; established indication referenced in this pack: del(5q) MDS), so this section is included, though most granular toxicity data is a flagged gap (DG001, Blocking).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Immunomodulatory drug (IMiD), CRBN-E3 ligase–mediated mechanism (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/SFDA package-insert warnings and contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack, meaning a formal S1 safety pre-evaluation cannot currently be completed. No drug-drug interaction records were found (query status: not_found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and clinical evidence for AML (one completed randomized Phase 2 trial plus a systematic review, evidence level L2) are reasonably supportive, but the **Blocking** safety data gap (DG001 — no TFDA/SFDA package insert available) prevents the required S1 safety pre-evaluation, and Lenalidomide currently has zero market authorizations in Saudi Arabia. These two factors together mean the candidate cannot proceed past a Hold at this stage.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) to unblock the S1 safety evaluation (DG001)
- DrugBank-sourced mechanism of action and toxicity/myelosuppression detail (DG002)
- Clarification of local regulatory pathway, given the drug is not currently marketed in Saudi Arabia
- Additional AML-specific (rather than MDS-transformed) efficacy data to strengthen the mechanistic link beyond L2

---

*Note: This evidence pack also scored five other candidate indications for Lenalidomide. Notably, rank 6 ("partial deletion of the long arm of chromosome 5," L1, two trials including a completed Phase 3 RCT) corresponds to Lenalidomide's already-established del(5q) MDS mechanism rather than a genuinely new indication. Ranks 4–5 (aregenerative anemia; congenital sideroblastic anemia) were assessed as Hold — likely ontology-mapping noise or mechanistically unrelated to Lenalidomide's confirmed CRBN pathway.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

