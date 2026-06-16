---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide: From Broad-Spectrum Alkylating Chemotherapy to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is a classical nitrogen mustard alkylating agent used globally across oncology and immunology settings, though it holds no current SFDA registration in Saudi Arabia.
The TxGNN model predicts it may be particularly effective for **Myeloid Leukemia** — spanning both myeloablative conditioning for allogeneic HSCT and post-transplant GVHD prevention —
with **multiple completed Phase 2/3 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SFDA-approved indication on record (not currently marketed in Saudi Arabia) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record retrieved for this analysis. Based on known clinical information, cyclophosphamide is an alkylating agent (nitrogen mustard class) whose active metabolites — primarily 4-hydroxycyclophosphamide and phosphoramide mustard — form DNA inter- and intra-strand crosslinks, triggering apoptosis in rapidly proliferating cells such as leukemic blasts. At myeloablative doses it eliminates residual disease and creates marrow space for donor engraftment; at lower doses it selectively depletes proliferating alloreactive T cells while sparing quiescent regulatory T cells (Tregs).

Myeloid leukemia involves clonal expansion of malignant myeloid progenitors in the bone marrow. Cyclophosphamide's myeloablative properties have made it a cornerstone of conditioning regimens for allogeneic HSCT in AML: the BuCy (busulfan + cyclophosphamide) protocol has been a reference-standard myeloablative conditioning regimen for decades, and remains in active use as shown by Phase 3 data (NCT01191957, n=252). A completed Phase 3 trial also demonstrated its role in high-dose intensification prior to autologous SCT in adult myeloid leukemia (NCT00002945).

A second, more contemporary mechanistic rationale centers on post-transplant cyclophosphamide (PTCy): administered at 50 mg/kg on days +3 and +4 following allo-HSCT, PTCy eliminates alloreactive T cells that have proliferated in response to donor-host MHC mismatches, thereby preventing graft-versus-host disease (GVHD) while preserving graft-versus-leukemia (GVL) activity. PTCy has emerged as the preferred GVHD prophylaxis strategy across haploidentical, matched-related, and matched-unrelated donor settings in AML, accumulating registry-level cohort evidence exceeding 1,800 patients (PMID 39939431). The TxGNN prediction is therefore strongly supported by both mechanistic plausibility and clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01191957](https://clinicaltrials.gov/study/NCT01191957) | Phase 3 | Completed | 252 | Prospective randomized comparison of IV BuFlu vs BuCy2 as conditioning for AML patients ≥40 years in complete remission undergoing allo-HSCT; primary endpoints transplant-related mortality at 1 year and anti-leukemic efficacy — the pivotal dataset for Cy-based conditioning in older AML |
| [NCT00002945](https://clinicaltrials.gov/study/NCT00002945) | Phase 3 | Completed | 61 | High-dose cytarabine + idarubicin induction followed by high-dose etoposide + cyclophosphamide intensification, autologous SCT, and IL-2 immune modulation in previously untreated adult myeloid leukemia; evaluates Cy as a key intensification component |
| [NCT00003868](https://clinicaltrials.gov/study/NCT00003868) | Phase 2 | Completed | 40 | Radiolabeled BC8 (anti-CD45) antibody combined with cyclophosphamide and TBI followed by HLA-matched related or unrelated HSCT in advanced AML and MDS; directly tests Cy as part of targeted radioimmuno-conditioning, with long-term survival data |
| [NCT00005892](https://clinicaltrials.gov/study/NCT00005892) | N/A | Completed | N/A | Moderate-dose cyclophosphamide plus radiotherapy before allogeneic BMT in AML and MDS related to Fanconi's anemia; determines whether dose-attenuated Cy-containing conditioning can reduce morbidity while maintaining efficacy |
| [NCT07108530](https://clinicaltrials.gov/study/NCT07108530) | Phase 2 | Recruiting | 50 | Multicenter single-arm study evaluating an integrated induction-consolidation-transplantation protocol in adult AML (excluding M3 subtype); two modern induction options (IAV and DAV regimens), representing current standard-of-care transplant trajectory |
| [NCT03602898](https://clinicaltrials.gov/study/NCT03602898) | Phase 2 | Withdrawn | 0 | Randomized design comparing ATG vs post-transplant cyclophosphamide (PTCy) vs calcineurin inhibitor + methotrexate as GVHD prophylaxis after myeloablative unrelated donor PBSC transplantation; withdrawn before enrolment, but the scientific question remains clinically active and unanswered |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cyclophosphamide/fludarabine/TBI myeloablative preparative regimen for unrelated umbilical cord blood transplantation in hematological malignancies including myeloid leukemia; largest UCB-conditioning dataset with explicit Cy dosing |
| [NCT00852709](https://clinicaltrials.gov/study/NCT00852709) | Phase 1 | Terminated | 35 | Dose-escalation study of clofarabine followed by escalating fractionated cyclophosphamide in children with relapsed or refractory acute leukemias; provides MTD and safety data for Cy in the pediatric leukemia context |
| [NCT01338987](https://clinicaltrials.gov/study/NCT01338987) | Phase 2 | Completed | 76 | Lupron to enhance lymphocyte immune reconstitution following allogeneic BMT (Cy as preparative regimen component); 9-year enrolment period with molecular imaging evaluation, offering long-term safety and immune reconstitution data |
| [NCT04835519](https://clinicaltrials.gov/study/NCT04835519) | Phase 1/2 | Completed | 5 | CD33 CAR-T cells in relapsed/refractory AML; cyclophosphamide (250 mg/m²) used as lymphodepletion pretreatment alongside fludarabine, confirming its enabling role for next-generation cellular immunotherapy in AML |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic Review / NMA | Bone Marrow Transplantation | Bayesian network meta-analysis of myeloablative conditioning regimens for AML undergoing allo-HSCT in complete remission; Bu/Cy (oral 16 mg/kg or IV 12.8 mg/kg) benchmarked against all major alternatives — defines relative efficacy and toxicity positioning |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective Cohort | Bone Marrow Transplantation | 1,823 AML patients in CR1 receiving first allo-HSCT with PTCy; analyzed impact of conditioning intensity stratified by cytogenetic/molecular risk — largest published PTCy dataset in AML to date |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort / Registry | Haematologica | 217 AML patients receiving MAC + PTCy-based GVHD prophylaxis; 2-year OS 77%, EFS 72%; assesses prognostic significance of ELN 2022 genetic risk categories in the PTCy era |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Retrospective Cohort | European Journal of Haematology | MAC vs RIC conditioning in AML patients <65 years receiving ATG + PTCy-based GVHD prophylaxis; demonstrates that conditioning intensity modulation within a PTCy backbone impacts disease control without proportional toxicity increase |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Prospective Phase 2 | Transplant Immunology | Cladribine + BuCy as intensive conditioning prior to allo-HSCT in relapsed/refractory AML; directly evaluates an augmented Cy-containing conditioning regimen for the most difficult-to-treat AML patients |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Retrospective Cohort | Future Oncology | Head-to-head comparison of BuCy vs FluBu myeloablative conditioning for allo-HSCT in AML; confirms BuCy as an active comparator with similar efficacy and a distinct toxicity profile |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Retrospective Cohort | Cytotherapy | Prognostic factors in haploidentical HSCT with PTCy for AML; identifies disease status, donor-recipient CMV serostatus, and conditioning intensity as key outcome predictors in the PTCy paradigm |
| [32428903](https://pubmed.ncbi.nlm.nih.gov/32428903/) | 2021 | Retrospective Cohort | Acta Haematologica | PTCy (50 mg/kg, days +3/+4) + ATG (4.5 mg/kg) as GVHD prophylaxis for high-risk AML and MDS undergoing allo-HCT; compared to alternative prophylaxis regimens, demonstrating the combination's feasibility in very high-risk disease |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Retrospective Series | Leukemia & Lymphoma | High-dose cyclophosphamide (HDCy, 60 mg/kg) as emergency cytoreduction in 27 AML patients with hyperleukocytosis or leukostasis; demonstrates direct anti-leukemic efficacy outside the transplant setting |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Retrospective Cohort | Int'l J Molecular Sciences | PTCy as GVHD prophylaxis in pediatric AML after matched related and unrelated donor HSCT; first published pediatric AML dataset in this context, addressing an important gap in the evidence base |

---

## Saudi Arabia Market Information

Cyclophosphamide is currently not registered with the Saudi Food and Drug Authority (SFDA). No product licenses, approved dosage forms, or approved indications are on record. Formal market authorization would be required before clinical use under Saudi Arabia regulatory jurisdiction.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High — leukopenia, thrombocytopenia, and anemia are expected dose-dependent effects; nadir typically occurs 8–14 days post-administration; high-dose regimens used in AML conditioning carry severe myeloablation by design |
| Emetogenicity Classification | Moderate (standard doses) to High (high-dose conditioning ≥600 mg/m²); prophylactic anti-emetic regimens including NK1-receptor antagonists are required at conditioning doses |
| Monitoring Items | CBC with differential (daily during conditioning, then per protocol), serum creatinine and LFTs, urinalysis and urine microscopy (hemorrhagic cystitis surveillance), electrolytes, and SIADH monitoring at high doses |
| Handling Protection | Required — cytotoxic drug handling protocols mandatory, including closed-system drug transfer devices, biological safety cabinet preparation, and appropriate PPE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide's role in myeloid leukemia is supported by decades of clinical evidence, including completed Phase 3 randomized trials of BuCy conditioning in AML (n=252), prospective Phase 2 data in relapsed/refractory AML, and registry-scale retrospective cohorts encompassing over 1,800 AML patients receiving PTCy-based GVHD prophylaxis. The mechanistic rationale — myeloablation of leukemic blasts and selective elimination of alloreactive T cells — is well-characterized in the transplant literature. The TxGNN prediction at 99.47% is consistent with this established body of evidence.

**To proceed, the following is needed:**
- Saudi Arabia SFDA registration pathway assessment and market access strategy for an unregistered cytotoxic agent
- Formal package insert (SmPC) retrieval to document official warnings, contraindications, and drug-drug interactions
- DrugBank MOA record completion to support regulatory submission documentation
- Mesna co-administration protocol specification for hemorrhagic cystitis prevention in high-dose conditioning regimens
- Mapping to local Saudi Arabia AML transplant practice guidelines to identify the specific clinical niche (BuCy conditioning vs. PTCy GVHD prophylaxis) where registration adds greatest value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

