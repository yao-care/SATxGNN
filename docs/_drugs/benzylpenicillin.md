---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 7
---

# Benzylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Benzylpenicillin: From Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (Penicillin G) is one of the oldest natural β-lactam antibiotics, historically used to treat serious bacterial infections caused by susceptible Gram-positive organisms, including streptococcal, pneumococcal, and spirochetal infections.
The TxGNN model predicts it may be effective for **Pericoronitis** (acute infection around partially erupted wisdom teeth),
with **no registered clinical trials** but **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (streptococcal, pneumococcal, syphilis) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Benzylpenicillin (Penicillin G) is a classic natural penicillin whose β-lactam ring irreversibly binds penicillin-binding proteins (PBPs), inhibiting bacterial cell wall peptidoglycan cross-linking and achieving bactericidal activity. Although detailed MOA data is not captured in the current regulatory dataset, this mechanism is extensively documented in the pharmacological literature and is specific to organisms that rely on peptidoglycan for structural integrity.

Pericoronitis is a mixed bacterial infection arising around partially erupted mandibular third molars. The predominant flora consists of Gram-positive streptococci, peptostreptococci, and strict anaerobes including *Bacteroides* and *Fusobacterium* — organisms that fall squarely within benzylpenicillin's classical spectrum. The mechanistic link is therefore direct and well-grounded: PBP inhibition is bactericidal against the primary pathogens driving pericoronitis, making the TxGNN prediction biologically plausible.

A key limitation documented in the literature (PMID 12789143) is the presence of β-lactamase-producing strains among pericoronitis isolates, which can reduce benzylpenicillin's efficacy. Expert consensus (PMID 1873287) and systematic review evidence (PMID 35959239) recommend that penicillins be used as first-line monotherapy for dental infections, with metronidazole added when strict anaerobic coverage is required. This does not negate the prediction, but suggests that benzylpenicillin may be most appropriate as part of a combination regimen rather than as sole agent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for benzylpenicillin in pericoronitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39068391](https://pubmed.ncbi.nlm.nih.gov/39068391/) | 2024 | RCT | BMC Oral Health | A combination mouthwash (chlorhexidine + benzydamine + nanosilver + amoxicillin + metronidazole) significantly reduced pain and improved maximum mouth opening in acute pericoronitis |
| [35959239](https://pubmed.ncbi.nlm.nih.gov/35959239/) | 2022 | Systematic Review | JAC-Antimicrobial Resistance | β-Lactams should be first-line monotherapy for dental infections with systemic involvement; combination with metronidazole reserved for refractory cases |
| [16781343](https://pubmed.ncbi.nlm.nih.gov/16781343/) | 2006 | Prospective Cohort | J Oral Maxillofac Surg | Prospective series of severe odontogenic infections; characterized causative organisms and antibiotic treatment outcomes across infection stages |
| [1873287](https://pubmed.ncbi.nlm.nih.gov/1873287/) | 1991 | Expert Survey | Br J Oral Maxillofac Surg | British oral surgeons identified penicillins (including amoxicillin) and metronidazole as effective antimicrobials for acute pericoronitis, which is dominated by anaerobic organisms |
| [12789143](https://pubmed.ncbi.nlm.nih.gov/12789143/) | 2003 | Microbiological Study | Oral Surg Oral Med Oral Pathol | Characterised pericoronitis flora around mandibular third molars; notable proportion of β-lactamase-producing strains identified as a resistance concern for benzylpenicillin |
| [40381916](https://pubmed.ncbi.nlm.nih.gov/40381916/) | 2025 | Surveillance Study | J Infect Chemother | Second nationwide antimicrobial susceptibility surveillance of odontogenic infection isolates in Japan, including pericoronitis group; updated resistance profiles reported |
| [26067725](https://pubmed.ncbi.nlm.nih.gov/26067725/) | 2015 | Retrospective Cohort | J Contemp Dent Pract | Analysed prevalence, demographic patterns, and antibiotic management of odontogenic infections in a university hospital dental emergency service |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | Eur J Translat Myol | Reviewed antibiotic choices for odontogenic infections during pregnancy; penicillins highlighted as the safest first-line option |
| [29693642](https://pubmed.ncbi.nlm.nih.gov/29693642/) | 2018 | Narrative Review | Antibiotics (Basel) | Reviewed antibiotic prescribing for oro-facial infections in paediatric patients; documented overuse and misuse patterns; β-lactams recommended as first-line |
| [21027620](https://pubmed.ncbi.nlm.nih.gov/21027620/) | 1946 | Historical Case Report | Am J Orthod Oral Surg | Early case report of submaxillary abscess secondary to acute pericoronitis successfully treated by aspiration and direct instillation of penicillin; historical proof-of-concept |

---

## Saudi Arabia Market Information

Benzylpenicillin currently holds no SFDA authorizations and is not marketed in Saudi Arabia.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for benzylpenicillin in pericoronitis is well-established — the primary causative organisms (Gram-positive streptococci, peptostreptococci, and strict anaerobes) lie within the drug's classical spectrum — and is corroborated by microbiological surveillance data, expert consensus, and observational evidence (L3). However, the absence of registered clinical trials, the presence of β-lactamase-producing strains in the pericoronitis flora, and the lack of SFDA market authorization require structured risk management before clinical deployment.

**To proceed, the following is needed:**
- **Regulatory pathway assessment**: Determine whether benzylpenicillin can be imported or registered via SFDA's standard or expedited pathways for essential medicines
- **Complete MOA and safety dossier**: Retrieve full mechanism of action data and package insert warnings/contraindications from DrugBank and original regulatory filings
- **Local susceptibility mapping**: Obtain Saudi Arabia–specific antimicrobial susceptibility data for pericoronitis isolates to estimate the prevalence of β-lactamase-producing strains
- **Combination therapy protocol**: Define whether benzylpenicillin should be paired with metronidazole for adequate anaerobic coverage, based on local resistance profiles
- **Prospective clinical validation**: Design a registry study or controlled trial in Saudi Arabia to generate local efficacy and safety data before broad formulary adoption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

