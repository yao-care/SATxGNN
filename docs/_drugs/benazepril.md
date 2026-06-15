---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 5
---

# Benazepril
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE (angiotensin-converting enzyme) inhibitor, a drug class established for treating hypertension and cardiovascular-renal conditions, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
with **no registered clinical trials** and **no direct publications** currently identified for this specific drug-disease pair — however, the prediction is strongly supported by ACE inhibitor class-effect mechanistic evidence, as renovascular hypertension is driven by the very pathway this drug class blocks.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / cardiovascular-renal protection (ACE inhibitor class; not registered in Saudi Arabia) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Benazepril belongs to the ACE inhibitor (ACEi) drug class. Although formal DrugBank MOA data is currently unavailable, ACE inhibitors work by blocking the renin-angiotensin system (RAS): they inhibit the enzymatic conversion of angiotensin I to angiotensin II, thereby reducing systemic vasoconstriction, lowering blood pressure, and suppressing aldosterone-mediated sodium retention.

Malignant renovascular hypertension is mechanistically defined by pathological overactivation of the renin-angiotensin system — typically triggered by renal artery stenosis causing ischemia-driven renin hypersecretion. This creates an angiotensin II surge that drives severe, rapidly progressive hypertension with end-organ damage (retinopathy, encephalopathy, renal failure). ACE inhibitors directly interrupt this disease-driving pathway at its effector step, making the TxGNN prediction biologically compelling and consistent with established pharmacology.

There is, however, a critical safety paradox that governs clinical applicability: ACE inhibitors are **contraindicated** in bilateral renal artery stenosis (bilateral RAS) and in stenosis of a solitary functioning kidney. In these anatomical configurations, glomerular filtration is maintained by angiotensin II-mediated efferent arteriolar constriction — blocking this compensatory mechanism with an ACEi precipitates acute renal failure. Careful pre-treatment anatomical screening (renal Doppler ultrasound or MR angiography) to confirm unilateral disease is therefore a non-negotiable prerequisite before any clinical use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benazepril in malignant renovascular hypertension.

---

## Literature Evidence

Currently no direct publications linking Benazepril specifically to malignant renovascular hypertension are available.

> **Note on class-effect evidence:** Large RCTs with other ACE inhibitors provide indirect mechanistic support. The REIN trial (ramipril) demonstrated significant renoprotection in hypertensive nephropathy, and multiple studies confirm ACEi as first-line therapy for non-bilateral renovascular hypertension. Transferability of this class evidence to benazepril requires evaluation but is pharmacologically plausible.

---

## Saudi Arabia Market Information

Benazepril is not currently registered or marketed in Saudi Arabia. No authorization records are on file. Any clinical use would require regulatory pathway assessment via the Saudi Food and Drug Authority (SFDA) prior to deployment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical class-level warning:** ACE inhibitors (including benazepril) are contraindicated in bilateral renal artery stenosis and in renal artery stenosis of a solitary kidney. Administering an ACEi in these patients can precipitate acute, potentially irreversible renal failure. In the clinical context of renovascular hypertension evaluation, pre-treatment vascular imaging to exclude bilateral stenosis is mandatory before any ACEi therapy is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model identifies a mechanistically compelling prediction: ACE inhibitors directly block the renin-angiotensin system that drives malignant renovascular hypertension, and class-effect evidence from RCTs (e.g., ramipril REIN trial) provides credible indirect biological support. The prediction is not speculative — it reflects established cardiovascular pharmacology. However, no benazepril-specific clinical trials or literature exist for this indication, the drug is unregistered in Saudi Arabia, and the bilateral RAS contraindication introduces a safety-critical patient selection requirement that must be operationalized before any trial or clinical use.

**To proceed, the following is needed:**
- Retrieve formal MOA data from DrugBank (resolves data gap DG002) to confirm class membership and receptor binding profile
- Download and parse the benazepril package insert to document contraindications and warnings (resolves data gap DG001)
- Assess SFDA regulatory pathway for a currently unregistered drug (market access prerequisite)
- Define a mandatory pre-treatment imaging protocol (renal Doppler or MRA) to screen out bilateral RAS patients before any clinical evaluation
- Conduct a systematic literature review of class-effect ACEi data in renovascular hypertension to formally map transferability to benazepril
- Design an exploratory case series or single-arm pilot study in confirmed unilateral renovascular hypertension patients with close renal function monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

