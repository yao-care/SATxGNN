---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Cancer Chemotherapy to Liver Sarcoma

> **Note on indication selection**: This Evidence Pack evaluated 10 TxGNN-predicted indications for fluorouracil (mostly rhabdomyosarcoma subtypes and sickle-cell/haemoglobinopathy syndromes). Nine of the ten reached only decision-stage S0 ("Hold") with **zero** supporting clinical trials or literature — the model itself flags several as likely embedding noise. **Liver Sarcoma** (rank 7) is the only candidate reaching decision-stage S1, with the highest evidence tier (L3) in the batch, so it is used as the headline candidate below rather than the raw rank-1 prediction.

## One-Sentence Summary

Fluorouracil (5-FU) is a long-established fluoropyrimidine antimetabolite chemotherapy agent; this Evidence Pack does not contain its Saudi Arabia-approved indication text (drug is currently unmarketed there). The TxGNN model predicts possible activity in **Liver Sarcoma**, supported by **6 clinical trials** (only indirectly relevant — none is a dedicated liver-sarcoma trial) and **20 publications**, mostly preclinical sarcoma models and small human case series/cohorts.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Saudi Arabia licences exist for fluorouracil in this pack (drug is not marketed locally) |
| Predicted New Indication | Liver Sarcoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this candidate is not available in the Evidence Pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, fluorouracil is a fluoropyrimidine antimetabolite that is converted intracellularly to active metabolites which inhibit thymidylate synthase, blocking DNA synthesis in rapidly dividing cells — a mechanism not specific to any one tissue of origin.

This broad-spectrum cytotoxic mechanism is the rationale offered in the Evidence Pack for extending 5-FU from its established solid-tumour chemotherapy role into liver sarcoma: both are proliferative malignancies theoretically sensitive to antimetabolite therapy. However, the supporting evidence is indirect — it consists mainly of murine sarcoma-180/RIF-1 tumour models and small human cohorts/case reports of primary or undifferentiated liver sarcoma treated with multi-agent chemotherapy (not 5-FU monotherapy trials for this specific tumour type). No trial in the pack was designed specifically to test fluorouracil in liver sarcoma.

## Clinical Trial Evidence

None of the 6 retrieved trials directly targets fluorouracil in liver sarcoma; all are graded B/C relevance (colorectal cancer or general solid-tumour trials that happen to include a 5-FU-containing regimen).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03914170](https://clinicaltrials.gov/study/NCT03914170) | N/A | Completed | 70 | Retrospective study of FOLFIRINOX (incl. 5-FU) + cetuximab in RAS wild-type metastatic colorectal cancer; relevance grade B — drug matches but indication is CRC, not liver sarcoma |
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | Phase 4 | Recruiting | 40 | Atezolizumab + bevacizumab with Y-90 radioembolization for hepatocellular carcinoma bridging/downstaging to transplant; does not use 5-FU, general HCC not sarcoma (grade C) |
| [NCT01374425](https://clinicaltrials.gov/study/NCT01374425) | Phase 2 | Completed | 376 | MAVERICC: bevacizumab + mFOLFOX6 vs. FOLFIRI with biomarker stratification in previously untreated metastatic CRC (grade C) |
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | Completed | 553 | Cetuximab + FOLFOX-4 vs. FOLFOX-4 alone in first-line metastatic CRC, RAS wild-type Chinese subjects (grade C) |
| [NCT05919264](https://clinicaltrials.gov/study/NCT05919264) | Phase 1/2 | Recruiting | 595 | FOG-001 safety/efficacy in advanced/metastatic solid tumours; no 5-FU, no sarcoma specificity (grade C) |
| [NCT04999761](https://clinicaltrials.gov/study/NCT04999761) | Phase 1 | Recruiting | 917 | AB122 platform study of tolerability/safety across advanced solid tumour cohorts; no 5-FU, no sarcoma specificity (grade C) |

## Literature Evidence

20 publications were retrieved; the 10 most directly relevant to fluorouracil and (liver) sarcoma are listed below. None is an RCT — evidence consists of human cohort/case-report series and preclinical animal models.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29346784](https://pubmed.ncbi.nlm.nih.gov/29346784/) | 2019 | Cohort | Digestive Surgery | Surgical treatment and chemotherapy experience in adult primary liver sarcoma at a single China hospital, evaluating diagnosis and prognosis |
| [3603715](https://pubmed.ncbi.nlm.nih.gov/3603715/) | 1987 | Retrospective cohort | Tumori | Italian multicentre retrospective study of undifferentiated (embryonal) sarcoma of the liver in 8 children |
| [11294295](https://pubmed.ncbi.nlm.nih.gov/11294295/) | 2001 | Case Report | J Hepatobiliary Pancreat Surg | Two paediatric cases of ruptured undifferentiated liver sarcoma treated with cisplatin/adriamycin/cyclophosphamide (not 5-FU) |
| [9051138](https://pubmed.ncbi.nlm.nih.gov/9051138/) | 1997 | Preclinical | Gan to Kagaku Ryoho | Spontaneous liver metastasis model of retroperitoneal sarcoma (LMFS) in BALB/c mice, evaluating antitumor effects of HCFU (a 5-FU derivative) |
| [10584572](https://pubmed.ncbi.nlm.nih.gov/10584572/) | 1999 | Preclinical | Gan to Kagaku Ryoho | HCFU (5-FU derivative) combined with angiogenesis inhibitor TNP-470 against liver metastasis in a retroperitoneal sarcoma mouse model |
| [52569](https://pubmed.ncbi.nlm.nih.gov/52569/) | 1975 | Preclinical | Gan | Effects of several antitumor agents, including 5-fluorouracil, on sarcoma-180 cells transplanted to liver, kidney, and lung in mice |
| [37112602](https://pubmed.ncbi.nlm.nih.gov/37112602/) | 2023 | Preclinical | Toxics | Combined chamomile flower extract and 5-FU chemotherapy tested in a Sarcoma 180 in vivo mouse model |
| [1997177](https://pubmed.ncbi.nlm.nih.gov/1997177/) | 1991 | Preclinical | Cancer Research | 19F-MRS study of 5-FU metabolism in murine RIF-1 (fibrosarcoma) tumors and liver |
| [1406088](https://pubmed.ncbi.nlm.nih.gov/1406088/) | 1992 | Preclinical | Magn Reson Imaging | Thymidine-modulated 5-FU metabolism in liver and RIF-1 fibrosarcoma tumors, studied by 19F-MRS |
| [3630210](https://pubmed.ncbi.nlm.nih.gov/3630210/) | 1987 | Preclinical | Xenobiotica | Metabolism of a 5-FU prodrug (PH-FU) in rat liver and enzyme induction by phenobarbital |

## Saudi Arabia Market Information

Fluorouracil is currently **not marketed** in Saudi Arabia — the Evidence Pack contains zero authorization records (`total_licenses: 0`, `licenses: []`). No product/dosage-form/indication information is available to tabulate.

## Cytotoxicity

Fluorouracil is a fluoropyrimidine antimetabolite and is classified as antineoplastic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions apply per standard institutional protocol; no drug-specific detail available in this pack |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack — a Blocking-severity data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication in this pack directly tests fluorouracil in liver sarcoma; supporting evidence is limited to preclinical sarcoma-180/fibrosarcoma models and small retrospective human cohorts/case reports using other chemotherapy regimens. Combined with a Blocking-severity gap in TFDA/SFDA safety labeling (DG001) and the drug not being marketed in Saudi Arabia, the evidence does not yet support progression past the research question stage.

**To proceed, the following is needed:**
- Saudi Arabia (SFDA) package insert / label data — warnings, contraindications, DDI (Blocking gap, DG001)
- DrugBank-sourced mechanism of action detail for fluorouracil (High-severity gap, DG002)
- A dedicated preclinical or early-phase study of fluorouracil specifically in liver sarcoma, rather than indirect CRC/HCC trials or generic sarcoma-180 models
- Re-evaluation of the 9 lower-tier predicted indications (all S0/Hold, L5) if future TxGNN model updates surface supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

