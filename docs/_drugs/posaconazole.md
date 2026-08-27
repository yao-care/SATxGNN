---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

> Posaconazole is a triazole antifungal, generally known for the prophylaxis and treatment of invasive fungal infections in high-risk patients; it is not currently marketed in Saudi Arabia, so no official approved-indication text is available in this evidence pack.
> The TxGNN model predicts it may be effective for **Pneumocystosis (PCP)**,
> but this is currently supported by only **2 clinical trials** (neither of which directly studied posaconazole) and **5 publications** (none of which directly assess posaconazole for PCP).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in Saudi Arabia regulatory data (drug not marketed); generally known as prophylaxis/treatment of invasive fungal infections (triazole antifungal class) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Posaconazole is part of the triazole antifungal class, its efficacy in invasive fungal infection prophylaxis has been proven, and mechanistically may be applicable to pneumocystosis.

Posaconazole inhibits fungal CYP51 (lanosterol 14-α-demethylase), blocking ergosterol synthesis in the fungal cell membrane. It is clinically used for prophylaxis of invasive Aspergillus and Candida infections in high-risk populations such as allogeneic hematopoietic stem cell transplant (allo-HCT) and graft-versus-host disease (GVHD) patients.

However, the mechanistic link to pneumocystosis is weak. *Pneumocystis jirovecii* has a membrane/cell wall biology distinct from typical fungi, and its sensitivity to triazole agents is not well-established or consistent in the literature. Standard treatment for PCP remains trimethoprim-sulfamethoxazole (TMP-SMX); triazole antifungals are not a recognized treatment or prophylaxis option for PCP. The connection here likely reflects an indirect association — both indications fall under "antifungal prophylaxis in immunocompromised transplant patients" — rather than a target-specific mechanism against *Pneumocystis*.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Evaluates **Rezafungin** (an echinocandin, not posaconazole) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic HCT recipients. Relevance graded **C** — different study drug, no direct link to posaconazole or pneumocystosis. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens post-transplant; posaconazole may appear only as background standard-of-care antifungal prophylaxis, not as a PCP-directed intervention. Relevance graded **B**, no results yet available. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet Infectious Diseases | UK best-practice update on diagnosis of serious fungal diseases (diagnostics-focused; not a posaconazole-PCP efficacy study). |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and PCP; notes mould-active posaconazole prophylaxis reduces invasive candidiasis in high-risk hemato-oncology patients, but does not establish posaconazole efficacy against *Pneumocystis*. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | Clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease; general guideline, not posaconazole/PCP-specific. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | PK/Review | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal/antimicrobial agents; pharmacokinetic background only, no PCP efficacy data. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications in acute GVHD after liver transplant; infection-management context only, not a posaconazole-PCP study. |

*Note: relevance classification for all 5 publications is marked "pending" in the source data — none has been confirmed as directly evaluating posaconazole for pneumocystosis.*

---

## Saudi Arabia Market Information

Posaconazole is not currently marketed in Saudi Arabia (0 authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at the mechanism/preclinical level only (L4) — no clinical trial or publication directly evaluates posaconazole for pneumocystosis, and the proposed mechanistic link is indirect (shared antifungal-prophylaxis context rather than target-specific activity against *P. jirovecii*). A blocking data gap (missing TFDA/SFDA package insert) also prevents entry into the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — required to clear the S1 safety gate
- DrugBank-sourced mechanism of action (MOA) detail
- Confirmed original indication and regulatory status (drug is currently unmarketed in Saudi Arabia)
- Direct clinical or in vitro evidence of posaconazole activity against *Pneumocystis jirovecii*, beyond its role as background antifungal prophylaxis in transplant settings
- Drug-drug interaction (DDI) data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

