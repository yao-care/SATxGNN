---
layout: default
title: Glatiramer
parent: تنبؤ نموذجي فقط (L5)
nav_order: 293
evidence_level: L5
indication_count: 1
---

# Glatiramer
{: .fs-9 }

مستوى الأدلة: **L5** | دواعي الاستعمال المتوقعة: **1** 
{: .fs-6 .fw-300 }

---

## جدول المحتويات
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## تقرير التقييم الصيدلاني

</div>

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer acetate is an immunomodulator whose established clinical use is relapsing-remitting multiple sclerosis. The TxGNN model predicts a possible link to **Hemoglobinopathy**, but this direction is currently supported by **0 clinical trials** and only **1 case-report-level publication**, indicating an early, prediction-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (relapsing-remitting) — inferred from known pharmacology; no formal indication text available (see below) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (flagged as a High-severity data gap requiring a DrugBank API query). Based on known pharmacology, glatiramer acetate is a random co-polymer that mimics myelin basic protein; it modulates T-cell activity and induces a Th2 immune shift, and this mechanism underlies its proven efficacy in multiple sclerosis.

Hemoglobinopathies (e.g., sickle cell disease, thalassemia) are, by contrast, genetic disorders of hemoglobin structure or synthesis, with core pathology centered on erythropoiesis and hemoglobin chain assembly — a pathway with no established direct connection to glatiramer's immunomodulatory mechanism.

The TxGNN score of 0.99 most likely reflects an indirect knowledge-graph association — for example, shared inflammatory or vaso-occlusive complication nodes seen in sickle cell disease — rather than a validated causal mechanism. This should be treated as a purely predictive, hypothesis-generating link rather than mechanistically confirmed evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case report | Revue neurologique | Describes a 35-year-old woman with a history of beta thalassemia (a hemoglobinopathy) who developed multiple immune disorders after stopping natalizumab for MS; she had previously received first-line subcutaneous immunomodulatory treatment (a category that includes glatiramer). The case does not directly evaluate glatiramer's efficacy against hemoglobinopathy — the connection is incidental (shared patient comorbidity), not a treatment outcome. |

## Saudi Arabia Market Information

Glatiramer is not currently marketed in Saudi Arabia (0 authorizations on record), so no product/dosage-form data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single model-generated prediction (L5) with no clinical trials and only one indirectly related case report; the mechanistic rationale for glatiramer acting on hemoglobinopathy is speculative rather than established. The drug is also not currently marketed in Saudi Arabia, and a Blocking data gap (TFDA/local package insert safety data) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/local package insert safety data (key warnings, contraindications, DDI) — currently Blocking
- Formal DrugBank-sourced mechanism of action data
- Preclinical or mechanistic studies directly linking glatiramer's immune pathway to hemoglobinopathy pathophysiology
- Any prospective clinical or observational evidence beyond the single incidental case report
## إخلاء المسؤولية

هذا المحتوى لأغراض البحث فقط ولا يشكل نصيحة طبية.
يلزم التحقق السريري قبل أي تطبيق سريري.

---

