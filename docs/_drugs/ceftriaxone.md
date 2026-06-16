---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ceftriaxone: From Systemic Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic used worldwide for serious systemic bacterial infections including meningitis, sepsis, and community-acquired pneumonia. The TxGNN model predicts it may be effective for **Infectious Otitis Media** — the strongest repurposing signal among 7 predicted indications — with **3 clinical trials** and **19 publications** currently supporting this direction. This multi-indication analysis also identifies **Suppurative Otitis Media** and **Chronic Otitis Media** as secondary research-worthy targets (L3), while three other predicted indications are assessed as Hold due to absent mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic bacterial infections (meningitis, sepsis, pneumonia) — international approvals; no Saudi Arabia license data available |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All Predicted Indications (Multi-Indication Summary)

The following table summarises all 7 TxGNN-predicted indications, re-sorted by evidence quality rather than raw model score:

| Evidence Rank | Disease | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|---|---|---|---|---|---|---|
| 1 | Infectious otitis media | 99.26% | L1 | 3 | 19 | Proceed with Guardrails |
| 2 | Suppurative otitis media | 99.02% | L3 | 0 | 20 | Research Question |
| 3 | Chronic otitis media | 99.01% | L3 | 0 | 19 | Research Question |
| 4 | Hyperamylasemia | 99.39% | L4 | 0 | 3 | Hold |
| 5 | Polyclonal hyperviscosity syndrome | 99.39% | L5 | 0 | 0 | Hold |
| 6 | Congenital analbuminemia | 99.37% | L5 | 0 | 0 | Hold |
| 7 | Blood group incompatibility | 99.12% | L5 | 0 | 2 | Hold |

> **Analyst note:** The top three TxGNN-ranked indications by model score (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia) all lack clinical or mechanistic support. Infectious otitis media ranks only 4th by model score yet carries L1 evidence — illustrating that raw TxGNN score alone should not drive prioritisation decisions.

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is listed as a data gap in this Evidence Pack. Based on established pharmacological knowledge, ceftriaxone exerts bactericidal activity by irreversibly binding to penicillin-binding proteins (PBPs) on the bacterial cell membrane, inhibiting peptidoglycan cross-linking and causing osmotic lysis. Its extended plasma half-life (~8 hours) enables once-daily dosing, and it achieves therapeutic concentrations in middle ear fluid — a pharmacokinetic property critical for otitis media treatment.

Infectious otitis media (acute otitis media, AOM) is predominantly caused by three bacterial pathogens: *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Ceftriaxone demonstrates excellent in vitro activity against all three, including many penicillin-resistant *S. pneumoniae* strains. For patients in whom first-line oral amoxicillin fails, or where oral administration is not feasible (vomiting, poor compliance), intramuscular ceftriaxone (50 mg/kg IM, max 1 g, single or 3-day course) has become a well-established rescue strategy endorsed by multiple international pediatric infectious disease guidelines.

Notably, TxGNN also predicted suppurative otitis media (rank 6, L3) and chronic otitis media (rank 7, L3) as separate targets, all from the same mechanistic branch. This clustering of three closely related middle-ear infection entities reinforces the biological coherence of the prediction. The primary consideration is not clinical plausibility — this is already established — but rather the **regulatory status in Saudi Arabia** (0 current authorisations), which creates both a gap and an actionable registration opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Multicenter double-blind RCT comparing 5-day vs 10-day antibiotic courses in children aged 6–23 months with AOM; evaluates clinical cure rates and antimicrobial resistance impact. Methodologically rigorous design; terminated early (enrollment challenges), reducing evidence weight. |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Tympanostomy tube placement vs non-surgical management for recurrent AOM in children over 2 years. Not a direct ceftriaxone efficacy trial, but provides disease burden context and benchmark outcomes for AOM episodes. |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study of Prevnar 13 vaccine impact on AOM rates in children. Provides epidemiological context on *S. pneumoniae* serotype distribution relevant to ceftriaxone's pathogen coverage. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective randomised single-blind trial: single IM ceftriaxone dose vs 10-day oral TMP-SMZ for AOM (Greater Boston Otitis Media Study Group). Key head-to-head comparative efficacy data for IM ceftriaxone. |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | 1-day vs 3-day IM ceftriaxone regimen for non-responsive AOM in children. Three-day course demonstrated superior bacteriologic eradication for drug-resistant *S. pneumoniae*. |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review/Guidelines | *JAMA Network Open* | Optimal pediatric outpatient antibiotic prescribing practices in the US; addresses appropriateness of ceftriaxone as rescue therapy for AOM and antimicrobial stewardship considerations. |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Clinical recommendations for prevention and antimicrobial treatment of AOM and meningitis in children with cochlear implants; ceftriaxone positioned as preferred parenteral agent. |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Review | *Pediatrics* | Cochlear implant management guideline: pneumococcal AOM prevention via vaccination and ceftriaxone treatment for AOM/meningitis in high-risk paediatric patients. |
| [38368849](https://pubmed.ncbi.nlm.nih.gov/38368849/) | 2024 | Review | *American Journal of Emergency Medicine* | Acute mastoiditis (serious AOM complication with high morbidity/mortality): ceftriaxone as backbone IV/IM empirical therapy in emergency settings. |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | *Int J Pediatric Otorhinolaryngology* | Large US primary care cohort documenting real-world IM ceftriaxone use patterns for AOM; identifies clinical factors associated with prescribing and antimicrobial resistance implications. |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Cohort | *Pediatric Infectious Disease Journal* | Dynamics of pneumococcal nasopharyngeal carriage in children with non-responsive AOM treated with 1-day vs 3-day IM ceftriaxone; 3-day regimen superior for resistant strains. |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical Study | *Pediatric Infectious Disease Journal* | Bacteriologic efficacy of 3-day IM ceftriaxone regimen specifically in non-responsive AOM children; establishes eradication rates against key middle ear pathogens. |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus | *Clinical Pediatrics* | Roundtable consensus recommendations for AOM management integrating MEDLINE evidence; ceftriaxone defined as second-line option for treatment failures and penicillin-allergic patients. |

---

## Saudi Arabia Market Information

Ceftriaxone currently has **no registered products in Saudi Arabia** (SFDA authorisations: 0). No authorisation table can be generated from the available data.

This represents a significant regulatory gap for a drug that appears on the WHO Model List of Essential Medicines and is widely marketed across the United States, Europe, and Asia-Pacific. The absence of local registration does not reflect a clinical evidence gap but rather a market access gap — which is the primary barrier to clinical deployment in Saudi Arabia.

---

## Safety Considerations

Complete package insert safety data (SFDA/TFDA warnings and contraindications) was not available at the time of this analysis. Please refer to the originator package insert for full safety information.

The following safety signals are well-documented in the published literature and warrant attention:

- **Biliary sludge and pseudocholelithiasis**: Ceftriaxone precipitates calcium salt complexes in bile; particularly relevant at high doses and in paediatric patients. Reversible upon discontinuation.
- **Neonatal hyperbilirubinemia**: Ceftriaxone displaces bilirubin from albumin binding sites and is **contraindicated** in neonates with hyperbilirubinemia or those receiving calcium-containing IV infusions (fatal cardiopulmonary precipitate cases reported).
- **Immune-mediated haemolytic anaemia**: Rare but potentially fatal immune haemolysis via hapten mechanism; requires immediate discontinuation if suspected.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftriaxone has robust mechanistic support and L1 clinical evidence for infectious otitis media — including two randomised controlled trials directly evaluating IM ceftriaxone for AOM treatment, reinforced by multiple international consensus guidelines positioning it as the standard rescue antibiotic. The primary barrier to deployment in Saudi Arabia is not clinical uncertainty but the complete absence of local SFDA market authorisation (0 products registered), which requires a regulatory pathway evaluation rather than additional evidence generation.

**To proceed, the following is needed:**
- SFDA regulatory pathway assessment for ceftriaxone registration in Saudi Arabia (standalone submission vs. reference to FDA/EMA approvals as established essential medicine)
- Complete package insert review to resolve the Blocking data gap on warnings and contraindications (DG001)
- DrugBank MOA data retrieval to formally document mechanism of action (DG002 — High severity)
- Paediatric dosing and IM formulation protocol review appropriate for Saudi Arabia clinical settings
- Drug-drug interaction profile assessment (DDI database query returned no results; manual review of package insert required)
- Institutional antimicrobial stewardship alignment for intramuscular ceftriaxone use in outpatient AOM management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

