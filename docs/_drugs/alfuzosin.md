---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist, globally established for the treatment of benign prostatic hyperplasia (BPH) and lower urinary tract symptoms (LUTS), though it has not received regulatory approval in Saudi Arabia.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital disorder characterised by dense, excessive hair growth across the entire body surface.
Currently, **no clinical trials** and **no publications** directly support this repurposing direction, placing this candidate at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia / Lower Urinary Tract Symptoms (global approval; not registered in Saudi Arabia) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist. Its established clinical role is to relax smooth muscle in the prostate and bladder neck, thereby relieving urinary obstruction in men with BPH. Detailed mechanism of action data was not retrievable from the current evidence pack, but alfuzosin's pharmacological class is universally recognised in clinical and regulatory literature.

Alpha-1 adrenergic receptors are expressed in hair follicle dermal papilla cells, and sympathetic nervous tone is known to influence the hair follicle growth cycle. On this basis, there is a superficial theoretical link between an alpha-1 blocker and hair follicle phenotypes. However, Ambras type hypertrichosis universalis congenita is caused by chromosomal rearrangements disrupting the TRPS1/EXT1 gene locus — a structural genetic defect. No adrenergic receptor antagonist can correct a chromosomal structural abnormality.

The most probable explanation for this high-scoring TxGNN prediction is a knowledge graph artefact: the model's KG contains "hair follicle phenotype" nodes shared between alfuzosin's known receptor targets and the Ambras syndrome phenotype, generating a high numerical score without reflecting a true pharmacological mechanism. This prediction should be read as a KG structural co-occurrence, not a genuine repurposing signal.

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
Ambras type hypertrichosis universalis congenita is a structural chromosomal/genetic disorder (TRPS1/EXT1 locus), and the alpha-1 adrenergic blockade mechanism of alfuzosin has no plausible pharmacological pathway to modify or reverse this defect. With zero supporting clinical trials, zero relevant publications, no Saudi Arabia market presence, and a mechanistic assessment that points to a KG artefact rather than a true drug–disease relationship, this indication does not warrant further investigation.

**To proceed, any future reconsideration would require:**
- Confirmed mechanism of action data (MOA) from DrugBank API
- Full safety profile (warnings, contraindications) extracted from the package insert
- At least one preclinical study demonstrating that alpha-1 receptor modulation influences the TRPS1/EXT1 pathway or the Ambras phenotype
- Consideration of whether alternate predicted indications with stronger mechanistic rationale — notably **allergic urticaria (rank 7)**, where adrenergic urticaria subtype has reported prazosin use, or **persistent fetal circulation syndrome (rank 8)**, where pulmonary vascular alpha-1 receptors provide a mechanistic basis — merit a separate evaluation ahead of this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

