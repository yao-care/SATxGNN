---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Breast Cancer

## One-Sentence Summary

Olaparib is a PARP inhibitor originally developed for maintenance treatment of platinum-sensitive, BRCA-mutated relapsed ovarian, fallopian tube, or peritoneal cancer. The TxGNN model predicts it may also be effective for **female breast carcinoma**, a prediction already strongly corroborated by real-world evidence — **80 clinical trials** and **20 publications** are on file, including two pivotal completed Phase 3 RCTs (OlympiAD, OlympiA).

*Note: `taiwan_regulatory.licenses` and `drug.original_indications` are empty in this evidence pack — the original-indication description above is drawn from clinical trial descriptive text (NCT05078671), not from a formal regulatory record.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maintenance treatment of BRCA-mutated, platinum-sensitive relapsed ovarian, fallopian tube, or primary peritoneal cancer (sourced from trial text, not formal regulatory data) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record is not yet available in our data pipeline (flagged as a High-severity data gap). However, the mechanistic rationale is well established in the supporting literature: Olaparib is a PARP1/2 inhibitor that blocks base-excision repair (BER) of single-strand DNA breaks. In tumor cells with BRCA1/2 mutations or broader homologous recombination deficiency (HRD) — which are also deficient in double-strand break repair — this creates **synthetic lethality**, selectively killing tumor cells while sparing normal cells.

Ovarian cancer and breast cancer share substantial overlap in BRCA-driven, HRD-positive tumor biology, since BRCA1/2 germline mutations confer elevated risk for both cancers and produce tumors with the same repair-deficient phenotype. This shared biology is why the mechanism validated in ovarian cancer translates directly to BRCA-mutated and HRD-positive breast cancer.

This is not merely a theoretical extrapolation: the pivotal Phase 3 OlympiAD and OlympiA trials have already demonstrated clinically meaningful benefit of olaparib in gBRCA-mutated, HER2-negative breast cancer (both metastatic and high-risk early-stage settings), and Olaparib is approved for breast cancer indications by major regulators (FDA, EMA) elsewhere. In this evidence pack, the prediction functions largely as **regulatory catch-up** for a market (Saudi Arabia) where the drug is not yet marketed, rather than a purely novel biological hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | Rollover study continuing olaparib for patients already showing clinical benefit in parent oncology studies — reflects established long-term use pattern |
| [NCT05078671](https://clinicaltrials.gov/study/NCT05078671) | Phase 4 | Recruiting | 160 | Post-marketing PK-boosting study to improve exposure, tolerance and cost-effectiveness of approved olaparib regimens |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recruiting | 2900 | ComboMATCH — large genomically-matched basket trial with an olaparib arm for molecularly selected breast cancer |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC — personalized treatment of high-risk breast cancer using olaparib as a study drug |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab + radiotherapy ± olaparib in metastatic triple-negative/HR+ HER2- breast cancer |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib sequencing vs. capecitabine as first-line therapy in BRCA1/2-mutated HER2- advanced breast cancer |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after response to trabectedin-PLD in recurrent ovarian carcinoma (HRD biology directly relevant to breast cancer rationale) |
| [NCT07321015](https://clinicaltrials.gov/study/NCT07321015) | Phase 2 | Not yet recruiting | 72 | Maintenance fluzoparib (another PARP inhibitor) in platinum-sensitive advanced TNBC with/without BRCA1/2 mutation — class-level support |
| [NCT06545942](https://clinicaltrials.gov/study/NCT06545942) | Phase 1 | Active, not recruiting | 220 | MOMA-313 alone or combined with a PARP inhibitor in HRD-positive advanced/metastatic solid tumors |
| [NCT05700669](https://clinicaltrials.gov/study/NCT05700669) | Phase 1/2 | Completed | 3 | AsiDNA + olaparib basket study including breast cancer patients who progressed on prior PARP inhibitor therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT (Phase 3, OlympiA) | New England Journal of Medicine | Adjuvant olaparib significantly reduced recurrence in gBRCA1/2-mutated, high-risk early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT (Phase 3, OlympiAD) | New England Journal of Medicine | Olaparib showed antitumor activity and improved outcomes in metastatic breast cancer with germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT (Phase 3, OlympiAD) | Annals of Oncology | Final OS/tolerability results: olaparib improved PFS vs. chemotherapy of physician's choice in gBRCA-mutated HER2- metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT (Phase 3, OlympiAD extended) | European Journal of Cancer | Extended follow-up confirms olaparib's PFS benefit and manageable safety in gBRCA-mutated metastatic breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT (Phase 3, OlympiA) | Annals of Oncology | Overall survival analysis of adjuvant olaparib in gBRCA1/2-mutated, high-risk early breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT (Phase 2, TBCRC 048) | Journal of Clinical Oncology | Olaparib response in metastatic breast cancer with somatic BRCA or non-BRCA HR-pathway mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (Phase 2, I-SPY2) | Cancer Cell | Durvalumab + olaparib + paclitaxel increased pathologic complete response in high-risk HER2- breast cancer |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Phase 2 (NOBROLA) | Breast (Edinburgh, Scotland) | Olaparib monotherapy activity in HRD-positive, non-germline-BRCA-mutated advanced triple-negative breast cancer |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Phase IIIb / Real-world (LUCY) | Breast Cancer Research and Treatment | Real-world effectiveness and safety of olaparib in gBRCA-mutated, HER2- metastatic breast cancer, consistent with OlympiAD |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for gBRCA-mutated HER2- breast cancer |

---

## Saudi Arabia Market Information

Olaparib currently has **no marketing authorization on file** for Saudi Arabia (`market_status: 未上市`, 0 licenses recorded). No product/dosage-form registry data is available to populate an authorization table.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor acting via synthetic lethality — not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) — two independent, completed Phase 3 RCTs (OlympiAD, OlympiA) plus a substantial post-marketing/real-world dataset already establish olaparib's efficacy and general safety in BRCA-mutated/HRD breast cancer. However, Blocking-severity data gaps around Saudi Arabia-specific safety documentation and the drug's current "not marketed" status mean this cannot yet proceed as an unconditional "Go."

**To proceed, the following is needed:**
- SFDA-approved package insert (warnings, precautions, contraindications) — currently a Blocking data gap
- Formal DrugBank/regulatory mechanism-of-action record — currently a High-severity data gap
- Drug-drug interaction (DDI) profile — current query returned no data
- Saudi Arabia market entry/registration pathway assessment, since the product is not currently marketed there
- BRCA/HRD biomarker testing infrastructure and monitoring plan appropriate for local clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

