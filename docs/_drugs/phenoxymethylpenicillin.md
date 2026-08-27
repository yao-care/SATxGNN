---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
---

# Phenoxymethylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenoxymethylpenicillin: From Bacterial Infections to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (Penicillin V, DrugBank DB00417) is a narrow-spectrum oral beta-lactam antibiotic; detailed data on its original approved indication and mechanism of action were not retrievable in this dataset. TxGNN's top-ranked prediction is **Epiglottitis**, but this signal is currently supported by **no clinical trials and no literature** — it is a model-only prediction (L5). A second candidate, **Laryngitis**, was also predicted with a similar score and is backed by **19 publications**, but the existing randomized evidence in that literature actually argues *against* penicillin V's efficacy for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (drug class: narrow-spectrum penicillin/beta-lactam antibiotic) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as data gap DG002, DrugBank query pending). Based on known pharmacology, phenoxymethylpenicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, and its efficacy against susceptible Gram-positive and some Gram-negative organisms is well established as a drug class.

Epiglottitis is predominantly a bacterial airway infection, historically associated with *Haemophilus influenzae* type b and also seen with *Streptococcus* species. On a purely mechanistic basis, a beta-lactam antibiotic has theoretical activity against susceptible causative organisms, which is the basis for the TxGNN association.

However, this mechanistic plausibility does not translate cleanly into clinical applicability: epiglottitis is an airway emergency that standardly requires broad-spectrum, intravenous antibiotics (e.g., ceftriaxone) to cover beta-lactamase-producing strains. Phenoxymethylpenicillin is an oral, narrow-spectrum agent — both its route of administration and antimicrobial spectrum are mismatched with the acute standard of care, which is why the underlying evidence pack itself classifies this rationale as mechanistically limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Epiglottitis.

### Secondary Candidate: Laryngitis (TxGNN score 99.85%, L2)

TxGNN also ranked **Laryngitis** highly for this drug. Unlike Epiglottitis, this candidate has substantial literature — but the direct evidence is negative for penicillin V:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3918495](https://pubmed.ncbi.nlm.nih.gov/3918495/) | 1985 | RCT (Tier 1) | Ann Otol Rhinol Laryngol | Double-blind study in 100 adults with acute laryngitis: penicillin V showed **no better resolution of vocal symptoms than placebo** |
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | RCT (Tier 2) | Acta Otolaryngol Suppl | Notes prior finding that **phenoxymethylpenicillin had no effect on the clinical course** of acute laryngitis; erythromycin was tested as an alternative |
| [26002823](https://pubmed.ncbi.nlm.nih.gov/26002823/) | 2015 | Review (Tier 1) | Cochrane Database Syst Rev | Cochrane review (latest update) on antibiotics for acute laryngitis in adults; most cases are viral and antibiotic benefit is not well established |
| [23543536](https://pubmed.ncbi.nlm.nih.gov/23543536/) | 2013 | Review (Tier 1) | Cochrane Database Syst Rev | Earlier Cochrane update of the same systematic review, consistent conclusions |

The drug's own repurposing rationale for laryngitis notes that acute laryngitis is mostly viral in etiology, so a cell-wall-synthesis inhibitor has a mechanistic basis only in the minority of bacterial cases — consistent with the negative RCT findings above. This candidate is evidence-richer than Epiglottitis but the existing direct evidence weighs against efficacy rather than supporting it.

---

## Saudi Arabia Market Information

Phenoxymethylpenicillin is **not currently marketed** in Saudi Arabia per this dataset (0 registered licenses found).

---

## Safety Considerations

TFDA/regulatory package insert data (warnings, contraindications, drug interactions) could not be retrieved for this drug in the current dataset — this is flagged as a **blocking data gap (DG001)** that must be resolved before the candidate can enter formal safety screening (S1 stage). Please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Epiglottitis prediction is model-only (L5) with zero supporting trials or literature, and the mechanistic rationale itself flags a route/spectrum mismatch with standard-of-care treatment for this airway emergency. Safety evaluation cannot proceed until the blocking package-insert data gap is closed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications, DDI) — DG001, Blocking
- Confirmed mechanism of action from DrugBank — DG002, High
- Targeted literature/trial search specific to epiglottitis (current search returned zero hits)
- If pursuing the Laryngitis candidate instead, the existing negative RCT evidence (PMID 3918495, 1632252) should be explicitly weighed — current data leans toward rejecting rather than advancing that indication
- Route-of-administration assessment (oral vs. IV) given epiglottitis is an acute airway emergency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

