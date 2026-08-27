---
layout: default
title: Ferric Carboxymaltose
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 1
---

# Ferric Carboxymaltose
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

# Ferric Carboxymaltose: From Iron Deficiency Anemia to Bronchitis

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement therapy, originally used to correct iron deficiency anemia (including in chronic kidney disease and heart failure patients). The TxGNN model predicts it may be effective for **Bronchitis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on knowledge-graph association alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (per evidence pack rationale; not confirmed via formal license text — no Taiwan license record available) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known information, ferric carboxymaltose is an intravenous iron formulation used to replenish iron stores and support erythropoiesis in iron deficiency anemia; its efficacy in that setting is well established, but no mechanistic or empirical link to bronchitis has been documented.

The evidence pack's own rationale is explicit that this connection is speculative: it notes only an "extremely indirect hypothesis" — that iron deficiency might affect airway mucosal immune function, or that anemia of chronic disease commonly co-occurs with respiratory symptoms — with no experimental or clinical data demonstrating a treatment effect on bronchitis.

A TxGNN score of 0.99 reflects the strength of association within the knowledge graph, not causal or clinical evidence. Given that both the original indication and MOA fields are themselves data gaps, and zero trials or publications exist for this drug-disease pair, the mechanistic plausibility of this prediction cannot currently be substantiated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

This product is not currently marketed in Taiwan (0 licenses on record); no authorization or product data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are flagged as a Blocking data gap — DG001 — required before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, literature, or mechanistic evidence connecting ferric carboxymaltose to bronchitis — the prediction is supported only by a TxGNN association score (L5, decision stage S0). A Blocking data gap on TFDA safety labeling also prevents any safety pre-assessment at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolves DG001 (Blocking)
- Confirmed drug mechanism of action from DrugBank — resolves DG002 (High)
- Confirmed original indication / license text (currently unavailable — 0 Taiwan licenses on record)
- Any preclinical, observational, or trial data specifically evaluating iron repletion in bronchitis, to move evidence level beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

