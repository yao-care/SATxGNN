---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 5
---

# Lamivudine
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

# Lamivudine: From HIV-1/Hepatitis B Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor historically used for HIV-1 infection and chronic hepatitis B.
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) infection**, but this is a macaque-model research entity used to study HIV pathogenesis, not a human disease — so despite a **99.93% prediction score** and **20 supporting publications**, it is not a viable human repurposing target.
> All five predicted indications in this evidence pack carry significant data-quality problems (species mismatch, obsolete disease terms, or disease-label errors), so none currently support a Go decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection / Chronic Hepatitis B (commonly known use; not captured in the Saudi Arabia regulatory data — see Safety section) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on generally known pharmacology, lamivudine is a nucleoside reverse transcriptase inhibitor (NRTI) that has proven efficacy against retroviruses (HIV-1) and hepadnaviruses (HBV) by terminating viral DNA chain synthesis.

The model's association between lamivudine and "SIV infection" is mechanistically genuine but clinically misdirected. SIV is a lentivirus closely related to HIV, and its reverse transcriptase is structurally similar enough that lamivudine is active against it — this is confirmed by the literature evidence below, which repeatedly documents the M184V resistance mutation, the same mutation that defines lamivudine resistance in human HIV-1 patients. This shows the model correctly captured a real pharmacological relationship.

However, "SIV infection" is not a human disease entity — it is the standard macaque animal model used to study HIV/AIDS pathogenesis and antiretroviral prophylaxis in primate research. There is no human population with SIV infection to repurpose a drug for, so this candidate cannot proceed to a clinical repurposing pathway despite the strong evidence base. It should be treated as a data-ontology artifact of the prediction pipeline rather than a genuine indication candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Cohort | Journal of Virology | M184V resistance mutation emerges in SIV reverse transcriptase under lamivudine/emtricitabine therapy, reducing viral fitness — mirrors the clinical resistance pathway seen in human HIV-1 |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | Cohort | Journal of Virology | M184V reversion is selected by tenofovir even when lamivudine is co-administered, in the SIV macaque model |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Cohort | AIDS | Post-exposure prophylaxis with zidovudine + lamivudine + indinavir prevented vaginal SIV transmission in macaques |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Cohort | Journal of Virology | Quadruple antiretroviral therapy including lamivudine produced rapid viral decay in SIV-infected macaques |
| [9237655](https://pubmed.ncbi.nlm.nih.gov/9237655/) | 1997 | Review | FEBS Letters | Reviews nucleoside analogue derivatives with activity against HIV, HBV and SIV, contextualizing lamivudine's antiviral class |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Cohort (pending classification) | Journal of Virology | HAART regimen with subcutaneous lamivudine suppressed viral load in RT-SHIV-infected rhesus macaques |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Cohort (pending classification) | Journal of Virology | Early post-exposure lamivudine-containing HAART altered lymphocyte proliferation kinetics during primary SIV infection |
| [12163615](https://pubmed.ncbi.nlm.nih.gov/12163615/) | 2002 | Cohort (pending classification) | Journal of Virology | M184V mutation (lamivudine resistance marker) delays reversion of attenuated SIV variants |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Cohort (pending classification) | Journal of Virology | HAART including lamivudine reduced SHIV viremia but bone marrow hematopoietic defects persisted in macaques |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Cohort (pending classification) | Retrovirology | Timing of short-term HAART initiation affects SIV tissue viral load and reservoir seeding in macaques |

---

## Saudi Arabia Market Information

Lamivudine is not currently marketed in Saudi Arabia; no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: DG001 (TFDA/local package insert warnings and contraindications) is flagged as a **Blocking** data gap, meaning no safety pre-assessment (S1) can currently be completed for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate, SIV infection, is a primate research model rather than a human disease, so it cannot be advanced as a repurposing indication regardless of its strong mechanistic and literature support.
- The remaining four TxGNN-ranked candidates in this pack (feline AIDS, a rare neurodevelopmental disorder, an obsolete hyperlipidemia term, and hepatitis C) each carry disqualifying data issues on inspection — the feline-AIDS and hepatitis-C evidence sets are actually mismatched human HIV/hepatitis-B trials, and the other two have no supporting evidence at all. None currently support a Go or Guardrails decision.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action documentation (DG002)
- A corrected disease-ontology mapping run so genuine human-disease candidates (rather than animal models or mislabeled entities) can be evaluated for this drug
- If a genuine human indication emerges from re-mapping, dedicated clinical trial and literature searches specific to that indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

