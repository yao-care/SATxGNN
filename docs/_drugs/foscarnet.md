---
layout: default
title: Foscarnet
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 4
---

# Foscarnet
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

# Foscarnet: From Antiviral Therapy to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Foscarnet is a pyrophosphate analog antiviral agent that inhibits viral DNA polymerase/reverse transcriptase (per mechanism notes on file; formal original-indication data is not recorded in this dataset). The TxGNN model predicts a possible link to **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and has been internally flagged as likely graph-embedding noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (no approved indication text on file; known mechanistically as an antiviral) |
| Predicted New Indication | Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured MOA field. Based on the mechanistic notes recorded alongside this candidate, foscarnet inhibits viral DNA polymerase/reverse transcriptase — a mechanism used clinically against herpesviruses such as CMV and HSV/VZV.

The predicted indication, autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome, is a hereditary vascular disorder caused by defects in the COL4A1/COL4A2 collagen genes. There is no known mechanistic overlap between a collagen-structural disorder and an antiviral polymerase-inhibition pathway.

The TxGNN score is high (0.9956), but this appears to be a graph-embedding artifact rather than a biologically grounded signal: no clinical trials, literature, or ICTRP records connect foscarnet to this disease. The reviewing rationale attached to this candidate explicitly characterizes it as embedding noise. The prediction should not be interpreted as mechanistically plausible without independent corroborating evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Foscarnet currently holds no marketing authorization in Saudi Arabia (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has an evidence level of L5 — a model prediction with no supporting clinical trials or literature — and the internal review explicitly flags it as likely embedding noise with no plausible mechanistic link. Additionally, a **Blocking** data gap (TFDA package insert warnings/contraindications, DG001) prevents this candidate from entering the S1 safety pre-assessment stage regardless of prediction strength.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to unblock S1 safety review
- Confirmed original indication and mechanism of action (MOA) from DrugBank or regulatory source
- Independent literature or preclinical data specifically linking foscarnet to a collagen-vasculopathy pathway before any further evaluation is warranted

*Note: three other TxGNN candidates for this drug (rheumatoid arthritis, diabetic nephropathy, brain small vessel disease with ocular anomalies) were also screened in this evidence pack and were similarly assessed as Hold due to keyword-mismatch literature or absent mechanistic rationale — none currently support progression.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

