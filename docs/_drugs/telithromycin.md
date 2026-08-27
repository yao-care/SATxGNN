---
layout: default
title: Telithromycin
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
---

# Telithromycin
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

# Telithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Telithromycin is a ketolide-class antibacterial agent; the evidence pack does not record its originally approved indication or detailed mechanism of action (both flagged as data gaps). The TxGNN model predicts it may be relevant to **Hyperamylasemia**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licenses on file; telithromycin is classified as a ketolide antibiotic — semi-synthetic erythromycin derivative) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (DG002, severity: High) — the `original_moa` field is a data gap. Based on information embedded elsewhere in this evidence pack, telithromycin is a ketolide antibiotic that acts by binding the bacterial 50S ribosomal subunit to inhibit protein synthesis, and it has documented activity against atypical respiratory pathogens (e.g., *Chlamydophila*).

The model's own rationale for this specific candidate is explicit and negative: *"There is no known mechanism linking the protein-synthesis-inhibiting action of ketolide antibiotics to pancreatic amylase metabolism; no clinical or literature evidence exists — this is a pure prediction."* Hyperamylasemia is a metabolic/pancreatic finding with no established pharmacological connection to antibacterial protein-synthesis inhibition.

Because both the mechanistic pathway and any supporting evidence are absent, this candidate should be read as an unvalidated model signal rather than a mechanistically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Telithromycin is not currently registered or marketed in Saudi Arabia (0 authorizations on file; `market_status`: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA package-insert warnings/contraindications are recorded as a **Blocking** data gap — DG001 — meaning no safety pre-screening (S1) can be completed until this is resolved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are zero clinical trials or publications connecting telithromycin to hyperamylasemia (Evidence Level L5, decision stage S0) — this is an unvalidated model output. In addition, a Blocking data gap on TFDA labeling (warnings/contraindications) prevents even a baseline safety assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to clear the Blocking gap and enable S1 safety screening
- DrugBank/mechanism-of-action data to evaluate biological plausibility for hyperamylasemia
- Targeted literature or preclinical search specifically on telithromycin (not just the ketolide class) and pancreatic amylase pathways
- Re-evaluation once any clinical or mechanistic evidence emerges, or consideration of higher-evidence candidates in this same prediction set (e.g., rank 6, septicemic plague, currently at L4/S1) as an alternative priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

