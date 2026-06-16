---
layout: default
title: Calcium Lactate Gluconate
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 2
---

# Calcium Lactate Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Calcium Lactate Gluconate: From Calcium Supplementation to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium lactate gluconate is a highly bioavailable calcium salt used as a calcium supplement in pharmaceutical and functional food formulations, with no registered indication in Taiwan.
The TxGNN model's top-ranked prediction is **Calcium-Alkali Syndrome** (score 99.34%), but the mechanistic analysis identifies this as a **likely false positive** — the drug is a causative agent of this syndrome, not a therapeutic candidate.
The second-ranked prediction, **Primary Bone Dysplasia with Defective Bone Mineralization** (score 99.28%), carries more scientific rationale for calcium-deficiency subtypes, yet remains at evidence level **L5** with no clinical trials or literature identified for either indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No registered indication (not marketed in Taiwan) |
| Predicted New Indication (Rank 1) | Calcium-Alkali Syndrome ⚠️ Likely false positive |
| Predicted New Indication (Rank 2) | Primary Bone Dysplasia with Defective Bone Mineralization |
| TxGNN Prediction Score | 99.34% (Rank 1) / 99.28% (Rank 2) |
| Evidence Level | L5 (Model prediction only, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for calcium lactate gluconate. Based on its known pharmacological properties, it is a soluble calcium salt that delivers ionizable calcium with high gastrointestinal bioavailability — making it a preferred form for oral calcium supplementation in both pharmaceutical preparations and functional foods.

**Rank 1 — Calcium-Alkali Syndrome: A Predicted False Positive**

The TxGNN model likely identified calcium lactate gluconate through the calcium ion metabolism node and linked it to calcium-alkali syndrome. However, the clinical direction is entirely reversed: calcium-alkali syndrome is caused by excessive intake of absorbable calcium combined with alkaline substances, resulting in hypercalcemia, metabolic alkalosis, and renal impairment. Calcium lactate gluconate is itself a causative agent of this syndrome when taken in excess — not a therapeutic drug. This prediction should be treated as a model false positive arising from an incorrect causal direction (drug → disease, not drug ← disease).

**Rank 2 — Primary Bone Dysplasia with Defective Bone Mineralization: Mechanistically Plausible but Scope-Limited**

Calcium lactate gluconate can provide highly bioavailable ionic calcium, which is an essential substrate for hydroxyapatite crystallization during bone mineralization. In bone mineralization disorders where dietary calcium deficiency is the primary driver — such as nutritional rickets — calcium supplementation has a clear mechanistic rationale. However, most primary bone dysplasias involve genetic defects in alkaline phosphatase (*ALPL*), phosphate metabolism (*PHEX*), or collagen biosynthesis genes. Calcium supplementation cannot correct these upstream genetic defects, and the expected clinical benefit is therefore limited to the narrow calcium-deficiency subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for either predicted indication.

---

## Literature Evidence

Currently no related literature available for either predicted indication.

---

## Taiwan Market Information

Calcium lactate gluconate has no registered product authorizations in Taiwan. The drug is currently not marketed and holds zero licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (calcium-alkali syndrome) is a likely false positive due to incorrect causal direction — this drug is an established cause of the syndrome, not a treatment for it. The second-ranked prediction (primary bone dysplasia) has limited mechanistic plausibility restricted to calcium-deficiency subtypes only, and neither indication is supported by any clinical trials or published literature (evidence level L5).

**To proceed, the following is needed:**
- Retrieve formal MOA data from DrugBank (DG002) to enable mechanistic linkage analysis
- Determine whether any subtype of primary bone dysplasia with defective bone mineralization is primarily driven by calcium deficiency rather than a genetic defect — this would identify the actionable patient population
- Conduct a targeted literature search on calcium supplementation in nutritional rickets and hypocalcemia-associated bone dysplasia
- Review TxGNN model outputs for other calcium-based compounds to assess whether calcium-alkali syndrome appears systematically as a false positive class
- Retrieve Taiwan package insert warnings and contraindications (DG001) before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

