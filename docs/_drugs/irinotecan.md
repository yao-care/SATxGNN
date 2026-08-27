---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 1
---

# Irinotecan
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

# Irinotecan: From Colorectal Cancer to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan (DB00762) is a topoisomerase I inhibitor prodrug historically used in colorectal cancer chemotherapy. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **22 clinical trials** and **20 publications** currently identified, though only a small subset directly studies irinotecan itself in breast cancer — most of the strongest literature concerns SN-38 (irinotecan's active metabolite) delivered via the antibody-drug conjugate sacituzumab govitecan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (known clinical use; not captured in the structured `original_indications` field — see Data Gap note below) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this Evidence Pack (`original_moa` = Data Gap). Based on known pharmacology, irinotecan is a camptothecin-class prodrug that is converted in vivo to its active metabolite SN-38, which inhibits Topoisomerase I. This causes accumulation of single-strand DNA breaks, S-phase cell cycle arrest, and apoptosis — a broad-spectrum cytotoxic mechanism rather than a breast-cancer-specific target.

Because this mechanism acts on rapidly dividing cells generally, it is plausible against breast cancer as well as colorectal cancer, and this is best understood as re-validation of an existing broad-spectrum cytotoxic agent in a new tumor type, rather than a novel mechanistic hypothesis. Consistent with this, a meaningful share of the supporting evidence comes not from irinotecan itself but from sacituzumab govitecan, a Trop-2-targeted antibody-drug conjugate that delivers the same active moiety (SN-38) directly to breast tumor cells — an indirect but mechanistically coherent line of support.

Direct clinical evidence for irinotecan itself in breast cancer does exist (e.g., single-agent and combination Phase I/II trials), but it remains limited in scale and mostly historical, so this signal should be treated as a research-stage repurposing candidate rather than an established therapeutic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Randomized, open-label trial of single-agent irinotecan (two dosing schedules) in metastatic breast cancer after anthracycline/taxane/capecitabine failure — most direct evidence available. |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast cancer; small sample but directly tests the drug/indication pair. |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Third-line-or-later single-agent irinotecan in locally recurrent/metastatic breast cancer in Chinese patients previously treated with anthracyclines and taxanes. |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 plus irinotecan in resistant solid tumors, with a dedicated Part II cohort in triple-negative recurrent breast cancer. |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Basket study of navicixizumab alone or with paclitaxel/irinotecan, including a TNBC cohort (Cohort C). |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | MM-398 (nanoliposomal irinotecan, Nal-IRI) tumor drug-level and imaging feasibility study across solid tumors. |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | IMMU-132 (SN-38 antibody-drug conjugate, precursor to sacituzumab govitecan) in epithelial cancers including breast. |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | Completed | 38 | Irinotecan combined with gemcitabine in unresectable/metastatic solid tumors. |
| [NCT02033551](https://clinicaltrials.gov/study/NCT02033551) | Phase 1 | Completed | 47 | Extension study of veliparib alone or with carboplatin/paclitaxel or FOLFIRI (irinotecan-containing regimen) in solid tumors. |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101, a nanoparticle formulation of SN-38 (irinotecan's active metabolite), dose-finding study in advanced solid tumors. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | RCT | Future Oncology | TROPiCS-02 Phase III trial design: sacituzumab govitecan (SN-38 payload) in HR+/HER2- metastatic breast cancer. |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | RCT/Cohort (Phase 2) | New England Journal of Medicine | ASCENT trial: sacituzumab govitecan in refractory metastatic triple-negative breast cancer, delivering high SN-38 concentrations to tumor. |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | RCT/Subgroup | Journal of Clinical Oncology | Sacituzumab govitecan efficacy in HR+/HER2- endocrine-resistant metastatic breast cancer. |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Phase 1/2 | Journal of Clinical Oncology | Sacituzumab govitecan (SN-38 ADC) in heavily pretreated metastatic triple-negative breast cancer. |
| [32727805](https://pubmed.ncbi.nlm.nih.gov/32727805/) | 2020 | Pilot clinical study | Anticancer Research | Direct pilot study of irinotecan + S-1 (IRIS regimen) for advanced/metastatic breast cancer. |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review/Rationale | Oncology (Williston Park) | Rationale for mitomycin and irinotecan combination use in advanced breast cancer, based on topoisomerase I upregulation. |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | Broad review of irinotecan (CPT-11) antitumor activity, explicitly including breast cancer among responsive tumor types. |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical | Anticancer Research | Irinotecan halted or regressed growth in human breast cancer xenograft models (MCF7, MDA-MB-231, T47D). |
| [26101915](https://pubmed.ncbi.nlm.nih.gov/26101915/) | 2015 | Preclinical/Mechanistic | Oncotarget | Trop-2 as a target for SN-38 (irinotecan active metabolite) delivery via antibody-drug conjugate. |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Phase 1 (first-in-human) | Clinical Cancer Research | First-in-human trial of the anti-Trop-2/SN-38 conjugate sacituzumab govitecan across diverse metastatic solid tumors. |

---

## Saudi Arabia Market Information

No marketing authorizations are currently on record for irinotecan in Saudi Arabia (market status: 未上市 / not marketed; total licenses: 0).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin-class prodrug) |
| Myelosuppression Risk | High — irinotecan is well established to cause dose-limiting neutropenia, including febrile neutropenia; severe acute and delayed diarrhea is also a hallmark toxicity. Institution-specific toxicity/label data is pending TFDA package insert review (see Safety Considerations). |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential (neutrophils in particular), liver function, renal function, electrolytes, bowel/diarrhea monitoring |
| Handling Protection | Requires cytotoxic/hazardous drug handling precautions per institutional protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. Local TFDA-equivalent warning and contraindication data could not be retrieved for this drug (blocking data gap — see below), and no drug-drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug is not currently marketed in this jurisdiction, and a blocking data gap (missing local package insert warnings/contraindications) prevents completion of the S1 safety pre-assessment. Clinical evidence for irinotecan itself in breast cancer is Evidence Level L2 (one completed Phase 2 trial), with most higher-quality trial data actually supporting a related but distinct agent (sacituzumab govitecan). This positions the candidate at the "Research Question" stage rather than ready for a Go/Guardrails decision.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings, contraindications, DDI) to complete the S1 safety evaluation (blocking gap)
- Confirmed DrugBank mechanism-of-action record for irinotecan
- Clarification of whether irinotecan-specific evidence (vs. SN-38-ADC evidence) is sufficient on its own to support the indication, or whether this should be reframed as support for an SN-38-conjugate class effect
- Route-of-administration compatibility assessment (currently pending in evidence pack)
- Local market/regulatory pathway confirmation given current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

