---
layout: default
title: Tenoxicam
parent: 僅模型預測 (L5)
nav_order: 608
evidence_level: L5
indication_count: 10
---

# Tenoxicam
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

# Tenoxicam: From Musculoskeletal & Rheumatic Pain to Rheumatoid Arthritis

## One-Sentence Summary

> Tenoxicam is an oxicam-class NSAID historically used worldwide for osteoarthritis, ankylosing spondylitis, and other rheumatic and musculoskeletal pain conditions, but it currently holds **no marketing authorization in Saudi Arabia**.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, a use already well-documented in the international literature,
> with **1 clinical trial** and **20 publications** (10 most relevant summarized below) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Saudi Arabia (0 approved licenses); internationally documented as an oxicam-class NSAID for osteoarthritis, ankylosing spondylitis, and rheumatic/musculoskeletal pain |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source drug record. Based on known pharmacological class information, tenoxicam is an oxicam-class NSAID (structurally and pharmacologically related to piroxicam) that non-selectively inhibits cyclooxygenase (COX-1/COX-2), reducing prostaglandin synthesis and thereby producing analgesic, anti-inflammatory, and antipyretic effects. This is the standard pharmacological basis for symptomatic treatment of rheumatoid arthritis (RA).

Notably, this is not a novel mechanistic leap: multiple historical studies in the evidence pack (1985–1996) already directly compared tenoxicam against piroxicam, aceclofenac, and naproxen specifically in RA populations, showing comparable efficacy and tolerability. The "unmarketed" status in Saudi Arabia therefore reflects a **market-entry gap rather than an efficacy gap** — tenoxicam has been an accepted RA therapy in multiple jurisdictions for decades.

Mechanistically, RA is a chronic inflammatory joint disease driven substantially by COX-mediated prostaglandin production, which is precisely the pathway tenoxicam targets. This makes the TxGNN prediction consistent with, rather than divergent from, tenoxicam's established pharmacology — the model has effectively re-identified a well-known indication that has simply not yet been formalized for this market.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | NA | Completed | 80 | Compared tenoxicam, paracetamol, and tenoxicam-paracetamol combination for postoperative pain in double-jaw surgery; supports tenoxicam's analgesic/anti-inflammatory profile, though not RA-specific (relevance grade B — general/postoperative pain population, not confirmed RA cohort) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | The Journal of Rheumatology | Tenoxicam 20mg OD vs piroxicam 20mg OD in 102 RA patients — no difference in efficacy; similar adverse event rates |
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clinical Rheumatology | Aceclofenac vs tenoxicam in 292 RA patients over 3 months — both groups improved, comparable efficacy and safety |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | RCT (multicentre) | The Journal of International Medical Research | General-practice study of tenoxicam 20mg/day in 2,963 OA/RA patients over 12 weeks — symptom reduction, most continued long-term |
| [2512637](https://pubmed.ncbi.nlm.nih.gov/2512637/) | 1989 | RCT (double-blind) | Scandinavian Journal of Rheumatology Supplement | 4-year long-term trial of tenoxicam plus basis therapy (gold/D-penicillamine) in 20 RA patients — sustained analgesic/anti-inflammatory improvement |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | RCT (double-blind) | The British Journal of Clinical Practice | Large multicentre parallel-group study of tenoxicam vs piroxicam in 1,328 OA/RA patients — tenoxicam showed slightly greater effect on global assessment |
| [2595345](https://pubmed.ncbi.nlm.nih.gov/2595345/) | 1989 | RCT (double-blind pilot) | Scandinavian Journal of Rheumatology Supplement | Randomized pilot comparing tenoxicam and piroxicam on grip strength in 10 RA patients — no significant difference between treatments |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | RCT (double-blind, parallel) | European Journal of Rheumatology and Inflammation | Double-blind parallel trials of tenoxicam vs piroxicam in osteoarthrosis, RA, and ankylosing spondylitis — tenoxicam at least as effective and well tolerated |
| [3315620](https://pubmed.ncbi.nlm.nih.gov/3315620/) | 1987 | Review | Drugs | Preliminary review of tenoxicam's pharmacodynamics, pharmacokinetics, and efficacy across RA, OA, ankylosing spondylitis, and gout |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Updated review of tenoxicam pharmacology and therapeutic efficacy in rheumatic diseases — efficacy at least equivalent to other NSAIDs, tolerability at least comparable to piroxicam |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Review | Clinical Pharmacokinetics | Review of tenoxicam clinical pharmacokinetics — near-complete oral absorption, ~99% protein binding, long half-life supporting once-daily dosing |

---

## Saudi Arabia Market Information

Currently no marketing authorization records exist for tenoxicam in Saudi Arabia (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug interaction data are currently available in the source records; the TFDA/SFDA package insert has not yet been obtained.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs and reviews spanning 1985–1996 consistently support tenoxicam's efficacy and tolerability in RA, comparable to established NSAIDs such as piroxicam, aceclofenac, and naproxen — this is a mechanistically sound and historically validated use, not a speculative one. However, tenoxicam currently has zero marketing authorizations in Saudi Arabia and lacks local safety documentation, so market entry requires standard regulatory and safety diligence rather than new efficacy studies.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently blocking, required before safety pre-assessment (S1) can proceed
- Confirmed mechanism of action documentation from DrugBank
- Saudi Arabia regulatory filing / registration pathway assessment (currently 0 licenses)
- Formal drug-drug interaction (DDI) database confirmation (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

