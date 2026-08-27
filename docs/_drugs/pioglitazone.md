---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 496
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# PIOGLITAZONE: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (TZD) / PPAR-γ agonist historically used as an insulin sensitizer in type 2 diabetes mellitus. The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare autosomal-recessive skeletal dysplasia, with a prediction score of **99.59%** — but this candidate is supported by **zero clinical trials** and **zero publications**, and the evidence pack itself flags the mechanistic link as likely graph-embedding noise rather than a real biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from drug class/literature context; no formal indication text available — see note below) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty and `original_indications` was not populated in this Evidence Pack, so no formal approved-indication text is available. The "Type 2 Diabetes Mellitus" original indication above is inferred from the drug class and repeated context in the supporting literature (thiazolidinedione, insulin resistance), not from a licensed label.*

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is marked as a data gap in this Evidence Pack. Based on the class context embedded in the supporting literature, pioglitazone is a thiazolidinedione that acts as a PPAR-γ agonist, improving peripheral insulin sensitivity and pancreatic beta-cell function in type 2 diabetes.

For the top-ranked candidate, **opsismodysplasia**, the repurposing rationale supplied with this pack is explicit that no credible mechanistic link exists: opsismodysplasia is a rare autosomal-recessive skeletal dysplasia associated with INPPL1/OSSA-related ossification defects, and there is no known biological connection between this pathway and PPAR-γ agonism. The rationale itself states that the high TxGNN score "should be attributed to knowledge-graph link noise, not mechanistic inference."

By contrast, several lower-ranked candidates in this pack show a more plausible (if still theoretical) mechanistic thread through PPAR-γ's role in adipocyte differentiation (e.g., the lipodystrophy/lipoatrophy cluster, ranks 5–8), and one candidate — pancreatic agenesis (rank 9) — has actual literature support, though the rationale notes this is likely keyword co-occurrence from general TZD/diabetes reviews rather than disease-specific evidence. None of the seven predicted indications in this pack currently rises above L4/L5 evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Pioglitazone is not marketed in Saudi Arabia under this Evidence Pack (`market_status: 未上市`, 0 authorizations recorded) — no product authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (opsismodysplasia) has only model-prediction-level evidence (L5) with no supporting trials or literature, and the pack's own mechanistic rationale characterizes the TxGNN association as likely graph noise rather than a genuine signal. No candidate among the seven predicted indications in this pack reaches L3 or higher.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank-sourced mechanism of action detail — currently a High-severity data gap (DG002)
- If pursuing a lipodystrophy-related candidate instead (ranks 5–8), preclinical/mechanistic studies directly testing PPAR-γ agonism in that disease context, since current rationale notes the drug's known clinical effect (fat redistribution/hypertrophy) may run counter to the therapeutic direction needed
- If pursuing pancreatic agenesis (rank 9), disease-specific studies rather than general T2DM/PPAR-γ reviews, since current literature does not address this population
- Saudi Arabia market/regulatory status confirmation, given the drug is currently unmarketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

