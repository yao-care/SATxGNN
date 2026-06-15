---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
---

# Anastrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Anastrozole: From HR+ Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation non-steroidal aromatase inhibitor, internationally established as the standard adjuvant endocrine therapy for postmenopausal women with hormone receptor-positive (HR+) breast cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **0 registered clinical trials** and **20 publications** currently in the evidence pack — including multiple landmark Phase 3 RCTs.
**Important context:** this prediction aligns with anastrozole's already-established primary indication rather than representing a novel repurposing opportunity; the high TxGNN score (99.68%) reflects validation of existing knowledge graph evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+ breast cancer in postmenopausal women (internationally established; no Saudi Arabia authorization on file) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed (0 authorizations on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Anastrozole competitively inhibits CYP19A1 (aromatase), the enzyme responsible for converting androgens to estrogens in peripheral tissues. In postmenopausal women, peripheral aromatization is virtually the sole source of circulating estrogens. By suppressing plasma estradiol by over 99%, anastrozole directly eliminates the principal mitogenic driver in hormone receptor-positive breast tumors. The mechanism is highly target-selective, with no direct cytotoxic activity.

The clinical link between anastrozole and female breast carcinoma is among the most robustly validated in oncology. The ATAC trial (Phase 3 RCT, n = 9,366, median follow-up 68 months) established that five years of adjuvant anastrozole significantly prolonged disease-free survival compared to tamoxifen in postmenopausal women with localized HR+ breast cancer. The IBIS-II program subsequently extended the application to chemoprevention in high-risk postmenopausal women, demonstrating sustained breast cancer incidence reduction well beyond the active treatment period. These findings form the basis of global guideline endorsement by ESMO, ASCO, and NCCN.

Because female breast carcinoma is anastrozole's primary approved indication in most regulatory jurisdictions (FDA, EMA, Japan PMDA), this TxGNN prediction functions as a **knowledge-graph validation** rather than a novel repurposing signal. The more exploratory repurposing candidates for this drug appear at lower ranks in this evidence pack (neuroblastoma, retroperitoneal neoplasm, monocytic leukemia), which carry far weaker mechanistic rationale and lack supporting clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under the specific query parameters ("ANASTROZOLE" + "female breast carcinoma", queried 2026-04-20) were retrieved in this evidence pack. This is attributable to query-parameter specificity rather than a genuine absence of trials — anastrozole has an extensive Phase 2/3 registration history in breast cancer. A direct ClinicalTrials.gov search using broader terms (e.g., "anastrozole breast cancer") yields several hundred completed and ongoing studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT | Lancet | ATAC trial (n = 9,366): anastrozole significantly prolonged disease-free survival vs tamoxifen (575 vs 651 events, HR favoring anastrozole) after 5 years of adjuvant treatment in postmenopausal HR+ localized breast cancer |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | Phase 3 RCT (chemoprevention) | Lancet | IBIS-II long-term results: anastrozole significantly reduced incidence of both invasive breast cancer and DCIS vs placebo in high-risk postmenopausal women, with benefit persisting well beyond the 5-year treatment period |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | Phase 3 RCT | Lancet | IBIS-II DCIS (double-blind RCT): anastrozole superior to tamoxifen in preventing locoregional and contralateral breast cancer recurrence in postmenopausal women with locally excised HR+ DCIS |
| [9024711](https://pubmed.ncbi.nlm.nih.gov/9024711/) | 1997 | Phase 3 RCT | Cancer | Pivotal Phase III trial (n = 386): anastrozole 1 mg and 10 mg daily comparable to megestrol acetate in advanced breast carcinoma progressing after tamoxifen; established 1 mg as the clinical dose |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis | Oncotarget | Meta-analysis of RCTs comparing anastrozole vs tamoxifen: anastrozole shows superior disease-free survival and time to progression, with lower rates of endometrial cancer and thromboembolic events |
| [30499075](https://pubmed.ncbi.nlm.nih.gov/30499075/) | 2020 | Meta-analysis | Pathology Oncology Research | Meta-analysis (7 RCTs, DCIS + BCS + RT setting): tamoxifen reduces ipsilateral recurrence; 2 RCTs directly compare tamoxifen vs anastrozole in DCIS, informing endocrine therapy selection |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | GWAS / Phase 3 | JCI Insight | GWAS within MA.27 Phase III RCT (anastrozole vs exemestane, n = 4,465+): CSMD1 SNP associated with breast cancer-free interval; identifies additional non-aromatase mechanisms including fatty acid synthase regulation |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Review | Expert Opinion on Drug Safety | Comprehensive drug monograph: third-generation AI adjuvant RCTs consistently demonstrate greater efficacy vs tamoxifen; reviews tolerability, bone/lipid effects, and clinical positioning |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Systematic Review | Revista da Associacao Medica Brasileira | Systematic review of anastrozole in chemoprevention and treatment of hormone-sensitive breast cancer in postmenopausal women; summarizes pharmacodynamic and pharmacokinetic considerations including inter-individual variability |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Pharmacogenomics | Clinical Pharmacology and Therapeutics | SNP-treatment interaction analysis (n = 4,465): identified genetic variants differentially predicting efficacy of anastrozole versus exemestane in the adjuvant setting, supporting genotype-guided AI selection |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Hormonal/Endocrine (non-steroidal aromatase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low — anastrozole has no direct bone marrow suppressive mechanism; myelosuppression is not a recognized class effect |
| Emetogenicity Classification | Minimal — oral tablet formulation; clinical trials report nausea in fewer than 10% of patients, generally mild and self-limiting |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and annually; significant fracture and osteoporosis risk with long-term use), lipid profile, liver function (ALT/AST), musculoskeletal symptom assessment (arthralgia is a leading cause of treatment discontinuation) |
| Handling Protection | Standard pharmaceutical handling procedures; cytotoxic drug handling precautions are not required for this endocrine agent |

---

## Safety Considerations

Please refer to the package insert for safety information. (Formal key warnings, contraindications, and drug interaction data were not available in the current evidence pack.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for female breast carcinoma is supported by the highest possible evidence level (L1), with multiple landmark Phase 3 RCTs confirming anastrozole's efficacy and favorable tolerability in HR+ breast cancer. The primary barrier to clinical deployment in Saudi Arabia is the absence of local regulatory registration rather than any uncertainty about clinical benefit.

**To proceed, the following is needed:**

- **Regulatory pathway**: Obtain Saudi Arabia SFDA marketing authorization for anastrozole (originator Arimidex or approved generic); confirm current import and dispensing status
- **Safety documentation**: Retrieve full prescribing information (package insert) for formal safety review, particularly regarding contraindications in premenopausal women and patients with severe hepatic impairment
- **Baseline monitoring infrastructure**: Confirm availability of DEXA scanning for bone mineral density monitoring prior to initiating long-term therapy
- **Patient selection criteria**: Define eligibility (postmenopausal status, confirmed HR+/HER2− pathology by IHC, ECOG PS 0–2) and document local estrogen receptor testing capability
- **Drug interaction screening**: Conduct formal DDI review, particularly for co-administration with estrogen-containing products (direct antagonism) and CYP enzyme-inducing agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

