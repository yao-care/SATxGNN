---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 8
---

# Corifollitropin Alfa
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

# Corifollitropin Alfa: From Controlled Ovarian Stimulation to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa is a long-acting recombinant FSH (follicle-stimulating hormone) analog originally developed for controlled ovarian stimulation (COS) in women undergoing assisted reproductive technology (ART).
The TxGNN model predicts it may have activity in **Gastroduodenitis**, yet with **0 clinical trials** and **0 publications** directly supporting this direction, the prediction is entirely model-derived.
All eight top-ranked predicted indications stand at L5 evidence level, indicating that substantial biological validation is required before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Controlled ovarian stimulation (COS) in women undergoing assisted reproductive technology |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, corifollitropin alfa (DrugBank: DB09066) is a long-acting recombinant FSH analog that binds and activates the FSH receptor (FSHR), triggering the cAMP/PKA → MAPK/PI3K signaling cascade to stimulate follicular growth and maturation. Its efficacy in controlled ovarian stimulation for ART is well-established, with regulatory approval in the EU and other jurisdictions (marketed as **Elonva** by MSD/Merck). Saudi Arabia regulatory records show no approved licenses to date.

The connection between FSH receptor agonism and gastroduodenitis is biologically implausible under current knowledge. FSH receptors are predominantly expressed in gonadal granulosa cells and testicular Sertoli cells, with no documented role in gastroduodenal mucosal physiology. Gastroduodenitis is driven primarily by *H. pylori* infection, NSAID-induced mucosal damage, or acid hypersecretion — pathways entirely outside the FSH signaling axis. No published literature has linked FSH signaling to gastroduodenal mucosal protection or repair.

The TxGNN model's high confidence score (99.65%) most likely reflects a **graph topology artifact** rather than a true biological relationship. The model may have captured disease co-occurrence or ontological proximity within the knowledge graph without an underlying drug-disease mechanistic link. This prediction should be treated as a purely computational hypothesis and does not warrant progression to preclinical studies without a foundational mechanistic rationale being established first.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Corifollitropin alfa is **not approved or marketed in Saudi Arabia**. No SFDA authorization records are on file, and no licensed products exist in the Saudi market as of the data cutoff (2026-06-16).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, drug interactions) could not be retrieved for this candidate. The package insert from the originating regulatory authority (EMA/TFDA) should be consulted before any clinical evaluation. Resolving this data gap is flagged as a **Blocking** prerequisite (DG001) for a complete safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (gastroduodenitis) is supported by no clinical trials, no relevant literature, and no established mechanistic link to corifollitropin alfa's FSH receptor agonist mechanism. The biological rationale in the Evidence Pack explicitly identifies this as a probable knowledge-graph artifact. An L5 rating with no converging biological signal does not justify resource investment in this indication at this time.

**To proceed, the following is needed:**

- **Resolve MOA data gap (DG002):** Retrieve full mechanistic data from DrugBank API (DB09066) to enable proper mechanistic-link analysis across all predicted indications
- **Resolve safety data gap (DG001 — Blocking):** Download and parse the EMA/TFDA package insert to obtain warnings, contraindications, and precautions before any S1 safety screening can proceed
- **Basic science feasibility check:** Confirm whether FSH receptors are expressed in gastroduodenal mucosal tissue before committing to any preclinical work on this specific indication
- **Re-triage toward higher-plausibility candidates:** Two predictions in this pack warrant a preliminary mechanistic literature review ahead of this indication:
  - **Pulmonary Hypertension (Rank 6)** — FSH receptor expression has been reported in human pulmonary artery smooth muscle and endothelial cells, with observational data linking post-menopausal FSH elevation to pulmonary vascular remodeling; the net functional direction (pro- vs. anti-proliferative) requires clarification
  - **Migraine Disorder (Rank 2)** — Menstrual cycle FSH fluctuations are associated with menstrual migraine frequency, and FSH receptors have been detected in cerebrovascular tissue; the effect direction of FSH agonism on migraine remains undefined and should be explored via cortical spreading depression (CSD) animal models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

