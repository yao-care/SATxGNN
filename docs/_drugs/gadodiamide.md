---
layout: default
title: Gadodiamide
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 2
---

# Gadodiamide
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

# Gadodiamide: From MRI Contrast Imaging to Rheumatoid Arthritis

## One-Sentence Summary

Gadodiamide is a gadolinium-based contrast agent used to enhance magnetic resonance imaging (MRI) — it is a diagnostic agent, not a therapeutic drug for any disease. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** with a **99.16%** prediction score, but this is supported by **0 clinical trials** and **10 publications**, all of which are diagnostic-imaging studies rather than therapeutic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None — Gadodiamide is a non-specific extracellular gadolinium chelate used solely as an MRI contrast agent; it has no therapeutic indication |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on known pharmacology, gadodiamide is a non-specific extracellular gadolinium chelate whose only function is T1-relaxation-based signal enhancement on MRI. It has no known pharmacological or immunomodulatory activity, and no plausible mechanistic link to rheumatoid arthritis pathology (e.g., TNF-α, IL-6, synovial angiogenesis).

All 10 supporting publications describe using gadodiamide-enhanced MRI to *image and diagnose* synovitis or bone erosion in RA or related arthritides — they are diagnostic co-occurrence studies, not evidence of therapeutic effect. This pattern is consistent with a text-mining confound artifact: the drug and disease co-occur frequently in the literature because gadodiamide is used to *scan* RA patients, not to *treat* them.

The second-ranked prediction, osteoarthritis susceptibility (score 99.11%), has zero supporting clinical trials or literature at all, further indicating these are low-confidence model outputs rather than genuine repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17935920](https://pubmed.ncbi.nlm.nih.gov/17935920/) | 2009 | Imaging/Diagnostic | European journal of radiology | Distribution of ultrasound-guided intra-articular injection in RA wrist joints |
| [18286282](https://pubmed.ncbi.nlm.nih.gov/18286282/) | 2008 | Imaging/Diagnostic | Skeletal radiology | Contrast-enhanced MRI analysis of hands/wrists in psoriatic arthritis |
| [17289759](https://pubmed.ncbi.nlm.nih.gov/17289759/) | 2008 | Imaging/Diagnostic | Annals of the rheumatic diseases | MRI and bone scintigraphy for differential diagnosis of unclassified arthritis |
| [17340197](https://pubmed.ncbi.nlm.nih.gov/17340197/) | 2007 | Imaging/Diagnostic | Annals of biomedical engineering | Kinetic modeling of contrast-enhanced MRI to assess RA wrist inflammation |
| [11454641](https://pubmed.ncbi.nlm.nih.gov/11454641/) | 2001 | Imaging/Diagnostic | Annals of the rheumatic diseases | Low-field dedicated MRI in untreated recent-onset RA |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Imaging/Diagnostic | European radiology | 1-year interval MRI features predicting bone erosions in inflammatory joint disease |
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Imaging/Diagnostic | The Journal of rheumatology | MRI features of wrist/finger joints across inflammatory joint disease groups |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Imaging/Diagnostic | European radiology | Comparison of extremity MRI (0.2T) vs high-field MRI (1.5T) in arthritic small joints |
| [11868082](https://pubmed.ncbi.nlm.nih.gov/11868082/) | 2002 | Imaging/Diagnostic | European radiology | Synovial membrane volume determination: manual vs stereologic method on MRI |
| [11274835](https://pubmed.ncbi.nlm.nih.gov/11274835/) | 2001 | Imaging/Diagnostic (normal subjects) | European journal of radiology | Normal gadolinium enhancement patterns of atlantoaxial joints on MRI |

*Note: all 10 publications are diagnostic-imaging studies using gadodiamide-enhanced MRI to visualize joint pathology; none provide evidence of therapeutic effect in rheumatoid arthritis.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA package insert warnings/contraindications are marked as a Blocking data gap — this must be resolved before any S1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic plausibility linking gadodiamide (an inert MRI contrast agent) to rheumatoid arthritis treatment, no clinical trials exist, and all supporting literature reflects diagnostic co-occurrence rather than therapeutic evidence — this prediction is most likely a text-mining confound artifact rather than a genuine repurposing candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking gap
- Drug mechanism of action (MOA) data from DrugBank
- Any preclinical or mechanistic study directly linking gadolinium chelates to immune/synovial pathways, if such evidence exists
- Independent confirmation that the TxGNN signal is not an artifact of diagnostic-imaging literature co-occurrence before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

