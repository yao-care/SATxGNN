---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen: From Pain and Inflammation (NSAID) to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a propionic-acid-derivative NSAID; no product-specific original indication text is available in this evidence pack, and it is not currently marketed in Saudi Arabia.
The TxGNN model's top prediction is **Brachydactyly-Syndactyly Syndrome**, a rare genetic limb-development disorder,
but this is supported by **0 clinical trials** and **0 publications** — the score is a knowledge-graph output only, with no confirmatory evidence of any kind.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license records; naproxen is a known NSAID used for pain/inflammation/arthritis) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known information, naproxen is a propionic acid derivative NSAID that inhibits COX-1/COX-2 to block prostaglandin synthesis, and its efficacy in pain and inflammatory conditions is well established.

However, the evidence pack's own mechanistic assessment for this prediction is explicitly negative: brachydactyly-syndactyly syndrome is a rare skeletal/limb developmental disorder driven by genetic defects, with **no known relationship** to naproxen's anti-inflammatory/prostaglandin-inhibition pathway. The high TxGNN score is noted to likely reflect topological similarity between skeletal/limb-related nodes in the knowledge graph rather than genuine pharmacological plausibility, and no supporting animal or in vitro studies exist.

The same pattern holds across all four ranked predictions in this evidence pack (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome) — all are rare genetic developmental syndromes, all lack a credible mechanistic link to NSAID pharmacology, and all are scored L5/S0/Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trials, no literature, no confirmed mechanism of action, and no market presence in Saudi Arabia. The predicted indication itself is explicitly flagged in the evidence pack as mechanistically implausible (likely a graph-topology artifact rather than a pharmacologically grounded signal), placing it firmly at evidence stage S0/L5.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data (DG002)
- Preclinical or mechanistic studies connecting NSAID/prostaglandin pathways to the relevant skeletal-dysplasia gene targets
- Any real-world or case-level evidence for brachydactyly-syndactyly syndrome (or the other three ranked candidates) before this leaves model-prediction-only status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

