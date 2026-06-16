---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan Cilexetil is an angiotensin II receptor blocker (ARB) widely used to treat hypertension and to provide cardiorenal protection in chronic kidney disease and heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** with a prediction score of **99.68%**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this specific indication — the mechanistic rationale is strong, but clinical evidence is entirely absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Cardiorenal protection (general ARB class indication; no SFDA-registered license on file) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured DrugBank fields in this Evidence Pack. Based on known pharmacology and the mechanistic context provided in the repurposing rationale, Candesartan Cilexetil is a prodrug that is hydrolysed to its active form, Candesartan, which selectively blocks the angiotensin II type 1 (AT1) receptor. This inhibits angiotensin II-mediated vasoconstriction, aldosterone secretion, and TGF-β-driven renal fibrosis, resulting in renal afferent and efferent arteriolar dilation, reduced intraglomerular pressure, and attenuation of tubular fibrosis.

Malignant hypertensive renal disease is a severe end-organ complication in which sustained, extreme blood pressure elevation causes fibrinoid necrosis of renal arterioles, rapidly progressive nephrosclerosis, and loss of GFR. The renin–angiotensin–aldosterone system (RAAS) is highly activated in this condition, making AT1 receptor blockade a mechanistically well-matched intervention. Landmark RCTs such as IDNT and RENAAL have demonstrated that ARBs reduce the rate of renal function decline and proteinuria in hypertensive nephropathy and diabetic nephropathy — conditions that share substantial pathophysiological overlap with malignant hypertensive renal disease.

The gap between mechanistic plausibility and clinical evidence is the central challenge here. No trial or publication with the precise ICD diagnostic code for "malignant hypertensive renal disease" has been indexed. This likely reflects a classification and coding gap rather than genuine absence of biological rationale: most real-world evidence is embedded within broader hypertensive nephropathy or CKD trials, not coded to this specific entity. A focused literature re-query using alternate MeSH terms (hypertensive nephrosclerosis, malignant nephrosclerosis) and review of IDNT/RENAAL sub-analyses may recover relevant evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Candesartan Cilexetil in Malignant Hypertensive Renal Disease.

> **Note:** The absence of indexed trials reflects the specificity of the disease label. Broader hypertensive nephropathy trials (e.g., IDNT for irbesartan, RENAAL for losartan) provide class-level evidence for ARBs and may inform feasibility planning for a candesartan-specific study.

---

## Literature Evidence

Currently no related literature directly linking Candesartan Cilexetil to Malignant Hypertensive Renal Disease is available.

> **Note:** Twenty publications were retrieved for the adjacent indication "pulmonary hypertension owing to lung disease and/or hypoxia" (Rank 4), but all were classified as non-relevant (general hypoxia reviews covering brain aging, oncology, and multiple sclerosis with no direct connection to candesartan or pulmonary hypertension). They are excluded here per relevance standards.

---

## Saudi Arabia Market Information

Candesartan Cilexetil is **not currently registered** with the Saudi Food and Drug Authority (SFDA). No active licenses or approved indications are on file as of the data cutoff (2026-06-15).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Status:** Key warnings, contraindications, and drug-drug interaction data were not retrievable from the structured sources queried. A known class-level safety concern relevant to this evaluation: **ARBs are contraindicated in bilateral renal artery stenosis**, which can present similarly to malignant renovascular hypertension. Renal function (serum creatinine, eGFR) and potassium levels require close monitoring when initiating therapy in any hypertensive nephropathy patient.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between AT1 receptor blockade and attenuation of hypertensive renal injury is scientifically sound and supported by class-level RCT evidence (IDNT, RENAAL), but no clinical trial or publication has been indexed specifically for candesartan cilexetil in malignant hypertensive renal disease under this diagnostic code, placing this prediction at Evidence Level L5. A Research Question designation is appropriate — this is a hypothesis worth investigating, not a candidate ready for development.

**To proceed, the following is needed:**

- **Broader literature re-query** using MeSH terms "hypertensive nephrosclerosis," "malignant nephrosclerosis," and "accelerated hypertension renal failure" combined with "candesartan" or "ARB" to surface evidence miscoded under alternate labels
- **Sub-analysis review** of IDNT (irbesartan) and RENAAL (losartan) for malignant-phase or rapidly progressive subgroups — provides class evidence that may anchor a candesartan research proposal
- **MOA data retrieval** from DrugBank API (DG002) to formally document AT1 antagonism and support mechanistic write-up
- **Safety package completion** (DG001): retrieval of SFDA/TFDA package insert warnings and contraindications, particularly bilateral RAS exclusion criteria, before any clinical feasibility assessment
- **Clarification of disease scope**: confirm whether "malignant hypertensive renal disease" as used in this model maps to ICD-10 I12/I13 hypertensive CKD subgroups or to the narrower "malignant phase" / hypertensive emergency with acute kidney injury — this determines which trial designs are applicable
- If literature re-query yields ≥1 relevant observational study or RCT sub-analysis, evidence level may be upgraded to L3/L4 and decision reconsidered as **Proceed with Guardrails**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

