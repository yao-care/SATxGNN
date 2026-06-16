---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 1
---

# Domperidone
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

# Domperidone: From Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist, widely used as a prokinetic agent and antiemetic for nausea, vomiting, and gastroparesis.
The TxGNN model predicts it may have activity in **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
however there are currently **no registered clinical trials and no supporting publications** for this direction, leaving the prediction entirely model-driven.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nausea, vomiting, and gastroparesis (peripheral dopamine antagonist / prokinetic) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (0 registered products) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Domperidone is a **peripheral dopamine D2/D3 receptor antagonist** that does not readily cross the blood-brain barrier. Its prokinetic and antiemetic effects arise from blockade of D2 receptors in the gastrointestinal tract and chemoreceptor trigger zone.

The proposed mechanistic link to NSIAD is indirect and speculative. Dopaminergic signaling is known to have modulatory effects on renal collecting duct AQP2 water channels and V2 receptor (AVPR2) pathways. In theory, peripheral D2R antagonism could influence these downstream signals. However, NSIAD arises from a **constitutively activating gain-of-function mutation in AVPR2**, causing the V2 receptor to remain permanently active regardless of vasopressin or upstream dopaminergic tone. Blocking D2 receptors cannot correct a constitutively active V2R conformation.

The mechanistic rationale, as also noted in the Evidence Pack's own `repurposing_rationale`, is **extremely weak and purely inferential**, with no biochemical, cellular, or animal-model data supporting a direct effect of domperidone on NSIAD pathophysiology. The TxGNN model's high confidence score likely reflects latent graph topology patterns rather than a validated mechanistic signal.

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
This is a pure TxGNN model prediction (Evidence Level L5) with no registered clinical trials, no published literature, and a mechanistically implausible link — NSIAD is driven by constitutive AVPR2 gain-of-function that is upstream of and independent of dopaminergic modulation. Additionally, domperidone carries a well-known cardiac safety concern (QT prolongation risk) that would impose a significant risk burden for a rare disease repurposing hypothesis with no preliminary evidence.

**To proceed, the following would be needed:**

- **Preclinical mechanistic data**: In vitro or animal-model evidence that D2R antagonism meaningfully affects AVPR2 constitutive activity, AQP2 trafficking, or urine osmolality in NSIAD-relevant models — without this, the hypothesis cannot advance
- **MOA data retrieval**: Full DrugBank MOA and toxicity profile for domperidone (currently Data Gap)
- **Safety package review**: Package insert warnings and contraindications (particularly cardiac QT prolongation data) must be retrieved and evaluated before any human study design
- **TFDA/regulatory status clarification**: Domperidone is not marketed in Taiwan; any study initiation would require import or compassionate use regulatory pathway
- **NSIAD expert consultation**: Given the extreme rarity of NSIAD and its specific genetic etiology, a disease-expert review of plausibility should precede any resource commitment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

