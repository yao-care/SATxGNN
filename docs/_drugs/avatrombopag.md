---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: From Thrombocytopenia to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is a thrombopoietin receptor agonist (TPO-RA) approved in multiple markets for thrombocytopenia associated with chronic liver disease and immune thrombocytopenia (ITP), though it is not currently authorized in Saudi Arabia.
The TxGNN model predicts it may be effective for **Marcothrombocytopenia with Mitral Valve Insufficiency** — a rare condition characterized by large-platelet thrombocytopenia concurrent with cardiac valve disease.
This prediction is supported by **0 clinical trials** and **0 publications** specific to this indication, making it a pure model-generated hypothesis requiring prospective research.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thrombocytopenia (chronic liver disease / immune thrombocytopenia) — no Saudi Arabia authorization on record |
| Predicted New Indication | Marcothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 99.9954% |
| Evidence Level | L5 — Model prediction only, no clinical or published studies |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Avatrombopag belongs to the thrombopoietin receptor agonist (TPO-RA) class — the same class as eltrombopag and romiplostim. It acts by binding to and activating the TPO receptor (c-Mpl) on megakaryocytes, stimulating their proliferation and differentiation to increase platelet production. Its efficacy in platelet-count-deficient states has been demonstrated in pivotal trials for chronic liver disease–associated thrombocytopenia and chronic ITP.

Marcothrombocytopenia (macro-thrombocytopenia) refers to a subtype of thrombocytopenia characterized by abnormally large platelets alongside reduced platelet counts. Many forms arise from impaired megakaryocyte maturation or dysregulated thrombopoiesis — precisely the pathway where TPO-RA therapy exerts its effect. This mechanistic overlap provides a biologically plausible rationale for TxGNN's high-confidence score: the model likely identified the shared thrombopoiesis node in the knowledge graph.

However, the co-occurring **mitral valve insufficiency** component of this disease entity has no known mechanistic connection to avatrombopag's pharmacology — it is most likely a comorbidity descriptor rather than a drug target. The prediction should therefore be interpreted narrowly: avatrombopag may address the thrombocytopenic component of this syndrome, but cardiac valve disease would require separate management. Any translational research would need to confirm which molecular subtype of marcothrombocytopenia is involved and whether TPO-RA stimulation is appropriate or potentially harmful (e.g., risk of thromboembolism in valve disease patients).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for avatrombopag in marcothrombocytopenia with mitral valve insufficiency.

---

## Literature Evidence

Currently no related literature available for avatrombopag in marcothrombocytopenia with mitral valve insufficiency.

---

## Saudi Arabia Market Information

Avatrombopag has no authorized products registered with the Saudi Food and Drug Authority (SFDA). No license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams:** Avatrombopag carries a class-level risk of thromboembolic events common to all TPO-RAs. This concern is particularly relevant for the predicted indication, where the co-existing mitral valve insufficiency may create an elevated baseline thrombotic risk. Any prospective use would require careful benefit-risk assessment and dedicated cardiovascular monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 prediction — no clinical trials, no published literature, and no regulatory approval in Saudi Arabia exist for this indication. While the TPO-RA mechanism has a plausible biological link to the thrombocytopenic component of marcothrombocytopenia, the cardiac comorbidity dimension introduces a safety complexity that has not been studied, and the disease entity itself is extremely rare.

**To proceed, the following is needed:**

- **MOA documentation:** Obtain full DrugBank and package insert data to formally confirm mechanism of action and contraindication profile
- **Safety data gap resolution:** Retrieve SFDA/FDA package insert to assess key warnings and contraindications (currently all Data Gap — DG001 is Blocking severity)
- **Disease subtype stratification:** Identify specific molecular subtypes of marcothrombocytopenia where TPO-RA stimulation is biologically appropriate (e.g., MYH9-related disease vs. GPIb deficiency)
- **Thromboembolic risk assessment:** Evaluate whether the presence of mitral valve insufficiency constitutes a contraindication to TPO-RA use in this population
- **Rare disease expert consultation:** Engage hematology and cardiology specialists to assess feasibility of a prospective case series or registry study
- **Saudi Arabia regulatory pathway:** Confirm whether an import/compassionate use pathway exists prior to any clinical evaluation, given zero current SFDA authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

