---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Adult Rheumatic/Musculoskeletal Disorders to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a classic oxicam-class NSAID used for inflammatory and musculoskeletal pain conditions in adults. Among the TxGNN model's top-ranked candidates for this drug, **Juvenile Idiopathic Arthritis (JIA)** is the only prediction supported by real-world clinical evidence — including two historical randomized controlled trials of piroxicam itself in juvenile arthritis and two modern network meta-analyses of NSAIDs in JIA (13 publications total). The model's top 8 raw-score predictions (rare skeletal dysplasia syndromes, WHIM syndrome, etc.) were reviewed and assessed as likely embedding artifacts with no pharmacological plausibility, so they are not carried forward as the featured candidate — see the note below.

> **Note on TxGNN ranking:** This evidence pack contains 10 TxGNN predictions. Ranks 1–8 (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, acromesomelic dysplasia, brachyolmia variants, pseudoachondroplasia, myosclerosis, WHIM syndrome) each score higher than JIA but have **zero clinical trials and zero literature hits**, and the pack's own mechanistic rationale for each explicitly labels them as probable model false positives (disease-node clustering by skeletal/genetic pathway, unrelated to COX inhibition). Rank 9 (rheumatoid nodulosis) has one weak, indirect case report about methotrexate rather than piroxicam. Rank 10, **Juvenile Idiopathic Arthritis**, is the only candidate with an actual evidence base and is used as the featured indication for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory data (Saudi Arabia: not marketed, no license text on file); piroxicam is pharmacologically an NSAID used for adult rheumatic/musculoskeletal inflammatory pain |
| Predicted New Indication | Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data (DrugBank MOA field) was not available for this drug. However, the evidence pack's own repurposing rationale for the JIA candidate describes the mechanism directly: piroxicam is an oxicam-class, non-selective COX-1/COX-2 inhibitor that suppresses prostaglandin synthesis, producing anti-inflammatory, analgesic, and antipyretic effects — the standard pharmacological basis for NSAID use in inflammatory arthritis.

Juvenile Idiopathic Arthritis is mechanistically continuous with adult inflammatory arthritis (rheumatoid arthritis, osteoarthritis), where NSAIDs are a well-established first-line symptomatic therapy. Other oxicam/propionic-acid class NSAIDs referenced in the same literature set (naproxen, oxaprozin, nabumetone, pirprofen) are already used across this disease spectrum, supporting the plausibility of piroxicam's applicability to JIA specifically.

Critically, this is not a purely computational prediction: piroxicam itself was directly studied in children with juvenile (chronic) rheumatoid arthritis in two head-to-head RCTs against naproxen in the 1980s, and two recent (2021, 2024) systematic reviews/network meta-analyses re-evaluate NSAID comparative efficacy and safety in JIA. This combination of historical direct trial evidence and current systematic-review context is what distinguishes this candidate from the model's other high-score-but-unsupported predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov / ICTRP both returned 0 results for this drug-disease pair).

*(Note: two relevant randomized trials exist but are only indexed as PubMed literature, not as registered trial records — see Literature Evidence below.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | RCT | European Journal of Rheumatology and Inflammation | 26 children with juvenile rheumatoid arthritis randomized to piroxicam vs naproxen; painful/swollen joint counts decreased significantly with piroxicam |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | Multicentre 8-week double-blind crossover trial in 47 children with juvenile chronic arthritis comparing piroxicam vs naproxen; no significant difference between treatments |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Review | World Journal of Clinical Cases | Systematic review and network meta-analysis of NSAIDs (including piroxicam-class agents) for JIA, comparing relative efficacy |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Review | Indian Pediatrics | Systematic review and network meta-analysis comparing efficacy and safety of nine NSAIDs in JIA patients |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | PK Study | European Journal of Clinical Pharmacology | Steady-state pharmacokinetics of piroxicam in 10 children with rheumatic disease; Cmax and half-life characterized for pediatric dosing |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review | Clinical Rheumatology | Long-term toxicity study of antirheumatic/anti-inflammatory drugs (including NSAIDs) in a pediatric rheumatology cohort |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort | International Ophthalmology | Frequency/complications of chronic iridocyclitis in ANA-positive pauciarticular JCA, an extra-articular manifestation relevant to disease management |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | Review of nabumetone (related NSAID) therapeutic use and safety in osteoarthritis and rheumatoid arthritis |
| [1617910](https://pubmed.ncbi.nlm.nih.gov/1617910/) | 1992 | Review | Clinical Pharmacy | Review of oxaprozin (related NSAID), pharmacology and clinical efficacy in inflammatory joint disease |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Critical Reviews in Therapeutic Drug Carrier Systems | Review of microencapsulated NSAID drug-delivery systems for arthritis, including juvenile idiopathic arthritis |

---

## Saudi Arabia Market Information

Piroxicam is not currently marketed in Saudi Arabia — 0 product authorizations on file.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data were available in this evidence pack — TFDA package insert and DDI queries returned no usable data.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct piroxicam RCTs in juvenile (chronic) rheumatoid arthritis plus two recent NSAID-class systematic reviews/network meta-analyses in JIA give this candidate an L1 evidence level with a plausible, well-established mechanism (COX-1/2 inhibition). However, the drug is not currently marketed in Saudi Arabia and formal safety/labeling data are absent, so guardrails are needed before advancing.

**To proceed, the following is needed:**
- Saudi Arabia (SFDA) regulatory pathway assessment for a pediatric JIA indication, since piroxicam has no current market authorization
- Package insert / TFDA warnings, contraindications, and pediatric dosing safety data (currently a Blocking data gap)
- Formal drug-drug interaction profile
- Review of modern pediatric NSAID safety guidance given the age of the primary piroxicam RCTs (1986–1987) and known long-term GI/renal risk profile of piroxicam relative to newer NSAIDs in the same literature set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

