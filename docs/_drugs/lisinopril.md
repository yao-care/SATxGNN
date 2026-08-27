---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From ACE Inhibitor Therapy to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor (ACEi); no local (Saudi Arabia) registration data or original indication text is available in this evidence pack, but ACEi is globally established for hypertension, heart failure, and post-MI cardioprotection. The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but currently **no clinical trials** and **no literature** directly support this specific anatomical MI subtype — the prediction rests entirely on class-level mechanistic reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local registry data (drug not marketed in Saudi Arabia); known globally as an ACE inhibitor for hypertension/heart failure |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lisinopril in this evidence pack. Based on known information, lisinopril is part of the ACE inhibitor (ACEi) class, which suppresses the renin-angiotensin-aldosterone system (RAAS) to reduce cardiac afterload and limit ventricular remodeling.

ACEi is an established standard-of-care drug class after myocardial infarction, with the class effect confirmed by landmark Phase 3 trials (e.g., GISSI-3, ISIS-4, SAVE) referenced in the model's rationale. However, "posterolateral myocardial infarction" is an anatomical/ECG-localization subtype of MI rather than a distinct disease entity, and this evidence pack contains **zero trials and zero publications** specific to this subtype.

The prediction is therefore best understood as an extrapolation of ACEi's well-known post-MI class effect to a fine-grained anatomical label, rather than evidence of a distinct, independently validated indication. The same pattern repeats for the closely related predictions "posteroinferior myocardial infarction" (rank 2) and "septal myocardial infarction" (rank 7), all scored nearly identically and all lacking subtype-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Lisinopril currently has no marketing authorization on file in Saudi Arabia (0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (posterolateral myocardial infarction) has no direct clinical trial or literature support — it relies solely on generic ACEi post-MI class-effect reasoning applied to a specific anatomical subtype, which is insufficient to justify moving past the research-question stage.

**To proceed, the following is needed:**
- SFDA package insert (warnings/contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Local original-indication/registration data for lisinopril in Saudi Arabia
- Literature or trial search specifically targeting posterolateral/posteroinferior MI subtypes (not just "myocardial infarction" broadly) to confirm whether subtype-specific evidence exists

**Note on alternative candidate:** Among the other 9 predictions in this pack, "chronic pulmonary heart disease" (rank 9) has materially stronger support — 2 direct lisinopril studies (PMID 17047621, PMID 14524095, L3 evidence) and a "Proceed with Guardrails" recommendation, alongside a flagged DDI risk (lisinopril + tizanidine, PMID 20852161). This may be a more actionable repurposing candidate than the current top-ranked prediction and warrants separate evaluation. Conversely, ranks 3, 6, 8, and 10 are flagged in the source data as low-plausibility or safety-hold cases (including a possible embedding artifact and a relative-contraindication scenario in renovascular hypertension) and should not be pursued further without additional evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

