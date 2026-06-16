---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is a second-generation HIV-1 protease inhibitor approved for treating HIV-1 infection in adults and pediatric patients.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **0 clinical trials** and **4 non-human primate studies** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Darunavir is a second-generation HIV-1 protease inhibitor that binds tightly to the active site of the HIV-1 protease enzyme, preventing cleavage of viral polyprotein precursors and blocking the production of mature, infectious virions. Its exceptionally high genetic barrier to resistance — compared with first-generation agents such as lopinavir — and broad activity against wild-type and multi-drug-resistant HIV-1 strains have made it a backbone of modern combination antiretroviral therapy (cART).

The mechanistic case for activity against SIV rests on structural homology: SIV and HIV-1 are both primate lentiviruses, and their protease enzymes share approximately 85–90% amino acid sequence identity. Consistent with this, all four supporting publications used Darunavir as a component of intensified cART regimens in SIVmac239- or SIVmac251-infected rhesus macaques, demonstrating clinically relevant viral suppression and enabling study of latent reservoir dynamics — the same scientific problems driving HIV cure research in humans.

However, the residual 10–15% amino acid divergence between SIV and HIV-1 proteases means that binding affinity cannot be assumed equivalent without dedicated enzyme assays. More importantly, SIV infection is a non-human primate pathogen with no direct human clinical counterpart: this TxGNN prediction reflects Darunavir's validated utility in preclinical animal models rather than a conventional repurposing opportunity targeting a new human disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darunavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | NHP Experiment | AIDS Res Hum Retroviruses | Evaluated two novel coformulated cART regimens including darunavir in SIVmac239-infected rhesus macaques; both regimens achieved sustained, clinically relevant viral suppression suitable for reservoir studies |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | NHP Experiment | PLoS Pathogens | Highly intensified multi-drug ART (including darunavir) suppressed SIVmac251 viremia across a broad viral load range (10³–10⁷ copies/mL) and significantly restricted the measurable viral reservoir in rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | NHP Experiment | PLoS One | cART (including darunavir) combined with the HDAC inhibitor SAHA in SIV-infected Chinese-origin rhesus macaques; examined reservoir persistence and the "shock-and-kill" latency reversal concept |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | NHP Experiment | AIDS (London) | Auranofin co-administered with cART (including darunavir) in an SIV monkey model; demonstrated restriction of lentiviral reservoir cells and containment of viral load following ART suspension |

> **Note:** All four studies are Tier 3 non-human primate experiments. No randomized controlled trials or observational human studies were identified for this indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire evidence base for this prediction consists of non-human primate animal model studies (L4), and SIV infection is by definition a primate pathogen with no direct human clinical target — the prediction captures Darunavir's established role as a cART component in preclinical HIV research, rather than identifying a novel clinical repurposing opportunity. The remaining three TxGNN predictions further support a conservative posture: feline AIDS (L5) is mechanistically unsupported given FIV protease divergence; the neurodevelopmental disorder (L5) has no biological rationale linking HIV protease inhibition to neurodevelopment; and familial combined hyperlipidemia (L5) is a **pharmacological reversal signal** — Darunavir/ritonavir is a known inducer of hypertriglyceridemia and elevated LDL-C, making this a documented adverse effect rather than a therapeutic target.

> ⚠️ **Data Pipeline Note:** The clinical trial NCT02770508 retrieved for the "feline AIDS" indication is a Phase 4 human HIV-1 study with no feline disease relevance (Grade C mapping error). This reflects a false-positive retrieval in the evidence pipeline and should be corrected upstream.

**To proceed, the following is needed:**

- Formal in vitro enzyme-binding assays confirming Darunavir activity against SIV protease specifically (to resolve the 10–15% sequence divergence uncertainty)
- Clarification of the intended clinical context: if the goal is optimizing NHP model fidelity for HIV cure research, this evidence supports continued use; if pursuing a de novo human clinical indication, redirect effort to higher-evidence human disease associations
- Full MOA and safety profile data (currently unavailable in this dataset) to enable S1 safety screening
- Package insert review to complete contraindication and warning assessment (DG001 gap, currently blocking S1 entry)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

