---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus — A Multi-Candidate TxGNN Evaluation

## One-Sentence Summary

Insulin Aspart is a rapid-acting human insulin analogue originally developed and approved for glycaemic control in **diabetes mellitus (Type 1 and Type 2)** as mealtime/bolus therapy. The TxGNN model's top-ranked prediction is **Type 1 Diabetes Mellitus** (score **99.95%**), which is important to flag upfront: this is a **re-confirmation of the drug's existing standard-of-care indication**, not a genuine repurposing signal, and is supported by **93 registered clinical trials (top 10 summarized below)** and **20 related publications**. The model additionally surfaced **9 further candidate indications** at very high scores (>99.3%), but only 3 of these (permanent neonatal diabetes, thiamine-responsive dysfunction syndrome/TRMA, pancreatic agenesis) have plausible mechanistic grounding worth further research; the remaining 6 show signs of knowledge-graph confounding (comorbidity co-occurrence, reverse causation) and are not actionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1 and Type 2) — rapid-acting mealtime/bolus insulin. (Structured license text unavailable; drug is not currently marketed in Saudi Arabia.) |
| Predicted New Indication | Type 1 Diabetes Mellitus *(Note: this is the drug's already-established indication, not a novel repurposing candidate — see rationale below)* |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data for this record is currently unavailable (flagged as data gap DG002, High severity — remediation: query DrugBank API directly). Based on well-established pharmacological knowledge, Insulin Aspart is a rapid-acting recombinant human insulin analogue (proline→aspartic acid substitution at position B28) designed for faster subcutaneous absorption than regular human insulin, providing prandial (mealtime) glycaemic control as part of basal-bolus regimens.

**Important flag on the top-ranked prediction:** Type 1 Diabetes Mellitus is not a new indication for Insulin Aspart — it is the condition for which the drug class was designed and is already globally approved. In T1DM, autoimmune destruction of pancreatic β-cells causes absolute insulin deficiency; Insulin Aspart directly substitutes for the missing physiological prandial insulin secretion. This is a first-order, direct causal mechanism rather than a predictive inference, which is why the evidence level reaches L1 (supported by dozens of completed trials and RCTs). The evidence pack itself annotates this entry as one that should be presented separately from genuine repurposing candidates, and this report follows that guidance.

### Overview of the Other 9 TxGNN-Predicted Candidates

Because this evidence pack is unusually rich in per-candidate mechanistic rationale, the remaining 9 predictions are summarized here rather than being treated as noise:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Consideration |
|------|---------|-------------|-----------------|----------|--------------------|
| 2 | Autoimmune oophoritis | 99.92% | L5 | Hold | Likely reflects APS-2 comorbidity (T1DM + autoimmune oophoritis) rather than a treatment mechanism; no trials/literature |
| 3 | Opsismodysplasia | 99.59% | L5 | Hold | INPPL1(SHIP2) shares the PI3K/AKT insulin-signalling pathway, but the disease is a skeletal dysplasia, not a metabolic disorder; no clinical logic for insulin treatment |
| 4 | Thiamine-responsive dysfunction syndrome (TRMA/Rogers) | 99.57% | L4 | Research Question | Diabetes component of TRMA is genuinely insulin-treated in practice, but zero trials/literature in this pack — mechanistically plausible, evidentially unsupported |
| 5 | Permanent neonatal diabetes mellitus (PNDM) | 99.55% | L3 | Proceed with Guardrails | KCNJ11/ABCC8/INS mutations cause neonatal insulin deficiency analogous to T1DM; insulin is already standard therapy for most PNDM subtypes; only 1 review article in this pack |
| 6 | Classic stiff person syndrome (SPS) | 99.51% | L5 | Hold | Likely knowledge-graph confounding via shared GAD65 autoantibody with T1DM comorbidity, not a treatment mechanism; standard SPS therapy is benzodiazepines/IVIG/rituximab |
| 7 | Focal stiff limb syndrome | 99.51% | L5 | Hold | Same GAD65/T1DM comorbidity confound as rank 6 |
| 8 | Pancreatic agenesis | 99.44% | L4 | Research Question | Congenital absence of islet cells (PTF1A/GATA6) is an extreme form of absolute insulin deficiency — plausible, but the 2 literature hits in this pack are indirect (insulin autoimmune syndrome case series; general T2D insulin review) |
| 9 | Drug-induced localized lipodystrophy | 99.35% | L5 | Hold | **Reverse-causation risk**: insulin injections are a well-documented *cause* of injection-site lipodystrophy, not a treatment for it. Likely a text-mining artifact |
| 10 | Centrifugal lipodystrophy | 99.32% | L5 | Hold | Same lipodystrophy semantic-confusion risk as rank 9; distinct paediatric disease of unknown etiology |

---

## Clinical Trial Evidence

*(Extracted from the Type 1 Diabetes Mellitus candidate — top 10 of 93 registered trials, prioritized by relevance grade and phase)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Multinational crossover comparing detemir+aspart vs. NPH+aspart on hypoglycaemia frequency in well-controlled T1D basal-bolus regimen |
| [NCT03143816](https://clinicaltrials.gov/study/NCT03143816) | Phase 4 | Completed | 60 | Real-life pilot comparing prandial insulin aspart vs. inhaled Technosphere insulin in T1D patients on multiple daily injections |
| [NCT01194258](https://clinicaltrials.gov/study/NCT01194258) | Phase 2 | Completed | 132 | Double-blind crossover comparing lispro-PH20 or aspart-PH20 vs. insulin lispro in basal-bolus therapy |
| [NCT01992588](https://clinicaltrials.gov/study/NCT01992588) | Phase 1 | Completed | 48 | PK/PD of faster-acting insulin aspart (FIAsp) as a CSII bolus vs. standard aspart in T1D |
| [NCT03959514](https://clinicaltrials.gov/study/NCT03959514) | Phase 1 | Completed | 18 | Glucose-clamp PK/PD/safety study comparing ultra-rapid AT247 vs. NovoRapid® and Fiasp® in T1DM |
| [NCT07068295](https://clinicaltrials.gov/study/NCT07068295) | Phase 1 | Completed | 65 | PK/PD/safety of investigational fast-acting insulin NNC0471-0119 vs. insulin aspart via insulin pump |
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Once- vs. twice-daily detemir dosing frequency in children/adolescents with T1D, using aspart as mealtime bolus |
| [NCT01774565](https://clinicaltrials.gov/study/NCT01774565) | N/A | Completed | 43 | Closed-loop glucose control comparing faster-acting aspart vs. standard aspart in insulin-treated diabetes |
| [NCT05653050](https://clinicaltrials.gov/study/NCT05653050) | N/A | Completed | 26 | Closed-loop glucose control vs. standard pump + CGM therapy in adolescents with T1D |
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Safety and efficacy of insulin aspart vs. insulin lispro in insulin pumps (CSII) in children/adolescents with T1D |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6 phase 3a trial: once-weekly insulin icodec vs. once-daily degludec in basal-bolus regimen for T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT non-inferiority trial: degludec vs. detemir (both combined with aspart) in pregnant women with T1D |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT/Systematic Review | Diabetes & Metabolism | Systematic review confirming efficacy/safety of insulin aspart vs. regular human insulin in T1D and T2D |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Clinical Trial | Expert Opin Pharmacother | Evidence review of biphasic insulin aspart 30 in the treatment of Type 1 diabetes |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Comprehensive review of T1D pathophysiology, epidemiology, and micro/macrovascular complications |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Management of T1D in pregnancy: lifestyle, pharmacological treatment, and diabetes technology |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Insulin aspart in T1D/T2D shows more rapid absorption and improved HbA1c vs. regular human insulin |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Review of insulin aspart use in the management of T1D and T2D |
| [31345519](https://pubmed.ncbi.nlm.nih.gov/31345519/) | 2019 | Review | Endocrinol Metab Clin North Am | T1D in pregnancy: CGM, CSII, closed-loop systems, and fast-acting insulins |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vascular Health and Risk Management | Insulin degludec/aspart combination for treatment of T1D and T2D |

---

## Saudi Arabia Market Information

Insulin Aspart currently has **no registered authorizations in Saudi Arabia** (market status: Not Marketed; total licenses: 0). No product-level licensing data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Package insert warnings/contraindications (DG001) are classified as a **Blocking**-severity data gap in this evidence pack, and DDI query results returned "not found." Until the SFDA/manufacturer package insert PDF is retrieved and parsed, this candidate cannot complete the S1 safety pre-screening stage — this applies to all indications assessed above, including the confirmatory T1DM entry.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(applies specifically to the confirmatory Type 1 Diabetes Mellitus indication and, secondarily, to permanent neonatal diabetes mellitus as a research-worthy extension)*

**Rationale:**
- The Type 1 Diabetes Mellitus signal reflects the drug's already-validated, globally standard use, backed by extensive Phase 3/4 trial data and multiple RCTs (L1) — there is no scientific uncertainty about efficacy, only administrative/regulatory gaps for the Saudi Arabia market.
- Permanent neonatal diabetes mellitus (rank 5, L3) has strong mechanistic plausibility (insulin deficiency from KCNJ11/ABCC8/INS mutations) and reflects existing clinical practice, but this pack contains only one supporting review article.
- The other 8 candidates (ranks 2, 3, 4, 6, 7, 8, 9, 10) lack clinical trial or literature support in this pack; several (autoimmune oophoritis, stiff person syndrome variants, both lipodystrophy entries) show clear signs of knowledge-graph confounding (comorbidity co-occurrence or reverse causation) rather than genuine therapeutic signal, and should be marked **Hold**.

**To proceed, the following is needed:**
- Retrieve and parse the SFDA/manufacturer package insert PDF to resolve the Blocking-severity safety data gap (DG001) before any S1 safety pre-screening can be completed.
- Query DrugBank API to obtain structured mechanism-of-action data (DG002).
- For permanent neonatal diabetes, TRMA/Rogers syndrome, and pancreatic agenesis (ranks 4, 5, 8): commission a targeted literature search for direct evidence (case series/registry data), since these are rare monogenic diseases unlikely to have registered RCTs.
- For the 6 "Hold" candidates: no further evidence-gathering is recommended given the mechanistic implausibility or confounding risk identified; these should be deprioritized in favor of higher-yield candidates from other drugs in the pipeline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

