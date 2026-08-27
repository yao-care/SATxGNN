---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 1
---

# Micafungin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Micafungin: From Invasive Fungal Infection to Candida Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin antifungal, established for treating invasive Candida infections such as candidemia and esophageal candidiasis.
The TxGNN model predicts it may be effective for **Candida Urinary Tract Infection (Candiduria)**,
with **no registered clinical trials** but **13 supporting publications** — largely case reports, case series, and retrospective cohorts — currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infection (candidiasis) — general antifungal indication known from drug class; no Saudi Arabia-specific approved indication text available (not marketed) |
| Predicted New Indication | Urinary Tract Infection — specifically *Candida* spp. urinary tract infection (candiduria), not bacterial UTI |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. However, the evidence pack's own repurposing rationale identifies micafungin's pharmacological class clearly: it is an **echinocandin** antifungal that inhibits fungal cell-wall **1,3-β-D-glucan synthase**, an enzyme essential to *Candida* and other fungal pathogens but absent in human cells.

This predicted "new indication" is narrower than a typical repurposing case. TxGNN's "urinary tract infection" label, when read against the supporting literature, refers specifically to UTIs caused by *Candida* species (including *C. glabrata*, *C. krusei*, and *C. auris*) rather than bacterial UTI. Because micafungin's fungicidal spectrum already covers these organisms in bloodstream and systemic infections, extending its use to the urinary tract is a mechanistically direct application of existing antifungal activity rather than a novel biological hypothesis.

The main historical objection to echinocandins for UTI has been their high protein binding and low urinary excretion. Multiple studies in the evidence set (e.g., PMID 27424599) directly address this concern, showing that measured urinary micafungin concentrations are sufficient to achieve fungicidal effect and can be optimized with therapeutic drug monitoring — partially resolving the traditional pharmacokinetic doubt.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | PK Study | Int J Antimicrob Agents | 6 UTI cases successfully treated with micafungin; urinary drug levels sufficient for fungicidal effect despite low excretion, TDM proposed to optimize dosing |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int Urol Nephrol | Evaluated candiduria eradication rates in hospitalized patients treated with micafungin |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Retrospective Cohort (multi-institutional) | Antimicrob Agents Chemother | 305 hospitalized patients; characterized candiduria management patterns and antifungal overtreatment of asymptomatic cases |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Case Series (pediatric) | Pediatr Int | PICU children with hospital-acquired Candida UTI treated with micafungin; treatment success rates reported by species |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Med Mycol Case Rep | 5 candiduria cases treated with parenteral micafungin ≥6 days; fungal clearance achieved within 30 days |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Epidemiological/Susceptibility Survey | Ther Adv Infect Dis | *Candida* species distribution and antifungal susceptibility in vulvovaginal candidiasis and UTI, Vietnam 2023 |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infect Dis | Chronic symptomatic *C. krusei* UTI eradicated with increased-dose micafungin in a liver/kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Front Pediatr | Micafungin used to treat *C. glabrata* urinary infection in a premature neonate |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | *C. auris* UTI in a nursing home patient with multiple comorbidities |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Med Mycol Case Rep | Unilateral renal fungus ball caused by *C. glabrata*, treated with antifungal therapy plus endoscopic extraction |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and specific (echinocandin activity against *Candida* extended to the urinary tract), and it is supported by consistent case reports, case series, and two retrospective cohorts spanning multiple *Candida* species — including resistant ones such as *C. krusei* and *C. auris*. However, there are no controlled clinical trials, and micafungin is not currently marketed in Saudi Arabia, so this indication cannot yet be recommended without further safety and regulatory groundwork.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently a **Blocking** gap preventing initial safety (S1) evaluation
- Confirmed mechanism-of-action documentation from DrugBank (High-severity gap)
- Drug-drug interaction data (current DDI query returned no results)
- Prospective or controlled studies specifically evaluating micafungin for candiduria, to move beyond case-level (L3) evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

