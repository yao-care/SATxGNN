---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Palliative Hormonal Therapy to Endometrial Carcinoma

## One-Sentence Summary

> Megestrol acetate is a synthetic progestin classically used as palliative hormonal therapy for advanced breast/endometrial cancer and for cancer-related cachexia/anorexia.
> The TxGNN model predicts it may be effective for **Uterine Corpus Endometrial Carcinoma** — specifically in early-stage and fertility-sparing settings —
> with **3 clinical trials** currently supporting this direction, though no dedicated literature has yet been indexed for this specific disease term.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no Saudi licenses on file); classically used as palliative progestin therapy for advanced breast/endometrial cancer and cancer-related cachexia/anorexia |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma (early-stage / fertility-sparing setting) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap). Based on known pharmacology, megestrol acetate is a synthetic progestin whose efficacy in advanced breast cancer and endometrial carcinoma as palliative hormonal therapy has long been established clinically.

Mechanistically, megestrol acetate directly activates the progesterone receptor (PR) on endometrial cells, suppressing estrogen-driven endometrial proliferation and promoting differentiation. This is the classic mechanism underlying progestin therapy for endometrial carcinoma, particularly in PR-positive, low-grade tumors and in patients desiring fertility preservation.

What makes this prediction notable is not that megestrol is mechanistically novel for endometrial cancer — it is already used off-label in this context — but that the supporting trials point to an emerging, narrower application: early-stage/fertility-sparing management (conservative treatment instead of hysterectomy) rather than the traditional advanced/palliative use. This represents a genuine shift in clinical positioning worth tracking as a distinct repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Randomized comparison of continuous vs. sequential progestin (megestrol) therapy for endometrial intraepithelial neoplasia/atypical hyperplasia in a fertility-preservation cohort; small sample and termination limit strength of evidence |
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial of temsirolimus alone vs. combined with megestrol acetate + tamoxifen in advanced, persistent, or recurrent endometrial carcinoma; megestrol used to block estrogen-driven tumor growth |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor combined with progesterone vs. progesterone alone for fertility-sparing treatment of early-stage endometrial cancer; exploratory, status unconfirmed |

---

## Literature Evidence

Currently no related literature available for this specific indication (uterine corpus endometrial carcinoma).

---

## Saudi Arabia Market Information

Megestrol acetate is not currently marketed in Saudi Arabia — no registered authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA package insert retrieval is flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale (PR agonism on estrogen-driven endometrial tissue) is well established, and one completed Phase 2 RCT (n=73) plus two smaller/early-phase supporting trials give this an L2 evidence level. However, formal safety labeling (TFDA package insert) is entirely missing — a blocking gap — and the drug is not currently marketed in Saudi Arabia, so guardrails are required before any clinical application in this new fertility-sparing context.

**To proceed, the following is needed:**
- TFDA package insert with warnings/contraindications (DG001, blocking — required before safety pre-assessment can proceed)
- Formal mechanism of action documentation from DrugBank or equivalent source (DG002)
- Confirmatory larger-scale trial data, since the most directly relevant RCT (NCT00503581) was terminated at n=9
- Saudi Arabia regulatory registration pathway assessment, given zero current authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

