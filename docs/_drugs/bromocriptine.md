---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Parkinson's Disease / Hyperprolactinemia to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is a dopamine D2/D3 receptor agonist with established clinical use in Parkinson's disease, hyperprolactinemia, and acromegaly. The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation** (TxGNN score: 99.83%), with **no clinical trials and no published literature** currently supporting this direction. Across all 10 ranked predictions, **schizophrenia (rank 9)** represents the only indication with meaningful evidence (L3; 3 clinical trials, 20 publications), though its recommendation remains Hold due to the paradoxical safety profile.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia (0 authorizations; bromocriptine is broadly known for Parkinson's disease, hyperprolactinemia, and acromegaly) |
| Predicted New Indication (Rank 1) | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, bromocriptine is a dopamine D2/D3 receptor agonist — this characterization is referenced consistently across all ten repurposing rationale assessments in this evidence pack. It has established efficacy in conditions driven by hyperdopaminergic or hypodopaminergic states, including Parkinson's disease, prolactin-secreting pituitary adenomas (prolactinomas), acromegaly, and antipsychotic-associated metabolic disturbances.

The predicted indication — **congenital disorder of glycosylation with defective fucosylation (CDG-IIc, also known as Leukocyte Adhesion Deficiency type II / LAD II)** — is a rare inherited metabolic disease caused by biallelic mutations in the *SLC35C1* gene encoding the GDP-fucose transporter. The resulting defect impairs fucosylation of glycoproteins and glycolipids across cell types, leading to recurrent infections, intellectual disability, and growth retardation. The mechanistic assessment in this evidence pack is unambiguous: *"There is no known biological link between bromocriptine's D2 agonist mechanism and the fucosylation pathway. There is no clinical or basic science evidence supporting this indication."*

This prediction most likely reflects graph-topology co-embedding patterns within the TxGNN disease knowledge graph rather than direct pharmacological plausibility. The rank 1 position (score 99.83%) does not imply biological confidence — it reflects the model's internal node similarity metric, which can be driven by indirect network connections. The complete absence of any supporting evidence reinforces a conservative Hold stance for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Bromocriptine is currently **not marketed in Saudi Arabia**. No regulatory authorizations are on record. The regulatory query (2026-03-29) returned zero results.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Full safety data (key warnings, contraindications, drug-drug interactions) was not retrieved in this evidence pack. DrugBank query was successful (result count: 1) but MOA and safety fields remain unpopulated. The TFDA package insert query also returned a result; manual extraction of warning/contraindication text is required before any clinical use assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure TxGNN model prediction (Evidence Level L5) for a rare inherited metabolic enzyme defect. No clinical trials, observational studies, or published literature support bromocriptine's use in congenital glycosylation disorders. The mechanistic bridge between dopaminergic D2/D3 receptor agonism and fucosylation biosynthesis has not been established in any preclinical or clinical context.

**To proceed, the following is needed:**
- Preclinical studies (cell-based assays or animal models of *SLC35C1*-deficient cells) to determine whether D2/D3 receptor agonism has any effect on GDP-fucose transport or fucosylation efficiency
- MOA data retrieval from DrugBank API (DG002, currently High-severity data gap)
- Full safety profile extraction from TFDA package insert (DG001, currently Blocking data gap): warnings, contraindications, and DDI profile
- Expert consultation from a specialist in congenital disorders of glycosylation to assess biological plausibility

---

### Note on Broader Prediction Landscape

Among all 10 TxGNN-predicted indications for bromocriptine, **schizophrenia (rank 9, score 99.73%)** stands out as the only indication with non-trivial evidence:

| Rank | Disease | Evidence Level | Trials | Publications | Decision |
|------|---------|----------------|--------|--------------|---------|
| 1 | Congenital disorder of glycosylation with defective fucosylation | L5 | 0 | 0 | Hold |
| 3 | Retinal dystrophy with or without extraocular anomalies | L5 | 0 | 15 (mostly off-target) | Hold |
| 6 | Hydranencephaly | L5 | 0 | 1 (mismatched) | Hold |
| **9** | **Schizophrenia** | **L3** | **3** | **20** | **Hold** |

The schizophrenia evidence is mechanistically coherent (bromocriptine as a D2 agonist influences the dopamine hypothesis of schizophrenia) but carries a critical safety signal: PMID 8120934 documents *bromocriptine-induced schizophrenia* in a susceptible patient, and all three clinical trials target antipsychotic side effects (hyperprolactinemia, metabolic disturbances) rather than core psychiatric symptoms. A separate focused report on the bromocriptine–schizophrenia pair is recommended if further evaluation is desired.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

