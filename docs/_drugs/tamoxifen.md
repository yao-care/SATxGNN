---
layout: default
title: Tamoxifen
parent: 僅模型預測 (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Tamoxifen
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

Using the provided evidence pack directly (no applicable skill for this templated report-writing task) — here is the report.

---

# Tamoxifen: From Estrogen Receptor-Positive Breast Cancer to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is a selective estrogen receptor modulator (SERM) with a long-established role in treating estrogen receptor-positive breast cancer. The TxGNN model's top-ranked new signal is **Mammary Paget Disease**, a rare cutaneous manifestation of underlying ductal breast carcinoma, but this specific candidate is currently supported by only **1 indirectly relevant clinical trial** and **13 publications**, most of which are case reports.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Mammary Paget Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: The original approved indication could not be extracted — no market authorizations or original-indication records are present in this evidence pack (see Data Gap DG002, MOA).*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tamoxifen in this evidence pack (Data Gap DG002, severity: High). Based on known pharmacology, tamoxifen is a SERM that competitively antagonizes estrogen receptor (ER) signaling in breast tissue, and its efficacy in ER-positive breast cancer is well established in the broader literature — a fact reflected throughout this pack's other predicted indications (e.g., breast carcinoma in situ and ER-positive breast cancer, both supported by L1-level evidence from multiple completed Phase 3 RCTs such as NSABP B-17/B-24, RTOG 9804, and TAM-01).

Mammary Paget disease is a rare intraepidermal adenocarcinoma of the nipple-areola complex that, in the majority of cases, overlies an underlying ductal carcinoma in situ (DCIS) or invasive ductal carcinoma — most of which are ER-positive. The mechanistic rationale for tamoxifen is therefore an extension of its established role in ER-positive ductal breast cancer, rather than a novel mechanism specific to Paget disease itself.

However, this specific candidate indication is not directly validated: the single associated clinical trial (NCT00002920) tested medroxyprogesterone acetate for preventing tamoxifen-induced endometrial pathology, not tamoxifen's efficacy against Paget disease. The literature evidence is dominated by case reports and one retrospective cohort/meta-analysis, with tamoxifen appearing only incidentally in a minority of treated patients. No dedicated prospective or randomized study of tamoxifen for Paget disease exists in this pack.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Evaluated medroxyprogesterone acetate vs. observation to prevent endometrial pathology in postmenopausal breast cancer patients (including Paget's disease of the nipple) treated with tamoxifen. Addresses tamoxifen-associated endometrial safety monitoring, not efficacy against Paget disease itself. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Retrospective Cohort/Meta-analysis | Breast Care (Basel) | Compiled outcome data on Paget's disease of the breast; total local recurrence rate as high as 20–40% across surgical approaches. |
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case Report | Investigational New Drugs | Successful treatment of hormone receptor-positive metastatic extramammary Paget disease with tamoxifen. |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case Report | Breast (Edinburgh) | Extensive nipple Paget's disease responded to tamoxifen combined with radiation therapy. |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Case Series (n=48) | British Journal of Surgery | Series of Paget's disease of the nipple; treatments included mastectomy, cone excision, and tamoxifen (1 case). |
| [18288984](https://pubmed.ncbi.nlm.nih.gov/18288984/) | 2008 | Review | Current Medicinal Chemistry | Review of pharmacotherapies for bone-loss diseases; discusses estrogen receptor modulators including tamoxifen in cancer prevention/treatment context. |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case Report/Review | Il Giornale di Chirurgia | Male breast Paget's disease case; notes absence of standard treatment guidelines. |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case Report | Surgery Today | Synchronous bilateral breast cancer with Paget's disease and invasive ductal carcinoma. |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case Report | Arch Gynecol Obstet | Vulvar and breast Paget's disease with synchronous underlying cancer. |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case Report | American Surgeon | Paget's disease of the male breast; review of 32 world-literature cases. |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Case Series | Clinical Breast Cancer | Paget's disease of the nipple as local recurrence after breast-conservation treatment. |

## Cytotoxicity

Tamoxifen's DrugBank category data and formal toxicity classification are marked as a Data Gap in this evidence pack, but it is well established in general pharmacology as a hormonal (non-cytotoxic) antineoplastic agent used across ER-positive breast malignancies, including the predicted indication here.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/targeted therapy (SERM) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low — tamoxifen is not characteristically myelosuppressive |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function, endometrial/gynecological surveillance (estrogenic effect on endometrium), coagulation status (VTE risk); CBC if combined with cytotoxic regimens |
| Handling Protection | Tamoxifen appears on hazardous-drug lists (reproductive toxicity/carcinogenicity classification) in several institutional guidelines; handle per local hazardous-drug precautions despite its non-cytotoxic mechanism |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — TFDA package insert retrieval is flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, mammary Paget disease, has only L4-level evidence — case reports and one retrospective cohort — with no dedicated clinical trial testing tamoxifen's efficacy for this specific presentation. The single associated trial addresses tamoxifen safety monitoring, not treatment efficacy.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank
- Drug-drug interaction data (currently not found)
- A dedicated prospective study or case series specifically evaluating tamoxifen efficacy in mammary Paget disease
- Note: this evidence pack also contains two other predicted indications for tamoxifen — **breast carcinoma in situ** (rank 4) and **estrogen-receptor positive breast cancer** (rank 8) — both rated L1 with multiple completed Phase 3 RCTs and a "Proceed with Guardrails" recommendation; these represent substantially stronger, near-established candidates and may warrant separate prioritized review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

