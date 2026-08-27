---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 551
evidence_level: L5
indication_count: 6
---

# Risperidone
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

# Risperidone: From Psychotic Disorders to Major Affective Disorder

## One-Sentence Summary

Risperidone is a second-generation (atypical) antipsychotic originally used to treat psychotic disorders such as schizophrenia and bipolar mania. The TxGNN model predicts it may also be effective for **Major Affective Disorder** (encompassing treatment-resistant depression and bipolar disorder), with **37 clinical trials** and **20 publications** — including several completed Phase 3 RCTs — currently supporting this direction.

*Note: This evidence pack contains 6 TxGNN-predicted indications for risperidone. Five of the six (ranked #1–#5 by raw TxGNN score) have little to no supporting evidence and are flagged in the data itself as low-plausibility or noise. This report focuses on the one candidate with substantive clinical evidence — "Major Affective Disorder" (rank #6) — and summarizes the other five separately below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (`original_indications` is empty, drug is unmarketed locally). Globally, risperidone is approved for schizophrenia and bipolar mania. |
| Predicted New Indication | Major Affective Disorder (treatment-resistant depression / bipolar disorder) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap (`original_moa: [Data Gap]`) in this evidence pack. However, the pack's own repurposing rationale consistently describes risperidone as a **D2/5-HT2A receptor antagonist** with 5-HT2A–dominant binding — the pharmacological signature characteristic of second-generation antipsychotics.

Risperidone is already established in psychotic disorder treatment and — critically — is already approved in many markets for **bipolar mania**, which is itself classified as an affective (mood) disorder. This creates a direct mechanistic bridge to the TxGNN prediction: the same D2/5-HT2A antagonism that controls manic and psychotic symptoms is the pharmacological basis for using risperidone as (1) an augmentation agent in antidepressant-refractory major depressive disorder and (2) a mood-stabilizing/maintenance therapy in bipolar disorder.

This is not a purely computational leap — it is supported by a substantial existing literature base of adjunctive-use studies, several completed Phase 3 RCTs (see below), and a mature real-world prescribing pattern of risperidone augmentation in psychiatry, making this the strongest-evidenced prediction in the pack (L1, compared to L3–L5 for the others).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI monotherapy in unipolar treatment-resistant depression; efficacy, safety, and long-term maintenance vs. placebo augmentation |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind, placebo-controlled adjunctive risperidone in major depressive disorder with sub-optimal response to antidepressants |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Double-blind, placebo-controlled risperidone monotherapy in ambulatory bipolar disorder with comorbid anxiety |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Placebo-controlled trial of valproate + risperidone in young children (3–7 yr) with bipolar disorder |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Double-blind, placebo/active-controlled study of risperidone long-acting injectable (LAI) monotherapy for prevention of mood episodes in Bipolar I disorder |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | Treatment of Early Age Mania (TEAM) study — lithium, valproate, and risperidone in children/adolescents with bipolar disorder or mania symptoms |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Double-blind, placebo-controlled risperidone monotherapy in ambulatory bipolar disorder with moderately severe anxiety |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Controlled trial of risperidone vs. divalproex sodium with MRI assessment of affected circuitry in pediatric bipolar disorder |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Risperidone augmentation in patients with failed/partial response to antidepressant therapy |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Pilot trial of risperidone vs. olanzapine as add-on to SSRI in treatment-resistant depression |

*27 additional trials with lower direct relevance (comparator/observational/imaging studies) are on file but omitted here for brevity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Randomized trial of risperidone for treatment-refractory major depressive disorder |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review / Network Meta-analysis | J Affective Disorders | Compares efficacy/discontinuation of augmentation agents (incl. risperidone) in treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review / Meta-analysis | J Psychopharmacology | Augmentation/combination treatments for early-stage treatment-resistant depression |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review / Meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in major depressive disorder |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Review | Cochrane Database Syst Rev | Second-generation antipsychotics for major depressive disorder and dysthymia |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review | J Psychopharmacology | Efficacy/tolerability of antidepressant + second-generation antipsychotic combinations vs. esketamine vs. lithium |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | Annals of Pharmacotherapy | Efficacy and safety of risperidone augmentation for major depressive disorder |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Efficacy/tolerability of antidepressant augmentation with atypical antipsychotics (17 trials, 3807 patients) |
| [23554581](https://pubmed.ncbi.nlm.nih.gov/23554581/) | 2013 | Meta-analysis | PLoS Medicine | Risk-benefit profile of adjunctive atypical antipsychotics for depression |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Review | Expert Opin Pharmacother | Risperidone long-acting injection as monotherapy/adjunctive maintenance therapy in bipolar I disorder |

*10 additional publications (mostly narrative reviews and case reports) are on file but omitted here for brevity.*

---

## Saudi Arabia Market Information

Risperidone currently has **no marketed products on file in Saudi Arabia** (0 authorizations, `market_status: 未上市`). No local approved indication text is available for comparison against the predicted use.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-interaction data are available in this evidence pack — `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all data gaps or "not found".)

---

## Other Predicted Indications (Screened — Hold)

The remaining five TxGNN predictions in this pack rank higher by raw model score but have essentially no supporting evidence and are explicitly flagged in the rationale text as low-plausibility:

| Rank | Disease | Evidence | Rationale (from pack) | Decision |
|---|---|---|---|---|
| 1 | Gaze palsy, familial horizontal, with progressive scoliosis | None | ROBO3-related axon pathway disorder, no known link to monoamine antagonism | Hold |
| 2 | Asperger syndrome, susceptibility to | None | Predicted entity is a genetic-susceptibility label, not a treatable clinical population | Hold |
| 3 | Amelocerebrohypohidrotic syndrome | None | Rare genetic syndrome, no biological link to D2/5-HT2A mechanism | Hold |
| 4 | Phelan-McDermid syndrome | 3 publications (case study, review, preclinical) | Symptomatic (irritability/aggression) rationale plausible, no controlled trials in this population | Research Question |
| 5 | Trichotillomania | 10 publications (mostly case reports) | Plausible as SSRI-augmentation strategy, but no RCT evidence | Research Question |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Major Affective Disorder indication only; all other predicted indications in this pack remain on Hold)*

**Rationale:**
Multiple completed Phase 3 RCTs and systematic reviews/meta-analyses support risperidone as an adjunctive treatment for treatment-resistant depression and as monotherapy/maintenance for bipolar disorder — this is an L1 evidence level with an existing, mature clinical practice pattern, not merely a model prediction.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently a Blocking data gap — DG001)
- Formal mechanism-of-action documentation from DrugBank (currently a High-severity data gap — DG002)
- A regulatory pathway assessment, since risperidone is not currently marketed in Saudi Arabia (0 authorizations)
- Drug-drug interaction data (current DDI query returned "not found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

