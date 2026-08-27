---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 654
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan (DrugBank DB00177) is an angiotensin II receptor blocker (ARB) originally used to treat hypertension and related cardiovascular conditions. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this direction is currently supported only by **1 preclinical publication** (from a different drug class) and **0 clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(general pharmacological knowledge — Saudi-specific label text unavailable, drug not currently marketed locally)* |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker (ARB class), and its efficacy in hypertension has been well established clinically. Mechanistically, AT1 blockade lowers intraglomerular pressure and reduces proteinuria, which provides a plausible rationale for a renal-protective role in hypertensive nephropathy.

However, the strength of the supporting evidence for this specific candidate indication is limited. The single associated publication (PMID 24368192) studied **avosentan**, an endothelin receptor antagonist — a different drug class entirely — in a rat model of hypertensive nephropathy. This can only serve as indirect mechanistic support and does not directly demonstrate valsartan's effect in malignant hypertensive renal disease.

Notably, a closely related candidate in this Evidence Pack — **malignant renovascular hypertension** (rank 2, same TxGNN score tier) — is backed by more direct mechanistic evidence: PMID 11560862 shows AT1 receptor blockade (valsartan's own pharmacological class) preventing lethal malignant hypertension in an animal model, tied to renal fibrinoid necrosis driven by RAAS overactivation. This suggests the broader "malignant hypertension renal" cluster may warrant evaluation together rather than in isolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical (animal model; different drug class — avosentan) | Pharmacological research | In double-transgenic rats (human renin/angiotensinogen), endothelin antagonism at doses avoiding fluid retention was protective against hypertensive nephropathy; supports RAAS/endothelin-pathway relevance to renal protection but does not test valsartan directly. |

---

## Saudi Arabia Market Information

Valsartan is currently **not marketed** in Saudi Arabia (0 authorizations on file); no product license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The Saudi/SFDA package insert (warnings and contraindications) is flagged as a **Blocking** data gap (DG001) in this Evidence Pack, meaning the candidate cannot yet proceed to an S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this specific indication is preclinical and indirect only (L4 — one animal study from a different drug class, no clinical trials), and the drug is not currently marketed in Saudi Arabia. A blocking data gap on TFDA/SFDA label warnings and contraindications also prevents entry into S1 safety pre-assessment.

**To proceed, the following is needed:**
- SFDA package insert (warnings, contraindications) to clear the S1 safety gate
- Verified mechanism of action data from DrugBank (currently a data gap)
- Direct valsartan-specific evidence (clinical or preclinical) for malignant hypertensive renal disease, rather than cross-class inference
- Consider evaluating jointly with rank 2 ("malignant renovascular hypertension"), which has stronger direct AT1-blockade mechanistic support (L3, decision stage S1)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

