---
layout: default
title: Ferrous Gluconate
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 5
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ferrous Gluconate: From Iron-Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferrous gluconate is an oral iron salt used to treat and prevent iron-deficiency anemia. The TxGNN model predicts it may also be effective for **Plummer-Vinson syndrome**, a condition classically caused by chronic iron deficiency, but no clinical trials or published literature specific to this indication were found in the current evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron-deficiency anemia (general pharmacological use — not recorded in the regulatory data available for this pack) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous gluconate is an iron-replacement salt used to correct iron-deficiency anemia by restoring iron stores needed for hemoglobin synthesis.

Plummer-Vinson syndrome (also known as Paterson-Kelly syndrome or sideropenic dysphagia) is classically defined by the triad of iron-deficiency anemia, esophageal web, and dysphagia. Chronic iron deficiency is considered central to its pathophysiology, and iron repletion is a standard part of its clinical management, often associated with symptomatic improvement or resolution of the esophageal web. This gives the TxGNN prediction a plausible mechanistic basis even though the disease label itself is not primarily a hematologic diagnosis.

That said, this evidence pack found zero clinical trials and zero literature entries specifically indexed under "Plummer-Vinson syndrome" combined with ferrous gluconate. The searches may be limited by terminology — literature on this condition is more often indexed under "Paterson-Kelly syndrome" or "sideropenic dysphagia" rather than the disease ontology term used here, so the absence of hits should not be read as absence of clinical precedent.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high and the underlying mechanism (correcting the iron deficiency that underlies Plummer-Vinson syndrome) is clinically plausible, but there is currently no clinical trial or literature evidence directly supporting this specific indication, and core safety data (TFDA warnings/contraindications) remain a blocking data gap.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action reference from DrugBank (DG002)
- A repeat literature/trial search using synonyms ("Paterson-Kelly syndrome", "sideropenic dysphagia") in case the disease-ontology term used here under-captures relevant publications
- Confirmation of Saudi Arabia market/licensing status, given the drug is currently recorded as not marketed with 0 authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

