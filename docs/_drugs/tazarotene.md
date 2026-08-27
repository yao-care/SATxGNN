---
layout: default
title: Tazarotene
parent: 僅模型預測 (L5)
nav_order: 597
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tazarotene: From Topical Retinoid Therapy to Seborrheic Dermatitis

## One-Sentence Summary

> Tazarotene is a topical retinoid compound; its original approved indication is not on file for this market (the drug is currently unmarketed in Saudi Arabia).
> The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**, with the top prediction score in this evidence pack (99.79%),
> but supporting evidence is currently limited to a single, disease-mismatched clinical trial and no dedicated literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not marketed locally) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tazarotene has not yet been retrieved for this evidence pack (flagged as a High-severity data gap, remediation pending via DrugBank API query). Based on the mechanistic rationale attached to this prediction, tazarotene acts as a RAR-β/γ selective retinoid receptor agonist that modulates keratinocyte differentiation and suppresses inflammatory mediators via RAR signaling — a mechanism class already used topically in other keratinization-related dermatoses.

However, the mechanistic link to seborrheic dermatitis is assessed as weak. Seborrheic dermatitis is primarily driven by *Malassezia*-associated inflammation and sebaceous gland dysregulation rather than a keratinization disorder, so the connection to tazarotene's known retinoid activity is theoretical extrapolation rather than a direct pathophysiological link supported by dedicated evidence.

For context, this TxGNN run also generated two lower-ranked candidates for tazarotene: **seborrheic keratosis** (score 99.51%, evidence level L4, stage "Research Question") — supported by a systematic review and a comparative RCT-type study of topical keratosis treatments including tazarotene — and **vulvar inverted follicular keratosis** (score 99.38%, evidence level L5, "Hold") with no supporting trials or literature. Despite its lower TxGNN score, seborrheic keratosis currently has a stronger evidentiary basis than the top-ranked seborrheic dermatitis prediction and may warrant closer follow-up.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | NA | Unknown | 40 | Studies platelet-rich plasma plus topical retinoids vs. topical retinoids alone in **acne vulgaris**, not seborrheic dermatitis. Flagged as relevance grade C (disease mismatch) and does not support this indication. |

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Tazarotene currently holds no marketing authorization in Saudi Arabia (0 licenses on file); no product/dosage-form records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial linked to this prediction studies a mismatched population (acne vulgaris, not seborrheic dermatitis), there is no supporting literature, and the mechanistic rationale is explicitly assessed as weak/theoretical. In addition, safety/warning data required for initial safety screening (S1) is currently unavailable — a Blocking-severity data gap.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (Blocking gap — required before any S1 safety assessment)
- Confirmed mechanism-of-action data via DrugBank API (High-severity gap)
- Dedicated clinical trials or literature evaluating tazarotene specifically in seborrheic dermatitis
- Consider reprioritizing research effort toward **seborrheic keratosis**, which currently has stronger literature support (systematic review + comparative study) despite its lower TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

