---
layout: default
title: Olaratumab
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Olaratumab
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

# Olaratumab: From Soft Tissue Sarcoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Olaratumab is a monoclonal antibody originally approved for advanced soft tissue sarcoma, but it was withdrawn from the global market in 2019 after its confirmatory trial failed to show a survival benefit. The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — a pure model prediction with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft Tissue Sarcoma *(external background knowledge — not confirmed by this dataset's official fields; original_moa and original_indications are Data Gaps DG001/DG002)* |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% (rank 772) |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (Data Gap DG002, severity High). Based on external background knowledge not verified against this dataset's DrugBank/TFDA fields, Olaratumab is a human IgG1 monoclonal antibody against PDGFRα (platelet-derived growth factor receptor alpha), originally approved as Lartruvo for advanced soft tissue sarcoma in combination with doxorubicin, and globally withdrawn in 2019 after the confirmatory ANNOUNCE trial failed to demonstrate a statistically significant overall survival benefit.

There is no established biological relationship between soft tissue sarcoma and urothelial carcinoma of the prostatic urethra, and no known role for PDGFRα signaling in the pathogenesis of this tumor type. The prediction appears to be driven purely by TxGNN embedding similarity rather than any confirmed shared mechanism.

Because both the original MOA field and the original indication field are Data Gaps in this dataset, this mechanistic reasoning rests on unverified external knowledge and should not be treated as validated. It is included only for transparency and must be confirmed against DrugBank/regulatory sources before being used in any decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Olaratumab is an antineoplastic agent (monoclonal antibody used in soft tissue sarcoma per external background knowledge).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-PDGFRα monoclonal antibody) — inferred from external knowledge, not confirmed in this dataset |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical trial and zero literature support for this indication, no confirmed mechanistic rationale (PDGFRα biology has no established link to urothelial carcinoma), and a Blocking data gap on TFDA package insert/safety data (DG001) prevents even an initial safety screen. Olaratumab is also globally discontinued (per external knowledge) and not marketed in Saudi Arabia, which raises a separate feasibility question independent of the evidence level.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/manufacturer package insert to resolve DG001 (Blocking)
- Confirm mechanism of action and original indication via DrugBank API to resolve DG002
- Independently verify Olaratumab's regulatory/withdrawal status before any further evaluation
- Assess commercial/supply feasibility given the drug's global market withdrawal
- Note a data-quality issue found elsewhere in this evidence pack: the literature match for the rank-10 candidate ("breast tumor luminal A or B") was a false positive caused by keyword mismatch on "B" (luminal B) — recommend auditing the literature-search logic before trusting literature counts for other candidates in this batch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

