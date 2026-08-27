---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR inhibitor originally developed for advanced renal cell carcinoma, pancreatic/GI neuroendocrine tumours, tuberous sclerosis-associated tumours, and prevention of organ transplant rejection. The TxGNN model's top-ranked new signal is **Liposarcoma**, supported by **1 active Phase 2 clinical trial** and **5 publications**, though the drug's overall evidence portfolio is strongest for a different candidate — **unclassified renal cell carcinoma** — which has two completed head-to-head Phase 2 RCTs (see Portfolio Overview below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local (Saudi Arabia) regulatory data — drug is not marketed there. Internationally, everolimus is approved for advanced renal cell carcinoma, pancreatic/GI/lung neuroendocrine tumours, tuberous sclerosis-associated SEGA/renal angiomyolipoma, HR+/HER2- breast cancer (with exemestane), and prevention of organ transplant rejection. |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (Hold pending trial readout) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack, remediation: query DrugBank API). Based on known pharmacology, everolimus is an mTOR (mammalian target of rapamycin) inhibitor, a class already validated in oncology for tumours driven by PI3K/Akt/mTOR pathway activation.

Dedifferentiated liposarcoma has documented activation of the Akt-mTOR and MAPK pathways, which provides a mechanistic rationale for mTOR-directed therapy. This is consistent with everolimus's known activity in other mTOR-pathway-driven cancers (e.g., renal cell carcinoma, neuroendocrine tumours).

The strongest direct evidence is an ongoing Phase 2 trial combining everolimus with the CDK4/6 inhibitor ribociclib in advanced dedifferentiated liposarcoma and leiomyosarcoma, based on preclinical synergy between CDK4 and mTOR inhibition. However, this trial is single-arm, still active (not yet reporting final efficacy), and evaluates a combination rather than everolimus monotherapy — so the mechanistic rationale is more mature than the direct clinical evidence at this time.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Two-arm study of ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B); evaluates anti-tumour activity of the doublet in patients with ≥1 prior systemic therapy; estimated completion 2025-12, no final results reported yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial report | Clinical Cancer Research | Reports on the SAR-096 trial: ribociclib (CDK4/6 inhibitor) + everolimus (mTOR inhibitor) shows synergistic growth inhibition in preclinical tumour models, rationale for the combination in DDL/LMS. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Review of CDK inhibitor (palbociclib) combination therapies identified via patient-derived orthotopic xenograft (PDOX) sarcoma models. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/preclinical | Tumour Biology | Demonstrates activation of the Akt-mTOR and MAPK pathways in dedifferentiated liposarcoma specimens, with in vitro antitumor effects of an mTOR inhibitor. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical (not everolimus-based) | Anticancer Research | Eribulin combined with mechanistically different anticancer agents in liposarcoma xenograft models; everolimus not the study drug. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclinical (not everolimus-based) | Oncogene | XPO1 inhibitor selinexor disrupts transcriptional regulatory circuitry in dedifferentiated liposarcoma; everolimus not the study drug. |

---

## Saudi Arabia Market Information

Everolimus is currently **not marketed** in Saudi Arabia per this evidence pack (0 authorizations on file), so no product/dosage-form table is available.

---

## Cytotoxicity

Everolimus is an antineoplastic agent (oncology indications include renal cell carcinoma and neuroendocrine tumours), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps in this evidence pack — TFDA/local package insert retrieval is listed as a **Blocking** gap, DG001.)

---

## Other Candidate Indications (Portfolio Overview)

This evidence pack scored 10 candidate indications for everolimus. Liposarcoma ranks #1 by TxGNN score, but **unclassified renal cell carcinoma (#9)** has the most mature clinical evidence — two independent, completed, head-to-head Phase 2 RCTs (ESPN, ASPEN) directly testing everolimus — and is the only candidate reaching decision stage S3 / "Proceed with Guardrails."

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Liposarcoma | 99.88% | L2 | S2 | Research Question |
| 2 | Ovarian myxoid liposarcoma | 99.84% | L5 | S0 | Hold |
| 3 | Dermatofibrosarcoma protuberans | 99.82% | L5 | S0 | Hold |
| 4 | Parameningeal embryonal rhabdomyosarcoma | 99.77% | L3 | S1 | Research Question |
| 5 | Botryoid-type embryonal rhabdomyosarcoma (vagina) | 99.76% | L3 | S1 | Research Question |
| 6 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.75% | L3 | S1 | Research Question |
| 7 | Rhabdomyosarcoma (disease) | 99.74% | L2 | S2 | Research Question |
| 8 | Prostate embryonal rhabdomyosarcoma | 99.74% | L3 | S1 | Research Question |
| **9** | **Unclassified renal cell carcinoma** | **99.72%** | **L2** | **S3** | **Proceed with Guardrails** |
| 10 | RCC with Xp11.2 translocation/TFE3 fusion | 99.72% | L4 | S1 | Research Question |

For unclassified RCC, mTOR pathway activation underlies non-clear-cell RCC (especially papillary subtype) tumour biology. ESPN and ASPEN (both Phase 2 RCTs, everolimus vs. sunitinib) generally favoured sunitinib on PFS, so everolimus is best positioned as a guardrailed option for specific pathological subtypes or poor-risk patients rather than a first-line recommendation.

---

## Conclusion and Next Steps

**Decision: Research Question (Liposarcoma) / Proceed with Guardrails (Unclassified RCC — recommended parallel track)**

**Rationale:**
For the top TxGNN-ranked indication, liposarcoma, the mechanistic rationale (Akt-mTOR pathway activation) is sound but direct clinical evidence is limited to one ongoing, single-arm combination trial with no reported results — insufficient to move beyond a research question at this time. Within the same evidence pack, unclassified renal cell carcinoma has a substantially stronger base (two completed Phase 2 RCTs testing everolimus directly) and already warrants guardrailed consideration.

**To proceed, the following is needed:**
- TFDA/local package insert data (Blocking gap — required before any S1 safety assessment)
- Confirmed mechanism of action detail from DrugBank (High-severity gap)
- Final results of NCT03114527 (est. completion 2025-12) before advancing the liposarcoma indication
- If pursuing unclassified RCC: subtype/risk-stratification criteria to define the "guardrails" for use, given sunitinib's generally favourable head-to-head PFS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

