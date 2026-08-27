---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 633
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Trastuzumab emtansine (T-DM1, marketed as Kadcyla) is an antibody-drug conjugate already established for HER2-positive breast cancer.
> The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
> with **4 clinical trials** and **15 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (per Kadcyla® post-marketing use referenced in the evidence base; Saudi Arabia license text not available — see Market Information below) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not returned for this drug (flagged as a High-severity data gap in the evidence pack). However, the evidence base itself documents the mechanism: trastuzumab emtansine is an antibody-drug conjugate (ADC) in which trastuzumab, an anti-HER2 monoclonal antibody, is linked via a non-cleavable linker to DM1, a maytansinoid microtubule inhibitor. The antibody component binds HER2-overexpressing tumor cells, is internalized, and releases the cytotoxic DM1 payload intracellularly — meaning the drug's activity is fundamentally HER2-dependent, not PR-dependent.

PR status is a co-existing biomarker in breast cancer, not a drug target. PR-positive disease frequently overlaps with HER2-positive disease (HR+/HER2+ subtype), so the "new" indication predicted here is best understood as a HER2-positive subgroup defined additionally by PR positivity, rather than a mechanistically novel target population. This is consistent with literature in the evidence pack (e.g., PMID 33726508, "Current trends in the treatment of HR+/HER2+ breast cancer") that explicitly discusses T-DM1 use in this overlapping population.

Because efficacy depends on HER2 expression rather than PR status, the prediction is mechanistically plausible wherever HER2 positivity co-occurs with PR positivity, but PR status alone does not independently support activity. For context, the same evidence pack shows a related indication — PR-**negative** breast cancer — with stronger evidence (L1, multiple completed Phase 2/3 studies including a Kadcyla post-marketing surveillance study), which is the more established HER2+/HR− population for T-DM1. This reinforces that the PR+ prediction rides on the underlying HER2+ mechanism rather than a new biological rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (observational) | Completed | 1,151 | Retrospective multicenter study estimating prevalence and treatment patterns of HER2-low metastatic breast cancer via IHC rescoring in previously HER2-negative patients |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | De-escalation of adjuvant chemotherapy in HER2+/ER-negative, node-negative early breast cancer achieving pCR after neoadjuvant dual HER2 blockade |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | Atezolizumab vs. placebo added to neoadjuvant ddAC-paclitaxel + trastuzumab + pertuzumab in early HER2-positive breast cancer (IMpassion050); T-DM1 arm not confirmed from available summary |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Preoperative T-DM1 + pertuzumab in early-stage HER2-positive breast cancer, examining impact of HER2 heterogeneity on treatment response |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline | J Clin Oncol | ASCO clinical practice guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline | Eur J Cancer | EGTM biomarker guidelines: mandates HER2 testing for all anti-HER2 therapies including T-DM1, alongside routine ER/PR testing |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review/Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Overview of targeted/cytotoxic breast cancer therapies, framed around HER2/HR/ER/PR status |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Review | J Clin Oncol | Earlier ASCO clinical practice guideline for systemic therapy in HER2-positive advanced breast cancer |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | Current treatment trends in HR+/HER2+ breast cancer, including T-DM1 and neratinib |
| [37445276](https://pubmed.ncbi.nlm.nih.gov/37445276/) | 2023 | Preclinical | J Clin Med | Aminosteroid RM-581 reduces proliferation across all breast cancer molecular subtypes (ER/PR/HER2-defined), alone and combined with standard treatments |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Report | Front Oncol | Pyrotinib plus metronomic vinorelbine in HER2-positive breast cancer with leptomeningeal disease |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Case Report | BMJ Case Rep | Receptor conversion (including PR status change) with vocal cord paralysis as presenting sign of metastatic breast cancer |
| [40642740](https://pubmed.ncbi.nlm.nih.gov/40642740/) | 2025 | Case Report | J Med Cases | Durable response with trastuzumab deruxtecan (related ADC) in HER2-mutant triple-negative breast cancer |

---

## Saudi Arabia Market Information

No licenses are currently on record — `taiwan_regulatory.licenses` is empty and `total_licenses` is 0. Trastuzumab emtansine is not currently marketed in Saudi Arabia per the available regulatory data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC) with a conventional cytotoxic payload — anti-HER2 antibody (trastuzumab) conjugated via a non-cleavable linker to the maytansinoid microtubule inhibitor DM1 |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions (as a cytotoxic-payload ADC, hazardous-drug handling precautions are generally applicable) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — TFDA/SFDA package insert warnings and contraindications must be obtained before any S1 safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is sound but not novel — PR positivity is a co-existing biomarker in a population where T-DM1's HER2-dependent activity is already established, and evidence quality (L2) is moderate rather than definitive for this specific PR+ framing. Critically, a **Blocking**-severity data gap on TFDA/SFDA warnings and contraindications means this candidate cannot yet clear a safety pre-assessment, regardless of the efficacy rationale.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — Blocking gap, required before any safety evaluation
- Documented mechanism of action from DrugBank — High-severity gap, needed to formally substantiate the mechanistic rationale
- Saudi Arabia licensing/market entry status confirmation, since the drug is currently not marketed
- Confirmation of T-DM1 as the actual study intervention in NCT03726879 (title was truncated in source data)
- PR-status-stratified outcome data from trials such as NCT01745965 (rank 3 evidence set) to directly test PR-dependence of response, rather than relying on HER2+/PR+ overlap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

