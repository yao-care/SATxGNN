---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a pyrimidine analog antimetabolite with decades of established use in acute leukemia, working by blocking DNA synthesis specifically during the S phase of cell division.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**, a finding supported by **3 registered clinical trials** (all indirect) and **20 publications** that together establish historical precedent but limited modern evidence.
This is best characterized as an early research hypothesis — the historical signal exists, but the evidence base requires prospective validation before clinical advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute leukemia (AML / ALL) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not marketed (0 registered products) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, cytarabine (cytosine arabinoside, Ara-C) is a nucleoside analog that is phosphorylated intracellularly to ara-CTP, which competes with dCTP for incorporation into DNA and inhibits DNA polymerase α. This mechanism is strictly S-phase specific — cells actively replicating DNA are selectively targeted.

Small cell lung carcinoma is one of the most proliferative solid tumors in oncology, typically presenting with Ki-67 indices exceeding 50–80%. This biological characteristic directly aligns with cytarabine's mode of action: the higher the fraction of cells in S phase at any given moment, the greater the theoretical susceptibility to Ara-C. The same logic underlies cytarabine's dominance in acute leukemia, where blast cells proliferate rapidly.

Historically, cytarabine did appear in SCLC treatment protocols. A 1979 study combined cytosine arabinoside with cyclophosphamide, doxorubicin, and concurrent radiotherapy in 20 previously untreated SCLC patients, achieving a 78% combined response rate. Subsequent work evaluated VP-16 plus infusional Ara-C in relapsed SCLC (1988), and cytarabine has been used intrathecally for SCLC leptomeningeal metastases — a recognized complication of the disease. In vitro data further demonstrate collateral sensitivity to cytarabine in doxorubicin/VM-26-resistant SCLC cell lines, suggesting a potential niche in drug-resistant disease. These data points explain why the TxGNN graph-based model, which captures biological similarity relationships, scored this prediction highly — yet the absence of modern prospective trials reflects that this combination was ultimately displaced by etoposide-platinum regimens without rigorous Phase 3 comparison.

---

## Clinical Trial Evidence

The three registered trials identified for this drug-disease pair do not directly evaluate cytarabine in SCLC. All three involve intrathecal pemetrexed for lung cancer-related leptomeningeal metastases, providing only conceptual support for intrathecal chemotherapy as a delivery route.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed + involved-field radiotherapy for leptomeningeal metastasis from solid tumors; mentions cytarabine as the existing intrathecal standard, indirectly validating intrathecal route feasibility |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent NSCLC leptomeningeal metastasis; background explicitly references cytarabine and liposomal cytarabine as current standards for intrathecal use |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | NSCLC adjuvant chemotherapy (vinorelbine, cisplatin, pemetrexed); terminated early due to insufficient enrollment, cytarabine not a study agent — minimal relevance |

> No clinical trials directly evaluating systemic cytarabine for SCLC are currently registered on ClinicalTrials.gov.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Pilot Clinical Study | Medical and Pediatric Oncology | Cytosine arabinoside + cyclophosphamide + doxorubicin + concurrent radiotherapy in 20 untreated SCLC patients; 78% combined response rate reported |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical Study | American Journal of Clinical Oncology | Ara-C 100 mg/m²/day continuous infusion in SCLC: no responses as monotherapy in 10 heavily pretreated patients; added to CAV regimen in 25 extensive-stage patients with exploratory activity |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical Study | American Journal of Clinical Oncology | VP-16 (etoposide) + infusional Ara-C (45 mg/m²/day × 72h) in 17 refractory SCLC patients; assessed response to this salvage combination regimen |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Basic Science | Biochemical Pharmacology | MDR SCLC cell lines (daunorubicin/VM-26-resistant) show collateral sensitivity to cytarabine and gemcitabine; provides mechanistic rationale for Ara-C in drug-resistant SCLC |
| [1360876](https://pubmed.ncbi.nlm.nih.gov/1360876/) | 1992 | Basic Science | Cancer Chemotherapy and Pharmacology | Doxorubicin-sensitive and resistant SCLC cell lines evaluated for cross-sensitivity; Ara-C sensitivity pattern correlates with etoposide and vincristine sensitivity |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case Report | Cancer & Chemotherapy | Stage IV SCLC with meningeal carcinomatosis treated with multidisciplinary approach including intrathecal chemotherapy; illustrates clinical role of intrathecal Ara-C in SCLC CNS metastases |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | American Journal of Medicine | Meningeal carcinomatosis in 60 evaluable SCLC patients; establishes CNS/meningeal involvement patterns and chemotherapy response landscape |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | Journal of Clinical Oncology | CALGB randomized trial of chemotherapy + radiotherapy ± warfarin in limited-stage SCLC; cytarabine-containing consolidation was part of the treatment backbone |
| [18600541](https://pubmed.ncbi.nlm.nih.gov/18600541/) | 2008 | Basic Science | Nucleosides, Nucleotides & Nucleic Acids | hENT1 and hCNT1 nucleoside transporter expression confirmed in NSCLC cell lines and patient samples; these transporters are required for cytarabine cellular entry and efficacy |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics and Chemotherapy | Foundational review of Ara-C analogs; covers cytidine deaminase-mediated inactivation, resistance mechanisms, and structural derivatives with implications for solid tumor applications |

---

## Saudi Arabia Market Information

Cytarabine currently has **no registered drug products** in Saudi Arabia. No regulatory authorizations exist, and the drug is not commercially available through standard market channels. Any clinical use would require importation under a named-patient or compassionate-use framework, subject to Saudi Food and Drug Authority (SFDA) approval.

---

## Cytotoxicity

Cytarabine is a conventional cytotoxic antineoplastic agent. It meets all criteria for this section: it is a fluoropyrimidine-class antimetabolite used as backbone chemotherapy in hematologic malignancies, with well-characterized cytotoxic properties.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Pyrimidine analog / Antimetabolite |
| Myelosuppression Risk | High — leukopenia, thrombocytopenia, and anemia are the dose-limiting toxicities; Grade IV myelosuppression reported in ~32% of patients at high-dose regimens (3 g/m²) |
| Emetogenicity Classification | Low to moderate at standard doses; moderate at intermediate/high doses |
| Monitoring Items | CBC with differential (mandatory, frequent); liver function tests; renal function; cerebellar function assessment for high-dose protocols (cerebellar syndrome is a recognized neurotoxicity) |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices, appropriate PPE required throughout preparation and administration |

---

## Safety Considerations

Please refer to the package insert for full safety information. Formal warning and contraindication data are not available in the current Evidence Pack.

> The absence of local SFDA labeling data represents a blocking gap for safety pre-screening. The known cytotoxic profile includes severe myelosuppression, hepatotoxicity at high doses, and cerebellar neurotoxicity (high-dose syndrome). Drug-drug interaction data could not be retrieved in this evidence cycle.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Despite a high TxGNN prediction score (99.78%) and a historically grounded mechanistic rationale — SCLC's extreme proliferative nature aligns with cytarabine's S-phase specificity — the available clinical evidence is entirely retrospective, dated (1979–1997), and small in scale. Cytarabine was tested in SCLC decades ago but was not adopted into standard practice, likely displaced by more active etoposide-platinum combinations. No modern prospective trials exist to confirm or refute its efficacy against current SCLC biology. This remains a hypothesis worthy of structured investigation rather than direct clinical application.

**To proceed, the following is needed:**

- **Safety data package**: Obtain and review SFDA package insert or international labeling (e.g., EMA/FDA) to fulfill the blocking DG001 gap before any clinical safety evaluation
- **MOA clarification**: Retrieve full DrugBank MOA entry (DG002) to formally document DNA polymerase α inhibition and S-phase specificity for the mechanistic dossier
- **Historical failure analysis**: Systematically review why cytarabine was not retained in SCLC protocols — was it toxicity, lack of additive benefit over CAV/EP, or simply lack of Phase 3 investment?
- **Nucleoside transporter profiling**: Confirm hENT1/hCNT1 expression in contemporary SCLC specimens (both treatment-naïve and platinum-refractory), since transporter levels are the primary predictor of Ara-C cellular uptake
- **Preclinical validation**: Test cytarabine in modern SCLC cell lines (including SCLC-A/N/P/I subtypes) and patient-derived xenograft models to generate contemporary efficacy and resistance data
- **Regulatory pathway**: If evidence develops favorably, cytarabine would require full product registration in Saudi Arabia from the ground up, as no authorizations currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

