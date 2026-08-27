---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Acute Promyelocytic Leukemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (all-trans retinoic acid) is a retinoid classically used systemically as differentiation therapy for acute promyelocytic leukemia and topically for acne vulgaris. The TxGNN model's top-ranked prediction for this drug is **Rheumatoid Nodulosis**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-based inference. Across all 10 TxGNN-ranked candidates in this evidence pack, only **osteoarthritis** (rank 7) has a meaningful literature base (20 papers), and even that evidence is mechanistically contradictory.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Promyelocytic Leukemia (systemic) / Acne Vulgaris (topical) — based on general pharmacological knowledge; not confirmed by this evidence pack (no `original_indications` or Saudi license text available) |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on general pharmacological knowledge, tretinoin is a retinoid that acts as an agonist of retinoic acid receptors (RARs), and its efficacy as a differentiating agent in acute promyelocytic leukemia — as well as its keratinocyte-modulating effect in acne — is well established.

For the top-ranked prediction, rheumatoid nodulosis, the stated rationale is that retinoic acid signaling may theoretically influence immune cell differentiation and inflammatory regulation. However, this link is explicitly described in the evidence pack as a graph-topology inference with **no supporting experimental or clinical data** — the same caveat applies to ranks 2–6, 8, and 9 (all juvenile arthritis/spondyloarthropathy/skeletal dysplasia predictions), which share zero trials and zero literature.

The one candidate with a substantive literature base is osteoarthritis (rank 7), but the underlying biology is not one-directional: some studies (e.g., ALDH1A2 genetic association data) suggest endogenous retinoic acid is chondroprotective, while others directly model "retinoic acid-induced osteoarthritis," implicating RA-driven upregulation of cartilage-degrading enzymes (ADAMTS-4/5, MMPs). This contradiction means the existing evidence describes a **safety signal of uncertain direction** rather than a validated therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

### Other Predicted Indications (for context — this is a multi-candidate evidence pack)

| Rank | Disease | TxGNN Score | Evidence Level | Evidence Summary |
|------|---------|-------------|-----------------|-------------------|
| 1 | Rheumatoid Nodulosis | 99.84% | L5 | No trials, no literature |
| 2 | RF-positive Polyarticular JIA | 99.82% | L5 | No trials, no literature |
| 3 | Juvenile Idiopathic Arthritis | 99.80% | L5 | No trials, no literature |
| 4 | Juvenile Chronic Polyarthritis | 99.78% | L5 | No trials, no literature |
| 5 | Spondyloarthropathy, susceptibility to | 99.71% | L5 | No trials, no literature |
| 6 | Juvenile Arthritis (LACC1 defect) | 99.55% | L5 | No trials, no literature |
| 7 | Osteoarthritis | 99.44% | L4 | 20 publications; mechanistically contradictory (protective vs. pathogenic RA signaling) |
| 8 | Pseudoachondroplasia | 99.35% | L5 | No trials, no literature |
| 9 | Acromesomelic Dysplasia, Hunter-Thompson type | 99.30% | L5 | No trials, no literature |
| 10 | Quinquaud's Folliculitis Decalvans | 99.30% | L4 | 1 case report (disease description only, no tretinoin treatment data) |

## Saudi Arabia Market Information

Tretinoin currently holds no market authorization in Saudi Arabia (0 licenses on file; market status: Not Marketed).

## Safety Considerations

TFDA/SFDA package insert warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — DDI query returned "not found," and this gap is flagged as **Blocking** (prevents entry into S1 safety evaluation). Please refer to the official package insert for safety information once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid nodulosis) has no clinical, preclinical, or literature support beyond the TxGNN score itself, and every other high-ranking candidate except osteoarthritis shares that same absence of evidence. Osteoarthritis has literature volume but the mechanistic direction is unresolved (retinoic acid appears both protective and pathogenic depending on the study), and a blocking safety data gap prevents any S1-level review regardless of indication.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications, DDI) — currently blocking
- Confirmed mechanism of action data from DrugBank
- If pursuing the osteoarthritis lead: resolution of the conflicting retinoic acid signaling data (protective vs. cartilage-degrading) through targeted preclinical work before any clinical hypothesis is formed
- For the remaining L5 candidates: at minimum, preclinical or case-level evidence before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

