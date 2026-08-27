---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is a classic barbiturate anticonvulsant, established for epilepsy. The TxGNN model's top-ranked prediction for this drug is **Trigeminal Nerve Neoplasm**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags the score as a likely model-clustering artifact rather than a specific signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (barbiturate-class anticonvulsant; no Saudi Arabia license record available to confirm formally) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, primidone is a barbiturate anticonvulsant metabolized in the liver to phenobarbital and PEMA (phenylethylmalonamide), acting through GABA-A receptor modulation and broad-spectrum ion-channel suppression.

There is no known pathway linking this mechanism to tumour biology of the trigeminal nerve. The evidence pack's own annotation for this candidate states explicitly: the score (~0.9999) is nearly identical across many unrelated predicted indications for this drug, indicating a **score-clustering artifact** rather than a mechanistically specific signal — not a genuine repurposing hypothesis.

Notably, several *lower*-ranked predictions in this same evidence pack are mechanistically far more coherent and carry actual literature support: reflex/situational epilepsy subtypes (e.g., **micturition-induced seizures**, **audiogenic seizures**, **startle epilepsy**) align directly with primidone's established anticonvulsant mechanism and are backed by real (if largely indirect) clinical literature, including one Phase 3-grade RCT (NEJM 1985, PMID 3925335) comparing primidone to other established AEDs. These represent a more defensible research direction than the top-scored Trigeminal Nerve Neoplasm candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Primidone is not currently registered or marketed in Saudi Arabia (0 authorizations, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA package insert warnings/contraindications are flagged in the evidence pack as a **Blocking** data gap — this must be resolved before any S1 safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Trigeminal Nerve Neoplasm) has no clinical trial or literature support and no plausible mechanistic link to primidone's known pharmacology; the evidence pack itself identifies the score as a clustering artifact rather than a real signal. This candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action from DrugBank or primary literature
- If pursuing this drug further, redirect research focus to the higher-evidence reflex-epilepsy candidates in this same pack (micturition-induced seizures, audiogenic seizures, startle epilepsy — all L3–L4, with real literature including one RCT), rather than the top TxGNN score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

