---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 1
---

# Adapalene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Adapalene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

Adapalene is a third-generation synthetic retinoid, primarily indicated for acne vulgaris treatment via selective activation of nuclear retinoic acid receptors.
The TxGNN model predicts it may be effective for **Zinc, Elevated Plasma**, with a high algorithmic score of 99.51%; however, there are currently **no clinical trials** and **no publications** supporting this direction, making this a model-prediction-only candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne Vulgaris (retinoid class; no local Saudi Arabia registration on record) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Adapalene is a third-generation synthetic retinoid (vitamin A analogue) that selectively activates the RAR-β and RAR-γ subtypes of retinoic acid receptors, as well as RXR nuclear receptors. Its primary therapeutic effect in acne comes from normalising keratinocyte differentiation and reducing follicular hyperkeratosis — a purely topical, locally confined mechanism with minimal systemic absorption under standard use.

The theoretical mechanistic link to zinc metabolism is indirect and structurally fragile. The DNA-binding domains of RAR/RXR receptors contain zinc finger motifs, creating a graph-level association between "retinoid receptor activation" and "zinc biology." Additionally, metallothionein — a zinc-binding protein — can in principle be upregulated by retinoid signalling. However, activating RAR/RXR receptors does not lower circulating plasma zinc; if anything, the relationship is directionally neutral or inverted. There is no published pharmacokinetic or mechanistic evidence that topical adapalene achieves systemic concentrations sufficient to influence zinc homeostasis.

The very high TxGNN score (0.995, rank 7,755) most likely reflects a **knowledge graph message-passing artefact**: the shared neighbourhood path "RAR/RXR → zinc finger proteins → zinc metabolism disorders" inflates the graph-based co-occurrence signal without corresponding biological or clinical plausibility. This pattern — high algorithmic score, zero real-world evidence — is a known limitation of graph neural network repurposing models and warrants caution before any downstream investment.

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
The prediction is L5 (model only) with no supporting clinical trials or literature, and the proposed mechanistic link between a topically applied retinoid and systemic zinc dysregulation lacks biological plausibility; the high TxGNN score is most likely a graph-structure artefact rather than a genuine therapeutic signal.

**To proceed, the following is needed:**
- Independent mechanistic validation: demonstrate whether any retinoid (oral or topical) can meaningfully alter plasma zinc in a relevant in vitro or in vivo model before committing to clinical investigation
- MOA data from DrugBank to confirm whether adapalene exerts any systemic effects that could reach zinc-regulating tissues
- Review of whether the TxGNN knowledge graph node for "zinc, elevated plasma" is sufficiently distinct from non-disease states (zinc supplementation, laboratory measurement artefacts) to represent a valid therapeutic target
- If pre-clinical plausibility is established, a targeted PubMed and ICTRP search using expanded query terms (e.g., "retinoid AND zinc metabolism") to rule out any unpublished or grey-literature signals
- Safety profile gap-fill: obtain full contraindication and warning data before any systemic formulation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

