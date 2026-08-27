---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 611
evidence_level: L5
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Teriflunomide: From No Registered Indication to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide is not currently marketed in Saudi Arabia and has no approved indication on file in this dataset. The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)**, with **28 clinical trials** and **19 publications** currently supporting this direction — including several head-to-head Phase 3 trials against other disease-modifying therapies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (drug not marketed; no license data available) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record for teriflunomide (DrugBank DB08880). However, the retrieved literature consistently describes it as a selective and reversible inhibitor of the mitochondrial enzyme dihydro-orotate dehydrogenase (DHODH), which blocks de novo pyrimidine synthesis and reduces the proliferation of activated T and B lymphocytes (Scott LJ, *Drugs*, 2019, PMID 31098896).

No original indication is registered for this drug in the current dataset, so a direct mechanistic bridge between "original" and "new" indication cannot be drawn from the evidence pack. That said, the volume and maturity of the RRMS-specific evidence base (28 registered trials, multiple completed Phase 3 RCTs, 19 publications including three NEJM head-to-head comparator trials) indicate this is not a speculative model-only extrapolation but a well-characterized, clinically validated use of the compound in this disease area.

Mechanistically, the anti-proliferative effect on activated lymphocytes is directly relevant to RRMS, an autoimmune-mediated demyelinating disease driven by T- and B-cell activation — which is consistent with why this pathway has been extensively studied as a disease-modifying strategy in this population.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | Pivotal RCT evaluating teriflunomide's effect on relapse frequency and disability accumulation (EDSS) in relapsing MS |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Rater-blinded comparison of teriflunomide vs. interferon beta-1a on time to treatment failure, relapse rate, and fatigue |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension documenting safety/tolerability of teriflunomide 7 mg and 14 mg over time |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension of a Phase 2 study assessing long-term safety and efficacy |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Investigator-initiated real-world effectiveness study in a routine MS clinic setting (≥2 years follow-up) |
| [NCT03768648](https://clinicaltrials.gov/study/NCT03768648) | N/A | Completed | 75 | Real-life assessment of cognition and non-conventional MRI markers in patients treated with Aubagio |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Completed | 50 | 12-month observational study of Aubagio's effect on gray matter pathology via MRI |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Measured teriflunomide concentrations in serum and cerebrospinal fluid at the 14 mg daily dose |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic Phase 4 study on regulatory B lymphocytes as mediators of teriflunomide's therapeutic effect |
| [NCT02833714](https://clinicaltrials.gov/study/NCT02833714) | N/A | Terminated | 26 | Characterized teriflunomide's effect on B-cell activation markers and cytokine secretion |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | New England Journal of Medicine | ASCLEPIOS trials: ofatumumab vs. teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | New England Journal of Medicine | Tolebrutinib (BTK inhibitor) vs. teriflunomide in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | New England Journal of Medicine | Ublituximab (anti-CD20) vs. teriflunomide in relapsing MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | The Lancet Neurology | evolutionRMS1/2: evobrutinib (BTK inhibitor) vs. teriflunomide, two Phase 3 trials |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM trial: ponesimod vs. teriflunomide, first head-to-head oral DMT Phase 3 comparison |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT (subgroup) | Multiple Sclerosis Journal | ASCLEPIOS I/II: outcomes in treatment-naive patients, ofatumumab vs. teriflunomide |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systematic Review / Network Meta-analysis | Cochrane Database of Systematic Reviews | Comparative efficacy of immunomodulators/immunosuppressants in RRMS |
| [37528262](https://pubmed.ncbi.nlm.nih.gov/37528262/) | 2023 | Meta-analysis | Neurotherapeutics | Post-marketing comparison of dimethyl fumarate vs. teriflunomide |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Comprehensive review of teriflunomide's mechanism, efficacy, and tolerability in RRMS |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | General review of MS diagnosis and treatment, including oral DMTs |

## Saudi Arabia Market Information

Teriflunomide currently has no product authorization on record in Saudi Arabia (0 licenses; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical evidence for teriflunomide in RRMS is exceptionally strong (L1: multiple completed Phase 3 RCTs, including several head-to-head comparator trials in major journals), but this evaluation cannot proceed to safety assessment because the TFDA package insert warnings/contraindications (DG001) are marked as a **Blocking** data gap, and no DDI or Saudi Arabia licensing data exist for this compound.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently blocking
- Mechanism of action confirmation from DrugBank (DG002)
- Drug-drug interaction data (current query returned no results)
- Local market entry/registration pathway assessment, since the drug is not currently marketed in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

