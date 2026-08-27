---
layout: default
title: Sulindac
parent: 僅模型預測 (L5)
nav_order: 590
evidence_level: L5
indication_count: 10
---

# Sulindac
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

Using the evidence pack as given — no skill needed here, this is a direct report-writing task with an explicit template supplied in the prompt.

Note: the evidence pack's regulatory data is under `taiwan_regulatory` (candidate_id `TW-DB00605...`), not Saudi Arabia — I've relabeled that section "Taiwan" to match the actual source field rather than copy the template's placeholder label.

---

# Sulindac: From an Undocumented Original Indication to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Sulindac's original approved indication and mechanism of action are not available in this data pull (both flagged as data gaps). The TxGNN model predicts a possible association with **acromesomelic dysplasia, Hunter-Thompson type**, a rare GDF5-related skeletal dysplasia, but this is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-similarity signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — sulindac holds no Taiwan marketing licenses, so no approved indication text exists in this record |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sulindac is not available in this evidence pack, and no original indication text was retrieved (the drug has no Taiwan market authorizations). Without MOA or original-indication data, there is no basis to construct a mechanistic bridge to acromesomelic dysplasia, Hunter-Thompson type — a rare, genetically defined skeletal dysplasia associated with the GDF5 gene.

The evidence pack's own rationale for this candidate states plainly that the link is "a pure TxGNN embedding similarity score, with no supporting literature or trials." Targeted searches against ClinicalTrials.gov, ICTRP, and PubMed for sulindac + this disease term all returned zero results (query log IDs 5–7). This is the weakest tier of repurposing evidence: a graph-embedding similarity score with no independent corroboration.

This pattern repeats across all 10 predicted indications in this pack (see below) — each is an ultra-rare disease with a high TxGNN score but zero trials and zero literature. Two candidates (WHIM syndrome, rheumatoid vasculitis) at least have a plausible generic rationale (NSAID-class anti-inflammatory activity), but even these remain unconfirmed by any dataset in this pull.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications (Rank 2–10)

All ranked candidates share the same evidence profile as the top prediction — high TxGNN score, zero trials, zero literature, L5/Hold — and are listed here for completeness:

| Rank | Disease | TxGNN Score | Notes |
|------|---------|------|-------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.90% | No mechanistic hypothesis available |
| 3 | Brachyolmia | 99.90% | No mechanistic hypothesis available |
| 4 | Myosclerosis | 99.89% | No mechanistic hypothesis available |
| 5 | Pseudoachondroplasia | 99.85% | COMP-gene chondrodysplasia; no supporting data |
| 6 | Brachydactyly-syndactyly syndrome | 99.82% | No mechanistic hypothesis available |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.81% | No mechanistic hypothesis available |
| 8 | WHIM syndrome | 99.74% | Generic NSAID anti-inflammatory rationale only |
| 9 | Rheumatoid vasculitis | 99.63% | Generic NSAID anti-inflammatory rationale only |
| 10 | Hypermobility of coccyx | 99.56% | Structural/mechanical condition; no pharmacologic rationale |

---

## Taiwan Market Information

Sulindac currently holds **no marketing authorization in Taiwan** (0 licenses; market status: Not marketed). No product name, dosage form, or approved-indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all unavailable in this pull; TFDA package insert retrieval is flagged as a **blocking** data gap — DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this pack sits at Evidence Level L5 (model prediction only) with zero clinical trials and zero literature support, and sulindac has no MOA data, no documented original indication, and no Taiwan market presence to anchor a mechanistic argument. There is nothing here to progress on.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or another primary source (DG002)
- Original approved indication(s) for sulindac, to establish a baseline for indication-similarity reasoning
- At minimum, preclinical/mechanistic literature connecting sulindac's pharmacology to any of the predicted rare-disease candidates before advancing past L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

