---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class antimicrotubule agent originally approved for ovarian cancer and later extended globally to breast, lung, and other solid tumors — though the drug-level database record for this candidate has a data gap on original indication and MOA. TxGNN predicts continued/expanded effectiveness in **Female Breast Carcinoma**, a prediction already reinforced by **50+ clinical trials** and **20 publications**. Importantly, this is not a genuinely novel repurposing hypothesis: paclitaxel is already a globally approved standard-of-care chemotherapy for breast cancer, so this candidate should be read primarily as a confirmation of known efficacy against a backdrop of missing local (Saudi Arabia) regulatory data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in database (Data Gap); publicly known original approval was for ovarian cancer, later extended to breast cancer, NSCLC, and Kaposi's sarcoma |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa and original_indications are both flagged as Data Gaps). Based on publicly available clinical knowledge, paclitaxel is a taxane-class microtubule-stabilizing agent that binds β-tubulin, blocks microtubule depolymerization, and disrupts mitotic spindle function — arresting rapidly dividing cells (including breast cancer cells) at the G2/M phase and inducing apoptosis. This mechanism is not specific to any single tumor type, which is why taxanes are broadly active across ovarian, breast, lung, and other solid tumors.

Paclitaxel is already a globally approved, guideline-recommended chemotherapy for breast cancer across all major receptor subtypes (HER2-positive, ER-positive, and triple-negative), commonly used in both neoadjuvant/adjuvant and metastatic settings, often in combination with anthracyclines, platinum agents, or HER2-targeted therapies. Because of this, the TxGNN "prediction" for female breast carcinoma is best interpreted as validating an already-established clinical use rather than surfacing a genuinely new repurposing signal — the model's high confidence score is expected given the depth of existing evidence.

The genuine gap this candidate surfaces is not therapeutic plausibility but administrative: the underlying drug record lacks a documented original indication, MOA, and TFDA-equivalent safety labeling, and the local regulatory record shows the product as not marketed with zero authorizations in Saudi Arabia. Any "repurposing" action here is really a market-registration and safety-documentation exercise rather than an efficacy-validation exercise.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00016406](https://clinicaltrials.gov/study/NCT00016406) | Phase 3 | Completed | 399 | Doxorubicin/cyclophosphamide followed by weekly paclitaxel ± filgrastim for inflammatory/locally advanced breast cancer — direct adjuvant efficacy evidence |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Neoadjuvant carboplatin+docetaxel vs carboplatin+paclitaxel in Stage I–III triple-negative breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel + carboplatin + trastuzumab as first-line therapy in HER2-overexpressing metastatic breast cancer |
| [NCT00014222](https://clinicaltrials.gov/study/NCT00014222) | Phase 3 | Completed | 2,104 | Large adjuvant intergroup trial comparing sequenced EC+filgrastim+epoetin→paclitaxel vs AC→paclitaxel vs CEF in node-positive/high-risk breast cancer |
| [NCT00003877](https://clinicaltrials.gov/study/NCT00003877) | Phase 1/2 | Completed | 30 | Stromagen-supported stem cell transplantation after high-dose chemotherapy in metastatic breast cancer |
| [NCT01705691](https://clinicaltrials.gov/study/NCT01705691) | Phase 2 | Completed | 50 | Weekly paclitaxel or eribulin followed by AC as neoadjuvant therapy in HER2-negative locally advanced breast cancer |
| [NCT01307891](https://clinicaltrials.gov/study/NCT01307891) | Phase 2 | Completed | 64 | Abraxane ± tigatuzumab in metastatic triple-negative breast cancer |
| [NCT00044525](https://clinicaltrials.gov/study/NCT00044525) | Phase 2 | Completed | 82 | Efficacy/safety of IV BAY59-8862 in taxane-resistant metastatic breast cancer |
| [NCT00005649](https://clinicaltrials.gov/study/NCT00005649) | Phase 2 | Completed | N/A | Capecitabine + standard paclitaxel as first/second-line therapy in metastatic breast carcinoma |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Paclitaxel-trastuzumab adjuvant therapy for HER2-overexpressing Stage II/IIIA breast cancer |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects on breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review establishing paclitaxel's approved role in metastatic breast and ovarian cancer |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort | Cancer | Phase II trial of doxorubicin + paclitaxel in advanced breast carcinoma; importance of prior anthracycline exposure |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohort | BioMed Research International | Real-world efficacy of neoadjuvant EC + weekly paclitaxel-trastuzumab in HER2-positive breast carcinoma |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Pending | Chemical Biology & Drug Design | Therapeutic potential of paclitaxel combinations against breast carcinoma with in vivo biomarker identification |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Pending | J Immunother Cancer | Paclitaxel's effect on tumor-associated macrophages enhancing PD-1 blockade in TNBC |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Pending | Nature Communications | TEKT4 germline variants enriched in paclitaxel-resistant breast tumors |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Pending | Molecular Pharmacology | Reversal of stathmin-mediated resistance to paclitaxel in breast carcinoma cells |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Pending | Cancer | Paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | Pending | Cancer | GONO randomized trial: concomitant vs sequential epirubicin and paclitaxel as first-line therapy in metastatic breast carcinoma |

## Saudi Arabia Market Information

Paclitaxel is currently **not marketed** in Saudi Arabia per this dataset, with **0 registered authorizations** and no license records available. No marketing authorization table can be produced from the source data.

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia, including febrile neutropenia, is the characteristic dose-limiting toxicity of taxanes |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (neutrophil count), liver function, hypersensitivity reaction monitoring during infusion, peripheral neuropathy assessment |
| Handling Protection | Must follow institutional cytotoxic drug handling and administration protocols, including premedication for hypersensitivity reactions |

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack has no drug interaction data (query returned "not_found") and no key warnings or contraindications on file — this is flagged as a **Blocking** data gap (DG001) that prevents completion of the S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical trial/literature base for paclitaxel in breast carcinoma is extensive and well established (L1 evidence), but this reflects existing standard-of-care use rather than a novel repurposing signal. The binding constraint is not efficacy but missing local regulatory and safety documentation (Saudi Arabia: not marketed, 0 authorizations) and a Blocking-severity gap on TFDA-equivalent warnings/contraindications.

**To proceed, the following is needed:**
- TFDA (or Saudi SFDA) package insert with warnings/contraindications (DG001, Blocking — required before S1 safety pre-assessment can proceed)
- Confirmed drug-level MOA and original indication documentation (DG002)
- Local drug interaction (DDI) data, currently unqueried/not found
- Confirmation of Saudi Arabia market/registration pathway, given the current "not marketed / 0 licenses" status appears inconsistent with paclitaxel's global availability and warrants verification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

