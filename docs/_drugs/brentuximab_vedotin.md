---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma / Systemic ALCL to Follicular Lymphoma

## One-Sentence Summary

Brentuximab Vedotin (BV, Adcetris®) is an anti-CD30 antibody-drug conjugate approved globally for Classical Hodgkin Lymphoma and Systemic Anaplastic Large Cell Lymphoma, though not yet registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **6 clinical trials** and **20 publications** currently supporting this direction.
Evidence sits at the L3 level — driven by exploratory Phase 2 data and a biomarker-selected (CD30+) patient rationale, with a concerning pattern of trial withdrawals and terminations that warrants careful interpretation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Classical Hodgkin Lymphoma / Systemic Anaplastic Large Cell Lymphoma (global approvals; not registered in Saudi Arabia) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not returned from the database query. Based on known pharmacology, Brentuximab Vedotin is an antibody-drug conjugate in which the anti-CD30 monoclonal antibody brentuximab is covalently linked to monomethyl auristatin E (MMAE), a potent microtubule-disrupting agent. When BV binds to a CD30-expressing cancer cell, the conjugate is internalized, MMAE is released intracellularly, and the resulting microtubule disruption leads to G2/M cell-cycle arrest and apoptosis. This mechanism is well-characterized in CD30-high malignancies — Classical Hodgkin Lymphoma and sALCL — where BV is an established standard of care.

Follicular lymphoma (FL) is a B-cell indolent lymphoma in which CD30 expression is typically low or absent on standard disease cells. However, a clinically meaningful subset undergoes histological transformation — most notably transformation to CD30+ Anaplastic Large Cell Lymphoma — where the mechanistic rationale for BV becomes direct and compelling. A published case report (PMID 32476657) documents complete response to BV in a patient with Grade I FL that transformed to CD30+ ALK1-negative ALCL, providing proof-of-concept at the patient level. Even outside of overt transformation, some FL tumors express CD30 on a proportion of cells, and CD30 IHC can prospectively identify candidates.

The TxGNN prediction is biologically plausible within the context of a biomarker-selected population. The key constraint is that CD30-positive FL represents a small fraction of all FL patients, making mandatory pre-treatment CD30 IHC screening (typically ≥10% positive threshold) a prerequisite for any treatment application. The currently recruiting trial NCT04587687 — specifically designed for BV + Bendamustine in relapsed/refractory FL — provides the most direct signal of clinical feasibility, though results are not yet mature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + Bendamustine directly targeting R/R FL; the most relevant ongoing trial, providing a direct feasibility signal for this indication |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Rituximab + Bendamustine ± BV for R/R CD30+ DLBCL; early termination may reflect enrollment difficulty in CD30+ B-cell NHL or insufficient efficacy signal |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + Rituximab as frontline for CD30+/EBV+ lymphomas including FL subset; small terminated trial providing safety data for FL subgroup |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | RBv induction followed by RBvB for newly diagnosed post-transplant lymphoproliferative disorders with CD20/CD30 expression; withdrawn before enrollment |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + Pembrolizumab for recurrent systemic PTCL; withdrawn before enrollment — conceptually interesting combination, no execution data |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + Bendamustine + Rituximab for R/R CD30+ B-cell NHL; withdrawn before enrollment — multiple FL-adjacent trial withdrawals represent a warning signal |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Clinical Study | Blood Advances | LYSA Phase 2: BV + gemcitabine (GBV) followed by BV maintenance in R/R PTCL with ≥5% CD30+; establishes BV combination activity even in CD30-low settings |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Prospective/Observational | Advances in Therapy | Real-world BV + CEP as frontline for CD30+ NHL (PTCL subtypes); high ORR in CD30+ settings supports BV's breadth across lymphoma types |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Cohort | European Journal of Haematology | BV + ICE in R/R PTCL; demonstrates BV salvage combination feasibility and safety |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Current and upcoming treatments for common PTCL subtypes; BV + CHP established as frontline for CD30+ PTCL, informing CD30-targeting strategy |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy landscape in indolent NHL including FL; contextualizes the role of targeted agents in FL treatment evolution |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology (ASH Education Program) | BV integration and novel agents in PTCL management; reviews BV's expanding scope |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | Review | Hematological Oncology | PTCL treatment landscape: what's next; discusses BV's frontline role and emerging combinations |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplantation | Post-ASCT maintenance strategies in lymphoma including FL; BV's consolidation role in high-risk lymphomas |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Case Report | Skin Appendage Disorders | Extensive alopecia mucinosa (folliculotropic mycosis fungoides, CTCL) achieving response to BV; demonstrates BV activity in follicular-pattern T-cell disease |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf Journal of Oncology | **Grade I FL transformation to CD30+ ALK1-negative ALCL achieving complete response to BV + high-dose methotrexate** — the most directly relevant case demonstrating BV's mechanistic proof-of-concept in transformed FL |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC); anti-CD30 antibody conjugated to MMAE (microtubule inhibitor/auristatin class) |
| Myelosuppression Risk | Moderate to High — MMAE payload causes neutropenia and thrombocytopenia; neutropenia is the most common Grade ≥3 adverse event reported in BV clinical trials |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (prior to each cycle), peripheral neuropathy assessment (cumulative MMAE neurotoxicity is dose-limiting), liver function tests, renal function, infusion reaction monitoring |
| Handling Protection | Must follow cytotoxic drug handling regulations; ADC biohazard precautions required for preparation and administration of MMAE-containing conjugate |

---

## Safety Considerations

Please refer to the package insert for safety information. Specific warnings and contraindications data were not available in the current evidence pack; drug interaction data returned no results in this dataset.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
BV has a clear mechanistic basis in CD30+ follicular lymphoma — particularly in the transformation-to-ALCL subpopulation — and there is an active dedicated trial (NCT04587687), but 4 of 6 FL-adjacent trials were terminated or withdrawn before meaningful enrollment, overall evidence remains at L3, and the eligible CD30+ FL population is inherently small and requires prospective biomarker selection.

**To proceed, the following is needed:**
- Mandatory CD30 IHC screening (≥10% tumor cell positivity threshold) to identify the eligible FL patient subset before any treatment decision
- Mature efficacy and safety results from NCT04587687 (BV + Bendamustine in R/R FL; currently recruiting, target n=23)
- Investigation into the cause of the high trial withdrawal/termination rate across FL-directed BV studies (4/6 non-completing) — understanding whether this reflects enrollment difficulty, interim efficacy signals, or regulatory issues
- Saudi Arabia regulatory pathway assessment for BV importation, named-patient compassionate use, or local trial sponsorship
- Comprehensive safety monitoring plan addressing peripheral neuropathy, myelosuppression, infusion reactions, and cumulative MMAE toxicity in the FL patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

