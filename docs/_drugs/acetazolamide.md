---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma / Altitude Sickness to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor with established uses in glaucoma, altitude sickness prevention, and epilepsy as an adjunct therapy; it is not currently registered in Saudi Arabia.
The TxGNN model ranks **Exercise-Induced Malignant Hyperthermia** as its top predicted new indication with a score of **99.95%**,
but **no clinical trials** and **no publications** currently support this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia (globally established uses: glaucoma, acute mountain sickness, epilepsy adjunct) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, acetazolamide inhibits carbonic anhydrase (CA) enzymes — particularly CA II and CA IV — suppressing bicarbonate reabsorption in the renal proximal tubule. This produces a mild metabolic acidosis and alters downstream ion transport. These effects underlie its proven benefits in reducing intraocular pressure (glaucoma), stimulating the hypoxic ventilatory response (altitude sickness), and modulating neuronal membrane excitability (epilepsy adjunct).

Exercise-induced malignant hyperthermia (EIMH) is a rare but life-threatening disorder — most commonly linked to RYR1 gene mutations — in which vigorous physical exertion triggers uncontrolled calcium release from the skeletal muscle sarcoplasmic reticulum, producing a catastrophic hypermetabolic crisis. The established first-line treatment is dantrolene, a direct RYR1 calcium channel inhibitor.

The mechanistic link between acetazolamide and EIMH is indirect and unsupported. While CA inhibition could theoretically buffer the metabolic acidosis that accompanies the hypermetabolic crisis, this represents a downstream supportive effect rather than addressing the core pathophysiology of uncontrolled RYR1-mediated calcium dysregulation. The high TxGNN prediction score likely reflects graph-level proximity in the disease-drug knowledge network — possibly via shared ontology nodes with conditions where acetazolamide demonstrably works (e.g., hypokalemic periodic paralysis, where it prevents membrane excitability attacks) — rather than a direct mechanistic route to EIMH.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Safety Signal from Adjacent Evidence:** Across the broader 10-indication evidence set, PMID [19653068](https://pubmed.ncbi.nlm.nih.gov/19653068/) (2009) documents acetazolamide-induced adynamic ileus (paralytic intestinal obstruction), and PMID [13659695](https://pubmed.ncbi.nlm.nih.gov/13659695/) (1959) reports similar drug-induced paralytic ileus. The proposed mechanism is electrolyte imbalance (hypokalemia) from CA inhibition leading to reduced intestinal motility. This adverse effect is relevant context for any critical-care application of acetazolamide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.95%), exercise-induced malignant hyperthermia requires direct RYR1/calcium channel-targeted intervention, and acetazolamide's carbonic anhydrase inhibition has no established mechanistic route to this pathway. There is zero clinical or preclinical evidence to justify advancing this indication.

**To proceed, the following is needed:**
- Preclinical studies in RYR1-mutant animal models to test whether CA inhibition has any measurable effect on hypermetabolic crisis severity
- Detailed MOA data from DrugBank (DB00819) to identify any indirect pathways not yet characterized
- Safety profile data from the SFDA package insert (currently not available in this data set)
- Expert consultation with neuromuscular disease and malignant hyperthermia specialists before any human study design

---

> **Broader Landscape Note:** Among all 10 TxGNN predictions evaluated for acetazolamide, **Cardiomyopathy (Rank 7, score 99.83%)** is by far the most evidence-supported candidate — with 3 active Phase 4 RCTs (largest: [NCT06166654](https://clinicaltrials.gov/study/NCT06166654), n=939) and 10 publications, qualifying as **L2 evidence** with a **"Proceed with Guardrails"** recommendation. The post-ADVOR-trial evidence base for acetazolamide augmenting loop-diuretic therapy in acute decompensated heart failure is the most actionable repurposing direction in this evidence set and warrants a dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

