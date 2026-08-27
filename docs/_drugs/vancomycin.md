---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Vancomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Vancomycin: From Gram-Positive Bacterial Infections to Streptococcal Pneumonia

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic historically used for serious Gram-positive bacterial infections (e.g., MRSA, enterococcal infections). Among the 10 candidate indications predicted by TxGNN for this drug, **Streptococcal Pneumonia** is the only one with genuine mechanistic and clinical support, backed by **3 clinical trials** and **20 publications**, including a meta-analysis of randomized controlled trials. Note that this candidate was selected over the model's top-ranked prediction (diffuse scleroderma, score 99.92%) because that and most other high-scoring predictions (paratyphoid fever, salmonellosis, typhoid fever, etc.) target Gram-negative organisms that vancomycin cannot penetrate, and are flagged in the evidence pack itself as likely knowledge-graph co-occurrence noise rather than real signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Serious Gram-positive bacterial infections (e.g., MRSA) — general pharmacological indication; no formal local approval record exists |
| Predicted New Indication | Streptococcal Pneumonia |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal structured mechanism-of-action record is not available for this drug (DrugBank MOA field is flagged as a data gap). Based on information available in this evidence pack, vancomycin is a glycopeptide antibiotic that inhibits cell wall synthesis in Gram-positive bacteria by binding the D-Ala-D-Ala terminus of peptidoglycan precursors, blocking cross-linking and ultimately causing bacterial cell lysis.

*Streptococcus pneumoniae* is a Gram-positive coccus, and vancomycin's mechanism is directly applicable to it — particularly for penicillin- or cephalosporin-resistant pneumococcal strains, or severe community-/hospital-acquired pneumonia where concurrent MRSA cannot be excluded. In these settings, vancomycin is already a recognized empirical or confirmatory treatment option in clinical practice.

This distinguishes streptococcal pneumonia from the model's other top-ranked predictions: diseases such as paratyphoid fever, salmonellosis, and typhoid fever are caused by Gram-negative organisms, whose outer membrane vancomycin cannot cross — meaning it has no intrinsic antibacterial activity against them despite high TxGNN scores. Streptococcal pneumonia is therefore best understood not as a novel repurposing hypothesis, but as a mechanistically sound, evidence-consistent indication that TxGNN correctly recovered from the knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05395520](https://clinicaltrials.gov/study/NCT05395520) | N/A | Unknown | 146 | Evaluates whether AUC-based vancomycin monitoring is appropriate beyond serious MRSA infections, given its broad Gram-positive coverage including streptococcal infections |
| [NCT04464291](https://clinicaltrials.gov/study/NCT04464291) | N/A | Completed | 500 | Epidemiological survey of circulating *S. pneumoniae* serotypes in Russia, providing disease-burden background but no vancomycin treatment arm |
| [NCT02538211](https://clinicaltrials.gov/study/NCT02538211) | N/A | Completed | 63 | Studies intestinal microbiome influence on vaccine immune response; not a direct vancomycin efficacy trial for pneumonia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211409](https://pubmed.ncbi.nlm.nih.gov/21211409/) | 2010 | Meta-analysis (RCT-based) | Chinese J Tuberculosis and Respiratory Diseases | Meta-analysis of RCTs comparing linezolid vs. vancomycin for Gram-positive pneumonia |
| [10712318](https://pubmed.ncbi.nlm.nih.gov/10712318/) | 2000 | RCT | Am J Respir Crit Care Med | Prospective randomized trial of quinupristin/dalfopristin vs. vancomycin for Gram-positive nosocomial pneumonia (n=298) |
| [26664260](https://pubmed.ncbi.nlm.nih.gov/26664260/) | 2015 | Retrospective clinical study | Int J Med Sci | No resistance detected to penicillin, cefuroxime, cefotaxime, or vancomycin in pneumococcal pneumonia inpatients |
| [36028454](https://pubmed.ncbi.nlm.nih.gov/36028454/) | 2022 | Surveillance/Cohort | Indian J Med Microbiol | Antibiotic resistance rates and penicillin MIC distribution in streptococcal pneumonia patients (2013–2019) |
| [27929242](https://pubmed.ncbi.nlm.nih.gov/27929242/) | 2016 | Review (Guideline) | American Family Physician | Community-acquired pneumonia diagnosis and management guideline |
| [27161775](https://pubmed.ncbi.nlm.nih.gov/27161775/) | 2016 | Cohort | Clin Infect Dis | Prevalence and clinical characteristics of *S. aureus* community-acquired pneumonia, informing empirical Gram-positive coverage choices |
| [9404765](https://pubmed.ncbi.nlm.nih.gov/9404765/) | 1997 | Review | Chest | Discusses penicillin dosing for pneumococcal pneumonia and concerns about vancomycin overuse |
| [16341681](https://pubmed.ncbi.nlm.nih.gov/16341681/) | 2005 | Review | Eur J Clin Microbiol Infect Dis | Antibiotic management of ventilator-associated pneumonia due to resistant Gram-positive bacteria |
| [16735146](https://pubmed.ncbi.nlm.nih.gov/16735146/) | 2006 | Review | American Journal of Medicine | Antimicrobial resistance in Gram-positive bacteria, including MRSA and VRE context for vancomycin use |
| [3630711](https://pubmed.ncbi.nlm.nih.gov/3630711/) | 1987 | Preclinical (mouse-protection model) | Acta Pathol Microbiol Immunol Scand B | In vivo/in vitro correlation of vancomycin bactericidal activity against *S. pneumoniae* |

---

## Saudi Arabia Market Information

Vancomycin currently has **0 marketing authorizations** on record and is **not marketed** in Saudi Arabia (`taiwan_regulatory.market_status = 未上市`). No product license or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data are currently available for this drug in the evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vancomycin's mechanism of action (Gram-positive cell wall synthesis inhibition) is directly applicable to *Streptococcus pneumoniae*, and this is supported by a meta-analysis of RCTs, a head-to-head randomized trial, and multiple cohort/surveillance studies — this is an established clinical use pattern rather than a speculative repurposing hypothesis. However, the drug is not currently marketed locally and a blocking safety data gap remains unresolved.

**To proceed, the following is needed:**
- Local SFDA-approved package insert (warnings/contraindications) — currently a **Blocking** data gap (DG001)
- Formal DrugBank-sourced mechanism-of-action documentation (High-severity data gap, DG002)
- Drug-drug interaction data (current query status: not found)
- Local marketing authorization / registration pathway assessment, since the drug currently has zero licenses in Saudi Arabia
- Alignment with local clinical treatment guidelines for resistant or severe pneumococcal pneumonia before formal positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

