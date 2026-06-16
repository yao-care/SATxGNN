---
layout: default
title: Cilazapril
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 4
---

# Cilazapril
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

# Cilazapril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Cilazapril is an ACE (angiotensin-converting enzyme) inhibitor belonging to the RAAS drug class, classically used for the treatment of hypertension and heart failure.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension with Unclear Multifactorial Mechanism (Group 5 PH)**,
with **no clinical trials** and **no direct publications** currently supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / Heart Failure (ACE inhibitor class; no Saudi Arabia registration on file) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Cilazapril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II (Ang II), thereby reducing systemic vasoconstriction, lowering blood pressure, and decreasing aldosterone secretion. It belongs to the same drug class as Ramipril and Lisinopril, which have well-documented cardiovascular and renal protective effects.

The mechanistic connection to pulmonary hypertension with unclear multifactorial mechanism (Group 5 PH) runs through the RAAS pathway: Ang II promotes pulmonary vasoconstriction and vascular remodeling, so ACE inhibition could theoretically reduce pulmonary vascular resistance. This pathway-level similarity is likely what drove the high TxGNN score, as the model operates on biological network topology rather than direct clinical endpoints.

However, this theoretical plausibility does not translate to clinical practice. ACE inhibitors are **not** included in any current guideline as treatment for pulmonary arterial hypertension or Group 5 PH. The TxGNN score almost certainly reflects RAAS graph-topology similarity rather than a genuine therapeutic signal. There are currently no clinical trials or disease-specific publications to support this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Cilazapril has **no registered authorizations** in Saudi Arabia (SFDA). There are no approved products, licensed indications, or dosage forms on record. Any future use would require a new regulatory filing.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note — Critical Safety Signal for Rank 4 Prediction:** Although the primary focus of this report is the top-ranked indication, the evidence pack flags a clinically important contraindication for the rank 4 prediction (malignant renovascular hypertension): in patients with bilateral renal artery stenosis or stenosis of a solitary kidney, GFR maintenance depends on Ang II–mediated efferent arteriolar tone. ACE inhibition removes this compensatory mechanism and can precipitate **acute kidney injury**. This is a known absolute contraindication for ACE inhibitors in renovascular hypertension and must be factored into any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.20%) based on RAAS pathway graph similarity, but there is zero clinical trial evidence, zero disease-specific literature, and no regulatory precedent supporting Cilazapril for pulmonary hypertension with unclear multifactorial mechanism. An L5 evidence level is insufficient to justify advancement toward clinical evaluation without foundational data.

**Summary of All Four Predicted Indications:**

| Rank | Indication | Evidence Level | Recommendation |
|------|-----------|---------------|----------------|
| 1 | Pulmonary hypertension with unclear multifactorial mechanism | L5 | Hold |
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | L5 | Hold — 20 PubMed hits retrieved are general hypoxia biology papers, not Cilazapril-specific (likely keyword co-occurrence false positives) |
| 3 | Malignant hypertensive renal disease | L4 | Research Question — mechanistically plausible via ACE inhibitor class effect (AASK trial precedent for Ramipril/Lisinopril), but no Cilazapril-specific data |
| 4 | Malignant renovascular hypertension | L5 | Hold — **known contraindication**: bilateral renal artery stenosis risk of AKI with ACE inhibition |

**To proceed, the following is needed:**

- Retrieve full MOA documentation from DrugBank to formally confirm mechanistic plausibility
- Conduct a systematic review of ACE inhibitor class-level evidence across PH subtypes (Group 1–5) before concluding on Cilazapril
- Obtain and parse the package insert (SFDA or equivalent) for complete warnings, contraindications, and DDI profile — currently a blocking data gap
- Assess whether Rank 3 (malignant hypertensive renal disease) warrants a separate, more focused evidence-gathering effort, given that the ACE inhibitor class has RCT-level support (AASK trial) for hypertensive nephropathy
- Determine the regulatory pathway for first-time SFDA registration of Cilazapril in Saudi Arabia before any repurposing strategy can be operationalized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

