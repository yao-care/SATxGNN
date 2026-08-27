---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
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

Using the report format specified in the prompt to produce the evaluation report directly from the Evidence Pack.

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin degludec (DrugBank DB09564, brand name Tresiba) is an ultra-long-acting basal insulin analogue used broadly in the management of diabetes mellitus.
> The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**, with **50 clinical trials** and **20 publications** currently associated with this drug-disease pair —
> however, this predicted indication substantially overlaps with insulin degludec's already-established, real-world use in type 1 diabetes, so the trial/literature volume reflects confirmatory clinical experience rather than novel repurposing evidence. Two other data gaps (TFDA safety labeling and mechanism-of-action detail) currently block a full evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`taiwan_regulatory.licenses` and `original_indications` are both empty). Insulin degludec is generally known as a basal insulin used across diabetes mellitus management. |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% (raw score 0.9944; overall model rank 8,518) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified) — see caveat below |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Caveat on Evidence Level:** The L1 rating reflects trial *volume*, not novelty. Nearly all identified Phase 3 trials (e.g. BEGIN, BOOST, SWITCH, PRONTO-T1D series) compare insulin degludec against other basal insulins for its *already-approved* use in type 1 diabetes, rather than testing it as a *new* indication. This is important context for interpreting the "repurposing" signal below.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the evidence pack (`original_moa` = Data Gap, flagged as DG002/High severity). Based on generally known pharmacology, insulin degludec is an ultra-long-acting basal insulin analogue that forms soluble multihexamers after subcutaneous injection; these are slowly and continuously converted into monomers, producing a flat, stable, ultra-long duration of glucose-lowering action with reduced day-to-day variability compared with earlier basal insulins (glargine, detemir). This mechanism is consistent with its role as a foundational basal insulin for glycemic control.

The predicted new indication — type 1 diabetes mellitus — is mechanistically coherent because basal insulin replacement is a cornerstone of type 1 diabetes management (absolute insulin deficiency), and insulin degludec's pharmacokinetic profile (low peak-to-trough variability, reduced nocturnal hypoglycemia risk) has been extensively studied in this population.

However, this is an important limitation rather than a confirmation of novel repurposing value: type 1 diabetes mellitus is **already a standard, well-established use case** for insulin degludec (marketed as Tresiba, used in basal-bolus regimens). The large trial and literature volume returned by TxGNN's evidence search therefore reflects the depth of *existing* clinical experience with this drug in this disease, not a newly discovered therapeutic opportunity. The other five TxGNN-predicted diseases for this drug (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, focal stiff limb syndrome, classic stiff person syndrome) returned **zero** clinical trials and **zero** literature hits, meaning none of them currently have independent evidentiary support either.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1,108 | Faster-acting insulin aspart vs NovoRapid, both combined with insulin degludec, in adults with Type 1 Diabetes — confirms glycemic efficacy of degludec-based basal-bolus regimens |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1,392 | PRONTO-T1D: LY900014 vs insulin lispro, both combined with glargine or degludec, in adults with Type 1 Diabetes |
| [NCT05904743](https://clinicaltrials.gov/study/NCT05904743) | Phase 4 | Completed | 141 | INHALE-3: inhaled insulin (Afrezza) + degludec vs usual care in adults with Type 1 Diabetes |
| [NCT02662114](https://clinicaltrials.gov/study/NCT02662114) | N/A | Completed | 2,302 | EU-TREAT: European retrospective study of effectiveness of Tresiba® after switching basal insulin in Type 1/Type 2 Diabetes |
| [NCT05069545](https://clinicaltrials.gov/study/NCT05069545) | N/A | Completed | 411 | Real-world study of NovoPen® 6 with Tresiba® & Fiasp® in Type 1 Diabetes glycemic control |
| [NCT03557892](https://clinicaltrials.gov/study/NCT03557892) | N/A | Completed | 28 | Crossover trial: CSII + CGM vs multi-injection therapy using degludec as basal insulin in Type 1 Diabetes |
| [NCT02536859](https://clinicaltrials.gov/study/NCT02536859) | Phase 1 | Completed | 60 | PK/PD comparison of insulin degludec vs insulin glargine 300 U/mL at steady state in Type 1 Diabetes |
| [NCT06238778](https://clinicaltrials.gov/study/NCT06238778) | Phase 2 | Active, not recruiting | 227 | HDV-insulin lispro vs insulin lispro alone in adults with Type 1 Diabetes receiving insulin degludec (liver-targeting insulin approach) |
| [NCT03838783](https://clinicaltrials.gov/study/NCT03838783) | Phase 4 | Unknown | 30 | FIT Untethered: degludec + CSII combination regimen during exercise in Type 1 Diabetes |
| [NCT06945406](https://clinicaltrials.gov/study/NCT06945406) | Phase 1 | Recruiting | 124 | Ongoing safety/PK/PD study of novel agent LY4057996 in healthy participants and participants with Type 1 and Type 2 Diabetes |

*Note: 50 trials total were returned for this drug-disease pair; the above 10 were selected for phase/relevance. Most trials study insulin degludec as an already-used comparator/backbone therapy rather than as a novel intervention for type 1 diabetes.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: once-weekly insulin efsitora alfa vs once-daily insulin degludec, phase 3 non-inferiority trial in adults with Type 1 Diabetes |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs once-daily insulin degludec in basal-bolus regimen for Type 1 Diabetes |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: insulin degludec vs insulin detemir (both + aspart) in pregnant women with Type 1 Diabetes, non-inferiority trial |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: degludec vs glargine U100 in Type 1 Diabetes patients prone to nocturnal severe hypoglycemia |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP: basal insulin degludec vs aspart via insulin pump, glycemic control comparison in Type 1 Diabetes |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX: degludec 100 IU/mL vs glargine 300 IU/mL efficacy/safety in Type 1 Diabetes |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1: glargine 300 U/mL vs degludec 100 U/mL around exercise sessions in Type 1 Diabetes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review/Meta-analysis | Clin Ther | Efficacy and tolerability of insulin degludec vs other long-acting basal insulins in Type 1 and Type 2 Diabetes |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review/Network Meta-analysis | Value Health | Comparative efficacy/safety of basal insulin regimens (including degludec) in adults with Type 1 Diabetes |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Current status of insulin degludec in Type 1 and Type 2 Diabetes based on randomized and observational trials |

*20 publications total were returned; the above 10 prioritize RCTs and systematic reviews.*

---

## Saudi Arabia Market Information

Insulin degludec currently has **no registered market authorization in Saudi Arabia** in this evidence pack (`total_licenses = 0`, `market_status = 未上市`). No product/dosage-form/authorization records are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI records are all unavailable in this evidence pack — flagged as DG001, a **Blocking**-severity data gap that prevents initial safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking**-severity data gap (DG001 — missing TFDA/regulatory package insert warnings and contraindications) prevents even an initial safety assessment (S1) of this candidate, regardless of the strength of efficacy evidence.
- The top-ranked predicted indication (type 1 diabetes mellitus) largely overlaps with insulin degludec's already-established use as a basal insulin, meaning the abundant trial/literature volume is confirmatory rather than evidence of genuine repurposing opportunity; the drug is also not currently marketed in Saudi Arabia (0 authorizations), so there is no existing local regulatory foothold to build on.
- The four other TxGNN-predicted diseases beyond the top two (opsismodysplasia, thiamine-responsive dysfunction syndrome, focal stiff limb syndrome, classic stiff person syndrome) have zero supporting trials or literature and cannot currently be evaluated.

**To proceed, the following is needed:**
- TFDA/Saudi regulatory package insert data (warnings, contraindications, DDI) to resolve the Blocking data gap (DG001)
- DrugBank/validated mechanism-of-action data (DG002) to properly assess mechanistic plausibility
- A clarified repurposing rationale distinguishing this candidate from insulin degludec's existing, approved use in type 1 diabetes — or reprioritization toward the lower-ranked, currently evidence-free predicted indications if genuine novelty is the goal
- Local market access/registration assessment, given zero current authorizations in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

