---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide is a DMARD (disease-modifying antirheumatic drug) originally used to treat rheumatoid arthritis by inhibiting DHODH and suppressing pyrimidine synthesis in activated lymphocytes. The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital skeletal malformation disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (general pharmacological knowledge; not available in the Saudi Arabia regulatory dataset — drug is unmarketed) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note:** A second candidate indication was also predicted — colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 99.93%, rank 1741) — with the same L5 evidence level, no trials, and no literature. Both are treated identically below since indication #1 is the top-ranked prediction.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, leflunomide is a DHODH (dihydroorotate dehydrogenase) inhibitor and immunomodulator, and its efficacy in rheumatoid arthritis has been proven; mechanistically it is not obviously applicable to brachydactyly-syndactyly syndrome.

Importantly, the evidence pack itself is explicit on this point: brachydactyly-syndactyly syndrome is a congenital skeletal developmental disorder typically driven by mutations in genes such as *GDF5* and *HOXD*, and there is **no known biological connection** between this pathway and leflunomide's immunomodulatory/DHODH-inhibitory mechanism. The same applies to the second candidate, colobomatous microphthalmia-rhizomelic dysplasia syndrome, another congenital developmental syndrome with no established link to leflunomide's known pharmacology.

In both cases, the prediction rests solely on the TxGNN model score, with no clinical trials, no literature, and no articulated mechanistic rationale. This places both candidates at the lowest confidence tier and they should not be interpreted as biologically validated leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Leflunomide is not currently marketed in Saudi Arabia (0 authorizations on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by a raw TxGNN model score (L5), with zero clinical trials, zero literature, and no plausible mechanistic link to leflunomide's known pharmacology. There is currently no basis to advance either candidate.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action (MOA) from DrugBank or primary literature
- Preclinical or case-level evidence establishing biological plausibility for either indication
- If plausibility is established, targeted literature/clinical trial searches using alternate disease terminology (these are rare/orphan conditions that may be indexed under synonyms)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

