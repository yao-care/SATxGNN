---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is an antiepileptic drug used to treat partial-onset (focal) seizures in epilepsy. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but the supporting evidence currently available (**1 ongoing Phase 3 trial** and **14 publications**) centers almost entirely on bipolar *depressive* episodes rather than manic episodes — a partial mismatch between the predicted label and the actual evidence base that must be flagged before further action.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / partial-onset (focal) seizures *(inferred from trial and literature context — no official Saudi indication text is available, drug is not yet marketed)* |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed official mechanism-of-action data is not available (Data Gap DG002). However, the evidence pack itself contains mechanistic context: lacosamide selectively enhances the **slow inactivation of voltage-gated sodium channels**, producing extended stabilization of neuronal cell membranes, and it also interacts with **CRMP2 (collapsin response mediator protein 2)**. This dual mechanism is shared conceptually with older sodium-channel-modulating antiepileptics (e.g., carbamazepine, lamotrigine, valproate) that are already established mood stabilizers — supporting a plausible, class-level rationale for a psychiatric repurposing signal.

Epilepsy and bipolar disorder are frequently comorbid, and several AEDs originally developed for seizure control were later repurposed as mood stabilizers via this same membrane-stabilizing mechanism. This precedent is the core rationale behind the TxGNN prediction.

That said, the evidence curator's own relevance grading flags an important caveat: the only registered clinical trial (NCT07412132, grade B) targets **major depressive episodes** of Bipolar I/II disorder, not manic episodes as the predicted disease label states. Most supporting publications similarly describe lacosamide's effect on **depressive/anxious mood symptoms**, not mania. This is a meaningful indication mismatch — the mechanistic and clinical signal is real, but it points more strongly toward bipolar depression than toward the specific "manic" label TxGNN assigned.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Randomized, double-blind trial of lacosamide as augmentation therapy for moderate-to-severe **major depressive episodes** in Bipolar I/II disorder — note: targets depressive, not manic, episodes. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective controlled study | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs. other antiepileptics as mood stabilizers in bipolar disorder patients without epilepsy. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week open-label pilot evaluating efficacy and safety of lacosamide for bipolar depression. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report (adverse event) | Indian J Psychol Med | Lacosamide-precipitated neutropenia in a patient with bipolar disorder and comorbid epilepsy. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical mood stabilization with lacosamide in a patient with mood disorder comorbid with PTSD and fronto-temporal epilepsy; describes sodium-channel slow-inactivation mechanism. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicenter study | Epilepsy Behav | Lacosamide improved depression and anxiety symptoms in patients with focal-onset seizures. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Management of a pregnant patient with Bipolar I disorder and comorbid seizure-like activity. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | 2018 update on therapeutic drug monitoring of antiepileptic drugs, noting use in bipolar disorder management. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Adv Drug Deliv Rev | Overview of AEDs approved 1990–2011, including lacosamide's pharmacokinetics and tolerability profile. |
| [16732716](https://pubmed.ncbi.nlm.nih.gov/16732716/) | 2006 | Review | Expert Opin Investig Drugs | Review of second-generation AEDs including lacosamide. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review (mechanism) | ACS Chem Neurosci | Druggability of CRMP2, a target relevant to lacosamide's proposed mechanism in neurological/neuropsychiatric disease. |

## Saudi Arabia Market Information

Lacosamide is **not currently marketed** in Saudi Arabia (0 product authorizations on file), so no local product/indication data is available for review.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale (sodium-channel slow inactivation, class-level precedent among mood-stabilizing AEDs) is plausible, and there is a genuine, if modest, clinical evidence base (tier-2 retrospective and open-label studies, one recruiting Phase 3 RCT). However, the evidence consistently concerns bipolar **depressive** episodes, not the **manic** episodes named in the prediction, so the current label should be treated as a hypothesis to refine rather than a confirmed direction.

**To proceed, the following is needed:**
- Resolve the manic-vs-depressive indication mismatch — consider re-scoping the candidate indication to "bipolar depression" pending clarification
- Await completion of NCT07412132 (estimated completion 2027-01) for controlled efficacy data
- Obtain TFDA/official package insert warnings and contraindications (Data Gap DG001, Blocking — required before any S1 safety assessment)
- Obtain formal drug mechanism-of-action documentation from DrugBank (Data Gap DG002)
- Since the drug is unmarketed in Saudi Arabia, a market-entry/regulatory pathway assessment would be needed before any local clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

