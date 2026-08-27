---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 2
---

# Nimodipine
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

# Nimodipine: From Cerebral Vasospasm Prevention to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a dihydropyridine L-type calcium channel blocker whose established clinical role is preventing cerebral vasospasm after subarachnoid hemorrhage (per mechanistic notes in this evidence pack; official original-indication data is currently a gap).
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in structured data (data gap); mechanistic notes reference cerebral vasospasm prevention after subarachnoid hemorrhage |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (data gap DG002). Based on the rationale notes accompanying this prediction, nimodipine is a highly lipophilic L-type calcium channel blocker (dihydropyridine class) whose known clinical effect is relaxation of cerebral vascular smooth muscle, used to prevent vasospasm after subarachnoid hemorrhage.

HoFH pathology arises from LDL receptor (or APOB/PCSK9) gene defects that impair LDL clearance — a lipid-metabolism pathway with no known mechanistic overlap with calcium channel signaling. The high TxGNN score (99.29%) most likely reflects an indirect association in the model's embedding space (e.g., clustering with cardiovascular disease comorbidities) rather than a genuine pharmacological link.

A second predicted indication, nephrogenic syndrome of inappropriate antidiuresis (NSIAD, score 99.05%), shows the same pattern: NSIAD is driven by gain-of-function AVPR2 mutations acting through the renal cAMP/AQP2 pathway, with no established connection to calcium channel blockade. Both predictions currently rest on model output alone, with no supporting trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Nimodipine is not currently marketed in Saudi Arabia; no product authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications (HoFH and NSIAD) are Evidence Level L5 — model prediction only, with no clinical trials, literature, or established mechanistic link. This is compounded by a Blocking data gap (DG001: TFDA warnings/contraindications unavailable), which prevents even an initial safety screen, and the drug is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — required before any safety assessment (DG001)
- Confirmed original MOA and approved indication data from a structured source such as DrugBank (DG002)
- Independent mechanistic or preclinical evidence connecting calcium channel blockade to lipid metabolism (HoFH) or AVPR2/AQP2 signaling (NSIAD)
- Ongoing literature/trial monitoring, since no evidence currently exists for either predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

