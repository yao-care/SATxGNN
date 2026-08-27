---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X

## One-Sentence Summary

Mecasermin is recombinant human IGF-1, historically used for severe primary IGF-1 deficiency (per the mechanistic rationale on file; no formal indication record exists in this evidence pack). The TxGNN model's top-ranked prediction is **Monosomy X (Turner syndrome)**, but currently **no clinical trials** and **no published literature** support this direction — the prediction rests on model score alone. Four other candidate indications in this evidence pack show the same pattern (score-only, zero trials/literature) and are noted below for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe Primary IGF-1 Deficiency (stated in rationale text only — not confirmed by a formal indication or license record in this pack) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for mecasermin in this evidence pack (flagged as a High-severity data gap, DG002). Mecasermin is known generally as recombinant human IGF-1, the downstream effector of the growth hormone (GH) axis.

The rationale supplied for this prediction notes that Monosomy X (Turner syndrome) commonly presents with growth failure, and a subset of patients respond poorly to GH therapy — since IGF-1 acts downstream of GH, there is an indirect mechanistic plausibility to using mecasermin in this population.

However, this plausibility is unsupported by any actual study: zero clinical trials and zero publications were found for mecasermin in Monosomy X. The prediction should be read as a hypothesis generated purely from the TxGNN knowledge graph, not as an evidence-backed signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Underlying data gap: TFDA/SFDA package insert warnings and contraindications are marked Blocking (DG001) — this drug cannot proceed to the S1 safety pre-screen until that data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — a TxGNN score with zero corroborating clinical trials or literature — and a Blocking data gap on package-insert safety data (DG001) independently prevents any safety pre-screen. This candidate cannot advance until both gaps close.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — Blocking gap, source: TFDA official site, PDF parse
- Confirmed original indication and mechanism of action for mecasermin — High-severity gap, source: DrugBank API
- At least preclinical or case-level evidence connecting mecasermin to Monosomy X before any trial-design discussion
- Note: the other 4 candidates in this pack (Wolman disease, GH insensitivity syndrome w/ immune dysregulation 2, esophageal varices with/without bleeding) carry the same L5/Hold status and the same blocking gaps — none are ready for independent evaluation either.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

