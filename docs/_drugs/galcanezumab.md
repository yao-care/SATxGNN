---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor II Deficiency

## One-Sentence Summary

Galcanezumab is a monoclonal antibody targeting CGRP (calcitonin gene-related peptide), a mechanism publicly known to be used for migraine prevention — though this evidence pack does not itself contain confirmed original-indication data. The TxGNN model predicts potential effectiveness for **Heparin Cofactor II Deficiency**, a rare inherited coagulation disorder, but this direction is currently supported **only by the model score (99.50%)** — zero clinical trials and zero publications were found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not included in this evidence pack; per public drug labeling, galcanezumab is indicated for migraine prevention |
| Predicted New Indication | Heparin cofactor II deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack. Based on publicly known pharmacology, galcanezumab is a humanized monoclonal antibody that binds CGRP and blocks its receptor signaling, and its efficacy in migraine prevention is well established.

However, the repurposing rationale supplied with this prediction is itself skeptical: it states there is **no known physiological or regulatory relationship** between the CGRP signaling pathway and heparin cofactor II (a serine protease inhibitor that suppresses thrombin) or the related coagulation-factor disorders in ranks 2 and 3 (antithrombin deficiency, factor V excess). These are inherited, gene-driven coagulation abnormalities (e.g., SERPINC1 mutations), a disease category mechanistically distant from a neuropeptide-blocking antibody.

The high TxGNN score (~99.4–99.5%) therefore reflects graph-neural-network link prediction only, not biological or clinical evidence. Without a plausible mechanistic bridge and without any trials or literature, this prediction should be treated as hypothesis-generating rather than actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other TxGNN Predictions (Same Data Pull)

Two additional candidates were generated in this batch, both similarly unsupported:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials/Literature |
|------|----------------------|-------------|-----------------|--------------------|
| 2 | Antithrombin deficiency type 2 | 99.41% | L5 | None found |
| 3 | Factor V excess with spontaneous thrombosis | 99.41% | L5 | None found |

All three predictions cluster around the same score range and share the same limitation: no mechanistic, trial, or literature support.

---

## Saudi Arabia Market Information

Galcanezumab is not currently marketed in Saudi Arabia — no authorization records exist in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications are ultra-rare, genetically-driven coagulation disorders with no clinical trials, no literature, and no plausible mechanistic link to galcanezumab's known CGRP-blocking action — the evidence pack's own analysis reaches this same conclusion. A high model score alone (L5) does not justify advancing past initial screening.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently flagged as blocking/high-severity data gaps; TFDA package insert warnings and contraindications are unresolved)
- Any preclinical or mechanistic study exploring CGRP pathway involvement in coagulation-factor regulation, to justify the prediction beyond the model score
- Regulatory status confirmation and market-entry pathway assessment for Saudi Arabia, since the drug is not currently marketed there
- DDI data (currently "not found") before any safety evaluation can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

