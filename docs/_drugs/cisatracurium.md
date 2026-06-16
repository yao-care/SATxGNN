---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent (NMBA) used perioperatively to facilitate endotracheal intubation and maintain skeletal muscle relaxation during surgery or mechanical ventilation in intensive care.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, yet there are currently **0 clinical trials** and **0 publications** directly supporting this therapeutic direction.
All 10 predicted indications in this evidence pack are rated L5 (model prediction only), and mechanistic analysis across every candidate condition reveals no plausible biological link to cisatracurium's pharmacology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade for endotracheal intubation and skeletal muscle relaxation during surgery / ICU mechanical ventilation |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (0 approved licenses) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, cisatracurium is a benzylisoquinolinium-type non-depolarizing NMBA that competitively antagonizes nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction, preventing acetylcholine-induced muscle depolarization. Its established clinical role is strictly perioperative: facilitating tracheal intubation and maintaining muscle relaxation during general anesthesia or ICU ventilator management.

Cauda equina syndrome is a neurological emergency caused by acute compression of the nerve root bundle (cauda equina) in the lumbar spinal canal, presenting with low back pain, lower-limb weakness, and bladder/bowel dysfunction. The definitive treatment is urgent surgical decompression. There is no established biological pathway by which peripheral nAChR blockade at the motor end plate could relieve compressed lumbar nerve roots or alter the underlying pathophysiology of cauda equina syndrome.

The high TxGNN score (99.99%, global rank 334) most likely reflects indirect graph traversal through shared spinal/neural pathway nodes in the knowledge graph rather than a genuine therapeutic signal — what the evidence pack authors themselves characterize as "graph diffusion noise." This prediction should not be interpreted as a clinical repurposing opportunity without substantial preclinical evidence to the contrary.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating cisatracurium for cauda equina syndrome are registered.

---

## Literature Evidence

Currently no related literature directly examining cisatracurium as a treatment for cauda equina syndrome is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for prescribers:** Although not captured in the current evidence pack, one clinically important drug interaction is well-established in the literature: magnesium sulfate (the standard treatment for preeclampsia/eclampsia) potentiates neuromuscular blockade and requires cisatracurium dose reduction. This is a safety consideration during anesthetic management, not a therapeutic repurposing signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for cisatracurium are rated L5 with no supporting clinical trials or literature for the top-ranked indication, and mechanistic analysis consistently shows no plausible link between peripheral nAChR blockade and any of the predicted conditions — including cauda equina syndrome, preeclampsia, migraine disorder, irritable bowel syndrome, and thrombotic disease. The predictions most likely represent knowledge-graph diffusion artifacts rather than genuine repurposing signals.

**To proceed further, the following would be needed:**

- Identification of a biologically plausible mechanism linking cisatracurium to any of the predicted indications
- At least one preclinical study or case series demonstrating pharmacodynamic activity in the target disease context
- Complete safety data: package insert warnings, contraindications, and full DDI profile (currently all flagged as data gaps)
- Re-evaluation using a refined knowledge graph with noise-reduction filters to suppress diffusion artifacts from high-connectivity nodes
- If any indication is to be prioritized, a formal literature review beyond the automated search should be conducted to rule out indirect evidence (e.g., case reports, secondary analyses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

