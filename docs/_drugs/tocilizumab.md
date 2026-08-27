---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody originally developed for rheumatoid arthritis (RA) and related autoimmune conditions. The TxGNN model ranks **Ankylosing Spondylitis** as its top predicted new indication with a **99.99%** score, and **9 clinical trials** and **19 publications** are available — but the two pivotal Phase 3 RCTs among them were both terminated for lack of efficacy, directly contradicting the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (inferred from evidence-pack rationale; no official Saudi label text available — see note below) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty (drug not marketed in Saudi Arabia), so the original indication cannot be sourced from an approved label. It is inferred from repeated statements in the evidence pack's own repurposing rationale (e.g., "IL-6 is a key pathogenic factor in RA") and from literature abstracts describing tocilizumab's approved use.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this drug (Data Gap DG002, High severity). Based on information embedded in the evidence pack itself, tocilizumab is a humanized monoclonal antibody that blocks the IL-6 receptor (IL-6R), and its efficacy in RA — a disease driven substantially by IL-6-mediated synovial inflammation — is well established across the accompanying literature.

The mechanistic rationale for extrapolating to ankylosing spondylitis (AS) is that IL-6 is a pro-inflammatory cytokine implicated broadly in rheumatic disease pathology, and AS shares clinical and immunological overlap with RA as a chronic inflammatory arthritis. TxGNN's knowledge-graph proximity between IL-6R blockade and AS reflects this superficially plausible link.

However, this mechanistic extrapolation has already been **directly tested and refuted in humans**. Two Phase 3 randomized, double-blind, placebo-controlled trials (BUILDER-1, NCT01209689; BUILDER-2, NCT01209702) were both terminated early because tocilizumab failed to separate from placebo on ASAS20/40 response. The dominant literature consensus (e.g., PMID 22452603, "Antagonizing IL-6 in ankylosing spondylitis") attributes this to axial spondyloarthritis being driven predominantly by the TNF-α/IL-17 axis rather than IL-6, unlike RA. This is a case where the TxGNN score is very high, but confirmatory human trial evidence points the opposite direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | BUILDER-1: RCT in TNF-inadequate-responder AS patients; terminated early at interim analysis for lack of efficacy (ASAS20/40 not met) — direct negative evidence. |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | BUILDER-2: seamless Ph2/3 RCT in TNF-naïve AS patients; terminated for insufficient efficacy, consistent with BUILDER-1 — confirms IL-6 blockade does not work in AS. |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Bayesian RCT of secukinumab (not tocilizumab) in Takayasu arteritis; related large-vessel vasculitis population, not directly informative for AS. |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2500 | Observational biomarker/cytokine-profiling study across systemic inflammatory diseases; not treatment-specific. |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10000 | Korean nationwide biologics/tsDMARD registry covering RA, AS and PsA; real-world safety observation, no hypothesis testing. |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA patients; translational immunology, not an AS efficacy trial. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; not AS-specific efficacy data. |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1431 | Real-world observational study of Inflectra (infliximab, not tocilizumab); low relevance. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750000 | Population-level study of incident immune-mediated inflammatory disease risk under biologics/immunosuppressants; class-level, not tocilizumab-specific. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT results | Ann Rheum Dis | Primary publication of BUILDER-1/BUILDER-2 results — tocilizumab failed to demonstrate short-term symptomatic efficacy in AS. |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-Analysis | Medicine | Comparative effectiveness review of biologic regimens for AS across RCTs through 2015. |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clinical Rheumatology | Serious infection risk with biologics in axial spondyloarthritis/nr-axSpA — safety-focused synthesis. |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Short review specifically on IL-6 antagonism in AS, discussing the mechanistic rationale and its limitations. |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Biologic agents for AS beyond TNFα antagonists, including IL-6 pathway blockers. |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clin Exp Rheumatol | Comparative review of biologics in RA vs. AS, noting differing efficacy/pathogenesis between the two diseases. |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | Review | Curr Pharm Biotechnol | Overview of biologics across RA, PsA, and spondyloarthritis including AS. |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Review | Open Access Rheumatol | Comprehensive review of biologics in RA, AS, and PsA including anti-cytokine agents. |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Treatment options for TNF-inhibitor-refractory AS, surveying alternative drug classes. |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case report | Frontiers in Medicine | Two cases of AA amyloidosis secondary to AS successfully treated with tocilizumab — a positive signal, but limited to a rare AS complication (amyloidosis), not axial disease activity itself. |

---

## Saudi Arabia Market Information

Tocilizumab is currently **not marketed** in Saudi Arabia — the evidence pack lists 0 authorizations (`taiwan_regulatory.total_licenses = 0`, `market_status = 未上市`), so no product/dosage-form table can be produced.

---

## Safety Considerations

No safety warning, contraindication, or drug interaction data are currently available for this candidate. This is flagged in the evidence pack as **Data Gap DG001 (Blocking severity)** — its absence means this candidate cannot proceed to the S1 safety evaluation stage until TFDA/SFDA package insert data is obtained and parsed.

Please refer to the official package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the evidence volume nominally meets the L1 threshold (2 Phase 3 RCTs), both trials (BUILDER-1 and BUILDER-2) were **terminated for lack of efficacy**, providing direct clinical evidence against — not for — this indication, despite the very high TxGNN score. Combined with the drug's non-marketed status in Saudi Arabia and a Blocking-severity safety data gap (DG001), this candidate does not support a Go decision.

**To proceed, the following is needed:**
- Confirm this candidate should be deprioritized given the negative RCT outcomes, rather than pursued further as an AS indication
- Obtain TFDA/SFDA package insert data (warnings, contraindications, DDI) to close Data Gap DG001
- Obtain confirmed mechanism-of-action documentation to close Data Gap DG002
- If continuing repurposing work on this drug, consider re-scoping toward **rheumatoid factor-positive polyarticular JIA** (rank 10 in this evidence pack), which shows a more evidence-consistent profile — L2 evidence level with a "Proceed with Guardrails" recommendation, supported by a pivotal completed Phase 3 trial (NCT00988221) in the closely related pJIA population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

