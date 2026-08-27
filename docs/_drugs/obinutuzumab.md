---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the Evidence Pack, this drug candidate has **three** predicted indications (candidate_id ends in `-multi`), with very different evidence maturity — Follicular Lymphoma has 50 trials + 20 publications (L1), while the two CLL/SLL molecular subtypes have zero trials/literature (L5). I've structured the report around the strongest, decision-relevant prediction (Follicular Lymphoma) and added a transparent supplementary section for the two low-evidence subtype hypotheses rather than silently dropping them.

---

# Obinutuzumab: TxGNN-Predicted Expansion to Follicular Lymphoma (with CLL/SLL Molecular Subtypes as Exploratory Hypotheses)

## One-Sentence Summary

Obinutuzumab (DrugBank DB08935) is a glycoengineered, humanized type II anti-CD20 monoclonal antibody; its original approved indication is not recorded in this dataset (data gap). The TxGNN model's best-supported prediction is **Follicular Lymphoma**, backed by **50 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs. The model additionally flags two molecularly-defined **CLL/SLL** subtypes with an equally high prediction score, but currently **no clinical trials or literature** were found under those precise subtype labels.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset — no `taiwan_regulatory.licenses` records and `original_indications` is empty (drug not yet marketed in Saudi Arabia) |
| Predicted New Indication | Follicular Lymphoma *(primary; see also two exploratory CLL/SLL subtype predictions below)* |
| TxGNN Prediction Score | 99.18% (Follicular Lymphoma, model rank 11593) |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-level mechanism-of-action data was not returned for this drug in the current dataset (`original_moa: [Data Gap]`). However, the collected trial and literature evidence itself describes the mechanism: obinutuzumab is a third-generation, fully humanized, glyco-engineered **type II anti-CD20 monoclonal antibody (IgG1)**. Compared with first-generation anti-CD20 agents (e.g., rituximab), its glycoengineering enhances antibody-dependent cellular cytotoxicity (ADCC) and phagocytosis (ADCP), and it induces greater direct (non-apoptotic) B-cell killing.

Follicular lymphoma tumor cells, like other mature B-cell malignancies, uniformly express the CD20 surface antigen — the same target obinutuzumab was engineered against. This is not a distant mechanistic leap: obinutuzumab already has a well-established clinical development pathway in CD20+ B-cell malignancies (both CLL/SLL and follicular lymphoma appear repeatedly across the trial evidence as related, CD20-driven disease entities), which is consistent with the TxGNN model correctly recovering a mechanistically coherent target-disease relationship rather than a speculative one.

The strength of this specific prediction is corroborated by the large, high-quality evidence base returned: the pivotal Phase 3 **GALLIUM** trial (PMID 29856692, 37404773) demonstrated that obinutuzumab-based immunochemotherapy significantly improved progression-free survival versus rituximab-based regimens in previously untreated follicular lymphoma, and the Phase 2 **GALEN** (PMID 31296423) and Phase 2 **ROSEWOOD** (PMID 37506346) studies further support activity in relapsed/refractory disease. This depth of independent replication across trial phases and settings is what elevates this prediction from a theoretical hypothesis to an actionable, evidence-backed indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Active, not recruiting | 33 | Obinutuzumab + CC-99282 in previously untreated, high tumor-burden FL |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A (real-world) | Recruiting | 332 | Real-world efficacy/safety of obinutuzumab-based therapy in untreated FL |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Completed | 96 | Obinutuzumab + lenalidomide in previously untreated FL |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1/2 | Completed | 317 | Obinutuzumab + lenalidomide across untreated and R/R FL cohorts (precursor to GALEN) |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Active, not recruiting | 40 | Chemo-free obinutuzumab + ibrutinib + venetoclax in untreated FL |
| [NCT01691898](https://clinicaltrials.gov/study/NCT01691898) | Phase 1/2 | Completed | 231 | Polatuzumab vedotin + obinutuzumab in relapsed/refractory FL and DLBCL |
| [NCT06806033](https://clinicaltrials.gov/study/NCT06806033) | Phase 2 | Recruiting | 100 | CRS-profile optimization for glofitamab + GemOx in relapsed/refractory aggressive B-NHL |
| [NCT05169658](https://clinicaltrials.gov/study/NCT05169658) | Phase 2 | Completed | 42 | Subcutaneous mosunetuzumab ± polatuzumab vedotin and obinutuzumab in untreated indolent B-NHL |
| [NCT06918015](https://clinicaltrials.gov/study/NCT06918015) | Phase 2 | Not yet recruiting | 58 | Zanubrutinib + GCVP (obinutuzumab-based regimen) in untreated FL |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1,095 | Epcoritamab + R2 vs. chemoimmunotherapy in untreated FL (large Phase 3 program; obinutuzumab likely comparator/pretreatment arm) |

*Note: 50 trials total were returned; the table above prioritizes trials in which obinutuzumab is the primary backbone agent (Grade A relevance) plus representative larger studies.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | N Engl J Med | Obinutuzumab-based vs. rituximab-based chemotherapy for first-line follicular lymphoma |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM study: obinutuzumab significantly prolonged PFS vs. rituximab across chemotherapy backbones |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM final analysis: obinutuzumab vs. rituximab immunochemotherapy in untreated iNHL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in R/R FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | Lancet Haematol | GALEN: obinutuzumab + lenalidomide in relapsed/refractory FL |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | RCT/Cohort | Haematologica | Polatuzumab vedotin + bendamustine + rituximab/obinutuzumab in R/R FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Impact of obinutuzumab alone and in combination for FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | Comprehensive review of FL management, including obinutuzumab-based regimens |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Front Pharmacol | Efficacy, safety, and cost-effectiveness of obinutuzumab in FL |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Review | Drugs Today | Obinutuzumab in follicular lymphoma |

---

## Other TxGNN-Predicted Indications (Exploratory Hypotheses)

Beyond follicular lymphoma, the model separately flagged two closely related, molecularly-defined disease labels with an almost identical prediction score (**99.21%**), but the current evidence collection found **zero clinical trials and zero publications** under either precise label:

| Predicted Disease | TxGNN Score | Evidence | Level | Recommendation |
|---|---|---|---|---|
| Pregerminal center CLL/SLL (IGHV-unmutated) | 99.21% | 0 trials / 0 literature | L5 | Research Question |
| CLL/SLL with IGHV somatic hypermutation | 99.21% | 0 trials / 0 literature | L5 | Research Question |

**Why these are still worth tracking:** Mechanistically, obinutuzumab's cytotoxicity acts directly on the CD20 antigen and is not expected to depend on IGHV mutation status, so the mechanistic rationale is strong for both subtypes. The absence of evidence is most likely an **ontology-matching gap** — real-world trials and PubMed records almost never register under these precise IGHV-subtype labels, and instead use the umbrella term "CLL/SLL." This means the true evidence base may exist but was not captured under this exact disease name, rather than genuinely not existing. Per the evidence pack's own scoring rules, however, these remain L5/Research Question until a broader CLL/SLL-label search is performed and reviewed against these specific molecular subgroups.

**Recommended action:** Re-run trial/literature retrieval using the broader term "chronic lymphocytic leukemia/small lymphocytic lymphoma" (without the IGHV-subtype qualifier), then manually screen for IGHV-status-stratified subgroup data before deciding whether these two entries can be upgraded past L5.

---

## Saudi Arabia Market Information

Obinutuzumab currently has **no marketing authorization on file in Saudi Arabia** — `total_licenses = 0` and market status is recorded as **Not marketed (未上市)**. No product names, dosage forms, or approved-indication text are available in this dataset.

---

## Cytotoxicity

Obinutuzumab is an antineoplastic monoclonal antibody used exclusively in hematologic malignancies (CLL/SLL, follicular lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (immunotherapeutic anti-CD20 monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions — no DrugBank/TFDA toxicity data available in this dataset. Class-related B-cell depletion effects (profound/prolonged B-lymphopenia, hypogammaglobulinemia, increased infection risk) are noted in the trial evidence base (e.g., NCT04918940, post-vaccination immunization study in anti-CD20-treated patients) but formal hematologic toxicity grading was not retrieved |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (CBC) with differential, serum immunoglobulin levels, infection surveillance — based on the class-level B-cell depletion mechanism noted above; confirm against official labeling once available |
| Handling Protection | Please refer to the package insert warnings and precautions — biologic (monoclonal antibody) handling requirements should be confirmed against institutional hazardous-drug policy |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable in this dataset (`safety.key_warnings`, `safety.contraindications` both unresolved; DDI query returned `not_found`).

**Note:** The evidence pack flags this as a **Blocking**-severity data gap (DG001 — TFDA/local package-insert warnings and contraindications), explicitly noted as preventing entry into the S1 safety initial-evaluation stage. This gap must be resolved before any regulatory or clinical-use decision is finalized, independent of how strong the efficacy evidence is.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(applies to the Follicular Lymphoma indication; the two CLL/SLL molecular-subtype predictions remain at Hold/Research Question pending re-query — see above)*

**Rationale:**
- Follicular lymphoma is supported by L1-level evidence — multiple completed Phase 2/3 trials and RCTs (GALLIUM, GALEN, ROSEWOOD) — giving high confidence in efficacy and target biology.
- However, a **Blocking** safety data gap (DG001: TFDA/package-insert warnings and contraindications not yet retrieved) means the safety initial-evaluation (S1) stage cannot be completed, and the drug is not currently marketed in Saudi Arabia (0 authorizations) — hence "Guardrails" rather than an unconditional "Go."

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/local package insert to close the Blocking safety data gap (DG001) and complete S1 safety screening
- Obtain DrugBank MOA data to complete the mechanism-of-action record (DG002)
- Confirm local market-authorization pathway, since obinutuzumab currently has zero licenses in Saudi Arabia
- Re-run clinical trial/literature retrieval using the broader "CLL/SLL" term (without IGHV-subtype qualifiers) to determine whether the two exploratory subtype predictions can be upgraded beyond L5
- Establish a DDI query source, since the current interaction database returned no results (`not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

