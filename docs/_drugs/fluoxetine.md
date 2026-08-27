---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From Major Depressive Disorder to Phobic Disorder

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) whose established therapeutic role is Major Depressive Disorder (MDD). The TxGNN model generated 10 candidate new indications for this drug; most top-ranked candidates (e.g., schizoid, histrionic, paranoid personality disorder) show high raw similarity scores but lack disease-specific clinical support. This report focuses on **Phobic Disorder**, the candidate with the strongest actual evidence base — **6 clinical trials** (including a completed Phase 3 RCT) and **20 publications**, several of them direct fluoxetine RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — referenced as fluoxetine's core approved indication in the underlying evidence texts; formal Saudi Arabia license/indication text is unavailable (drug not marketed locally) |
| Predicted New Indication | Phobic Disorder |
| TxGNN Prediction Score | 99.63% (rank 6280 of candidate pool) |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, fluoxetine is an SSRI that enhances serotonergic neurotransmission by potently and selectively inhibiting neuronal reuptake of serotonin — a mechanism already proven effective in MDD.

Phobic Disorder sits within the same serotonergically-mediated anxiety-spectrum family as MDD, and SSRIs are a standard pharmacological class for panic disorder, agoraphobia, and social phobia. This mechanistic continuity is well supported empirically: fluoxetine has a completed Phase 3 RCT specifically in childhood/adolescent social phobia (NCT00043537), plus a substantial body of direct RCTs and systematic reviews spanning panic disorder, agoraphobia, and generalized social phobia.

Notably, this candidate was selected over the raw top-ranked TxGNN prediction (schizoid personality disorder, score 99.92%), because the evidence pack's own rationale explicitly flags that top score as likely driven by semantic clustering around "personality disorder" terms rather than a disease-specific mechanistic link — no clinical trials and only tangential literature support it. Phobic Disorder, agoraphobia, and melancholia were the only candidates in this pack reaching L1–L2 evidence with an actionable recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00043537](https://clinicaltrials.gov/study/NCT00043537) | Phase 3 | Completed | 139 | 4-year RCT comparing behavioral therapy, fluoxetine, and placebo for childhood/adolescent social phobia — direct, highest-quality efficacy evidence for this indication |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8800 | Individual patient data meta-analysis on antidepressant (incl. SSRI) efficacy across anxiety-disorder severity strata |
| [NCT05002309](https://clinicaltrials.gov/study/NCT05002309) | Phase 2 | Recruiting | 100 | RCT comparing CBT vs. optimized pharmacotherapy in early-onset youth depression, relevant to anxiety-spectrum comorbidity |
| [NCT00004446](https://clinicaltrials.gov/study/NCT00004446) | N/A | Completed | 80 | Fluoxetine efficacy/durability in depersonalization disorder, including comorbid social phobia/panic/anxiety subgroups |
| [NCT06942494](https://clinicaltrials.gov/study/NCT06942494) | N/A | Recruiting | 88 | Family-based CBT self-help RCT for adolescent OCD — indirect relevance via anxiety-spectrum comorbidity |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | Not yet recruiting | 80 | Hydroxyzine vs. treatment-as-usual pilot RCT for panic disorder — comparator study, not fluoxetine-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9812120](https://pubmed.ncbi.nlm.nih.gov/9812120/) | 1998 | RCT | Am J Psychiatry | Fluoxetine vs. placebo RCT in panic disorder; evaluates outcome measures beyond panic-attack frequency |
| [36519357](https://pubmed.ncbi.nlm.nih.gov/36519357/) | 2023 | Review | Expert Opin Pharmacother | Up-to-date overview of pharmacotherapy, including SSRIs, for social anxiety disorder |
| [15466674](https://pubmed.ncbi.nlm.nih.gov/15466674/) | 2004 | RCT | Arch Gen Psychiatry | Fluoxetine vs. CBT vs. placebo in generalized social phobia |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | SSRIs, including fluoxetine, proven superior to placebo in panic disorder and agoraphobia |
| [7786880](https://pubmed.ncbi.nlm.nih.gov/7786880/) | 1995 | RCT/Pharmacologic study | J Psychiatry Neurosci | Open fluoxetine trial in panic disorder with platelet binding study |
| [17092192](https://pubmed.ncbi.nlm.nih.gov/17092192/) | 2006 | Review | J Clin Psychiatry | Evidence review of SSRIs (fluoxetine, paroxetine, etc.) for social anxiety disorder |
| [10471245](https://pubmed.ncbi.nlm.nih.gov/10471245/) | 1999 | Review | Harvard Rev Psychiatry | SSRI class review including panic disorder as an established indication |
| [11593305](https://pubmed.ncbi.nlm.nih.gov/11593305/) | 2001 | RCT | Braz J Med Biol Res | Double-blind RCT comparing mirtazapine vs. fluoxetine in panic disorder |
| [9192539](https://pubmed.ncbi.nlm.nih.gov/9192539/) | 1997 | Open-label trial | J Child Adolesc Psychopharmacol | Open-label pediatric fluoxetine trial for mixed anxiety disorders |
| [7836341](https://pubmed.ncbi.nlm.nih.gov/7836341/) | 1995 | Short communication | J Clin Psychiatry | Early clinical report on fluoxetine and social phobia |

---

## Saudi Arabia Market Information

Fluoxetine currently holds **no marketing authorization in Saudi Arabia** (0 licenses on record). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — SFDA package insert has not yet been retrieved.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phobic Disorder is the best-supported repurposing candidate in this evidence pack — L1 evidence anchored by a completed Phase 3 pediatric social phobia RCT plus multiple direct fluoxetine RCTs/reviews across the panic/agoraphobia/social phobia spectrum. However, the drug is not currently marketed in Saudi Arabia, and the TFDA/SFDA package insert (warnings/contraindications) is an unresolved **Blocking** data gap that prevents this candidate from formally entering safety pre-assessment (S1).

**To proceed, the following is needed:**
- Retrieve the SFDA/TFDA package insert (warnings, contraindications, DDI) — currently Blocking
- Retrieve confirmed mechanism of action (MOA) data from DrugBank
- Confirm formal original approved indication and license status, since Saudi Arabia license records are empty
- If pursuing registration, define a route-to-market pathway given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

