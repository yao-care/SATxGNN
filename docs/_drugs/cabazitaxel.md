---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a next-generation taxane approved by the FDA for metastatic castration-resistant prostate cancer (mCRPC) that has progressed after docetaxel-based regimens.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **0 registered clinical trials** and **20 publications** (including 1 Phase II RCT) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), post-docetaxel |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, cabazitaxel belongs to the taxane class (like paclitaxel and docetaxel) and acts by stabilizing microtubules, thereby blocking mitotic progression and triggering apoptosis in rapidly dividing tumor cells. A key distinguishing feature is its markedly reduced affinity for P-glycoprotein (P-gp), the major multidrug-resistance efflux pump — this makes it active in settings where paclitaxel and docetaxel have lost efficacy due to P-gp overexpression.

Breast cancer is one of the most taxane-sensitive solid tumors, and paclitaxel/docetaxel are cornerstones of both early-stage and metastatic treatment. Because cabazitaxel shares the same microtubule-stabilizing mechanism while circumventing P-gp–mediated resistance, its extension into breast cancer — particularly in taxane-pretreated or triple-negative (TNBC) settings — is mechanistically well-justified. The GENEVIEVE Phase II RCT (PMID 28768217) directly tested cabazitaxel as neoadjuvant therapy in HER2-negative breast cancer, providing the strongest available clinical validation.

An additional mechanistic angle comes from preclinical TNBC research (PMID 33753567) showing that cabazitaxel repolarises tumour-associated macrophages (TAMs) to enhance CD47-blockade immunotherapy. This immunomodulatory effect is distinct from its cytotoxic activity and opens the door to combination strategies in TNBC, a subtype with limited therapeutic options and high unmet need.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cabazitaxel in female breast carcinoma.

> **Note:** The GENEVIEVE study (PMID 28768217) was a published Phase II RCT not captured in ClinicalTrials.gov/ICTRP query results. This trial constitutes the primary clinical evidence supporting L2 classification.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | European Journal of Cancer | GENEVIEVE study: cabazitaxel vs. weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer (triple-negative or luminal B); compared pathological complete response (pCR) rates |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | European Journal of Cancer | Dose-escalation study of cabazitaxel + capecitabine in metastatic breast cancer previously treated with anthracyclines and taxanes; established MTD, safety, PK, and preliminary activity |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Clinical PK Review | British Journal of Clinical Pharmacology | Comprehensive review of TDM-based dose personalisation for taxanes (paclitaxel, docetaxel, cabazitaxel, nab-paclitaxel); PK–PD relationships and clinical use considerations |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical (in vitro/in vivo) | Journal for Immunotherapy of Cancer | Cabazitaxel repolarises tumour-associated macrophages in TNBC, synergising with CD47-targeted immunotherapy to enhance programmed cell removal (PrCR); novel immunomodulatory mechanism |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | Cabazitaxel-loaded PACA nanoparticles evaluated in patient-derived TNBC xenograft; prior results showed complete remission in 6/8 tumors vs. free drug |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | PEBCA nanoparticle-encapsulated cabazitaxel achieved complete remission in 6/8 basal-like PDX breast cancer tumors vs. 1/8 with free drug; superior efficacy via nanoformulation |
| [36918084](https://pubmed.ncbi.nlm.nih.gov/36918084/) | 2023 | Preclinical | Journal of Controlled Release | Redox-responsive chondroitin sulfate nanomedicine co-delivering cabazitaxel + dasatinib to target CAF–tumor crosstalk in breast cancer; reduced invasion and metastasis in vivo |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Preclinical | Bioconjugate Chemistry | Cyclic cell-penetrating peptide conjugated cabazitaxel targeting integrin and EDB-fibronectin biomarkers for selective delivery in breast and prostate cancer models |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chemistry and Physics of Lipids | Cabazitaxel + thymoquinone co-loaded lipospheres exploit dual mechanism (microtubule inhibition + HDAC inhibition) against breast tumors; modulation of p53, STAT3, Bax/BCL-2 |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | Mechanisms of cabazitaxel resistance characterised in MCF-7 breast cancer cell models; cabazitaxel showed significantly lower cross-resistance than paclitaxel/docetaxel in MDR variants |

---

## Saudi Arabia Market Information

Cabazitaxel is currently not marketed in Saudi Arabia and holds no SFDA authorizations.

---

## Cytotoxicity

Cabazitaxel is a cytotoxic antineoplastic agent (taxane class). The following assessment is based on its established pharmacological profile.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (semisynthetic taxoid, microtubule stabiliser) |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia reported in ~8% of patients in pivotal trials. G-CSF prophylaxis is required per current guidelines. Anaemia and thrombocytopenia also occur. |
| Emetogenicity Classification | Low to moderate (similar to docetaxel) |
| Monitoring Items | CBC with differential (before each cycle and between cycles as clinically indicated), serum creatinine, hepatic transaminases (ALT/AST), bilirubin, electrolytes; neurological assessment for peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations — double-glove, closed-system drug transfer devices (CSTDs) recommended; biohazard disposal required |

---

## Safety Considerations

Please refer to the package insert for warnings, contraindications, and drug interaction information. No local SFDA label data is currently available; the EU/FDA SmPC should be consulted as the primary safety reference.

Key pharmacological safety signals known from the drug class:
- **Myelosuppression:** Severe neutropenia is the principal toxicity. Primary G-CSF prophylaxis is strongly recommended, particularly in patients ≥65 years or with risk factors.
- **Hypersensitivity:** Premedication with antihistamines, corticosteroids, and H2-blockers is required before each infusion.
- **Renal impairment:** Use in patients with creatinine clearance <15 mL/min is not recommended.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The GENEVIEVE Phase II RCT directly demonstrates cabazitaxel's clinical activity in HER2-negative breast cancer, providing L2-level evidence that, combined with a well-understood taxane mechanism of action and emerging TNBC immunotherapy synergy data, establishes a credible and evidence-backed repurposing hypothesis.

**To proceed, the following is needed:**

- **Formal MOA documentation:** Obtain full DrugBank record for DB06772 to complete the mechanistic link analysis
- **Saudi Arabia regulatory strategy:** File SFDA new drug application or explore named-patient / compassionate use pathway, as cabazitaxel is not currently registered in Saudi Arabia
- **Safety baseline:** Retrieve official prescribing information (EU SmPC or FDA label) to populate warnings, contraindications, and drug-drug interaction data
- **Clinical trial review:** Conduct expanded search for cabazitaxel breast cancer trials beyond the ClinicalTrials.gov/ICTRP query (e.g., EU Clinical Trials Register, ANZCTR) to identify whether Phase III data exists in specific breast cancer subtypes (TNBC, luminal B)
- **Subtype-specific evidence stratification:** Separate evidence by breast cancer subtype (TNBC vs. HR+/HER2- vs. HER2+) to identify the population with the strongest benefit–risk profile for a Saudi Arabia pilot study
- **G-CSF protocol:** Establish mandatory G-CSF prophylaxis protocol before any clinical use, given the high febrile neutropenia risk in new patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

