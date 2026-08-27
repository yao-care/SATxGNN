---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: From Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated radiographic contrast medium (used for X-ray/CT/myelography imaging), not a therapeutic agent, and is not currently marketed in Saudi Arabia. The TxGNN model predicts it may be effective for **Insomnia** (score 99.87%), but this prediction is supported by **zero clinical trials and zero publications**, and the evidence pack's own analysis flags it as a likely false positive driven by knowledge-graph co-occurrence (e.g., "renal function testing / hospitalization context") rather than a real pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Saudi regulatory data (no licenses on file); known use is as a radiographic contrast agent for X-ray/CT/myelography |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Iohexol is a non-ionic iodinated contrast medium used diagnostically for imaging (X-ray, CT, myelography). It has no established central nervous system penetration and no known receptor-binding activity relevant to sleep regulation (e.g., GABA or serotonergic pathways).

The evidence pack's own mechanistic assessment is explicit: the drug has no CNS pharmacology, so there is no plausible biological basis for an anti-insomnia effect. The high TxGNN score is most likely explained by spurious co-occurrence in the knowledge graph — iohexol frequently appears in contexts like renal function testing (GFR measurement) and hospitalization, which may also correlate with sleep-related diagnoses in the training data, without reflecting a true drug-disease relationship.

A second, lower-ranked candidate (anxiety, score 99.25%) was also evaluated and shows the same pattern: 6 associated clinical trials exist, but all were graded "C" (low relevance) — they involve iohexol only as a GFR-measurement tool in transplant, bariatric surgery, or critical-illness studies, not as an anxiolytic treatment. This reinforces that the signal is a data-pipeline artifact (keyword/entity mismatch) rather than genuine repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Insomnia.

*(Note: 6 trials were retrieved for the secondary candidate "anxiety," but all were assessed as Grade C / not relevant — iohexol was used only as a renal-clearance measurement agent, not as a treatment. These are not included here as they do not support the primary predicted indication.)*

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are marked as a Blocking data gap — retrieval and parsing from the official source is required before any S1 safety screening can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications (insomnia and anxiety) are L5 evidence level with no genuine supporting clinical trials or literature, and the drug's known pharmacology (a non-CNS-active contrast agent) provides no mechanistic basis for either. The evidence pack itself identifies this as likely noise from knowledge-graph co-occurrence rather than a true repurposing signal.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action from DrugBank or primary literature
- A targeted literature/trial search specifically for iohexol + CNS/sleep/anxiety pharmacology to rule out or confirm any genuine signal before further evaluation
- If no genuine signal is found, this candidate should be deprioritized rather than advanced to S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

