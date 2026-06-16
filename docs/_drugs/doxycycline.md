---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic and a WHO-recommended first-line treatment for Chlamydia trachomatis infections, Rocky Mountain spotted fever, Lyme disease, and malaria prophylaxis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **no registered clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Saudi Arabia registration on file; known for broad-spectrum bacterial infections (chlamydia, Lyme disease, rickettsia, malaria prophylaxis) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known information, doxycycline is a tetracycline-class antibiotic; its efficacy against a wide range of intracellular and extracellular bacteria — including Chlamydia trachomatis — has been well established clinically, and it additionally exhibits anti-inflammatory activity through inhibition of matrix metalloproteinases (MMPs).

The mechanistic link to punctate epithelial keratoconjunctivitis is indirect. Chlamydia trachomatis infection causes follicular conjunctivitis; one recognised sequela of this infection is persistent superficial punctate epithelial keratitis (SPEK), which can persist even after the conjunctival follicles resolve. In this scenario, doxycycline acts by eliminating the infectious trigger rather than by directly targeting the corneal epithelial lesions.

The sole supporting publication (PMID 1424659, 1992) describes exactly this sequence in two patients — chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline, followed by recurrent bilateral punctate corneal epithelial lesions despite pathogen clearance. This underscores that the keratitis may represent a post-infectious immune phenomenon rather than active infection, meaning antibiotic treatment alone may be insufficient, and no interventional study has specifically evaluated doxycycline for the keratitis itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | Cornea | Two patients with Chlamydia trachomatis follicular conjunctivitis developed persistent bilateral punctate epithelial keratitis after initial resolution with tetracycline or doxycycline; corneal lesions at various epithelial levels with fluorescein staining and anterior stromal oedema, suggesting a post-infectious immune-mediated process |

---

## Saudi Arabia Market Information

Doxycycline currently has no registered products in the Saudi Arabia drug database. No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single 1992 case series reporting post-chlamydial keratitis as a sequela after doxycycline treatment; no clinical trials have directly evaluated doxycycline for punctate epithelial keratoconjunctivitis itself, and the available case report actually demonstrates that antibiotic treatment did not prevent subsequent corneal disease, raising questions about the drug's direct therapeutic value for this indication.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data retrieval from DrugBank API to confirm anti-inflammatory properties relevant to corneal epithelium
- Saudi Arabia package insert (download and parse PDF) for key warnings and contraindications
- Drug interaction (DDI) profile review before any clinical application
- Prospective observational or pilot clinical study evaluating whether sub-antimicrobial dose doxycycline (via MMP inhibition) reduces recurrence of post-chlamydial punctate keratitis
- Route compatibility assessment: determine whether systemic oral dosing or topical ophthalmic formulation is appropriate for this indication
- Ophthalmology specialist consultation to distinguish active chlamydial keratitis from immune-mediated post-infectious keratitis, as the treatment rationale differs substantially between the two
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

