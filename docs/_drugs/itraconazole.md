---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal agent, pharmacologically used to treat systemic fungal infections (specific approved-indication text is not available in this evidence pack, and the drug is not currently marketed in Saudi Arabia). The TxGNN model predicts a possible association with **Pneumocystosis**, but the underlying evidence base is thin — **0 clinical trials** and **20 publications**, none of which directly test itraconazole against Pneumocystis jirovecii/carinii — and the drug's own mechanism argues against efficacy in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic fungal infections (antifungal agent class; specific indication text not available in evidence pack — no Saudi license records exist) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Itraconazole is an azole-class antifungal. Its mechanism of action, as captured in the repurposing rationale, is inhibition of lanosterol 14α-demethylase, which blocks ergosterol biosynthesis in the fungal cell membrane. This mechanism underlies its efficacy against organisms such as Aspergillus, Candida, and Histoplasma species.

Pneumocystis jirovecii (the causative organism of pneumocystosis), however, has an atypical cell membrane that contains cholesterol rather than ergosterol, and it lacks the azole drug target altogether. This is consistent with well-established clinical practice: azoles, including itraconazole, are not first-line or standard therapy for Pneumocystis pneumonia — that role belongs to trimethoprim-sulfamethoxazole (TMP-SMX).

Given this mechanistic mismatch, the high TxGNN score most likely reflects the model picking up a semantic/network proximity between itraconazole and Pneumocystis within a broader "immunocompromised host / opportunistic infection" cluster (both concepts co-occur heavily in HIV, transplant, and immunodeficiency literature), rather than a genuine pharmacological link. This prediction should be treated as a probable false positive rather than a credible repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled Phase III trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients; not specific to Pneumocystis. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Summarizes therapy/prophylaxis for Pneumocystis carinii, Toxoplasma, Leishmania and trypanosome infections, covering mechanism, dosing and efficacy of each agent class. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Overview of primary/secondary prophylaxis for HIV-related opportunistic infections; notes OIs occur in up to 40% of patients with CD4 <250/mm³. |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Reviews prophylaxis and treatment strategies for infections, including fungal, in bone marrow transplant recipients. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Discusses infection (bacterial, fungal, viral) as a leading cause of morbidity/mortality after lung transplantation. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK) | Clinical Pharmacokinetics | Reviews penetration of antifungal, antitubercular and other anti-infective agents into pulmonary epithelial lining fluid. |
| [11362422](https://pubmed.ncbi.nlm.nih.gov/11362422/) | 1995 | Review | PI Perspective | General review on strategies for preventing opportunistic infections. |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort (retrospective) | Transplantation Proceedings | Single-center study of invasive fungal infections after kidney transplantation, associated with increased mortality and graft dysfunction. |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian Journal of Medical Microbiology | Compares respiratory fungal pathogen profile and susceptibility between immunocompetent and immunocompromised hosts, correlated with CD4+ T-cell counts. |
| [17594870](https://pubmed.ncbi.nlm.nih.gov/17594870/) | 2007 | Cohort | Allergologia et Immunopathologia | 25-year experience of chronic granulomatous disease in pediatric patients, including associated fungal infection risk. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association conflicts with itraconazole's known mechanism of action — Pneumocystis lacks the ergosterol-based drug target azoles require — and no clinical trials or itraconazole-specific literature support use in pneumocystosis. The high TxGNN score is best explained by semantic clustering around "immunocompromised host / opportunistic infection" rather than a true mechanistic signal.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently a Blocking data gap)
- Confirmed original indication text and MOA sourced directly from a regulatory or DrugBank record (currently a High-severity data gap)
- A pharmacology review specifically addressing whether any azole has plausible activity against Pneumocystis before this candidate is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

