---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Aflibercept: From Retinal Vascular Disease to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF Trap fusion protein used to treat retinal vascular diseases such as neovascular age-related macular degeneration, diabetic macular edema, and retinal vein occlusion.
The TxGNN model predicts it may be effective for **Esotropia** (inward eye deviation / 內斜視),
with **no clinical trials** and **no published literature** currently supporting this direction — placing this prediction at **L5 (model prediction only)**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Retinal vascular disease (neovascular AMD, DME, RVO) — not marketed in Taiwan |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Aflibercept acts as a "VEGF Trap" — a recombinant fusion protein that binds VEGF-A, VEGF-B, and PlGF with high affinity, thereby suppressing pathological angiogenesis and vascular leakage. Its established clinical role is in retinal vascular conditions where aberrant VEGF signaling drives neovascularization. Detailed MOA data from DrugBank was not fully retrieved in this run, but the mechanism is well characterized in published literature.

The potential mechanistic link to esotropia is indirect and speculative. VEGF signaling participates in embryonic development of the oculomotor nuclei and vascularization of extraocular muscles. Furthermore, intravitreal anti-VEGF injections used in retinopathy of prematurity (ROP) have been associated with changes in strabismus incidence in follow-up studies — though whether this effect is protective or causative remains unresolved. A third, more tenuous pathway involves ciliary body vascular modulation secondarily affecting accommodation-related structures.

Despite these indirect connections, there is currently no established causal mechanism by which VEGF inhibition corrects ocular misalignment in esotropia. The high TxGNN score (0.994) most likely reflects non-specific proximity within the ophthalmology node cluster of the knowledge graph rather than a genuine pharmacological relationship. This prediction should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting the use of aflibercept in esotropia, and the mechanistic link is indirect at best. The TxGNN high score most likely reflects knowledge graph topology rather than true pharmacological relevance to ocular misalignment.

**To proceed, the following is needed:**
- Retrieve Taiwan package insert / TFDA label to establish a safety baseline (currently a Blocking data gap — DG001)
- Retrieve complete MOA data from DrugBank (currently a High-severity data gap — DG002)
- Conduct a targeted literature review on anti-VEGF exposure and strabismus outcomes in ROP patient cohorts as the closest available proxy evidence
- Obtain preclinical evidence demonstrating a VEGF-dependent pathway in esotropia pathogenesis before further investment
- Obtain clinical expert opinion from a strabismus/pediatric ophthalmology specialist to assess biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

