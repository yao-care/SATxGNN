---
layout: default
title: Pyridostigmine
parent: 僅模型預測 (L5)
nav_order: 529
evidence_level: L5
indication_count: 7
---

# Pyridostigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Pyridostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is a cholinesterase inhibitor whose established use is symptomatic control of myasthenia gravis (MG); formal Taiwan license/indication records are not available in this evidence pack, but the drug's core pharmacology is already directed at this disease. The TxGNN model predicts it may be effective for **Myasthenia Gravis with Thymus Hyperplasia** — a common AChR-antibody-positive MG subtype rather than a distinct disease — supported by **0 clinical trials** and **3 publications** currently indexed for this specific term.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from license records (data gap); known pharmacology indicates established use in myasthenia gravis symptom control |
| Predicted New Indication | Myasthenia Gravis with Thymus Hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known information, Pyridostigmine is an acetylcholinesterase inhibitor that increases acetylcholine concentration at the neuromuscular junction — this is the core pharmacological mechanism already used for symptomatic treatment of myasthenia gravis (MG).

Thymus hyperplasia is not a separate disease process from a pharmacological standpoint — it is a common histological finding in AChR-antibody-positive MG. The neuromuscular junction defect that pyridostigmine treats is present regardless of whether thymus hyperplasia is also observed. As stated in the model's rationale: *"Pyridostigmine 抑制乙醯膽鹼酯酶，提升神經肌肉接合處 ACh 濃度，此為 MG 症狀治療的核心藥理機轉，與是否合併胸腺增生無關"* (the mechanism is independent of thymus status).

Consequently, this prediction largely reflects an **already-established clinical practice** rather than a novel hypothesis — pyridostigmine is the standard symptomatic agent for AChR-antibody-positive MG, of which thymus hyperplasia is a frequent subtype, not a new pharmacological target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | Retrospective analysis of 39 non-thymomatous, AChR-antibody-positive, late-onset MG patients showing 2-year post-thymectomy outcomes, relevant to the thymus-hyperplasia MG population that relies on pyridostigmine for symptom control. |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Reviews MG pathology, autoantibody-driven neuromuscular junction dysfunction, and disease heterogeneity across MG subtypes including those with thymic involvement. |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case Report | Neuromuscular Disorders | Case of MuSK-positive MG with thymus hyperplasia presenting as dropped head syndrome; illustrates the clinical link between thymus hyperplasia and MG subtypes, though MuSK-positive disease responds less predictably to cholinesterase inhibitors than AChR-positive disease. |

## Saudi Arabia Market Information

No licenses currently registered — Pyridostigmine is not marketed in Taiwan (0 authorizations; `taiwan_regulatory.market_status` = 未上市).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are a Blocking data gap — DG001 — and must be resolved before any S1 safety review can proceed.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted "new" indication is mechanistically not a novel hypothesis but an established use pattern (AChE inhibition for MG symptom control) applied to a common MG subtype; evidence level is L3 (cohort/review-level, no dedicated RCTs for this specific subtype term), and the drug is currently unmarketed in Taiwan, so guardrails around access and safety documentation are required before advancing.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking) — required for S1 safety review
- DrugBank/formal MOA documentation (DG002, High)
- Route compatibility assessment (currently pending in evidence pack)
- Taiwan market-access pathway evaluation, given 0 current licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

