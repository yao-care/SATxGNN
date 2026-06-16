---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# CHLORTHALIDONE: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic widely used in clinical practice for hypertension and edema management, though no formal original indication is recorded for this jurisdiction.
The TxGNN model predicts it may have potential for **Primary Hereditary Glaucoma** with a confidence score of **99.92%** (Rank #1 among all predictions).
However, **no clinical trials and no relevant literature** currently support this specific repurposing direction — this prediction remains at the L5 evidence level, a model-generated hypothesis with zero clinical translation to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no registered product in this jurisdiction) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no clinical studies) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this dataset. Based on known pharmacological classification, chlorthalidone is a thiazide-like diuretic that lowers blood pressure primarily by inhibiting sodium-chloride cotransporters (NCC) in the distal convoluted tubule, reducing sodium reabsorption, plasma volume, and ultimately systemic vascular resistance. Its diuretic effect is more prolonged than conventional thiazides (half-life ~40–60 hours).

The theoretical mechanistic bridge to glaucoma lies in intraocular pressure (IOP) reduction. Thiazide-like diuretics may lower IOP via two indirect pathways: (1) systemic osmotic effects that reduce aqueous humor production, and (2) a weak carbonic anhydrase inhibitory activity that loosely resembles the mechanism of established IOP-lowering agents such as acetazolamide and dorzolamide. However, chlorthalidone's overlap with dedicated carbonic anhydrase inhibitors is limited, and neither pathway has been shown to produce clinically meaningful IOP reduction at therapeutic diuretic doses.

Primary hereditary glaucoma is driven by genetic mutations — most commonly in *MYOC*, *CYP1B1*, and *LTBP2* — that impair trabecular meshwork drainage. A systemic volume-reducing agent does not address this structural outflow obstruction. The TxGNN model's high confidence score is likely attributable to shared graph nodes between cardiovascular and ophthalmologic disease networks, rather than a true pharmacological signal. No clinical or preclinical evidence specific to this indication was identified in the current evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Chlorthalidone has **no registered products or marketing authorizations** in Saudi Arabia at the time of this analysis. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model's highest-confidence prediction (99.92%) pointing to primary hereditary glaucoma, this indication is entirely unsupported by clinical trials or relevant published literature (Evidence Level L5). The mechanistic connection between a thiazide-like diuretic and a genetically-driven drainage disorder is indirect and speculative, and chlorthalidone holds no market authorization in Saudi Arabia.

**Notable finding across all 10 predicted indications:**
The strongest evidence-supported indication in this full analysis is **Chronic Pulmonary Heart Disease** (Rank #8, Evidence Level L3). A 1967 clinical observational study (PMID [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/)) directly reports chlorthalidone use in congestive heart failure caused by chronic cor pulmonale. While historical, this constitutes direct clinical evidence and warrants evaluation as a separate, higher-priority research question than the top TxGNN-ranked indication.

**To proceed, the following is needed:**

- **MOA data**: Retrieve from DrugBank to confirm pharmacological rationale for any target indication
- **Safety profile**: Obtain package insert warnings and contraindications from SFDA/TFDA to enable safety screening (currently a blocking data gap)
- **For chronic pulmonary heart disease** (Rank #8): Commission a systematic literature review to identify modern evidence building on the 1967 historical data; assess feasibility of a prospective observational study
- **For glaucoma indications** (Ranks #1–2): Require dedicated preclinical IOP studies with chlorthalidone before any clinical consideration
- **Regulatory pathway**: Given zero Saudi Arabia market authorizations, any advancement requires a full regulatory strategy for market entry alongside the repurposing program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

