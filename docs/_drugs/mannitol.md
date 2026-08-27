---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# MANNITOL: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a hyperosmotic agent classically used as an osmotic diuretic (e.g., for cerebral edema/raised intracranial pressure, oliguria); no approved-indication text is present in this evidence pack. The TxGNN model predicts it may be relevant to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this is currently supported by **0 clinical trials** and only **1 publication** — a general review on hyponatremia pitfalls that does not discuss mannitol specifically. Evidence is model-prediction-only at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications` empty, MOA marked as Data Gap). Mannitol is generically known as an osmotic diuretic (cerebral edema/↑ICP, oliguria) — general pharmacology knowledge, not sourced from this evidence pack |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% (rank 1047) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for mannitol in this evidence pack (marked as a Data Gap). Based on general pharmacological knowledge, mannitol is a hyperosmotic agent that produces osmotic diuresis; this property means it can influence serum sodium and free-water balance, which is mechanistically adjacent to the pathophysiology of NSIAD (an inappropriate antidiuresis/hyponatremia disorder).

However, the connection identified in this evidence pack is weak. The single literature reference (PMID 26706473) is a general review of common pitfalls in evaluating hyponatremic patients and does **not** specifically discuss mannitol as a therapy for NSIAD. The repurposing rationale itself flags that the direction of effect is unclear: mannitol's osmotic diuretic action could theoretically influence serum sodium concentration, but whether this would help (treat) or worsen NSIAD is not established, and no drug-specific evidence exists.

Given the absence of any clinical trials, any disease-specific mechanistic literature, or drug-specific studies, this prediction should be regarded as a model-generated hypothesis only, not a clinically supported association.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Reviews common pitfalls in diagnosing/managing hyponatremia in hospitalized patients; general guidance on avoiding under- or over-treatment. Does not specifically discuss mannitol or its use in NSIAD. |

## Saudi Arabia Market Information

Mannitol is not currently marketed in Saudi Arabia per this evidence pack (0 authorizations, no license records available).

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and drug interactions — are marked as data gaps; TFDA-equivalent package insert warnings could not be retrieved, which is flagged as a **Blocking** data gap for safety pre-screening.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with no clinical trials and a single, non-specific review article whose relevance to mannitol is indirect and whose direction of effect (therapeutic vs. harmful) is unclear. In addition, a **Blocking** data gap on TFDA-equivalent safety warnings/contraindications currently prevents even an initial (S1) safety screen.

**To proceed, the following is needed:**
- TFDA/Saudi package insert warnings and contraindications (Blocking gap — required before any safety pre-screening)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Drug-specific preclinical or mechanistic studies linking mannitol to NSIAD or serum sodium regulation
- Clarification of directionality — whether mannitol's osmotic effect would ameliorate or exacerbate NSIAD-related hyponatremia — before any clinical hypothesis testing is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

