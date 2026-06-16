---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# BUSULFAN: From Chronic Myelogenous Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically used as conditioning therapy before allogeneic hematopoietic stem cell transplantation (HSCT) in leukemia and other hematologic malignancies.
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myelogenous leukemia (CML); HSCT conditioning for hematologic malignancies (global approvals; no SFDA registration) |
| Predicted New Indication | Myelodysplastic Syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured database. Based on known information, busulfan is a bifunctional alkylating agent that exerts its effect through DNA cross-linking, causing irreversible inhibition of rapidly proliferating cells — particularly hematopoietic progenitor cells. This myeloablative property forms the mechanistic basis for its decades-long role as conditioning therapy before allogeneic HSCT. The drug's efficacy in eliminating abnormal hematopoietic clones in leukemia is well established, and this mechanism is directly applicable to MDS.

In MDS, the core pathology involves clonal abnormalities in hematopoietic stem cells resulting in ineffective hematopoiesis and progressive risk of leukemic transformation. Busulfan's myeloablative action eliminates these abnormal hematopoietic clones and creates the necessary engraftment space for donor cells in allogeneic HSCT. Intravenous busulfan combined with fludarabine (Bu/Flu regimen) has become one of the standard conditioning approaches for MDS patients undergoing HSCT, achieving effective clearance of abnormal clones with manageable toxicity — and this is explicitly reflected in the mechanistic link described for this indication.

Both the original application (leukemia) and the predicted new indication (MDS) are clonal hematopoietic disorders where myeloablation is the therapeutic rationale. This mechanistic overlap is reinforced by four Phase 3 randomized controlled trials in the literature directly studying busulfan-based conditioning in MDS, along with more than 50 clinical trials across multiple HSCT platforms, together justifying the L1 evidence classification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Phase 2 | Recruiting | 220 | Direct RCT comparing benadamustine vs ruxolitinib added to fludarabine/busulfan conditioning for haploidentical HSCT in MDS/myelofibrosis; the most current randomized evidence with busulfan as the core conditioning backbone |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax + timed sequential busulfan + cladribine + fludarabine before allogeneic HSCT for AML and MDS; directly and prospectively tests busulfan as the core drug in MDS conditioning |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Completed | 30 | Clofarabine + IV busulfan + thymoglobulin (CBT) reduced-intensity conditioning prior to HSCT for high-risk AML, MDS, or ALL; demonstrated anti-tumor efficacy with manageable toxicity |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Phase 2 | Completed | 35 | Fludarabine + busulfan + alemtuzumab reduced-toxicity conditioning for children with stem cell defects, marrow failure, or MDS undergoing allogeneic HSCT |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Completed | 120 | Allogeneic sibling and unrelated donor HCT with busulfan + etoposide + cyclophosphamide for MDS and myeloproliferative disorders; assessed tolerability and efficacy in patients aged 51–60 |
| [NCT02221310](https://clinicaltrials.gov/study/NCT02221310) | Phase 2 | Completed | 25 | Gemtuzumab ozogamicin + busulfan + cyclophosphamide followed by allogeneic HSCT for high-risk AML and MDS; evaluated targeted immunochemotherapy combined with busulfan myeloablation |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | Completed | 34 | Reduced-intensity conditioning with busulfan/clofarabine prior to allogeneic HSCT; tested novel busulfan-based combination in MDS and AML setting |
| [NCT02626715](https://clinicaltrials.gov/study/NCT02626715) | Phase 2 | Completed | 21 | Myeloablative vs reduced-intensity conditioning for children and young adults with AML/MDS undergoing HSCT; compared two busulfan-based conditioning regimens for toxicity and efficacy |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | N/A | Completed | 30 | Non-T-cell depleted HLA-haploidentical familial donor HSCT after reduced-intensity busulfan conditioning; provided important safety data for busulfan RIC in MDS and bone marrow failure |
| [NCT05027945](https://clinicaltrials.gov/study/NCT05027945) | Phase 2 | Recruiting | 54 | Allogeneic HSCT for VEXAS syndrome, which shares MDS-like clonal bone marrow abnormalities; busulfan-containing conditioning regimen used to achieve myeloablation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT | The Lancet Haematology | Phase 3 open-label multicenter RCT: G-CSF + decitabine added to busulfan-cyclophosphamide conditioning significantly reduced relapse vs busulfan-cyclophosphamide alone in MDS-RAEB and secondary AML undergoing allogeneic HSCT |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | The Lancet Haematology | MC-FludT.14/L trial: treosulfan-fludarabine was non-inferior to reduced-intensity busulfan-fludarabine in older or comorbid AML/MDS patients; validated busulfan-flu as the reference standard comparator |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT (Phase 3, final analysis) | American Journal of Hematology | Final analysis of 476-patient Phase 3 RCT showing treosulfan non-inferior to reduced-intensity busulfan for event-free survival in older AML/MDS patients undergoing allogeneic HCT |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase III RCT | Journal of Clinical Oncology | BMT CTN Phase III randomized trial comparing myeloablative (including busulfan-based) vs reduced-intensity conditioning in AML and MDS patients undergoing allogeneic HCT; found comparable OS with different toxicity-relapse tradeoffs |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Contemporary review of allogeneic HSCT for MDS and myelofibrosis; confirms busulfan-based conditioning regimens as central to curative treatment strategy for eligible higher-risk MDS patients |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review & Meta-analysis | Frontiers in Oncology | Systematic review and meta-analysis comparing treosulfan- vs busulfan-based conditioning for MDS/AML before allogeneic HCT; pooled analysis of long-term outcomes and toxicity |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective Cohort | Transplantation and Cellular Therapy | Myeloablative busulfan + fludarabine with in vivo T-cell depletion shown safe and effective for AML and MDS patients undergoing allogeneic HSCT regardless of age or HCT-CI score |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Retrospective Cohort | Transplantation and Cellular Therapy | Single-center propensity score-matched comparison of treosulfan- vs busulfan-based conditioning in 138 MDS patients at Princess Margaret Hospital (2015–2022) |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Retrospective Cohort | Bone Marrow Transplantation | Nationwide Japanese registry analysis (2006–2018): fludarabine/busulfan (Flu/Bu4) vs busulfan/cyclophosphamide (Bu4/Cy) myeloablative conditioning specifically for MDS patients |
| [38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/) | 2024 | Retrospective Cohort | Transplantation and Cellular Therapy | Italian pediatric multicenter study assessing long-term toxicities (growth, gonadal, thyroid, cardiac) after HSCT with treosulfan- or busulfan-based conditioning in children with acute leukemia or MDS |

---

## Saudi Arabia Market Information

Busulfan currently has no registered product authorizations with the Saudi Food and Drug Authority (SFDA). The drug is not marketed in Saudi Arabia. Any clinical use would require import authorization or regulatory submission through SFDA.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Bifunctional alkylating agent (busulfan class; cell-cycle non-specific) |
| Myelosuppression Risk | **High** — Myelosuppression is the intended pharmacological mechanism; complete bone marrow ablation is the therapeutic goal in HSCT conditioning. Universal and severe pancytopenia (neutropenia, thrombocytopenia, anemia) occurs following high-dose administration and persists until donor engraftment |
| Emetogenicity Classification | Moderate to high (IV high-dose regimen); low to moderate (oral dosing) |
| Monitoring Items | CBC with differential (daily during conditioning and engraftment period), liver function tests (hepatic sinusoidal obstruction syndrome / VOD risk is significant with high-dose busulfan), therapeutic drug monitoring (TDM — AUC-guided dosing recommended for IV busulfan), renal function, neurological status (seizure risk at myeloablative doses — prophylactic anticonvulsants, typically phenytoin or levetiracetam, are required) |
| Handling Protection | Must follow cytotoxic drug handling regulations for both oral tablet and IV formulations; standard PPE and closed-system drug transfer devices required during IV preparation |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 randomized controlled trials directly studying busulfan-based conditioning in MDS patients confirm its clinical utility, with the evidence meeting L1 criteria. The mechanistic rationale is sound — busulfan's myeloablative effect is precisely what is needed to eliminate abnormal hematopoietic clones before allogeneic HSCT. However, the complete absence of SFDA registration is a critical regulatory gap, and full safety data from a structured source was not available in this evidence pack.

**To proceed, the following is needed:**

- **Regulatory pathway**: Obtain SFDA import authorization or initiate product registration for busulfan (IV and/or oral) in Saudi Arabia before clinical deployment
- **Safety documentation**: Review full prescribing information from FDA/EMA label, particularly for hepatic veno-occlusive disease (VOD) monitoring, seizure prophylaxis protocol, and contraindications
- **Pharmacokinetic monitoring protocol**: Establish therapeutic drug monitoring (TDM) capability for IV busulfan AUC-guided dosing; this is standard of care to minimize toxicity variability
- **Drug interaction screening**: Conduct formal drug-drug interaction assessment (DDI data not available in this evidence pack), particularly for co-medications affecting busulfan metabolism (CYP3A4 interactions)
- **Institutional HSCT program readiness**: Confirm that the treating institution has an established allogeneic HSCT program with expertise in busulfan-based conditioning, supportive care infrastructure (including engraftment monitoring), and GVHD management capability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

