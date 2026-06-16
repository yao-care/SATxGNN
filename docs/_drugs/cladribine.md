---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 7
---

# Cladribine
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analogue with established efficacy in hairy cell leukemia, exerting selective cytotoxicity against lymphoid cells via deoxycytidine kinase (dCK)-mediated DNA strand breakage.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
however **no clinical trials and no supporting publications** exist for this repurposing direction — the prediction rests entirely on knowledge-graph topology inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hairy Cell Leukemia |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on information embedded in the repurposing rationale, Cladribine is a purine nucleoside analogue (deoxyadenosine analogue) that is phosphorylated intracellularly by deoxycytidine kinase (dCK), accumulating as an active triphosphate that causes DNA strand breaks and induces apoptosis in non-dividing cells. This mechanism confers particularly potent activity in lymphoid malignancies with high dCK expression — hairy cell leukemia being the textbook indication.

Parameningeal embryonal rhabdomyosarcoma is a mesenchymal-origin pediatric tumor arising near the meninges (nasal cavity, paranasal sinuses, middle ear, infratemporal fossa). Standard treatment follows IRS/ARST protocols combining vincristine, actinomycin-D, and cyclophosphamide (VAC) with local irradiation. Cladribine's mechanistic advantage in lymphoid cells does not readily translate to rhabdomyosarcoma: the dCK expression level and purine metabolism enzyme ratios in RMS cell lines are entirely unknown, and no experimental data establish drug sensitivity.

The TxGNN model prediction is driven by knowledge-graph topological similarity — Cladribine's disease-node neighborhood in the KG overlaps with rhabdomyosarcoma subtypes through shared gene and pathway nodes, not through direct mechanistic or pharmacological evidence. While this is a valid signal for hypothesis generation, it does not constitute a plausible biological link without preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cladribine in parameningeal embryonal rhabdomyosarcoma.

---

## Literature Evidence

Currently no related literature available for Cladribine in parameningeal embryonal rhabdomyosarcoma.

---

## Cytotoxicity

Cladribine is an antineoplastic purine nucleoside analogue (antimetabolite) used in the treatment of hairy cell leukemia and multiple sclerosis. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analogue (antimetabolite) |
| Myelosuppression Risk | High — severe and prolonged neutropenia, thrombocytopenia, and anaemia are expected on-target effects; nadir typically occurs 2–4 weeks post-infusion |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (weekly during and after treatment), liver function tests, renal function, CD4+ lymphocyte count (prolonged lymphopenia risk) |
| Handling Protection | Must be handled according to cytotoxic drug handling regulations; preparation in a biological safety cabinet, PPE required |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Full warning text and contraindications were not retrievable from the current data sources. Known class-level concerns include severe and prolonged myelosuppression, opportunistic infections secondary to profound CD4+ lymphopenia, fever, and teratogenicity — formal verification against the approved prescribing information is required before any clinical use.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven TxGNN-predicted indications for Cladribine in this Evidence Pack are rated L5 (model prediction only), with zero registered clinical trials and no relevant literature across any rhabdomyosarcoma or bile duct sarcoma subtype. The mechanistic link between Cladribine's lymphoid-selective, dCK-dependent cytotoxicity and mesenchymal-origin RMS tumors is biologically unestablished — the prediction reflects knowledge-graph topology, not pharmacological plausibility.

**To proceed, the following is needed:**

- **Preclinical dCK expression data**: Measure dCK activity and 5′-nucleotidase (dNT) ratios in RMS cell lines (RD, Rh30, RMS-YM) to determine whether Cladribine's selectivity mechanism is operative in mesenchymal tumors
- **In vitro cytotoxicity assay**: IC₅₀ determination in at least 2–3 RMS cell lines before any animal model investment
- **Formal MOA documentation**: Retrieve complete DrugBank MOA entry and Taiwan/FDA-approved package insert mechanistic description
- **Safety data gap resolution**: Obtain full warning text and contraindications from TFDA package insert or EMA/FDA prescribing information
- **Orphan disease context review**: Parameningeal embryonal RMS is a rare pediatric cancer; any repurposing effort should engage pediatric oncology specialists and review current IRS/COG cooperative group trial data to assess unmet need and combinability with standard VAC therapy
- **Broader RMS literature sweep**: A systematic PubMed search using broader terms (cladribine + sarcoma, 2-CdA + mesenchymal neoplasm) may surface indirect mechanistic clues not captured in the current targeted query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

