---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 2
---

# Trimethoprim
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

# Trimethoprim: From Antibacterial Agent to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a dihydrofolate reductase (DHFR)-inhibiting antibacterial agent; detailed mechanism-of-action documentation for this candidate is currently unavailable (data gap). The TxGNN model's top-ranked prediction is efficacy in **Punctate Epithelial Keratoconjunctivitis** (score 99.57%), but this candidate currently has **zero supporting clinical trials or publications** — it is a pure model prediction. A second, closely-scored TxGNN prediction for the same drug, **Conjunctivitis** (score 99.17%), is far better supported, with **3 clinical trials** and **9 relevant publications** (out of 20 retrieved), including a completed Phase 4 RCT of the marketed trimethoprim/polymyxin B combination for bacterial conjunctivitis — this second indication is presented separately below because it materially changes the evidence picture for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory filings (drug not currently marketed in Taiwan; no license on file). Trimethoprim is internationally established as a synthetic antibacterial (DHFR inhibitor) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: a second TxGNN prediction for this drug — Conjunctivitis — has a materially stronger evidence base (L1, "Proceed with Guardrails"). See the dedicated section below.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for trimethoprim is flagged as a data gap (DG002, High severity, source: DrugBank query pending). Based on generally known pharmacology, trimethoprim is a DHFR inhibitor that blocks bacterial folate synthesis and is used as an antibacterial agent; its established efficacy against susceptible bacteria has not been formally linked in this evidence pack to a specific original indication (Taiwan regulatory data returns no licenses).

For **Punctate Epithelial Keratoconjunctivitis** specifically, the TxGNN score is high (0.9957) but the relationship to trimethoprim's known antibacterial mechanism is only theoretical. This condition is more commonly associated with viral (e.g., adenovirus) or atypical (e.g., chlamydial) pathogens for which trimethoprim lacks clear antimicrobial activity. No clinical trials or literature currently support this specific link — it should be treated as a hypothesis-generating signal only, not a validated pharmacological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Second TxGNN Prediction: Conjunctivitis (Stronger Evidence Base)

Because this evidence pack contains a second predicted indication for trimethoprim with substantially more support, it is presented here in full for decision-making completeness.

| Item | Content |
|------|------|
| Predicted New Indication | Conjunctivitis (disease) |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L1 |
| Recommended Decision | Proceed with Guardrails |

**Mechanistic rationale:** Trimethoprim is a DHFR inhibitor with direct antibacterial activity against common conjunctivitis pathogens (*Haemophilus influenzae*, *Staphylococcus* spp., *Streptococcus* spp.). Clinically, the polymyxin B/trimethoprim combination (Polytrim) is already an approved topical treatment for bacterial conjunctivitis — this is a well-established use, not merely a model hypothesis.

### Clinical Trials

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Single-blind RCT directly comparing Polytrim (polymyxin B/trimethoprim) ophthalmic solution vs. moxifloxacin ophthalmic solution for pediatric conjunctivitis ("pink eye"); the most directly relevant efficacy evidence |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Phase 3 | Completed | 218 | Community-based double-blind placebo-controlled RCT of prophylactic antibiotics in measles infection (Guinea-Bissau); evaluates broader complication prevention, only indirectly related to conjunctivitis treatment |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Phase 4 | Completed | 252 | Antibiotic resistance and microbiome surveillance in children (Burkina Faso); background resistance data, not a conjunctivitis efficacy trial |

### Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT (Multicenter) | J Pediatr Ophthalmol Strabismus | Compared speed of clinical efficacy of polymyxin B/trimethoprim vs. 0.5% moxifloxacin for bacterial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical Trial | Am J Ophthalmol | Clinical evaluation of trimethoprim-containing ophthalmic solutions (with sulfacetamide or polymyxin B) for bacterial conjunctivitis/blepharitis |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic Review/Meta-analysis | J Pediatric Infect Dis Soc | Systematic review of antibiotic treatments, including trimethoprim, for neonatal chlamydial conjunctivitis |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Case Series/Survey | Clin Therapeutics | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution |
| [21988450](https://pubmed.ncbi.nlm.nih.gov/21988450/) | 2011 | Cohort/Epidemiology | Curr Eye Res | Analysis of nontypeable *S. pneumoniae* in sporadic bacterial conjunctivitis cases across prospective multicenter clinical studies |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Cohort | Antibiotics (Basel) | Clinical and molecular characteristics of MSSA ocular infection in Taiwan — local epidemiological relevance |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Guidance on controlling contagious bacterial conjunctivitis with antimicrobial agents |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Review of etiology and management of acute infectious conjunctivitis in children |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Case Report | Ophthalmic Plast Reconstr Surg | Chronic conjunctivitis due to *Nocardia nova*, isolate sensitive to trimethoprim/sulfamethoxazole |

---

## Taiwan Market Information

Trimethoprim currently holds no drug license in Taiwan (market status: Not Marketed; 0 authorizations on file). No product/dosage-form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package insert warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before a formal safety review (Stage S1) can be conducted for either predicted indication.

---

## Conclusion and Next Steps

**Decision: Hold** (for the primary prediction, Punctate Epithelial Keratoconjunctivitis)

**Rationale:**
This is a pure TxGNN model prediction (L5) with no supporting clinical trials or literature, and only a theoretical mechanistic link to trimethoprim's antibacterial activity. It does not meet the bar for further investment at this time.

**For the secondary prediction (Conjunctivitis), an interim decision of "Proceed with Guardrails" is supportable** given one directly relevant completed Phase 4 RCT and multiple supporting publications — but this cannot advance past initial safety screening until the blocking TFDA data gap (DG001) is resolved.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — blocking gap, required for S1 safety review (DG001)
- DrugBank-sourced mechanism-of-action confirmation (DG002)
- If pursuing Punctate Epithelial Keratoconjunctivitis: targeted literature/trial search to establish any real-world basis before further evaluation
- If pursuing Conjunctivitis: confirm whether existing trimethoprim/polymyxin B ophthalmic products (e.g., Polytrim) are relevant comparators for a Taiwan market entry strategy, since local licenses are currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

