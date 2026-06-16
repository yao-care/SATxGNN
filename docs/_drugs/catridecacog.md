---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# CATRIDECACOG: From Congenital Factor XIII Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

CATRIDECACOG (recombinant coagulation Factor XIII A-subunit, brand name Tretten) is approved for prophylaxis of bleeding episodes in adults and adolescents with congenital Factor XIII A-subunit deficiency.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **no clinical trials** and **no published literature** currently supporting this direction — the prediction rests entirely on knowledge graph proximity among bleeding disorders.
Evidence level is L5 (model prediction only), and the current recommendation is **Hold** pending mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Factor XIII A-subunit deficiency (bleeding prophylaxis) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

CATRIDECACOG is a recombinant human Factor XIII A-subunit (rFXIII-A). Factor XIII is a transglutaminase activated by thrombin in the final steps of the coagulation cascade; it cross-links fibrin chains to produce a mechanically stable, protease-resistant clot. Its approved use targets the rare inherited deficiency where fibrin stabilization itself is impaired.

Primary release disorder of platelets (dense granule or α-granule secretion defects) represents a fundamentally different pathophysiology: the core defect lies in upstream platelet activation and granule exocytosis, not in fibrin cross-linking. FXIII acts exclusively at the downstream fibrin stabilization stage and cannot correct defective platelet degranulation. An indirect compensatory hypothesis exists — exogenous FXIII supplementation might partially reinforce a fibrin network that is inadequate due to diminished platelet contribution to primary hemostasis — but this remains purely speculative and carries no demonstrated clinical significance.

The high TxGNN score most likely reflects the proximity of "primary release disorder of platelets" and "congenital FXIII deficiency" within the bleeding-disorder subgraph of the biomedical knowledge graph, rather than a direct mechanistic connection. At this stage, the biological rationale is insufficient to advance without supporting preclinical or clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

CATRIDECACOG is not currently marketed or registered in Saudi Arabia. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (primary release disorder of platelets, pseudo-von Willebrand disease, Glanzmann thrombasthenia) carry L5 evidence with zero supporting clinical trials or publications; the mechanistic link between FXIII and platelet-release disorders is indirect and speculative, making advancement without further validation premature.

**To proceed, the following is needed:**

- **Mechanistic proof-of-concept**: In vitro or ex vivo studies demonstrating whether supplemental FXIII can compensate for primary hemostatic defects caused by platelet granule release failure
- **MOA data (DG002)**: Retrieve full DrugBank pharmacology entry to formally document mechanism and known targets
- **Safety data (DG001)**: Obtain approved package insert (Saudi Arabia / EMA / FDA) to populate key warnings, contraindications, and special population data
- **Glanzmann thrombasthenia pivot**: Among the three predicted indications, rank 3 (Glanzmann thrombasthenia) carries the strongest biological rationale — FXIII cross-links fibrin–fibronectin to compensate for absent platelet aggregation, and a documented biochemical synergy with rFVIIa exists. This indication should be prioritised as the primary research question over platelet release disorders
- **Literature scan broadening**: Search for any FXIII use in platelet function disorders under alternate search terms (e.g., storage pool disease, delta-granule deficiency, secretion defects) before a final Hold decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

