---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina Pectoris to Alopecia

## One-Sentence Summary

Isosorbide dinitrate is an organic nitrate (NO donor) vasodilator whose established clinical role — evident from its trial history in this Evidence Pack — is coronary artery disease/angina pectoris and heart failure. The TxGNN model's top-ranked prediction for this drug is **Alopecia**, but this direction currently has **0 clinical trials** and **0 publications** supporting it, and the mechanistic rationale is unconfirmed extrapolation rather than documented evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina Pectoris / Coronary Artery Disease (established vasodilator use — inferred from trial evidence in this pack; not sourced from a formal label, see note below) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** The Evidence Pack's `original_indications` and `taiwan_regulatory.licenses` fields are both empty (drug not marketed in this jurisdiction, and DG001 flags TFDA/SFDA label data as a Blocking gap). The angina/coronary artery disease use stated above is drawn from other parts of this same Evidence Pack (the rank-6 "vascular disease" candidate's trial and literature evidence), not from a formal regulatory source — it should be independently verified before use in any regulatory-facing document.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is flagged as a Data Gap (DG002) in this pack. However, other candidates within the same bundle document that isosorbide dinitrate is a nitric oxide (NO) donor that relaxes vascular smooth muscle via the cGMP pathway — the classical pharmacological basis for its use in coronary artery disease and angina pectoris (see the rank-6 "vascular disease" rationale, supported by a completed Phase 3 trial).

For the alopecia prediction specifically, the proposed mechanism is that vasodilation could theoretically increase follicular blood flow, by loose analogy to minoxidil (a different vasodilator with an established topical hair-growth indication). This is a plausible-sounding but **unverified** hypothesis — there is no clinical or preclinical data in this pack testing isosorbide dinitrate for hair growth.

A notable caution: this same TxGNN run also ranks three other hair-related conditions highly for this drug — congenital hypotrichosis milia (rank 2), hypotrichosis simplex of the scalp (rank 3), diffuse alopecia areata (rank 5), and even the *opposite* phenotype, hypertrichosis (rank 7). All carry zero supporting evidence. This clustering pattern is more consistent with a "hair-related disease" artifact in the model's embedding space than with a genuine, differentiated pharmacological signal — a concern the Evidence Pack's own rationale text for the hypertrichosis candidate raises explicitly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction has zero clinical trials, zero publications, and a mechanistic link that is speculative analogy rather than tested pharmacology (L5, S0). It also co-occurs with a cluster of other unsupported hair-disease predictions for the same drug, raising the possibility of model noise rather than true signal.

**To proceed, the following is needed:**
- Preclinical evidence (e.g., follicular blood flow / dermal penetration studies) testing whether systemic or topical isosorbide dinitrate has any effect on hair growth, before any clinical hypothesis is credible
- Resolution of DG001 (TFDA/SFDA label warnings/contraindications) and DG002 (MOA documentation), both currently blocking/high-severity gaps
- Clarification of whether the "hair-related disease" cluster in this drug's TxGNN output reflects a real biological signal or an embedding-space artifact, before investing further in any candidate in that cluster

**Separately worth flagging:** within this same bundle, the rank-6 "vascular disease" candidate has materially stronger evidence — a completed Phase 3 trial (ACIP) plus multiple RCTs/cohort studies, evidence level L1, decision stage S3, recommendation "Proceed with Guardrails" — consistent with isosorbide dinitrate's known antianginal/vasodilator pharmacology. If the goal is to identify a viable repurposing candidate for this drug rather than to evaluate the single top TxGNN score, that candidate warrants review ahead of alopecia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

