---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 2
---

# Larotrectinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Larotrectinib: From NTRK Fusion-Positive Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is a first-in-class, tumor-agnostic TRK inhibitor whose globally recognized approved use is for NTRK gene fusion–positive solid tumors (Saudi Arabia–specific approval status is not confirmed in this evidence pack). The TxGNN model predicts possible efficacy in **Multiple Endocrine Neoplasia**, currently supported by **1 clinical trial** (a genotype-matched basket trial, not disease-specific) and **2 publications**. Evidence for this specific indication remains preliminary and largely mechanistic rather than confirmatory.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTRK gene fusion-positive solid tumors (general/global knowledge; no Saudi Arabia license record found in this evidence pack) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 (mechanism/case-level evidence; the one registered trial is an active, not-completed basket study not specific to this indication) |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for larotrectinib is not available in this evidence pack (Data Gap DG002). Based on known information, larotrectinib is a selective, ATP-competitive inhibitor of the tropomyosin receptor kinases (TRKA/B/C, encoded by NTRK1/2/3), and its efficacy in NTRK fusion–driven solid tumors is well established internationally as a tissue-agnostic therapy.

Multiple endocrine neoplasia (particularly the MEN2/medullary thyroid carcinoma phenotype) is primarily driven by activating mutations in the RET proto-oncogene rather than NTRK fusions. The mechanistic link proposed here is therefore indirect: RET and TRK are both receptor tyrosine kinases that converge on overlapping downstream signaling (RAS/MAPK, PI3K/AKT) pathways, and the supporting literature (e.g., PMID 38438731) specifically discusses RET-driven thyroid cancer and resistance mechanisms relevant to TRK/RET inhibitor class effects rather than larotrectinib efficacy in MEN itself.

Because this rationale rests on shared pathway biology rather than a direct target match, it should be regarded as hypothesis-generating. The single registered trial (MATCH) is a broad genotype-matched screening study across many tumor types, not a MEN-specific trial, which further limits how much can be concluded at this stage.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | MATCH basket trial assigning genotype-directed targeted therapy to refractory advanced solid tumors/lymphomas/myelomas; not specific to multiple endocrine neoplasia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Overview of kinase-inhibitor therapy for advanced thyroid cancer, including mutation-specific (RET/NTRK-directed) agents |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Case Report | NPJ Precision Oncology | Case of RET-driven medullary thyroid carcinoma developing resistance to RET-selective TKI therapy; informs cross-kinase resistance mechanisms relevant to TRK-pathway inhibitors |

## Saudi Arabia Market Information

Larotrectinib is currently not marketed in Saudi Arabia, and no authorization records are available in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRK kinase inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Low, based on the internationally known drug-class profile of TRK inhibitors; not confirmed against local (Saudi) toxicity data (see Data Gap DG001) |
| Emetogenicity Classification | Low, typical for oral targeted kinase inhibitors |
| Monitoring Items | Liver function tests, CBC, and (in pediatric patients) growth and neurodevelopmental monitoring, per internationally published prescribing information |
| Handling Protection | Standard oral oncology drug handling; formal hazardous-drug handling classification should follow local institutional policy pending Saudi package insert confirmation |

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data for this drug are not yet available in this evidence pack (Data Gap DG001, severity: Blocking) — this must be resolved before any S1 safety screening can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between larotrectinib and multiple endocrine neoplasia is indirect (RET-driven biology, not direct NTRK fusion overlap), the only registered trial is a non-disease-specific basket study, and a Blocking-severity safety data gap (TFDA/SFDA package insert) prevents initial safety screening.

**To proceed, the following is needed:**
- Saudi Arabia (SFDA) package insert warnings/contraindications (resolves DG001, Blocking)
- Confirmed DrugBank mechanism-of-action and categorization data (resolves DG002)
- A disease-specific (not basket-design) trial or observational study in multiple endocrine neoplasia
- Confirmation of Saudi Arabia regulatory/market status for larotrectinib

*Note:* TxGNN also flagged **HER2-positive breast carcinoma** (score 99.14%) as a secondary candidate for this drug, but evidence is currently thinner — zero registered trials and only one preclinical publication (PMID 38852701, combination TrkA/JAK2 inhibition study) — and would need independent evaluation if pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

