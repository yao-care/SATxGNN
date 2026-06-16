---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor globally approved for benign prostatic hyperplasia (BPH) and androgenetic alopecia, but it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital generalised hair-overgrowth syndrome.
Currently **no clinical trials** and **no publications** specifically support this repurposing direction, placing the evidence at the lowest possible grade (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BPH and androgenetic alopecia (global approvals; no Saudi Arabia registration) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dutasteride inhibits both type 1 and type 2 isoforms of 5α-reductase, blocking the conversion of testosterone to dihydrotestosterone (DHT). By reducing systemic and local DHT levels, it suppresses androgen-driven hair follicle miniaturisation — which underpins its established use in androgenetic alopecia and BPH. Detailed mechanism of action data was not retrievable from the current data sources; the above summary is based on published pharmacology.

Ambras syndrome arises from chromosomal rearrangements at 8q22–24 that disrupt the TRPS1/EXT1 genomic region. The resulting generalised hypertrichosis is driven by dysregulation of TGF-β/BMP developmental signalling pathways that govern hair follicle morphogenesis in early embryonic life — a pathway entirely distinct from the androgen (DHT/5α-R) axis. There is no established mechanistic node at which dutasteride could intervene in Ambras syndrome pathobiology.

The exceptionally high TxGNN score (99.998%) most likely reflects a **knowledge graph neighbourhood artifact**: Ambras syndrome, other hypertrichoses, and androgenetic alopecia all share adjacency in the "hair follicle disorder" node cluster of the biomedical knowledge graph, making dutasteride appear relevant by graph proximity rather than genuine shared biology. This pattern is well recognised in graph-based repurposing models and should not be interpreted as evidence of therapeutic efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dutasteride in Ambras Type Hypertrichosis Universalis Congenita.

---

## Literature Evidence

Currently no related literature available for Dutasteride in Ambras Type Hypertrichosis Universalis Congenita.

---

## Saudi Arabia Market Information

Dutasteride has no approved products registered in Saudi Arabia. No authorisation records are available in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns dutasteride a near-perfect score for Ambras Type Hypertrichosis Universalis Congenita, all 10 predicted indications across this evaluation sit at Evidence Level L5 (model prediction only, no clinical data). The mechanistic connection between dutasteride's DHT-suppressing action and the TGF-β/BMP-driven pathology of Ambras syndrome is absent; the high model score is attributable to knowledge graph proximity among hair follicle diseases, not plausible biology.

**To proceed, the following is needed:**

- Retrieve formal MOA documentation from DrugBank (currently unavailable)
- Investigate whether 5α-reductase expression is relevant in the TRPS1/EXT1 regulatory network or its downstream TGF-β/BMP signalling cascade
- Commission preclinical studies (e.g., hair follicle cell models or Ambras mouse models) to test any androgenic contribution to phenotype severity
- Separately review indication **Rank 8 (Diffuse Alopecia Areata / AGA overlap)**, which carries a "Research Question" recommendation and has at least one supporting AGA narrative review (PMID 41714473) — this is a more mechanistically defensible candidate for further exploration
- Confirm Saudi Arabia registration pathway requirements before any clinical development planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

