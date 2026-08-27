---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl: From Severe Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid, historically used for severe acute/chronic pain management and as an anesthesia adjunct. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this direction is currently supported only by the model score — **no clinical trials and no literature** have been found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe pain management / anesthesia (opioid analgesic) — not present in this Evidence Pack, based on general drug identity knowledge |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% (rank 8252) |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — DrugBank MOA query pending). Based on general pharmacological knowledge, fentanyl is a highly potent mu-opioid receptor agonist. Opioids of this class are well known to stimulate non-osmotic release of antidiuretic hormone (ADH), which can produce dilutional hyponatremia and a clinical picture resembling the Syndrome of Inappropriate Antidiuretic Hormone secretion (SIADH).

NSIAD produces an identical clinical and biochemical picture to SIADH, but its underlying cause is a constitutively active vasopressin V2 receptor mutation rather than elevated circulating ADH. This creates only an **indirect mechanistic link**: fentanyl's opioid-driven ADH stimulation could plausibly phenocopy or aggravate an antidiuretic state, but it would not correct — and could theoretically worsen — the receptor-level defect that actually defines NSIAD. There is no original-indication overlap to reinforce this connection (fentanyl has no history of use in water-balance or renal tubular disorders).

Given the absence of any supporting clinical trial or literature evidence, this prediction should be treated as a hypothesis generated purely by the TxGNN model, not as a mechanistically validated repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Fentanyl is currently **not marketed** in this jurisdiction (0 authorizations on file), so no product/license table is available.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA package insert warnings/contraindications are marked as a **Blocking** data gap — DG001 — and have not yet been retrieved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the prediction is unsupported by any clinical trial or literature evidence, the mechanistic link to NSIAD is indirect and speculative, and the drug is not currently marketed in this jurisdiction. A Blocking-severity safety data gap (TFDA package insert) also precludes even a preliminary safety screen (S1).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required before any safety pre-screen
- Confirmed mechanism of action data from DrugBank
- Preclinical or case-level evidence directly linking opioid pharmacology to NSIAD/antidiuretic states
- Regulatory pathway assessment given current non-marketed status

---
*Note: A second, lower-priority candidate (Tourette syndrome, TxGNN score 99.05%, rank 13027) was also evaluated in this Evidence Pack. It carries the same Hold recommendation (L5/S0) — the proposed mechanistic link (endogenous opioid hypothesis in tic modulation) is weak, direction-uncertain, and mismatched with fentanyl's short-acting, high-abuse-liability profile versus the chronic pediatric/adolescent-onset nature of Tourette syndrome. No clinical trials or literature support this direction either.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

