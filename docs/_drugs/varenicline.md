---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
---

# Varenicline
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

Using the drug-repurposing evidence pack you provided, here is the evaluation report for VARENICLINE.

---

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

> Varenicline is a nicotinic acetylcholine receptor (nAChR) partial agonist originally developed and used for smoking cessation (tobacco dependence).
> The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported by **0 clinical trials** and only **1 publication** — a cardiac arrest adverse-event case report, not an efficacy study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation / tobacco dependence (inferred from literature evidence in this pack; no formal Taiwan/KSA license record available) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for varenicline is flagged as a data gap in this evidence pack (DG002, High severity). Based on information available in the supporting literature, varenicline acts as a partial agonist at α4β2 nicotinic acetylcholine receptors and a full agonist at α7 nAChRs — this is the pharmacology underlying its approved use in smoking cessation, where it reduces nicotine craving and withdrawal symptoms.

However, the repurposing rationale for this specific prediction is explicit that **no established mechanistic link exists** between nAChR partial agonism and migraine pathophysiology (e.g., the trigeminovascular system or CGRP pathway). The single literature record associated with this indication is not an efficacy study at all — it is a case report of cardiac arrest following varenicline use, which is an adverse-event signal rather than evidence of therapeutic benefit.

In short, the high TxGNN score (99.92%, rank 1913) reflects a model-generated association, not corroborating clinical or mechanistic evidence. The only real-world data point associated with this candidate points toward a safety concern rather than a treatment opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case Report | Therapie | Case report of cardiac arrest associated with varenicline use — an adverse-event report, not evidence of efficacy in migraine |

---

## Saudi Arabia Market Information

Varenicline is currently **not marketed** and has no license records on file (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on the TxGNN model score with no supporting clinical trials and no genuine efficacy literature; the sole associated publication reports a serious cardiac adverse event, which raises a safety flag rather than supporting therapeutic potential. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data confirming or refuting any plausible nAChR–migraine pathway link
- TFDA/regulatory package insert data on warnings, contraindications, and cardiovascular risk (currently blocking — DG001)
- Preclinical or mechanistic studies specifically evaluating varenicline in migraine models
- Systematic review of the cardiac safety signal (e.g., PMID 19585710) before any further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

