---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor Lysis Syndrome (Hyperuricemia) to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase used to rapidly lower plasma uric acid in patients undergoing chemotherapy for hematologic malignancies (tumor lysis syndrome). The TxGNN model predicts it may be relevant to **Renal Hypouricemia**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a model-generated hypothesis only, and the underlying rationale itself flags the mechanistic direction as questionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia associated with tumor lysis syndrome in hematologic malignancies (general drug knowledge — not confirmed by a Saudi Arabia filing, as the product is not marketed there) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rasburicase is a recombinant urate oxidase (uricase) that directly catalyzes the enzymatic oxidation of uric acid into allantoin, a far more water-soluble compound that is readily excreted renally. Its established clinical role is to rapidly and profoundly **lower** plasma uric acid in patients at risk of tumor lysis syndrome during chemotherapy.

Renal hypouricemia, however, is a condition defined by **abnormally low** serum uric acid caused by a defect in renal tubular urate reabsorption (e.g., URAT1/GLUT9 transporter mutations) — the opposite metabolic direction from hyperuricemia. The evidence pack's own repurposing rationale acknowledges this: the mechanistic link is described as "near-synonymous" with the drug's known pharmacology (both concern uric acid regulation) rather than genuine new pathological insight, and explicitly notes there is no trial or literature support for using a uric-acid-lowering enzyme in a disease that already has pathologically low uric acid.

This pattern is consistent with a TxGNN embedding-similarity artifact — the model likely associates rasburicase with "uric acid"-related disease terms broadly, without distinguishing direction of effect. The same caution applies even more strongly to ranks 3–10 (hepatic porphyria, copper-associated cirrhosis, portal hypertension disorders, hepatopulmonary syndrome, portal vein thrombosis, phenylalanine metabolism disorder), for which the rationale text explicitly states there is **no identifiable mechanistic link** at all. Rank 2 (HGPRT partial deficiency / Kelley-Seegmiller syndrome) is the one prediction with a biologically coherent rationale, since hyperuricemia is a downstream complication of that disorder — but it likewise has zero supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Rasburicase is currently **not marketed** in Saudi Arabia (0 authorizations on file); no license or approved-indication records are available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA package insert warnings and contraindications are listed as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Renal Hypouricemia) has no clinical or literature support, and the evidence pack's own mechanistic rationale flags it as a directionally questionable extrapolation rather than a validated new pathology link — a uric-acid-lowering enzyme is unlikely to be therapeutic for a disease of already-low uric acid. Combined with the drug's non-marketed status in Saudi Arabia and complete absence of safety/DDI data, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Formal, sourced mechanism-of-action documentation (DrugBank query) — currently a High-severity gap (DG002)
- A clinical or preclinical rationale that addresses the directional mismatch between rasburicase's hyperuricemia-lowering effect and a hypouricemic target condition
- DDI and contraindication data before any safety pre-assessment (S1) can begin
- If rank 2 (HGPRT partial deficiency) is pursued instead, at minimum case-report or preclinical evidence connecting rasburicase to that indication, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

