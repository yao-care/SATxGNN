---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell Carcinoma/Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-kinase inhibitor (VEGFR1-3, PDGFR-β, RAF/MEK/ERK pathway) originally established for renal cell carcinoma and hepatocellular carcinoma. The TxGNN model predicts it may be effective for **Liposarcoma**, with **2 clinical trials** (1 flagged as a data-linkage error) and **8 publications** currently supporting this direction — evidence remains at a preclinical/early-clinical stage rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (RCC), Hepatocellular carcinoma (HCC) — inferred from trial/literature context in this pack; no Saudi Arabia-specific approved-indication text is on file (0 licenses) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record for sorafenib is a data gap (DG002). However, the literature evidence collected in this pack consistently describes sorafenib (BAY 43-9006) as a multi-target kinase inhibitor acting on VEGFR1–3, PDGFR-β, and the RAF/MEK/ERK signaling axis, which underlies its established antiangiogenic and antiproliferative activity in RCC and HCC.

Liposarcoma, particularly the dedifferentiated subtype, shares relevant biology: preclinical work in this pack (PMID 23416162) shows PTEN down-regulation as a malignant signature in dedifferentiated liposarcoma xenografts, and direct in-vitro data (PMID 18413802) demonstrated sorafenib inhibits growth and MAPK signaling in dedifferentiated liposarcoma cell lines (LS141, DDLS) alongside malignant peripheral nerve sheath tumor cells. Soft tissue sarcomas as a class have also shown clinical activity with sorafenib (SWOG S0505, PMID 21751200).

Because the RAF/MAPK and PDGFR pathways sorafenib targets are also implicated in several soft-tissue-sarcoma subtypes, extrapolation to liposarcoma has a plausible mechanistic basis — but the clinical evidence base is not liposarcoma-subtype-specific and remains at an early, hypothesis-generating stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY-9006) tested in advanced soft tissue sarcomas — rationale based on blocking growth-signaling enzymes and tumor blood flow; not liposarcoma-subtype-specific in design |

*Note: NCT02048371 (SARC024) was excluded — the evidence pack's own relevance grading flagged it as a data-linkage error (the trial actually studies regorafenib, not sorafenib), so it is not counted as evidence for this drug.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT (Phase 2, SWOG S0505) | Cancer | Intergroup Phase 2 trial establishing feasibility/activity of sorafenib's anti-VEGFR/RAF profile in advanced soft tissue sarcoma |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Annals of Surgical Oncology | Neoadjuvant sorafenib plus conformal radiotherapy in extremity soft-tissue sarcoma, testing synergy of antiangiogenic therapy with RT |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven soft tissue sarcoma therapy review; notes high trabectedin activity specifically in myxoid liposarcoma, framing subtype-specific drug selection |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Subtype-based soft tissue sarcoma treatment review reiterating histology-specific drug-selection principles |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse-model review proposing CDK-inhibitor combination strategies for sarcoma, contextualizing targeted-therapy combinations |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibited growth and MAPK signaling in dedifferentiated liposarcoma cell lines (LS141, DDLS) — direct preclinical liposarcoma data |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models identified PTEN down-regulation as a malignancy signature, supporting kinase/PI3K-pathway targeting rationale |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Response to **trabectedin** (a different drug) in synovial sarcoma with lung metastases — included for subtype-treatment landscape context only |

---

## Saudi Arabia Market Information

Sorafenib is currently **not marketed** in Saudi Arabia in this data set (0 licenses on file), so no authorization table is available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR1-3, PDGFR-β, RAF/MEK/ERK pathway) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is driven mostly by preclinical studies and reviews plus a single relevant completed Phase 2 trial in soft tissue sarcoma broadly (not liposarcoma-subtype-specific); one of the two logged trials is a confirmed data-linkage error and does not count as evidence.
- Two blocking/high-severity data gaps remain unresolved: SFDA package-insert warnings/contraindications (DG001, Blocking) and a formal DrugBank MOA record (DG002, High), which prevents safety pre-screening.

**To proceed, the following is needed:**
- SFDA package insert (warnings, contraindications) to clear the S1 safety gate (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Liposarcoma-subtype-specific clinical trial data (current evidence is soft-tissue-sarcoma-wide, not liposarcoma-specific)
- Correction/removal of the NCT02048371 data-linkage error from the evidence source
- Resolution of the "not_found" DDI query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

