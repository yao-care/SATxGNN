---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From an Established Antifolate Therapy to Ten TxGNN-Predicted Oncologic and Hematologic Indications

## One-Sentence Summary

Methotrexate (DrugBank DB00563) is a dihydrofolate reductase (DHFR) inhibitor whose original approved indication is not captured in this evidence pack (Taiwan market data gap). TxGNN generated **10 predicted new indications** for this candidate, ranging from speculative (6 indications with no supporting trials or literature) to moderately supported (**Hodgkin's lymphoma** and **rhabdomyosarcoma**, each backed by graded clinical trials and cohort/RCT-level literature). Only 2 of the 10 candidates currently clear the bar for "Proceed with Guardrails"; the rest remain at Hold or Research Question stage pending further evidence.

---

## Quick Overview

*(Per methodology, this table reflects `predicted_indications[0]` — the single highest-ranked TxGNN prediction. A full 10-candidate comparison follows immediately below.)*

| Item | Content |
|------|------|
| Predicted New Indication (Rank 1) | Pulmonary Blastoma |
| TxGNN Prediction Score (Rank 1) | 99.45% |
| Evidence Level (Rank 1) | L5 (model prediction only, no trials or literature) |
| Market Status (Taiwan) | Not Marketed |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision (Rank 1) | Hold |

### Full Indication Portfolio (All 10 TxGNN Predictions)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pulmonary blastoma | 99.45% | L5 | S0 | Hold |
| 2 | Primary pulmonary lymphoma | 99.45% | L4 | S1 | Research Question |
| 3 | Small cell lung carcinoma | 99.43% | L3 | S1 | Hold |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | 99.42% | L5 | S0 | Hold |
| 5 | Hodgkin's lymphoma | 99.32% | **L2** | **S2** | **Proceed with Guardrails** |
| 6 | Rhabdomyosarcoma | 99.25% | **L2** | **S2** | **Proceed with Guardrails** |
| 7 | Pregerminal center CLL/SLL | 99.23% | L5 | S0 | Hold |
| 8 | CLL/SLL with IGHV somatic hypermutation | 99.23% | L5 | S0 | Hold |
| 9 | Parameningeal embryonal rhabdomyosarcoma | 99.21% | L5 | S0 | Hold |
| 10 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.21% | L5 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank/TFDA is not available for methotrexate in this evidence pack (flagged as a High-severity data gap, DG002). However, the mechanistic rationale documented for every predicted indication converges on the same pharmacology: methotrexate is a **dihydrofolate reductase (DHFR) inhibitor** that blocks folate metabolism and thereby suppresses DNA synthesis in rapidly dividing cells. This antifolate/antimetabolite mechanism is the basis for every repurposing hypothesis below.

Six of the ten predicted indications (pulmonary blastoma, well-differentiated fetal adenocarcinoma of the lung, pregerminal-center CLL/SLL, IGHV-hypermutated CLL/SLL, parameningeal embryonal rhabdomyosarcoma, and botryoid-type embryonal rhabdomyosarcoma of the vagina) are pure mechanism-based extrapolations from TxGNN's knowledge graph with **zero supporting trials or literature** — they should be treated as hypotheses only.

The remaining four indications have a plausible, evidence-anchored rationale:
- **Primary pulmonary lymphoma** and **small cell lung carcinoma**: methotrexate has historical use as a component of multi-agent chemotherapy for systemic lymphomas and was tested in SCLC combination regimens in the 1970s–1990s, though both have since been superseded by modern standards (e.g., platinum-etoposide for SCLC).
- **Hodgkin's lymphoma**: methotrexate was a core component of the historical VBM (vinblastine, bleomycin, methotrexate) regimen for early-stage Hodgkin lymphoma, with actual Phase-level clinical evidence (see below), even though it has been superseded by ABVD as first-line therapy.
- **Rhabdomyosarcoma**: methotrexate has direct Phase II pediatric trial evidence and documented combination use with doxorubicin in sarcomas, though it is not part of the current first-line VAC (vincristine/actinomycin/cyclophosphamide) standard.

Notably, the literature evidence set also reflects methotrexate's well-established use in **rheumatoid arthritis** (e.g., PMID 7653488, 16287579 — methotrexate-associated lymphoproliferative disorders in RA patients), consistent with its known long-term immunomodulatory/antifolate use outside oncology, even though this original indication is not separately recorded in the Taiwan regulatory data supplied.

---

## Clinical Trial Evidence

### Rank 2 — Primary Pulmonary Lymphoma (10 graded trials; 2 additional trials pending relevance grading, not shown)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00916630](https://clinicaltrials.gov/study/NCT00916630) | Phase 1 | Completed | 18 | Pemetrexed (antifolate, MTX-related) in recurrent CNS lymphoma — mechanistically related but different drug and organ (CNS, not lung); Grade B relevance |
| [NCT00013533](https://clinicaltrials.gov/study/NCT00013533) | Early Phase 1 | Completed | 30 | Non-myeloablative HLA-matched allogeneic transplant for pediatric hematologic malignancies broadly; not lymphoma-specific |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Observational biomarker study across immune-mediated skin diseases; not an interventional efficacy study |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Busulfan/fludarabine/TBI non-myeloablative transplant for hematologic malignancies generally |
| [NCT00448201](https://clinicaltrials.gov/study/NCT00448201) | Phase 2 | Completed | 71 | Reduced-intensity allogeneic transplant for patients ineligible for intensive therapy |
| [NCT02911142](https://clinicaltrials.gov/study/NCT02911142) | Phase 1/2 | Active, not recruiting | 17 | Lenalidomide + modified DA-EPOCH-R for primary effusion lymphoma; regimen doesn't clearly include MTX |
| [NCT00051311](https://clinicaltrials.gov/study/NCT00051311) | Phase 2 | Completed | 62 | EPOCH-F/R induction + reduced-intensity transplant with cyclosporine/MTX GVHD prophylaxis |
| [NCT02345850](https://clinicaltrials.gov/study/NCT02345850) | Phase 3 | Completed | 346 | Calcineurin-inhibitor-free GVHD prophylaxis vs. tacrolimus/MTX; MTX used as prophylaxis, not lymphoma treatment |
| [NCT01338987](https://clinicaltrials.gov/study/NCT01338987) | Phase 2 | Completed | 76 | Lupron to enhance lymphocyte reconstitution post-transplant; not MTX efficacy data |
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | Completed | 431 | Tacrolimus/MTX vs. post-transplant cyclophosphamide regimen for GVHD prophylaxis |

**Overall assessment**: No trial directly evaluates methotrexate as treatment for primary pulmonary lymphoma; most relevant support comes from antifolate-class evidence in CNS lymphoma (Grade B) and MTX's established role in transplant-related GVHD prophylaxis for lymphoma patients.

### Rank 3 — Small Cell Lung Carcinoma (10 graded trials; 3 additional trials pending relevance grading, not shown)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03520842](https://clinicaltrials.gov/study/NCT03520842) | Phase 2 | Completed | 22 | Regorafenib + oral methotrexate in KRAS-mutated NSCLC — Phase II with actual MTX efficacy data, but NSCLC not SCLC; Grade B |
| [NCT00743379](https://clinicaltrials.gov/study/NCT00743379) | Phase 1/2 | Completed | 71 | TH-302 + gemcitabine/docetaxel/pemetrexed dose-escalation across pancreatic/prostate/NSCLC |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for NSCLC leptomeningeal metastasis |
| [NCT04747912](https://clinicaltrials.gov/study/NCT04747912) | Phase 2 | Suspended | 25 | Chemotherapy-free induction for Ph+ ALL; unrelated to SCLC |
| [NCT04356222](https://clinicaltrials.gov/study/NCT04356222) | Phase 4 | Unknown | 30 | Durvalumab + intrathecal chemo for NSCLC leptomeningeal metastasis |
| [NCT02385110](https://clinicaltrials.gov/study/NCT02385110) | Phase 2 | Completed | 18 | Alemtuzumab/tocilizumab + etoposide/dexamethasone for HLH; unrelated to SCLC |
| [NCT07156604](https://clinicaltrials.gov/study/NCT07156604) | Phase 2 | Not yet recruiting | 30 | Vebreltinib neoadjuvant therapy for MET-exon-14-skipping NSCLC |
| [NCT04356118](https://clinicaltrials.gov/study/NCT04356118) | Phase 4 | Unknown | 30 | Recombinant human endostatin for NSCLC leptomeningeal metastasis |
| [NCT00354393](https://clinicaltrials.gov/study/NCT00354393) | Phase 2 | Completed | 9 | Multi-modality therapy (including MTX) for malignant pleural mesothelioma |
| [NCT03537833](https://clinicaltrials.gov/study/NCT03537833) | N/A | Completed | 172 | PPI association with pemetrexed hematologic toxicity; safety, not efficacy |

**Overall assessment**: Only one trial (Grade B) provides direct MTX efficacy data, and it is in NSCLC rather than SCLC. Historical SCLC-specific MTX evidence exists only in older literature (see below); current SCLC standard of care has moved to platinum-etoposide.

### Rank 5 — Hodgkin's Lymphoma (10 graded trials; ~37 additional trials remain pending relevance grading, not shown)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01746992](https://clinicaltrials.gov/study/NCT01746992) | Phase 4 | Unknown | 200 | CTOP/ITE/MTX vs. CHOP as first-line therapy for newly-diagnosed T-cell non-Hodgkin lymphoma; randomized comparison including MTX-containing arm |
| [NCT05583071](https://clinicaltrials.gov/study/NCT05583071) | Phase 2 | Recruiting | 20 | MTX + tafasitamab + lenalidomide + rituximab for primary CNS lymphoma patients ineligible for transplant |
| [NCT03602898](https://clinicaltrials.gov/study/NCT03602898) | Phase 2 | Withdrawn (enrollment 0) | 0 | ATG/post-transplant cyclophosphamide vs. calcineurin-inhibitor/MTX GVHD prophylaxis |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat + tacrolimus + MTX for GVHD prevention post-transplant |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | N/A | Completed | 30 | Non-T-cell-depleted haploidentical transplant after reduced-intensity conditioning |
| [NCT01181271](https://clinicaltrials.gov/study/NCT01181271) | Phase 2 | Completed | 42 | Sequential autologous → non-myeloablative allogeneic transplant for poor-risk lymphoma |
| [NCT00003650](https://clinicaltrials.gov/study/NCT00003650) | Phase 3 | Completed | 179 | Combination chemotherapy in children with T-cell/pre-B-cell NHL |
| [NCT00612716](https://clinicaltrials.gov/study/NCT00612716) | Phase 2 | Completed | 6 | Unrelated/partially-matched allogeneic transplant for lymphoma, myeloma, CLL |
| [NCT04283955](https://clinicaltrials.gov/study/NCT04283955) | N/A | Completed | 93 | Retrospective cohort: MTHFR polymorphisms and high-dose MTX toxicity in pediatric NHL |
| [NCT00221325](https://clinicaltrials.gov/study/NCT00221325) | Phase 1 | Completed | 14 | Intraventricular rituximab + MTX for recurrent CNS/intraocular lymphoma |

**Overall assessment**: The strongest direct evidence is a Phase IV randomized comparison of an MTX-containing regimen (CTOP/ITE/MTX) vs. CHOP, though scoped to T-cell NHL broadly rather than classical Hodgkin lymphoma specifically. Supporting literature (below) provides the more Hodgkin-specific historical trial data (VBM regimen).

### Rank 6 — Rhabdomyosarcoma (4 trials, all graded)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357084](https://clinicaltrials.gov/study/NCT00357084) | Phase 2 | Completed | 53 | Methotrexate + glucocorticoids for newly-diagnosed acute GVHD after non-myeloablative transplant; direct MTX efficacy/tolerability data, Grade A relevance |
| [NCT00253552](https://clinicaltrials.gov/study/NCT00253552) | N/A | Terminated | 4 | Filgrastim-primed bone marrow HLA-matched transplant pilot study |
| [NCT00003273](https://clinicaltrials.gov/study/NCT00003273) | Phase 2 | Withdrawn (enrollment 0) | 0 | Dose-intensive chemotherapy for pediatric malignant brain tumors |
| [NCT00112645](https://clinicaltrials.gov/study/NCT00112645) | Phase 1 | Completed | 10 | Allogeneic transplant toxicity study for relapsed/refractory pediatric solid tumors |

**Overall assessment**: Direct rhabdomyosarcoma-specific trial evidence is limited in the registered-trials database; the strongest supporting evidence for this indication comes from the historical literature (Phase II pediatric MTX trial, below).

---

## Literature Evidence

### Rank 2 — Primary Pulmonary Lymphoma (10 graded publications; 9 additional publications pending classification, not shown)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30842385](https://pubmed.ncbi.nlm.nih.gov/30842385/) | 2019 | Cohort | Rinsho Ketsueki | Retrospective survival analysis of PCNSL patients treated with high-dose MTX + rituximab |
| [11244328](https://pubmed.ncbi.nlm.nih.gov/11244328/) | 2001 | Cohort | Oncology | High-dose MTX + vincristine + procarbazine without intrathecal chemo, followed by consolidation RT, for PCNSL |
| [15747120](https://pubmed.ncbi.nlm.nih.gov/15747120/) | 2005 | Cohort | Annals of Hematology | Modified ProMACE-MOPP regimen with moderate-dose MTX for PCNSL |
| [29931605](https://pubmed.ncbi.nlm.nih.gov/29931605/) | 2018 | Review | Curr Treat Options Oncol | Molecular features and CNS recurrence risk of extranodal DLBCL by primary site |
| [41485126](https://pubmed.ncbi.nlm.nih.gov/41485126/) | 2026 | Review | Cancer | First-line BTK/PD-1 inhibitor regimen excluding methotrexate for PCNSL |
| [32590768](https://pubmed.ncbi.nlm.nih.gov/32590768/) | 2020 | Case Report | Medicine | Two cases of primary pulmonary extranodal NK/T-cell lymphoma, nasal type |
| [40283500](https://pubmed.ncbi.nlm.nih.gov/40283500/) | 2025 | Case Report | J Clin Med | Massive pericardial effusion/PE secondary to primary mediastinal NHL in pregnancy |
| [38720609](https://pubmed.ncbi.nlm.nih.gov/38720609/) | 2024 | Case Report | Kyobu Geka | Primary pulmonary DLBCL caused by methotrexate-associated lymphoproliferative disorder, mimicking advanced lung cancer |
| [35831185](https://pubmed.ncbi.nlm.nih.gov/35831185/) | 2022 | Case Report | Rinsho Ketsueki | Primary cutaneous anaplastic large cell lymphoma responding to low-dose MTX |
| [30076020](https://pubmed.ncbi.nlm.nih.gov/30076020/) | 2018 | Case Report | Am J Otolaryngol | Post-treatment sequelae of primary laryngeal NK/T-cell lymphoma |

### Rank 3 — Small Cell Lung Carcinoma (10 graded publications; 10 additional publications pending classification, not shown)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2983855](https://pubmed.ncbi.nlm.nih.gov/2983855/) | 1985 | Cohort | Cancer | MTX + high-dose vincristine added to CAV regimen with radiotherapy in 50 evaluable SCLC patients; MTX addition did not improve response |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Cohort | Med Pediatr Oncol | Cyclophosphamide/adriamycin + cytosine arabinoside + radiotherapy protocol including maintenance chemo in SCLC |
| [1666468](https://pubmed.ncbi.nlm.nih.gov/1666468/) | 1991 | Cohort | Tumori | CCNU + MTX salvage chemotherapy in 34 SCLC patients resistant to CAV/PE; 21.2% objective response rate |
| [6280794](https://pubmed.ncbi.nlm.nih.gov/6280794/) | 1982 | Cohort | Bull Cancer | CALGB experience: cyclophosphamide ± MTX ± vincristine regimens in SCLC; no significant survival difference among arms |
| [32152484](https://pubmed.ncbi.nlm.nih.gov/32152484/) | 2020 | Review | Nat Rev Clin Oncol | Folate receptor α as anticancer target, contextualizing MTX/pemetrexed antifolate mechanism in lung and other solid tumors |
| [205153](https://pubmed.ncbi.nlm.nih.gov/205153/) | 1978 | Review | Ann Intern Med | Overview of SCLC therapeutic management including combination chemotherapy era |
| [6282790](https://pubmed.ncbi.nlm.nih.gov/6282790/) | 1982 | Review | Int J Radiat Oncol Biol Phys | Role of thoracic/cranial irradiation combined with chemotherapy in SCLC |
| [7921445](https://pubmed.ncbi.nlm.nih.gov/7921445/) | 1994 | Cohort | Am J Respir Crit Care Med | KS1/4-methotrexate immunoconjugate studied in 11 advanced NSCLC patients; dose-escalation toxicity data |
| [32888268](https://pubmed.ncbi.nlm.nih.gov/32888268/) | 2021 | Preclinical | Curr Top Med Chem | Solid nanodispersion formulation to improve MTX solubility/bioavailability for SCLC treatment |
| [25879815](https://pubmed.ncbi.nlm.nih.gov/25879815/) | 2015 | Case Report | Am J Case Rep | Meningeal carcinomatosis from NSCLC responding to salvage intrathecal etoposide after first-line MTX failure |

### Rank 5 — Hodgkin's Lymphoma (10 graded publications; 10 additional publications pending classification, not shown)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | RCT | Cancer | Gruppo Italiano Studio Linfomi trial: VBM (vinblastine/bleomycin/MTX) chemotherapy + irradiation for early-stage favorable Hodgkin lymphoma |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review | Crit Rev Oncol Hematol | Review of 9 small trials of VBM + involved-field radiotherapy for early-stage Hodgkin lymphoma: 94–100% complete remission, 75–95% 5-year PFS, but notable pulmonary toxicity |
| [35848760](https://pubmed.ncbi.nlm.nih.gov/35848760/) | 2022 | Cohort | Am J Surg Pathol | 9p24.1 alteration and PD-L1 expression compared across de novo and MTX-associated EBV+ classical Hodgkin lymphoma |
| [8635099](https://pubmed.ncbi.nlm.nih.gov/8635099/) | 1996 | Cohort | Cancer | IVAM (ifosfamide/etoposide/cytarabine/MTX) salvage chemotherapy in relapsed/refractory aggressive NHL |
| [7653488](https://pubmed.ncbi.nlm.nih.gov/7653488/) | 1995 | Cohort | Am J Med | Retrospective study of hematologic malignancies (including lymphoma) associated with MTX use in rheumatoid arthritis |
| [28380678](https://pubmed.ncbi.nlm.nih.gov/28380678/) | 2017 | Cohort | Cancer Science | Clinicopathological comparison of MTX-associated DLBCL vs. classical Hodgkin lymphoma subtypes |
| [11368287](https://pubmed.ncbi.nlm.nih.gov/11368287/) | 2001 | Review | Drugs | Bendamustine review noting 61–97% response rates in Hodgkin/NHL combination regimens |
| [12967352](https://pubmed.ncbi.nlm.nih.gov/12967352/) | 2003 | Review | Clinical Evidence | Non-Hodgkin lymphoma treatment evidence review |
| [16467107](https://pubmed.ncbi.nlm.nih.gov/16467107/) | 2006 | Preclinical | Clin Cancer Res | Pralatrexate + gemcitabine superior to MTX + cytarabine in preclinical NHL models |
| [24246254](https://pubmed.ncbi.nlm.nih.gov/24246254/) | 2014 | Case Report | J Oral Maxillofac Surg | EBV+ oral ulceration simulating Hodgkin lymphoma in a patient on MTX therapy |

### Rank 6 — Rhabdomyosarcoma (10 graded publications; 10 additional publications pending classification, not shown)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | RCT | J Pediatr Hematol Oncol | Phase II trial of high-dose MTX in previously-untreated children/adolescents with high-risk unresectable or metastatic rhabdomyosarcoma |
| [36614297](https://pubmed.ncbi.nlm.nih.gov/36614297/) | 2023 | Cohort | Int J Mol Sci | BOMP-EPI regimen (bleomycin/vincristine/MTX/cisplatin alternating with etoposide/cisplatin/ifosfamide) in 10 adult relapsed/metastatic RMS patients |
| [3475644](https://pubmed.ncbi.nlm.nih.gov/3475644/) | 1987 | Cohort | Oncology | Weekly doxorubicin + MTX combination in 55 sarcoma patients; 28% objective response at higher dose levels |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Cohort | Oncotarget | Pilot study of pediatric metronomic 4-drug regimen |
| [9862574](https://pubmed.ncbi.nlm.nih.gov/9862574/) | 1998 | Cohort | Br J Cancer | Adjuvant chemotherapy (including rhabdomyosarcoma patients) for resected primary cardiac sarcoma |
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Value of adjuvant chemotherapy in pediatric sarcomas, including rhabdomyosarcoma |
| [38323945](https://pubmed.ncbi.nlm.nih.gov/38323945/) | 2024 | Review | Int J Radiat Oncol Biol Phys | PENTEC review of radiation myelopathy risk factors in pediatric cancer patients |
| [9039735](https://pubmed.ncbi.nlm.nih.gov/9039735/) | 1996 | Review | Br Med Bull | Overview of controversies in childhood sarcoma management |
| [2811561](https://pubmed.ncbi.nlm.nih.gov/2811561/) | 1989 | Case Report | Laryngoscope | Rhabdomyosarcoma of the ear and temporal bone treated with multimodality therapy |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case Report | Hinyokika Kiyo | Refractory prostatic rhabdomyosarcoma case managed with combination chemotherapy |

### Indications with No Clinical Trial or Literature Evidence

Pulmonary blastoma, well-differentiated fetal adenocarcinoma of the lung, pregerminal-center CLL/SLL, IGHV-hypermutated CLL/SLL, parameningeal embryonal rhabdomyosarcoma, and botryoid-type embryonal rhabdomyosarcoma of the vagina currently have **no related clinical trials or literature registered**.

---

## Cytotoxicity

Methotrexate is an antineoplastic/cytotoxic agent (confirmed by the mechanistic rationale in this evidence pack — DHFR inhibitor used across multiple oncologic predicted indications — and by its established use in hematologic malignancy chemotherapy regimens documented above).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antifolate / dihydrofolate reductase inhibitor class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Hodgkin's lymphoma and rhabdomyosarcoma only) **/ Research Question** (primary pulmonary lymphoma) **/ Hold** (small cell lung carcinoma and the six evidence-free candidates)

**Rationale:**
- **Hodgkin's lymphoma** and **rhabdomyosarcoma** (L2, S2) each have a genuine Phase-level clinical trial history plus RCT/cohort-grade literature supporting MTX use, even though neither is a current first-line standard — these merit guarded advancement with updated evidence review.
- **Primary pulmonary lymphoma** (L4, S1) has only mechanism-adjacent evidence (antifolate class data in CNS lymphoma) and warrants a defined research question rather than immediate progression.
- **Small cell lung carcinoma** (L3, S1) evidence is real but 30–45 years old and reflects regimens superseded by platinum-etoposide; not actionable without contemporary data.
- The remaining six candidates (L5, S0) are pure knowledge-graph extrapolations with zero clinical or literature support and should remain on Hold.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001) that prevents any S1 safety pre-assessment for the entire candidate set
- Confirmed drug-mechanism-of-action data from DrugBank — currently a **High**-severity data gap (DG002)
- Drug-drug interaction (DDI) data — current query status is "not found"
- Route-of-administration and dosage-form compatibility assessment (all 10 candidates show `route_compatibility.status: pending`)
- For the two Guardrails candidates: a contemporary literature/guideline review to confirm whether MTX still has a defensible clinical role given that ABVD (Hodgkin) and VAC (rhabdomyosarcoma) are now first-line standards
- Taiwan market/licensing data verification, since the current record shows methotrexate as unmarketed in Taiwan with zero authorizations, which should be re-confirmed given its broad global availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

