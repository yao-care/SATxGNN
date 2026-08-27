---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 6
---

# Rasagiline
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

# Rasagiline: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

> Rasagiline is an irreversible MAO-B inhibitor established for Parkinson's disease.
> The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests solely on the model's score (**99.71%**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (inferred from drug class/MOA referenced in the evidence pack's own rationale text; not present in structured `original_indications` or Saudi licensing data) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (`original_moa` is flagged as a data gap, DG002). Based on information embedded in the model's own rationale text, rasagiline is an irreversible monoamine oxidase type B (MAO-B) inhibitor, established for Parkinson's disease, where it reduces dopamine breakdown to improve motor symptoms.

PLA2G6-associated neurodegeneration (PLAN) is a heterogeneous disease group. One adult-onset subtype (PARK14, dystonia-parkinsonism) overlaps clinically with Parkinson's disease, so increased synaptic dopamine via MAO-B inhibition could theoretically offer partial motor benefit. However, most PLAN cases are infantile-onset or atypical neuroaxonal dystrophy phenotypes with a weak connection to the dopamine pathway, and there is no clinical or literature evidence currently supporting this indication.

Notably, of the six TxGNN predictions returned in this batch, only two — this one and rank 4 ("paralysis agitans, juvenile, of Hunt," essentially early-onset Parkinsonism) — have a plausible mechanistic link to the dopamine/MAO-B pathway. The other four (Rasmussen encephalitis, myelitis, transaldolase deficiency, polymicrogyria syndrome) have no known biological connection to rasagiline's mechanism, which suggests the model's ranking here reflects graph topology similarity rather than validated pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Rasagiline is not currently marketed in Saudi Arabia (市場狀態: 未上市); there are no authorization records in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/SFDA package insert warnings and contraindications are marked as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's topological score (L5) with zero clinical trials and zero literature. The drug is not marketed in Saudi Arabia, and package-insert safety data is a Blocking gap that prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Preclinical or case-level evidence linking MAO-B inhibition to the PARK14 subtype of PLA2G6-associated neurodegeneration specifically (rather than PLAN broadly)
- Assessment of Saudi Arabia regulatory pathway, given the drug currently has no market presence there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

