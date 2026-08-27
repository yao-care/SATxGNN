---
layout: default
title: Hydroquinone
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 4
---

# Hydroquinone
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

# Hydroquinone: From Hyperpigmentation/Melasma to Seborrheic Keratosis

## One-Sentence Summary

Hydroquinone has no formally registered indication in Saudi Arabia (not currently marketed), but the evidence pack itself documents its established use as a topical tyrosinase-inhibiting depigmenting agent for hyperpigmentation and melasma. The TxGNN model predicts it may be effective for **seborrheic keratosis**, but this is currently supported only by **0 clinical trials** and **2 literature items** (one observational cohort study, one review), neither of which studied the disease directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in Saudi Arabia (未上市, 0 authorizations); evidence pack indicates established use as a topical depigmenting agent for hyperpigmentation/melasma |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for hydroquinone is not currently available in this evidence pack (data gap, High severity). However, based on the trial and literature evidence gathered, hydroquinone is a well-characterized tyrosinase inhibitor that reduces melanin synthesis, and it is used clinically as a topical skin-lightening agent for hyperpigmentation and melasma — this is corroborated by multiple trials in the pack that use "4% hydroquinone" as an active comparator for melasma (e.g., NCT05969587, NCT00616239, NCT02977507).

Seborrheic keratosis, particularly its dermatosis papulosa nigra (DPN) variant common in darker-skinned patients, frequently presents with visibly hyperpigmented lesions. This creates a superficial mechanistic overlap with hydroquinone's pigment-suppressing action, which is the basis of the TxGNN association.

However, the core pathology of seborrheic keratosis is benign keratinocyte hyperproliferation — not a melanocyte-driven process. Hydroquinone's tyrosinase inhibition can at most address secondary pigmentation of the lesion (a cosmetic effect) and does not target the proliferative epidermal pathology itself. This is therefore a symptomatic/cosmetic association rather than a disease-modifying mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort | J Plast Reconstr Aesthet Surg | Prospective observational study developing a combination treatment algorithm for overlapping facial pigmentary disorders in Asian patients; not specific to seborrheic keratosis or hydroquinone monotherapy. |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | J Drugs Dermatol | Review of treatment options for dermatosis papulosa nigra (histologically related to seborrheic keratosis); focuses on physical removal techniques for aesthetic concerns, not pharmacologic (hydroquinone) therapy. |

---

## Saudi Arabia Market Information

Hydroquinone currently has no marketing authorization in Saudi Arabia (未上市, 0 licenses on file).

---

## Other Predicted Indications (Lower Priority, Not Advanced)

Three additional TxGNN-predicted indications were evaluated but are not recommended for further work:

- **Vulvar inverted follicular keratosis** (score 99.64%) — L5, no clinical trials or literature at all; purely a model-level association with no known pathological link to tyrosinase inhibition.
- **Exanthem** (score 99.42%) — 7 clinical trials and 1 literature item were retrieved, but every trial actually concerns melasma/hyperpigmentation (not exanthem), suggesting a likely TxGNN disease-ontology mapping error rather than a genuine signal.
- **Lichen disease** (score 99.07%) — L4, literature concerns lichen planus pigmentosus, where the actual reported treatment is topical tacrolimus, not hydroquinone; the mechanistic link is weak.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (seborrheic keratosis) is supported only by an observational cohort study and a review of an adjacent condition (DPN), with no disease-specific clinical trials, and the proposed mechanism addresses only secondary pigmentation rather than the disease's core proliferative pathology. Combined with a Blocking-severity data gap (no TFDA/SFDA package insert available for safety screening) and the drug's current non-marketed status in Saudi Arabia, the evidence does not support advancing beyond a research question at this time.

**To proceed, the following is needed:**
- Official SFDA/TFDA package insert (warnings, contraindications, DDI) to complete the S1 safety screen (resolves DG001)
- DrugBank/pharmacology MOA data to properly assess mechanistic plausibility (resolves DG002)
- Disease-specific studies (ideally RCTs) of hydroquinone or class agents in seborrheic keratosis or DPN
- Re-verification of the "exanthem" TxGNN mapping, given the strong mismatch between the predicted disease label and the retrieved trial evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

