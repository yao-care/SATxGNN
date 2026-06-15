---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to RCC Associated with Neuroblastoma

## One-Sentence Summary

Axitinib (Inlyta®) is a selective VEGFR-1/2/3 tyrosine kinase inhibitor, FDA-approved for second-line treatment of advanced renal cell carcinoma and used in first-line combination regimens with immune checkpoint inhibitors (pembrolizumab+axitinib, avelumab+axitinib).
The TxGNN model predicts it may be effective for **renal cell carcinoma associated with neuroblastoma**, an extremely rare pediatric overlap syndrome.
However, **no clinical trials or publications** currently support this specific direction — this prediction is based solely on knowledge graph topology, and should be treated as a hypothesis-generating signal only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (globally approved, second-line; **not registered in Saudi Arabia**) |
| Predicted New Indication | Renal Cell Carcinoma Associated with Neuroblastoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published literature included in the evidence dataset, axitinib is an oral second-generation tyrosine kinase inhibitor with potent and highly selective inhibitory activity against VEGFR-1, -2, and -3 — with IC₅₀ values approximately 10-fold lower than sunitinib or sorafenib. Its antitumour effect in clear cell RCC is well established: VHL gene mutation leads to HIF stabilization → VEGF/VEGFR axis overactivation → tumour neoangiogenesis, which axitinib directly suppresses. This mechanism underpins its role in the landmark AXIS trial (second-line mRCC) and the KEYNOTE-426 and JAVELIN Renal 101 first-line combination approvals.

Renal cell carcinoma associated with neuroblastoma is an extremely rare paediatric entity, representing co-occurrence or overlapping histology of neuroblastoma and renal malignancy. Both tumour types may harbour VEGF-driven angiogenesis, providing a theoretical basis for VEGFR inhibition. However, the dominant oncogenic driver in neuroblastoma is ALK mutation (or MYCN amplification), not VEGFR, which substantially weakens the mechanistic link. Objective response rates to standard VEGFR-TKIs may be considerably lower in this context compared to clear cell RCC.

The TxGNN model assigns a prediction score of 99.90% (rank 2250 among all disease nodes), most likely reflecting topological proximity in the knowledge graph between RCC nodes and neuroblastoma-associated renal tumour nodes — rather than direct biological evidence. Without any specific clinical trial, case series, or mechanistic study for this subtype, the prediction cannot be actioned in a clinical or regulatory context at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Axitinib is an antineoplastic targeted therapy (VEGFR-TKI) for renal cell carcinoma.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective VEGFR tyrosine kinase inhibitor (second-generation TKI) |
| Myelosuppression Risk | Low (VEGFR-TKIs do not directly suppress bone marrow; haematological toxicity is uncommon compared to conventional cytotoxics) |
| Emetogenicity Classification | Low (oral TKI; nausea reported but high-grade vomiting is uncommon) |
| Monitoring Items | Blood pressure (hypertension is the most common class effect — monitor at baseline and regularly), liver function (ALT/AST/bilirubin), thyroid function (TSH), urine protein (proteinuria), CBC, renal function |
| Handling Protection | Standard oral oncology medication precautions apply; cytotoxic drug handling regulations are not generally mandated for targeted oral TKIs, but institutional policy should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Renal cell carcinoma associated with neuroblastoma is an extremely rare paediatric entity for which there is currently no clinical trial data, published case reports, or mechanistic studies supporting axitinib use; the TxGNN prediction (L5 — model prediction only) is insufficient to advance to any clinical evaluation stage. Furthermore, axitinib is not registered in Saudi Arabia for any indication, meaning baseline regulatory and safety documentation would need to be established before any repurposing pathway could begin.

**To proceed, the following is needed:**
- Natural history data and case series for neuroblastoma-associated RCC to characterise VEGF/VEGFR expression in this subtype
- Preclinical studies (cell lines or patient-derived tumour models) assessing axitinib activity in neuroblastoma-RCC overlap tissue
- Paediatric pharmacokinetics and safety characterisation (children have different TKI metabolism; see published narrative review PMID 39326645 on axitinib outcomes across age groups)
- Detailed MOA data from DrugBank to confirm biological plausibility of VEGFR targeting in this subtype
- Saudi Arabia (SFDA) registration pathway assessment if clinical evidence accumulates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

