---
layout: default
title: Lindane
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Lindane
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

# Lindane: From Ectoparasiticide (Scabies/Lice) Use to Cervical Neuroblastoma

## One-Sentence Summary

Lindane is a historically used organochlorine ectoparasiticide (scabicide/pediculicide); formal original-indication and mechanism-of-action data are not on file for this record. The TxGNN model predicts activity for **Cervical Neuroblastoma** (top-ranked of 10 candidate indications, all clustered in head/neck and cystic neoplasm categories), but **0 clinical trials** and **0 publications** currently support any of these predictions — this is a model-score-only signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in structured data (record has no `licenses`/`original_indications` entries); rationale notes describe Lindane as an organochlorine insecticide/scabicide |
| Predicted New Indication | Cervical Neuroblastoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for this record (flagged as a High-severity data gap, DG002). Based on the contextual notes accompanying the predictions, Lindane's known pharmacology is that of a **GABA-gated chloride channel antagonist** — a neurotoxic mechanism that produces CNS overexcitation, which is itself its principal safety concern rather than a therapeutic mechanism relevant to oncology.

No mechanistic pathway links this GABA-antagonist activity to neuroblastoma, or to any of the other nine predicted indications (benign neoplasm of tongue, epiglottis neoplasm, odontogenic cyst, pre-malignant neoplasm, hypopharynx neoplasm, jugular foramen schwannoma, cystic neoplasm, buccal mucosa neoplasm, inner ear neoplasm). The strong clustering of predictions around head-and-neck and cystic neoplasm categories, all with near-identical TxGNN scores (~99.9%) and consecutive model ranks (2075–2169), is more consistent with an embedding-space artifact than a genuine pharmacological signal — a pattern each rationale entry explicitly flags.

Compounding this, Lindane is **not marketed in Saudi Arabia** (0 licenses on file) and a Blocking-severity data gap (DG001: TFDA label warnings/contraindications) means the drug cannot yet clear even a preliminary safety screen (S1). There is no basis at this time to consider the mechanism "applicable" to the predicted indications beyond the raw model score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable in this record; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are TxGNN score-only (L5) with zero supporting clinical trials or literature, no plausible mechanistic link, and a Blocking-severity data gap in TFDA safety labeling that prevents even a preliminary safety assessment. The drug is also not marketed in Saudi Arabia.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official TFDA/regulatory package insert for warnings and contraindications
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to properly evaluate mechanistic plausibility
- Independent literature/preclinical search specifically for Lindane–oncology pathway links, given none surfaced in PubMed/ClinicalTrials.gov/ICTRP queries
- Reassess whether the head-and-neck/cystic-neoplasm prediction cluster reflects a genuine signal or a TxGNN embedding artifact before allocating further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

