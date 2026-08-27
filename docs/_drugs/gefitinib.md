---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor (EGFR-TKI) established for EGFR-mutation-positive non-small cell lung cancer (NSCLC).
The TxGNN model's top-ranked prediction is **Fibromatosis, Gingival** (score 99.89%), but this candidate is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic assessment explicitly states no pathological link to the EGFR pathway exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR-mutated non-small cell lung cancer (NSCLC) — no Saudi Arabia label text available; inferred from cited literature within this evidence pack |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is flagged as a data gap in this pack (DG002). However, the literature entries captured elsewhere in the pack consistently identify gefitinib as a selective EGFR tyrosine kinase inhibitor, clinically used for chemoresistant/EGFR-mutant NSCLC — this is well-established pharmacology, not a data gap in practice.

For the top-ranked prediction, **fibromatosis, gingival**, the evidence pack's own repurposing rationale states this is a reactive/benign fibrous gum overgrowth with no known EGFR-pathway pathology, and that the score reflects the TxGNN model alone — no clinical trials, ICTRP records, or PubMed literature were returned in the corresponding queries. This is consistent with an L5 evidence level (model prediction only) and a Hold recommendation.

Among the ten predicted indications supplied, two — **lung hilum carcinoma** (rank 5) and **pulmonary sulcus neoplasm** (rank 9) — are anatomic subtypes of NSCLC and therefore fall within gefitinib's established mechanistic domain. These reached L4 evidence and an S1 "Research Question" stage, but each is backed by only a single case report or an indirect narrative review, not indication-specific trial data. The remaining candidates (gingival fibromatosis, lung fibroma, IBMPFD, lung hamartoma, benign lung neoplasm, the Leukomelanoderma syndrome, lung germ cell tumor, junctional epidermolysis bullosa) either have no mechanistic rationale, no supporting evidence, or literature that is a keyword-match artifact unrelated to the actual disease (e.g., the one clinical trial retrieved for lung germ cell tumor enrolled head-and-neck/NSCLC patients, not germ cell tumor patients). None of the ten candidates currently meet a bar higher than L4.

## Clinical Trial Evidence

Currently no related clinical trials registered for Fibromatosis, Gingival.

## Literature Evidence

Currently no related literature available for Fibromatosis, Gingival.

## Saudi Arabia Market Information

Gefitinib is not marketed in Saudi Arabia (0 authorizations on record), so no product/license table is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, skin toxicity, and QT interval — literature within this evidence pack documents gefitinib-associated interstitial lung disease, QT prolongation, and acneiform skin eruptions as recognized class effects |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (gingival fibromatosis) has no mechanistic plausibility, no clinical trials, and no literature support — it is an L5, model-only signal. Even the two mechanistically plausible NSCLC-subtype candidates (lung hilum carcinoma, pulmonary sulcus neoplasm) are backed only by a single case report or indirect review, insufficient to justify progression.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a Blocking data gap (DG001) preventing S1 safety evaluation
- Confirmed DrugBank mechanism-of-action record (DG002)
- If pursuing the NSCLC-subtype candidates (lung hilum carcinoma, pulmonary sulcus neoplasm), targeted trial or case-series data specific to those anatomic presentations rather than general NSCLC or single case reports
- Re-evaluation of the TxGNN ranking pipeline for the gingival fibromatosis and similarly unrelated candidates, given the absence of any corroborating evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

