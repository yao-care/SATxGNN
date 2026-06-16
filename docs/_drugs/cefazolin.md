---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# CEFAZOLIN: From Surgical Prophylaxis to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, widely recognized as the gold-standard agent for perioperative surgical prophylaxis and treatment of gram-positive bacterial infections per ASHP and IDSA guidelines.
The TxGNN model predicts it may be effective for **Infectious Otitis Media** (prediction score: 99.44%), with **1 clinical trial** and **3 publications** currently identified in support of this direction — though the clinical trial was terminated before completion and evidence remains at an observational level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Surgical prophylaxis; gram-positive bacterial infections (skin, soft tissue, urinary tract) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not captured in this dataset. Based on established pharmacological knowledge, Cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and triggering bacterial lysis. Its antimicrobial spectrum is strongest against gram-positive organisms — particularly *Staphylococcus aureus* and *Streptococcus pyogenes* — with limited activity against gram-negative species.

The connection to infectious otitis media is mechanistically partial. Acute otitis media is most commonly caused by *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*, for which Cefazolin has significant coverage gaps. However, in cases where *S. aureus* or *S. pyogenes* are the predominant pathogens (a recognized minority of presentations), Cefazolin's spectrum aligns well. A 2025 case report (PMID 39567876) documents Cefazolin's use in Gradenigo syndrome — a rare, severe complication of petrous apicitis secondary to acute otitis media — as part of an empiric combination regimen targeting gram-positive organisms in a serious ENT infection.

The TxGNN model's high confidence score (99.44%) likely reflects the pathogen-level mechanistic overlap rather than a direct indication match. Clinically, Cefazolin's IV/IM-only route of administration and incomplete pathogen coverage reduce its practicality as a primary therapy for typical community-acquired otitis media, though there may be a niche role in inpatient or post-surgical ENT contexts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Evaluated short-course (5-day) vs. standard-duration (10-day) antimicrobial therapy in children aged 6–23 months with acute otitis media; designed as a randomized, double-blind, placebo-controlled trial. Trial was terminated before completion. The specific antibiotic studied is not confirmed to be Cefazolin, and no efficacy results are available. The termination is an important caution signal. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Report | Ann Otol Rhinol Laryngol | Ceftazidime + Cefazolin empiric combination therapy for pediatric Gradenigo syndrome (a rare, severe complication of otitis media with petrous apicitis); supports Cefazolin's contribution as gram-positive coverage in complicated ENT infections where *S. aureus* and *Streptococcus* spp. are implicated |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Med J | Overview of cephalosporin antibiotics in pediatric practice; notes the class's efficacy against gram-positive cocci and selected gram-negative bacilli, with potential application in pediatric ear infections, particularly in penicillin-allergic patients |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Series/Review | Clinical Pharmacy | Case review of Stevens-Johnson syndrome in a child who received Cefazolin during management of otitis media and febrile seizures; provides indirect evidence of historical Cefazolin use in the otitis media clinical context, and also raises awareness of hypersensitivity risk |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** One literature item (PMID 3742953) documents Stevens-Johnson syndrome in a patient receiving Cefazolin for an otitis media episode, and the mechanistic rationale for Rank 8 (allergic otitis media) explicitly flags that beta-lactam antibiotics — including Cefazolin — are known triggers for severe hypersensitivity reactions including anaphylaxis and SJS. This cross-sensitivity risk (approximately 1–2% with penicillin-allergic patients) warrants standard beta-lactam allergy screening before use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole identified clinical trial was terminated before completion and cannot confirm Cefazolin as the study agent, leaving the highest available evidence at the observational/case report level (L3). More fundamentally, Cefazolin's antimicrobial spectrum has insufficient coverage of the three most common pathogens in infectious otitis media (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*), making it unsuitable as a first-line empiric monotherapy for this indication without further subgroup stratification.

**To proceed, the following is needed:**
- **Pathogen subtype stratification:** Identify patient populations with *S. aureus*- or *S. pyogenes*-predominant otitis media, where Cefazolin's spectrum is most relevant
- **Safety data gap (DG001):** Retrieve full warnings and contraindications from the package insert before any clinical use assessment
- **MOA documentation (DG002):** Formal DrugBank MOA data to complete the mechanistic linkage analysis
- **Route feasibility assessment:** Clarify whether IV/IM administration is compatible with the target clinical setting (inpatient ENT vs. outpatient primary care)
- **Prospective study design:** A protocol targeting Cefazolin as perioperative prophylaxis or adjunct treatment in complicated otitis media cases (e.g., Gradenigo syndrome, post-tympanoplasty) would be the most scientifically justified next step given current evidence
- **Saudi Arabia regulatory pathway:** Since Cefazolin is not currently marketed in Saudi Arabia (0 authorizations), regulatory submission would require a full dossier prior to any market access strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

