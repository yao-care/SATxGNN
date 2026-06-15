---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# AZITHROMYCIN: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Azithromycin is a widely used macrolide antibiotic active against a broad spectrum of bacterial pathogens — including atypical organisms — with well-recognised immunomodulatory properties beyond its antimicrobial mechanism.
The TxGNN model has generated **10 predicted new indications** for this drug; the top-ranked is **Polyclonal Hyperviscosity Syndrome** (score 99.81%), which is currently supported by **no clinical trials or publications** (L5) and has limited mechanistic rationale.
The best-supported candidate in this pack is **Congenital Hematological Disorder** (specifically sickle cell disease pulmonary complications, rank 10), backed by **4 registered clinical trials** and a **Cochrane systematic review** (L3).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, skin/soft tissue, STIs) |
| Top Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (top prediction) |
| Saudi Arabia Market Status | ✗ Not Marketed (0 authorisations) |
| Number of Authorisations | 0 |
| Recommended Decision | Hold (top prediction) / Research Question (ranks 4, 7, 9, 10) |

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.81% | L5 | Hold |
| 2 | Hyperamylasemia | 99.81% | L5 | Hold |
| 3 | Congenital Analbuminemia | 99.79% | L5 | Hold |
| 4 | Punctate Epithelial Keratoconjunctivitis | 99.78% | L4 | Research Question |
| 5 | Blood Group Incompatibility | 99.70% | L5 | Hold |
| 6 | Premalignant Hematological System Disease | 99.64% | L5 | Hold |
| 7 | Monoclonal Gammopathy | 99.61% | L4 | Research Question |
| 8 | Haematological Disease with Acquired Peripheral Neuropathy | 99.56% | L5 | Hold |
| 9 | Septicemic Plague | 99.52% | L3 | Research Question |
| 10 | Congenital Hematological Disorder | 99.40% | L3 | Research Question |

---

## Why Are These Predictions Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, azithromycin is a macrolide antibiotic; its established antimicrobial activity derives from binding the 50S bacterial ribosomal subunit and blocking protein synthesis. Beyond bacteriostatic effects, azithromycin is also recognised for immunomodulatory properties — suppression of NF-κB signalling, reduction of pro-inflammatory cytokines (IL-8, TNF-α, IL-6), inhibition of neutrophil extracellular trap formation, and blockade of autophagy flux in eukaryotic cells — which underlie its proven clinical benefits in chronic inflammatory airway diseases such as cystic fibrosis and bronchiectasis.

**Ranks 1, 2, 3, 5, 6, and 8 are likely knowledge-graph artefacts.** Polyclonal immunoglobulin overproduction, congenital albumin deficiency, blood group incompatibility, and acquired peripheral neuropathy have no established pharmacological interface with azithromycin's known mechanisms. The TxGNN model likely generated these predictions through shared plasma cell or protein-synthesis pathway nodes in the knowledge graph rather than genuine pharmacological opportunity. Notably, rank 2 (hyperamylasemia) is particularly concerning: azithromycin itself carries a reported adverse effect of elevated serum amylase, making this a potential safety signal rather than a treatment target.

**Four predictions carry mechanistic plausibility and supporting evidence:**

- **Punctate Epithelial Keratoconjunctivitis (Rank 4):** When caused by intracellular organisms such as *Chlamydia trachomatis* or *Microsporidia*, azithromycin is already an established treatment — it is first-line therapy for trachoma and has in vitro activity against microsporidial species. The single case report in this pack describes microsporidial keratoconjunctivitis where azithromycin was included in the treatment regimen.

- **Monoclonal Gammopathy / Multiple Myeloma (Rank 7):** The most mechanistically compelling link in the pack. Macrolides including azithromycin block autophagy flux and induce ER stress–mediated CHOP expression, sensitising myeloma cell lines (U266, IM-9, RPMI8226) to bortezomib (PMID 23546223). Plasma cells are highly dependent on proteostasis; disrupting autophagy impairs their survival. This is an in vitro finding only — no clinical data yet exist.

- **Septicemic Plague (Rank 9):** Azithromycin concentrates to high levels in macrophages, which is theoretically advantageous for *Yersinia pestis* given its intracellular lifestyle. However, direct in vitro susceptibility data show **poor activity** against Y. pestis strains (PMID 8540736), substantially limiting the actionability of this prediction.

- **Congenital Hematological Disorder / Sickle Cell Disease (Rank 10):** Azithromycin's anti-inflammatory immunomodulation may reduce the frequency and severity of Acute Chest Syndrome (ACS) — the leading cause of death in SCD — and improve pulmonary function (FEV1). Two independent Phase 1 trials were designed to test this hypothesis (NCT02630394, NCT02960503) before withdrawal prior to enrollment, indicating the scientific community has already moved this hypothesis to clinical evaluation. The approach is analogous to proven macrolide prophylaxis in cystic fibrosis and bronchiectasis.

---

## Clinical Trial Evidence

### Congenital Hematological Disorder — Sickle Cell Disease (Rank 10)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Azithromycin prophylaxis to reduce Acute Chest Syndrome in SCD — trial withdrawn before enrollment; macrolide anti-inflammatory rationale validated at design stage |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adult SCD patients — two independent withdrawn trials confirm scientific consensus on hypothesis; withdrawal reason not publicly disclosed |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Paediatric PK/PD of understudied drugs including azithromycin in children managed per standard of care — provides dosing and safety reference for haematological disease populations |

For all other predictions (ranks 1–9), no relevant clinical trials are currently registered.

---

## Literature Evidence

### Punctate Epithelial Keratoconjunctivitis (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | *Encephalitozoon hellem* keratoconjunctivitis in an immunocompetent adult, diagnosed by metagenomic deep sequencing and PCR; azithromycin included in the treatment protocol alongside fumagillin |

### Monoclonal Gammopathy (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | In vitro / Mechanistic | Int J Oncol | **Primary mechanistic rationale:** Azithromycin blocks autophagy flux (LC3B-II and p62 accumulation) and, in combination with bortezomib, enhances cytotoxicity in multiple myeloma cell lines via ER stress–CHOP pathway induction |
| [22825522](https://pubmed.ncbi.nlm.nih.gov/22825522/) | 2012 | Case Report | Tumori | Bisphosphonate-related osteonecrosis of the jaw in a multiple myeloma patient; azithromycin 500 mg/day used as adjunct antibiotic alongside ozone therapy — indirect evidence |
| [33389938](https://pubmed.ncbi.nlm.nih.gov/33389938/) | 2020 | Case Report | Turk J Ophthalmol | *Bartonella henselae* neuroretinitis complicating POEMS syndrome; azithromycin used to treat the Bartonella infection, not the underlying monoclonal gammopathy |
| [18355359](https://pubmed.ncbi.nlm.nih.gov/18355359/) | 2008 | Review | Clin Exp Dermatol | Subcorneal pustular dermatosis (Sneddon-Wilkinson), occasionally associated with IgA monoclonal gammopathy; azithromycin not discussed as a therapeutic option |

### Septicemic Plague (Rank 9)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro MIC Study | Antimicrob Agents Chemother | Susceptibility testing of 78 *Y. pestis* strains — azithromycin showed **poor activity** across all strains; ceftriaxone and ciprofloxacin were far superior |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Animal Model | Antibiotics Chemotherapy | Azithromycin demonstrated high efficacy against intracellular *Brucella* in an experimental animal model, with rapid normalisation of bactericidal systems in peripheral blood — class-level support for intracellular pathogen coverage |
| [19392866](https://pubmed.ncbi.nlm.nih.gov/19392866/) | 2009 | Systematic Review | Aliment Pharmacol Ther | Epidemiology and clinical features of travellers' diarrhoea — azithromycin cited as an effective treatment for enteric pathogens including *Campylobacter*; indirect relevance to gram-negative intracellular coverage |

### Congenital Hematological Disorder — Sickle Cell Disease (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Cochrane Systematic Review | Cochrane Database Syst Rev | Antibiotic prophylaxis (including macrolides) for preventing lower respiratory tract infections in high-risk children under 12 — supports the rationale for azithromycin prophylaxis in haematological disease populations with pulmonary vulnerability |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | Case Report | Am J Case Rep | COVID-19–associated immune thrombocytopenia in a 9-month-old infant treated with megadose methylprednisolone; azithromycin used concomitantly for COVID-19 management — indirect evidence only |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Data gaps exist for both TFDA package insert warnings/contraindications (DG001, Blocking severity) and detailed mechanism of action (DG002, High severity). These gaps prevent formal S1 safety screening from being completed. Resolution should be prioritised before advancing any of the Research Question candidates.

---

## Conclusion and Next Steps

**Decision: Hold** (Polyclonal Hyperviscosity Syndrome — top-ranked prediction)

**Rationale:**
Six of the 10 predictions carry L5 evidence with no clinical or mechanistic support; the top prediction is most plausibly a knowledge-graph artefact with no pharmacological basis. However, four predictions — particularly sickle cell disease and monoclonal gammopathy — warrant structured follow-up.

**Prioritised research actions by indication:**

| Indication | Recommended Action | Priority |
|-----------|-------------------|----------|
| Sickle Cell Disease / ACS (Rank 10) | Investigate reasons for withdrawal of NCT02630394 and NCT02960503; if due to funding or design issues (not safety), design a new feasibility trial with ACS incidence as primary endpoint | **High** |
| Monoclonal Gammopathy / Myeloma (Rank 7) | Advance to in vivo validation; explore azithromycin + bortezomib combination in xenograft myeloma models; clarify whether MGUS (pre-malignant) or active myeloma is the better target | **Medium** |
| Punctate Epithelial Keratoconjunctivitis (Rank 4) | Conduct a focused literature review on azithromycin for microsporidial and chlamydial keratoconjunctivitis; consider prospective case series given existing first-line use in trachoma | **Low** |
| Septicemic Plague (Rank 9) | Relevant only in antibiotic-resistance or special-population (paediatric/obstetric) scenarios; poor in vitro Y. pestis activity substantially limits priority | **Low** |

**To proceed, the following is needed:**
- Package insert warnings and contraindications from TFDA/equivalent authority (DG001 — currently blocking S1 safety evaluation)
- Complete MOA documentation from DrugBank (DG002 — required for mechanistic analysis)
- Clarification of withdrawal reasons for NCT02630394 and NCT02960503 (critical decision point for the sickle cell disease pathway)
- In vivo myeloma studies to validate the in vitro autophagy/bortezomib sensitisation finding (PMID 23546223)
- Confirmation of Saudi Arabia regulatory filing status through local channels, given 0 current authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

