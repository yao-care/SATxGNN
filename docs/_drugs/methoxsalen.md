---
layout: default
title: Methoxsalen
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From Psoriasis/Vitiligo (Photochemotherapy) to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen (8-MOP) is a psoralen photosensitizer that, combined with UVA exposure (PUVA) or extracorporeal photopheresis (ECP), has an established role in treating T-cell-driven skin conditions such as psoriasis and vitiligo. The TxGNN model predicts it may be effective for **localized pagetoid reticulosis**, a rare cutaneous T-cell lymphoma (CTCL) subtype, but this specific prediction currently has **no direct clinical trial or literature support** — the rationale rests on extrapolation from a closely related CTCL indication rather than dedicated evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from this evidence pack (Saudi regulatory/TFDA package insert data blocked — see Data Gap DG001); known pharmacologically as a psoralen used in PUVA photochemotherapy for psoriasis and vitiligo |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (mechanism-based extrapolation; no direct trials or literature for this specific indication) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for methoxsalen is not available in this evidence pack (Data Gap DG002). Based on known pharmacology, methoxsalen is a psoralen (furocoumarin) photosensitizer: upon UVA activation it intercalates into DNA and forms crosslinks, which suppresses proliferation of activated lymphocytes. This mechanism underlies its established clinical use in PUVA photochemotherapy and, more specifically, extracorporeal photopheresis (ECP) — a therapy already used in practice for cutaneous T-cell lymphomas such as Sézary syndrome and early mycosis fungoides.

Localized pagetoid reticulosis is a rare, indolent localized subtype of mycosis fungoides, and therefore belongs to the same T-cell lymphoma spectrum as "indolent primary cutaneous T-cell lymphoma" (rank 2 in this prediction set, evidence level L3, supported by 2 publications on photopheresis in CTCL). The mechanistic rationale for methoxsalen in localized pagetoid reticulosis is therefore biologically plausible by class extension — but it is an indirect inference, not evidence specific to this exact disease entity. No clinical trials, ICTRP registrations, or PubMed literature were found querying methoxsalen against "localized pagetoid reticulosis" directly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*(Note: related literature exists for the closely related indication "indolent primary cutaneous T-cell lymphoma" — Crovetti et al. 2000, PMID [12118838](https://pubmed.ncbi.nlm.nih.gov/12118838/), a 5-year photopheresis cohort in CTCL; and an Ontario HTA review, PMID [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) — but neither addresses localized pagetoid reticulosis specifically.)*

## Saudi Arabia Market Information

Methoxsalen has no marketing authorizations currently registered in Saudi Arabia (market status: not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (localized pagetoid reticulosis) has no direct clinical trial or literature evidence — support is limited to mechanistic extrapolation from a related, better-evidenced CTCL indication. Combined with the drug's unmarketed status in Saudi Arabia and blocking safety data gaps, this does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank or equivalent source — currently a High-severity gap (DG002)
- Targeted literature/trial search specifically for methoxsalen in localized pagetoid reticulosis (rather than the broader CTCL category)
- Drug interaction (DDI) profile, currently unresolved ("not_found")
- If pursued, consider prioritizing the better-evidenced related indication (indolent primary cutaneous T-cell lymphoma, L3/S2) as the more defensible research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

