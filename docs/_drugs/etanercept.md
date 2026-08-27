---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 6
---

# Etanercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the drug-repurposing evaluation report template (v5) supplied in this task to structure the output from the Evidence Pack.

A note on scope before the report: this Evidence Pack (`TW-DB00005-multi`) contains **6** TxGNN-predicted indications for etanercept, not one. Per the template's extraction rules, the primary title/overview must be built from `predicted_indications[0]` (rheumatoid vasculitis). I have followed that rule for the main body, but because two of the other five candidates (`inflammatory spondylopathy`, `polyarticular juvenile rheumatoid arthritis`) turn out to already be **approved indications** for etanercept rather than novel repurposing hypotheses, and because the rank‑1 candidate's own evidence argues against efficacy, I've added a closing comparison table so this isn't lost. This deviates slightly from the letter of the template but is necessary for the report not to mislead.

---

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α receptor fusion protein (p75 TNFR:Fc) whose established use is in rheumatoid arthritis and related inflammatory arthritides (JIA, psoriatic arthritis, ankylosing spondylitis).
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, an extra-articular, severe manifestation of RA, with **6 clinical trials** and **20 publications** identified.
However, the directly relevant Phase 1/2 RCT was **negative**, and a substantial body of the literature instead documents etanercept **inducing** vasculitis-like events rather than treating them — this evidence base points toward a safety signal, not a therapeutic opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Saudi Arabia licensing data (drug not marketed); literature in this pack indicates original approved use in Rheumatoid Arthritis and related inflammatory arthritides (JIA, psoriatic arthritis, ankylosing spondylitis) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for etanercept in this Evidence Pack (marked as a data gap). Based on the literature captured in this pack, etanercept is a dimeric fusion protein combining the p75 TNF receptor with the Fc portion of human IgG1; it binds circulating TNF-α and blocks its pro-inflammatory activity. This mechanism underlies its approved efficacy in rheumatoid arthritis and other TNF-α–driven inflammatory arthritides.

Rheumatoid vasculitis (RV) is recognized in the literature as one of the most severe extra-articular manifestations of rheumatoid arthritis, arising from the same underlying autoimmune/inflammatory process, and TNF-α is implicated in the vascular endothelial inflammation and immune-complex deposition seen in systemic vasculitides such as ANCA-associated vasculitis. On paper, this gives biological plausibility to the idea that a drug already effective against RA's joint disease could also help control RA's vascular complications.

However, the direct evidence in this pack argues the opposite direction. The one trial that tested etanercept specifically in a vasculitis population — NCT00001901 (the WGET trial, Phase 1/2, etanercept + standard therapy in Wegener's granulomatosis/ANCA-associated vasculitis) — found **no significant benefit** and an increased risk of solid tumors. More strikingly, at least six literature entries in this pack (PMIDs 15853915, 12209493, 11792895, 15801034, 25544845, 41327089) describe etanercept **inducing or being temporally associated with** cutaneous or systemic vasculitis, lupus-like disease, and nodulosis — a recognized class effect of anti-TNF agents ("paradoxical vasculitis"). This mechanistic ambiguity means the prediction should be treated as a signal to investigate rather than a validated therapeutic hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 1/2 | Completed | 60 | WGET trial — etanercept + standard therapy in Wegener's granulomatosis (ANCA-associated vasculitis); direct test of the hypothesis but a **key negative result**, with increased solid-tumor risk noted |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study of the risk of new immune-mediated inflammatory disease developing in patients on biologics/immunosuppressants for an existing IMID — relevant to the "induced vasculitis" safety signal |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; not vasculitis-specific |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world treatment pathways/outcomes in moderate RA patients starting etanercept vs. non-biologic therapy; not vasculitis-specific |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of treatment patterns for biologic DMARDs in RA in China; not vasculitis-specific |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional study of tocilizumab (not etanercept) in RA; provides background only |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological therapy (including TNF inhibitors) for rheumatoid vasculitis; frames current evidence base for the indication |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology, Dialysis, Transplantation | Explicitly questions whether TNFα blockade has a role in ANCA-associated vasculitis and glomerulonephritis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort (BSRBR-RA) | RMD Open | Compares risk of lupus-like and vasculitis-like events in TNF-inhibitor-treated RA patients vs. non-biologic DMARDs — a pharmacovigilance-grade safety signal |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | The Journal of Rheumatology | TNF-α blockade and the risk of (induced) vasculitis |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case series / immunology study | Scandinavian Journal of Immunology | Cutaneous vasculitis associated with both etanercept and infliximab |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case report | Arthritis and Rheumatism | Accelerated nodulosis and vasculitis following etanercept therapy for RA |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case report | Rheumatology (Oxford) | Etanercept and infliximab associated with cutaneous vasculitis |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case report | The Journal of Rheumatology | Proliferative lupus nephritis and leukocytoclastic vasculitis during etanercept treatment |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case report | Case Reports in Medicine | Large vessel vasculitis occurring in an RA patient under anti-TNF therapy |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Case report | BMC Nephrology | RA patient developing membranous nephropathy and ANCA-associated vasculitis successively |

## Saudi Arabia Market Information

Etanercept is currently **not marketed in Saudi Arabia** per this Evidence Pack (`market_status: 未上市`, 0 total licenses). No authorization records are available to summarize.

## Safety Considerations

No structured TFDA/SFDA package-insert warnings, contraindications, or DDI records are available for etanercept in this Evidence Pack (DG001, flagged as a **Blocking** data gap — package-insert PDF has not yet been retrieved/parsed; DDI query returned `not_found`).

**Literature-derived safety signal (from the evidence collected above, not from a formal label source):** Multiple independent case reports and a UK national cohort (BSRBR-RA, PMID 28123776) in this pack describe etanercept being temporally associated with **inducing** cutaneous and systemic vasculitis, lupus-like syndrome, and accelerated nodulosis in RA patients — a recognized class effect of TNF inhibitors. This is directly material to evaluating the rank-1 predicted indication and should be treated as an active safety consideration, separate from and in addition to the missing formal label data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct clinical trial testing etanercept in a vasculitis population (NCT00001901, WGET) was **negative** and showed increased solid-tumor risk, while multiple case reports and a comparative cohort study suggest etanercept may **induce** rather than treat vasculitis — a known anti-TNF class effect. The mechanistic hypothesis is biologically plausible in principle, but the weight of directly relevant evidence in this pack points against pursuing rheumatoid vasculitis as a repurposing candidate.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings, contraindications, and DDI data (DG001, Blocking — currently prevents entry into S1 safety pre-screening)
- Structured mechanism-of-action data from DrugBank (DG002)
- Detailed efficacy/safety results of the WGET trial (NCT00001901), not just the summary
- A formal pharmacovigilance assessment of the etanercept-induced-vasculitis signal before any further repurposing evaluation
- Clarification of whether the TxGNN knowledge-graph edge reflects a "treats" relationship or is picking up "co-occurs with / induces" signal from the adverse-event literature — this distinction changes the entire interpretation of the prediction

---

### Other Predicted Indications in This Evidence Pack

Because this pack (`TW-DB00005-multi`) evaluated 6 TxGNN predictions for etanercept, the table below summarizes the remaining candidates for completeness. Notably, two of the strongest-evidence candidates (rank 3, rank 5) are **not novel** — they are reconfirmations of etanercept's existing approved indications, not new repurposing opportunities.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------------|-----------------|-----------------|------------------|------|
| 1 | Rheumatoid vasculitis | 99.71% | L3 | S1 | Hold | Covered above — negative RCT, induction signal |
| 2 | Hypermobility of coccyx | 99.63% | L5 | S0 | Hold | No clinical/literature evidence; structural/mechanical condition with no plausible TNF-α mechanism — likely knowledge-graph noise |
| 3 | Inflammatory spondylopathy | 99.57% | L1 | S3 | Proceed with Guardrails | **Already an approved indication** (ankylosing spondylitis); this is a reconfirmation of existing evidence, not a new hypothesis |
| 4 | Kummell disease | 99.55% | L5 | S0 | Hold | No clinical/literature evidence; post-traumatic avascular necrosis, non-inflammatory — no plausible mechanism, likely noise |
| 5 | Polyarticular juvenile rheumatoid arthritis | 99.50% | L1 | S3 | Proceed with Guardrails | **Already an approved indication** (JIA, approved since 1999); reconfirmation, not novel |
| 6 | Vertebral disease | 99.16% | L2 | S2 | Research Question | Disease label is non-specific and largely overlaps with rank 3's evidence base; needs disambiguation before further evaluation |

**Overall implication:** none of the six TxGNN-predicted indications in this pack currently represent a validated, *novel* repurposing opportunity for etanercept — the highest-evidence hits are already-labeled uses, the top-ranked genuinely new hypothesis (rheumatoid vasculitis) is contradicted by its own key trial and safety literature, and two candidates appear to be model noise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

