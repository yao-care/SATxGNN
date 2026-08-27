---
layout: default
title: Trioxsalen
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Trioxsalen
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

# Trioxsalen: From Vitiligo (PUVA Photochemotherapy) to Vaginitis

## One-Sentence Summary

Trioxsalen is a psoralen photosensitizer traditionally used with UVA light (PUVA therapy) for vitiligo repigmentation and psoriasis; it has no marketing authorization in Saudi Arabia. The TxGNN model predicts it may be effective for **Vaginitis**, but this is a pure graph-embedding prediction with **0 clinical trials** and **0 publications** currently supporting it. Nine additional vulvovaginal-tract conditions (leukoplakia of vagina, vaginal discharge, bacterial vaginosis, etc.) scored similarly (~99.5–99.8%) and share the same evidence gap.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured regulatory data (drug not marketed); per the evidence pack's mechanistic notes, trioxsalen is a psoralen used with UVA (PUVA) for vitiligo repigmentation and psoriasis |
| Predicted New Indication | Vaginitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a Data Gap in this evidence pack. What is available comes from the repurposing rationale itself: trioxsalen is a photo-activated DNA cross-linking agent, used clinically as part of PUVA therapy to induce pigmentation changes and apoptosis of hyperproliferative cells in vitiligo and psoriasis.

Critically, the evidence pack's own mechanistic analysis states there is **no known link** between this mechanism and vaginitis pathophysiology — vaginitis is typically infectious or inflammatory in origin, whereas trioxsalen's activity is photochemical DNA cross-linking that requires UVA exposure at the treatment site. The rationale explicitly labels this connection "無" (none), noting the prediction is driven purely by TxGNN graph-embedding similarity rather than any pharmacological rationale.

The one biologically plausible cluster among the 10 predictions is proliferative/keratotic epithelial lesions (e.g., leukoplakia of vagina, vulvar inverted follicular keratosis, vulvar neoplasm), where PUVA's apoptosis-inducing effect on hyperproliferative tissue has a loose theoretical parallel — but even there, no local gynecological application precedent or supporting data exists, and systemic/local photosensitization carries its own safety concerns (e.g., photo-toxicity risk noted for atrophic and ulcerated mucosa in ranks 6 and 9).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Trioxsalen has no marketing authorizations in Saudi Arabia (0 licenses on record); no product/dosage-form data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this is offset by L5 evidence (no clinical trials, no literature, no established mechanistic link — the pack's own analysis states "無" mechanistic connection to vaginitis) and the drug's complete absence from the Saudi Arabian market. There is nothing here to act on beyond the model signal itself.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently blocking even a baseline safety review
- Confirmed original indication and MOA data (DrugBank query for MOA text)
- Preclinical or mechanistic studies exploring any plausible link between psoralen photochemistry and vulvovaginal conditions, particularly the proliferative-lesion subgroup (leukoplakia, inverted follicular keratosis, vulvar neoplasm) if this candidate is revisited
- If pursued, an assessment of route feasibility, since PUVA requires site-directed UVA exposure not compatible with standard vaginal/vulvar administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

