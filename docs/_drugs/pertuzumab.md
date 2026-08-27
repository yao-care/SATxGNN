---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

> Pertuzumab is a HER2-targeted humanized monoclonal antibody, originally developed and approved elsewhere for HER2-positive breast cancer in combination with trastuzumab and chemotherapy; it is not currently marketed in Saudi Arabia.
> The TxGNN model predicts it may be effective for **normal breast-like subtype of breast carcinoma**,
> with **6 clinical trials** currently identified and **no dedicated literature** supporting this specific direction.
> Evidence quality is limited because none of the trials specifically enroll or stratify by this molecular subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (combination therapy with trastuzumab ± chemotherapy) — established elsewhere; not currently licensed in Saudi Arabia |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not available for this record. Based on established pharmacological knowledge (referenced within the evidence pack's own rationale fields, not the database MOA field), pertuzumab is a humanized monoclonal antibody that binds domain II of the HER2 (ERBB2) extracellular region, blocking HER2–HER3 heterodimerization and downstream PI3K/AKT and MAPK signaling. Its established efficacy in HER2-positive breast cancer is well proven when combined with trastuzumab and taxane chemotherapy.

"Normal-like" is one of the PAM50 intrinsic molecular subtypes of breast cancer. In the literature, it is frequently regarded as a technical artifact reflecting contamination by adjacent normal breast tissue rather than a distinct biological entity, and tumors classified this way typically show low HER2 expression. This weakens the mechanistic rationale: pertuzumab's activity depends on HER2 overexpression, which is not a defining feature of the normal-like subtype.

Consistent with this, the six clinical trials associated with this prediction are general HER2-positive neoadjuvant breast cancer studies — none specifically stratify or enrich for the normal-like subtype. This suggests a population-mismatch risk: the prediction may be capturing pertuzumab's broad association with "breast cancer" trials generally, rather than a genuine mechanistic link to this specific subtype. Confirming whether a clinically meaningful HER2-overexpressing sub-population exists within normal-like tumors is a prerequisite before this can be meaningfully advanced.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | Precision neoadjuvant therapy platform study across operable breast cancer subtypes to verify novel targeted drugs; population is broad, not normal-like-specific |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Nigerian cohort evaluating optimal neoadjuvant-to-adjuvant anti-HER2 therapy by HER2 status; regional, small sample |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as preoperative therapy for inflammatory breast cancer |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine combined with neoadjuvant chemotherapy and HER2-targeted antibody therapy; mixed immunotherapy/HER2-targeted mechanism |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Neoadjuvant therapy guided by in-vitro patient-derived tumor-like cell cluster drug screening in HER2-positive early breast cancer |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | ARIADNE trial: trastuzumab deruxtecan vs. standard preoperative treatment with biology-driven treatment selection in non-metastatic HER2-positive breast cancer |

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Pertuzumab currently holds no marketing authorization in Saudi Arabia (0 licenses on record; market status: Not Marketed). No product-level licensing details are available for this jurisdiction.

## Cytotoxicity

Pertuzumab is classified as an antineoplastic agent (HER2-targeted monoclonal antibody used in breast cancer treatment).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody; non-cytotoxic mechanism) |
| Myelosuppression Risk | Low — monoclonal antibodies are not directly myelosuppressive; hematologic risk in practice is largely driven by concurrent cytotoxic partners (e.g., docetaxel/paclitaxel) in combination regimens |
| Emetogenicity Classification | Low (minimal intrinsic emetogenic potential for the antibody component) |
| Monitoring Items | Cardiac function/LVEF (particularly when combined with trastuzumab), infusion-related reactions, CBC and organ function when combined with cytotoxic chemotherapy partners |
| Handling Protection | Standard biologics/monoclonal antibody handling; cytotoxic drug handling protocols apply to combination chemotherapy agents, not to pertuzumab itself |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (normal breast-like subtype) lacks a solid mechanistic foundation — this subtype is not consistently associated with HER2 overexpression, and none of the identified trials specifically target or stratify by it. Combined with the absence of any supporting literature, the evidence base is too weak and too indirect to proceed, even with guardrails.

**To proceed, the following is needed:**
- Confirmation of HER2-overexpression prevalence within the normal-like breast cancer subtype (biomarker/epidemiological data)
- TFDA/SFDA package insert data for warnings and contraindications (currently a Blocking data gap — DG001 — required before any S1 safety screening)
- Verified DrugBank mechanism-of-action data (currently a High-severity data gap — DG002)
- Consideration of the progesterone-receptor positive/negative breast cancer predictions (ranks 2–3 in this evidence pack), which show materially stronger evidence (L1, multiple completed Phase 3 RCTs) and may represent more actionable near-term repurposing candidates than this rank-1 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

