---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Febuxostat: From Hyperuricemia (Gout) to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor generally used to lower uric acid in gout/hyperuricemia (its Taiwan license data itself is not available in this evidence pack). TxGNN predicts a possible link to **renal hypouricemia**, but the model score is not supported by good evidence — only **1 low-quality clinical trial** and **2 review-level publications** exist, and the underlying pharmacology may actually run in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia/gout (based on known drug class — xanthine oxidase inhibitor; no Taiwan license record found, see data gap below) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supportive trial/mechanism confirmation) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information present in the evidence itself, febuxostat is known to work as a **xanthine oxidase inhibitor**, reducing uric acid production — this is the basis of its established gout/hyperuricemia use.

The prediction pairs this drug with **renal hypouricemia**, a condition of *abnormally low* serum urate. This is mechanistically the opposite of what febuxostat does: excessive lowering of uric acid (i.e., drug-induced hypouricemia) is a known **adverse effect** of febuxostat, not a therapeutic target. The evidence pack's own rationale flags this directly as a likely false positive — TxGNN's embedding may be confusing "a side effect the drug causes" with "a disease the drug treats."

Two lower-ranked but mechanistically more coherent candidates appear in the same evidence pack — HPRT partial deficiency (Kelley-Seegmiller syndrome) and Lesch-Nyhan syndrome — where xanthine oxidase inhibition (allopurinol-class) is already used clinically to manage the resulting hyperuricemia. These may be worth tracking separately as research questions, even though they scored lower and currently have only case-report-level evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Studied uric acid control's effect on stone recurrence and renal function in hyperuricemia-related calculi. Relevance graded **C**: the "title" field is only an institution name (Dept. of Urology, Shanghai Xu-hui Central Hospital), not an actual study title, and trial status is Unknown — insufficient to confirm relevance to febuxostat/renal hypouricemia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical rheumatology | Narrative review of hypouricemia etiology for rheumatologists; not specific to febuxostat as treatment. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review | Internal Medicine (Tokyo) | Case discussion of a renal hypouricemia (RHUC) patient in whom febuxostat is mentioned in the context of managing exercise-induced acute kidney injury risk — not as a treatment for hypouricemia itself. |

---

## Taiwan Market Information

Febuxostat currently holds **no marketing authorization in Taiwan** (0 licenses on record). TFDA package insert data could not be retrieved (data gap DG001, Blocking severity) — this alone prevents any safety pre-assessment (S1 stage) for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all unavailable in the current evidence pack — TFDA package insert retrieval is a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (renal hypouricemia) is mechanistically inconsistent with febuxostat's known pharmacology — the drug lowers uric acid, and hypouricemia is documented as an adverse effect, not a treatable target. Combined with L5 evidence (model prediction only), a single grade-C clinical trial, and review-level-only literature, this candidate does not warrant advancement past S0.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, Blocking — currently prevents any S1 safety pre-assessment)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- If pursuing repurposing research for febuxostat at all, consider redirecting to the mechanistically stronger candidates in this same pack (HPRT partial deficiency, Lesch-Nyhan syndrome), which align with febuxostat's actual uric-acid-lowering action — though both currently rest on case-report-level evidence only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

