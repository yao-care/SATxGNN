---
layout: default
title: Telaprevir
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
---

# Telaprevir
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

# Telaprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Telaprevir is a first-generation NS3/4A protease inhibitor originally developed and approved for chronic hepatitis C virus (HCV) genotype 1 infection. The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **18 clinical trials** and **20 publications** currently retrieved — however, essentially all of this evidence describes telaprevir being used to treat **HCV** in patients who are also HIV-positive (drug-interaction and safety studies), not any direct antiviral activity against HIV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C, Genotype 1 (inferred from clinical trial/literature evidence in this pack; not present in the structured license fields — see Data Gaps) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for telaprevir is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, telaprevir is a first-generation direct-acting antiviral (DAA) — specifically a peptidomimetic inhibitor of the **HCV NS3/4A serine protease**, which is essential for HCV polyprotein processing and replication. It was approved (in combination with peginterferon alfa and ribavirin) for chronic hepatitis C genotype 1.

The TxGNN model links telaprevir to HIV infectious disease at a very high graph-similarity score (99.98%), and the evidence retrieval layer surfaced 18 clinical trials and 20 publications. On closer inspection, however, none of this evidence demonstrates antiviral activity of telaprevir against HIV. Instead, it consists of pharmacokinetic drug-drug interaction (DDI) studies and real-world safety/efficacy studies of telaprevir **treating HCV** in patients co-infected with HIV (e.g., interactions with raltegravir, dolutegravir, etravirine, atazanavir, darunavir/ritonavir, efavirenz/tenofovir). HCV's NS3/4A serine protease has no structural or mechanistic homology to HIV's aspartic protease, and telaprevir has no reported anti-HIV activity.

This is a case where TxGNN's graph-based similarity appears to conflate "co-occurs in HIV/HCV-coinfection literature" with "treats HIV" — the disease-term overlap (HIV and HCV frequently co-occur in coinfection cohorts) likely drove the high score rather than a genuine pharmacological rationale. This is consistent with the evidence pack's own repurposing rationale, which explicitly notes the absence of a mechanistic link.

---

## Clinical Trial Evidence

*Note: the trials below study telaprevir's treatment of HCV in HIV/HCV-coinfected populations, not treatment of HIV itself.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01513941](https://clinicaltrials.gov/study/NCT01513941) | Phase 3 | Completed | 163 | Efficacy/safety of telaprevir + peg-IFN-alfa-2a + ribavirin for HCV-1 in HCV/HIV-1-coinfected patients (naïve and experienced) |
| [NCT01467479](https://clinicaltrials.gov/study/NCT01467479) | Phase 3 | Terminated | 185 | Telaprevir + peg-IFN-alfa-2a + ribavirin to treat HCV in HCV/HIV-1-coinfected subjects |
| [NCT01500616](https://clinicaltrials.gov/study/NCT01500616) | Phase 3 | Completed | 122 | Telaprevir + peg-IFN + ribavirin in HIV/HCV-1-coinfected patients with severe fibrosis/compensated cirrhosis |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unknown | 1000 | Real-life efficacy/tolerability of DAA-based (incl. telaprevir) regimens for HCV in HIV-coinfected patients (HEPAVIR cohort) |
| [NCT01447446](https://clinicaltrials.gov/study/NCT01447446) | N/A | Completed | 4442 | Observational cohort on utilization/impact of peg-IFN-based dual/triple (incl. telaprevir) therapy for HCV, including HIV/HCV-coinfected |
| [NCT01332955](https://clinicaltrials.gov/study/NCT01332955) | Phase 2 | Completed | 70 | Telaprevir + peg-IFN + ribavirin in HIV-HCV-coinfected prior treatment failures (ANRS HC26 TelapreVIH) |
| [NCT02124044](https://clinicaltrials.gov/study/NCT02124044) | Phase 2 | Completed | 30 | Daclatasvir + asunaprevir ± BMS-791325 in HIV-HCV-coinfected subjects (telaprevir referenced as prior standard) |
| [NCT01563328](https://clinicaltrials.gov/study/NCT01563328) | Phase 1 | Completed | 32 | PK interaction study: effect of boceprevir/telaprevir on dolutegravir (HIV integrase inhibitor) pharmacokinetics |
| [NCT01253551](https://clinicaltrials.gov/study/NCT01253551) | Phase 1 | Completed | 21 | PK interaction study: telaprevir vs. raltegravir (HIV drug) at steady-state in healthy subjects — confirms no clinically relevant interaction |
| [NCT00983853](https://clinicaltrials.gov/study/NCT00983853) | Phase 2 | Completed | 62 | Telaprevir + peg-IFN-alfa-2a + ribavirin for HCV in treatment-naïve HCV-1/HIV-1-coinfected subjects |

---

## Literature Evidence

*Note: all publications below discuss telaprevir's role in treating HCV within HIV-coinfected populations (efficacy/safety/DDI), not treatment of HIV itself.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26416471](https://pubmed.ncbi.nlm.nih.gov/26416471/) | 2015 | Cohort | The Journal of Infection | Early access programme (HPC3005) of telaprevir-based therapy in HIV-1/HCV coinfected patients with severe fibrosis/cirrhosis |
| [26483516](https://pubmed.ncbi.nlm.nih.gov/26483516/) | 2016 | Clinical trial report | J Antimicrob Chemother | INSIGHT study (NCT01513941): efficacy, safety and PK of telaprevir-based therapy in HCV-1/HIV-1-coinfected patients |
| [22345334](https://pubmed.ncbi.nlm.nih.gov/22345334/) | 2012 | Review | Annals of Hepatology | Review of DDIs with boceprevir/telaprevir, implications for HIV and transplant patients |
| [25385188](https://pubmed.ncbi.nlm.nih.gov/25385188/) | 2015 | Review | Liver International | DDIs of telaprevir/boceprevir modify medication adherence in HCV-mono- and HIV/HCV-coinfected patients |
| [25923540](https://pubmed.ncbi.nlm.nih.gov/25923540/) | 2015 | Cohort | PLoS One | Real-life safety and efficacy of boceprevir/telaprevir triple therapy against HCV in HIV coinfection |
| [23925383](https://pubmed.ncbi.nlm.nih.gov/23925383/) | 2013 | Cohort | AIDS | Efficacy and tolerance of telaprevir in HIV-HCV genotype 1-coinfected patients failing prior HCV therapy (24-week results) |
| [24796757](https://pubmed.ncbi.nlm.nih.gov/24796757/) | 2014 | Cohort | AIDS Patient Care and STDs | Real-world therapeutic potential of boceprevir/telaprevir triple therapy in HIV/HCV-coinfected patients |
| [24063901](https://pubmed.ncbi.nlm.nih.gov/24063901/) | 2013 | Review | Enfermedades Infecciosas y Microbiología Clínica | Safety and efficacy of telaprevir in patients with HIV and HCV coinfection |
| [25769784](https://pubmed.ncbi.nlm.nih.gov/25769784/) | 2015 | PK study | Int J Antimicrob Agents | PK interactions between telaprevir and antiretrovirals in HIV/HCV-coinfected patients with advanced liver fibrosis |
| [25845407](https://pubmed.ncbi.nlm.nih.gov/25845407/) | 2015 | Review | Seminars in Dialysis | HIV and HCV medications (incl. boceprevir/telaprevir) in end-stage renal disease |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA package insert warnings, contraindications, and drug interaction data are currently unavailable — see Data Gaps below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No mechanistic basis supports telaprevir's activity against HIV — HCV's NS3/4A serine protease target has no homology to HIV's aspartic protease, and all retrieved clinical/literature evidence documents telaprevir's use in treating **HCV** within HIV/HCV-coinfected cohorts, not efficacy against HIV itself. Combined with the drug's non-marketed status in Saudi Arabia and the absence of TFDA/SFDA safety labeling, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism of action (MOA) data via DrugBank — currently a high-severity gap (DG002)
- A genuine in vitro/in vivo demonstration of anti-HIV activity, since existing trials only address HCV treatment in HIV-coinfected patients
- Re-evaluation of whether the TxGNN score reflects a true pharmacological signal or a coinfection-cohort keyword artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

