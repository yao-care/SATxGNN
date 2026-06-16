---
layout: default
title: Clomifene
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Clomifene
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

# Clomifene: From Anovulatory Infertility to 46,XY Disorder of Sex Development due to Testicular Steroidogenesis Defect

## One-Sentence Summary

Clomifene is a selective estrogen receptor modulator (SERM) with a well-established role in inducing ovulation for anovulatory infertility, though no formal regulatory registration is on file in this data pack.
The TxGNN model generated **10 predicted indications** across reproductive and chromosomal disorders; the top-ranked prediction is **46,XY disorder of sex development due to testicular steroidogenesis defect** (score 99.90%).
However, **no clinical trials** and **no published literature** currently support this specific direction, and the mechanistic link is critically weak — this prediction is assessed as a knowledge graph false positive.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anovulatory infertility / ovulation induction — no regulatory authorization on file |
| Predicted New Indication | 46,XY disorder of sex development due to testicular steroidogenesis defect |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current data pack. Based on established pharmacological knowledge, Clomifene acts as a SERM by blocking hypothalamic estrogen receptors, thereby reducing negative feedback on GnRH release. This increases pulsatile FSH and LH secretion from the anterior pituitary. In males, the resulting surge in LH can stimulate Leydig cells in the testes to upregulate steroid synthesis — and it is this gonadotropin-stimulating pathway that likely caused the TxGNN knowledge graph to draw a link to disorders of testicular steroidogenesis.

However, 46,XY disorder of sex development due to testicular steroidogenesis defect is not a signalling problem — it is an enzymatic machinery failure. Mutations in steroidogenic enzymes such as StAR, CYP11A1, or CYP17A1 operate downstream of LH receptor activation. Even if Clomifene successfully raises endogenous LH to supraphysiological levels, that signal cannot be converted into functional steroid hormones because the enzymatic steps required to do so are broken. Increased upstream stimulation cannot bypass the enzymatic blockade.

This is most likely a knowledge graph false positive: TxGNN correctly identified the pharmacological connection between Clomifene and the hypothalamic-pituitary-gonadal (HPG) axis, but the model lacks the resolution to distinguish between signalling defects (potentially amenable to upstream stimulation) and enzymatic synthesis defects (not amenable to this approach).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

No marketing authorizations on file for Clomifene.

## Safety Considerations

Please refer to the package insert for safety information.

---

## Supplementary: All Predicted Indications at a Glance

This Evidence Pack is a multi-indication evaluation (candidate ID: TW-DB00882-multi). The table below summarizes all 10 TxGNN predictions for reference.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Mechanistic Assessment |
|------|----------------------|-------------|----------------|----------------|------------------------|
| 1 | 46,XY DSD due to testicular steroidogenesis defect | 99.90% | L5 | **Hold** | LH stimulation cannot bypass downstream enzyme defects (StAR/CYP11A1/CYP17A1) |
| 2 | Longitudinal vaginal septum | 99.87% | L5 | **Hold** | Structural Müllerian fusion defect; no pharmacological mechanism exists |
| 3 | Transverse vaginal septum | 99.87% | L5 | **Hold** | Same as above; assessed as knowledge graph false positive |
| 4 | Symptomatic fragile X syndrome in female carrier (FXPOI) | 99.69% | L5 | Research Question | Indirect: Clomifene may stimulate residual follicles in FXPOI, but ovarian reserve is already compromised |
| 5 | Blepharophimosis-epicanthus inversus-ptosis (BPES) | 99.61% | L5 | Research Question | FOXL2-related POI subgroup may respond to ovulation induction; eyelid defect itself has no drug target |
| 6 | BPES due to 3q23 rearrangement | 99.58% | L5 | Research Question | Same rationale as BPES; rarer genetic subtype with even lower research feasibility |
| 7 | Partial trisomy/tetrasomy of chromosome 18p | 99.54% | L5 | **Hold** | Chromosomal copy number anomaly; no estrogen receptor or HPG axis target exists |
| 8 | Partial trisomy/tetrasomy of chromosome 5p | 99.54% | L5 | **Hold** | Structural chromosomal anomaly (includes Cri du Chat region); no mechanism |
| 9 | Partial trisomy/tetrasomy of chromosome 12p | 99.54% | L5 | **Hold** | Pallister-Killian syndrome area; no pharmacological target for Clomifene |
| 10 | Ovarian remnant syndrome | 99.52% | **L4** | Research Question | Best-supported candidate: 1990 case series reports Clomifene used to stimulate and localize residual ovarian tissue prior to surgery |

> **Note on Rank 10 (Ovarian Remnant Syndrome):** Although ranked lowest among the 10 predictions, this candidate has the strongest mechanistic plausibility and the only available literature evidence (PMID [2216258](https://pubmed.ncbi.nlm.nih.gov/2216258/)). Clomifene was used diagnostically to stimulate residual ovarian tissue for localization before repeat surgery. This is a niche diagnostic utility rather than therapeutic treatment, but represents the only repurposing direction in this pack with real-world clinical data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction scores very high (99.90%) but represents a mechanistically implausible candidate — Clomifene acts upstream of the enzymatic defects that define this condition, making the prediction almost certainly a knowledge graph false positive. All 10 predicted indications are either false positives (structural/chromosomal anomalies) or very early-stage research questions with no clinical evidence. The only candidate with any supporting literature is Ovarian Remnant Syndrome (rank 10, L4), and even that evidence dates from 1990 and describes diagnostic rather than therapeutic use.

**To proceed, the following is needed:**
- Obtain MOA data from DrugBank (data gap DG002) to enable systematic mechanistic analysis across all 10 candidates
- Obtain TFDA/SFDA package insert warnings and contraindications (data gap DG001) before any safety evaluation can begin
- For Ovarian Remnant Syndrome specifically: conduct a targeted literature review to identify whether more recent evidence exists beyond the 1990 case series, then reassess as a potential Research Question candidate
- For the FOXL2/BPES and FXPOI candidates: consult reproductive endocrinology experts to assess whether Clomifene's SERM mechanism could have meaningful clinical utility in these ultra-rare POI subtypes
- Do not progress any chromosomal copy number or structural Müllerian anomaly candidates further — these are false positives that do not warrant additional investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

