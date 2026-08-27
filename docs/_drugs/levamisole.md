---
layout: default
title: Levamisole
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Levamisole
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

# Levamisole: From Antiparasitic Therapy to Drug-Induced Osteoporosis

## One-Sentence Summary

Levamisole is an anthelmintic/immunomodulatory agent; no original-indication or licensing data for it is on file in Saudi Arabia (0 authorizations, unmarketed). The TxGNN model's top-ranked prediction is **drug-induced osteoporosis**, but this prediction is supported by **0 clinical trials** and **0 publications** — it is model-score-only and, per the evidence pack's own rationale, likely embedding-space noise with no known mechanistic link to bone metabolism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data on file — Levamisole is not marketed in Saudi Arabia (0 licenses); general pharmacology classes it as an anthelmintic/immunomodulatory agent |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.9993% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Levamisole in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, Levamisole is an imidazothiazole-class anthelmintic with secondary immunomodulatory activity (T-cell activation, enhancement of phagocyte function); this is background context, not sourced from the evidence pack itself.

There is no established relationship between Levamisole's known pharmacology and bone metabolism. The evidence pack's own repurposing rationale is explicit on this point: no clinical trial or literature evidence exists for this indication, and the drug's known mechanisms (antiparasitic/immunomodulatory) have no known connection to osteoporosis pathophysiology. The evaluators assess this as likely noise from the TxGNN embedding space rather than a genuine mechanistic signal.

Given the complete absence of supporting studies, the mechanism cannot currently be considered applicable to this indication, and the prediction should be treated as hypothesis-generating only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

No marketing authorizations on file — Levamisole is currently unmarketed in Saudi Arabia (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (drug-induced osteoporosis) has no clinical trial or literature support, evidence level L5, and the evidence pack itself flags it as likely model noise with no plausible mechanistic link — there is nothing to act on at this time.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed mechanism of action data (DG002)
- Any preclinical or mechanistic evidence connecting Levamisole to bone metabolism, should this indication be pursued further
- Note: a materially stronger signal exists elsewhere in this evidence pack — the head & neck (hypopharynx) neoplasm prediction (rank 9) is supported by two RCTs (L2, "Research Question" stage) on Levamisole as post-operative adjuvant immunotherapy in laryngeal/head-neck carcinoma. This warrants a separate, dedicated evaluation rather than being folded into the osteoporosis prediction covered here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

