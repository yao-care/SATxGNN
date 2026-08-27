---
layout: default
title: Procyclidine
parent: 僅模型預測 (L5)
nav_order: 521
evidence_level: L5
indication_count: 10
---

# Procyclidine
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

# Procyclidine: From Parkinsonism (Anticholinergic Therapy) to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Procyclidine is a classic anticholinergic agent, referenced in this evidence pack as historically used to manage tremor and rigidity in Parkinsonism and drug-induced extrapyramidal symptoms. The TxGNN model's top prediction is **Rasmussen Subacute Encephalitis**, but this pairing is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-score prediction with no known mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Saudi Arabia licensing data (drug not marketed); referenced elsewhere in the evidence pack as an anticholinergic antiparkinsonian agent |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available for procyclidine in this evidence pack (flagged as a High-severity data gap requiring a DrugBank API lookup). Based on information embedded elsewhere in the evidence pack's own repurposing rationale, procyclidine is classified as a classic anticholinergic antiparkinsonian agent, historically used to relieve tremor and rigidity in Parkinsonism and drug-induced extrapyramidal symptoms.

Rasmussen subacute encephalitis, in contrast, is a chronic autoimmune/inflammatory encephalitis with no established pharmacological relationship to anticholinergic activity. The evidence pack's own mechanistic rationale for this pairing explicitly states there is no known mechanistic link — the prediction rests solely on the TxGNN model's graph-based score (rank 4801 among all model outputs), with no supporting clinical trials or literature identified.

By contrast, several lower-ranked candidates in this same prediction set — PLA2G6-associated neurodegeneration (rank 3), progressive supranuclear palsy-corticobasal syndrome (rank 7), and juvenile parkinsonism (rank 8) — carry a more plausible pharmacological rationale, since they involve parkinsonism-plus or dystonic phenotypes where anticholinergics are sometimes used symptomatically. These are staged as "Research Question" (L4/S1) rather than "Hold," and may warrant closer follow-up than the top-ranked Rasmussen encephalitis prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Procyclidine is currently **not marketed** in Saudi Arabia — no authorization records are on file (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen Subacute Encephalitis) is supported only by an L5 TxGNN model score, with zero clinical trials, zero publications, and no known mechanistic relationship between procyclidine's anticholinergic action and the disease's autoimmune/inflammatory pathology. This does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- TFDA/Saudi package insert warnings, contraindications, and safety data (currently Blocking data gap, DG001)
- Procyclidine's mechanism of action via DrugBank API (currently High-severity data gap, DG002)
- Preclinical or mechanistic studies specifically linking anticholinergic activity to Rasmussen encephalitis, if this indication is to be pursued further
- Consider redirecting research attention to the mechanistically plausible, higher-evidence-tier candidates in this set (PLA2G6-associated neurodegeneration, PSP-CBS, juvenile parkinsonism), which are already staged as Research Question rather than Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

