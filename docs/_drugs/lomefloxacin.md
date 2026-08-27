---
layout: default
title: Lomefloxacin
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Lomefloxacin
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

# Lomefloxacin: From Bacterial Infections (Fluoroquinolone Antibiotic) to Laryngotracheitis

## One-Sentence Summary

Lomefloxacin (DrugBank DB00978) is a fluoroquinolone-class antibacterial agent; the evidence pack does not specify its originally approved indication.
The TxGNN model predicts it may be effective for **Laryngotracheitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug class noted as fluoroquinolone antibacterial in TxGNN rationale text) |
| Predicted New Indication | Laryngotracheitis |
| TxGNN Prediction Score | 99.61% (overall model rank #6552) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on the information present, Lomefloxacin is a fluoroquinolone antibacterial that acts by inhibiting bacterial DNA gyrase and topoisomerase IV.

Laryngotracheitis, however, is predominantly a viral condition — most notably croup in pediatric patients — rather than a bacterial one. There is no tissue- or receptor-specific rationale linking fluoroquinolone pharmacology to this disease; a bacterial antibiotic could theoretically have a role only in the uncommon bacterial (e.g., bacterial tracheitis) subset of cases, which is not what this prediction addresses.

This prediction rank is derived purely from TxGNN embedding similarity (score 99.61%), with no corroborating clinical trial, literature, or mechanistic evidence. Notably, the remaining 9 of the top 10 TxGNN predictions for this drug are cardiac/structural conditions (e.g., heart valve disease, heart conduction disease, heart aneurysm) where the rationale text itself flags that fluoroquinolones carry *known risk signals* in the opposite direction — QT prolongation, aortic aneurysm/dissection, and tendon/connective tissue rupture — rather than any therapeutic mechanism. This pattern suggests the model's embedding space is picking up disease-relatedness signals that do not translate into a plausible repurposing rationale for this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Lomefloxacin is not marketed in Saudi Arabia — no product authorizations are on record (0 total licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence supports laryngotracheitis (or any of the other top-10 predicted indications) for Lomefloxacin, and the mechanistic rationale is weak-to-contradictory — several co-ranked predictions align with known fluoroquinolone *risk* signals rather than therapeutic benefit. The drug is also unmarketed in Saudi Arabia with a blocking data gap on regulatory safety labeling.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Prospective preclinical or clinical evidence specifically evaluating Lomefloxacin in laryngotracheitis (particularly bacterial tracheitis subtype) before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

