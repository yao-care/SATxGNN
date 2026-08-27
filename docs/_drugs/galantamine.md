---
layout: default
title: Galantamine
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 9
---

# Galantamine
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

# Galantamine: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Galantamine is an acetylcholinesterase inhibitor (AChEI) with nicotinic receptor allosteric-modulator activity, established in the literature for Alzheimer's disease dementia. The TxGNN model's top-ranked prediction is **Psychogenic Movement Disorders**, but this specific candidate currently has **0 clinical trials** and **0 publications** supporting it — it is a pure model score with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (mild-to-moderate dementia) — inferred from background literature within this evidence pack; no formal Saudi regulatory record exists |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed drug-specific mechanism of action data is not available (flagged as a High-severity data gap). Based on background information surfaced within the supporting literature for related candidates in this evidence pack, galantamine is a cholinesterase inhibitor that also acts as a positive allosteric modulator of nicotinic acetylcholine receptors, and is used clinically for Alzheimer's disease and related dementias (e.g. PMID 12611743, PMID 22070157, PMID 14564129). Its efficacy in dementia is well established; mechanistically, boosting central cholinergic tone is the basis for exploring effects on movement and neuropsychiatric symptoms.

For the top-ranked candidate itself — Psychogenic Movement Disorders — no clinical trial or literature evidence exists in this data pull. The repurposing rationale for this candidate is explicitly limited to the TxGNN score (0.9990) with no mechanistic argument available for direct evaluation.

Worth noting for context: within the same prediction set, two lower-ranked but evidence-backed candidates point to a more coherent mechanistic story — **Extrapyramidal and Movement Disease** (rank 4) and **Lingual-Facial-Buccal Dyskinesia / tardive dyskinesia** (rank 7) both reach L3 evidence (2 clinical trials plus Cochrane systematic reviews and an RCT, PMID 17388711). The proposed mechanism there — cholinergic compensation for antipsychotic-induced dopamine–acetylcholine imbalance in the basal ganglia — is biologically plausible, though a 2025 systematic review (PMID 40224553) also reports AChEIs can *induce* movement disorders, making this a bidirectional safety signal rather than a clean efficacy signal. These candidates would be a more productive starting point than the top-ranked, evidence-free prediction if this drug is pursued for the movement-disorder space.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Galantamine is not marketed in Saudi Arabia (0 authorizations on file); no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA package insert warnings and contraindications are listed as a Blocking data gap (DG001) — this must be resolved before any formal safety pre-screening (S1) can proceed for this drug, regardless of indication.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Psychogenic Movement Disorders) has no clinical trial or literature support — it is a bare model score at evidence level L5. Combined with the drug's blocking safety data gap (no TFDA/SFDA label data) and zero market presence in Saudi Arabia, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed drug-specific mechanism of action data (DG002)
- If continuing to explore galantamine for the movement-disorder space, re-scope evaluation toward the higher-evidence candidates in this pack (extrapyramidal/movement disease and tardive dyskinesia, both L3/S1), rather than the unsupported top TxGNN rank
- Independent confirmation of the drug's approved indication and regulatory history, since no license or original-indication data was returned in this evidence pull
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

