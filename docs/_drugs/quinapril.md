---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Quinapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril is an ACE inhibitor whose established pharmacological class use is blood pressure control; the TxGNN model's top prediction is **malignant hypertensive renal disease**, with a very high similarity score (99.86%) but **zero clinical trials and zero literature records** directly supporting this specific indication. Given the complete absence of drug-specific evidence and a known safety caveat for ACE inhibitors in renovascular pathology, the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded — Quinapril is not marketed in Saudi Arabia, so no approved indication text exists. Publicly known pharmacology confirms it is an ACE inhibitor used for hypertension (class-level, not indication-specific to this dataset). |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for quinapril is not available in the drug-level database record (MOA: Data Gap). Based on publicly known pharmacology, however, quinapril is confirmed to be an angiotensin-converting enzyme (ACE) inhibitor that lowers angiotensin II, a class-level antihypertensive mechanism shared across ACE inhibitors.

The predicted indication, malignant hypertensive renal disease, is a severe hypertensive emergency with secondary renal injury. In theory, blood-pressure control via ACE inhibition could plausibly slow progression of hypertensive nephropathy, which is the mechanistic basis TxGNN is likely drawing on.

However, this is a **class-level, indirect inference** rather than evidence specific to quinapril or this indication. Importantly, malignant renovascular hypertension frequently coexists with bilateral renal artery stenosis, a setting in which ACE inhibitors are well known to risk **precipitating acute renal failure** rather than protecting the kidney. This mechanistic link therefore carries a meaningful safety caveat that must be weighed against the theoretical benefit, and should not be read as a straightforward "supportive" mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Quinapril currently has no market authorization records in Saudi Arabia (market status: not marketed; total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (malignant hypertensive renal disease) has no supporting clinical trials or literature — evidence rests entirely on the TxGNN model score (Evidence Level L5, Decision Stage S0). Combined with a known ACE-inhibitor safety concern in renovascular hypertension pathology and the drug's non-marketed status in Saudi Arabia, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert data on warnings, contraindications, and drug interactions (currently a Blocking data gap)
- Confirmed mechanism of action record for quinapril (currently a High-severity data gap)
- Targeted literature or preclinical search specific to quinapril and malignant hypertensive renal disease/renovascular hypertension, including assessment of bilateral renal artery stenosis risk
- Evaluation of whether the four lower-ranked predictions (malignant renovascular hypertension, WHO Group 3/5 pulmonary hypertension, Braddock syndrome) merit further work — internal review already flags these as mechanistically weak or likely knowledge-graph noise, with the 20 pulmonary-hypertension literature hits assessed as unrelated hypoxia/oncology basic science rather than drug-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

