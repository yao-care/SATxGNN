---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 2
---

# Carbetocin
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

# Carbetocin: From Postpartum Haemorrhage Prevention to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a synthetic long-acting oxytocin analogue (oxytocin receptor agonist), clinically established for prevention of uterine atony and postpartum haemorrhage following caesarean section.
The TxGNN model predicts it may be effective for **Isotretinoin-like Syndrome**,
however **no clinical trials** and **no published literature** currently support this direction — the prediction is driven solely by knowledge graph topology.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of uterine atony and postpartum haemorrhage (oxytocin receptor agonist, established pharmacological class) |
| Predicted New Indication | Isotretinoin-like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Carbetocin is a long-acting synthetic analogue of endogenous oxytocin, acting selectively on the oxytocin receptor (OXTR). Its pharmacological action is concentrated on two domains: peripheral smooth muscle contraction of the uterus (driving its use in postpartum haemorrhage prevention), and central nervous system modulation of social behaviour and bonding through the oxytocin pathway.

Isotretinoin-like syndrome (retinoic acid embryopathy) arises from excessive retinoic acid exposure during embryonic development, causing aberrant cranial neural crest cell migration and differentiation via the RAR/RXR nuclear receptor signalling pathway. This is a developmental teratogenicity syndrome — not a disease state that involves oxytocin receptor biology in any known mechanistic framework. There is no documented biochemical crossover between OXTR signalling and retinoic acid/RAR/RXR pathways in the current literature.

The very high TxGNN score (99.15%) therefore reflects knowledge graph topological proximity — likely mediated through shared network neighbours in the disease–gene–protein interaction graph — rather than a direct biological hypothesis. In the absence of any experimental, preclinical, or mechanistic evidence, this must be classified as a distant model-driven prediction with very low clinical credibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Carbetocin is not currently registered or authorised by SFDA in Saudi Arabia. No product licence records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, the mechanistic pathway of carbetocin (OXTR agonism → uterine contraction / CNS oxytocin modulation) has no known intersection with isotretinoin-like syndrome pathophysiology (excess retinoic acid → RAR/RXR-mediated cranial neural crest disruption). With zero supporting clinical trials or literature, and evidence classified at L5, advancing this candidate would require first establishing a plausible biological hypothesis — which does not currently exist.

Note: The second-ranked prediction (Goodman syndrome / ACPS IV, TxGNN score 99.06%) faces an identical evidence vacuum and an equally distant mechanistic rationale (RAB23/Hedgehog pathway vs. OXTR), and is likewise recommended Hold pending any hypothesis generation.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking OXTR signalling to retinoic acid embryopathy or neural crest biology (e.g., oxytocin–retinoic acid crosstalk in neural development)
- Preclinical in vitro or in vivo data demonstrating any relevant biological effect of carbetocin in a teratogenicity or neural crest model
- Full mechanism of action data from DrugBank (DG002: currently missing)
- SFDA package insert safety data including warnings and contraindications (DG001: currently missing)
- Review of whether isotretinoin-like syndrome is a viable therapeutic target at all (it is a teratogenicity outcome syndrome, not a chronic treatable disease state)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

