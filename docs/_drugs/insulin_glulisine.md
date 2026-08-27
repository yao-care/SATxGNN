---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus (Insulin Therapy) to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin glulisine is a rapid-acting recombinant human insulin analogue (marketed globally as Apidra) used for glycemic control in diabetes mellitus.
> The TxGNN model's top prediction — **Type 1 Diabetes Mellitus** — is supported by **50 clinical trials** and **19 publications**, but this is not a novel repurposing signal: it corresponds to glulisine's already-established, on-label indication.
> The candidate's own repurposing rationale flags this explicitly, and a **blocking data gap** (no Saudi Arabia/TFDA package insert on file) currently prevents a formal safety review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from this Evidence Pack — no Saudi Arabia license records and `original_indications` is empty. Based on drug class, insulin glulisine is generically used for glycemic control in diabetes mellitus (insulin therapy). |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin glulisine is a recombinant rapid-acting human insulin analogue produced by substituting two amino acids in the insulin B-chain (B3 Lys→Glu, B29 Lys→Glu). This modification accelerates absorption and onset of action compared to regular human insulin, while the molecule retains full affinity for the insulin receptor. Mechanistically, it acts identically to endogenous insulin: receptor binding drives cellular glucose uptake and suppresses hepatic glucose output, replacing the absolute insulin deficiency that defines Type 1 Diabetes Mellitus.

Unlike most TxGNN candidates in this pipeline, this is **not a case of mechanistic extrapolation from a distant original indication**. The repurposing rationale for this candidate states directly that Type 1 Diabetes Mellitus is already an approved indication for glulisine (marketed as Apidra), and that the high TxGNN score reflects a genuine, well-established pharmacological relationship rather than a newly discovered one. In other words, the model has correctly reconstructed known clinical pharmacology rather than surfaced a novel therapeutic hypothesis.

Because `original_moa` in this Evidence Pack is a data gap and no Saudi Arabia license/package-insert text is available, the on-label indication cannot be independently confirmed from local regulatory sources — this should be treated as an open item rather than an assumption, even though the mechanistic story is internally consistent and well documented in the trial/literature evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Phase 3 | Completed | 224 | Multicenter RCT comparing biosimilar GP40321 to Apidra® (glulisine) in T1DM; assessed non-inferior immunogenicity, efficacy, and safety. |
| [NCT01194258](https://clinicaltrials.gov/study/NCT01194258) | Phase 2 | Completed | 132 | Double-blind crossover comparing PH20-accelerated lispro/aspart formulations to insulin lispro for prandial control in basal-bolus therapy. |
| [NCT02509429](https://clinicaltrials.gov/study/NCT02509429) | Phase 2 | Completed | 24 | Closed-loop artificial pancreas vs. insulin pump + threshold-suspend CGM to reduce nocturnal hypoglycemia in children with T1DM. |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week open-label study of glulisine + glargine in T1DM; evaluated HbA1c change and safety (adverse events, hematology, lipids). |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Randomized comparison of glulisine vs. lispro (both with glargine) in T1/T2DM; compared efficacy and hypoglycemia frequency. |
| [NCT00135941](https://clinicaltrials.gov/study/NCT00135941) | Phase 3 | Completed | 582 | Glargine + glulisine MDI vs. premixed insulin in T1/T2DM; evaluated patient-reported outcomes. |
| [NCT00174668](https://clinicaltrials.gov/study/NCT00174668) | Phase 3 | Completed | 311 | 52-week trial of intensified glulisine + glargine regimen vs. conventional two-injection therapy in poorly controlled T2DM. |
| [NCT01768559](https://clinicaltrials.gov/study/NCT01768559) | Phase 3 | Completed | 894 | 26-week RCT comparing lixisenatide to once-daily and three-times-daily glulisine, add-on to glargine ± metformin in T2DM. |
| [NCT01203111](https://clinicaltrials.gov/study/NCT01203111) | Phase 4 | Completed | 207 | Intensive glargine + glulisine regimen in T2DM inadequately controlled on basal insulin and oral agents; HbA1c and hypoglycemia endpoints. |
| [NCT01159353](https://clinicaltrials.gov/study/NCT01159353) | Phase 1 | Completed | 37 | Randomized PK/PD study comparing postprandial glucose excursion with glulisine vs. aspart in obese T2DM subjects. |

*40 additional registered trials exist in the Evidence Pack (mostly closed-loop/pump-technology and comparator studies) but are not listed here per the 10-trial display limit.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Hormone and Metabolic Research | Multinational RCT (n=683) comparing glulisine to lispro in adults with T1DM; established comparable efficacy/safety. |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | RCT (PK/PD, pediatric) | Diabetes Care | PK, postprandial glucose control, and safety of glulisine vs. regular human insulin in pediatric T1DM patients. |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | Phase III RCT | Diabetes, Obesity & Metabolism | Biosimilar insulin glulisine (T-Glu) vs. originator (R-Glu) in adults with T1DM; immunogenicity, efficacy, and safety. |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technology & Therapeutics | Three-way crossover RCT: glulisine vs. aspart vs. lispro via CSII in T1DM; glulisine trended toward fewer catheter occlusions. |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort (CSII pediatric) | Pediatrics International | 1-year cohort of glulisine via CSII in 20 children with T1DM; significant improvement in post-meal glucose. |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Review (clinical pharmacology) | Clinical Pharmacokinetics | Review of glulisine PK/PD: faster absorption and onset, shorter duration than regular human insulin. |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Review of glulisine's role in diabetes management; comparable glucose-lowering effect to lispro. |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative study | Acta Diabetologica | Real-world comparison of glulisine, lispro, and aspart in T1DM patients on CSII; effectiveness and hypoglycemia/DKA rates. |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT (pediatric) | Diabetes Technology & Therapeutics | 26-week basal-bolus trial comparing glulisine to lispro in pediatric T1DM; comparable efficacy and safety. |
| [29159123](https://pubmed.ncbi.nlm.nih.gov/29159123/) | 2016 | PK/PD study | Journal of Clinical & Translational Endocrinology | PK/PD of glargine-glulisine basal-bolus vs. premixed analog insulin across standardized meals in T1DM. |

*9 additional publications exist in the Evidence Pack but are not listed here per the 10-item display limit.*

---

## Saudi Arabia Market Information

Insulin glulisine is currently **not marketed** in Saudi Arabia per this Evidence Pack (`market_status: 未上市`, `total_licenses: 0`). No license records are available to summarize in table form.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were retrievable in this Evidence Pack — this is flagged as a **Blocking** data gap (DG001: TFDA/local package insert not yet obtained), which currently prevents a formal safety (S1) evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Clinical trial and literature evidence for glulisine in Type 1 Diabetes Mellitus is extensive and consistent (L1: multiple completed Phase 3 RCTs), but the candidate's own repurposing rationale indicates this is glulisine's known, already-approved indication rather than a novel repurposing opportunity — this materially limits its value as a *new* indication candidate.
- A **Blocking** data gap (no local package insert/regulatory warning data) means the safety initial screen (S1) cannot yet be completed, and the drug is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- Local package insert / TFDA-equivalent regulatory documentation (warnings, contraindications, DDI) to close the Blocking gap and enable S1 safety screening
- DrugBank-sourced MOA record to replace the current data gap and confirm the mechanistic narrative independently
- Clarification of whether this candidate should be reclassified as a **known-indication confirmation** rather than a repurposing opportunity, given the rationale text explicitly states T1DM is Apidra's approved use
- If reclassified, deprioritize in favor of ranks 2–10, none of which currently have clinical trial or literature support (L5, mostly "Hold")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

