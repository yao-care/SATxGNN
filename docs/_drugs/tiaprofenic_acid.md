---
layout: default
title: Tiaprofenic Acid
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
---

# Tiaprofenic Acid
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

# Tiaprofenic Acid: From NSAID (Pain/Inflammation) to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Tiaprofenic acid is a propionic-acid-class NSAID; the evidence pack does not record its originally approved indication text (not marketed in Saudi Arabia, no license data on file). The TxGNN model's top prediction is **Brachydactyly-Syndactyly Syndrome**, but this is a pure embedding-similarity signal — **0 clinical trials** and **0 publications** support it, and the model's own rationale states there is no known mechanistic overlap between COX-1/2 inhibition and this congenital skeletal disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not marketed in Saudi Arabia) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.99% (rank 344 overall) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Other candidates in this evidence pack** (all rank L5 / Hold, 0 trials, 0 literature):

| Rank | Disease | TxGNN Score | Recommendation |
|------|---------|-------------|-----------------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.99% | Hold |
| 3 | Brachyolmia-amelogenesis imperfecta syndrome | 99.99% | Hold |
| 4 | Acromesomelic dysplasia, Hunter-Thompson type | 99.99% | Hold |
| 5 | Myosclerosis | 99.99% | Hold |
| 6 | Spondyloarthropathy, susceptibility to | 99.99% | Hold |
| 7 | Brachyolmia | 99.99% | Hold |
| 8 | Factor 5 excess with spontaneous thrombosis | 99.98% | Hold |
| 9 | Heparin cofactor 2 deficiency | 99.98% | Hold |
| 10 | Pseudoachondroplasia | 99.98% | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tiaprofenic acid (marked as a data gap in this evidence pack). Based on the drug's own repurposing-rationale text, tiaprofenic acid is understood to act through COX-1/2 inhibition, suppressing prostaglandin synthesis — the standard NSAID mechanism.

For the top-ranked prediction, Brachydactyly-Syndactyly Syndrome, the model's own rationale is explicit that there is **no known disease-mechanism overlap**: this is a congenital limb-patterning disorder driven by specific developmental gene mutations, unrelated to inflammatory or prostaglandin pathways. The same pattern repeats across most of the other nine candidates — congenital skeletal dysplasias, structural/mineralization gene defects, and coagulation-factor disorders — none of which share a plausible pharmacological link to NSAID activity. Two candidates (spondyloarthropathy susceptibility, myosclerosis) have a theoretically plausible symptomatic-relief rationale (anti-inflammatory effect on joint/muscle symptoms), and two others (Factor V excess, heparin cofactor II deficiency) surface only as a **safety signal** (antiplatelet/bleeding-risk interaction), not a therapeutic one.

In short, this candidate set is a case where TxGNN's embedding similarity score is uniformly very high (>99.9%) across ten disparate rare diseases, without corresponding mechanistic, clinical, or literature support for any of them — consistent with a model-artifact signal rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Tiaprofenic acid is currently not marketed in Saudi Arabia; no authorization records exist in this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package-insert warnings/contraindications data collection is flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety pre-screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications sit at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the top-ranked candidate's own mechanistic rationale explicitly finds no pathway overlap with the drug's NSAID mechanism. A blocking data gap (TFDA safety labeling) also prevents any formal safety pre-screening at this time.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA package insert warnings/contraindications) — currently blocking
- Resolve DG002 (confirmed MOA from DrugBank) to properly assess mechanistic plausibility
- If pursuing further, prioritize the two candidates with a coherent (if unproven) symptomatic rationale — spondyloarthropathy susceptibility and myosclerosis — over the purely embedding-driven skeletal-dysplasia candidates
- Independent literature/trial search beyond the current negative pubmed/clinicaltrials/ICTRP queries before any re-scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

