---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
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

# Alfacalcidol: From Renal Bone Disease to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Alfacalcidol (1α-hydroxycholecalciferol) is a synthetic active vitamin D analog established for treating renal osteodystrophy, secondary hyperparathyroidism in chronic kidney disease, and osteomalacia. The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion** with a prediction confidence of **99.61%**; however, no clinical trials or direct publications were retrieved in this data collection cycle—the evidence gap reflects a search limitation rather than an absence of clinical rationale, as the mechanistic link is well-established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal osteodystrophy / secondary hyperparathyroidism / osteomalacia (established clinical use; no Saudi Arabia authorization on record) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 (mechanistic / preclinical; no direct clinical trials or literature retrieved) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Alfacalcidol is a pro-drug of calcitriol (1,25-dihydroxyvitamin D₃). Unlike native vitamin D, it already carries the 1α-hydroxyl group and requires only hepatic 25-hydroxylation to become fully active. This bypasses the rate-limiting renal 1α-hydroxylation step, making it pharmacologically active even when renal function is impaired or absent.

In familial isolated hypoparathyroidism caused by impaired PTH secretion, the deficiency of PTH leads directly to reduced renal 1α-hydroxylase (CYP27B1) activity. The downstream consequences—hypocalcemia, hyperphosphatemia, and impaired intestinal calcium absorption—are precisely the metabolic disturbances that alfacalcidol is designed to correct. By activating the vitamin D receptor (VDR) independently of PTH, alfacalcidol compensates for the entire downstream deficit with a single mechanism.

This is therefore not a novel or speculative repurposing hypothesis. Active vitamin D analogs, including alfacalcidol and calcitriol, represent the pharmacological standard of care for hypoparathyroidism globally. The TxGNN model's high-confidence prediction (rank 6,572 out of all disease-drug pairs) reflects the strong graph-structural similarity between the disease node and alfacalcidol's established indication network. The absence of retrieved literature in this data pull is assessed as a search gap, not a clinical evidence gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication in the data collection.

> **Note:** This reflects the search query for the precise OMIM/Orphanet term "familial isolated hypoparathyroidism due to impaired PTH secretion." Broader searches for alfacalcidol in hypoparathyroidism are likely to yield results and are recommended as a remediation step.

---

## Literature Evidence

Currently no related literature retrieved for this specific indication.

> **Note:** Same search-scope caveat applies. The mechanistic rationale in the repurposing section draws on well-known pharmacology rather than retrieved publications. A targeted PubMed search using MeSH terms `alfacalcidol AND hypoparathyroidism` is recommended.

---

## Saudi Arabia Market Information

Alfacalcidol is not currently registered or marketed in Saudi Arabia. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Full safety data (warnings, contraindications, drug interactions) was not retrieved in this data collection cycle. The following general cautions are known from pharmacological class:
> - **Hypercalcemia risk**: The most important class-level adverse effect; requires periodic monitoring of serum calcium.
> - **Drug Interactions**: Thiazide diuretics may potentiate hypercalcemia; cholestyramine and mineral oil may reduce absorption.
> - **Contraindications**: Generally contraindicated in hypercalcemia and vitamin D toxicity states.
>
> These are provided for orientation only. Formal safety review requires retrieval of the SFDA-approved package insert.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between alfacalcidol and familial isolated hypoparathyroidism due to impaired PTH secretion is pharmacologically mature and represents the drug's core mechanism of action—the TxGNN model's prediction is biologically sound. However, the current evidence pack contains no retrieved clinical trials or direct publications, placing this at Evidence Level L4, insufficient to advance to a formal repurposing recommendation without additional evidence retrieval.

**To proceed, the following is needed:**

- **Targeted literature search**: Re-query PubMed using `alfacalcidol[MeSH] AND hypoparathyroidism` and related MeSH terms; the current zero-hit result is inconsistent with the drug's known clinical use and indicates a search parameter issue.
- **MOA data retrieval**: Query DrugBank API for DB01436 to populate the formal mechanism of action field (currently flagged as Data Gap DG002).
- **Safety data retrieval**: Download and parse the Saudi Arabia / SFDA package insert to complete warnings and contraindications (Data Gap DG001, Blocking severity).
- **Indication specificity mapping**: Confirm whether existing hypoparathyroidism registrations in other jurisdictions (e.g., Japan, EU, UK) explicitly cover the familial isolated PTH-secretion subtype, which would elevate the evidence level to at least L2–L3.
- **Regulatory pathway assessment**: Since this drug is not marketed in Saudi Arabia (0 authorizations), a parallel track for new drug registration or named-patient access should be scoped alongside any repurposing evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

