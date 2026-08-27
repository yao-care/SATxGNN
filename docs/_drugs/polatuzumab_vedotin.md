---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From Diffuse Large B-Cell Lymphoma to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an antibody-drug conjugate (anti-CD79b + MMAE) originally approved for diffuse large B-cell lymphoma (DLBCL).
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction stands on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diffuse Large B-Cell Lymphoma (DLBCL) — per repurposing rationale text; structured `original_indications`/`original_moa` fields are not yet populated |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.34% (rank 9792) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data has not yet been loaded into the drug record (`original_moa` = Data Gap). Based on the mechanistic rationale accompanying this prediction, polatuzumab vedotin is an anti-CD79b monoclonal antibody conjugated to the microtubule inhibitor MMAE. It targets CD79b on the B-cell receptor complex, is internalized by CD79b-expressing B cells, and releases MMAE intracellularly to kill the cell. Its approved use is DLBCL.

HER2-positive breast carcinoma is driven by overexpression of the HER2/ERBB2 tyrosine kinase receptor — a pathway with no known intersection with CD79b/B-cell receptor signaling. Breast cancer cells are not known to express CD79b, the antibody's targeting antigen. The evidence pack itself flags this mechanistic link as weak-to-unsupported: the prediction is generated purely by the TxGNN model score, with no corroborating mechanism, clinical trial, or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Polatuzumab vedotin is not currently marketed in Saudi Arabia (0 authorizations on file), so no product license table is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-CD79b antibody carrying the microtubule-inhibitor payload MMAE) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is at evidence level L5 (model prediction only) with no clinical trials, no literature, and a mechanistic rationale that the evidence pack itself characterizes as weak/unsupported. A blocking data gap on TFDA-equivalent package insert warnings/contraindications (DG001) also prevents entry into safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications, DDI) to clear the blocking data gap (DG001)
- Structured original MOA and original indication data from DrugBank (DG002)
- Preclinical or mechanistic studies establishing a CD79b/ADC-relevant pathway in HER2-positive breast carcinoma
- At minimum, early-phase clinical or case-level evidence before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

