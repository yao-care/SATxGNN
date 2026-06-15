---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a selective neurokinin-1 (NK1) receptor antagonist, clinically used for the prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV). The TxGNN model ranks **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)** as the top predicted new indication with a score of **99.97%**, however **no clinical trials or published literature** currently support this specific pairing. Across all 10 top predictions in this run, the evidence base remains entirely at the model-prediction level (L5), with no directly relevant clinical data found for any candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV); postoperative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 — Model prediction only; no supporting clinical studies |
| Saudi Arabia Market Status | ✗ Not Marketed (0 SFDA authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (data gap DG002). Based on established pharmacology, aprepitant is an NK1 receptor antagonist that selectively blocks the binding of substance P (SP) in the central and peripheral nervous system. Its proven efficacy in CINV/PONV is mediated by interrupting SP-driven emetic signaling in the brainstem's area postrema and nucleus tractus solitarius.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare X-linked disorder caused by gain-of-function mutations in the *AVPR2* gene, which encodes the V2 vasopressin (antidiuretic hormone) receptor in the renal collecting duct. These mutations cause constitutive activation of aquaporin-2 insertion, resulting in persistent free water retention and dilutional hyponatremia — entirely independent of circulating vasopressin levels. The V2 receptor/aquaporin pathway and the NK1R/Substance P axis have no established direct pharmacological intersection.

The TxGNN model's high score most likely reflects shared neuroendocrine nodes in the underlying knowledge graph — specifically hypothalamic osmotic regulatory circuits that anatomically converge on both neuropeptide and vasopressin-related pathways — rather than a true mechanistic bridge. This prediction is best interpreted as a graph-topology signal requiring independent mechanistic validation before any translational consideration is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Aprepitant is not registered with the Saudi Food and Drug Authority (SFDA). No approved products, dosage forms, or indication authorizations are recorded in the Saudi Arabia market database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top TxGNN predictions for aprepitant are at evidence level L5 (model prediction only), aprepitant holds no SFDA registration, and the mechanistic link between NK1R antagonism and the rank-1 indication (NSIAD/AVPR2 gain-of-function pathology) is indirect and currently unsupported by any experimental data. The literature entries retrieved for ranks 3 and 6 were confirmed as false-positive matches unrelated to aprepitant or the target indications.

One candidate warrants separate tracking: **subarachnoid hemorrhage (rank #9, score 99.85%)** carries the strongest mechanistic rationale in this prediction set. Post-SAH neurogenic inflammation involves massive SP release, cerebral vasospasm, and neurogenic edema — all NK1R-mediated processes — and preclinical SAH models have shown that NK1R antagonism reduces brain water content and improves neurological outcomes (though not using aprepitant specifically). This indication should be escalated to a focused literature review before a final Hold decision is applied.

**To proceed, the following is needed:**

- Retrieve the aprepitant package insert (SFDA or FDA/EMA source) to populate warnings, contraindications, and drug interactions (data gap DG001 — currently Blocking)
- Confirm full MOA and pharmacodynamic profile via DrugBank API (data gap DG002)
- For NSIAD: evaluate any published NK1R/V2R crosstalk data in hypothalamic–renal neuroendocrine circuits; if none exists, formally close this candidate
- For SAH (rank #9): conduct a targeted PubMed search for "NK1 receptor antagonist + subarachnoid hemorrhage" to determine whether animal model evidence supports upgrading to L4, and if so, initiate a separate evaluation report for this indication
- For any indication that reaches L3 evidence: assess SFDA registration pathway requirements before advancing to clinical planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

