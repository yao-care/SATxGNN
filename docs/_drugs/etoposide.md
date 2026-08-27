---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From an Undocumented Original Indication to Multiple TxGNN-Predicted Oncology Indications

## One-Sentence Summary

Etoposide (DrugBank DB00773) is an established cytotoxic chemotherapy agent, though this evidence pack does not document its original approved indication or formal mechanism-of-action text. TxGNN generated **10 predicted indications** for this drug, ranging from already near-established uses — **Ewing sarcoma** and **rhabdomyosarcoma** (both L1 evidence, standard-of-care backbone drug) — to rare single-case-report hypotheses such as **embryonal extrahepatic bile duct rhabdomyosarcoma** (L5, prediction only). This is a multi-candidate evidence pack (`TW-DB00773-multi`), so this report ranks and evaluates all 10 predictions rather than a single one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `original_indications` or licensed labeling data available) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Total Predicted Indications (TxGNN) | 10 |
| Strongest Evidence Indications | Ewing sarcoma, Rhabdomyosarcoma (both L1) |
| Weakest Evidence Indications | Embryonal extrahepatic bile duct RMS, Extrahepatic bile duct RMS (both L5) |
| Overall Recommended Decision | Mixed — see per-indication table below |

### Predicted Indications Ranked by TxGNN Score

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Well-differentiated fetal adenocarcinoma of the lung | 99.94% | L4 | S0 | Hold |
| 2 | Primary pulmonary lymphoma | 99.94% | L2 | S2 | Proceed with Guardrails |
| 3 | Pulmonary blastoma | 99.94% | L4 | S1 | Research Question |
| 4 | Ewing sarcoma | 99.85% | L1 | S3 | Proceed with Guardrails |
| 5 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.80% | L4 | S0 | Hold |
| 6 | Rhabdomyosarcoma (disease) | 99.79% | L1 | S3 | Proceed with Guardrails |
| 7 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | L5 | S0 | Hold |
| 8 | Parameningeal embryonal rhabdomyosarcoma | 99.76% | L3 | S2 | Research Question |
| 9 | Extrahepatic bile duct rhabdomyosarcoma | 99.75% | L5 | S0 | Hold |
| 10 | Prostate embryonal rhabdomyosarcoma | 99.74% | L4 | S0 | Hold |

---

## Why Are These Predictions Reasonable?

Detailed formal mechanism-of-action data is not available in this evidence pack. Based on the repurposing rationale attached to each prediction, etoposide is consistently identified as a **topoisomerase II inhibitor** — it induces double-strand DNA breaks that are lethal to highly proliferative tumor cells. This single mechanism underlies all 10 predictions, but the strength of supporting evidence differs sharply by tumor type:

**Established-use extensions (Ewing sarcoma, rhabdomyosarcoma):** Etoposide is already a backbone component of standard regimens for both diseases (VDC/IE, IE, VAC/IE). For Ewing sarcoma specifically, the EWS-FLI1 fusion oncoprotein drives R-loop formation and impairs BRCA1-mediated repair, which is documented to confer high sensitivity to topoisomerase II inhibitors (PMID 29513652). These two predictions largely reflect an existing, guideline-supported indication rather than a novel hypothesis.

**Anatomically/histologically adjacent hypotheses (primary pulmonary lymphoma, parameningeal embryonal RMS):** These diseases belong to disease families (lymphoma, rhabdomyosarcoma) where etoposide-containing regimens (EPOCH, ICE, IE) are already standard, but no trial has specifically targeted the anatomic subtype named. The mechanistic link is sound, but site-specific clinical proof is limited to cohort/case-series data.

**Rare-tumor, single-case hypotheses (fetal adenocarcinoma of the lung, pulmonary blastoma, botryoid-type vaginal RMS, bile duct RMS variants, prostate embryonal RMS):** These are all very rare tumors where the mechanistic rationale is inferred by analogy to related embryonal/blastomatous tumor biology, but supporting evidence is limited to one or a handful of case reports, with no dedicated clinical trials. These remain research hypotheses only.

---

## Clinical Trial Evidence

### Primary Pulmonary Lymphoma (Rank 2, L2, Proceed with Guardrails)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001379](https://clinicaltrials.gov/study/NCT00001379) | Phase 2 | Completed | 94 | Lymphomatoid granulomatosis (a pulmonary lymphoproliferative disorder overlapping with primary pulmonary lymphoma) treated with alpha-interferon and/or chemotherapy |
| [NCT03077828](https://clinicaltrials.gov/study/NCT03077828) | Phase 2 | Unknown | 43 | Pembrolizumab + ICE (ifosfamide, carboplatin, etoposide) salvage chemotherapy in relapsed/refractory Hodgkin lymphoma |
| [NCT01445535](https://clinicaltrials.gov/study/NCT01445535) | Phase 1 | Completed | 15 | DA-EPOCH-R (includes etoposide) in T- and NK-cell lymphomas, a common histology of primary pulmonary lymphoma |
| [NCT05675410](https://clinicaltrials.gov/study/NCT05675410) | Phase 3 | Recruiting | 1875 | Immuno-oncology vs. standard chemotherapy (± etoposide-containing regimens) in Stage I–II classic Hodgkin lymphoma |
| [NCT02911142](https://clinicaltrials.gov/study/NCT02911142) | Phase 1/2 | Active, not recruiting | 17 | Lenalidomide + modified DA-EPOCH-R in primary effusion lymphoma / KSHV-associated large cell lymphoma |
| [NCT00013533](https://clinicaltrials.gov/study/NCT00013533) | Early Phase 1 | Completed | 30 | Non-myeloablative allogeneic stem cell transplant for pediatric hematologic malignancies |
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | Completed | 473 | Autologous PBSC transplant (ifosfamide, etoposide, carboplatin + rituximab) for lymphoma |
| [NCT00352027](https://clinicaltrials.gov/study/NCT00352027) | Phase 2 | Completed | 81 | Stanford V chemotherapy + low-dose radiotherapy in intermediate-risk pediatric Hodgkin lymphoma |
| [NCT00051311](https://clinicaltrials.gov/study/NCT00051311) | Phase 2 | Completed | 62 | EPOCH-F/R induction + reduced-intensity allogeneic HSCT for refractory/relapsed hematologic malignancies |
| [NCT00265889](https://clinicaltrials.gov/study/NCT00265889) | Phase 2 | Completed | 42 | Tandem autologous stem cell transplant for progressive/poor-risk recurrent Hodgkin lymphoma |

*Note: no trial specifically enrolled a primary pulmonary lymphoma population; all trials are general lymphoma studies using etoposide-containing regimens.*

### Ewing Sarcoma (Rank 4, L1, Proceed with Guardrails)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | First-line treatment of Ewing tumors with primary extrapulmonary dissemination, ages 2–50 |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy + radiotherapy + COX-2-targeted consolidation for metastatic Ewing sarcoma |
| [NCT00007813](https://clinicaltrials.gov/study/NCT00007813) | Phase 1 | Completed | 21 | High-dose etoposide + carboplatin + escalating cyclophosphamide with autologous CD34+ stem cell rescue |
| [NCT00876031](https://clinicaltrials.gov/study/NCT00876031) | Phase 3 | Completed | 195 | Randomized trial of maintenance O-TIE (etoposide, idarubicin, trofosfamide) in high-risk RMS/Ewing-like soft tissue sarcoma |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib + ifosfamide/carboplatin/etoposide (ICE) pediatric trial |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab (anti-IGF-1R) + multiagent chemotherapy (incl. etoposide) in newly diagnosed metastatic Ewing sarcoma |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Addition of vincristine-topotecan-cyclophosphamide to standard VDC/IE chemotherapy in non-metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification (standard vs. intensive) in non-metastatic Ewing sarcoma |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | N/A | Cyclophosphamide, doxorubicin, vincristine, etoposide, ifosfamide + resection/radiotherapy for PNET/Ewing sarcoma |
| [NCT06699472](https://clinicaltrials.gov/study/NCT06699472) | Phase 2 | Recruiting | 22 | Trilaciclib to prevent VDC/IE chemotherapy-related myelosuppression in Ewing sarcoma |

### Rhabdomyosarcoma (Rank 6, L1, Proceed with Guardrails)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00354744](https://clinicaltrials.gov/study/NCT00354744) | Phase 3 | Completed | 109 | Dose-compressed IE/VDC intensive multiagent therapy for high-risk rhabdomyosarcoma |
| [NCT00025441](https://clinicaltrials.gov/study/NCT00025441) | Phase 2 | Completed | N/A | Combination chemotherapy for metastatic rhabdomyosarcoma/malignant soft tissue sarcoma of childhood |
| [NCT00007813](https://clinicaltrials.gov/study/NCT00007813) | Phase 1 | Completed | 21 | High-dose etoposide + carboplatin + cyclophosphamide with autologous stem cell rescue (includes RMS) |
| [NCT00077285](https://clinicaltrials.gov/study/NCT00077285) | Phase 2 | Active, not recruiting | 65 | Irinotecan + carboplatin upfront window therapy for intermediate/high-risk rhabdomyosarcoma |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib + IE (ifosfamide, carboplatin, etoposide) pediatric trial |
| [NCT00025363](https://clinicaltrials.gov/study/NCT00025363) | Phase 2 | Completed | 150 | Randomized window study of irinotecan schedules ± tirapazamine for relapsed/progressive RMS |
| [NCT06669013](https://clinicaltrials.gov/study/NCT06669013) | Phase 3 | Recruiting | 40 | Dinutuximab beta + investigator-choice chemotherapy in GD2+ RMS/Ewing/osteosarcoma after 1st-line progression |
| [NCT04388839](https://clinicaltrials.gov/study/NCT04388839) | Phase 2 | Active, not recruiting | 12 | Evolution-inspired chemotherapy scheduling strategies in fusion-positive metastatic RMS |
| [NCT00379457](https://clinicaltrials.gov/study/NCT00379457) | Phase 3 | Unknown | 600 | RMS-2005 protocol comparing chemotherapy regimens for nonmetastatic rhabdomyosarcoma |
| [NCT00003052](https://clinicaltrials.gov/study/NCT00003052) | Phase 3 | Completed | 340 | Neoadjuvant EIA (etoposide, ifosfamide, adriamycin) ± regional hyperthermia in high-risk soft tissue sarcoma |

### Remaining Indications (Ranks 1, 3, 5, 7, 8, 9, 10)

Currently no related clinical trials are registered for: well-differentiated fetal adenocarcinoma of the lung, pulmonary blastoma, botryoid-type embryonal rhabdomyosarcoma of the vagina, embryonal extrahepatic bile duct rhabdomyosarcoma, parameningeal embryonal rhabdomyosarcoma, extrahepatic bile duct rhabdomyosarcoma, and prostate embryonal rhabdomyosarcoma.

---

## Literature Evidence

### Primary Pulmonary Lymphoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3875741](https://pubmed.ncbi.nlm.nih.gov/3875741/) | 1985 | Phase II/III | Gan no rinsho | Oral VP-16 (etoposide) in NHL and SCLC: 31% response rate in heavily pretreated NHL patients |
| [34350085](https://pubmed.ncbi.nlm.nih.gov/34350085/) | 2021 | Case series | Cureus | Primary mediastinal B-cell lymphoma treated with R-CEOP (rituximab, cyclophosphamide, etoposide, vincristine, prednisone) |
| [34329577](https://pubmed.ncbi.nlm.nih.gov/34329577/) | 2021 | Cohort | Lancet Haematology | Dose-dense BV-ICE (brentuximab vedotin + ifosfamide/carboplatin/etoposide) for relapsed/refractory classical Hodgkin lymphoma |
| [38555923](https://pubmed.ncbi.nlm.nih.gov/38555923/) | 2024 | Cohort | Lancet Haematology | Anti-CD30 CAR T cells as consolidation after autologous HSCT in high-risk CD30+ lymphoma |
| [15625540](https://pubmed.ncbi.nlm.nih.gov/15625540/) | 2005 | Cohort | Biol Blood Marrow Transplant | High-dose carmustine, etoposide, cisplatin for autologous transplant in relapsed/refractory lymphoma |
| [32590768](https://pubmed.ncbi.nlm.nih.gov/32590768/) | 2020 | Case report | Medicine | Primary pulmonary extranodal NK/T-cell lymphoma, nasal type: two cases and literature review |
| [25527680](https://pubmed.ncbi.nlm.nih.gov/25527680/) | 2014 | Case report | BMJ Case Reports | Primary pulmonary lymphoma in a patient with advanced AIDS |
| [30076020](https://pubmed.ncbi.nlm.nih.gov/30076020/) | 2018 | Case report | Am J Otolaryngol | Post-treatment sequelae and management of primary laryngeal NK/T-cell lymphoma |
| [19879424](https://pubmed.ncbi.nlm.nih.gov/19879424/) | 2009 | Review | Adv Cancer Res | Review of clusterin and chemoresistance mechanisms relevant to anticancer agent resistance |

### Ewing Sarcoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | NEJM | Addition of ifosfamide + etoposide to standard chemotherapy improved survival in Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012 trial comparing two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT | Trials | EURO EWING 2012 protocol: international RCT for newly diagnosed Ewing sarcoma family tumors |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | Ganitumab + interval-compressed chemotherapy in newly diagnosed metastatic Ewing sarcoma (COG trial) |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy improves outcome in localized Ewing sarcoma (COG) |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review/Guideline | Cancer | Consensus recommendations for Ewing sarcoma management, National Ewing Sarcoma Tumor Board |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Cohort | Sarcoma | Oral etoposide for relapsed/refractory Ewing sarcoma in adolescents and adults |
| [37093679](https://pubmed.ncbi.nlm.nih.gov/37093679/) | 2023 | Cohort | Jpn J Clin Oncol | Clinical characteristics of primary cutaneous/subcutaneous Ewing sarcoma |
| [34962714](https://pubmed.ncbi.nlm.nih.gov/34962714/) | 2022 | Cohort | Pediatr Blood Cancer | Chemotherapy-induced thrombocytopenia in Ewing sarcoma and romiplostim supportive care |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Basic mechanism | Nature | EWS-FLI1 causes R-loops and blocks BRCA1 repair, explaining Ewing sarcoma sensitivity to etoposide |

### Rhabdomyosarcoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11846301](https://pubmed.ncbi.nlm.nih.gov/11846301/) | 2001 | RCT | J Pediatr Hematol Oncol | Ifosfamide + etoposide superior to vincristine + melphalan in metastatic rhabdomyosarcoma (IRSG) |
| [26503200](https://pubmed.ncbi.nlm.nih.gov/26503200/) | 2016 | Cohort | J Clin Oncol | Dose-compressed IE/VDC + irinotecan + radiation in high-risk rhabdomyosarcoma (COG) |
| [17091486](https://pubmed.ncbi.nlm.nih.gov/17091486/) | 2008 | Cohort | Pediatr Blood Cancer | Alternating VDC/etoposide-ifosfamide vs. IRS-IV in intermediate-risk rhabdomyosarcoma |
| [9849484](https://pubmed.ncbi.nlm.nih.gov/9849484/) | 1998 | Cohort | Eur J Cancer | Alternating VDC and etoposide/ifosfamide for intermediate-risk rhabdomyosarcoma |
| [40591908](https://pubmed.ncbi.nlm.nih.gov/40591908/) | 2025 | Cohort | J Pediatr Hematol Oncol | Clinical features and treatment outcomes in 65 children with head and neck rhabdomyosarcoma |
| [36614297](https://pubmed.ncbi.nlm.nih.gov/36614297/) | 2023 | Cohort | Int J Mol Sci | Platinum-based regimens (incl. etoposide) active in advanced pediatric-type RMS in adults |
| [37138963](https://pubmed.ncbi.nlm.nih.gov/37138963/) | 2023 | Cohort | Ecancermedicalscience | Outcome and FOXO1 fusion impact in non-metastatic childhood rhabdomyosarcoma |
| [32658380](https://pubmed.ncbi.nlm.nih.gov/32658380/) | 2020 | Cohort | Pediatr Blood Cancer | Metronomic cyclophosphamide-etoposide + valproic acid for refractory/relapsing pediatric malignancies |
| [37568826](https://pubmed.ncbi.nlm.nih.gov/37568826/) | 2023 | Review | Cancers | Review of maintenance chemotherapy for rhabdomyosarcoma |
| [10754991](https://pubmed.ncbi.nlm.nih.gov/10754991/) | 2000 | Review | Cancer Invest | Progress in diagnosis and treatment of rhabdomyosarcoma and related soft tissue sarcomas |

### Parameningeal Embryonal Rhabdomyosarcoma (Rank 8)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40591908](https://pubmed.ncbi.nlm.nih.gov/40591908/) | 2025 | Cohort | J Pediatr Hematol Oncol | 49.2% of pediatric head/neck RMS cases were parameningeal; treatment outcomes described |
| [12654440](https://pubmed.ncbi.nlm.nih.gov/12654440/) | 2003 | Retrospective | Int J Radiat Oncol Biol Phys | Radiation volume influences outcome in pediatric parameningeal rhabdomyosarcoma |
| [10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/) | 2000 | Cohort | J Clin Oncol | Intensified therapy benefit for local/regional embryonal rhabdomyosarcoma (IRS-IV) |
| [18521303](https://pubmed.ncbi.nlm.nih.gov/18521303/) | 2001 | Review | Sarcoma | Major lessons from IRS-I through IRS-IV studies underlying current RMS treatment protocols |

### Remaining Indications (Ranks 1, 3, 5, 7, 9, 10)

These indications are supported only by single or very few case reports/reviews, all describing case-level chemotherapy response rather than trial-level evidence:

- **Well-differentiated fetal adenocarcinoma of the lung** ([PMID 33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/), 2020, case report/review) — classic biphasic pulmonary blastoma case treated with nedaplatin/paclitaxel, not etoposide directly.
- **Pulmonary blastoma** — multiple case reports across decades (e.g. [PMID 6086368](https://pubmed.ncbi.nlm.nih.gov/6086368/), 1984, complete remission with CCNU/vincristine/VP-16/cyclophosphamide), but no systematic trial evidence exists for this rare tumor.
- **Botryoid-type embryonal rhabdomyosarcoma of the vagina** ([PMID 23903199](https://pubmed.ncbi.nlm.nih.gov/23903199/), 2013, case report) — adult cervical rhabdomyosarcoma case, anatomically adjacent but not the vaginal botryoid subtype specifically.
- **Prostate embryonal rhabdomyosarcoma** — supported by general IRSG cohort/review literature ([PMID 11846299](https://pubmed.ncbi.nlm.nih.gov/11846299/), [PMID 10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/)), no site-specific studies.
- **Embryonal extrahepatic bile duct rhabdomyosarcoma** and **extrahepatic bile duct rhabdomyosarcoma** — currently no related literature available.

---

## Cytotoxicity

Etoposide is a conventional cytotoxic chemotherapy agent (topoisomerase II inhibitor, epipodophyllotoxin class), consistent across all 10 predicted-indication rationales and its established use in Ewing sarcoma, rhabdomyosarcoma, and lymphoma regimens.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase II inhibitor / epipodophyllotoxin class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions — no drug-specific toxicity grading data available in this evidence pack |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic agent handling precautions apply; specific protocol not documented in this evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction, contraindication, or warning data was returned for etoposide in this evidence pack (DDI query status: not found; key warnings and contraindications: not documented).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Ewing sarcoma, rhabdomyosarcoma, primary pulmonary lymphoma) / **Hold** (remaining 7 rare-tumor hypotheses)

**Rationale:**
- Ewing sarcoma and rhabdomyosarcoma have L1 evidence (multiple completed Phase 3 RCTs) and reflect etoposide's already-established role as a chemotherapy backbone — these are extensions of existing use, not novel repurposing candidates, and should move directly to guardrail-based clinical adoption review rather than exploratory repurposing workup.
- Primary pulmonary lymphoma (L2) and parameningeal embryonal rhabdomyosarcoma (L3) have plausible mechanistic support and some trial/cohort evidence but lack site-specific studies — worth a guarded/research-question track.
- The remaining 6 predictions (fetal adenocarcinoma of the lung, pulmonary blastoma, vaginal botryoid RMS, bile duct RMS variants, prostate embryonal RMS) rest on single case reports or pure model extrapolation (L4–L5) and should be held pending stronger evidence.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — DG001)
- Formal DrugBank mechanism-of-action and toxicity data (currently a High-severity data gap — DG002)
- Saudi Arabia market/licensing confirmation (drug currently shows as not marketed with 0 licenses)
- Site-specific clinical evidence for primary pulmonary lymphoma and parameningeal embryonal RMS before advancing beyond research-question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

