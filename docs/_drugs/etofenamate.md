---
layout: default
title: Etofenamate
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Etofenamate
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

# Etofenamate: From Topical Anti-Inflammatory Use to Spondyloarthropathy, Susceptibility To

## One-Sentence Summary

Etofenamate is a fenamate-class NSAID historically marketed as a topical gel (e.g., Rheumon) for musculoskeletal and rheumatic pain, though this pack contains no confirmed original-indication record. TxGNN's top-ranked prediction, **Spondyloarthropathy, susceptibility to**, scores **99.9997%** but is a genetic-risk label rather than a treatable disease, and is supported by **zero clinical trials and zero publications** — this looks like a knowledge-graph artifact, not a real signal. A secondary candidate, **ankylosing spondylitis** (rank 2), is mechanistically far more plausible and has one relevant PK study, but still no efficacy evidence specific to this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed for Saudi Arabia (drug not marketed there); literature references topical use (Rheumon gel) for musculoskeletal/soft-tissue pain |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.9997% (global rank 28) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for etofenamate in this pack. Based on known information, etofenamate belongs to the fenamate class of NSAIDs (COX-1/COX-2 inhibition), typically formulated as a topical gel; a cited study (PMID 11455681) describes it as "Rheumon gel" used for low back pain and knee synovitis, indicating an anti-inflammatory/analgesic profile applied to musculoskeletal soft-tissue and joint conditions.

The top-ranked predicted indication, "spondyloarthropathy, susceptibility to," is not a disease state — it is a genetic-risk classification. A drug cannot treat susceptibility itself, so this prediction has no direct clinical operational meaning. The most likely explanation is that the TxGNN knowledge graph conflated this susceptibility node with related inflammatory arthropathy nodes, producing a high but clinically non-actionable score.

By contrast, rank 2 — ankylosing spondylitis, an actual inflammatory spondyloarthropathy — is mechanistically coherent: NSAIDs are established first-line symptomatic therapy for AS as a class effect. The associated literature (PMID 11455681) shows etofenamate reaches detectable concentrations in both serum and synovial fluid after iontophoretic application, supporting adequate joint-tissue penetration. However, this is a pharmacokinetic study, not an efficacy trial, so it cannot substantiate therapeutic benefit in AS.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for "Spondyloarthropathy, susceptibility to."

*(For context only — not applicable to the rank-1 prediction above: rank 2, ankylosing spondylitis, is supported by one PK study, [PMID 11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/), 2001, Arzneimittel-Forschung, showing etofenamate is detectable in serum and synovial fluid after iontophoresis — not an efficacy study.)*

---

## Saudi Arabia Market Information

Etofenamate is not currently marketed in Saudi Arabia; no product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction targets a genetic susceptibility classification rather than a treatable disease, has zero supporting trials or literature, and lacks a coherent mechanistic pathway — evidence level L5, model prediction only. This candidate should not advance.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or another authoritative source
- TFDA/manufacturer package insert for safety, warnings, and contraindications
- If pursuing the drug class more broadly, drug-specific efficacy evidence in an actual inflammatory spondyloarthropathy (e.g., ankylosing spondylitis) rather than the susceptibility-label prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

