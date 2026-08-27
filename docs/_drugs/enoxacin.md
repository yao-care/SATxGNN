---
layout: default
title: Enoxacin
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Enoxacin
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

# Enoxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

> Enoxacin is a fluoroquinolone antibiotic, originally developed for bacterial infections (its mechanism of action targets bacterial DNA gyrase/topoisomerase IV).
> The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**,
> but **zero clinical trials** and **zero publications** currently support this direction — the prediction rests solely on a knowledge-graph score.

Note: this evidence pack contains 10 TxGNN-predicted indications for enoxacin (candidate set `TW-DB00467-multi`); all 10 carry the same evidence gap (no trials, no literature) and are scored L5/Hold. This report focuses on the top-ranked candidate and flags the others for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (no approved-indication records on file); enoxacin is a known fluoroquinolone-class antibacterial |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for enoxacin in this evidence pack. Based on known drug-class information, enoxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV; its efficacy against bacterial infections is well established.

However, the mechanistic link to the predicted indication is weak. Polyclonal hyperviscosity syndrome is a disorder of plasma cell/immunoglobulin overproduction, and there is no known pharmacological pathway connecting an antibacterial DNA-gyrase inhibitor to immunoglobulin metabolism or plasma viscosity regulation. The evidence pack's own rationale for this candidate explicitly states there is "no identifiable mechanistic link," and the same caveat applies to most of the other 9 ranked candidates in this set (e.g., hyperamylasemia, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy) — none of which have a plausible pharmacological connection to an antibacterial agent.

The one partial exception among the 10 candidates is rank 8, "septicemic plague" (caused by *Yersinia pestis*), where an antibacterial mechanism is at least directionally plausible. That candidate, however, ranks lower than the top prediction and still has no supporting clinical or literature evidence. Overall, the high TxGNN score for this top candidate should be interpreted as a graph-embedding signal rather than a mechanistically grounded hypothesis, and it should not be treated as clinical evidence on its own.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

No marketing authorization records found — enoxacin is currently not marketed in Saudi Arabia (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: package-insert warnings/contraindications and drug-drug interaction data could not be retrieved for this drug in the current evidence pack (flagged as a **Blocking** data gap — TFDA/label warnings and contraindications are required before this candidate can proceed to initial safety screening, S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported only by a TxGNN graph score (L5), with no clinical trials, no literature, and no coherent mechanistic rationale connecting enoxacin's antibacterial mode of action to polyclonal hyperviscosity syndrome. Combined with a blocking gap in safety/label data, there is insufficient basis to advance this candidate beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) package insert with warnings and contraindications — currently a blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- Preclinical or mechanistic studies establishing a biological rationale linking fluoroquinolone pharmacology to plasma cell/immunoglobulin disorders
- If pursuing repurposing further, consider prioritizing mechanistically more plausible candidates from this same prediction set (e.g., septicemic plague) over the top-ranked but mechanistically unsupported candidate
- Formal confirmation of enoxacin's original approved indication(s), which are not present in the current evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

