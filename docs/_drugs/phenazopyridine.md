---
layout: default
title: Phenazopyridine
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 1
---

# Phenazopyridine
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

# Phenazopyridine: From Urinary Tract Pain (Dysuria) to Bronchitis

## One-Sentence Summary

> Phenazopyridine is an azo-dye urinary tract analgesic traditionally used to relieve burning and pain during urination.
> The TxGNN model predicts it may be effective for **Bronchitis**, but this is currently a **pure model prediction**
> with **no clinical trials, no literature, and no mechanistic overlap** identified to support the connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on file (no Saudi Arabia license); known pharmacological use is relief of urinary tract pain/dysuria (azo dye local anesthetic) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% (rank 11,012 among predictions) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (recorded as a data gap). Based on known pharmacology, phenazopyridine is an azo-dye local anesthetic that acts topically on the urinary tract mucosa to relieve dysuria (burning pain during urination). It has no established action on airway epithelium, respiratory inflammatory pathways, or respiratory pathogens.

Bronchitis is a respiratory tract inflammatory/infectious condition. There is no known pharmacological, anatomical, or mechanistic overlap between phenazopyridine's urinary-tract analgesic action and bronchitis pathophysiology.

The TxGNN score of 0.992 reflects similarity within the model's knowledge-graph embedding space, not a validated mechanistic or clinical relationship. In this case the model's own evidence review explicitly flags the mechanistic link as absent, and this is corroborated by a complete lack of supporting clinical trials or literature. This prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN embedding score (L5) with no clinical trials, no literature, and no plausible mechanistic pathway connecting a urinary-tract analgesic to bronchitis. The drug is also not currently marketed in Saudi Arabia. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/original regulatory package insert (warnings, contraindications, DDI)
- Any preclinical or mechanistic studies establishing a plausible link between phenazopyridine and respiratory tract inflammation
- Re-evaluation once independent clinical or literature evidence emerges; absent that, this candidate should not proceed past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

