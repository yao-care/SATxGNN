---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid (ICS) developed for asthma and allergic rhinitis, acting via glucocorticoid receptor activation to suppress airway inflammation.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with a prediction confidence of **99.96%**; however, **no clinical trials or supporting literature** currently exist to validate this specific repurposing direction, and a fundamental route-of-administration barrier remains unresolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / Allergic Rhinitis (inhaled corticosteroid; not registered in Taiwan) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, ciclesonide is a prodrug ICS that is converted to its active metabolite **des-ciclesonide** in the airways. Des-ciclesonide binds glucocorticoid receptors (GR), suppresses NF-κB signalling, and reduces the release of pro-inflammatory cytokines — including IL-4, IL-5, and IL-13 — that are the central mediators of Th2-driven inflammation.

Atopic eczema shares this same Th2-dominant immunological architecture with asthma: IgE sensitization, eosinophilic infiltration, and cytokine dysregulation overlap substantially between the two conditions. Topical corticosteroids are, in fact, the established first-line anti-inflammatory treatment for atopic dermatitis. This mechanistic congruence logically explains why TxGNN scored this indication highly at rank 1.

The critical obstacle, however, is the **route of administration**. Ciclesonide is engineered as an inhaled aerosol designed to deposit in the airways. Treating atopic eczema requires topical cutaneous delivery — a formulation that does not currently exist for ciclesonide. Without a dedicated topical preparation, the active metabolite cannot reach the target tissue in meaningful concentrations. This is a formulation development challenge rather than a question of mechanistic fit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for atopic eczema.

---

## Taiwan Market Information

Ciclesonide is currently **not registered** in Taiwan. No marketing authorizations have been issued by the TFDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN's prediction is immunologically coherent — corticosteroids are the backbone of atopic eczema management — but ciclesonide's inhaled-only formulation presents a fundamental route-of-administration barrier, and no clinical or literature evidence exists to support this specific repurposing direction at this time.

**To proceed, the following is needed:**
- MOA data from DrugBank to formally document the mechanistic link between des-ciclesonide and Th2 cytokine suppression in skin
- Feasibility study for topical ciclesonide formulation (skin penetration, stability, release kinetics)
- Preclinical efficacy data for des-ciclesonide in validated atopic dermatitis models (e.g., MC903 or DNCB murine models)
- Complete safety package insert retrieval (TFDA/EMA/FDA labels) before any clinical assessment can proceed
- Clarification of whether ranks 1 and 3 (atopic eczema / dermatitis atopic) represent duplicate ICD ontology entries; if so, consolidate confidence estimates before advancing either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

