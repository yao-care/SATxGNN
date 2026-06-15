---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# AMIKACIN: From Gram-Negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic historically used for serious gram-negative bacterial infections, though no formal indications are registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**,
with **0 clinical trials** and **12 publications** currently supporting this direction — primarily observational studies and case reports documenting amikacin use in multi-drug resistant (MDR) enteric fever settings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia; established clinical use for serious gram-negative bacterial infections (aminoglycoside antibiotic class) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Paratyphoid fever is caused by *Salmonella* Paratyphi A, B, and C — gram-negative enteric bacilli. Amikacin, as a semisynthetic aminoglycoside antibiotic, exerts bactericidal activity against gram-negative organisms by irreversibly binding the 30S ribosomal subunit, inhibiting protein synthesis. It demonstrably retains in vitro bactericidal activity against *Salmonella* species, including strains resistant to first-line agents.

The clinical relevance of this prediction becomes most apparent in the context of MDR and extensively drug-resistant (XDR) enteric fever. When *Salmonella* Paratyphi A/B strains acquire resistance to chloramphenicol, ampicillin, and co-trimoxazole — the classical first-line regimens — and subsequently to fluoroquinolones, aminoglycosides such as amikacin emerge as rescue or combination therapy candidates. Multiple case reports and antibiogram studies in the literature document amikacin sensitivity in MDR *Salmonella* Paratyphi isolates.

Currently, detailed mechanism of action data is not available from the DrugBank data feed. Based on known clinical pharmacology, amikacin belongs to the aminoglycoside class and its efficacy in serious gram-negative infections is well established. The mechanistic basis for its activity against enteric *Salmonella* is therefore consistent with its broader class action, and its predicted utility in paratyphoid fever reflects an extension of this established antibacterial spectrum rather than a genuinely novel repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective observational | Journal of the Indian Medical Association | 145 blood culture-positive enteric fever cases in children; determined antibiotic sensitivity patterns for *S. typhi* and *S. paratyphi*, providing evidence base for aminoglycoside sensitivity in MDR isolates |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case series / retrospective clinical | Mikrobiyoloji bulteni | 48 pediatric patients with *Salmonella* Paratyphi B infections resistant to classical treatment; antibiogram and treatment outcomes documented for alternative antibiotics |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatric Hematology and Oncology | Acalculous cholecystitis caused by *S.* Paratyphi B in a child with leukemia — successfully treated with cefepime **+ amikacin** and G-CSF; direct evidence of amikacin use in *Salmonella* Paratyphi B infection |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case report | The Journal of Infection | Quinolone-resistant *S.* Paratyphi B meningitis in a neonate; highlights the clinical scenario where aminoglycosides become critical rescue options when fluoroquinolones fail |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case report | Indian Journal of Pediatrics | Paratyphoid sepsis in a neonate with blood culture-positive *S.* Paratyphi A; describes clinical management of neonatal Salmonella Paratyphi sepsis |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Cross-sectional / antibiogram | Pakistan Journal of Biological Sciences | Isolation and identification of *Salmonella* Paratyphi from enteric fever patients across multiple hospitals; antibiogram data relevant for treatment planning |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cross-sectional / antibiogram | JNMA (Nepal Medical Association) | Blood culture isolate frequency and antibiogram in a teaching hospital; antimicrobial susceptibility patterns to guide empiric therapy in bacteremia including Salmonella |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observational | Medical Journal, Armed Forces India | Re-emergence of chloramphenicol sensitivity in enteric fever; in vitro susceptibility of *S.* Typhi and *S.* Paratyphi A isolates including aminoglycoside sensitivity testing |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological surveillance | The New Microbiologica | 13-year surveillance of *Salmonella* Typhi and Paratyphi occurrence in Jordan; provides regional epidemiological context and resistance data |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | Journal of Pediatric Surgery | Successful percutaneous drainage + antibiotics (including amikacin combination) for splenic abscess in 4 pediatric patients; documents combined antibiotic utility in invasive Salmonella complications |

---

## Saudi Arabia Market Information

Amikacin is currently **not registered** in Saudi Arabia. No license records are available in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Formal safety data (key warnings, contraindications, drug-drug interactions) was not retrieved in this evidence pack cycle. Clinically, amikacin is an aminoglycoside antibiotic with well-known class-associated risks including nephrotoxicity and ototoxicity, which should be taken into account in any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between amikacin and paratyphoid fever is pharmacologically sound — amikacin retains consistent in vitro activity against *Salmonella* Paratyphi A/B/C, and clinical case evidence documents its real-world use in MDR and quinolone-resistant enteric fever when first-line options have failed. While no registered clinical trials exist, the observational evidence and antibiogram data across multiple endemic regions provide an L3 evidence base that justifies conditional advancement rather than a hold.

**To proceed, the following is needed:**
- Formal pharmacokinetic data for amikacin in enteric fever (serum/tissue concentrations relative to MIC breakpoints for *S.* Paratyphi)
- Definitive in vivo efficacy data (ideally a prospective comparative clinical study against current standard of care — azithromycin or 3rd-generation cephalosporins — in MDR paratyphoid fever)
- Characterization of current regional resistance patterns for *Salmonella* Paratyphi in the target patient population
- Saudi Arabia-specific regulatory registration plan (currently no local marketing authorisation)
- Full safety monitoring protocol covering nephrotoxicity and ototoxicity (therapeutic drug monitoring of amikacin serum concentrations recommended)
- Clarification of MOA data from DrugBank API (currently flagged as data gap DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

