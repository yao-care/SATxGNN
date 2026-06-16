---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

The txgnn-pipeline skill confirms this is within the TxGNN drug repurposing domain. The report format is defined in the system prompt. Generating the report now:

---

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI) approved for treating HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection** — the primate analogue of HIV used in AIDS research animal models —
with **1 clinical trial** and **16 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (integrase strand transfer inhibitor; reference indication — not registered in Saudi Arabia) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current data pack. Based on known pharmacological class information, Dolutegravir is an integrase strand transfer inhibitor (INSTI) that blocks the HIV integrase enzyme from inserting viral cDNA into the host cell genome — a step essential for viral replication. This mechanism is highly targeted and structurally defined, making its cross-species applicability a meaningful scientific question.

SIV integrase shares the same Mg²⁺-dependent DDE catalytic motif as HIV integrase, with high structural homology at the active site. This means DTG's mechanism can, in principle, act directly on SIV integrase. Published literature has confirmed that SIVmac239 and related strains are susceptible to INSTIs including DTG, that drug resistance mutation pathways parallel those seen in HIV, and that DTG-containing antiretroviral regimens can suppress SIV replication to clinically relevant levels in rhesus macaque models. One case study documents successful DTG-based cART in a captive chimpanzee with SIVcpz-induced immunodeficiency.

The primary practical application of this prediction is not a conventional clinical repurposing scenario, but rather: (1) use of DTG in non-human primate (NHP) SIV models to study HIV cure strategies, latency, and vaccine development; or (2) veterinary management of SIV-infected primates in research or zoological settings. The scientific basis is sound, but the target disease population is non-human, which fundamentally shapes the evidence pathway and decision framework.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab combined with ART (including DTG) in HIV/SIV-infected subjects to achieve virological remission after ART interruption; primary focus is immune modulation rather than DTG efficacy per se. Extremely small sample, outcome unknown. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Animal Study (In vivo) | J Virology | DTG monotherapy in SIV-infected macaques selects multiple resistance mutation patterns; demonstrates direct antiviral activity against SIV, with variable virological outcomes depending on resistance pathway |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Case Study / Animal | Retrovirology | Successful treatment of SIVcpz-induced immunodeficiency in a captive western chimpanzee using DTG-based cART; first documented in vivo efficacy in the direct HIV-1 progenitor virus |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro / Mechanistic | J Virology | Characterisation of INSTI (including DTG) resistance profiles in SIVmac239; confirms SIV susceptibility to DTG and parallel resistance mutation phenotypes to HIV |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Review | FEBS Journal | X-ray crystal structures of HIV/SIV intasome complexes explain DTG binding to integrase and resistance mechanisms; provides structural basis for cross-species INSTI activity |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (Comparative) | AIDS Res Hum Retroviruses | Evaluated DTG-containing injectable cART regimens in SIVmac239-infected rhesus macaques; demonstrated effective SIV suppression to clinically relevant levels |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Animal Study | Pharmaceutics | Pharmacological validation of long-term DTG-inclusive ART in SIVmac251-infected NHP model; assessed PK of tenofovir, emtricitabine, and dolutegravir in macaques |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Animal Study | Front Immunology | CNS extracellular water and white matter tract changes in SIV-infected macaques before and after FTC+TDF+DTG initiation; documents neurological effects of DTG-based ART in NHP model |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Study | mBio | Lentiviral (HIV/SIV) persistence in brain reservoirs despite effective DTG-based ART; findings in NHP model and human samples support CNS as sanctuary site |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In vitro / Mechanistic | Clin Infect Dis | DTG and raltegravir exert pro-adipogenic and pro-fibrotic effects in human/simian adipose tissue; mechanistic study using simian tissue highlights metabolic safety signals relevant to NHP models |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro / Mechanistic | J Virology | HIV-1 INSTI resistance mutations introduced into SIVmac239 confirm susceptibility to DTG and characterise resistance pathways; foundational cross-species pharmacology work |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically well-grounded — SIV and HIV share highly conserved integrase architecture, and multiple animal studies confirm DTG antiviral activity against SIV in non-human primate models. However, SIV infection is a disease of non-human primates, not humans; this is fundamentally a research/veterinary application rather than a conventional clinical repurposing candidate, and the single registered clinical trial (n=12, status unknown) does not provide human efficacy data for SIV as a disease entity.

**To proceed, the following is needed:**

- **Clarification of use case**: Define whether the objective is (a) DTG use in NHP research models (preclinical HIV cure/vaccine research), (b) veterinary management of SIV-infected zoo or research primates, or (c) exploration of DTG for rare cross-species lentiviral infections in humans — each pathway requires a fundamentally different evidence and regulatory strategy
- **MOA data confirmation**: Retrieve full DrugBank mechanism of action data and structure-activity relationship details for DTG at the SIV integrase active site
- **Safety data retrieval**: Obtain package insert warnings, contraindications, and drug interaction profile (TFDA/FDA sources) to complete the safety assessment before any S1 evaluation
- **Veterinary PK data**: If the target is veterinary use, species-specific pharmacokinetics in macaques or cats (see rank 2: feline AID) are needed; the Kim 2023 FIV study (PMID 37112803) provides a starting point for domestic cat dosing
- **Regulatory pathway**: For NHP research use, confirm whether any institutional IACUC or import/export regulatory framework in Saudi Arabia or the relevant jurisdiction governs off-label antiretroviral use in research animals

> **Note on ranks 2 and 3**: The second-ranked indication — feline acquired immunodeficiency syndrome (FIV; score 99.85%) — is similarly a veterinary application with one direct PK/clinical outcomes study in DTG-treated FIV-infected cats (PMID 37112803) and should be considered alongside rank 1 if the use case expands to veterinary antiretroviral therapy. The third-ranked indication — neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (score 99.80%) — has no supporting evidence (L5) and is classified as Hold pending basic mechanistic hypothesis validation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

