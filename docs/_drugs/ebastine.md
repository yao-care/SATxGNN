---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the specified v5 report template to turn this Evidence Pack into the formatted markdown report.

# Ebastine: From Allergic Rhinitis to Coronary Artery Disease

## One-Sentence Summary

Ebastine (DrugBank DB11742) is a second-generation H1-antihistamine, generally known for treating **allergic rhinitis and chronic urticaria** (note: this original-indication detail is background pharmacological knowledge, not present in the Evidence Pack itself, since `original_indications` and Saudi Arabia licenses are both empty). The TxGNN model predicts it may be effective for **Coronary Artery Disease**, but this is currently supported only by **0 clinical trials** and **1 (unclassified) publication**, so the evidence base is very thin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in Evidence Pack (no Saudi Arabia licenses, `original_indications` empty). Generally known as allergic rhinitis / chronic idiopathic urticaria — unverified against a local label |
| Predicted New Indication | Coronary Artery Disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002, High severity). Based on known information, ebastine is a second-generation, non-sedating H1-antihistamine, and its efficacy in allergic conditions is well established; a direct pharmacological rationale for coronary artery disease is not documented in this Evidence Pack.

The only supporting literature (PMID 18004755) is not a study of ebastine's clinical effect at all — it is a homology-modeling/molecular-docking study of **cytochrome P450 2J2 (CYP2J2)**, an enzyme that epoxidizes arachidonic acid into eicosatrienoic acids (EETs) implicated in coronary artery disease and hypertension. TxGNN appears to have linked ebastine to coronary artery disease (and, in the second-ranked prediction, myocardial ischemia) through this CYP2J2-related pathway in its knowledge graph, since both predictions cite the identical paper.

This is a plausible but unverified mechanistic hypothesis rather than direct evidence: the paper does not study ebastine as a CYP2J2 substrate/inhibitor, and its `classification` and `relevance` fields are both still marked "pending." Coronary artery disease and myocardial ischemia are clinically overlapping (ischemic heart disease spectrum), which is consistent with both diseases receiving similar TxGNN scores (99.18% and 99.10%) from the same underlying signal — but this should be treated as a single, unconfirmed hypothesis rather than two independent lines of evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Mechanistic / in-silico (preclinical) | Proteins | Homology modeling and molecular docking of human CYP2J2, the enzyme that epoxidizes arachidonic acid into eicosatrienoic acids linked to coronary artery disease and hypertension; does not directly evaluate ebastine's clinical effect on CAD (classification/relevance still marked "pending") |

*Note: the same single paper is the only literature cited for the second predicted indication (myocardial ischemia, score 99.10%) as well.*

---

## Saudi Arabia Market Information

Ebastine is not currently marketed in Saudi Arabia — 0 authorizations on record (`taiwan_regulatory.total_licenses = 0`, `licenses = []`).

---

## Safety Considerations

Please refer to the package insert for safety information.

- Key warnings, contraindications, and DDI data are all currently unavailable (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` all report no data / not found).
- Data Gap **DG001** (TFDA/Saudi package insert warnings & contraindications) is flagged as **Blocking severity** — its stated impact is that this candidate **cannot proceed to the S1 safety pre-assessment stage** until resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The coronary artery disease prediction rests on a single, mechanistically indirect, and still-unclassified paper about a metabolic enzyme (CYP2J2) rather than any direct study of ebastine — with zero registered clinical trials, this is model-prediction-only evidence (L5).
- A Blocking data gap (DG001: no package insert / safety data) means a required safety pre-assessment (S1) cannot even begin, and the drug is not marketed in Saudi Arabia at all.

**To proceed, the following is needed:**
- Resolve DG001: obtain the package insert (warnings, contraindications) to unblock the S1 safety pre-assessment
- Resolve DG002: obtain detailed MOA data from DrugBank to properly evaluate the CYP2J2 mechanistic link
- Complete classification/relevance review of PMID 18004755 to confirm whether it actually supports a CAD-related mechanism for ebastine
- Search for additional preclinical or clinical evidence directly connecting ebastine (or its active metabolite carebastine) to cardiovascular/ischemic outcomes
- Establish a DDI profile, since the current query returned "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

