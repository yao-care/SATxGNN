---
layout: default
title: Trifarotene
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 2
---

# Trifarotene
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

# Trifarotene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

Trifarotene (DB12808) is not currently marketed in Saudi Arabia and its official original indication/mechanism-of-action data are missing from regulatory sources; based on the rationale embedded in this evidence pack, it is a topical RAR-γ selective retinoid known elsewhere for acne vulgaris. The TxGNN model's top prediction is **Zinc, Elevated Plasma**, with a 99.40% score but **zero supporting clinical trials or publications**, and the model's own rationale states no known pharmacological link exists between trifarotene and zinc metabolism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in regulatory filings (not marketed in Saudi Arabia); per the evidence pack's rationale text, trifarotene is a topical RAR-γ agonist known elsewhere for acne vulgaris |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trifarotene is currently a data gap in this evidence pack. Based on the rationale text accompanying the model's secondary prediction, trifarotene is known to be a fourth-generation topical RAR-γ selective retinoic acid receptor agonist, with an established use in acne vulgaris.

For the top-ranked prediction (**Zinc, Elevated Plasma**), the model's own mechanistic rationale explicitly states that no pharmacological relationship has been identified between trifarotene and zinc metabolism, plasma zinc regulation, metallothionein expression, or renal zinc excretion pathways. Trifarotene's target (RAR-γ) has no known connection to zinc homeostasis. This prediction therefore rests on the TxGNN similarity score alone, with no mechanistic or clinical corroboration — consistent with its L5 evidence level and "Hold" recommendation.

A second, lower-scoring prediction in this pack (**pyogenic arthritis-pyoderma gangrenosum-acne syndrome / PAPA syndrome**, score 99.32%) is mechanistically more plausible, since severe cystic acne is one of PAPA syndrome's three defining features, and trifarotene's keratinocyte-modulating effect could theoretically address that acne component. However, this connection is only to one symptom domain — it does not extend to the disease's inflammasome-driven arthritis or pyoderma gangrenosum components, and it is likewise unsupported by any clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Trifarotene is not currently marketed in Saudi Arabia (0 authorizations on record); no license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA label warnings and contraindications for trifarotene are a flagged Blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Zinc, Elevated Plasma) has no supporting clinical trials, no literature, and no plausible mechanistic link per the model's own rationale — this is a pure L5 model-score prediction. In addition, a Blocking data gap on TFDA/SFDA label warnings and contraindications means the drug cannot yet enter initial safety screening (S1) for any indication.

**To proceed, the following is needed:**
- Official TFDA/SFDA package insert (warnings, contraindications, DDI) — currently a Blocking gap
- Confirmed original mechanism of action and approved indication from DrugBank or regulatory sources
- If pursuing the secondary signal (PAPA syndrome) instead, dedicated literature/trial search and expert mechanistic review, since current evidence is limited to symptom overlap with acne
- Re-evaluation once any clinical trial or literature evidence emerges for either predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

