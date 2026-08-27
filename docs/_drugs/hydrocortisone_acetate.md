---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate: From Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate is a corticosteroid (glucocorticoid); the evidence pack does not contain a documented original indication or mechanism-of-action record for this specific entry (data gap). The TxGNN model predicts it may be effective for **Alopecia Areata**, and this is currently supported by **1 completed Phase 3 clinical trial** and **2 publications**, reflecting reinforcement of an already-established corticosteroid use in this condition rather than a novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license or indication text on file — data gap) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 (1 completed Phase 3 RCT) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug entry (data gap DG002). Based on known pharmacological classification, hydrocortisone acetate is a corticosteroid (glucocorticoid); its anti-inflammatory and immunosuppressive effects — including suppression of local T-lymphocyte infiltration — are pharmacologically well established for this drug class.

Alopecia areata is itself an autoimmune, T-cell-mediated form of hair loss. Topical and intralesional corticosteroids are already a standard-of-care treatment option for alopecia areata in clinical practice. This means the TxGNN prediction is not proposing a novel mechanistic hypothesis, but rather reinforces an existing, clinically established use — which is corroborated by the completed Phase 3 trial and older case-series/review literature identified below.

No original indication data was returned for this drug in the current evidence pack, so the relationship between the (unknown) original indication and alopecia areata cannot be characterized. This should be treated as a data completeness gap rather than a negative finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized controlled trial comparing clobetasol propionate 0.05% cream vs. hydrocortisone 1% cream in children with alopecia areata; hydrocortisone 1% cream used directly as the active comparator arm, providing direct (not merely mechanistic) evidence for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Case series | Przeglad dermatologiczny | Treatment of severe forms of alopecia areata using intralesional subcutaneous injections of hydrocortisone acetate suspension. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | General review of topical corticosteroid therapy in dermatology; notes hydrocortisone acetate's anti-inflammatory effect as a benchmark comparator for newer topical corticosteroids. |

---

## Saudi Arabia Market Information

No marketing authorizations are currently on file — the drug is not marketed in Saudi Arabia (0 authorizations recorded).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in the evidence pack — DG001, Blocking.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT directly supports hydrocortisone 1% cream's use in alopecia areata, consistent with corticosteroids' established role in this condition, but the drug is not currently marketed in Saudi Arabia and critical safety documentation is missing.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Mechanism of action documentation from DrugBank (DG002, High)
- Drug interaction (DDI) data, currently not found
- Saudi Arabia market authorization pathway assessment, given current "not marketed" status
- Route/formulation compatibility check for the alopecia areata indication (topical vs. intralesional use)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

