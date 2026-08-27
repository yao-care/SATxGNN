---
layout: default
title: Paroxetine
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 1
---

# Paroxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Paroxetine: From Depression/Anxiety Disorders to Ohdo Syndrome and Variants

## One-Sentence Summary

Paroxetine is a selective serotonin reuptake inhibitor (SSRI), widely used for depression and anxiety disorders. The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**, a rare congenital chromatin-modifier disorder, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic link is biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression / anxiety disorders (SSRI antidepressant class; specific regulatory indication text not available in evidence pack) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known general pharmacology, paroxetine is an SSRI that inhibits the neuronal serotonin transporter (SLC6A4), and its efficacy in depression and anxiety disorders is well established.

Ohdo syndrome (including Say-Barber-Biesecker-Young-Simpson and other variants) is a rare congenital developmental disorder caused by mutations in the chromatin-modifying enzymes KAT6A/KAT6B, presenting with intellectual disability, blepharophimosis, and skeletal/cardiac anomalies. This pathology involves chromatin acetylation machinery, which has no known mechanistic overlap with serotonin transporter inhibition.

**Caution:** the TxGNN score of 0.99 is very high, but it is a pure graph-neural-network prediction based on drug–disease association topology, with no known biological plausibility identified to support it. Given the sparsity of rare-disease training data, this is highly suspected to be a spurious association arising from indirect, biologically meaningless paths in the embedding space rather than a genuine pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Paroxetine is not marketed in Saudi Arabia under this evidence pack (0 licenses on record); no product authorization details are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported solely by a TxGNN model score (L5, no clinical trials or literature) and the disclosed mechanistic rationale explicitly flags the association as biologically implausible and likely a data-driven artifact given the unrelated chromatin-modifier pathology of Ohdo syndrome. Additionally, a Blocking data gap exists on TFDA/SFDA package insert safety data, preventing even a preliminary safety review.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) to close the Blocking safety data gap
- Verified drug mechanism of action (MOA) data from DrugBank or primary literature
- Independent preclinical or mechanistic evidence linking SSRI activity to KAT6A/KAT6B-related pathology before further investment
- Re-evaluation if new clinical trials or literature supporting this indication emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

