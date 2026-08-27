---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
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

# Tenofovir Disoproxil: From HIV-1/Chronic Hepatitis B Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor prodrug whose evidence pack does not contain confirmed original-indication or mechanism-of-action data.
The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, an animal-model lentiviral disease, supported by only **2 clinical trials (both graded low relevance/noise)** and **20 publications (almost entirely animal studies in macaques)**.
Because the predicted "new indication" is not a human disease, this candidate does **not** represent an actionable drug-repurposing opportunity in its current form.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` empty) — see note below |
| Predicted New Indication | Simian Immunodeficiency Virus Infection (animal-model disease, not a human indication) |
| TxGNN Prediction Score | 99.95% (global rank 1239) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on established pharmacological knowledge outside this evidence pack, tenofovir disoproxil is a prodrug of tenofovir, a nucleotide reverse transcriptase inhibitor (NRTI) used against HIV-1 and chronic hepatitis B — this classification is **not sourced from the evidence pack itself** and should be independently confirmed once the MOA data gap (DG002) is resolved.

Mechanistically, the prediction is explainable: SIV is a lentivirus closely related to HIV, and reverse transcriptase structure is highly conserved across the lentivirus family, so tenofovir's antiretroviral activity plausibly extends to SIV — this is well documented in decades of macaque pre-exposure-prophylaxis (PrEP) research (see literature below).

However, this mechanistic plausibility does **not** constitute a novel repurposing hypothesis. SIV infects macaques, not humans; it is a laboratory/veterinary disease ontology term, not a condition tenofovir could be prescribed for in a human patient. The evidence collected essentially re-confirms tenofovir's known antiretroviral mechanism in an animal PrEP model rather than identifying a new human therapeutic use. The two associated clinical trials are both graded "C" (low relevance/noise — one tests raltegravir, not tenofovir; the other tests vedolizumab in human HIV, unrelated to SIV) and were matched on string similarity alone. The remaining three ranked predictions (feline AIDS, a rare neurodevelopmental disorder, and an obsolete hyperlipidemia term) are similarly not viable human indications — see Conclusion below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | HIV/SIV viral decay kinetics study using raltegravir, not tenofovir; withdrawn with zero enrollment. Graded low relevance (noise match). |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + antiretroviral therapy in human HIV-infected subjects; does not involve tenofovir or SIV specifically. Graded low relevance (noise match). |

Neither trial provides direct evidence for tenofovir in SIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT (human) | Pharmacotherapy | Review/evaluation of systemic HIV pre-exposure prophylaxis strategies |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Observational (African green monkeys) | Journal of Virology | SIVagm dynamics and antiretroviral (tenofovir + emtricitabine) effect in natural-host monkeys |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal Study (infant macaques) | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 protect infant macaques against repeated oral SIV challenge |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal Study (macaques) | J Infect Dis | TDF chemoprophylaxis provides partial protection against SHIV in macaques with multiple viral challenges |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Animal Study (macaques) | J Virol | Tenofovir vaginal gel provides durable protection against vaginal SHIV infection in macaques |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal Study (macaques) | J Infect Dis | Oral FTC/TDF prevents transmission of tenofovir-resistant (K65R) SHIV in macaques |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Study (macaques) | J Infect Dis | Oral FTC/tenofovir alafenamide protects macaques from rectal SHIV infection |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal Study (macaques) | J Infect Dis | FTC/TDF prevents vaginal SHIV infection in macaques co-infected with Chlamydia/Trichomonas |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Animal Study (macaques) | JCI Insight | Hypo-osmolar rectal douche tenofovir formulation prevents SHIV acquisition in macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal Study (macaques) | J Infect Dis | Tenofovir alafenamide/elvitegravir vaginal inserts give extended post-exposure protection against SHIV in macaques |

All literature evidence is preclinical/animal-model in nature; there is no human clinical evidence for tenofovir in SIV infection (which by definition cannot occur in humans). An additional 10 literature records in the evidence pack were unclassified ("pending") and are not included above.

---

## Saudi Arabia Market Information

Tenofovir disoproxil currently has no marketing authorization on record in Saudi Arabia (`total_licenses: 0`, `market_status: 未上市/Not Marketed`); no license entries are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the four TxGNN-predicted indications for this candidate is currently actionable. The top-ranked prediction, SIV infection, is a macaque-only lentiviral disease rather than a human indication — the supporting evidence, though mechanistically coherent, only reconfirms tenofovir's known antiretroviral activity in animal PrEP models. The remaining ranked predictions are similarly non-viable: feline AIDS is a veterinary disease with no supporting literature, the neurodevelopmental disorder shows no mechanistic link and is likely an embedding-similarity artifact, and the hyperlipidemia term is flagged obsolete in its source ontology. In addition, drug-level data (original indications, MOA, Taiwan/Saudi regulatory status, safety warnings) are all missing from this evidence pack, blocking any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — this is a **Blocking** data gap (DG001) that must be resolved before any S1 safety review
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Confirmed original indication(s) and regulatory status for tenofovir disoproxil
- Re-run of the TxGNN prediction excluding non-human disease ontology terms, to surface genuinely translatable human indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

