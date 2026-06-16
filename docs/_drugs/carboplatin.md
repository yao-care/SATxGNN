---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a second-generation platinum-based chemotherapy agent originally established for ovarian cancer treatment, with additional clinical use across lung, bladder, and head-and-neck cancers.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with the evidence base already at L1 — supported by **multiple completed Phase III RCTs** and **20 publications** — including the landmark GeparSixto trial, BCIRG-006, and the ongoing KEYNOTE-868 programme.
The prediction accurately reflects an indication where carboplatin has transitioned well beyond hypothesis into established clinical practice for specific subtypes, making expedited adoption appropriate with appropriate safeguards.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian cancer (established global clinical use; no Saudi Arabia registration on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carboplatin is a platinum coordination compound that forms interstrand DNA cross-links, triggering irreparable double-strand breaks and subsequent apoptosis. Detailed pharmacological data were not captured in the current Evidence Pack; however, carboplatin's mechanism is well-characterised from decades of clinical use. The key mechanistic insight is that tumour cells harbouring homologous recombination deficiency (HRD) — most commonly driven by BRCA1/2 mutations or epigenetic silencing of DNA repair genes — are unable to resolve platinum-induced DNA damage, rendering them exquisitely sensitive to carboplatin. This biological vulnerability is far more prevalent in breast cancer than in many other solid tumours.

Triple-negative breast cancer (TNBC) and HER2-positive breast cancer are the two subtypes where carboplatin's role is best established. TNBC lacks targetable hormone and HER2 receptors, leaving chemotherapy as the primary systemic treatment; the BRCA1/2 germline mutation rate in TNBC approaches 10–20%, and HRD rates (including non-BRCA causes) are higher still. In HER2-positive disease, the TCbHP regimen — docetaxel, carboplatin, trastuzumab, pertuzumab — exploits synergy between platinum-induced DNA damage and HER2 pathway blockade, achieving high pathologic complete response (pCR) rates without anthracycline-related cardiotoxicity. The functional connection between ovarian cancer (where HRD is endemic) and breast cancer is mechanistically direct: both tumour types share the BRCA1/2 mutation landscape, and carboplatin's efficacy in one predicts activity in the other.

The TxGNN model's 99.86% score for this repurposing direction is therefore not a speculative extrapolation — it reflects a graph-neural-network recognising an already well-validated biological connection. Clinical data have confirmed what the model predicts, making this among the strongest drug-indication pairings in the TxGNN output for carboplatin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3,222 | BCIRG-006: TCH (docetaxel/carboplatin/trastuzumab) vs AC-TH vs AC-T in HER2+ operable breast cancer. TCH demonstrated non-inferior disease-free survival with significantly lower cardiac toxicity than anthracycline-containing arms; foundational evidence establishing carboplatin as a standard adjuvant component in HER2+ disease |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Randomised Phase III: TCHP (docetaxel/carboplatin/trastuzumab/pertuzumab) ± oestrogen deprivation as neoadjuvant therapy for HR+/HER2+ locally advanced breast cancer; evaluates pCR as primary endpoint and confirmed carboplatin as core of the dual-HER2-blockade neoadjuvant backbone |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | Nab-paclitaxel + gemcitabine or carboplatin vs gemcitabine/carboplatin doublet as first-line treatment in triple-negative metastatic breast cancer; directly compares carboplatin-containing regimens in the TNBC first-line setting |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomised neoadjuvant: carboplatin/docetaxel vs carboplatin/paclitaxel followed by doxorubicin/cyclophosphamide in stage I–III TNBC; evaluates whether the pairing drug affects carboplatin's contribution to pCR |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | NACATRINE trial: neoadjuvant carboplatin in TNBC, with particular focus on BRCA1/2 mutation carriers; conducted in Brazil, demonstrating real-world feasibility across diverse populations |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | Active, not recruiting | 120 | Pembrolizumab + carboplatin/docetaxel neoadjuvant regimen in stage I–III TNBC; assesses whether PD-1 blockade synergises with carboplatin-induced immunogenic cell death to improve pCR |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC trial: epirubicin/cyclophosphamide followed by docetaxel/carboplatin in Nigerian women with TNBC; uses blood biomarkers to identify chemoresistance, extending carboplatin evidence to under-represented populations |
| [NCT04083963](https://clinicaltrials.gov/study/NCT04083963) | Phase 2 | Active, not recruiting | 13 | Weekly carboplatin + paclitaxel followed by doxorubicin/cyclophosphamide in operable TNBC; evaluates simplified weekly platinum scheduling for improved tolerability |
| [NCT07528898](https://clinicaltrials.gov/study/NCT07528898) | Phase 2 | Not yet recruiting | 100 | Response-guided neoadjuvant SHR-A1811 (anti-HER2 ADC) + pertuzumab vs standard carboplatin-based therapy in HER2+ early/locally advanced breast cancer; carboplatin arm serves as the current standard-of-care comparator |
| [NCT06234137](https://clinicaltrials.gov/study/NCT06234137) | N/A | Recruiting | 154 | Docetaxel/carboplatin + inetetamab + pyrotinib (TCbIP) as neoadjuvant therapy for locally advanced HER2+ breast cancer; evaluates total pathologic complete response (tpCR) and long-term event-free survival |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase II/III) | Lancet Oncology | GeparSixto: Adding carboplatin to neoadjuvant chemotherapy significantly improved pCR in TNBC (53.2% vs 36.9%; p=0.005) and showed a trend in HER2+ disease; established carboplatin as a neoadjuvant standard in TNBC |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | Phase II RCT | Clinical Cancer Research | NeoSTOP (multisite): Anthracycline-free carboplatin/taxane regimen achieved comparable pCR rates to anthracycline-containing carboplatin regimens in stage I–III TNBC, supporting carboplatin as sufficient backbone without anthracycline toxicity |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: Camrelizumab (anti-PD-1) combined with carboplatin-containing neoadjuvant chemotherapy significantly improved pCR vs chemotherapy alone in early/locally advanced TNBC; reflects carboplatin's continued role as immunotherapy backbone |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nature Communications | MUKDEN 06: ARX788 + pyrotinib vs standard TCbHP neoadjuvant in HER2+ breast cancer; TCHP arm (carboplatin-containing) used as the active comparator, confirming its status as the current gold-standard comparator in HER2+ neoadjuvant trials |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase III RCT | European Journal of Cancer | BROCADE3 final overall survival data: Veliparib + carboplatin/paclitaxel vs placebo + carboplatin/paclitaxel in BRCA1/2-mutated HER2-negative advanced breast cancer; improved PFS demonstrated; confirms carboplatin as preferred backbone in BRCA-mutated advanced disease |
| [35462344](https://pubmed.ncbi.nlm.nih.gov/35462344/) | 2022 | Individual-patient meta-analysis | Breast | Pooled individual-participant data meta-analysis confirms that adding carboplatin to neoadjuvant/adjuvant chemotherapy in TNBC improves both pCR rate and overall survival — resolving prior uncertainty on survival benefit |
| [40329228](https://pubmed.ncbi.nlm.nih.gov/40329228/) | 2025 | Real-world cohort | BMC Cancer | Multicenter real-world analysis: carboplatin in neoadjuvant chemotherapy improved pCR and survival in TNBC regardless of HER2-low or HER2-zero status, broadening the applicable population |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I/II | Breast Cancer Research and Treatment | Carboplatin + gemcitabine + mifepristone in advanced breast and ovarian cancer: mifepristone (glucocorticoid receptor antagonist) enhances carboplatin-induced apoptosis by blocking GR-mediated chemoresistance — mechanism-expanding combination |
| [40468999](https://pubmed.ncbi.nlm.nih.gov/40468999/) | 2025 | Phase II | Acta Oncologica | TCHL 5-year follow-up: TCH (docetaxel/carboplatin/trastuzumab) ± lapatinib as neoadjuvant for HER2+ breast cancer; long-term efficacy and serum biomarker predictors reported, supporting sustained carboplatin activity |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase II | Breast Cancer Research | Carboplatin + bevacizumab in breast cancer brain metastases: demonstrated meaningful intracranial responses in a population with very limited systemic options, expanding carboplatin's role into CNS-involved disease |

---

## Saudi Arabia Market Information

Carboplatin does not currently hold any drug authorizations in Saudi Arabia (0 registered products, market status: not marketed). Clinicians wishing to use carboplatin in Saudi Arabia would need to source it through special import authorisation or named-patient/compassionate use programmes under SFDA regulations.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum-based alkylating agent (second-generation platinum compound) |
| Myelosuppression Risk | **High** — Thrombocytopenia is the dose-limiting toxicity; neutropenia and anaemia are also common, especially in combination with taxanes. In the TCHP regimen, grade 3/4 anaemia occurred in up to 40% of patients, with dose reduction of carboplatin associated with reduced transfusion requirements (PMID 35837812). High-dose carboplatin regimens (AUC ≥6) carry greater risk. |
| Emetogenicity Classification | Moderate to high — Carboplatin at AUC ≥4 is classified as highly emetogenic per MASCC/ESMO guidelines; appropriate prophylactic antiemetic regimens (NK1 antagonist + 5-HT3 antagonist + dexamethasone) are required |
| Monitoring Items | Complete blood count with differential (before each cycle, and mid-cycle if high-dose); serum creatinine and calculated GFR (carboplatin dosing via Calvert formula requires accurate GFR); electrolytes (Mg²⁺, K⁺, Ca²⁺); audiological assessment for high-dose regimens (ototoxicity reported in salvage HD-carboplatin contexts); baseline and ongoing peripheral neuropathy assessment when combined with taxanes |
| Handling Protection | Must follow cytotoxic drug handling regulations; prepare under vertical laminar airflow biological safety cabinet (Class II or III); wear double chemotherapy gloves, impermeable gown, and eye/face protection; use closed-system drug transfer devices (CSTDs) to minimise aerosolisation; all waste classified as cytotoxic/hazardous waste |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: SFDA package insert data and key warnings/contraindications were not available in the current Evidence Pack (Data Gap DG001). A complete safety review — including renal function thresholds for dose reduction, pregnancy/lactation contraindications, and specific drug interaction warnings — must be conducted against the product package insert prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase III randomised trials (BCIRG-006: n=3,222; TCHP neoadjuvant: n=315; BROCADE3) and the pivotal GeparSixto Phase II/III trial collectively establish carboplatin as an evidence-based treatment option for female breast carcinoma — specifically in TNBC and HER2-positive subtypes — meeting the L1 evidence threshold for clinical adoption. The TxGNN model's 99.86% prediction score accurately reflects the strength of this pre-existing clinical evidence base.

**To proceed, the following is needed:**

- **Import authorisation**: Carboplatin is not currently registered in Saudi Arabia; procurement via SFDA special import or named-patient pathway must be arranged before clinical use
- **Safety data gap resolution**: Obtain and review the SFDA/product-specific package insert (Data Gap DG001) to confirm key warnings, contraindications, and dose adjustment criteria for renal impairment — mandatory before initiating treatment
- **MOA documentation**: Retrieve complete pharmacological data from DrugBank (Data Gap DG002) to support the institutional repurposing dossier
- **Patient selection criteria**: Define biomarker-driven eligibility — BRCA1/2 germline testing and HRD status assessment are strongly recommended, as carboplatin benefit is most pronounced in HRD-positive TNBC; subtype-specific protocols should be differentiated (TNBC vs HER2-positive)
- **Haematological monitoring protocol**: Establish pre-treatment baseline CBC, renal function (GFR for Calvert dosing), and electrolytes, with a cycle-by-cycle monitoring schedule and pre-defined dose-reduction thresholds for thrombocytopenia and anaemia
- **Audiological monitoring plan**: Required if high-dose carboplatin regimens (AUC >6) or salvage regimens with cumulative platinum exposure are considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

