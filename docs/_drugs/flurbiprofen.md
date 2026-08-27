---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From NSAID Analgesic/Anti-Inflammatory Use to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a propionic-acid–derivative NSAID; its original approved indication text is not available in the current dataset, but it is a well-established analgesic/anti-inflammatory agent. The TxGNN model's highest-ranked *evidence-backed* prediction is **Ankylosing Spondylitis**, supported by **7 head-to-head randomized controlled trials** conducted between 1974–1986 and a total of **20 PubMed publications**. Note: among the 10 TxGNN candidates in this pack, 9 (ranks 1–7, 9, 10) are flagged by the model's own rationale as likely knowledge-graph noise on rare orphan skeletal syndromes with no supporting evidence — only ankylosing spondylitis (rank 8) has real clinical and literature support, so this report focuses on that candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available records (Flurbiprofen is a propionic-acid NSAID historically used for pain and inflammatory joint disease; specific approved indication text is a data gap) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, flurbiprofen is a non-selective COX-1/COX-2 inhibitor belonging to the propionic-acid class of NSAIDs — the same pharmacological class as indomethacin, naproxen, and phenylbutazone, all of which have established roles in inflammatory spondyloarthropathies.

Ankylosing spondylitis (AS) is a chronic inflammatory spondyloarthropathy in which prostaglandin-mediated inflammation drives axial pain, stiffness, and joint damage. NSAIDs are first-line symptomatic therapy for AS per standard rheumatology practice, so a COX-inhibiting agent like flurbiprofen is mechanistically well-suited to this indication — this is not a mechanistically novel hypothesis but a class-consistent one.

Notably, the literature evidence in this pack shows flurbiprofen already has a substantial clinical trial history in AS dating back to the 1970s–80s, with head-to-head comparisons against indomethacin, phenylbutazone, and naproxen. This suggests the TxGNN prediction is recovering a genuine, previously demonstrated clinical use rather than identifying a truly novel indication — which strengthens confidence in the model's signal but also means the "new indication" framing should be understood as an evidence-supported use case, not an unprecedented hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries in ClinicalTrials.gov or ICTRP for flurbiprofen + ankylosing spondylitis in this pack; evidence is derived from historical published literature below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT | British Medical Journal | Double-blind cross-over in 35 AS patients: flurbiprofen 150mg/day well tolerated, efficacy approaching phenylbutazone 300mg/day |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT | Annals of the Rheumatic Diseases | Double-blind cross-over comparing indomethacin, flurbiprofen, and placebo in AS (placebo-controlled design) |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT | Current Medical Research and Opinion | Parallel double-blind RCT, 26 active AS patients: flurbiprofen (150-200mg/day) equally effective as indomethacin, no withdrawals for lack of efficacy |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT | Southern Medical Journal | Parallel double-blind RCT, 26 AS patients: flurbiprofen vs indomethacin equally effective for pain/tenderness relief |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT | European Journal of Clinical Pharmacology | Parallel double-blind RCT, 27 AS patients: flurbiprofen vs phenylbutazone equally effective, phenylbutazone favored on subjective improvement (not statistically significant) |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT | The New Zealand Medical Journal | 4-week double-blind crossover, 30 AS patients: flurbiprofen 200mg/day vs naproxen 750mg/day, comparable efficacy; more side effects with flurbiprofen |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT | The American Journal of Medicine | Randomized double-blind, 57 AS patients over 26 weeks: flurbiprofen 200mg/day effective vs indomethacin; some patients controlled on 100mg/day |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT | The American Journal of Medicine | Randomized double-blind 26-week study, 90 AS patients: flurbiprofen 200mg/day as effective as phenylbutazone 300mg/day |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Cohort | The American Journal of Medicine | Pooled safety analysis across 9 Phase 3 trials, 1,677 patients (AS, OA, RA): no clinically significant liver/kidney signal with flurbiprofen |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Review of flurbiprofen pharmacology and therapeutic use in RA, OA, AS; 120-300mg/day comparable to aspirin/indomethacin with fewer side effects |

---

## Saudi Arabia Market Information

Flurbiprofen currently has no marketed product license in Saudi Arabia (`market_status: 未上市`, `total_licenses: 0`) — no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Drug-specific warnings, contraindications, and interaction data are not available in this evidence pack — DG001 flags this as a Blocking data gap for safety pre-screening. As a general class consideration, propionic-acid NSAIDs such as flurbiprofen carry known risks of GI bleeding, renal impairment, and cardiovascular events that would need to be confirmed against the actual product label before clinical use.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Seven independent RCTs (1974–1986) directly support flurbiprofen's efficacy in ankylosing spondylitis with a class-consistent COX-inhibition mechanism, but the drug is not currently marketed in Saudi Arabia and lacks a local package insert, so safety pre-screening (S1) cannot be completed.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert data — warnings, contraindications, DDI (DG001, Blocking)
- Confirmed mechanism of action and formal original-indication label text (DG002, High)
- Saudi Arabia regulatory pathway assessment given current non-marketed status
- Positioning analysis against already-approved NSAIDs in AS treatment guidelines, since this is a corroborative rather than novel indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

