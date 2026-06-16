---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carvedilol: From Hypertension / Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a non-selective β-blocker and α1-blocker well established in the treatment of hypertension and heart failure; its original approved indications were not captured in the current dataset.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** — a severe, hypertension-driven form of acute kidney injury — based on its antihypertensive and renoprotective pharmacological profile.
Currently, **no clinical trials** and **no published literature** specifically supporting this repurposing direction were identified, placing this prediction at evidence level **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in dataset (established use: hypertension, heart failure) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (model prediction only, no empirical studies) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on well-established pharmacological knowledge, carvedilol is a third-generation, non-selective β1/β2/α1-adrenoceptor antagonist. Its antihypertensive effect arises from two complementary mechanisms: β1-blockade reduces cardiac output and suppresses renin release from juxtaglomerular cells, while α1-blockade lowers peripheral vascular resistance by relaxing arterial smooth muscle — including renal afferent arterioles. In addition, carvedilol possesses unique antioxidant properties attributed to its carbazole moiety, which may confer supplementary cytoprotection beyond pure adrenergic blockade.

Malignant hypertensive renal disease (malignant hypertensive nephropathy) is defined by severe, rapidly progressive hypertension causing fibrinoid necrosis of renal arterioles, glomerular ischemia, and microangiopathic injury. The pathophysiology is driven by extreme glomerular hyperperfusion and activation of the renin-angiotensin-aldosterone system (RAAS). Rapid blood pressure reduction is the cornerstone of treatment. Carvedilol's dual adrenergic blockade directly addresses both the systemic pressure load and the renal RAAS hyperactivation, providing a mechanistically coherent rationale for potential benefit.

That said, carvedilol's role in this specific disease context remains hypothetical. The TxGNN model's high score (99.55%) most likely reflects the strong structural and pharmacological overlap between blood pressure control and hypertensive nephropathy in the knowledge graph, rather than disease-specific clinical evidence. No clinical trial or targeted literature was identified. This prediction should be treated as a hypothesis-generating signal requiring prospective validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Carvedilol is not approved or marketed in Taiwan; no product authorizations are on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on the TxGNN model output (L5) with zero supporting clinical trials or targeted literature. While the mechanistic rationale connecting carvedilol's dual adrenergic blockade to malignant hypertensive renal disease is pharmacologically plausible, the complete absence of empirical evidence precludes any advancement toward clinical application at this stage. Notably, the four remaining top-ranked predictions — malignant renovascular hypertension, pulmonary hypertension due to hypoxia (WHO Group 3), pulmonary hypertension with multifactorial mechanism (WHO Group 5), and Braddock syndrome — are all also at L5 with no supporting evidence, and two of the pulmonary hypertension indications carry active safety concerns (β-blockade may be relatively contraindicated).

**To proceed, the following is needed:**

- Broaden literature search using alternative MeSH terms (e.g., "hypertensive emergency," "hypertensive nephropathy," "malignant hypertension kidney") to confirm no relevant studies were missed
- Retrieve complete carvedilol MOA documentation from DrugBank (DB01136) to formally characterize the mechanistic link
- Obtain Taiwan package insert (仿單) to assess contraindications and key warnings — currently a blocking data gap (DG001)
- Assess whether published guidelines for malignant hypertension mention β/α-blocker use, to determine if carvedilol occupies any adjunctive role
- Evaluate safety of carvedilol in severe renal impairment (GFR < 30 mL/min) before any renal disease repurposing study design
- If the mechanistic rationale is confirmed by domain experts, initiate a scoping review protocol before committing to preclinical or clinical study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

