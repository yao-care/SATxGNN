---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# DACARBAZINE: From Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is a classic alkylating cytotoxic agent widely established as a first-line reference therapy for advanced melanoma and as part of the ABVD combination regimen for Hodgkin's lymphoma.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm**, with **1 clinical trial** (using the structurally related agent temozolomide, not Dacarbazine directly) and **20 publications** of mixed relevance currently identified.
Direct clinical evidence supporting Dacarbazine in this specific indication remains sparse, and the current evidence base supports a **Hold** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Melanoma (confirmed as standard first-line comparator in Phase 3 RCT literature); not formally registered in Saudi Arabia |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dacarbazine (DTIC) is a conventional triazene alkylating agent that undergoes hepatic microsomal oxidation to produce the active intermediate MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide). MTIC methylates DNA preferentially at the O6-guanine position, resulting in DNA double-strand breaks and downstream apoptosis in rapidly proliferating cells. This mechanism is shared with temozolomide, the oral second-generation analog that spontaneously decomposes to the identical MTIC intermediate — a fact that allows temozolomide clinical data to serve as a mechanistic (though not regulatory) proxy for Dacarbazine.

Upper aerodigestive tract neoplasms encompass cancers arising from the oral cavity, pharynx, larynx, nasal cavity, and esophagus. These are predominantly fast-dividing epithelial tumors, and in principle the alkylating mechanism of MTIC could confer antiproliferative activity. Historically, Dacarbazine-containing combination regimens (e.g., CYVADIC) have been used in rare head and neck tumor subtypes such as angiosarcoma, and Dacarbazine plus 5-FU has been explored in advanced medullary thyroid carcinoma — a neuroendocrine tumor of the thyroid, anatomically within the aerodigestive region — providing limited but tangible mechanistic precedent.

However, clinical translation faces significant barriers. The only registered trial in this indication used temozolomide (not Dacarbazine) and was terminated early; published results showed that MGMT promoter methylation did not reliably predict response in aerodigestive tract tumors. Squamous cell carcinomas and adenocarcinomas of this region generally show low sensitivity to alkylating agents compared to melanoma or Hodgkin's lymphoma. The TxGNN prediction is mechanistically plausible through the MTIC pathway, but direct evidence is currently insufficient to move beyond a preclinical/mechanistic rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Evaluated **temozolomide** (SCH 52365) — not Dacarbazine — in patients with MGMT-methylated advanced aerodigestive tract and colorectal cancers (head and neck, esophageal, NSCLC, CRC). Trial was terminated. Published results (PMID 23443801) showed MGMT methylation did not reliably predict response. Indirect evidence only: temozolomide shares Dacarbazine's active MTIC metabolite but is a distinct molecular entity with different pharmacokinetics and regulatory approval profile. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase 3 RCT | JAMA Oncology | Toripalimab vs Dacarbazine as first-line therapy for advanced acral melanoma (MELATORCH trial); Dacarbazine serves as the standard-of-care control arm, confirming its role as an established reference treatment |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Pilot clinical study | Annals of Oncology | **Direct use of Dacarbazine + 5-FU** in advanced medullary thyroid carcinoma (MTC), a neuroendocrine tumor of the aerodigestive region; limited activity observed, supporting biological rationale in neuroendocrine subtypes |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Review / Case series | Cancer & Chemotherapy | CYVADIC regimen (includes **DTIC/Dacarbazine**) used for angiosarcoma of the head and neck in elderly patients; combination chemotherapy with historically poor outcomes |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 single-arm trial | Molecular Cancer Therapeutics | Temozolomide in MGMT-methylated aerodigestive tract and colorectal cancers; MGMT status did not predict response reliably; indirect evidence that MTIC-based alkylation has limited single-agent activity in this tumor class |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Retrospective case series | Ear, Nose & Throat Journal | Clinicopathological and genetic features of malignant head and neck paragangliomas in 6 patients; explores treatment options including chemotherapy for this rare aerodigestive neuroendocrine subtype |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective cohort | Int J Radiation Oncology Biology Physics | Radiotherapy outcomes for esthesioneuroblastoma (olfactory neuroblastoma); chemotherapy used in combination for intranasal malignancies, providing treatment context for rare upper aerodigestive tract tumors |
| [3153227](https://pubmed.ncbi.nlm.nih.gov/3153227/) | 1986 | Case report | Pediatric Hematology and Oncology | Olfactory neuroblastoma in a 2-year-old; **DTIC-containing combination chemotherapy** used alongside cyclophosphamide; one of the few direct pediatric case reports implicating Dacarbazine in an upper aerodigestive tract tumor |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clinical Oncology | Comprehensive review of medullary thyroid carcinoma management including chemotherapy options for advanced/refractory disease; contextualizes Dacarbazine within MTC treatment history |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Review | Transfusion and Apheresis Science | Hodgkin lymphoma in HIV-infected patients with prominent head and neck lymphadenopathy; ABVD (dacarbazine-containing regimen) discussed; provides context for Dacarbazine's established role in lymphoma |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Epidemiological review | J Cancer Research & Clinical Oncology | Global burden of EBV-related cancers including nasopharyngeal carcinoma (an upper aerodigestive tumor); epidemiological context for the target tumor class only |

---

## Saudi Arabia Market Information

Dacarbazine is currently **not marketed in Saudi Arabia** (0 registered authorizations). No product license data is available. Any clinical use would require compassionate use authorization or an import permit under special circumstances.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (triazene class; prodrug activated to MTIC) |
| Myelosuppression Risk | High — leukopenia and thrombocytopenia are dose-limiting toxicities; bone marrow nadir typically occurs at 3–4 weeks post-infusion |
| Emetogenicity Classification | Moderate to High — Dacarbazine is considered a highly emetogenic agent at standard doses; 5-HT3 antagonist plus dexamethasone prophylaxis is required |
| Monitoring Items | CBC with differential (at baseline and before each cycle), liver function tests (ALT/AST/bilirubin), serum creatinine and BUN, electrolytes |
| Handling Protection | Preparation and administration must follow cytotoxic drug handling regulations; biological safety cabinet required; appropriate PPE (double gloves, closed-front gown, eye protection) mandatory |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.26%), the mechanistic basis relies on indirect analogy through the shared MTIC metabolite with temozolomide, and the only identified clinical trial for this indication used temozolomide — not Dacarbazine — and was terminated early with limited efficacy signal. Direct evidence for Dacarbazine in upper aerodigestive tract neoplasms is confined to small historical case series in rare subtypes (angiosarcoma, medullary thyroid carcinoma, olfactory neuroblastoma), which is insufficient to support clinical repurposing at this stage.

**To proceed, the following is needed:**

- **Formal MOA documentation**: Retrieve complete DrugBank mechanism of action data (currently a data gap) to strengthen the mechanistic rationale narrative
- **Safety review**: Obtain and parse the package insert (TFDA or EMA SmPC) to populate key warnings and contraindications before any safety assessment can proceed
- **Biomarker strategy**: Assess whether MGMT promoter methylation or other DNA repair pathway deficiencies can identify an aerodigestive tract subpopulation sensitive to alkylating agents
- **Preclinical validation**: Commission or identify in vitro studies of Dacarbazine activity against representative aerodigestive tract tumor cell lines (squamous, neuroendocrine subtypes)
- **Regulatory pathway**: Given zero Saudi Arabia authorizations, map a compassionate use or import permit framework before any clinical application
- **Trial differentiation from TMZ**: Clarify whether Dacarbazine offers a distinct clinical advantage over the oral temozolomide route in this setting, given that TMZ trials have already been attempted and showed limited benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

