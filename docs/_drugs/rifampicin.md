---
layout: default
title: Rifampicin
parent: 僅模型預測 (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Rifampicin
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

# Rifampicin: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Rifampicin (DrugBank DB01045) is a rifamycin-class antibiotic whose established clinical role is in the treatment of **tuberculosis** (this original-indication context is inferred from the supporting literature/trials in this pack, since no structured indication field was returned from TFDA/DrugBank licensing data). The TxGNN model predicts it may also be effective for **Conjunctivitis**, with a very high prediction score (99.95%) but currently **no registered clinical trials** and only **20 supporting publications**, most of them decades-old microbiology surveys or historical case reports rather than confirmatory trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (based on established clinical use; not present in this pack's structured licensing data) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information that is available, rifampicin belongs to the rifamycin class of antibiotics; its efficacy in tuberculosis has been well established for decades, and mechanistically it is a broad-spectrum bactericidal agent that could plausibly extend to bacterial and chlamydial conjunctivitis.

The repurposing rationale captured in the evidence pack is explicit on this point: topical rifampicin has direct antibacterial activity against *Chlamydia trachomatis* (the cause of trachoma) and against staphylococcal conjunctivitis — describing this as "a historically established therapy rather than a novel mechanism." This is consistent with the literature returned: a 1975 controlled trial in Tunisia compared 1% rifampicin ointment against tetracycline and boric acid for endemic trachoma (PMID 1096630), and a 1970 *Nature* paper first characterized the anti-trachoma activity of rifampicin and its rifamycin SV derivatives (PMID 5411121). A 2003 case report also documents systemic rifampin being used successfully as part of therapy for primary meningococcal conjunctivitis (PMID 14686993).

However, this body of evidence is old (largely 1970s–2011), consists mainly of microbiological susceptibility surveys rather than therapeutic trials, and — critically — **no clinical trials for rifampicin in conjunctivitis are currently registered** in ClinicalTrials.gov or ICTRP. The signal should be read as "biologically plausible and historically precedented," not as "clinically validated for modern use."

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | Clinical trial (open) | American Journal of Ophthalmology | Controlled Tunisian trial comparing topical 1% rifampicin ointment, 1% tetracycline ointment, and 5% boric acid ointment for endemic trachoma in schoolchildren; bacteriologic and slit-lamp follow-up to 39 weeks |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | Preclinical | Nature | Early characterization of anti-trachoma (*Chlamydia*) activity of rifampicin and rifamycin SV derivatives |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Case report | Clinical Microbiology and Infection | Primary meningococcal conjunctivitis in a healthy 6-year-old, initially treated with topical polymyxin B/neomycin/gramicidin, followed by systemic rifampin once diagnosed; no ocular or systemic complications |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Case report / commentary | Annals of Ophthalmology | Early clinical note on rifampicin use in ophthalmology (abstract not available) |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Microbiology susceptibility | Advanced Biomedical Research | Bacterial etiology and antibiotic susceptibility survey of conjunctivitis isolates in Kashan, Iran |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Microbiology susceptibility | Anales de Pediatría (Barcelona) | Identifies the most prevalent bacterial conjunctivitis pathogens and their antibiotic sensitivity profile |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Microbiology susceptibility | Journal of Ophthalmic Inflammation and Infection | Bacteriologic and plasmid analysis of conjunctivitis pathogens in Lagos, Nigeria, including antibiotic resistance patterns |
| [30347565](https://pubmed.ncbi.nlm.nih.gov/30347565/) | 2018 | Microbiology susceptibility | Chinese Journal of Ophthalmology | Genetic typing and antibiotic susceptibility of *S. aureus* strains isolated from keratitis or conjunctivitis patients |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | Microbiology susceptibility | Anales Españoles de Pediatría | Microbiologic study of 50 neonatal conjunctivitis samples with antibiotic sensitivity profiling |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Review / case series | Current Opinion in Ophthalmology | Review of ocular manifestations of cat-scratch disease (*Bartonella henselae*), including conjunctivitis (Parinaud's oculoglandular syndrome) |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are recorded as a **Blocking** data gap in this pack — see Conclusion below — and the DDI database query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for rifampicin in conjunctivitis is real but dated and indirect — a controlled trachoma trial from 1975 and a 1970 mechanistic paper, surrounded mostly by unrelated microbiology susceptibility surveys — with **zero currently registered clinical trials**. More decisively, TFDA package-insert warnings/contraindications data is missing and marked as a **Blocking** gap (DG001), which by design prevents this candidate from entering the S1 safety pre-assessment stage regardless of how promising the efficacy signal looks.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — Blocking gap DG001, required before any S1 safety review
- Confirmed drug mechanism-of-action detail from DrugBank — High-severity gap DG002
- A contemporary systematic review or trial evaluating rifampicin (topical/ophthalmic) against modern standard-of-care antibiotics for bacterial or chlamydial conjunctivitis
- Resolution of the DDI query (currently `not_found`)
- Clarification of Saudi Arabia registration status, since the drug is currently unmarketed with 0 licenses on file
- Note: rank 4 in this pack ("conjunctivitis (disease)") is a duplicate ontology node of rank 1 with identical evidence — recommend merging these nodes in the underlying database to avoid double-counting this signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

