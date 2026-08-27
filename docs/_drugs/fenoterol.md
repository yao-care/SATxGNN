---
layout: default
title: Fenoterol
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 8
---

# Fenoterol
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

# Fenoterol: From Bronchodilator (Asthma/COPD) to Multiple System Atrophy

## One-Sentence Summary

Fenoterol is a β2-adrenergic receptor agonist internationally known as a bronchodilator for asthma/COPD; it is **not currently marketed in Saudi Arabia**, so no local approved-indication or MOA record exists in this Evidence Pack. The TxGNN model's top-ranked prediction is **Multiple System Atrophy (MSA)**, but the accompanying mechanistic rationale itself flags this as a **potential safety concern rather than a therapeutic signal** (peripheral vasodilation could worsen the orthostatic hypotension already present in MSA), and there are **0 clinical trials and 0 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed for Saudi Arabia (drug not marketed; `original_indications` empty). Internationally known drug class: β2-adrenergic agonist bronchodilator (asthma/COPD) |
| Predicted New Indication | Multiple System Atrophy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on generally known pharmacology, fenoterol is a short-acting β2-adrenergic receptor agonist used internationally as a bronchodilator, and in some markets historically as a tocolytic (uterine relaxant) — neither of these established uses is regulatory-confirmed for Saudi Arabia, where the drug has no licenses on file.

For the top-ranked prediction, the model's own repurposing rationale is **not supportive** of therapeutic benefit: MSA commonly involves autonomic degeneration and orthostatic hypotension, and fenoterol's peripheral vasodilatory (β2) effect could plausibly **worsen** postural blood pressure control rather than treat the disease. The high TxGNN score most likely reflects network proximity within cardiovascular/autonomic pathways rather than a validated treatment direction, and the rationale text explicitly frames this as a safety concern, not an efficacy hypothesis.

It is worth noting that lower-ranked candidates in this pack — Raynaud's disease (rank 5) and sinoatrial node disease (rank 7–8) — have mechanistically more coherent (vasodilation for vasospasm; β1 cross-activity for chronotropic support) rationales and were scored "Research Question" rather than "Hold." These may be more productive starting points than the top-ranked MSA signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

No licensed products are currently registered in Saudi Arabia for fenoterol (`total_licenses: 0`, market status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (MSA) carries a mechanistic rationale that points toward potential harm (worsening orthostatic hypotension) rather than benefit, and is backed by zero clinical trials or publications (L5, model prediction only). Combined with the complete absence of local regulatory, MOA, and safety data, there is no basis to advance this candidate at present.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank or other primary source — currently a High-severity data gap
- Independent pharmacological/clinical review of whether the MSA safety concern can be ruled out, or whether the pipeline should re-rank toward Raynaud's disease or sinoatrial node disease as more mechanistically coherent candidates
- DDI data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

