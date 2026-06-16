---
layout: default
title: Dapoxetine
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 3
---

# Dapoxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# DAPOXETINE: From Premature Ejaculation to Migraine Disorder

## One-Sentence Summary

Dapoxetine is a short-acting selective serotonin reuptake inhibitor (SSRI) approved in multiple countries for the on-demand treatment of premature ejaculation (PE) in adult men.
The TxGNN model predicts it may have activity in **Migraine Disorder**, with **0 clinical trials** and **2 publications** (both narrative/observational in nature) currently supporting this direction.
Given the absence of direct clinical evidence and a fundamental pharmacokinetic barrier for this indication, the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Premature ejaculation (on-demand treatment) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, dapoxetine is a selective serotonin reuptake inhibitor (SSRI), uniquely engineered for on-demand dosing due to its ultra-short half-life (t½ ≈ 1.3 hours). It inhibits the serotonin transporter (SERT), producing a rapid, transient increase in synaptic serotonin — a pharmacokinetic profile that is precisely suited to premature ejaculation, where immediate central serotonergic enhancement delays ejaculation. Its efficacy in this indication is clinically well-established.

The TxGNN model infers a connection to migraine disorder via the shared serotonergic pathway. Serotonin (5-HT) is central to migraine pathophysiology: triptans — the first-line acute therapy — act as 5-HT1B/1D receptor agonists, and broader dysregulation of serotonergic tone has long been associated with migraine susceptibility. Other SSRIs (e.g., fluoxetine, venlafaxine) have been explored for migraine prevention. At the class level, SERT inhibition and serotonin modulation represent a plausible, if indirect, mechanistic bridge between dapoxetine and migraine biology.

However, the pharmacokinetic mismatch is critical and likely disqualifying: dapoxetine's t½ ≈ 1.3 h makes it incapable of maintaining the stable plasma concentrations required for migraine prophylaxis. For acute migraine treatment, SERT inhibition operates through a fundamentally different receptor pathway than triptans and has not demonstrated comparable efficacy. Additionally, existing evidence for SSRIs in migraine prevention is mixed, and none of that data can be directly extrapolated to dapoxetine. This represents the primary barrier to repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dapoxetine in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Narrative Review | Current Neuropharmacology | Broad review of off-label SSRI applications; mentions migraine as one potential off-label use for the SSRI class — does not evaluate dapoxetine specifically for migraine |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Observational Study | Urologia | Compliance study of dapoxetine in premature ejaculation; confirms SSRI mechanism and tolerability profile — no migraine-related data |

---

## Saudi Arabia Market Information

Dapoxetine currently holds no registered marketing authorizations in this market. No product-level authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials and no direct literature evidence support the use of dapoxetine in migraine disorder; the only indirect support derives from a general SSRI class review. More critically, dapoxetine's ultra-short half-life (t½ ≈ 1.3 h) presents a fundamental pharmacokinetic barrier to both preventive and acute migraine therapy, and this limitation has not been addressed in any published research program.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) — currently a data gap requiring DrugBank API query (DG002)
- Package insert safety data: key warnings and contraindications (DG001)
- Dedicated preclinical or mechanistic studies specifically evaluating dapoxetine in migraine models (required to progress beyond L4)
- A credible formulation strategy to overcome the pharmacokinetic barrier (e.g., modified-release formulation achieving sustained plasma exposure)
- Drug interaction profile for commonly co-prescribed migraine therapies (triptans, NSAIDs, anticonvulsants)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

