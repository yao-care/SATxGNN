---
layout: default
title: Piribedil
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 5
---

# Piribedil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Piribedil: From Parkinson's Disease to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Piribedil is a dopamine D2/D3 receptor agonist used internationally for Parkinson's disease and related motor disorders (per the drug's own mechanistic context in this evidence pack), though no confirmed local regulatory indication data is on file. The TxGNN model predicts a possible link to **retinal dystrophy with or without extraocular anomalies**, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the mechanistic link as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not locally registered) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap pending DrugBank API query). Based on contextual information present elsewhere in this evidence pack — specifically the rationale text attached to other candidate indications for this same drug — piribedil is understood to be a D2/D3 dopamine receptor agonist already approved in Europe and Asia for idiopathic Parkinson's disease. This is background context only, not a confirmed regulatory data point for this report.

For the top-ranked prediction here, retinal dystrophy with or without extraocular anomalies, the underlying pathology is photoreceptor/retinal pigment epithelium gene defects — a mechanism unrelated to systemic dopaminergic signaling. The evidence pack's own repurposing rationale explicitly notes that while dopaminergic amacrine cells exist in the retina and participate in light adaptation, there is no direct treatment-relevant mechanistic link to piribedil's systemic D2/D3 agonism, and classifies this as a low-relevance prediction with no supporting clinical or mechanistic literature.

Given the absence of any trials or publications and the model's own low-confidence rationale, this pairing should be treated as an unvalidated graph-model signal rather than a mechanistically grounded hypothesis. Notably, among the other four candidates in this pack, rank 5 (juvenile onset Parkinson disease 19A) shows a substantially stronger mechanistic rationale, since it shares the classic nigrostriatal dopamine-deficiency pathology that piribedil is already used to treat.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Piribedil is not marketed in this jurisdiction (0 authorizations on file); no product or dosage-form records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but is unsupported by any clinical trials, literature, or robust mechanistic reasoning — the evidence pack's own analysis rates the mechanistic link as low relevance (L5, S0 stage). In addition, a blocking safety data gap (missing TFDA/local package insert warnings and contraindications) prevents this candidate from entering initial safety screening (S1) regardless of predicted-indication strength.

**To proceed, the following is needed:**
- Local package insert / regulatory warnings and contraindications (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action data via DrugBank API query
- Confirmed original approved indication(s), since none are currently on file for this drug
- Consideration of re-prioritizing evaluation toward rank 5 (juvenile onset Parkinson disease 19A), which has a stronger mechanistic rationale given piribedil's established dopaminergic pharmacology, despite it too currently lacking clinical or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

