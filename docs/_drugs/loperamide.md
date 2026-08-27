---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripheral opioid-receptor agonist widely used to treat acute and chronic diarrhea.
The TxGNN model's top-ranked prediction is **Acute Contagious Conjunctivitis**,
but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model score with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhea (globally established use; no market-specific approved-indication text available — see note below) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty because loperamide has no marketing authorization on record in this dataset, so no approved-indication text could be extracted. "Diarrhea" above reflects loperamide's well-established international use, not a market-specific label.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap). Based on generally established pharmacology, loperamide is a peripheral µ-opioid receptor agonist acting on intestinal smooth muscle to reduce motility and secretion; it does not meaningfully cross the blood-brain barrier at therapeutic doses and has no known ocular or conjunctival target.

Per the evidence pack's own assessment: *"無機轉關聯、無臨床或文獻證據，僅為 TxGNN 預測分數"* — there is no mechanistic link and no clinical or literature evidence behind this candidate; it is a model score only. Acute contagious conjunctivitis is an infectious/inflammatory ocular surface condition with no plausible pharmacological connection to a gut-restricted anti-motility agent, so the high TxGNN score most likely reflects embedding-space proximity within a conjunctivitis-disease cluster rather than a genuine therapeutic signal (several lower-ranked candidates in this pack — chronic follicular conjunctivitis, conjunctival folliculosis, parasitic conjunctivitis, serous conjunctivitis — form the same unsupported cluster).

Separately, it is worth noting that other predictions in this evidence pack carry actual safety signal: literature on amebic dysentery (rank 2) reports a case of fulminant amoebic colitis associated with loperamide use, consistent with anti-motility agents being contraindicated in invasive enteric infections. This reinforces that loperamide's GI-restricted mechanism does not generalize to unrelated indications and should not be interpreted as support for the conjunctivitis prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Loperamide currently holds no marketing authorization on record in this dataset (`total_licenses = 0`, `market_status = 未上市/Not Marketed`), so no license table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute contagious conjunctivitis) is evidence level L5 — a model score with no clinical trials, no literature, and no plausible mechanistic rationale given loperamide's gut-restricted, non-CNS-penetrant pharmacology. There is no basis to advance this candidate past preliminary screening.

**To proceed, the following is needed:**
- Confirmed MOA data (DG002, High severity) to properly assess mechanistic plausibility for any candidate indication
- TFDA/SFDA package insert warnings and contraindications (DG001, Blocking) before any safety pre-assessment (S1) can proceed
- If repurposing work continues, prioritize re-scoring lower-ranked but evidence-backed candidates in this pack (e.g., gastroduodenitis, L3, flagged "Research Question") over the top TxGNN score alone
- Flag amebic/infectious diarrhea indications as a **contraindication signal**, not an opportunity, given the fulminant colitis case report (PMID 17241255)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

