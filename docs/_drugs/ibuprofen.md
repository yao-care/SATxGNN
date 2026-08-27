---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 7
---

# Ibuprofen
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

# Ibuprofen: From NSAID Analgesic Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Ibuprofen is a well-established NSAID (COX-1/COX-2 inhibitor) used for pain, inflammation and fever; its own approved-indication and Taiwan licensing data are not present in this evidence pack.
> The TxGNN model's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal disorder,
> but this and six other ranked candidates are supported by **0 clinical trials** and **0 publications** — model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Taiwan license or `original_indications` data). Ibuprofen is generically known as an NSAID for pain/inflammation/fever. |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ibuprofen is flagged as a data gap (DG002) in this pack. The only MOA information available comes from the model's own rationale notes, which describe ibuprofen as an NSAID that inhibits COX-1/COX-2 to reduce prostaglandin synthesis for anti-inflammatory and analgesic effect.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare hereditary skeletal dysplasia caused by GDF5 gene mutations, affecting cartilage formation and growth-plate development — a structural/developmental disorder, not an inflammatory or pain condition. The rationale accompanying this prediction explicitly states there is **no direct biological connection** between ibuprofen's COX-inhibition mechanism and GDF5-driven skeletal dysplasia, and attributes the high TxGNN score to indirect "bone/cartilage" node proximity in the knowledge graph rather than an established mechanistic pathway.

The remaining six ranked candidates (brachyolmia variants, myosclerosis, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) are similarly rare genetic/structural disorders, and their own rationale text likewise states "no known connection," "no direct relevance," or "theoretical only, no supporting evidence." One partial exception is pseudoachondroplasia, where NSAIDs could plausibly relieve secondary joint pain — but this reflects ibuprofen's existing standard analgesic use rather than a genuine new indication, and is unsupported by any disease-specific trial or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

No licenses currently registered for ibuprofen in this evidence pack — market status is 未上市 (not marketed), with 0 total authorizations recorded.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 7 TxGNN-predicted indications sit at evidence level L5 (model prediction only) with zero clinical trials and zero publications, and the model's own mechanistic rationale explicitly finds no meaningful biological link between ibuprofen's COX-inhibition mechanism and these rare genetic/structural disorders. Combined with a Blocking data gap on TFDA warnings/contraindications (DG001) and missing MOA confirmation (DG002), there is insufficient basis to advance past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed MOA via DrugBank API (DG002)
- Preclinical or mechanistic studies establishing biological plausibility for any candidate indication, particularly acromesomelic dysplasia (rank 1) or pseudoachondroplasia (rank 6, where symptomatic analgesic use is at least plausible)
- Taiwan regulatory/licensing status confirmation, since the drug is currently recorded as not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

