---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is an anti-CCR4 monoclonal antibody; the evidence pack's own rationale notes it is known to be used for cutaneous T-cell lymphoma (mycosis fungoides/Sézary syndrome), though this is not formally recorded in the structured indication field. The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction stands entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (mycosis fungoides/Sézary syndrome) — referenced only in the evidence pack's rationale text; the formal `original_indications` field is empty and `original_moa` is a data gap |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is marked as a data gap in this evidence pack. Based on the rationale accompanying the predictions, mogamulizumab is a monoclonal antibody targeting CCR4, which depletes CCR4-positive regulatory T cells (Tregs) via antibody-dependent cellular cytotoxicity (ADCC). This is described in the pack as general pharmacological knowledge, not a dataset-verified fact, and it is explicitly *not* tied to any CCR4 expression or Treg-infiltration data for urothelial cancers.

The proposed link to prostatic urethra urothelial carcinoma is a broad immuno-oncology inference: depleting Tregs could, in theory, relieve tumor-microenvironment immune suppression and enhance anti-tumor immunity across many solid tumors. No tumor-specific evidence — CCR4 expression levels, Treg infiltration patterns, or preclinical models in urothelial carcinoma — is provided to support this specific pairing.

Because the drug's established use (cutaneous T-cell lymphoma) is a hematologic malignancy with well-characterized CCR4 biology, while the predicted indication is a solid-tumor, epithelial malignancy of a different lineage, the mechanistic distance between the two is substantial. The high TxGNN score reflects network-level similarity in the model's embedding space, not a validated biological pathway between the two conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

Mogamulizumab is an antineoplastic monoclonal antibody (immunotherapy class, per its known use in T-cell lymphoma and its ADCC-based Treg-depletion mechanism described in the evidence pack).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CCR4 monoclonal antibody, ADCC-mediated Treg depletion) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, no clinical trials or literature), and the drug is not marketed in Taiwan. There is no tumor-specific mechanistic, preclinical, or clinical evidence connecting mogamulizumab to prostatic urethra urothelial carcinoma (or the other six ranked candidates, all similarly at L5/Hold).

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications) — currently a Blocking data gap preventing any safety pre-assessment
- Confirmed mechanism-of-action and formal original-indication record from DrugBank or a regulatory source
- CCR4 expression / Treg-infiltration data specific to urothelial carcinoma to test the mechanistic hypothesis
- A broader literature/trial search (including off-label case reports) before any further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

