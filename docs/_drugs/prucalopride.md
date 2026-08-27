---
layout: default
title: Prucalopride
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Chronic Constipation to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist used clinically for chronic idiopathic constipation and related gastrointestinal motility disorders. The TxGNN model's top-ranked prediction for this drug is **Hypoalphalipoproteinemia** (low HDL cholesterol), but this prediction is supported by **no clinical trials and no literature**, and the evidence pack itself flags it as possible model noise from sparse training data. This is a low-confidence, model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic idiopathic constipation / GI motility disorders (inferred from evidence-pack rationale text; not confirmed via official MOA source — see below) |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (`original_moa` is a data gap). Based on information embedded in the repurposing rationale text, prucalopride is a selective 5-HT4 receptor agonist, clinically used to stimulate colonic motility in chronic idiopathic constipation and related dysmotility conditions.

Hypoalphalipoproteinemia is a lipid metabolism disorder characterized by abnormally low HDL cholesterol, typically driven by genetic defects in lipoprotein transport and metabolism (e.g., ABCA1, APOA1). There is no established physiological pathway linking 5-HT4 receptor agonism (a gut motility mechanism) to lipoprotein metabolism.

The evidence pack's own mechanistic assessment is explicit on this point: *"無已知機轉將 5-HT4 受体促效與脂蛋白代謝（HDL 過低）連結，無任何臨床或文獻證據，屬純預測分數，可能為 TxGNN 於稀疏資料下的雜訊輸出"* — i.e., no known mechanism connects the two, and the prediction may simply be model noise under sparse data. This prediction should therefore be treated as exploratory only, not as a biologically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Prucalopride is not currently marketed in Saudi Arabia (0 authorizations on record), so no licensing/product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication carries a high TxGNN score but no mechanistic plausibility, no clinical trial evidence, and no supporting literature; the evidence pack itself flags the score as potentially reflecting model noise rather than a real signal. Combined with the drug's unmarketed status in Saudi Arabia, this candidate does not meet the threshold for further evaluation.

**To proceed, the following is needed:**
- A biologically plausible mechanistic hypothesis linking 5-HT4 agonism to lipoprotein/HDL metabolism, if this candidate is to be revisited
- Official MOA and TFDA/SFDA-equivalent package insert data (currently blocking per data-gap DG001/DG002)
- Consider deprioritizing this candidate in favor of other predictions in the same evidence pack with stronger (though still indirect) support — notably **amyloidosis** and **primary amyloidosis** (rank 6 and 9, evidence level L4, "Research Question" stage), where literature indicates GI dysmotility from autonomic/smooth-muscle amyloid infiltration, offering a more plausible rationale for a prokinetic agent like prucalopride
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

