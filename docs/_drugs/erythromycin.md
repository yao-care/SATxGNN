---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 5
---

# Erythromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic; however, no approved-indication or licensing data for this drug is currently on file in this market. The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but this direction is currently supported only by **0 clinical trials** and **2 publications** (a pediatric case-series review and an unrelated case report), with no evidence data specific to erythromycin's efficacy in this exact condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — original_indications and license records are empty; erythromycin is generically known as a macrolide antibiotic, but no market-specific approved-indication text is available |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on general pharmacological knowledge, erythromycin is a macrolide-class antibiotic that inhibits bacterial protein synthesis (50S ribosomal subunit binding) in susceptible Gram-positive and some Gram-negative organisms. Ophthalmic erythromycin ointment is a well-established formulation used for superficial bacterial conjunctival/corneal infections, including prophylaxis of neonatal gonococcal conjunctivitis.

Punctate epithelial keratoconjunctivitis, however, is a clinical presentation most frequently associated with viral pathogens (e.g., adenovirus) or atypical, non-bacterial organisms (e.g., Microsporidia, as described in the supporting literature below) rather than classic susceptible bacteria. Erythromycin has no activity against these causative agents.

Because of this mismatch, the mechanistic link identified in this evidence pack is characterized as **indirect**: erythromycin's plausible role would be limited to prevention or treatment of a *secondary* bacterial co-infection in cases of blepharokeratoconjunctivitis, rather than treatment of the underlying disease process itself. The high TxGNN prediction score should therefore be interpreted as a model-driven signal requiring substantial mechanistic and clinical corroboration before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review/Case series | Journal of Pediatric Ophthalmology and Strabismus | Describes history, symptoms, clinical signs, and treatment approach for chronic blepharokeratoconjunctivitis in children |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case report | Cornea | Reports a case of microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult, diagnosed via metagenomic deep sequencing and confirmed by PCR — a non-bacterial etiology not addressed by erythromycin |

---

## Saudi Arabia Market Information

Erythromycin is currently not marketed in this jurisdiction, and no product authorization or license records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.89%), the supporting evidence is limited to two non-comparative publications — a general pediatric case-series review and a case report describing a non-bacterial (microsporidial) etiology — with zero clinical trials. The disease is predominantly viral/atypical in origin, and the mechanistic rationale for erythromycin is explicitly indirect (only a supportive role against secondary bacterial co-infection). This does not meet the threshold for proceeding, even with guardrails.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a **Blocking** data gap — required before any safety pre-assessment can begin)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source (currently a **High**-severity data gap)
- Original approved-indication and licensing data for this drug in this market
- Preclinical or in-vitro evidence specifically demonstrating erythromycin activity against pathogens implicated in punctate epithelial keratoconjunctivitis
- Note: other TxGNN-predicted indications in this evidence pack — notably **lymphogranuloma venereum** (L3, Proceed with Guardrails) and **necrotizing ulcerative gingivitis** (L3, Proceed with Guardrails) — show stronger direct mechanistic and historical literature support and may warrant separate, higher-priority evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

