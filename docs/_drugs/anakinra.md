---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Autoinflammatory Disorders to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra is a recombinant human interleukin-1 receptor antagonist (IL-1Ra), globally recognized as a treatment for rheumatoid arthritis and hereditary autoinflammatory syndromes. The TxGNN model assigns its highest-ranked prediction to **Extracutaneous Mastocytoma** with a score of **99.93%**; however, **no clinical trials and no published literature** currently support this direction, making this a model-only signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from local registration (no Saudi Arabia authorization on file) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Anakinra (Kineret) functions as a recombinant human IL-1 receptor antagonist — competitively blocking both IL-1α and IL-1β from binding to the IL-1 type I receptor. This mechanism underlies its proven efficacy in IL-1-driven conditions such as rheumatoid arthritis, systemic juvenile idiopathic arthritis (sJIA), neonatal-onset multisystem inflammatory disease (NOMID), and hereditary periodic fever syndromes.

Extracutaneous mastocytoma is a rare soft-tissue neoplasm characterized by clonal proliferation of mast cells outside the skin. The dominant pathogenic driver is a **KIT gain-of-function mutation** (most commonly D816V), which causes constitutive activation of the KIT receptor tyrosine kinase — an oncogenic mechanism entirely distinct from IL-1–mediated inflammation. While mast cells do secrete IL-1 and participate in inflammatory networks, IL-1 signaling is a secondary environmental feature rather than the core oncogenic event.

The TxGNN model's high prediction score (0.999) for this pairing most plausibly reflects **disease network topological proximity** — extracutaneous mastocytoma sits near other mast cell activation and autoinflammatory nodes in the biological knowledge graph — rather than a direct pharmacological rationale. Without any preclinical, translational, or clinical evidence to support IL-1 blockade in mastocytoma, this prediction should be treated as a hypothesis-generating signal only, not an actionable repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model's high prediction score, the mechanistic link between anakinra's IL-1Ra activity and extracutaneous mastocytoma (a KIT-mutation-driven neoplasm) is indirect at best. The complete absence of any supporting clinical trial or published literature means there is no empirical basis to advance this indication at this time.

**To proceed, the following is needed:**
- Preclinical evidence establishing a functional role of IL-1 signaling in extracutaneous mastocytoma tumor biology or microenvironment
- Mechanistic data (MOA) for anakinra retrieved from DrugBank API or an approved product monograph
- Safety profile review from SFDA, EMA, or FDA package insert (currently a blocking data gap)
- Re-evaluation of whether TxGNN network topology proximity correlates with any known mast cell–IL-1 co-regulatory axis

> **Note:** While the top TxGNN prediction (rank 1) warrants a Hold, higher-quality evidence exists for other predicted indications in this pack — notably **autosomal recessive familial Mediterranean fever** (rank 3, L3, Proceed with Guardrails) and **pyogenic autoinflammatory syndrome / PAPA spectrum** (rank 9, L3, Proceed with Guardrails) — both of which have direct mechanistic alignment with anakinra's IL-1Ra activity and are supported by published literature including at least one systematic review. Those indications may be more actionable for follow-on evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

