---
layout: default
title: Pramipexole
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Pramipexole
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

# Pramipexole: From Parkinson's Disease/RLS to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Pramipexole is a non-ergot dopamine D2/D3 receptor agonist internationally known for treating Parkinson's disease and restless legs syndrome (this original-indication detail is public knowledge, not present in this evidence pack, since the drug is not licensed in Saudi Arabia).
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> but only **1 clinical trial** (rated low relevance) and **9 publications** (none a direct ADHD RCT) currently support this direction, and the proposed mechanism runs opposite to standard ADHD pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug not marketed in Saudi Arabia, no license records; publicly known for Parkinson's disease / RLS) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder |
| TxGNN Prediction Score | 99.99% (model rank 93) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap, DG002). Based on publicly known pharmacology, pramipexole is a non-ergoline dopamine D2/D3 receptor agonist, originally developed for Parkinson's disease and later extended to restless legs syndrome — indications outside the scope of this evidence pack since the drug is not registered in Saudi Arabia.

The mechanistic rationale for ADHD is genuinely double-edged. ADHD's dopamine hypothesis (reduced prefrontal-striatal dopaminergic transmission) theoretically supports testing a dopamine agonist. However, at low doses pramipexole preferentially activates presynaptic D2/D3 autoreceptors, which can **decrease** rather than increase net dopamine release — the opposite direction from standard ADHD pharmacotherapy (e.g., methylphenidate, a dopamine reuptake inhibitor that increases synaptic dopamine). This makes the mechanistic linkage speculative and directionally uncertain rather than a straightforward extension of known pharmacology.

Consistent with this, the only clinical trial retrieved (NCT00558766) was conducted in Parkinson's disease patients studying reward signaling, not ADHD patients, and was graded "C" (low relevance, likely a TxGNN noise match). None of the nine associated publications are ADHD-focused RCTs — most concern restless legs syndrome, periodic leg movements, or Tourette's syndrome, conditions that share dopaminergic biology with ADHD but are not equivalent to it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00558766](https://clinicaltrials.gov/study/NCT00558766) | N/A | Completed | 35 | Studied motor cortex reward signaling in Parkinson's disease patients on dopaminergic medications (via TMS); not an ADHD trial — graded low relevance (Grade C), likely a TxGNN false-positive link to ADHD. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22407510](https://pubmed.ncbi.nlm.nih.gov/22407510/) | 2012 | RCT | Movement Disorders | Multicenter placebo-controlled trial of pramipexole for Tourette's syndrome, testing whether dopamine normalization affects tic disorders (dopaminergic overlap with ADHD, not a direct ADHD trial). |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | RCT | Clinical Neuropharmacology | 11-week trial comparing piribedil vs. pramipexole/ropinirole on vigilance/cognition in Parkinson's disease with excessive daytime sleepiness. |
| [15540638](https://pubmed.ncbi.nlm.nih.gov/15540638/) | 2004 | Cohort | Developmental Medicine & Child Neurology | Periodic leg movements in prepubertal children with sleep disturbance; notes dopamine agonist (pramipexole) response in a pediatric population overlapping with ADHD comorbidity. |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | Review of restless-legs syndrome pathophysiology and dopaminergic treatment, a condition frequently comorbid with ADHD. |
| [19412489](https://pubmed.ncbi.nlm.nih.gov/19412489/) | 2006 | Review | Neuropsychiatric Disease and Treatment | Review of pramipexole's repurposed use in restless legs syndrome, illustrating precedent for indication expansion via the dopaminergic pathway. |
| [37342213](https://pubmed.ncbi.nlm.nih.gov/37342213/) | 2023 | Case Report | Frontiers in Pain Research | Case of chronic low back pain and oral dysesthesia comorbid with ADHD, treated with atomoxetine plus pramipexole, achieving remission. |
| [38649244](https://pubmed.ncbi.nlm.nih.gov/38649244/) | 2024 | Case Report | BMJ Case Reports | Hypokalaemia case in a patient with ADHD/autism on pramipexole among other medications; incidental co-mention, not an efficacy study. |
| [24079375](https://pubmed.ncbi.nlm.nih.gov/24079375/) | 2013 | Animal Model | Journal of Motor Behavior | Spontaneously hypertensive rat model proposed for studying RLS/PLM–ADHD co-occurrence; preclinical, mechanism-oriented. |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Science | Pharmacological Research | Receptor heteromerization study (α2A adrenoceptor–dopamine D4 receptor) relevant to impulsive-control disorders including ADHD; basic pharmacology, not clinical. |

---

## Saudi Arabia Market Information

Pramipexole is currently not marketed in Saudi Arabia — no license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as unresolved data gaps in this evidence pack — notably, TFDA package-insert warnings/contraindications are flagged as a **Blocking**-severity gap that prevents a full safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Despite a very high TxGNN prediction score, the supporting evidence is weak and the mechanistic rationale is directionally uncertain — low-dose pramipexole's autoreceptor-preferring action may reduce rather than increase dopamine tone, contrary to established ADHD pharmacology. The single retrieved clinical trial is unrelated to ADHD (Grade C relevance), and no direct ADHD RCT exists in the literature set. This corresponds to Evidence Level L4 / Decision Stage S1 — appropriate for a research question, not for clinical advancement.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap, DG002, High severity)
- TFDA/local package insert warnings and contraindications (currently a Blocking-severity data gap, DG001) — required before any S1 safety pre-assessment can proceed
- A hypothesis-testing preclinical or pilot study clarifying net dopaminergic effect (autoreceptor vs. postsynaptic activation) at ADHD-relevant doses
- Direct ADHD clinical trial data (none currently exist for this drug-indication pair)
- Since pramipexole holds zero licenses in Saudi Arabia, a regulatory pathway assessment would be needed before any local development

**Note:** Within this same evidence pack, the schizophrenia signal (rank 9; Evidence Level L2, Decision Stage S2, "Proceed with Guardrails") is substantially better supported — including a completed Phase 3 add-on RCT, a positive systematic review/meta-analysis, and multiple positive RCTs — and may warrant prioritization as a nearer-term repurposing candidate over ADHD.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

