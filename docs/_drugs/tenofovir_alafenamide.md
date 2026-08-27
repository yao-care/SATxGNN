---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 606
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tenofovir Alafenamide: From an Undocumented Original Indication to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Tenofovir alafenamide (DB09299) is a nucleotide analogue whose original approved indication and mechanism of action are not yet documented in current records.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome**, a veterinary (feline) disease,
> currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available regulatory/DrugBank records |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tenofovir alafenamide belongs to the nucleotide reverse transcriptase inhibitor class of antivirals, but its formally recorded original indication is not present in this evidence pack.

The top-ranked predicted indication, Feline Acquired Immunodeficiency Syndrome, is caused by Feline Immunodeficiency Virus (FIV) — a lentivirus in the same family as HIV, against which reverse-transcriptase-targeting antivirals such as tenofovir alafenamide are mechanistically active. This cross-species mechanistic analogy is a plausible basis for the TxGNN link, but it remains a knowledge-graph inference rather than a study-confirmed relationship — no clinical trial or literature evidence currently exists for this specific indication.

Notably, the second-ranked prediction in this evidence pack, "simian immunodeficiency virus infection," carries an almost identical TxGNN score and is supported by 1 clinical trial and 9 publications describing tenofovir alafenamide activity against SIV/SHIV in macaque models — evidence that is directly relevant to the drug's antiretroviral mechanism in a way the top-ranked feline indication is not. Reviewers may wish to weigh that candidate alongside this one when prioritizing follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Tenofovir alafenamide currently holds no marketing authorization in Saudi Arabia (market status: not marketed; 0 authorizations on record).

---

## Safety Considerations

Package insert warnings, contraindications, and drug-drug interaction data for tenofovir alafenamide have not yet been retrieved (TFDA source query pending). This is flagged as a **blocking gap** for safety assessment — please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Feline Acquired Immunodeficiency Syndrome) is supported only by the TxGNN model score with no clinical trial or literature evidence (L5), the drug is not marketed in Saudi Arabia, and retrieval of TFDA safety data is a blocking gap that prevents a preliminary safety (S1) assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings and contraindications) — blocking, required before any safety review
- Confirmed original indication(s) and mechanism of action (MOA) for tenofovir alafenamide
- Clarification of the human-relevance of a feline-specific predicted indication, or consideration of the better-evidenced rank-2 candidate (simian immunodeficiency virus infection)
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

