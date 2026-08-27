---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Diabetes Mellitus (Insulin Replacement) to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin detemir is a long-acting basal insulin analog used for exogenous insulin replacement in insulin-dependent diabetes.
> The TxGNN model's top-ranked prediction is **Type 1 Diabetes Mellitus**, supported by **50 clinical trials** and **19 publications** —
> however, this is very likely a **known, already-established indication** rather than a genuine new repurposing signal, and the "prediction" mainly reflects a gap in this drug's local (Saudi Arabia/SFDA) regulatory registry rather than a novel mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in registry (data gap) — pharmacologically, insulin detemir is an insulin analog used for exogenous insulin replacement in diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, insulin detemir is a long-acting basal insulin analog acylated with a 14-carbon fatty acid, which reversibly binds albumin to provide slow, prolonged absorption. Like all insulin products, it acts by binding the insulin receptor to promote peripheral glucose uptake and suppress hepatic gluconeogenesis — the standard mechanism of exogenous insulin replacement therapy.

Because of this mechanism, insulin detemir's clinical use **is** the management of insulin-dependent diabetes, including Type 1 Diabetes Mellitus. This means the "predicted new indication" surfaced by TxGNN is not a novel disease association discovered through cross-disease inference — it is the drug's core, already-proven use. The very large volume of supporting Phase 3/4 randomized trials (see below) confirms this is an established indication rather than an exploratory hypothesis.

The evidence pack itself flags this explicitly: the original indication field is empty and the SFDA/Saudi Arabia market record shows zero authorizations, which is why the model and registry infrastructure treat this as a "gap to fill" rather than recognizing it as already-known. **This case should be handled primarily as a data/registry completeness issue** (confirm and document insulin detemir's actual approved indication text once available), not evaluated using the standard repurposing-evidence workflow that applies to genuinely novel disease associations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Compared once- vs twice-daily insulin detemir injections in children/adolescents with T1DM; treat-to-target design. |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Randomized crossover trial comparing hypoglycaemia frequency: detemir + aspart vs NPH + aspart in basal-bolus T1DM regimen. |
| [NCT00537303](https://clinicaltrials.gov/study/NCT00537303) | Phase 4 | Completed | 296 | Compared step-wise addition of insulin aspart to once-daily detemir plus oral agents vs standard regimen. |
| [NCT00788840](https://clinicaltrials.gov/study/NCT00788840) | Phase 4 | Completed | 30 | 24-week randomized parallel trial comparing energy expenditure, weight, and glycaemic control with detemir vs NPH in a basal-bolus regimen. |
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | Completed | 501 | 2-year efficacy and safety comparison of insulin detemir vs NPH insulin in Type 1 diabetes (HbA1c, hypoglycaemia, antibodies). |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Compared insulin detemir vs NPH insulin (once/twice daily + mealtime aspart) in children and adolescents with T1DM. |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Randomized multinational trial comparing detemir vs NPH (both + aspart) in pregnant women with Type 1 diabetes. |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | 6-month multicentre trial comparing efficacy/safety of a 2400 nmol/mL detemir formulation vs NPH in T1DM basal-bolus regimen. |
| [NCT01545791](https://clinicaltrials.gov/study/NCT01545791) | N/A (observational) | Completed | 1037 | PREDICTIVE™ study — large multicentre real-world safety observation of detemir in T1DM and T2DM. |
| [NCT00789711](https://clinicaltrials.gov/study/NCT00789711) | N/A (observational) | Completed | 3131 | Multicentre observational study comparing safety/effectiveness of biphasic insulin aspart 30 vs detemir in diabetes. |

*(40+ additional completed trials are on record but omitted here for brevity; see evidence pack for the full list.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT (EXPECT trial) | Lancet Diabetes Endocrinol | Non-inferiority RCT of degludec vs detemir (both + aspart) in pregnant women with T1DM. |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review / Network Meta-Analysis | Value Health | Compared efficacy/safety of basal insulin regimens (including detemir) in adults with T1DM. |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane Systematic Review | Cochrane Database Syst Rev | Review of (ultra-)long-acting insulin analogues, including detemir, for people with T1DM. |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review / Meta-Analysis | Pol Arch Med Wewn | Detemir vs NPH insulin in Type 1 diabetes — glycaemic control outcomes. |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-Analysis | Clin Ther | Compared efficacy/tolerability of degludec vs other long-acting analogues (glargine, detemir) in T1D/T2D. |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Update on T1DM/T2DM treatment focusing on insulin detemir as a long-acting analog. |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Reviews detemir's mechanism (albumin binding) and use in T1DM/T2DM, including reduced hypoglycaemia risk. |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Comprehensive review of insulin detemir's pharmacology and use in T1DM/T2DM management. |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Reviews insulin analog preparations, including detemir, in children/adolescents with T1DM. |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Spotlight review on detemir's pharmacokinetics and clinical use in T1DM/T2DM. |

*(9 additional publications, mostly cost-effectiveness analyses and case reports, are on record but omitted here for brevity.)*

---

## Saudi Arabia Market Information

Currently no marketing authorization is recorded for insulin detemir in Saudi Arabia (market status: **Not Marketed**, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for insulin detemir in Type 1 Diabetes Mellitus is extremely strong (L1: numerous completed Phase 3/4 RCTs plus systematic reviews/meta-analyses), but this reflects the drug's **already-established use**, not a new repurposing discovery. The "Proceed with Guardrails" designation here should be interpreted as: proceed with formally documenting/confirming this as a known indication, guarded by the need to close the underlying data gaps before treating it as a repurposing candidate in downstream reports.

**To proceed, the following is needed:**
- Official original indication text and mechanism-of-action documentation from DrugBank/SFDA package insert (currently flagged as Blocking/High severity data gaps, DG001–DG002)
- Confirmation from SFDA on whether insulin detemir has ever held or is pending Saudi Arabia market authorization
- Re-classification of this candidate in the pipeline as "known indication — registry gap" rather than "novel repurposing prediction," to avoid consuming repurposing-review resources on an already-approved use
- Key warnings, contraindications, and DDI data (currently unavailable) before any safety-related claims can be made
- Note: predictions ranked #2–10 (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, focal stiff limb syndrome, classic stiff person syndrome, pancreatic agenesis, and three lipodystrophy/lipoatrophy indications) all carry L4–L5 evidence with no supporting trials or literature, and are appropriately scored **Hold** or **Research Question** — several (the lipodystrophy/lipoatrophy indications) likely represent reversed causality (insulin injection as a cause of the condition, not a treatment), and should not be advanced further without dedicated mechanistic review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

