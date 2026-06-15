---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# ATOSIBAN: From Preterm Labor to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is a competitive oxytocin/vasopressin V1A receptor antagonist approved in multiple countries as a tocolytic agent to suppress uterine contractions and delay preterm birth. The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, a rare genetic eye disease caused by mutations such as *MYOC* and *OPTN*. This prediction is currently supported by **0 clinical trials** and **0 publications** specifically addressing this indication — it remains a model-prediction-only finding with no experimental validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preterm labor (tocolysis) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Atosiban acts as a competitive antagonist at oxytocin (OT) and vasopressin V1A receptors. In preterm labor, it blocks OT receptors on uterine smooth muscle, suppressing myometrial contractions. Beyond the reproductive system, OT receptors have been identified in ocular tissues including the ciliary body and the trabecular meshwork — structures that govern aqueous humor dynamics and intraocular pressure (IOP). This anatomical finding provides a theoretical foothold for the prediction: if OT signaling influences IOP regulation, an OT receptor antagonist might in principle modulate this pathway.

However, primary hereditary glaucoma is fundamentally a genetic disease. Pathogenic mutations in *MYOC*, *OPTN*, *FOXC1*, and related genes alter trabecular meshwork development and protein homeostasis, driving elevated IOP through structural and molecular mechanisms that are distinct from OT receptor signaling. Whether atosiban's receptor blockade could meaningfully intersect with these genetic pathways is not established, and the directionality of any IOP effect remains entirely unknown.

The high TxGNN score (99.92%) at rank 1805 is most likely attributable to knowledge graph neighborhood effects — a clustering of IOP-related disease nodes near vasopressin/OT pathway nodes — rather than a validated mechanistic connection. The pipeline's own annotation confirms this concern, noting that no data exists to support OT antagonism as a strategy for hereditary glaucoma and that gene-mutation-driven pathogenesis weakens the mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Primary Hereditary Glaucoma.

---

## Literature Evidence

Currently no related literature available for Primary Hereditary Glaucoma.

---

## Saudi Arabia Market Information

Atosiban has not been approved for marketing in Saudi Arabia. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, preclinical, or mechanistic evidence directly linking atosiban to primary hereditary glaucoma management. The prediction score reflects knowledge graph topology rather than pharmacological plausibility — and the genetic etiology of hereditary glaucoma (MYOC/OPTN mutations affecting trabecular meshwork architecture) does not align with OT receptor antagonism as a therapeutic strategy.

**To proceed, the following is needed:**
- Preclinical studies examining whether OT receptor blockade alters intraocular pressure in validated animal models of hereditary glaucoma
- Molecular characterization of OT receptor expression and function in trabecular meshwork cells carrying MYOC/OPTN mutations
- Mechanistic studies clarifying the downstream effect of OT signaling on aqueous humor outflow resistance
- Full MOA and safety data for atosiban (currently unavailable — TFDA package insert parsing and DrugBank API query required)
- Comparative review of the broader TxGNN glaucoma cluster (ranks 1805–1828) to assess whether the prediction represents a genuine signal or a systematic false-positive arising from graph neighborhood effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

