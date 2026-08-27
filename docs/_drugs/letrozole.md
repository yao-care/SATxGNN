---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation nonsteroidal aromatase inhibitor globally established as a first-line endocrine therapy for hormone receptor-positive postmenopausal breast cancer. The TxGNN model's top prediction, **female breast carcinoma**, essentially confirms this already-established indication with a near-maximal score (99.98%), and the evidence base — **50 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications** — reflects mature, real-world validated use rather than a novel repurposing hypothesis. Nine additional predicted indications (ranks 2–10) explore adjacent or more speculative territory, ranging from guideline-supported extensions (e.g., ER-positive breast cancer, hormone-resistant breast carcinoma) to unsupported model artifacts (e.g., ER-negative breast cancer, fibrocystic disease).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer, hormone receptor-positive, postmenopausal (established global indication; not separately recorded in this dataset — Letrozole holds 0 marketing licenses in the Taiwan registry queried here) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> Note: This "predicted new indication" is, in substance, letrozole's well-known and globally guideline-endorsed use. Its presence at rank 1 with L1 evidence should be read as a **positive control confirming the model's calibration**, not as a genuine repurposing discovery. Ranks 4–8 (hormone-resistant, bilateral, gene-expression-defined, and ER-positive breast cancer variants) represent finer-grained extensions of the same core indication; ranks 3, 5, 9, and 10 are flagged in this dataset's own scoring as low-confidence or mechanistically inconsistent (see Data Gaps below for context).

---

## Why is This Prediction Reasonable?

The formal drug-level mechanism-of-action field for letrozole is marked as a data gap (DG002) in this dataset, and no Taiwan regulatory license text is available to source an "approved indication" description locally, since letrozole is not currently marketed in Taiwan (0 licenses on file). However, the per-indication analysis embedded in this evidence pack itself provides the relevant pharmacology: letrozole is a third-generation nonsteroidal aromatase inhibitor that blocks the conversion of androgens to estrogens, thereby depriving estrogen-receptor-positive (ER+) tumor cells of their growth signal. This is the drug's core, well-characterized mechanism — not an indirect inference.

Breast cancer, particularly the ER+/HER2- subtype in postmenopausal women, is the population in which this mechanism has the most direct pharmacological applicability. The evidence pack's own rationale for rank 1 states this plainly: aromatase inhibition is mechanistically matched to ER+ tumor biology, and letrozole is already a global standard-of-care agent in this setting (reflected in landmark trials such as BIG 1-98, PALOMA-2, and MONALEESA-2 appearing throughout the evidence tables).

By contrast, several lower-ranked predictions in this pack are mechanistically incoherent — most notably rank 3 (ER-negative breast cancer), where the evidence pack's own analyst explicitly flags a likely TxGNN entity/embedding confusion, since aromatase inhibitors are pharmacologically dependent on ER expression and are not expected to work in ER-negative disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00369850](https://clinicaltrials.gov/study/NCT00369850) | Phase 3 | Completed | 458 | Bone density/loss monitoring in postmenopausal breast cancer patients on long-term letrozole (IBCSG-1-98); establishes large-scale, long-term safety/use data. |
| [NCT03811509](https://clinicaltrials.gov/study/NCT03811509) | Phase 4 | Unknown | 1000 | Real-world cohort (B-ABLE) evaluating musculoskeletal effects and quality of life in breast cancer patients on aromatase inhibitors including letrozole. |
| [NCT05969184](https://clinicaltrials.gov/study/NCT05969184) | Phase 2 | Unknown | 94 | Palbociclib + endocrine therapy + anti-HER2 therapy in HR+/HER2+ advanced breast cancer. |
| [NCT00949598](https://clinicaltrials.gov/study/NCT00949598) | Phase 3 | Completed | 177 | Randomized double-blind neoadjuvant comparison of aromatase inhibitor vs. SERM (tamoxifen) in ER+ breast adenocarcinoma. |
| [NCT00673335](https://clinicaltrials.gov/study/NCT00673335) | Phase 3 | Completed | 170 | Letrozole vs. placebo for breast cancer prevention in postmenopausal BRCA1/BRCA2 mutation carriers. |
| [NCT07085767](https://clinicaltrials.gov/study/NCT07085767) | Phase 3 | Recruiting | 1000 | Palazestrant + ribociclib vs. letrozole + ribociclib, first-line ER+/HER2- advanced breast cancer (OPERA-02); letrozole as active comparator standard-of-care. |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Effects of letrozole vs. tamoxifen on bone and lipid metabolism in postmenopausal early breast cancer. |
| [NCT00893061](https://clinicaltrials.gov/study/NCT00893061) | Phase 3 | Completed | 44 | Cognitive function effects of adjuvant aromatase inhibitor vs. tamoxifen therapy. |
| [NCT02679755](https://clinicaltrials.gov/study/NCT02679755) | Phase 4 | Completed | 252 | Palbociclib + letrozole in postmenopausal HR+/HER2- advanced breast cancer where letrozole therapy is deemed appropriate. |
| [NCT04134598](https://clinicaltrials.gov/study/NCT04134598) | Phase 3 | Active, not recruiting | 926 | Radiation therapy vs. exclusive endocrine therapy (letrozole/AI) in low-risk elderly (≥70) early breast cancer (EUROPA). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | The New England Journal of Medicine | BIG 1-98: letrozole vs. tamoxifen as adjuvant treatment for steroid-hormone-receptor-positive breast cancer in postmenopausal women. |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT/Cohort | Computational and Mathematical Methods in Medicine | Efficacy, safety, and prognosis of sequential tamoxifen–letrozole therapy vs. letrozole monotherapy. |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | RCT | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial. |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Comprehensive review of letrozole pharmacology, toxicity, and therapeutic effects in HR+ breast cancer. |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Review | Breast Cancer Research and Treatment | The discovery and mechanism of action of letrozole as an aromatase inhibitor. |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacodynamics, pharmacokinetics, clinical efficacy and safety review of letrozole. |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh) | Development of letrozole and its use in advanced and neoadjuvant breast cancer settings. |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Comparative review of anastrozole, letrozole, and exemestane in early breast cancer management. |
| [22738819](https://pubmed.ncbi.nlm.nih.gov/22738819/) | 2012 | Systematic Review | Current Medical Research and Opinion | Lapatinib + letrozole vs. other first-line treatments in HR+/HER2+ metastatic breast cancer. |
| [41519129](https://pubmed.ncbi.nlm.nih.gov/41519129/) | 2026 | Trial report | Cell Reports Medicine | NeoPAL trial: molecular/cellular composition changes after neoadjuvant letrozole + palbociclib vs. chemotherapy in early luminal breast cancer. |

---

## Taiwan Market Information

Letrozole currently has **no marketing authorizations on file** in this dataset (market status: 未上市 / Not Marketed; total licenses: 0). No product-level licensing table can be generated from `taiwan_regulatory.licenses`. Confirming current registration status directly with TFDA is recommended before any Taiwan-market repurposing action is pursued.

---

## Cytotoxicity

Letrozole's original indication (breast cancer) and its established antineoplastic/endocrine-therapy classification meet the criteria for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/endocrine therapy — aromatase inhibitor (non-cytotoxic; mechanism-targeted rather than conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps or not found in this evidence pack — DG001 flags the TFDA package insert/warnings as a **blocking** gap for safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (female breast carcinoma) is supported by L1-level evidence — multiple completed Phase 3 RCTs and a mature literature base — but represents confirmation of letrozole's already-established global indication rather than a novel repurposing opportunity. Guardrails are warranted primarily because Taiwan-specific regulatory and safety documentation (package insert, contraindications, DDI) remain unfilled, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, blocking — required before any S1 safety pre-assessment)
- Formal mechanism-of-action record from DrugBank at the drug level (DG002, high priority)
- Confirmation of current Taiwan marketing/registration status, given 0 licenses on file
- Clarification of scope: since rank-1 "female breast carcinoma" is not a genuine new indication, consider whether this evaluation should instead prioritize a lower-ranked, evidence-supported extension (e.g., rank 4, hormone-resistant breast carcinoma, L2/Proceed with Guardrails) as the operative repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

