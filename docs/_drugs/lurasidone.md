---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Schizophrenia/Bipolar Depression to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone (DrugBank DB08815) is an atypical (second-generation) antipsychotic internationally marketed as Latuda for schizophrenia and bipolar I depression. The TxGNN model predicts it may also be effective for **manic bipolar affective disorder**, with **15 clinical trials** and **19 publications** retrieved for this indication — though most of that evidence base actually addresses the depressive pole of bipolar I disorder rather than mania specifically, a distinction discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no Saudi Arabia license data); internationally approved for schizophrenia and bipolar I depression (brand Latuda) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, this evidence pack does not contain structured mechanism-of-action data (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, lurasidone (development code SM-13496) is a benzisothiazole-derivative atypical antipsychotic that acts as a potent antagonist at dopamine D2 and serotonin 5-HT2A receptors, with high-affinity antagonism at 5-HT7 and partial agonism at 5-HT1A, and negligible affinity for H1/M1 receptors. This receptor profile — particularly 5-HT7 antagonism and 5-HT1A partial agonism — is believed to underlie mood-stabilizing and antidepressant effects, which is the pharmacological basis for its existing global approvals in bipolar I depression (monotherapy and adjunctive to lithium/divalproex).

Bipolar disorder involves both depressive and manic poles managed with overlapping pharmacological classes (antipsychotics, mood stabilizers), which is consistent with why a model would associate lurasidone with the broader "bipolar affective disorder" disease space.

**Important caveat:** the predicted indication here is specifically the *manic* pole ("manic bipolar affective disorder"), but nearly all retrieved clinical trial and literature evidence is for *bipolar I depression*, not mania. One review in the evidence set (PMID 31957501) explicitly states lurasidone "has not been studied in patients with mania or bipolar psychosis." This is a meaningful evidence gap that should not be glossed over — the strong evidence level (L1) reflects the bipolar depression literature, not direct mania efficacy data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Lurasidone adjunctive to lithium/divalproex for prevention of recurrence in Bipolar I Disorder, with/without rapid cycling or psychotic features |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | Placebo-controlled pivotal trial of SM-13496 (lurasidone) in Bipolar I Depression |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety of SM-13496 (lurasidone) in Bipolar I Disorder |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension of long-term safety/effectiveness of flexibly dosed lurasidone in pediatric subjects |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | Open-label extension of lurasidone adjunctive to lithium/divalproex in Bipolar I Disorder |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | 6-week double-blind, placebo-controlled RCT of flexibly dosed lurasidone in children/adolescents with Bipolar I Depression |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | 6-week multicenter double-blind, placebo-controlled RCT of lurasidone for Bipolar I Depression (trial terminated early) |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | SMART pragmatic RCT comparing four FDA-approved treatments (including lurasidone) for bipolar depression |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | ELICE-BD: 6-week RCT of lurasidone adjunctive therapy for cognitive functioning in euthymic Bipolar I/II patients |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | 6-week randomized, open-label study of lurasidone add-on vs. treatment-as-usual for cognitive functioning in euthymic Bipolar I patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Systematic Review/Meta-analysis | BMJ Mental Health | Dose-response meta-analysis of lurasidone efficacy, acceptability, and metabolic/endocrine profile in bipolar depression |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opinion on Pharmacotherapy | Reviews pharmacodynamics/pharmacokinetics and major RCTs of lurasidone; notes it has not been studied in mania or bipolar psychosis |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network Meta-analysis | The Lancet Psychiatry | Comparative efficacy/tolerability of pharmacological interventions (including lurasidone) for acute bipolar depression |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Guideline | Bipolar Disorders | CANMAT/ISBD 2018 bipolar disorder management guidelines |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Guideline | Bipolar Disorders | CANMAT/ISBD recommendations for bipolar disorder with mixed presentations |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Systematic Review/Network Meta-analysis | Molecular Psychiatry | Mood stabilizers/antipsychotics for maintenance-phase bipolar disorder |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Reviews antipsychotics (incl. lurasidone) approved for bipolar depression as antidepressant agents |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | General diagnosis and treatment review of bipolar disorder |
| [40808269](https://pubmed.ncbi.nlm.nih.gov/40808269/) | 2025 | Consensus/Task Force Report | Bipolar Disorders | ISBD Task Force consensus definition of treatment-resistant bipolar depression |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Editorial/Commentary | American Journal of Psychiatry | Commentary on lurasidone and bipolar disorder |

## Saudi Arabia Market Information

Lurasidone is currently **not marketed** in Saudi Arabia — no license/authorization records exist in this evidence pack (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data are currently available in this evidence pack (TFDA package insert data is flagged as a Blocking data gap, DG001).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The bipolar-disorder literature and clinical trial base for lurasidone is substantial (multiple completed Phase 3 RCTs, including two placebo-controlled pivotal trials), supporting L1 evidence overall. However, the predicted indication is specifically the *manic* pole, and the retrieved evidence is overwhelmingly for *bipolar depression* — direct efficacy data for mania/bipolar psychosis is explicitly stated as lacking in the literature, so this prediction should be pursued cautiously and not treated as directly validated.

**To proceed, the following is needed:**
- TFDA/local package insert with warnings and contraindications (Blocking gap, DG001) — required before any safety pre-assessment (S1)
- Verified mechanism-of-action documentation from DrugBank (High gap, DG002)
- Dedicated evidence review for lurasidone specifically in manic/mixed episodes (not just bipolar depression) to confirm applicability to the predicted indication
- Drug-drug interaction data, since none is currently available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

