---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 4
---

# Acitretin
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

# Acitretin: From Psoriasis to Acne (Disease)

## One-Sentence Summary

Acitretin is a second-generation aromatic synthetic retinoid, globally established for the treatment of severe psoriasis and keratotic skin disorders, though it currently holds no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Acne (Disease)**,
with **no directly relevant clinical trials** and **18 publications** (predominantly reviews, observational data, and case reports on acitretin and retinoids in acne-related conditions) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis / Keratotic skin disorders (established global indication; no Taiwan registration) |
| Predicted New Indication | Acne (Disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from regulatory databases is not available in this evidence pack. Based on established pharmacological knowledge, acitretin is the active metabolite of etretinate and belongs to the second-generation aromatic retinoids. It exerts its effects by binding to nuclear retinoid receptors (RARα/β/γ), which triggers transcriptional changes that normalize follicular keratinization, suppress excessive sebaceous gland secretion, and inhibit inflammatory mediator release — including leukotriene LTC4 from eosinophils. These three mechanisms directly address the core pathophysiology of acne: sebaceous hyperactivity, follicular plugging, and chronic inflammation.

The strongest evidence for this repurposing direction lies in acne inversa (hidradenitis suppurativa, HS) — a severe, recurrent inflammatory follicular disease considered mechanistically related to nodulocystic acne. Acitretin is explicitly named in the European S1 clinical guideline for HS, and long-term observational data (up to 25 years) documents its efficacy in this population. Direct evidence for conventional acne vulgaris is limited to case reports where acitretin was used after isotretinoin showed only partial response.

It is important to note that isotretinoin (a first-generation retinoid) remains the established standard of care for severe conventional acne. Acitretin shares the nuclear receptor pathway but is better validated for HS and other keratotic disorders. Its potential role in acne therapy is therefore positioned as a second-line alternative in special clinical circumstances — particularly for acne inversa — and must be accompanied by rigorous teratogenicity management (Pregnancy Category X; mandatory contraception for ≥3 years post-cessation due to potential reconversion to the long-acting etretinate in the presence of alcohol).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study examining whether nasal mucosal dryness from oral retinoids increases COVID-19 infection risk in acne patients. Primary subject is isotretinoin, not acitretin; provides indirect class-level safety context only and does not constitute direct evidence for acitretin in acne treatment. |

> **Note:** No clinical trials directly evaluating acitretin for the treatment of acne (disease) were identified in ClinicalTrials.gov or ICTRP searches.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Clinical Guideline (European S1) | J Eur Acad Dermatol Venereol | European S1 guideline for hidradenitis suppurativa/acne inversa; formally recommends acitretin as a systemic treatment option for this severe follicular acne-related condition |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Observational Study | Br J Dermatol | 25-year long-term results of acitretin therapy for hidradenitis suppurativa; demonstrates sustained clinical benefit in a condition closely related to nodulocystic acne |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Comprehensive overview of retinoid use across 15 years; covers acitretin's role in severe acne and acne-related dermatoses, alongside psoriasis and keratotic genodermatoses |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Current overview of vitamin A and retinoids in dermatology; positions oral retinoids including acitretin within contemporary acne treatment frameworks |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Hautarzt | Drug therapy of acne inversa; discusses acitretin within the systemic treatment algorithm alongside antibiotics and biologics |
| [26617362](https://pubmed.ncbi.nlm.nih.gov/26617362/) | 2016 | Review | Dermatol Clin | Medical treatments for hidradenitis suppurativa; acknowledges low evidence levels but documents promising results for acitretin pending RCT validation |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | PK/Efficacy Review | Clin Pharmacokinet | Pharmacokinetics and efficacy of retinoids including acitretin; confirms second-generation retinoid profile and primary indication in keratotic disorders with implications for acne |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Mechanistic Study | Dermatology | Examines retinoid inhibition of sebaceous gland activity as the mechanistic basis for anti-acne efficacy; explores whether acitretin can replicate isotretinoin's effect on sebaceous suppression |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Mechanistic Study | Prostaglandins | Acitretin inhibits eosinophil LTC4 release; supports the anti-inflammatory mechanism underlying its efficacy in acne and psoriasis |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case Report | Cutis | Direct case report: patient with severe nodulocystic facial acne and hidradenitis suppurativa treated with acitretin after two courses of isotretinoin showed only partial response; acitretin resolved persistent draining cysts |

---

## Saudi Arabia Market Information

Acitretin currently holds **no marketing authorizations** in Taiwan. No license records, approved dosage forms, or registered indications are on file.

---

## Safety Considerations

Please refer to the package insert for complete safety information, as formal warning and contraindication data was not available in this evidence pack.

**Critical class-level risk (pharmacological basis):**
Acitretin is an **absolute teratogen (Pregnancy Category X)**. Unlike isotretinoin (contraception required for 1 month post-cessation), acitretin can be re-esterified to the long-acting etretinate in the presence of alcohol, extending the teratogenic risk period to **≥3 years after treatment cessation**. This is the defining safety constraint for any acitretin repurposing program and must be reflected in all prescribing guardrails and patient selection criteria.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acitretin's nuclear retinoid receptor mechanism directly targets the pathophysiological drivers of acne, and its efficacy in the closely related acne inversa (HS) is supported by a European S1 clinical guideline and long-term observational data. However, direct RCT evidence for conventional acne vulgaris is absent, and the teratogenicity profile demands strict prescribing controls.

**To proceed, the following is needed:**

- **Indication scoping**: Clarify whether the target is acne inversa/HS (where L3 evidence and guideline support already exists) or conventional acne vulgaris (where only indirect and mechanistic data is available)
- **MOA documentation**: Retrieve complete pharmacological profile from DrugBank (DB00459) and package inserts
- **Safety data retrieval**: Download and parse package insert PDF from TFDA for formal warnings, contraindications, and DDI data (currently Blocking data gap)
- **Teratogenicity management protocol**: Develop a pregnancy prevention program (PPP) analogous to iPLEDGE (isotretinoin) or Pregnancy Prevention Programme (acitretin, EU), including alcohol abstinence counseling and extended contraception requirements
- **Market registration assessment**: Evaluate feasibility of Taiwan NDA submission given zero current authorizations and the need for a full teratogenicity risk management strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

