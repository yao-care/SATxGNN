---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia (ITP) to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin (TPO) receptor agonist whose established clinical role, per the evidence in this pack, is treating immune thrombocytopenia (ITP)-related platelet deficiency. The TxGNN model predicts it may also be effective for **Primary Release Disorder of Platelets**, but this specific prediction is currently supported by only **1 clinical trial** (observational, not an interventional drug trial) and **2 publications** (mechanistic/background literature).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Saudi Arabia licensing (drug not marketed); evidence pack rationale identifies romiplostim's actual approved-use category as **Immune Thrombocytopenia (ITP)** |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% (rank 8 among all predictions) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, a formal MOA record for romiplostim is not available in the structured drug data. However, the evidence pack's own mechanistic rationale describes romiplostim as a thrombopoietin (TPO) receptor agonist that directly stimulates megakaryocyte production and platelet release — the same mechanism underlying its established use in ITP.

"Primary release disorder of platelets" describes a defect in the release of platelets from megakaryocytes into circulation. Since romiplostim's core pharmacology acts precisely at this step of thrombopoiesis, the mechanistic link to this predicted indication is direct and biologically coherent — which is consistent with the very high TxGNN score (99.9998%).

That said, the supporting evidence currently available is indirect: the one linked clinical trial (NCT03820960) is an observational cohort study of thrombosis risk factors in ITP patients, not a trial testing romiplostim's efficacy in a platelet-release disorder. The two literature references describe megakaryocytopoiesis/thrombopoiesis biology and antibody-mediated impairment of proplatelet formation in ITP, rather than direct romiplostim intervention data for this exact disease label. Notably, a closely related indication category in this same evidence pack — "platelet-type bleeding disorder" (which the rationale explicitly ties to ITP, romiplostim's real-world approved use) — is supported by much stronger evidence, including a completed Phase 3 RCT (RECITE, NCT03362177). This suggests the mechanistic hypothesis is sound, but direct evidence for the specific "primary release disorder of platelets" label still needs to be built out.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational cohort study on thrombosis risk factors in immune thrombocytopenia (ITP); did not test romiplostim efficacy — provides indirect epidemiological data on the relevant patient population only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis biology, including thrombopoietin (TPO) as the primary growth factor for the megakaryocyte lineage — the mechanistic basis for TPO receptor agonists like romiplostim. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Cohort/Mechanistic | Haematologica | Shows that antiplatelet autoantibodies in ITP inhibit proplatelet formation by megakaryocytes and impair platelet release in vitro — directly relevant to the "platelet release disorder" mechanism, though not a romiplostim intervention study. |

## Saudi Arabia Market Information

Romiplostim is not currently marketed in Saudi Arabia (0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic case is strong — romiplostim's TPO receptor agonism directly targets the platelet-release pathway relevant to this indication — but the current evidence base consists only of an observational cohort study and background mechanistic literature, not an interventional trial of romiplostim in this specific disease. This warrants further investigation before advancing to a Go/Hold/Guardrails decision.

**To proceed, the following is needed:**
- Formal MOA and drug classification data from DrugBank (flagged as a High-severity data gap)
- TFDA/regulatory package insert data — warnings, contraindications, DDI (flagged as a Blocking data gap for safety review)
- An interventional trial or case series testing romiplostim specifically in patients with a primary platelet-release defect (rather than ITP generally)
- Clarification of how "primary release disorder of platelets" is diagnostically distinguished from ITP in the target population, to determine whether existing ITP trial data (e.g., the Phase 3 RECITE trial) can be extrapolated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

