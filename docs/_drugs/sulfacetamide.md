---
layout: default
title: Sulfacetamide
parent: 僅模型預測 (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Sulfacetamide
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

# Sulfacetamide: From Bacterial Infections to Postinfectious Vasculitis

## One-Sentence Summary

Sulfacetamide is a sulfonamide-class antibacterial agent, historically used as a topical anti-infective (e.g., ophthalmic and dermatologic bacterial infections). The TxGNN model predicts potential efficacy for **Postinfectious Vasculitis**, but currently **no clinical trials** and **no published literature** support this specific direction, and the underlying mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (general antibacterial, sulfonamide class) |
| Predicted New Indication | Postinfectious Vasculitis |
| TxGNN Prediction Score | 99.99% (rank 267 among all predictions) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sulfacetamide. Based on general pharmacological knowledge, sulfacetamide is a sulfonamide-class antibacterial that competitively inhibits dihydropteroate synthase, blocking bacterial folate synthesis — a purely antimicrobial mechanism with no known immunomodulatory or anti-inflammatory activity.

Postinfectious vasculitis is an immune-mediated condition that typically arises *after* an infection has resolved, driven by immune complex deposition or aberrant immune activation rather than by ongoing bacterial replication. Because sulfacetamide's only established mechanism is antibacterial, there is no plausible pathway by which it would modulate the immune processes underlying vasculitis.

The evidence pack's own rationale is explicit on this point: "Postinfectious vasculitis is an immune-mediated disease; sulfacetamide has only an antibacterial (non-immunomodulatory) mechanism, with no reasonable direct link, and no clinical evidence exists." This should be treated as a high TxGNN-score but low biological-plausibility candidate — a pattern consistent with a false-positive prediction rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Sulfacetamide currently holds no marketing authorization in Saudi Arabia (0 licenses on record; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score, this candidate has zero supporting clinical trials or literature, and the proposed mechanism (antibacterial) does not plausibly address the immune-mediated pathology of postinfectious vasculitis. This is not sufficient evidence to advance beyond the model-prediction stage.

**To proceed, the following is needed:**
- Preclinical or mechanistic data demonstrating any immunomodulatory activity of sulfacetamide
- At minimum, case reports or observational data linking sulfonamide antibacterials to vasculitis outcomes
- TFDA/manufacturer package insert data to complete the S1 safety screen (currently blocked — DG001)
- Confirmed original indication and MOA data from DrugBank/regulatory sources (currently blocked — DG002)

**Additional note:** This evidence pack contains 10 TxGNN-predicted indications for sulfacetamide. Among them, **otitis externa** (rank 3) is materially better supported — evidence level L2, with two double-blind RCTs (PMID 6269476, PMID 207210) and a "Proceed with Guardrails" recommendation — though it reflects sulfacetamide's known traditional antibacterial use rather than a novel repurposing hypothesis. If a report is needed for a genuinely actionable candidate, otitis externa is recommended as the primary subject instead.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

