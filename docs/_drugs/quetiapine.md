---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Psychiatric Disorders to Trichotillomania (Hair-Pulling Disorder)

## One-Sentence Summary

Quetiapine is an atypical antipsychotic (5-HT2A/D2 receptor antagonist), though no Saudi Arabia regulatory or original-indication data is available in this evidence pack. Among TxGNN's ten highest-ranked predictions, only **Trichotillomania** is supported by actual drug-specific evidence — **7 publications**, including case reports and reviews directly discussing quetiapine's use in this condition — while the model's single highest-scoring prediction was screened out as a false positive (see note below).

> **Screening note:** TxGNN's #1-ranked candidate, *retinal dystrophy with or without extraocular anomalies* (score 99.57%), was reviewed against its 15 supporting publications. None of these papers mention quetiapine — they are general pediatric ophthalmology/orbital-disease literature that co-occurs with the disease term only by name-matching. The evidence pack itself flags this as a spurious pairing with "no mechanistic link" and stage **S0/Hold**. It is therefore excluded from this report, which instead focuses on **Trichotillomania (rank 8)**, the only candidate with genuine drug-specific support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Saudi Arabia (0 licenses on file); no approved-indication text in this evidence pack |
| Predicted New Indication | Trichotillomania (hair-pulling disorder) |
| TxGNN Prediction Score | 99.38% (rank 9206 of TxGNN's ranked list) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank/regulatory sources for this drug (flagged as a High-severity data gap in this evidence pack). Based on known pharmacology, quetiapine acts as a 5-HT2A/D2 receptor antagonist, a mechanism shared by several atypical antipsychotics that are used off-label as augmentation agents for obsessive-compulsive and impulse-control spectrum disorders.

Trichotillomania is now classified within the OCD-spectrum of disorders, characterized by repetitive hair-pulling behavior with an impulse-control component. The mechanistic rationale for quetiapine is that its serotonergic/dopaminergic antagonism may modulate the same circuitry implicated in compulsive/impulsive symptom generation — a plausible but indirect link, since no publication in the evidence pack demonstrates this mechanism directly in trichotillomania patients.

The supporting literature consists mainly of case reports and narrative reviews describing favorable responses to quetiapine in individual patients, plus one report of quetiapine *exacerbating* obsessive-compulsive symptoms in a patient with comorbid trichotillomania — indicating the relationship is not uniformly positive and warrants controlled study before any clinical inference is drawn.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review/Case series | Psychiatry | Overview of trichotillomania pharmacotherapy; case report of a favorable clinical response to quetiapine in a 33-year-old patient |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case Report | Rev Bras Psiquiatr | Quetiapine reported as treatment for trichotillomania (abstract not available) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case Report | J Psychiatry Neurosci | Report of quetiapine exacerbating obsessive-compulsive symptoms in a patient with comorbid OCD, trichotillomania, and bipolar disorder — a cautionary counter-example |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Notes lack of consensus/guidelines for trichotillomania pharmacotherapy; calls for better clinician education |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | J Practical Nursing | General treatment overview of trichotillomania |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case Report/Review | Psychosomatics | Case report of recurrent Rapunzel syndrome (trichobezoar) secondary to trichotillomania, with literature review |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case Report | Case Rep Psychiatry | Trichotillomania presenting as a manifestation of early-onset dementia; not specific to quetiapine treatment |

## Saudi Arabia Market Information

Quetiapine currently holds no valid marketing authorization in Saudi Arabia (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA warnings, contraindications, or drug-interaction data were retrievable for this compound — flagged as a Blocking-severity data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to case reports and narrative reviews (no clinical trials, evidence level L4), and includes at least one report of symptom exacerbation rather than benefit — the signal is not yet strong or consistent enough to advance. The model's top-ranked candidate (retinal dystrophy) was already excluded as a screening artifact, underscoring the need for careful evidence review before any repurposing decision on this drug.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action data from DrugBank — currently a High-severity gap
- At least one controlled (non-case-report) study of quetiapine in trichotillomania before considering progression beyond Hold
- Drug interaction (DDI) data, currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

