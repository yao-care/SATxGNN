---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 613
evidence_level: L5
indication_count: 4
---

# Tetracycline
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

Using the report template supplied in this turn (no additional skill needed — it's a fully-specified document-generation task). Note: per the format rules, "Predicted New Indication" = `predicted_indications[0]`, which in this Evidence Pack is **punctate epithelial keratoconjunctivitis** (rank 1 by TxGNN score) — not chronic rhinosinusitis (rank 3), which actually has the stronger evidence base. I flag that discrepancy in the Next Steps section rather than silently substituting it.

---

# Tetracycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Tetracycline is a broad-spectrum tetracycline-class antibiotic classically used against susceptible bacterial infections, including chlamydial infections.
> The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
> but this direction is currently supported by only **1 historical case report** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Saudi Arabia regulatory data (product not marketed locally); tetracycline is classically indicated for susceptible bacterial infections |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tetracycline is a tetracycline-class antibiotic whose efficacy against susceptible bacterial infections (including *Chlamydia trachomatis*) is well established through inhibition of bacterial protein synthesis; mechanistically this class has long been used for chlamydial ocular and follicular conjunctivitis.

However, the mechanistic link supplied for this specific prediction is indirect. The single supporting publication (PMID 1424659) describes two patients whose punctate epithelial keratitis **developed after** their underlying chlamydial follicular conjunctivitis had already resolved with oral tetracycline or doxycycline — it is an observational account of a post-infectious complication, not a study evaluating tetracycline as treatment for the keratitis itself. The TxGNN association should therefore be read as a hypothesis generated from disease co-occurrence in the literature rather than as direct treatment evidence.

Given the absence of MOA confirmation, absence of dedicated clinical trials, and the observational (non-interventional) nature of the sole literature source, mechanistic plausibility for this indication remains unconfirmed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients treated with oral tetracycline/doxycycline for chlamydial follicular conjunctivitis subsequently developed recurrent, bilateral punctate epithelial keratitis after the conjunctivitis resolved; describes the post-infectious corneal complication, not a tetracycline treatment effect on keratitis |

---

## Saudi Arabia Market Information

Tetracycline is not currently marketed in Saudi Arabia — no product authorizations are on record in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA package insert retrieval is flagged as a **blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is supported by only one 1992 case report describing an association (post-infectious keratitis following treated chlamydial conjunctivitis), not a demonstrated treatment effect, and by zero registered clinical trials. A blocking data gap on official safety/contraindication information (DG001) also prevents this candidate from clearing initial S1 safety screening, and the drug has no current market presence in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data (DG002)
- A dedicated interventional or observational study evaluating tetracycline (or a class representative) specifically for punctate epithelial keratoconjunctivitis / post-chlamydial keratitis, rather than inference from an unrelated case report
- Drug interaction (DDI) database confirmation (currently "not_found")
- Note: among the four TxGNN-predicted indications in this pack, **chronic rhinosinusitis** (rank 3) has a substantially stronger evidence base (4 clinical trials including Phase 3, 20 publications including 2 systematic reviews, evidence level L2) and may warrant separate, prioritized evaluation as an alternative repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

