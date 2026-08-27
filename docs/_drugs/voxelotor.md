---
layout: default
title: Voxelotor
parent: 僅模型預測 (L5)
nav_order: 669
evidence_level: L5
indication_count: 7
---

# Voxelotor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Voxelotor: From Sickle Cell Disease to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Voxelotor is an allosteric haemoglobin oxygen-affinity modulator used in sickle cell disease (this original indication is referenced consistently in the evidence pack's rationale text, though the formal `original_indications`/`original_moa` fields are not yet populated). TxGNN predicts a possible link to **hereditary thrombocytopenia with normal platelets** with a very high similarity score, but **zero clinical trials and zero publications** currently support this direction, and the evidence pack's own mechanistic assessment finds no biological rationale connecting the two conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Sickle cell disease (per repurposing_rationale narrative; not yet confirmed in `original_indications`/TFDA licensing data) |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field. The repurposing rationale text notes that voxelotor is known to act as an allosteric haemoglobin oxygen-affinity modulator that inhibits haemoglobin polymerisation, the basis for its use in sickle cell disease.

However, this mechanism has no established connection to platelet biology. Hereditary thrombocytopenia with normal platelets is driven by megakaryocyte differentiation and platelet production pathways, which are pharmacologically distinct from haemoglobin oxygen-affinity modulation. The evidence pack's own analysis flags this explicitly: the prediction is attributed to the TxGNN embedding space clustering voxelotor near other haematological disorders (both sickle cell disease and hereditary thrombocytopenias sit in the "blood disorder" region of the model's representation), rather than to any known shared biological pathway.

This same pattern — a very high TxGNN score paired with an explicitly acknowledged absence of mechanistic plausibility — repeats across all 7 ranked predictions in this candidate set (see table below). None have any supporting clinical, literature, or mechanistic evidence; all are classified S0/L5/Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications (Same Candidate Set)

All secondary candidates share the same profile — high TxGNN score, no supporting evidence, no mechanistic plausibility, Hold recommendation:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 2 | Macrothrombocytopenia with mitral valve insufficiency | 99.58% | L5 | Hold |
| 3 | Dense granule disease | 99.58% | L5 | Hold |
| 4 | Transient neonatal thrombocytopenia | 99.57% | L5 | Hold |
| 5 | Thrombocytopenia | 99.51% | L5 | Hold |
| 6 | Acquired monoclonal Ig light chain-associated Fanconi syndrome | 99.13% | L5 | Hold |
| 7 | Primary release disorder of platelets | 99.00% | L5 | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 7 predicted indications for voxelotor in this candidate set are unsupported by clinical trials or literature and lack a plausible mechanistic link to the drug's known haemoglobin-modulating activity; the evidence pack itself characterises these as likely embedding-space noise rather than genuine repurposing signals. There is also no Saudi Arabia market presence and no TFDA package insert data available, blocking any safety pre-assessment (S1).

**To proceed, the following is needed:**
- Confirmed `original_moa` and `original_indications` data (DrugBank API query, currently marked High-severity gap)
- TFDA/regulatory package insert with warnings and contraindications (Blocking-severity gap)
- DDI query resolution (currently `not_found`)
- At minimum, preclinical or mechanistic literature establishing a biological pathway between haemoglobin oxygen-affinity modulation and platelet/megakaryocyte biology before any of these 7 candidates can move beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

