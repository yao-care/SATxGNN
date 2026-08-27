---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 6
---

# Zidovudine
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

# Zidovudine: From HIV/AIDS Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Zidovudine (AZT, DB00495) was the first antiretroviral approved for human HIV/AIDS infection, acting as a nucleoside reverse transcriptase inhibitor (NRTI). The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome** (FIV/FAIDS in cats) with a 99.96% score, but this is supported only by **0 clinical trials** and **20 veterinary/preclinical publications** — there is currently no human clinical evidence behind this specific top-ranked prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS infection (established use; no formal license record available in this evidence pack — see data gaps below) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV/FAIDS) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for zidovudine is flagged as a data gap in this evidence pack (DG002). Based on generally established pharmacology, zidovudine is a thymidine-analogue NRTI: after intracellular phosphorylation to its triphosphate form, it competitively inhibits viral reverse transcriptase and causes chain termination during proviral DNA synthesis, which is the basis of its efficacy against HIV.

The rationale linking zidovudine to feline acquired immunodeficiency syndrome is mechanistic homology rather than clinical translation: Feline Immunodeficiency Virus (FIV) belongs to the same *Lentivirus* genus as HIV and causes an immunodeficiency syndrome in cats that closely parallels human AIDS. Because FIV reverse transcriptase is structurally similar to HIV-1 reverse transcriptase, zidovudine shows in vitro and in vivo antiviral activity in cats, and FIV/FeLV-infected cats have long served as a veterinary/preclinical animal model for testing HIV antiretroviral strategies.

However, this is an **animal disease model, not a human indication**. All supporting evidence (20 publications, 0 clinical trials) is veterinary or preclinical (in vitro, SCID-feline mice, naturally/experimentally infected cats). It has no direct bearing on a novel human drug-repurposing opportunity, which is why the evidence level is capped at L4 (preclinical/mechanistic) and the underlying TxGNN scoring already recommends "Hold." Notably, two lower-ranked predictions in this pack — AIDS-related complex and congenital HIV infection — do have strong human clinical trial support (L1/S3, "Proceed with Guardrails"), but both are essentially restatements of zidovudine's already-approved original indication rather than novel repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | In vitro/Animal model | Antimicrobial Agents and Chemotherapy | Established FIV as a reverse-transcriptase-targeted chemotherapy model for AIDS |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Observational (feline) | Archives of Virology | Zidovudine lowered plasma (but not PBMC) FIV titer in experimentally infected cats |
| [7618256](https://pubmed.ncbi.nlm.nih.gov/7618256/) | 1995 | Animal model (SCID-feline mice) | Veterinary Immunology and Immunopathology | AZT reduced provirus burden and enhanced humoral immunity against FIV |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Animal RCT (FeLV, veterinary) | Antimicrobial Agents and Chemotherapy | IFN-alpha plus AZT evaluated in presymptomatic FeLV-induced immunodeficiency (FAIDS) |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | Animal prophylaxis study | Journal of Acquired Immune Deficiency Syndromes | AZT + IFN-alpha + IL-2 as prophylactic therapy for FeLV-FAIDS |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Animal cohort | Journal of Acquired Immune Deficiency Syndromes | Prophylactic AZT prevented early viremia/lymphocyte decline in FIV-inoculated cats |
| [8399067](https://pubmed.ncbi.nlm.nih.gov/8399067/) | 1993 | Animal model | Journal of Immunotherapy | Adoptive lymphocyte transfer + IFN-alpha + zidovudine reversed FeLV infection |
| [3034403](https://pubmed.ncbi.nlm.nih.gov/3034403/) | 1987 | Animal model | Cancer Research | Early AZT evaluation in FeLV-infected cats as a therapy/prophylaxis model for AIDS |
| [18550661](https://pubmed.ncbi.nlm.nih.gov/18550661/) | 2008 | Phylogenetic/genetic analysis | Journal of Virology | Genetic analysis of FIV in cats undergoing zidovudine (AZT) treatment vs. treatment-naïve |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | In vitro/in vivo study | Veterinary Immunology and Immunopathology | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in PBMCs |

---

## Market Information

Zidovudine currently has **0 registered authorizations** and is **not marketed** in the target jurisdiction per this evidence pack, so no license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as unresolved data gaps in this evidence pack — notably, TFDA package-insert warnings/contraindications are flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from entering initial safety (S1) evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (feline acquired immunodeficiency syndrome) is a veterinary disease with only preclinical/animal evidence and no human clinical trials, so it offers no actionable human repurposing pathway despite its high model score. The candidate's other high-scoring predictions are either mechanistically implausible/likely model noise (a rare genetic neurodevelopmental disorder; an obsolete hyperlipidemia term with an inverted mechanism) or, for the two indications with strong clinical evidence (AIDS-related complex, congenital HIV), simply restate zidovudine's existing approved indication rather than a novel use. Combined with a Blocking data gap on TFDA safety labeling and zero market presence, this candidate is not ready to advance.

**To proceed, the following is needed:**
- TFDA/official package insert warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- A genuinely novel, human-relevant predicted indication with supporting clinical evidence, since the current top-ranked candidate is not clinically actionable
- Clarification of local market/licensing status if repurposing within this jurisdiction is still being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

