---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From No Registered Indication to Leprosy

## One-Sentence Summary

Peppermint oil (DrugBank DB11198) has no approved indication on file for this evaluation and is not currently marketed in Taiwan. The TxGNN model's top-ranked prediction is **Leprosy**, but this signal is currently supported by **zero clinical trials** and **zero publications** — it is a pure model-score prediction with no biological plausibility evidence identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — product not marketed in Taiwan; no approved indication text on file |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for peppermint oil (flagged as a High-severity data gap). No original indication is on record in this evidence pack either, so there is no established pharmacology-to-pharmacology bridge to evaluate against leprosy.

The evidence pack's own rationale for this prediction is explicit: peppermint oil has no reported antimycobacterial activity, and no mechanistic, preclinical, trial, or literature data connect it to leprosy. This appears to be a high-confidence TxGNN score (rank 4012, score 0.998) unsupported by any real-world evidence — the kind of signal that requires independent biological validation before any further investment.

Notably, elsewhere in this same evidence pack, a *different* predicted indication for peppermint oil — **cardiovascular disease** (rank 9, score 99.13%) — does have supporting data: 2 completed trials (n=40 and n=36) on cardiometabolic/blood pressure outcomes, plus a menthol/TRPM8-mediated parasympathetic mechanism reported in the physiology literature (PMID 30070742), rated evidence level L2. That signal is mechanistically and evidentially far stronger than the leprosy prediction reviewed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no clinical trial, literature, or mechanistic support, and the drug's original MOA and indication data are both missing (DG001 is a Blocking-severity gap that prevents even an initial safety assessment). There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Original indication and MOA data for peppermint oil (currently absent from this evidence pack)
- TFDA/official package insert warnings, contraindications, and DDI data (DG001, Blocking)
- Any preclinical or in vitro antimycobacterial activity data, if this hypothesis is to be pursued further
- Consider re-scoping evaluation toward the **cardiovascular disease** prediction (rank 9, L2 evidence, 2 completed trials + mechanistic literature), which has materially stronger evidentiary support than the top-ranked leprosy signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

