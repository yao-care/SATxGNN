---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Trastuzumab is a HER2-targeted humanized monoclonal antibody whose established use is in HER2-overexpressing breast cancer.
> The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
> with **36 clinical trials** and **20 publications** currently supporting this direction — though most of this evidence targets HER2-positive/PR-positive co-expressing tumors rather than PR status independent of HER2.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer *(established use, evident throughout the trial/literature base; Saudi Arabia-specific approved indication text is not available because the drug is not currently marketed there — data gap)* |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (e.g., DrugBank MOA text) is flagged as a data gap in this evidence pack. However, the underlying pharmacology is well established across the trial and literature evidence itself: trastuzumab is a humanized IgG1 monoclonal antibody directed against the extracellular domain of HER2/ERBB2. It blocks HER2-mediated proliferative signaling and mediates antibody-dependent cellular cytotoxicity (ADCC) against HER2-overexpressing tumor cells.

Progesterone-receptor status is not itself a drug target — PR positivity is a hormone-receptor biomarker that commonly co-occurs with HER2 overexpression in a recognized clinical subgroup ("triple-positive," ER+/PR+/HER2+ breast cancer). As the repurposing rationale for this candidate notes, this prediction largely represents an extension within trastuzumab's existing core indication space (HER2-positive disease) rather than a mechanistically novel repurposing signal: PR positivity is a frequently co-assessed biomarker used to guide combination with endocrine therapy (e.g., aromatase inhibitors, tamoxifen, fulvestrant) alongside anti-HER2 blockade, as seen in trials such as NEOADAPT (letrozole/AI + pertuzumab/trastuzumab) and the WSG-ADAPT/WSG-TP-II program.

Because efficacy depends on HER2 co-expression rather than PR status alone, the mechanistic plausibility is strong specifically for the ER/PR+, HER2+ subgroup, and weaker as a general claim about PR-positive breast cancer irrespective of HER2 status. This distinction should guide any downstream biomarker-stratified protocol design.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Equivalence study of trastuzumab + QL1209 (pertuzumab biosimilar) + docetaxel vs. trastuzumab + pertuzumab + docetaxel in HER2+/ER-PR-negative early/locally advanced breast cancer neoadjuvant treatment. |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole + trastuzumab in ErbB2-overexpressing, ER and/or PR-positive metastatic breast cancer — direct PR+ population. |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) (NEOADAPT) | Phase 2 | Unknown | 7 | Neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab without chemotherapy in HR+ (ER+/PR+), HER2+ localized breast cancer. |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | Neoadjuvant Herceptin + docetaxel ± pertuzumab; compared pathological complete response rates across 4 arms in HER2+ breast cancer. |
| [NCT05905939](https://clinicaltrials.gov/study/NCT05905939) | N/A (retrospective) | Completed | 774 | Real-world multicenter retrospective study of treatment patterns and outcomes in Russian HER2-positive metastatic breast cancer patients on anti-HER2 therapy. |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3436 | Landmark adjuvant trial: AC followed by weekly paclitaxel with or without trastuzumab in HER2-overexpressing node-positive/high-risk node-negative breast cancer. |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy with or without trastuzumab in node-positive/high-risk node-negative HER2-low invasive breast cancer. |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy plus lapatinib vs. trastuzumab as first-line therapy for HER2-positive metastatic breast cancer. |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | Recruiting | 1100 | Double-blind, placebo-controlled study of short-duration preoperative trastuzumab in HER2-positive operable breast cancer. |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) (IMpassion050) | Phase 3 | Completed | 454 | Atezolizumab vs. placebo combined with neoadjuvant dose-dense AC → paclitaxel + trastuzumab + pertuzumab in early HER2-positive breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5-yr follow-up) | Lancet Oncology | NeoSphere trial: 5-year PFS, DFS, and safety of neoadjuvant pertuzumab + trastuzumab + docetaxel vs. trastuzumab + docetaxel in HER2+ breast cancer. |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT (Phase 2) | Lancet Oncology | monarcHER trial: abemaciclib + trastuzumab ± fulvestrant vs. standard chemotherapy + trastuzumab in HR+/HER2+ advanced breast cancer. |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT (Phase 3) | Lancet Oncology | ExteNET trial: neratinib after trastuzumab-based adjuvant therapy reduces recurrence in HER2+ early breast cancer. |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis (EBCTCG) | Lancet | Overview of randomized trials assessing chemotherapy/hormonal therapy effects on 15-year recurrence and survival in early breast cancer. |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT (Phase 2) | JAMA Oncology | WSG-TP-II trial: endocrine therapy + trastuzumab + pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer. |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Annals of Oncology | WSG-ADAPT HER2+/HR- trial: efficacy/safety of 12-week neoadjuvant trastuzumab + pertuzumab ± paclitaxel de-escalation. |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Translational/Cohort | Theranostics | Multi-omics landscape and trastuzumab responsiveness of ER+/PR+/HER2+ ("triple-positive") breast cancer across 5 cohorts. |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast (Edinburgh) | Clinical implications of intrinsic molecular subtypes (Luminal A/B, HER2-enriched, Basal-like) relevant to biomarker-guided treatment. |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective cohort | BMC Cancer | Single-center retrospective study of trastuzumab + fulvestrant in HR+/HER2+ advanced breast cancer. |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | Journal of Clinical Oncology | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer. |

---

## Saudi Arabia Market Information

Trastuzumab currently has **0 registered authorizations** and is marked as **Not Marketed** in Saudi Arabia in this evidence pack, so no product/authorization table is available.

---

## Cytotoxicity

Trastuzumab is an antineoplastic agent (HER2-targeted monoclonal antibody used across breast cancer indications throughout this evidence pack), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 humanized monoclonal antibody, not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Low as monotherapy; when combined with a chemotherapy backbone (e.g., docetaxel, paclitaxel), myelosuppression risk follows the chemotherapy partner rather than trastuzumab itself |
| Emetogenicity Classification | Low as monotherapy; combination-regimen emetogenicity is driven by the co-administered chemotherapy agent |
| Monitoring Items | Baseline and periodic LVEF/cardiac function (cardiotoxicity is a recognized class effect, reflected in cardiac-safety trials in this evidence base), infusion-related reaction monitoring, CBC and organ function if combined with chemotherapy |
| Handling Protection | Standard biologic/monoclonal antibody handling precautions and infusion monitoring; does not require conventional cytotoxic (DNA-damaging) drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The PR-positive breast cancer prediction is supported by L1-level evidence (36 trials, 20 publications), including multiple completed Phase 3 trastuzumab-based trials, but almost all of this evidence targets the HER2-positive/PR-positive co-expressing subgroup rather than PR status independent of HER2 — this distinction should be reflected in any protocol eligibility criteria. Other TxGNN-predicted indications for trastuzumab in this candidate set (ranks 5–10: e.g., malignant granular cell skin tumor, ectomesenchymoma, HHV-8-related tumor) have no supporting trials or literature (L5) and are correctly scored "Hold."

**To proceed, the following is needed:**
- Official TFDA/regulatory package insert warnings, contraindications, and drug-drug interaction data (currently flagged as Blocking data gaps)
- Confirmed drug mechanism-of-action documentation from DrugBank or equivalent source
- Saudi Arabia market authorization status confirmation, since the drug is currently listed as not marketed
- Biomarker-stratified analysis confirming whether efficacy signal depends on HER2 co-positivity rather than PR status alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

