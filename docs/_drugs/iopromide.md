---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is a non-ionic iodinated radiographic contrast medium used for diagnostic imaging (CT, angiography), not a therapeutic agent for any disease. TxGNN's top prediction proposes potential relevance to **osteoarthritis susceptibility**, but this ranking is supported by **0 clinical trials** and **0 publications** — it is a pure model artifact. Across all 10 ranked TxGNN candidates for this drug, none show genuine treatment-relevant evidence; the strongest literature hits describe iopromide only as an imaging tool used *during* diagnosis of these diseases, and one candidate (hemoglobinopathy) surfaces an adverse-event signal rather than an efficacy signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic radiographic/CT contrast imaging (iopromide is a non-ionic iodinated contrast medium; no formal "treatment indication" text is available in the evidence pack) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for iopromide (Data Gap, item DG002 in the evidence pack). Based on known information, iopromide is a non-ionic iodinated contrast medium administered intravascularly to enhance visualization on CT and angiographic imaging — it has no known pharmacodynamic activity on joint, cartilage, or bone biology.

For the top-ranked candidate, osteoarthritis susceptibility, the evidence pack itself states there is no plausible mechanistic link: iopromide has no known pharmacological target associated with OA susceptibility, and this pairing is a pure TxGNN knowledge-graph prediction with zero supporting literature or trials.

The next two candidates (osteoarthritis, rank 2; rheumatoid arthritis, rank 3) do return literature hits, but all of them describe iopromide being used as a contrast agent to *image* these diseases (CT-guided nerve blocks for hip pain, MRI/CT cartilage and synovitis quantification methodology) — not as a treatment. The TxGNN high scores most likely reflect co-occurrence of "drug + disease" in imaging-diagnostic contexts within the training knowledge graph, rather than any real therapeutic signal. No mechanistic rationale currently supports repurposing iopromide as a treatment for any of the 10 predicted indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked candidate (osteoarthritis susceptibility).

For context, lower-ranked candidates returned literature, but all are diagnostic/methodology papers, not treatment evidence:

| PMID | Year | Type | Journal | Key Findings | Related Candidate |
|------|-----|------|------|---------|---------|
| [11419151](https://pubmed.ncbi.nlm.nih.gov/11419151/) | 2001 | Case Series/Technical Report | European Radiology | CT-guided obturator nerve block technique for hip pain diagnosis/treatment — contrast used for procedural guidance, not OA therapy | Osteoarthritis (rank 2) |
| [9678042](https://pubmed.ncbi.nlm.nih.gov/9678042/) | 1998 | Methodology Study | Clin Orthop Relat Res | MRI cartilage volume/thickness measurement accuracy study using contrast-enhanced CT as reference — imaging methodology, not treatment | Osteoarthritis (rank 2) |
| [19435939](https://pubmed.ncbi.nlm.nih.gov/19435939/) | 2009 | Imaging Methodology Study | Radiology | Contrast-enhanced CT with digital bone masking to evaluate synovitis/bone erosion in RA — diagnostic tool evaluation, not therapy | Rheumatoid arthritis (rank 3) |
| [9094239](https://pubmed.ncbi.nlm.nih.gov/9094239/) | 1997 | Case Report | Pediatric Radiology | Lymphangiography (using contrast) in a neonate with Noonan syndrome — case report, not a hemoglobinopathy efficacy signal | Hemoglobinopathy (rank 9) |
| [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/) | 2006 | Case Report (Adverse Event) | Am J Hematol | Cerebral vaso-occlusive event following low-osmolar IV contrast in a sickle cell disease patient — **safety signal, not efficacy** | Hemoglobinopathy (rank 9) |

## Taiwan Market Information

Iopromide is not currently marketed in Taiwan (0 licenses on file); no product registration records are available.

## Safety Considerations

Please refer to the package insert for safety information (no TFDA warnings, contraindications, or DDI data are currently available — item DG001, flagged as a Blocking gap).

**Additional literature-derived safety signal:** One report (PMID 16628721) describes a cerebral vaso-occlusive event following low-osmolar intravenous contrast administration in a patient with sickle cell disease, suggesting iodinated contrast agents may carry elevated risk in hemoglobinopathy patients. This should be treated as a caution flag, not a repurposing opportunity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (osteoarthritis susceptibility) has zero clinical trial or literature support (L5). Even the best-evidenced candidates (osteoarthritis, rheumatoid arthritis; L4) are backed only by imaging-methodology papers that use iopromide as a diagnostic tool, not treatment evidence — and one candidate (hemoglobinopathy) surfaces an adverse-event signal rather than an efficacy signal. No mechanism of action data exists to support any therapeutic hypothesis.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank-confirmed mechanism of action — currently a High-severity data gap (DG002)
- A pharmacological or preclinical rationale connecting iodinated contrast agents to osteoarthritis, RA, or any other candidate's pathophysiology, since none currently exists
- If the hemoglobinopathy signal is pursued further, it should be evaluated as a contraindication/safety risk in sickle cell disease patients, not as a repurposing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

