---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Pimecrolimus (DrugBank DB00337) is a topical calcineurin inhibitor originally developed and used for **atopic dermatitis** (as documented in embedded trial records, e.g. Elidel® cream 1%).
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **1 completed Phase 2 clinical trial** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (mild-to-moderate) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured DrugBank mechanism-of-action field for pimecrolimus is currently a data gap (DG002). However, the literature evidence collected for this candidate independently describes the mechanism: pimecrolimus is an ascomycin-derivative **topical calcineurin inhibitor (TCI)** that selectively targets T cells and mast cells, inhibiting T-cell proliferation and the release of IL-2, IL-4, interferon-gamma and TNF-alpha, as well as mast cell degranulation (PMID 16033622). Unlike topical corticosteroids, it does not cause skin atrophy, which is why it was originally approved for long-term, sensitive-area use in atopic dermatitis.

Atopic dermatitis and seborrheic dermatitis are both chronic inflammatory dermatoses driven substantially by T-cell-mediated cytokine release, and seborrheic dermatitis additionally involves an inflammatory host response to *Malassezia* yeast. Because pimecrolimus's anti-inflammatory action is not antifungal-specific, its rationale in seborrheic dermatitis rests on suppressing the associated inflammatory/immune cascade rather than eradicating the organism — an approach already explored clinically as a non-steroidal alternative to corticosteroids and antifungals for facial and scalp involvement (PMID 31053034, "Off-label Uses of Topical Pimecrolimus").

This mechanistic plausibility is reinforced by direct clinical evidence: a dedicated Phase 2 RCT (NCT00403559) and multiple additional randomized/comparative studies and systematic reviews (below) have specifically tested pimecrolimus in seborrheic dermatitis, indicating this off-label use is already an active area of clinical practice rather than a purely computational prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | Randomized, double-blind, parallel-group, active-comparator-controlled exploratory study assessing Elidel (pimecrolimus) effectiveness for seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clinical and experimental dermatology | Randomized blinded trial comparing pimecrolimus 1% cream vs. sertaconazole 2% cream for facial seborrhoeic dermatitis |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | RCT (open, randomized, prospective, comparative) | Journal of dermatological treatment | Compared topical pimecrolimus 1% cream vs. ketoconazole 2% cream for seborrheic dermatitis |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic review of RCTs | Expert review of clinical pharmacology | Pimecrolimus 1% cream is well-tolerated and effective for seborrheic dermatitis, with comparable efficacy to corticosteroids/antimycotics |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic review | Cureus | Reviews efficacy/safety of pimecrolimus for facial seborrheic dermatitis among four established treatment categories (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | American journal of clinical dermatology | Systematic review of topical treatments, including pimecrolimus, for facial seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | Journal of drugs in dermatology | Overview of facial seborrheic dermatitis pathophysiology and therapeutic horizons, including calcineurin inhibitors |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | International journal of clinical practice | Describes pimecrolimus mechanism of action (T-cell/mast-cell targeting) and its use beyond atopic dermatitis |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Review | Journal of cutaneous medicine and surgery | Reviews off-label uses of topical pimecrolimus, focused on published RCTs across dermatologic conditions |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | Comparative study | Irish journal of medical science | Compares sertaconazole 2% cream vs. pimecrolimus 1% cream for seborrheic dermatitis treatment |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | American journal of clinical dermatology | Topical pimecrolimus 1% cream shown effective in resistant facial seborrheic dermatitis |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated Phase 2 RCT plus a consistent body of comparative studies and systematic reviews (evidence level L2) support pimecrolimus's efficacy in seborrheic dermatitis, and the proposed mechanism (TCI-mediated anti-inflammatory action) is biologically coherent with the original atopic dermatitis indication. However, the drug is currently **not marketed** in the target market (0 authorizations) and two drug-level data gaps remain unresolved.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, **Blocking** — required before safety pre-assessment/S1 can be completed)
- Structured DrugBank mechanism-of-action data (DG002, High priority — needed to formally validate the mechanistic linkage analysis)
- A drug-drug interaction (DDI) data source, since the current DDI query returned no results
- A market-entry/registration pathway assessment, since the product currently has zero local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

