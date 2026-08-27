---
layout: default
title: Gadoxetic Acid
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Gadoxetic Acid
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

# Gadoxetic Acid: From Liver MRI Contrast Imaging to Hyperthyroidism

## One-Sentence Summary

Gadoxetic acid (Gd-EOB-DTPA) is a hepatocyte-specific MRI contrast agent, not a therapeutic drug — it enhances liver imaging via OATP1B1/1B3-mediated hepatocyte uptake rather than exerting pharmacological activity against a disease target. The TxGNN model's top-ranked prediction is **Hyperthyroidism**, with a 99.89% similarity score, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic rationale explicitly finds no plausible biological link — indicating this is most likely a graph-embedding artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liver-specific MRI contrast enhancement (hepatobiliary imaging); no discrete disease indication recorded in this evidence pack |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.89% (global candidate rank 2480) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed pharmacological mechanism-of-action data for gadoxetic acid is not available from DrugBank in this evidence pack. Based on what is known, gadoxetic acid (Gd-EOB-DTPA) is a gadolinium-based contrast agent taken up specifically by hepatocytes via the OATP1B1/1B3 transporters, producing a T1-shortening effect that enhances liver lesion visualization on MRI. It has no established pharmacodynamic activity against any disease target — it is a diagnostic imaging agent, not a treatment.

Because gadoxetic acid's only known biological activity is transporter-mediated hepatocyte uptake for imaging contrast, there is no plausible pharmacological pathway connecting it to hyperthyroidism, a condition driven by thyroid hormone synthesis, receptor signaling, or autoimmune thyroid stimulation. The evidence pack's own mechanistic rationale for this prediction states explicitly that there is no known receptor, enzyme, or signaling pathway linking gadoxetic acid to hyperthyroidism, and attributes the score to embedding-space similarity noise.

This pattern is not isolated: ranks 2–9 of this candidate list show the same signature — high similarity scores, zero supporting trials or literature, and explicitly disclaimed mechanisms — including two veterinary-only conditions (infectious bovine rhinotracheitis, malignant catarrh) that cannot apply to a human drug. The one candidate with any literature support, thrombotic disease (rank 10), is backed only by two papers describing gadoxetic acid-enhanced MRI as a *diagnostic* tool for distinguishing tumor thrombus from bland thrombus and predicting post-TACE liver failure — not therapeutic evidence of anti-thrombotic activity. Taken together, this candidate set does not support a credible repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Gadoxetic acid is not currently marketed in Saudi Arabia; no drug authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (hyperthyroidism) is Evidence Level L5 (model prediction only) with no clinical, mechanistic, or literature support, and the evidence pack's own rationale explicitly rules out a plausible biological mechanism. Gadoxetic acid's known pharmacology — a hepatocyte-uptake imaging contrast agent — is inconsistent with any of the top-10 predicted indications.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/SFDA package insert — warnings/contraindications) before any S1 safety screening can occur
- Resolve high-priority data gap DG002 (confirmed MOA from DrugBank) to properly evaluate mechanistic plausibility
- Independent pharmacological or preclinical evidence linking gadoxetic acid to thyroid pathophysiology before this candidate advances past S0
- If pursued further, treat this as a low-priority/exploratory signal only — not a candidate for near-term clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

