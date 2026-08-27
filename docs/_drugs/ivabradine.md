---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine: From Sinoatrial Rate Control to Hypertrichosis (Disease)

## One-Sentence Summary

Ivabradine (DrugBank DB09083) is a selective If (HCN-channel) inhibitor acting on the sinoatrial node, used clinically for cardiac rate control. The TxGNN model's top prediction proposes potential relevance to **Hypertrichosis (disease)**, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review finds no known biological link between HCN-channel inhibition and hair follicle growth regulation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indications or licenses are recorded in the evidence pack; known mechanism (see below) is sinoatrial rate control |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Saudi Arabia Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for ivabradine is not available in the evidence pack (marked as a High-severity data gap). Based on the mechanistic notes attached to each predicted indication, ivabradine is described as a selective inhibitor of the cardiac If current (HCN channel), with its pharmacology confined to sinoatrial node rate control.

The evidence pack's own repurposing rationale explicitly states that this mechanism has **no known intersection** with hair-follicle growth regulation pathways (e.g., androgen signaling, WNT/Hedgehog). No biological hypothesis is offered to explain the high TxGNN similarity score, and no clinical, preclinical, or case-level literature currently exists linking ivabradine to hypertrichosis. This prediction should therefore be treated as a graph-embedding similarity signal rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Ivabradine is not marketed and has no recorded authorizations (0 licenses) in the current dataset; no product/dosage-form information is available.

---

## Other TxGNN Predictions for Ivabradine (Lower Priority)

The candidate pack contains five additional TxGNN-ranked predictions beyond the top hit. All carry L5 evidence and a Hold recommendation, and the mechanistic review found no plausible biological link for any of them:

| Rank | Predicted Indication | TxGNN Score | Evidence | Note |
|------|----------------------|-------------|----------|------|
| 2 | Ambras type hypertrichosis universalis congenita | 99.72% | None | Rare genetic syndrome (8q22 locus); no mechanistic overlap with HCN inhibition |
| 3 | Malformation syndrome with odontal/periodontal component | 99.72% | 20 publications (periodontology, unrelated to ivabradine) | Literature hits are keyword co-occurrence artifacts, not drug-specific evidence |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.70% | None | Neurodevelopmental disorder (e.g., ZIC1/ZIC4); no known mechanistic link |
| 5 | Isolated genetic hair shaft abnormality | 99.69% | None | Related to keratin genes (KRT, TCHH); no known mechanistic link |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 99.08% | None | AVPR2 gain-of-function disorder; no overlap with sinoatrial HCN pathway |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications for ivabradine are L5 (model prediction only), with no supporting clinical trials and either no literature or literature that is unrelated on closer review. The evidence pack's own mechanistic analysis finds no biological rationale connecting ivabradine's known HCN-channel/sinoatrial mechanism to any of the predicted diseases, and core regulatory/safety data (TFDA labeling, MOA, contraindications, DDI) are marked as gaps.

**To proceed, the following is needed:**
- Confirmed original indication and full MOA documentation (currently missing)
- TFDA package insert data (warnings, contraindications) — flagged as Blocking in the evidence pack
- A testable mechanistic hypothesis linking HCN-channel inhibition to hair-follicle biology, ideally supported by preclinical data
- Case reports, pharmacovigilance signals, or exploratory studies specifically evaluating ivabradine in hypertrichosis before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

