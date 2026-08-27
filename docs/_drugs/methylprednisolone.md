---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a synthetic glucocorticoid broadly used to suppress inflammatory and autoimmune activity across many conditions (specific original-indication and label data are not available in this evidence pack). The TxGNN model predicts it may be effective for **Alopecia Areata**, with **3 directly relevant clinical trials** and **10 supporting publications** (out of a larger, partly mismatched evidence set) currently backing this direction — including one completed Phase 4 prospective study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack — no Saudi Arabia licenses/label text on record; TFDA package insert data is a blocking gap (DG001) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, methylprednisolone is a synthetic glucocorticoid that binds the glucocorticoid receptor to broadly suppress pro-inflammatory gene transcription, cytokine release, and immune cell (including T-cell) activity — the basis for its established anti-inflammatory and immunosuppressive use across a wide range of autoimmune and inflammatory diseases.

Alopecia areata is now understood to be primarily a T-cell-mediated autoimmune attack on the hair follicle, in which cytotoxic T cells break follicular immune privilege and drive inflammatory infiltration around the bulb. Because methylprednisolone's core mechanism is broad immunosuppression, high-dose pulse dosing is mechanistically plausible for reducing this peri-follicular inflammatory attack and supporting hair regrowth in severe or treatment-resistant disease.

This is not a purely speculative model prediction: it is corroborated by a completed Phase 4 prospective study of oral mega-pulse methylprednisolone in severe, therapy-resistant alopecia areata, along with numerous retrospective cohorts and case series spanning several decades. What is still missing is a large, adequately powered Phase 3 RCT, which keeps the evidence level at L2 rather than L1.

---

## Clinical Trial Evidence

The evidence pack's raw trial list contains a substantial number of trials that were retrieved under the "alopecia areata" query but are actually about unrelated conditions (e.g., systemic lupus erythematosus, prostate cancer, primary headache) — these are excluded below as disease/drug mismatches. Trials genuinely relevant to alopecia areata:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone evaluated in severe, therapy-resistant alopecia areata; systemic pulse glucocorticoids effective in widespread AA but not clearly in totalis/universalis/ophiasic subtypes. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (Observational) | Completed | 296 | Prospective observational safety/effectiveness study of tofacitinib in alopecia, with participants receiving it with or without adjuvant prednisolone; not a direct methylprednisolone efficacy trial but relevant as corticosteroid-adjuvant context. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared DERMOJET vs. standard syringe for intralesional corticosteroid injection technique in alopecia areata; addresses delivery method rather than drug efficacy. |

*Note: Several additional trials in the raw evidence set (e.g., NCT04925934, NCT01972217, NCT05162586, NCT03616912) were graded "B" for relevance in the source data but their titles/summaries describe SLE or unrelated oncology studies — these appear to be query/classification errors and were excluded from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | RCT | Open Access Maced J Med Sci | Methotrexate combined with mini-pulse methylprednisolone evaluated in severe alopecia areata (Vietnamese cohort); supports combination pulse-steroid regimens in refractory disease. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, side effects, and prognostic factors across different corticosteroid pulse regimens in AA. |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Review (Systematic) | Dermatol Ther (Heidelb) | Systematic review of cyclosporine with and without systemic corticosteroids in AA treatment. |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | Int J Dermatol | Reviews treatment options for alopecia totalis/universalis; notes no therapy is FDA-approved, situating corticosteroid pulse therapy among available options. |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort | Indian J Dermatol Venereol Leprol | Evaluates IV methylprednisolone pulse therapy in severe, extensive, treatment-resistant AA. |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Cohort | J Dermatolog Treat | Combination cyclosporine + methylprednisolone in severe AA; addresses relapse after cyclosporine discontinuation. |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohort (Retrospective) | Dermatol Ther | Retrospective comparison of methylprednisolone alone vs. methylprednisolone + methotrexate in 26 patients with extensive AA. |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Cohort (Retrospective) | Indian J Dermatol | Examines sex differences in AA response to steroid pulse therapy. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | Reviews pediatric pulse-dose corticosteroid dosing/administration practices and side effects in AA. |
| [36681881](https://pubmed.ncbi.nlm.nih.gov/36681881/) | 2023 | Cohort (Retrospective) | J Eur Acad Dermatol Venereol | Long-term patient-reported experience with methylprednisolone pulse ± methotrexate in a French single-center cohort. |

*10 additional older case series/cohort papers (e.g., PMID 9777767, 22426909, 21592197, 23336179, 12746668, 25872976) further support pulse methylprednisolone use in severe AA but were deprioritized here per the RCT > Review > Case-report ranking rule.*

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this evidence pack — DG001 is a Blocking-severity gap preventing S1 safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound (T-cell-mediated autoimmune disease responsive to broad immunosuppression), and one completed Phase 4 prospective trial plus multiple retrospective cohorts and a Phase-adjacent RCT support real-world efficacy of pulse methylprednisolone in severe/treatment-resistant AA. However, no large Phase 3 RCT exists, and critical local safety/regulatory data are missing.

**To proceed, the following is needed:**
- TFDA/local package insert with warnings, contraindications, and DDI data (Blocking gap DG001)
- Detailed mechanism of action data from DrugBank (High-severity gap DG002)
- Confirmation of local market/regulatory pathway, since this product currently shows 0 authorizations and "Not Marketed" status
- A larger controlled (ideally Phase 3 RCT) trial to move the evidence level from L2 toward L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

