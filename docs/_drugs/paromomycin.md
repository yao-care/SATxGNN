---
layout: default
title: Paromomycin
parent: 僅模型預測 (L5)
nav_order: 477
evidence_level: L5
indication_count: 8
---

# Paromomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Paromomycin: From Intestinal Amebiasis to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Paromomycin is an aminoglycoside antibiotic used against intestinal amebiasis and other parasitic infections (e.g., leishmaniasis). The TxGNN model predicts potential efficacy for **Idiopathic Copper-Associated Cirrhosis**, but currently **no clinical trials and no literature** support this specific prediction, and the evidence pack's own mechanistic review flags the score as a likely knowledge-graph clustering artifact rather than genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intestinal amebiasis (antiparasitic aminoglycoside; not formally recorded as `original_indications` in this evidence pack) |
| Predicted New Indication | Idiopathic Copper-Associated Cirrhosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, paromomycin is an intestinal non-absorbable aminoglycoside that acts on protozoal/bacterial ribosomes, and its efficacy in intestinal amebiasis is well established.

However, there is no known mechanistic pathway connecting ribosome-targeting antimicrobial activity to copper metabolism or hepatic fibrosis processes relevant to idiopathic copper-associated cirrhosis. The evidence pack's own rationale is explicit on this point: the high TxGNN score likely reflects a clustering effect around "liver disease" nodes in the knowledge graph, not causal biological evidence.

For context, this same drug's evidence pack contains a lower-ranked candidate (peritonitis, rank 8) that is comparatively better supported — it is associated with published case reports and reviews on amoebic-related complications — though that literature is still largely indirect (mostly in vitro leishmaniasis drug-interaction studies rather than peritonitis-specific evidence).

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Paromomycin is currently **not marketed** in Saudi Arabia — no authorizations are on record (`total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (idiopathic copper-associated cirrhosis) has an L5 evidence level — model prediction only, with zero supporting clinical trials or literature — and the evidence pack's own analysis attributes the high score to a knowledge-graph artifact rather than a plausible pharmacological mechanism.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications, DDI) — currently a blocking data gap
- Confirmed mechanism of action documentation from DrugBank
- Any direct preclinical or clinical evidence linking paromomycin to copper metabolism or hepatic fibrosis pathways
- Consider re-evaluating the lower-score but literature-supported candidate (peritonitis, rank 8, L4, 20 publications) as a more grounded alternative repurposing hypothesis, noting most of that literature is indirect (leishmaniasis drug-interaction studies) rather than peritonitis-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

