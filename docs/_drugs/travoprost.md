---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost is a prostaglandin F2α analog (FP receptor agonist) known from its product class as an ophthalmic agent for glaucoma and ocular hypertension; this evidence pack does not contain a confirmed original indication or MOA record for the drug.
> The TxGNN model predicts potential efficacy for **Visceral Calciphylaxis**, but this is currently a **pure model prediction with 0 clinical trials and 0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` empty). Known from drug class: glaucoma / ocular hypertension (FP receptor agonist, prostaglandin analog) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% (rank 6 among predictions) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa` = Data Gap). Based on known product-class information, travoprost is a prostaglandin F2α analog and FP prostanoid receptor agonist, whose proven efficacy is in lowering intraocular pressure (IOP) via increased uveoscleral outflow in glaucoma and ocular hypertension — an indication not itself confirmed by structured data in this pack.

The proposed link to visceral calciphylaxis rests entirely on a theoretical extension of FP-receptor signaling to vascular calcification regulation. No clinical, preclinical, or literature evidence in this pack supports this pathway — the rationale explicitly notes it is "purely theoretical, with no supporting data." Given that travoprost is administered topically as an ophthalmic solution with minimal systemic absorption, a plausible mechanistic path to a systemic vascular calcification disorder is not established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Travoprost is not marketed in Saudi Arabia — no product authorizations are on record (`total_licenses` = 0, `licenses` empty).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings/contraindications data is flagged as a **Blocking** data gap (DG001) — this prevents a formal S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (visceral calciphylaxis) has an L5 evidence level — a TxGNN score alone, with zero clinical trials or literature support — and a Blocking data gap on TFDA warnings/contraindications prevents even a baseline safety assessment. There is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings, precautions, contraindications) — resolves Blocking gap DG001
- Confirmed mechanism of action (MOA) data via DrugBank — resolves High-severity gap DG002
- Confirmed original indication and regulatory approval history for travoprost
- Preclinical or mechanistic evidence connecting FP receptor signaling to vascular calcification pathways relevant to visceral calciphylaxis
- If pursuing a vascular-disease angle instead (rank 5 candidate, L4 evidence, 15 trials/20 publications identified but mostly graded as low relevance — ocular hyperemia/side-effect studies rather than therapeutic vascular disease evidence), a dedicated relevance re-grading of that evidence set would be required before advancing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

