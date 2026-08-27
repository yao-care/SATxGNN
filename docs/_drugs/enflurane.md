---
layout: default
title: Enflurane
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 8
---

# Enflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Enflurane: From General Anesthesia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Enflurane is a halogenated inhalational agent originally used for the induction and maintenance of general anesthesia.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-inference signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (inhalational anesthetic) — based on known drug classification; no structured `original_indications` or Saudi license data available in this evidence pack |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is a data gap). Based on known pharmacology, enflurane is a halogenated ether-class volatile general anesthetic whose sedative/hypnotic effect is mediated in part through positive allosteric modulation of the GABA-A receptor — the same broad receptor family targeted by benzodiazepines and other mood-stabilizing/anxiolytic agents used in bipolar disorder management. This shared receptor family is the sole basis for the model's association between enflurane and manic bipolar affective disorder.

However, the evidence pack's own repurposing rationale flags this link as weak: enflurane's GABA-A activity occurs only at anesthetic concentrations under acute, monitored inhalational administration — a delivery mode fundamentally incompatible with the chronic, oral maintenance therapy required for bipolar disorder. Furthermore, enflurane is well known for concentration-dependent **pro-convulsant EEG activity** (seizure-like spike-and-wave discharges), which is a safety concern rather than a therapeutic rationale in a psychiatric population already vulnerable to neurological instability.

Taken together, this is a case where the knowledge-graph embedding similarity (GABA-A pathway overlap) is mechanistically plausible only in the most superficial sense. There is no clinical, preclinical, or case-report evidence of any kind supporting this indication, and the drug's known safety profile (pro-convulsant activity, incompatible route of administration) argues against — rather than for — pursuing this direction without substantial further justification.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Enflurane is currently **not marketed** in Saudi Arabia (0 authorizations on file); no product license records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a computational embedding-similarity signal (Evidence Level L5) with no supporting clinical trials, literature, or preclinical data, and the drug is not currently marketed in Saudi Arabia. The proposed mechanistic link (GABA-A modulation) is directly undercut by enflurane's known pro-convulsant activity and its acute-inhalational-only route of administration, which is not compatible with chronic psychiatric maintenance therapy. All 7 other candidate indications in this evidence pack (Tourette syndrome, trichotillomania, dysthymic disorder, Prinzmetal angina, myofascial pain syndrome, migraine disorder, and bipolar disorder) share the same L5/Hold status for analogous reasons — none currently warrant advancement.

**To proceed, the following is needed:**
- Verified mechanism of action (MOA) data from DrugBank or primary pharmacology literature
- TFDA/SFDA package insert warnings, contraindications, and drug interaction data (currently blocking per data gap DG001)
- Any preclinical (in vitro/in vivo) evidence specifically linking enflurane exposure to mood stabilization
- Reassessment of route feasibility, since a chronic oral or alternative delivery formulation does not currently exist for this inhalational anesthetic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

