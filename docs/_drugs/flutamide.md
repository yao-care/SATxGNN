---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a nonsteroidal antiandrogen historically used as part of combined androgen blockade for prostate cancer. The TxGNN model's top-ranked prediction for this candidate is **"Prostate Cancer/Brain Cancer Susceptibility"** (score 99.98%), but this composite label currently has **zero clinical trials and zero publications** directly supporting it — the prostate-cancer component simply restates flutamide's known mechanism, while the brain-cancer component is an unsupported embedding-level association.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (established nonsteroidal antiandrogen use; not derived from Saudi Arabia registration data — no local licenses exist) |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap, DG002). Based on known pharmacology, flutamide is a nonsteroidal androgen receptor (AR) antagonist, traditionally used as a component of combined androgen blockade (with LHRH agonists) in prostate cancer — an established, decades-old use rather than a genuinely novel repurposing target.

The predicted indication in this record, "prostate cancer/brain cancer susceptibility," is a composite entity. Its prostate-cancer portion is mechanistically coherent with flutamide's known AR-antagonist activity and overlaps with the better-supported "male reproductive organ cancer" prediction elsewhere in this evidence pack (rank 6, L1 evidence). However, the brain-cancer portion has no known mechanistic basis — there is no data in this pack on AR expression in brain tumors or on flutamide's blood-brain-barrier penetration, and the association appears to be a pure TxGNN embedding-level artifact rather than a biologically grounded hypothesis.

Given this, the prediction as a whole should be treated as model output only, not as a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

No market authorization records exist for flutamide in Saudi Arabia — the drug is not currently marketed there (0 licenses on file).

## Cytotoxicity

Flutamide is a hormonal antineoplastic agent (AR-targeted antiandrogen) used in prostate cancer treatment, not a conventional cytotoxic chemotherapy drug. Formal DrugBank category and toxicity data were not returned in this evidence pack (query succeeded but content not captured; TFDA/SFDA package insert data is a blocking gap — DG001).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (AR antagonist) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests (ALT/AST) — flutamide carries a known hepatotoxicity risk noted elsewhere in this evidence pack; standard renal function/CBC monitoring per oncology practice |
| Handling Protection | Not classified as a cytotoxic hazardous drug; follow standard precautions per package insert once available |

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — DG001, blocking severity.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting clinical trials or literature (L5, model-prediction-only), and its brain-cancer component lacks any mechanistic rationale. The score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently blocking (DG001)
- DrugBank-sourced mechanism of action detail — currently high-priority gap (DG002)
- Dedicated literature/trial search specifically for AR expression or antiandrogen activity in CNS/brain tumors, since none currently exists
- **Note for reviewers:** rank 6 in this same evidence pack ("male reproductive organ cancer") carries far stronger evidence (L1, Phase 3 completed trials, "Proceed with Guardrails") and may be a more productive candidate to prioritize than this top-ranked but evidence-free prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

