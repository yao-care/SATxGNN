---
layout: default
title: Nortriptyline
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 2
---

# Nortriptyline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nortriptyline: From Tricyclic Antidepressant to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant (TCA); this evidence pack does not capture its originally-approved indication or full mechanism-of-action record (flagged as data gaps DG001/DG002).
The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, with **no registered clinical trials** but **20 supporting publications**, including one RCT and one Cochrane systematic review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (TFDA/SFDA package insert not yet retrieved — see Data Gap DG001) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data from DrugBank is currently unavailable for this drug (Data Gap DG002, High severity). Based on the literature-derived pharmacological profile captured in this evidence pack, nortriptyline is classified as a **tricyclic antidepressant (TCA)**.

Its primary pharmacological action is inhibition of norepinephrine (NE) reuptake, with some degree of serotonin reuptake inhibition as well. ADHD pathophysiology is closely linked to dysregulation of the prefrontal cortex NE/dopamine (DA) system, and this mechanism is highly similar to that of already-approved non-stimulant ADHD medications — **atomoxetine** (a selective NE reuptake inhibitor) and **bupropion** (an NE/DA reuptake inhibitor) — which provides moderate mechanistic plausibility for the TxGNN prediction.

Because the original approved indication is not captured in this evidence pack, the direct clinical relationship between nortriptyline's prior use and ADHD cannot be fully characterized here. However, the literature suggests nortriptyline may be particularly suitable for ADHD patients with comorbid tic disorders, where stimulants are often contraindicated — though findings on tic-exacerbation risk are inconsistent when compared with bupropion (see PMID 8428875 for contrast). This positions nortriptyline as a plausible second-line, non-stimulant candidate rather than a first-line therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | TCAs, including nortriptyline, evaluated as second-line treatment for reducing ADHD symptoms in children and adolescents |
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline's efficacy and tolerability in pediatric ADHD |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT | Pediatric Nephrology | Randomized double-blind trial of nortriptyline for treating enuresis in children with comorbid ADHD |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Clinical Guideline/Review | Ann Clin Psychiatry | CANMAT task force recommendations for managing mood disorders with comorbid adult ADHD |
| [7807071](https://pubmed.ncbi.nlm.nih.gov/7807071/) | 1995 | Systematic Assessment | J Nerv Ment Dis | Systematic assessment of tricyclic antidepressants, including nortriptyline, in adult ADHD treatment |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | Review of nonstimulant ADHD treatments; notes nortriptyline's noradrenergic activity but flags narrow therapeutic index and cardiovascular toxicity risk limiting use |
| [17915180](https://pubmed.ncbi.nlm.nih.gov/17915180/) | 2007 | Review | Neuropsychiatrie | Evidence-based pharmacotherapy algorithms for ADHD and comorbid psychiatric disorders |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opin Drug Saf | Safety review of non-stimulant ADHD agents, including tricyclic antidepressants such as nortriptyline |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Open-label/Cohort | J Am Acad Child Adolesc Psychiatry | Nortriptyline evaluated in children with ADHD and comorbid tic disorder/Tourette's syndrome |
| [8444763](https://pubmed.ncbi.nlm.nih.gov/8444763/) | 1993 | Retrospective Chart Review | J Am Acad Child Adolesc Psychiatry | Chart review of 58 pediatric/adolescent ADHD cases treated with nortriptyline |

---

## Saudi Arabia Market Information

Nortriptyline currently holds no marketing authorizations in Saudi Arabia (market status: Not Marketed; 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug-drug interaction (DDI) data are currently available in this evidence pack (DDI query returned "not found"); the TFDA/SFDA package insert has not yet been retrieved (Data Gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nortriptyline has a mechanistically plausible, noradrenergically-mediated rationale for ADHD and is supported by one completed RCT plus a Cochrane systematic review covering TCAs as second-line ADHD therapy — sufficient to justify continued evaluation, but no clinical trials are currently registered for this specific drug-indication pair, and it is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- DrugBank-verified structured mechanism-of-action data — currently a **High**-severity data gap (DG002)
- A completed drug-drug interaction (DDI) database query (current status: not found)
- Regulatory pathway assessment, since the drug is not currently marketed in Saudi Arabia
- Updated/contemporary RCT data — most supporting evidence predates 2005, with the only controlled trial dating to 2000
- Note: a second predicted indication, "ADHD, inattentive type" (TxGNN score 99.33%), was also flagged but has no supporting clinical trials or literature (Evidence Level L5) and is currently on **Hold**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

