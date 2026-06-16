---
layout: default
title: Dasabuvir
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 5
---

# Dasabuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dasabuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Dasabuvir (ABT-333) is a direct-acting antiviral originally used for chronic Hepatitis C Virus (HCV) Genotype 1 infection as part of the Viekira Pak combination regimen (ombitasvir/paritaprevir/ritonavir + dasabuvir). The TxGNN model predicts it may be effective for **Hepatitis B Virus (HBV) infection** with a prediction score of **99.37%** (rank 9,325 overall). However, no clinical trials have directly evaluated dasabuvir for HBV treatment, and available literature only documents HBV as a safety monitoring endpoint during HCV co-infection therapy — yielding an **L5 evidence level** and a **Hold** recommendation.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic HCV Genotype 1 infection (inferred from drug class; no Saudi Arabia regulatory records available) |
| Predicted New Indication | Hepatitis B Virus (HBV) Infection |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only; no direct clinical studies) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from current regulatory records. Based on known pharmacological information, dasabuvir (development code ABT-333) is a **non-nucleoside NS5B RNA-dependent RNA polymerase (RdRp) inhibitor** that binds the thumb II allosteric pocket of the HCV NS5B protein. It is used exclusively in combination with ombitasvir/paritaprevir/ritonavir (Viekira Pak / Exviera), achieving sustained virological response (SVR12) rates exceeding 95% in HCV Genotype 1b patients.

The TxGNN model assigns a high score because HCV and HBV share substantial phenotypic overlap — both are hepatotropic viruses causing chronic liver disease, cirrhosis, and hepatocellular carcinoma risk, and they share transmission routes and patient populations. This disease-level proximity in the knowledge graph drives a strong association. Several trials in this evidence pack reflect how commonly patients are co-infected with both viruses.

However, pharmacological mechanism transferability is very limited. HBV replicates through a **reverse transcriptase (RT) pathway** encoded by its DNA polymerase, which is mechanistically and structurally distinct from the HCV NS5B RdRp. The thumb II allosteric binding pocket that dasabuvir occupies has **no structural homologue in HBV reverse transcriptase**. Established HBV antivirals (tenofovir, entecavir) work through nucleoside RT inhibition — a mechanism dasabuvir does not possess. The TxGNN high score reflects graph topology (hepatitis disease clustering), not validated pharmacological applicability to HBV.

## Clinical Trial Evidence

All 14 retrieved trials evaluated dasabuvir in the context of **HCV treatment**. No trial has directly assessed dasabuvir's efficacy against HBV. The single most relevant trial (Grade B) monitored HBV only as a safety endpoint.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | HCV/HBV co-infected patients receiving DAA therapy; primary endpoint was HCV SVR; **HBV reactivation monitored as a safety indicator only** — no anti-HBV efficacy evaluation |
| [NCT01854697](https://clinicaltrials.gov/study/NCT01854697) | Phase 3 | Completed | 311 | MALACHITE-I: ABT-450/r/ombitasvir + dasabuvir vs telaprevir/pegIFN/RBV in treatment-naïve HCV GT1; no HBV component |
| [NCT01939197](https://clinicaltrials.gov/study/NCT01939197) | Phase 2/3 | Completed | 318 | TURQUOISE-I: ombitasvir/paritaprevir/r ± dasabuvir ± RBV in HCV GT1/4 + HIV-1 co-infection; HCV SVR12 as primary endpoint, no HBV data |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | TURQUOISE-CPB: OBV/PTV/r + dasabuvir + RBV in HCV GT1 decompensated cirrhosis; HCV safety and SVR12 only |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Post-marketing safety surveillance of DAA medications for HCV (including dasabuvir regimens); large observational study, HCV population only |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Completed | 89 | Dose-ranging study of ABT-493 and ABT-530 in HCV GT1; antiviral activity assessment in HCV, no HBV arm |
| [NCT01464827](https://clinicaltrials.gov/study/NCT01464827) | Phase 2 | Completed | 580 | ABT-450/r ± ABT-267 ± dasabuvir ± RBV for 8–24 weeks in HCV GT1; evaluates antiviral activity and PK of dasabuvir combination |
| [NCT01782495](https://clinicaltrials.gov/study/NCT01782495) | Phase 2 | Completed | 129 | CORAL-I: ABT-450/r/ombitasvir + dasabuvir ± RBV in liver or renal transplant recipients with HCV GT1/4; transplant special population, HCV-focused |
| [NCT02493855](https://clinicaltrials.gov/study/NCT02493855) | Phase 2 | Completed | 46 | Viral load kinetics with OBV/ABT-450/r + dasabuvir ± ribavirin in HCV GT1a treatment-naïve; exploratory PK/PD study, no HBV |
| [NCT00851890](https://clinicaltrials.gov/study/NCT00851890) | Phase 2 | Completed | 30 | Early dasabuvir (ABT-333) safety, tolerability, PK, and antiviral activity study in HCV GT1 patients; foundational dasabuvir characterization |

> **None of the 14 retrieved trials include an HBV treatment arm or endpoint.** Evidence level for dasabuvir in HBV: **L5**.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) | 2018 | Cohort | J Viral Hepatitis | HBV reactivation risk in HBV+HCV co-infected cirrhosis patients (N=2,070 HCV) treated with ombitasvir/paritaprevir/r + dasabuvir + RBV; HBV monitored as safety concern, no anti-HBV efficacy data |
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | RCT | Lancet Gastroenterol Hepatol | GARNET Phase 3b: OBV/PTV/r + dasabuvir for 8 weeks in HCV GT1b without cirrhosis; high SVR12 rates confirmed; HCV efficacy only |
| [28903508](https://pubmed.ncbi.nlm.nih.gov/28903508/) | 2017 | RCT Analysis | Clin Infect Dis | PrOD and ledipasvir/sofosbuvir regimens confer significant mortality benefit vs untreated HCV in a large VA cohort; demonstrates overall clinical value of dasabuvir-containing regimens |
| [28762541](https://pubmed.ncbi.nlm.nih.gov/28762541/) | 2018 | Real-world Cohort | J Gastroenterol Hepatol | Real-world effectiveness and safety of PrOD in Taiwan HCV GT1b patients; confirms high SVR rates in East Asian population with HCV; no HBV data |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver Int | Discusses pathways toward HCV eradication and HBV cure; highlights mechanistic distinctions between HCV DAAs and HBV antivirals and the separate drug development requirements |
| [36515288](https://pubmed.ncbi.nlm.nih.gov/36515288/) | 2022 | Epidemiology | Voprosy Virusologii | HBV, HCV, and HDV prevalence and molecular genetic characterization in HIV-positive patients; illustrates HBV/HCV co-infection epidemiology relevant to co-infection treatment context |
| [26043288](https://pubmed.ncbi.nlm.nih.gov/26043288/) | 2015 | Review | Rev Med Virol | Comprehensive review of HCV DAA development targeting NS3/4A, NS5A, and NS5B; explains dasabuvir's non-nucleoside NS5B inhibitor class and mechanism — highlights HCV specificity |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | In vitro/Resistance | Hepatology | HCV protease inhibitor resistance-associated substitutions across major genotypes; resistance mechanisms in HCV context, relevant to understanding dasabuvir combination partner durability |
| [26139639](https://pubmed.ncbi.nlm.nih.gov/26139639/) | 2015 | Review | Ann Pharmacother | Treatment considerations for special HCV GT1 populations (renal impairment, transplant, HIV co-infection) using dasabuvir-containing regimens; no HBV therapeutic discussion |
| [28992878](https://pubmed.ncbi.nlm.nih.gov/28992878/) | 2017 | Review | Hepatobiliary Pancreatic Dis Int | Peginterferon alfa-2a role in the DAA era for HCV; contextualizes DAA positioning including dasabuvir regimens in markets with access constraints |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dasabuvir's mechanism of action — inhibiting the HCV NS5B thumb II allosteric pocket — has **no structural equivalent in HBV**, which replicates through a reverse transcriptase pathway that existing nucleoside/nucleotide analogues (tenofovir, entecavir) already address effectively. The TxGNN score of 99.37% reflects graph-based disease proximity between viral hepatitides, not mechanistically supported repurposing potential. With zero relevant clinical trials, no direct literature evidence, no Saudi Arabia market presence, and missing safety data, this candidate does not meet the threshold for further development investment at this time.

**To proceed, the following is needed:**

- **Preclinical mechanistic assessment**: In vitro evaluation of dasabuvir against HBV DNA polymerase/RT activity, and computational docking analysis of the dasabuvir binding pose against HBV RT crystal structures
- **MOA documentation**: Full DrugBank API retrieval for NS5B binding characterization, selectivity profile, and any reported cross-reactivity data against other viral polymerases
- **Safety profile**: Obtain full package insert warnings and contraindications (SFDA/EMA/FDA label) to complete S1 safety screening — currently blocking formal safety evaluation
- **Mechanistic reconsideration**: Given the structural mismatch between HCV NS5B and HBV RT, a formal mechanistic review should determine whether any indirect antiviral pathway (e.g., host immune modulation observed post-SVR) could justify continued investigation, or whether resources should be redirected to better-supported HBV repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

