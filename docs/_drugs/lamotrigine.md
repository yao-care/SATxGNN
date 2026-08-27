---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Lamotrigine is a sodium-channel-blocking anticonvulsant established for epilepsy and bipolar disorder maintenance therapy.
> The TxGNN model predicts it may be effective for **Trigeminal Neuralgia**,
> with **4 clinical trials** (including a completed Phase 2/3 head-to-head trial and a placebo-controlled RCT) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial/generalized seizures) and bipolar disorder — per literature evidence in this pack; not verified against a Saudi regulatory source, as the drug is not currently marketed there |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The TxGNN model's single highest-scoring prediction for lamotrigine is actually "trigeminal nerve neoplasm" (99.97%), but this candidate has zero clinical trials, zero relevant literature, and its own rationale flags it as a likely ontology mismatch (neuralgia vs. neoplasm confusion in the underlying disease vocabulary) — it is scored L5/Hold. The second-ranked prediction, **trigeminal neuralgia** (99.89%), has a materially stronger evidence base and is the focus of this report.

Detailed formal mechanism-of-action documentation for lamotrigine was not retrievable in this evidence pack (DrugBank query gap, DG002). Based on the information available across the supporting literature, lamotrigine is a voltage-gated sodium-channel blocker that suppresses abnormal neuronal firing and excessive glutamate release — the same broad mechanistic class as carbamazepine and oxcarbazepine, the first-line drugs for trigeminal neuralgia (TN).

This mechanistic overlap explains why lamotrigine has already been trialed clinically as an add-on or alternative TN therapy: a completed Phase 2/3 study (NCT00913107) compared it head-to-head with carbamazepine, and a separate placebo-controlled add-on study (NCT00203229) tested Lamictal specifically in TN patients. Multiple published reviews and a case report of combination therapy (pregabalin + lamotrigine) in refractory TN reinforce the biological plausibility, even though lamotrigine remains an off-label option relative to carbamazepine/oxcarbazepine in most guidelines.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Direct comparison of lamotrigine vs. carbamazepine for efficacy and safety in trigeminal neuralgia (TGN). |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (lamotrigine) in patients with trigeminal neuralgia (tic douloureux). |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI-based evaluation of lamotrigine's effect on neuropathic facial pain/neuralgia; mechanistic, small-sample, not a primary efficacy endpoint study. |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Compares carbamazepine vs. oxcarbazepine (first-choice TN drugs); does not include a lamotrigine arm — indirect/competitor-drug relevance only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative study | Journal of the Chinese Medical Association | Direct comparison of lamotrigine (LTG) vs. carbamazepine (CBZ) for efficacy and side-effect profile in TN patients. |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on TN management, covering pharmacological options across specialties. |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Multiple Sclerosis and Related Disorders | Refractory TN in an MS patient successfully treated with combination therapy (pregabalin + lamotrigine) after carbamazepine intolerance. |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka (Neurological Surgery) | Reviews TN pharmacotherapy; notes lamotrigine (along with baclofen, IV lidocaine, botulinum toxin) as an effective off-label alternative to carbamazepine. |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Evidence-based review of current and innovative pharmacological options for typical and atypical TN. |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drugs used for TN, evaluating efficacy and side effects across prior reviews and meta-analyses. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on TN pharmacotherapy; discusses limitations of carbamazepine/oxcarbazepine and emerging alternatives. |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical guide to TN diagnosis, subclassification, and medical/surgical treatment decision-making. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of TN pathophysiology through to pharmacological treatment approaches. |
| [34003166](https://pubmed.ncbi.nlm.nih.gov/34003166/) | 2021 | Review | Neurology India | Overview of medical management strategies for trigeminal neuralgia. |

---

## Saudi Arabia Market Information

Lamotrigine currently holds no marketing authorization in Saudi Arabia — 0 licenses are on file and market status is recorded as **not marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not retrievable for this candidate — TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap, DG001, that must be resolved before any safety pre-evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed lamotrigine-specific studies (a placebo-controlled add-on trial and a Phase 2/3 head-to-head comparison with carbamazepine) plus guideline-level literature support biological plausibility and clinical precedent for lamotrigine in trigeminal neuralgia. However, the drug is unmarketed in Saudi Arabia and safety documentation is currently a blocking gap, so guardrails are required before advancing.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism-of-action documentation via DrugBank (currently a High-severity data gap)
- Drug-drug interaction data (current query status: not found)
- A Saudi regulatory pathway assessment, since lamotrigine has no existing marketing authorization there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

