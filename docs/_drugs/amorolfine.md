---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine: From Onychomycosis to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a morpholine-class topical antifungal, primarily used for the treatment of onychomycosis (fungal nail infection) by inhibiting ergosterol biosynthesis in fungal cell membranes.
The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**,
however, **0 clinical trials** and **0 publications** currently support this direction — this prediction is based solely on the graph neural network model output.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infection) — topical antifungal use |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Amorolfine belongs to the morpholine class of antifungals and works by inhibiting two key enzymes (Δ14-reductase and Δ7-8-isomerase) in the ergosterol biosynthesis pathway — a mechanism specific to fungal cell membranes. Its clinical use is confined to topical application for onychomycosis, with minimal systemic absorption.

The mechanistic bridge between antifungal activity and drug-induced osteoporosis is extremely tenuous. Some azole-class antifungals (e.g., fluconazole, itraconazole) have been investigated for indirect effects on bone metabolism through CYP3A4 inhibition, which can alter corticosteroid levels. However, amorolfine is a morpholine — a structurally and mechanistically distinct class — with no known CYP3A4 interaction profile and no reported involvement in bone remodeling pathways.

The repurposing rationale provided in the dataset acknowledges this gap directly: there is no known direct or indirect mechanistic intersection between amorolfine's ergosterol-targeting pathway and bone metabolism. The TxGNN model likely captured a distant node connection in the disease–drug knowledge graph, but biological plausibility for this prediction is very low. This should be treated as a model artifact rather than a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Amorolfine is not currently registered or marketed in Saudi Arabia. No authorization records were found in the regulatory database query (SFDA). This means there is no existing approval pathway, local safety data, or market precedent to draw upon for any potential repurposing evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction data was identified in the DDI query. No key warnings or contraindications data were available in this Evidence Pack. Given that amorolfine is applied topically with very low systemic bioavailability, systemic safety risks are generally considered low — but this should be formally verified against the full prescribing information before any repurposing consideration proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for amorolfine are rated L5 (model prediction only), with zero supporting clinical trials or peer-reviewed literature across every disease target searched. The top prediction — drug-induced osteoporosis — has no credible mechanistic basis linking morpholine antifungal activity to bone metabolism, making this a likely false-positive arising from graph network topology rather than biological relevance.

**To proceed, the following is needed:**

- Obtain amorolfine's full pharmacokinetic profile (systemic absorption, Cmax, protein binding) to assess whether any systemic exposure could theoretically produce off-target effects
- Commission a formal mechanistic review to determine whether any morpholine-class antifungal has demonstrated activity relevant to bone remodeling (osteoclast/osteoblast biology, calcium metabolism, Wnt/RANK-L pathways)
- If systemic formulations of amorolfine exist in any market, obtain those package inserts to evaluate whether bone-related adverse events have been reported
- Re-evaluate lower-ranked TxGNN predictions for signals with stronger mechanistic plausibility (e.g., fungal infections of specific anatomical sites where amorolfine could realistically be reformulated for systemic or regional delivery)
- Consider whether amorolfine is even the appropriate drug to evaluate for repurposing given: (a) it has no Saudi Arabia regulatory footprint, (b) all predicted indications are L5, and (c) the drug class has no biological rationale for the predicted targets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

