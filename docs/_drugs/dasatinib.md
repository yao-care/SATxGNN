---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is a multi-targeted tyrosine kinase inhibitor globally approved for Chronic Myeloid Leukemia (CML) and Philadelphia chromosome-positive Acute Lymphoblastic Leukemia (Ph+ ALL), though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Ewing Sarcoma** (rank #1, prediction score 99.90%), a rare and aggressive bone tumor predominantly affecting adolescents and young adults.
This direction is currently supported by **3 clinical trials** (including one completed Phase 2 trial in advanced sarcomas, n=366) and **9 publications** documenting Src kinase signaling as a targetable pathway in Ewing sarcoma biology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukemia (CML) / Ph+ ALL (global approval; not registered in Saudi Arabia) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (data gap DG002). Based on known pharmacological information and the repurposing rationale documented in the evidence pack, dasatinib is a multi-targeted inhibitor of BCR-ABL, Src family kinases, c-KIT, and PDGFR. Its established efficacy in BCR-ABL-driven hematologic malignancies provides the pharmacological foundation from which this repurposing prediction emerges.

The biological link to Ewing sarcoma centres on Src family kinase signalling. Multiple in vitro studies published between 2007 and 2022 consistently demonstrate that microenvironmental stress — hypoxia and nutrient deprivation within the tumour — upregulates Src activity in Ewing sarcoma cells, promoting invadopodia formation, invasive migration, and metastatic progression (PMID 27566104, 31521948, 35655525). Early preclinical work confirmed that dasatinib exhibits antiproliferative and antimigratory activity in Ewing sarcoma cell lines through inhibition of c-KIT, PDGFR, and Src (PMID 18202781, 17363602).

Clinically, a large Phase 2 basket trial (NCT00464620, n=366) has tested dasatinib across multiple advanced sarcoma subtypes including Ewing sarcoma. However, dasatinib failed as a single agent in this setting, with low overall response rates. The current evidence supports exploring dasatinib in combination strategies — for example, dual FAK+Src inhibition or dasatinib added to standard chemotherapy backbones — rather than single-agent use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Largest available clinical evidence: dasatinib in advanced sarcomas (multiple subtypes including Ewing sarcoma). Primary endpoints were objective response rate and 6-month progression-free survival. Single-agent activity was limited; Ewing-specific subgroup outcomes require the primary publication for detailed interpretation. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric study of dasatinib combined with ifosfamide, carboplatin, and etoposide in pediatric sarcomas (including Ewing sarcoma). Terminated extremely early due to insufficient enrollment (n=7 of planned target); no efficacy conclusions can be drawn. Provides limited combination safety data only. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy in paediatric relapsed/refractory solid tumours expressing B7-H3 target (includes Ewing sarcoma). Dasatinib appears in a supportive role as a CAR-T proliferation enhancer rather than as the primary investigational agent; limited direct relevance to dasatinib efficacy assessment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Research | Foundational study: dasatinib inhibits migration and invasion across diverse human sarcoma cell lines; bone sarcoma cells dependent on Src kinase for survival undergo dasatinib-induced apoptosis. Established the Src-targeting rationale for sarcomas. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncology Reports | Dasatinib demonstrates antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines through inhibition of c-KIT and PDGFR. Direct in vitro evidence in ES cell lines. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | In vitro / Mechanistic | Neoplasia | Microenvironmental stress (hypoxia/nutrient deprivation) activates Src-dependent invadopodia formation and cell migration in Ewing sarcoma; dasatinib blocks these Src-mediated effects, implicating tumour microenvironment as a key context for treatment. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | In vitro / Mechanistic | Neoplasia | Tenascin-C and Src cooperate to drive invadopodia-mediated invasion in Ewing sarcoma under microenvironmental stress; identifies a dasatinib-targetable signalling axis as a mediator of metastatic progression. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Translational / In vitro | Sarcoma | Targeting FAK-Src complex in Ewing sarcoma, DSRCT, and rhabdomyosarcoma; single-agent dasatinib failed in Phase 2 (NCT00464620), but combined FAK+Src inhibition restores in vitro activity, suggesting combination as a viable next step. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signalling in sarcoma biology covering cell proliferation, apoptosis, invasion, metastasis, and tumour microenvironment; supports dasatinib as a molecularly rational therapeutic approach across sarcoma subtypes. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | In vitro | Cell Communication and Signaling | CXCR4 antagonism activates receptor tyrosine kinase signalling in Ewing sarcoma cells; contextualises the receptor tyrosine kinase network that dasatinib targets and potential for combinations with chemokine axis agents. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Current Treatment Options in Oncology | Systemic therapy review for chondrosarcoma discussing antiangiogenic and targeted therapies including Src/PDGFR inhibitors; contextualises the broader bone tumour landscape for molecularly targeted approaches. Indirect relevance. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case Report | Case Reports in Oncology | Rare chromosomal abnormality in CML blast crisis illustrating BCR-ABL/TKI resistance mechanisms; peripheral relevance to Ewing sarcoma, included for completeness of dasatinib mechanistic context. |

---

## Saudi Arabia Market Information

Dasatinib is **not currently registered** in Saudi Arabia. No marketing authorisation records are available in the SFDA database at data cutoff (2026-06-16). Procurement would require import under a compassionate use or named-patient programme framework.

---

## Cytotoxicity

Dasatinib is an antineoplastic agent (targeted therapy indicated for leukaemia) and this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-targeted tyrosine kinase inhibitor (BCR-ABL, Src family kinases, c-KIT, PDGFR-β); not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (CBC) with differential; liver function tests; renal function; respiratory monitoring for pulmonary complications (interstitial pneumonitis and pleural effusion reported in CML literature: PMID 36346055, PMID 36448074) |
| Handling Protection | Standard oncology drug handling procedures apply; consult institutional cytotoxic drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Adverse events noted in the available literature** (derived from evidence collected for the myeloid leukemia indication):
> - **Pleural effusion / chylothorax** (PMID 36448074): Rare chylothorax reported in an 18-year-old CML patient on long-term dasatinib; pleural effusion is more broadly documented with dasatinib use
> - **Interstitial pneumonitis** (PMID 36346055): Case series identifies dasatinib-associated pulmonary toxicity as an under-reported but clinically significant concern requiring active respiratory monitoring

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Dasatinib has a mechanistically plausible and consistently supported preclinical basis for activity in Ewing sarcoma via Src family kinase inhibition, but the only completed clinical trial (Phase 2 basket trial NCT00464620) demonstrated limited single-agent activity in sarcomas broadly, and no Ewing sarcoma-specific clinical efficacy data is currently available in this pack. The evidence base is insufficient to justify direct clinical deployment without further targeted investigation.

**To proceed, the following is needed:**
- Retrieve Ewing sarcoma-specific subgroup outcomes from the NCT00464620 primary publication to quantify clinical response rates in this histology
- Explore dasatinib combination strategies informed by the preclinical literature — particularly dual FAK+Src inhibition (per PMID 35655525) or dasatinib added to standard chemotherapy (e.g., ICE regimen)
- Obtain full MOA data from DrugBank (data gap DG002) to complete the mechanistic rationale analysis
- Obtain Saudi Arabia/SFDA package insert or equivalent regulatory document (data gap DG001) before any clinical safety evaluation
- Consider in vivo (xenograft or PDX) validation of dasatinib ± combination in Ewing sarcoma models as a prerequisite before designing a new clinical trial
- Evaluate paediatric pharmacokinetic considerations given that Ewing sarcoma primarily affects adolescents and young adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

