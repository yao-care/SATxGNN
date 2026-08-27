---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 2
---

# Upadacitinib
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

# Upadacitinib: From Inflammatory Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

> Upadacitinib is a selective JAK1 inhibitor known (per available narrative context) for treating inflammatory/autoimmune conditions such as rheumatoid arthritis, atopic dermatitis, and ulcerative colitis; formal original-indication and MOA data are not recorded in this evidence pack.
> The TxGNN model predicts a possible effect on **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital developmental disorder,
> but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the score as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (background context indicates JAK1-inhibitor use in inflammatory disease, e.g. rheumatoid arthritis, atopic dermatitis, ulcerative colitis) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for upadacitinib is not available in this evidence pack (flagged as a High-severity data gap). Based on the limited narrative context provided, upadacitinib is understood to be a selective JAK1 inhibitor that suppresses cytokine signaling, used in inflammatory/autoimmune conditions.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a congenital ocular and skeletal malformation syndrome driven by developmental/genetic abnormalities, not by inflammatory or autoimmune pathology. There is no known mechanistic pathway connecting JAK1 inhibition to embryonic ocular or skeletal development.

The evidence pack's own repurposing rationale explicitly assesses this candidate as lacking biological plausibility: the high TxGNN score (99.61%) is most likely an artifact of the knowledge-graph embedding space rather than a genuine pharmacological signal, since no clinical trials, registry entries, or publications link upadacitinib to this disease. A second candidate in this same evidence pack, brachydactyly-syndactyly syndrome (score 99.58%, also a congenital skeletal malformation), was evaluated with the same conclusion — no known link to JAK-STAT pathway biology and no supporting evidence — and was likewise scored Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Upadacitinib is not marketed in Saudi Arabia (0 authorizations recorded), so no product-level licensing table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (Evidence Level L5), and there is no known mechanistic link between JAK1 inhibition and congenital ocular/skeletal developmental syndromes. The high TxGNN score most likely reflects embedding-space noise rather than a genuine repurposing signal; the same conclusion applies to the second candidate (brachydactyly-syndactyly syndrome) in this evidence pack.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for upadacitinib (currently a data gap)
- TFDA/SFDA package insert warnings and contraindications (currently a Blocking data gap)
- Drug-drug interaction data
- Independent biological-plausibility review before any further investment in this indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

