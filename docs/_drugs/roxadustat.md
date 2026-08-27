---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Roxadustat: From Renal Anemia to Dry Eye Syndrome

## One-Sentence Summary

> Roxadustat is a HIF prolyl-hydroxylase inhibitor (HIF-PHI) used to treat anemia associated with chronic kidney disease.
> The TxGNN model predicts it may be effective for **Dry Eye Syndrome**,
> but this is currently supported by only **1 observational clinical trial** (not an interventional efficacy study) and **no published literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal anemia (CKD-associated) — noted in trial context; not formally recorded in Saudi Arabia licensing data (drug is unmarketed) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for roxadustat is currently a data gap in this evidence pack. Based on information available within the evidence pack itself, roxadustat is a HIF-PHI (HIF prolyl-hydroxylase inhibitor) that stabilizes HIF-1α/2α to promote endogenous erythropoietin (EPO) production, and is used to treat renal anemia in patients with chronic kidney disease.

The proposed link to dry eye syndrome is mechanistic rather than clinical: the HIF pathway is involved in the hypoxic response and wound-repair processes of corneal and meibomian gland epithelium, so theoretically HIF stabilization could affect meibomian gland function. However, the only related study identified is an **observational** trial examining meibomian gland morphology/function in renal anemia patients — it does not administer roxadustat as an intervention nor evaluate dry eye as a treatment endpoint. It reflects a comorbidity association (renal anemia patients are themselves a population at elevated risk of dry eye) rather than causal drug evidence.

Three other TxGNN-predicted indications (bone Paget disease, dentinogenesis imperfecta, squamous cell carcinoma) were also flagged in this evidence pack, all at evidence level L5 with no supporting trials or literature. Notably, the squamous cell carcinoma prediction is explicitly framed in the evidence as a potential **safety risk signal** (HIF pathway activation is linked to tumor angiogenesis) rather than a therapeutic opportunity — a reminder that high TxGNN similarity scores do not by themselves indicate treatment benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | N/A | Unknown | 50 | Observational study of meibomian gland function/morphology in renal anemia patients (treated with EPO or roxadustat); does not test roxadustat as a dry eye treatment — relevance graded **C** (comorbidity observation, not causal drug evidence) |

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Roxadustat currently has no marketing authorization in Saudi Arabia (0 licenses on record; market status: 未上市/Not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data for roxadustat are currently unavailable in this evidence pack — including the TFDA package insert, which is flagged as a blocking data gap for safety pre-screening.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical evidence for the top-ranked indication (dry eye syndrome) is a single observational trial with no interventional or efficacy data (relevance grade C), and the drug itself is not currently marketed in Saudi Arabia. Combined with a blocking gap in TFDA safety data, there is insufficient basis to advance past initial safety screening.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation (DrugBank query)
- An interventional study directly testing roxadustat for dry eye syndrome (current evidence is comorbidity-only)
- Reassessment of the squamous cell carcinoma signal as a potential safety concern rather than a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

