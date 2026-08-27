---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a triazole antifungal originally used to treat fungal infections such as candidiasis and cryptococcal meningitis. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (e.g., candidiasis, cryptococcal meningitis) — general antifungal indication; local approved-label text is not available (drug is not currently marketed here) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on general pharmacological knowledge, fluconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol synthesis in the fungal cell membrane — its efficacy in fungal infections is well established.

Punctate epithelial keratoconjunctivitis, however, is most commonly caused by viral infection (e.g., adenovirus) or autoimmune processes (e.g., Thygeson's superficial punctate keratitis) rather than fungal infection. While fungal keratoconjunctivitis does exist as a distinct clinical entity, it is not the typical etiology behind this diagnostic label.

Given this mismatch between fluconazole's known antifungal mechanism and the predominantly non-fungal etiology of the predicted indication, the mechanistic link should be considered weak and speculative rather than well-supported. This prediction currently reflects a model-derived association only, without independent mechanistic, preclinical, or clinical corroboration.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5, no clinical or literature evidence), and the underlying mechanistic rationale is weak given the predominantly viral/autoimmune etiology of the target condition. Core safety data (TFDA package insert warnings/contraindications) is also a Blocking data gap, preventing any S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (DG001, Blocking — required before any safety screening can begin)
- Confirmed mechanism of action data via DrugBank (DG002)
- Preclinical or mechanistic studies specifically addressing fluconazole's activity in non-fungal punctate epithelial keratoconjunctivitis
- Any emerging clinical trial or literature evidence to raise the evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

