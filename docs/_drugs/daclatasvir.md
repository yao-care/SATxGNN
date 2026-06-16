---
layout: default
title: Daclatasvir
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Daclatasvir
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

# Daclatasvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Daclatasvir (BMS-790052) is a pangenotypic NS5A replication complex inhibitor, approved in multiple countries for the treatment of chronic Hepatitis C virus (HCV) infection in combination with other direct-acting antivirals.
The TxGNN model predicts it may be effective for **Hepatitis B Virus (HBV) Infection** with a confidence score of **99.80%**, making it the top-ranked repurposing candidate.
However, this prediction is supported by only **1 partially relevant clinical trial** (n=23) and a handful of observational studies — with the majority of available evidence reflecting HBV reactivation events *during* Daclatasvir therapy, not antiviral suppression of HBV.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Daclatasvir binds directly to the NS5A replication complex of HCV, disrupting viral RNA replication, assembly, and virion release. It is active across all HCV genotypes and has demonstrated sustained virologic response (SVR) rates exceeding 90% in combination regimens with sofosbuvir or asunaprevir. Its potent antiviral activity against a hepatotropic RNA virus forms the basis for the TxGNN knowledge graph placing it in proximity to other hepatitis viral infections — including HBV.

The mechanistic connection to HBV is, however, extremely tenuous. HBV is a partially double-stranded DNA virus (*Hepadnaviridae*) that replicates via reverse transcription of a pregenomic RNA (pgRNA) intermediate. It does not encode an NS5A homologous protein. One computational study (PMID 36838792) used in silico virtual screening to identify Daclatasvir as a potential binder to the ε stem-loop of HBV pgRNA — a cis-acting element required for polymerase binding and pgRNA packaging — but this remains entirely speculative with no wet-lab or in vivo validation.

The clinical evidence available paints a more cautionary picture. Rather than suppressing HBV, Daclatasvir-based DAA therapy in HBV/HCV co-infected patients has been repeatedly associated with **HBV reactivation** (PMID 27329484, 26297529, 29194858). The leading hypothesis is that rapid HCV clearance removes the immunosuppressive competition HCV exerted on HBV, allowing dormant HBV to resurge. This mechanistic inverse — Daclatasvir indirectly *unmasking* HBV rather than suppressing it — fundamentally undermines the repurposing rationale. The TxGNN high score most likely reflects disease ontology proximity (both are hepatotropic viral infections in the same MeSH neighbourhood) rather than true pharmacological activity against HBV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | The only trial directly enrolling HCV/HBV co-infected patients. Study purpose was to determine HBV reactivation incidence during anti-HCV DAA treatment — not to evaluate Daclatasvir's efficacy against HBV. Sample size far too small to draw conclusions on direct anti-HBV activity. |
| [NCT02098616](https://clinicaltrials.gov/study/NCT02098616) | N/A | Completed | 25 | Pilot HCV elimination trial evaluating DCV/ASV/BMS-791325 ± ribavirin for 4–8 weeks in genotype 1a HCV without cirrhosis. No HBV-specific design. |
| [NCT03687229](https://clinicaltrials.gov/study/NCT03687229) | N/A | Unknown | 60 | Mechanistic study on miRNA-122 and insulin resistance in chronic HCV patients receiving DAAs. No HBV relevance. |
| [NCT03572140](https://clinicaltrials.gov/study/NCT03572140) | N/A | Unknown | 297 | Safety and resistance-associated variant assessment for sofosbuvir/daclatasvir in chronic HCV GT-4. No HBV design. |
| [NCT02565888](https://clinicaltrials.gov/study/NCT02565888) | Phase 1 | Completed | 16 | Drug-drug interaction study between Daclatasvir and antiretrovirals (atazanavir/ritonavir or cobicistat) in healthy volunteers. PK study; no antiviral efficacy assessment. |
| [NCT01012895](https://clinicaltrials.gov/study/NCT01012895) | Phase 2 | Completed | 215 | Safety, PK, and pharmacodynamics of BMS-790052 + BMS-650032 in HCV genotype 1 null responders to standard of care. HCV-only population. |
| [NCT03612973](https://clinicaltrials.gov/study/NCT03612973) | N/A | Completed | 80 | Assessment of liver fibrosis, lipid profile, and insulin resistance in chronic HCV patients on DAA therapy. No HBV design. |
| [NCT00546715](https://clinicaltrials.gov/study/NCT00546715) | Phase 1/2 | Completed | 95 | Early single ascending dose study of daclatasvir in chronic HCV genotype 1 patients; safety and tolerability focus. No HBV relevance. |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | Active-controlled comparison of ABT-493/ABT-530 versus SOF+DCV in HCV genotype 3. No HBV patients enrolled. |
| [NCT02095860](https://clinicaltrials.gov/study/NCT02095860) | Phase 1 | Completed | 24 | Crossover PK study assessing food effect on DCV/ASV/BMS-791325 fixed-dose combination in healthy subjects. No disease-relevance to HBV. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | J Viral Hepatitis | Among 25 HBV co-infected patients receiving interferon-free DAA therapy (including asunaprevir + daclatasvir), HBV reactivation occurred in a subset. Confirms Daclatasvir does not suppress HBV replication and may unmask dormant infection. |
| [27329484](https://pubmed.ncbi.nlm.nih.gov/27329484/) | 2016 | Case Report | Clin J Gastroenterol | An 83-year-old woman developed acute hepatitis B after daclatasvir + asunaprevir therapy cleared her HCV. HBV reactivation directly following Daclatasvir use demonstrates absence of anti-HBV activity. |
| [26297529](https://pubmed.ncbi.nlm.nih.gov/26297529/) | 2016 | Case Report | Hepatol Res | HBV reactivation (anti-HBe hepatitis) emerged in an HBV/HCV co-infected patient during interferon-free daclatasvir + asunaprevir therapy, requiring tenofovir rescue. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | SOF/DCV-based therapy in Egyptian HCV and HCV/HBV co-infected patients confirmed high SVR rates for HCV component; did not evaluate direct antiviral activity of Daclatasvir against HBV. |
| [36838792](https://pubmed.ncbi.nlm.nih.gov/36838792/) | 2023 | In silico | Molecules | Virtual screening study identifying potential small molecule binders to the HBV pgRNA ε stem-loop (novel therapeutic target). Daclatasvir appeared as a candidate binder — entirely computational, no experimental validation. |
| [28555436](https://pubmed.ncbi.nlm.nih.gov/28555436/) | 2017 | Cohort | Indian J Gastroenterol | HBV co-infection was associated with higher HCC recurrence rates after DAA therapy in HCV patients; highlights clinical importance of HBV monitoring during DAA treatment. |
| [27311286](https://pubmed.ncbi.nlm.nih.gov/27311286/) | 2016 | Review | Rinsho Byori | Review of viral hepatitis therapy including DAA-era HCV treatment; discusses HBV reactivation as a recognised complication of interferon-free DAA regimens. |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Review of HCV DAA targets (NS3/4A, NS5A, NS5B); explicitly distinguishes HCV as curable with DAAs while noting HBV and HIV require entirely different treatment approaches. |
| [30369001](https://pubmed.ncbi.nlm.nih.gov/30369001/) | 2019 | Cohort | Transpl Infect Dis | SOF+DCV achieved high HCV SVR rates in kidney transplant recipients; good tolerability profile. No HBV data; included for drug safety characterisation. |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | SOF-VEL-VOX re-treatment in patients with prior daclatasvir failure in Rwanda; relevant to understanding limitations and resistance patterns of NS5A inhibitors. No HBV data. |

---

## Saudi Arabia Market Information

Daclatasvir is currently **not approved or marketed in Saudi Arabia**. No product registrations or authorisation numbers are on file with the regulatory authority. Any clinical use within Saudi Arabia would require individual patient compassionate access or import exemption procedures.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for HBV co-infected patients:** Multiple published case reports and cohort data document HBV reactivation during Daclatasvir-containing DAA regimens (PMID 27329484, 26297529, 29194858). Screening for HBsAg and anti-HBc prior to initiating any DAA therapy and appropriate HBV prophylaxis or monitoring are strongly recommended per current international guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Daclatasvir repurposing in HBV is critically weak — HBV lacks any NS5A homolog, replicates via reverse transcriptase rather than RNA-dependent RNA polymerase, and the available clinical evidence specifically documents that Daclatasvir does not suppress HBV replication. On the contrary, DAA-mediated HCV clearance can trigger HBV reactivation, representing a net safety concern rather than a therapeutic opportunity.

**To proceed, the following would be required:**

- **Wet-lab antiviral activity data**: In vitro HBV inhibition assays (HepG2.2.15, HBV-transfected cells) to experimentally verify or refute the in silico binding prediction (PMID 36838792)
- **Mechanism validation**: Biophysical binding confirmation of Daclatasvir to HBV pgRNA ε stem-loop (EMSA, ITC, or NMR)
- **MOA characterisation**: Formal Daclatasvir mechanism-of-action data from DrugBank to assess cross-target potential (currently unavailable)
- **Safety label review**: Full SFDA prescribing information for contraindications and warnings (currently unavailable)
- **Regulatory baseline**: Given zero Saudi Arabia market authorisations, any clinical development would require full dossier submission from scratch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

