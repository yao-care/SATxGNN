---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 5
---

# Golimumab
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

# GOLIMUMAB: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Golimumab is a fully human anti-TNF-α monoclonal antibody approved for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis. The TxGNN model predicts it may also be effective for **Rheumatoid Vasculitis**, a severe extra-articular complication of RA, but this direction is currently supported by only **3 clinical trials (none targeting vasculitis directly)** and **6 case-level publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (derived from supplied literature evidence, e.g. PMID 20065639, 28530020 — not from an SFDA license record, as none is on file) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (flagged internally as "Research Question," decision stage S1) |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for golimumab in this evidence pack (DrugBank MOA field returned a data gap). However, the supplied literature consistently describes golimumab as a fully human anti-TNF-α IgG1κ monoclonal antibody, approved for TNF-α-driven inflammatory arthritides.

Rheumatoid vasculitis is a rare but serious extra-articular complication of long-standing, seropositive rheumatoid arthritis, thought to arise from immune-complex-mediated vascular inflammation along shared TNF-α-driven pathways. Because golimumab already treats the underlying RA disease process, there is a plausible mechanistic rationale for benefit in its vasculitic complications — anti-TNF biologics have historically been associated with attenuated incidence of rheumatoid vasculitis compared to the pre-biologic era (as referenced in PMID 29075910).

That said, the mechanistic story is not one-directional: the literature also documents paradoxical vasculitis occurring *during* anti-TNF therapy (e.g., Takayasu's arteritis onset under anti-TNF treatment, PMID 22999907), and no retrieved trial uses rheumatoid vasculitis as a primary endpoint. This mixed signal is the main reason evidence strength remains low (L4) despite a very high TxGNN similarity score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry study on risk of incident immune-mediated inflammatory diseases in patients on biologics; general safety signal, not a vasculitis treatment trial |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional study of tocilizumab (not golimumab) in RA; included for background only |

None of the retrieved trials enroll or treat rheumatoid vasculitis as a primary population/endpoint.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | RCT (network meta-analysis, 36 RCTs) | Int J Mol Sci | Golimumab and other TNF inhibitors similarly reduce radiographic joint destruction in RA vs. methotrexate |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Overview of biologic therapies, including anti-TNF agents, across autoimmune/rheumatologic disease |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Frequency and treatment of end-stage renal disease in RA patients; background comorbidity context |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatol Int | Severe sepsis (pyoderma gangrenosum, pyogenic arthritis) in an RA patient on golimumab; notes declining rheumatoid vasculitis incidence since anti-TNF introduction |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocul Immunol Inflamm | Behçet-associated uveitis successfully treated with golimumab (off-label anti-TNF use precedent) |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel vasculitis) occurring *during* anti-TNF therapy — a cautionary signal |

---

## Saudi Arabia Market Information

Golimumab currently has no marketing authorization on file for Saudi Arabia (0 licenses registered); no product/dosage-form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA warnings, contraindications, and DDI data are not yet available for this drug — this is logged as a Blocking data gap and must be resolved before any S1 safety screening can proceed.)

---

## Other Predicted Indications in This Evidence Pack

This evidence pack (candidate set TW-DB06674-multi) contains 5 TxGNN-predicted indications for golimumab. For completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Rheumatoid vasculitis | 99.73% | L4 | Hold / Research Question | Covered above — primary subject of this report |
| 2 | Hypermobility of coccyx | 99.67% | L5 | Hold | No trials or literature; structural/mechanical condition with no known TNF-α pathology link — likely embedding false positive |
| 3 | Inflammatory spondylopathy | 99.66% | L1 | Proceed with Guardrails | Strong evidence (multiple completed Phase 3 RCTs, e.g. NCT00265083, NCT03270501), but this is essentially golimumab's **existing approved indication** (ankylosing spondylitis/axSpA), not a novel repurposing signal |
| 4 | Kummell disease | 99.61% | L5 | Hold | No trials or literature; vertebral avascular necrosis is not an inflammatory/TNF-driven condition — likely embedding false positive |
| 5 | Polyarticular juvenile rheumatoid arthritis | 99.59% | L1 | Proceed with Guardrails | Strong evidence (Phase 3 RCTs incl. NCT01230827, NCT02277444), but this is also an **existing approved pediatric indication** for golimumab, not a novel signal |

Ranks 3 and 5 validate that the TxGNN model correctly recovers golimumab's known label indications with high scores, which lends indirect credibility to the model's rank-1 prediction (rheumatoid vasculitis) even though that one lacks direct trial support.

---

## Conclusion and Next Steps

**Decision: Hold** (for Rheumatoid Vasculitis)

**Rationale:**
No clinical trial or study has evaluated golimumab specifically for rheumatoid vasculitis; existing evidence is limited to case reports with a mechanistically mixed safety signal (reports of both protective association and paradoxical anti-TNF-induced vasculitis). Combined with missing MOA and safety/package-insert data, the evidence does not yet support progression past S1.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap
- DrugBank-sourced mechanism of action confirmation
- A dedicated observational or case-series study of golimumab in confirmed rheumatoid vasculitis, given no such trial currently exists
- Reconciliation of the conflicting paradoxical-vasculitis safety signal (e.g., Takayasu's arteritis case, PMID 22999907) before any clinical exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

