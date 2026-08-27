---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 4
---

# Methylphenidate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Methylphenidate: Evaluation of Four TxGNN-Predicted Indications

*Note: This evidence pack (`TW-DB00422-multi`) contains four ranked predicted indications with very different evidence profiles rather than a single new-indication candidate. The report below covers all four, using the standard template sections adapted for a multi-candidate pack.*

## One-Sentence Summary

Methylphenidate is a CNS stimulant (DAT/NET reuptake inhibitor); the evidence pack does not record its original approved indication (data gap), though the underlying trial/literature evidence strongly indicates it is ADHD. TxGNN flags four candidate indications ranging from **near-zero-evidence, mechanistically unsupported hits** (faciodigitogenital syndrome, chondromyxoid fibroma) to a **well-evidenced but likely mislabeled "new" indication** (specific developmental disorder, i.e. ADHD — 16 trials, 18 publications) and one **exploratory augmentation hypothesis** (dysthymic disorder, 6 publications, no trials).

## Quick Overview

**Drug-level**

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (data gap); trial/literature content for the top-evidence candidate is entirely ADHD-related |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |

**Predicted indications (ranked)**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Faciodigitogenital syndrome | 99.998% | L5 | S0 | Hold |
| 2 | Chondromyxoid fibroma | 99.991% | L5 | S0 | Hold |
| 3 | Specific developmental disorder | 99.988% | L1 | S3 | Proceed with Guardrails |
| 4 | Dysthymic disorder | 99.11% | L4 | S1 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available at the drug record level (`original_moa: [Data Gap]`). However, the evidence pack's own rationale fields indicate methylphenidate inhibits the dopamine transporter (DAT) and norepinephrine transporter (NET), raising prefrontal cortical dopamine and norepinephrine levels — the standard pharmacological basis for ADHD treatment.

- **Rank 1 (faciodigitogenital syndrome)** and **Rank 2 (chondromyxoid fibroma)**: both are explicitly flagged in the pack's own rationale as having **no identifiable mechanistic link** to methylphenidate's monoamine reuptake-inhibition pathway. Faciodigitogenital syndrome is a congenital AR/GRIPAP1-related disorder; chondromyxoid fibroma is a benign bone/cartilage tumor. Neither pathophysiology intersects with CNS monoamine signaling. Both scores are TxGNN graph-relation artifacts with zero supporting trials or literature.
- **Rank 3 (specific developmental disorder)**: the DAT/NET mechanism directly matches the mechanism of action of stimulant therapy for ADHD, and the associated trial/literature evidence is entirely ADHD-focused. This strongly suggests the pack is surfacing methylphenidate's **already-established primary indication** under a broader/ambiguous disease-ontology label, rather than a genuine repurposing discovery — this should be treated as a data-completeness issue (see DG002 remediation) rather than a novel finding.
- **Rank 4 (dysthymic disorder)**: monoamine reuptake inhibition can theoretically enhance mood and motivational drive, and psychostimulant augmentation of antidepressants has real clinical precedent. However, this mechanism is indirect/adjunctive, not a mechanism specific to dysthymia's pathophysiology.

---

## Clinical Trial Evidence

### Rank 1 (Faciodigitogenital syndrome) / Rank 2 (Chondromyxoid fibroma)
Currently no related clinical trials registered.

### Rank 3 — Specific developmental disorder (ADHD-related)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02167048](https://clinicaltrials.gov/study/NCT02167048) | Phase 1/2 | Active, not recruiting | 52 | Low-dose vs. normal-dose psychostimulants on executive function in ADHD (combined/inattentive type), ages 6–18 |
| [NCT05974241](https://clinicaltrials.gov/study/NCT05974241) | Phase 4 | Completed | 36 | Methylphenidate vs. aripiprazole for irritability in ADHD children with emotion dysregulation |
| [NCT00310986](https://clinicaltrials.gov/study/NCT00310986) | N/A | Unknown | 22 | Breathing meditation combined with methylphenidate for ADHD children (RCT) |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1398 | ADDUCE project: chronic effects of methylphenidate on growth, neurological, psychiatric and cardiovascular systems |
| [NCT05669170](https://clinicaltrials.gov/study/NCT05669170) | Phase 2 | Not yet recruiting | 60 | Methylphenidate for apathy in Parkinson's disease veterans |
| [NCT04647500](https://clinicaltrials.gov/study/NCT04647500) | N/A | Completed | 45 | Methylphenidate/dopaminergic modulation on memory and executive function in 22q11.2 deletion syndrome |
| [NCT05185583](https://clinicaltrials.gov/study/NCT05185583) | Phase 2 | Completed | 18 | Double-blind RCT of methylphenidate for childhood apraxia of speech |
| [NCT07024303](https://clinicaltrials.gov/study/NCT07024303) | Early Phase 1 | Not yet recruiting | 20 | Medication vs. behavioral treatment for challenging behavior in autism |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART trial comparing methylphenidate, amphetamine, and alpha-2 agonists in ADHD with autism spectrum disorder |
| [NCT01554046](https://clinicaltrials.gov/study/NCT01554046) | N/A | Completed | 40 | Methylphenidate (Ritalin IR) in familial ADHD — symptom improvement and side effects |

*6 additional lower-relevance trials exist in the source data (general population/off-topic studies) and are omitted here.*

### Rank 4 (Dysthymic disorder)
Currently no related clinical trials registered.

---

## Literature Evidence

### Rank 1 (Faciodigitogenital syndrome) / Rank 2 (Chondromyxoid fibroma)
Currently no related literature available.

### Rank 3 — Specific developmental disorder (ADHD-related)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Review | Neuropharmacology | Neurobiology of ADHD — genetic basis, frontal-striatal circuit differences |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Cohort | Prog Neuropsychopharmacol Biol Psychiatry | Longitudinal MRI: age-dependent effects of cumulative methylphenidate exposure on brain structure and symptoms |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Cohort | Psychiatry Clin Neurosci | Dual-tracer PET study of extended-release methylphenidate effects on DAT/NET binding in adult ADHD |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Review | J Atten Disord | Evolution of methylphenidate mechanism-of-action research, adult vs. juvenile brain |
| [20483462](https://pubmed.ncbi.nlm.nih.gov/20483462/) | 2010 | Cohort | Psychiatry Research | EEG coherence differences between good and poor methylphenidate responders in ADHD children |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Cohort | Clin EEG Neurosci | Quantitative EEG in childhood ADHD and learning disabilities |
| [18309764](https://pubmed.ncbi.nlm.nih.gov/18309764/) | 2007 | Review | Nutrition and Health | ADHD drug vs. nutrition treatment overview, including methylphenidate side effects |
| [11990715](https://pubmed.ncbi.nlm.nih.gov/11990715/) | 2002 | Animal model | Behavioural Pharmacology | SHRSP rat model of developmental disorder with/without methylphenidate |
| [11563573](https://pubmed.ncbi.nlm.nih.gov/11563573/) | 2001 | Review | American Family Physician | Evaluation and treatment of ADHD |
| [20556767](https://pubmed.ncbi.nlm.nih.gov/20556767/) | 2010 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Meditation therapies for ADHD |

*8 additional lower-priority publications (genetics, drug-interaction reviews, qualitative studies) exist in the source data and are omitted here.*

### Rank 4 — Dysthymic disorder

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24045603](https://pubmed.ncbi.nlm.nih.gov/24045603/) | 2013 | Cohort | Clinical Neuropharmacology | Effect of methylphenidate on mood in ADHD with comorbid subsyndromal depression |
| [9614599](https://pubmed.ncbi.nlm.nih.gov/9614599/) | 1998 | Case series | Depression and Anxiety | Psychostimulant augmentation of second-generation antidepressants |
| [14609500](https://pubmed.ncbi.nlm.nih.gov/14609500/) | 2003 | Observational | Current Psychiatry Reports | Effects of amphetamine/methylphenidate on interpersonal perception of mood |
| [1351794](https://pubmed.ncbi.nlm.nih.gov/1351794/) | 1992 | Review | Clinical Therapeutics | Adult ADHD overview |
| [2225800](https://pubmed.ncbi.nlm.nih.gov/2225800/) | 1990 | Cohort | Comprehensive Psychiatry | Clinical/demographic profile of adults with residual-state ADHD |
| [16802263](https://pubmed.ncbi.nlm.nih.gov/16802263/) | 2006 | Review | Psychiatrische Praxis | Diagnosis/treatment of adult ADHD with comorbid drug addiction |

---

## Saudi Arabia Market Information

Methylphenidate is currently **not marketed** in Saudi Arabia under this evidence pack (0 authorizations, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — DG001 flags this as a **blocking** gap for the safety pre-assessment stage.)

---

## Conclusion and Next Steps

**Rank 1 (Faciodigitogenital syndrome) — Decision: Hold**
**Rationale:** No mechanistic plausibility and zero clinical/literature evidence; the TxGNN score reflects a graph-relation artifact, not a biologically grounded signal.
**To proceed:** Independent mechanistic or preclinical rationale would be required before any further investment; not recommended for active pursuit.

**Rank 2 (Chondromyxoid fibroma) — Decision: Hold**
**Rationale:** Same as above — no mechanistic link, no supporting evidence.
**To proceed:** Not recommended for active pursuit absent new evidence.

**Rank 3 (Specific developmental disorder) — Decision: Proceed with Guardrails**
**Rationale:** Strong trial (16) and literature (18) base with direct mechanistic support (DAT/NET inhibition), evidence level L1. However, the content of this evidence is essentially ADHD — methylphenidate's known primary indication — while the source record shows `original_indications` as empty and `original_moa` as a data gap.
**To proceed:**
- Verify with DrugBank/TFDA whether ADHD is already methylphenidate's approved indication before treating this as a "new" repurposing candidate (remediation for DG002)
- If confirmed as the existing indication, reclassify this pack entry rather than advancing it through the repurposing pipeline
- If genuinely unlisted for the target market, proceed with standard regulatory-filing evidence review

**Rank 4 (Dysthymic disorder) — Decision: Research Question**
**Rationale:** Plausible but indirect mechanistic hypothesis (stimulant augmentation of mood), supported only by low-tier literature (case series, observational, reviews) with no clinical trials.
**To proceed:**
- Targeted literature review or preclinical work on stimulant augmentation in dysthymia specifically
- Consider as a hypothesis-generating signal only, not for near-term clinical development

**Cross-cutting gap:** TFDA package insert warnings/contraindications (DG001, blocking) and detailed MOA (DG002, high) must be resolved before any candidate in this pack can advance to a formal safety pre-assessment (S1).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

