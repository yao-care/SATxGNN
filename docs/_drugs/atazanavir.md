---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 6
---

# Atazanavir
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

# Atazanavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Atazanavir is an HIV protease inhibitor used internationally for the treatment of HIV-1 and HIV-2 infection, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **1 publication** currently supporting this direction.
Of note, two additional predictions within the HIV disease spectrum — AIDS Related Complex (rank 5) and Congenital HIV Infection (rank 6) — carry **L1 evidence** backed by multiple completed Phase 3 trials, representing substantially more actionable repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1/HIV-2 infection (internationally approved; not registered in Saudi Arabia) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atazanavir is an azapeptide-class HIV protease inhibitor (PI). It selectively binds to and inhibits HIV-1/HIV-2 protease — the enzyme responsible for cleaving the Gag-Pol polyprotein precursor into structural proteins and enzymes required for mature, infectious virion assembly. Without active protease, newly budded viral particles remain immature and non-infectious. In clinical practice, atazanavir is pharmacokinetically boosted with ritonavir (300/100 mg once daily) or cobicistat and deployed as part of combination antiretroviral therapy (cART). It carries a distinct metabolic advantage over earlier PIs in that it causes less dyslipidaemia.

SIV (Simian Immunodeficiency Virus) is a lentivirus closely related to HIV that naturally infects non-human primates — chimpanzees, sooty mangabeys, and macaques. The SIV protease shares considerable structural and sequence homology with HIV-1 protease, making it a biologically plausible target for PI-class agents. Indeed, SIV-infected rhesus macaque models are the standard preclinical platform for testing HIV/AIDS therapeutics, and PI-containing HAART regimens have been evaluated in these models to study viral suppression, CNS reservoir dynamics, and immune reconstitution.

However, it is important to contextualise this prediction: SIV is not a human pathogen. Any repurposing application would be confined to veterinary or preclinical research settings rather than a human clinical indication. The TxGNN model likely generated this high-scoring prediction through structural homology propagation within its lentivirus knowledge-graph node cluster. The single supporting publication (a primate HAART model study) confirms biological plausibility but does not establish a human therapeutic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal Study (Primate Model) | The Journal of Infectious Diseases | SIV-infected macaques treated with HAART showed reduced CNS viral replication and neuroinflammation, but viral DNA persisted in the CNS despite effective plasma viremia suppression — highlighting the CNS reservoir problem relevant to both SIV and HIV |

---

## Saudi Arabia Market Information

Atazanavir has no regulatory authorisations in Saudi Arabia. It is not currently marketed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Simian immunodeficiency virus infection is a non-human primate disease with no established human clinical indication pathway; the sole supporting publication is a primate animal model study (evidence tier 3, L4), and no clinical trials exist. While the mechanistic extrapolation from HIV to SIV is biologically reasonable, this prediction does not translate into a viable human drug repurposing candidate.

**To proceed with SIV-related research, the following is needed:**
- Clarify the research question: Is the goal to use atazanavir in SIV macaque models to study CNS penetration and HIV-associated neurocognitive disorders (HAND)?
- If targeting HAND or CNS reservoir research: redesign as a dedicated CNS-HIV translational study
- Obtain full mechanism of action data for atazanavir (currently a data gap)
- Assess regulatory pathway in Saudi Arabia before any clinical application

---

### Higher-Priority Predictions Warranting Immediate Attention

Two TxGNN predictions within the HIV disease spectrum carry **L1 evidence** and a **"Proceed with Guardrails"** recommendation — far stronger than the rank-1 SIV prediction:

**AIDS Related Complex (rank 5, score 99.71%, L1)**
- 2 completed Phase 3 trials directly assessing atazanavir: [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) (n=571, ATV+RTV vs LPV/r) and [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) (n=82, paediatric Phase 3)
- AIDS Related Complex represents the mid-spectrum stage of HIV infection; atazanavir's direct mechanism (HIV protease inhibition) applies throughout the entire HIV disease continuum, including ARC
- 3 supporting publications including retrospective cohort and in vitro mechanistic studies

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | ATV+RTV or ATV+SQV combined with LPV/r, TDF and nucleoside backbone in treatment-experienced HIV subjects; head-to-head virologic suppression and safety data |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | ATV powder boosted with RTV in HIV-infected children ≥3 months to <6 years (PRINCE I); international multicentre PK, safety, and efficacy |

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort/Observational | AIDS Reviews | Risk factors for GI adverse events in HIV-treated patients; atazanavir-related tolerability profile in ARC/AIDS continuum |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Retrospective Cohort | J Acquir Immune Defic Syndr | Differential effects of cART regimens including PI-based therapy on AIDS-defining neurological conditions (neuroAIDS) |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | Medicinal Chemistry / In Vitro | Antimicrobial Agents and Chemotherapy | CNS-targeting HIV protease inhibitors with enhanced blood-brain barrier penetration — context for next-generation PI design beyond atazanavir |

---

**Congenital HIV / Prevention of Mother-to-Child Transmission (rank 6, score 99.71%, L1)**
- 33 clinical trials retrieved; 7 publications covering pregnancy PK, congenital anomaly surveillance, and placental drug transport

Selected key trials (top 10 by relevance):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | ATV/r vs LPV/r each with TDF/FTC over 96 weeks in treatment-naïve HIV-1 subjects; largest head-to-head PI comparison trial |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | Switch from boosted PI (including ATV/r) to D/C/F/TAF single-tablet regimen; largest completed randomised switch trial |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | ATV capsule + RTV in HIV-infected paediatric patients aged 6–<18 years; dedicated safety data collection in specific paediatric populations |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | PK of ARV and anti-TB drugs during pregnancy and postpartum; core dataset for ATV dosing adjustments in pregnancy |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A | Completed | 1,578 | IMPAACT P1026s — the definitive prospective PK study of ARVs including ATV in pregnant women and their infants |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS study — long-acting CAB+RPV vs PI-based (including ATV) regimens in virologically suppressed adults |
| [NCT00135356](https://clinicaltrials.gov/study/NCT00135356) | Phase 4 | Completed | 219 | REAL study — ATV/r substitution for lipodystrophy management in HIV-infected patients on HAART |
| [NCT01003990](https://clinicaltrials.gov/study/NCT01003990) | Phase 3 | Completed | 710 | Extended access study providing long-term safety data across ATV clinical trial completers |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II — ATV powder + RTV in paediatric patients 3 months to <11 years; safety, efficacy and PK |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | DTG/ABC/3TC vs ATV+RTV+TDF/FTC in HIV-1 infected ART-naïve women over 48 weeks |

Key literature for congenital HIV / PMTCT:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort (PHACS SMARTT) | Frontiers in Immunology | Comprehensive surveillance of in utero ARV toxicities across >3,500 HIV-exposed uninfected infants; metabolic, cardiac, neurological, and developmental outcomes assessed |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Prospective PK Study | Antiviral Therapy | ATV exposure remains adequate during pregnancy regardless of tenofovir co-use; informs dosing strategy for PMTCT |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Prospective Observational | JAMA Pediatrics | Congenital anomaly rates in HIV-exposed uninfected infants with in utero ARV exposure including ATV; safety signal assessment |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/Non-case (Pharmacovigilance) | European Journal of Clinical Pharmacology | European congenital anomaly registry analysis of ARV-exposed pregnancies; most recent pharmacovigilance dataset on ATV fetal safety |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In Vitro / Mechanistic | Reproductive Toxicology | ATV and RTV interactions with placental ABC transporters (ABCB1, ABCG2, ABCC2); explains moderate placental transfer and informs fetal exposure modelling |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Prospective Observational | Journal of AIDS and Immune Research | Newborn hearing screening outcomes in HIV-exposed uninfected infants from PHACS SMARTT; safety surveillance data |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance Database Analysis | Clinical Infectious Diseases | Pharmacovigilance database analysis of ARV safety signals in pregnancy; comparative context for ATV vs newer agents |

**Guardrails for congenital HIV / PMTCT indication:**
- Monitor for maternal nephrolithiasis (urinary crystal risk elevated in pregnancy)
- Neonatal hyperbilirubinaemia risk (UGT1A1 inhibition → indirect bilirubin accumulation)
- ATV AUC decreases ~17–28% during second/third trimester when co-administered with TDF; dose adjustment to ATV/r 400/100 mg may be required
- Placental transfer is moderate; neonatal exposure should be monitored
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

