---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Felbinac
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

# Felbinac: From Topical Musculoskeletal Pain to Brachyolmia-Amelogenesis Imperfecta Syndrome

## One-Sentence Summary

Felbinac is a biphenylacetic acid NSAID typically used as a topical formulation for musculoskeletal pain and inflammation (per the evidence pack's own mechanistic notes; no official original-indication or license record is available). The TxGNN model's top prediction is **Brachyolmia-Amelogenesis Imperfecta Syndrome**, but this is a rare skeletal/dental developmental disorder with **no clinical trials, no literature, and no plausible mechanistic link** to NSAID pharmacology — the evidence pack itself flags this as a likely graph-embedding false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no license or original-indication records; drug's rationale notes describe it as a topical NSAID for musculoskeletal pain) |
| Predicted New Indication | Brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the information present in the evidence pack, felbinac is described as a biphenylacetic acid-class NSAID that acts as a COX inhibitor, typically administered topically for musculoskeletal pain and inflammation.

Brachyolmia-amelogenesis imperfecta syndrome, however, is an extremely rare complex disorder combining skeletal dysplasia (short spine) with enamel formation defects, driven by structural-protein and mineralization-regulation gene pathways. There is no established pharmacological connection between NSAID/COX inhibition and this disease's pathology.

The evidence pack's own repurposing rationale for this candidate explicitly states that the mechanistic link is absent and characterizes the high TxGNN score as a typical case of embedding-based false positive for rare-disease nodes, rather than a genuine biological signal. This assessment should be taken at face value — the ranking score alone (rank 471 by TxGNN, 99.99% probability) does not compensate for the lack of mechanistic or empirical support.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for this indication, mechanism-of-action data for felbinac is unavailable, the drug is not marketed in Saudi Arabia (0 authorizations), and the evidence pack's own rationale identifies this top-ranked prediction as a likely knowledge-graph artifact with no biological plausibility.

**To proceed, the following is needed:**
- Felbinac mechanism-of-action data (DrugBank API query, currently blocking data gap)
- SFDA/TFDA package insert (warnings, contraindications, DDI) — currently blocking data gap
- Independent biological/genetic plausibility review for this candidate before any further investment
- Consider deprioritizing this rank-1 candidate in favor of the mechanistically more coherent, NSAID-class-relevant candidates in this evidence pack (e.g., spondyloarthropathy susceptibility, rheumatoid nodulosis, juvenile idiopathic arthritis — ranks 6, 7, 9, 10), which are flagged as "Research Question" rather than "Hold" and warrant lower-cost literature screening first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

