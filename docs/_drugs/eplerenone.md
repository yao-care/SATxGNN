---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Eplerenone: From Hypertension/Heart Failure to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Eplerenone (DrugBank DB00700) is a selective aldosterone (mineralocorticoid receptor) antagonist generally used for hypertension and chronic heart failure; however, this evidence pack contains no confirmed original-indication or regulatory license record for the drug in this jurisdiction. The TxGNN model predicts potential efficacy for **pulmonary hypertension with unclear multifactorial mechanism** (score **99.50%**), but currently **0 clinical trials** and **0 disease-specific publications** directly support this prediction — the association is based on the computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (no market license record); generally known as hypertension / chronic heart failure post-MI |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (this jurisdiction) | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002, High severity). Based on generally known pharmacology, eplerenone is a selective mineralocorticoid receptor (aldosterone) antagonist, structurally related to spironolactone but with greater receptor selectivity and fewer anti-androgenic effects. It is conventionally used for hypertension and chronic heart failure following myocardial infarction.

Mechanistically, chronic aldosterone/mineralocorticoid receptor activation is implicated in vascular remodeling, perivascular fibrosis, and endothelial dysfunction — processes that also feature in the pathogenesis of several pulmonary hypertension subtypes. This offers a biologically plausible, but currently unverified, rationale for TxGNN linking eplerenone to "pulmonary hypertension with unclear multifactorial mechanism."

It is worth noting that a closely related predicted term — "pulmonary hypertension owing to lung disease and/or hypoxia" (rank 2) — received an identical TxGNN score (99.50%) and returned 20 PubMed hits, whereas the rank-1 indication above returned none. On review, however, those 20 papers are general hypoxia-biology/neuroscience/oncology articles retrieved by keyword overlap ("hypoxia") rather than studies specifically evaluating eplerenone in pulmonary hypertension — none of the abstracts mention eplerenone. This tied-score, sibling-disease pattern is typical of TxGNN's ontology structure and should not be read as independent confirmation. As such, no indication in this cluster currently has genuine drug-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No marketing authorizations are on record for eplerenone in this jurisdiction (market status: 未上市 / not marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: retrieval of the official TFDA package insert warnings/contraindications is flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet pass initial safety screening (S1) until that document is obtained. The drug interaction database query also returned no results (`not_found`).)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction currently rests on the TxGNN model score alone (Evidence Level L5) — there are no clinical trials or eplerenone-specific literature supporting efficacy in pulmonary hypertension, the drug has no market presence in this jurisdiction, and a Blocking-severity safety data gap prevents initial safety screening.

**To proceed, the following is needed:**
- Obtain the official TFDA/manufacturer package insert (warnings, contraindications) to resolve the Blocking gap (DG001) and enable S1 safety screening
- Obtain confirmed original indication and mechanism-of-action documentation from DrugBank/regulatory sources (DG002)
- Run a targeted literature and clinical-trial search combining "eplerenone" specifically with pulmonary hypertension terms, since current hits under the sibling term (rank 2) are generic hypoxia-biology papers rather than drug-specific evidence
- Re-query the drug-interaction database via an alternate source, since the current query returned "not_found"
- If pursuing further, evaluate the sibling predicted term (rank 2, same score) in parallel, as ontology-adjacent terms may warrant a combined literature strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

