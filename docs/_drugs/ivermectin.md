---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 9
---

# Ivermectin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

> Ivermectin is an antiparasitic agent (avermectin class); no approved-indication data is on file in this market and detailed mechanism-of-action data has not yet been retrieved.
> The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, but this is currently supported by **0 clinical trials** and **0 publications**,
> and the model's own rationale states there is no known antifungal mechanism for ivermectin — this is a model-only prediction with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved-indication text on file (drug not marketed here; MOA is a data gap) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ivermectin is currently a data gap (DG002, High severity). Based on general pharmacological knowledge, ivermectin is an avermectin-class antiparasitic that acts on invertebrate glutamate-gated chloride channels, causing paralysis and death of parasites (nematodes, arthropods). It has no established antifungal mechanism.

Critically, the evidence pack's own rationale for this prediction states there is **no plausible biological link** between ivermectin and vulvovaginal candidiasis: candidiasis is a fungal infection, and ivermectin has no known antimycotic activity. The same caveat applies to all 9 of the drug's top-ranked predicted indications in this pack — they cluster around Candida species and vaginal/vulvar conditions, and each carries an identical "no known mechanism" rationale.

The two literature items found for other (lower-ranked) predictions in this pack — a case report on disseminated strongyloidiasis and a case report on ivermectin treating crusted scabies in immunocompromised children — do not concern Candida infections at all. They most likely surfaced through knowledge-graph co-occurrence (immunocompromised-host opportunistic infections) rather than a genuine antifungal signal. This pattern suggests the high raw TxGNN score reflects a graph-topology artifact rather than pharmacological plausibility, and should be weighted accordingly.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

*(Note: literature retrieved for other, lower-ranked predicted indications for this drug — e.g., a strongyloidiasis case report and a crusted-scabies case report — do not pertain to candidiasis and are not counted as supporting evidence here.)*

## Saudi Arabia Market Information

Currently not marketed; no product authorizations on file (total_licenses = 0).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable — DG001, Blocking severity, requires SFDA package-insert retrieval before any S1 safety review can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN score, this prediction has zero clinical trials, zero directly relevant literature, and no known antifungal mechanism — the model's own rationale explicitly flags the biological link as implausible. Evidence level is L5 (model prediction only), and this pattern is shared across all 9 top-ranked predictions for this drug in this pack, suggesting a systematic knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- SFDA package insert (warnings/contraindications) — currently Blocking (DG001)
- DrugBank mechanism-of-action data (DG002)
- In vitro or preclinical evidence of anti-*Candida* activity for ivermectin
- Independent pharmacology/mycology expert review before any further evidence-collection resources are allocated to this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

