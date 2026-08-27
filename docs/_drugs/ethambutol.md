---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 5
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is a first-line antituberculosis agent, originally used as part of combination therapy (isoniazid, rifampicin, pyrazinamide, ethambutol) for tuberculosis treatment. The TxGNN model predicts it may be effective for **Epiglottitis**, but currently only **2 publications** — neither specific to epiglottitis — support this direction, and **no clinical trials** have been identified, indicating substantial uncertainty.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (pulmonary/extrapulmonary) — based on standard clinical use as part of first-line anti-TB combination therapy; no Saudi Arabia license text is available because the product is not currently marketed |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Ethambutol is part of the standard first-line antituberculosis combination regimen (isoniazid, rifampicin, pyrazinamide, ethambutol; "HRZE"), acting by inhibiting arabinosyltransferase (the *embCAB* gene product) and blocking arabinogalactan synthesis in the mycobacterial cell wall. Its efficacy in tuberculosis is well established.

The link to epiglottitis is indirect. Acute epiglottitis is overwhelmingly a pyogenic bacterial disease (classically *Haemophilus influenzae*), with a pathogen profile, patient population, and disease course that differ substantially from mycobacterial infection. The theoretical rationale rests on the fact that laryngeal structures — including the epiglottis — can occasionally be involved in tuberculosis (laryngeal tuberculosis), a recognized extrapulmonary manifestation for which Ethambutol-containing regimens are already standard of care.

However, the retrieved literature describes laryngeal tuberculosis broadly rather than epiglottitis specifically, and neither publication documents a treatment response for isolated epiglottic disease. This prediction should therefore be read as a mechanistically plausible but currently unproven extension of the existing tuberculosis indication, applicable at most to a narrow subset of epiglottitis cases with a confirmed tuberculous etiology — not to typical (bacterial) acute epiglottitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case Series | The European Respiratory Journal | Review of 41 laryngeal tuberculosis cases (1975–1985); the epiglottis was the second most frequently affected site after the true vocal cords, and patients were treated with isoniazid, rifampicin, and ethambutol |
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Review | The Lancet. Infectious Diseases | General review of laryngeal tuberculosis; no abstract available and not specific to epiglottitis |

---

## Saudi Arabia Market Information

Ethambutol is currently **not marketed** in Saudi Arabia — no product authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A TFDA package insert (warnings/contraindications) has not yet been retrieved for this product, which is a blocking data gap for a full safety evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to epiglottitis is weak — both available publications describe laryngeal tuberculosis in general rather than epiglottitis, no clinical trials exist, and the mechanistic rationale only applies to the rare subset of epiglottitis with confirmed tuberculous etiology, not typical bacterial acute epiglottitis. This corresponds to Evidence Level L4 (mechanism/case-based only) and decision stage S1. (For context, two other TxGNN-predicted indications for this drug — laryngitis and peritonitis — currently show stronger evidence, L3/S2 "Proceed with Guardrails," and may warrant prioritization over epiglottitis.)

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a blocking gap (DG001)
- Detailed mechanism of action (MOA) data from DrugBank — currently a high-priority gap (DG002)
- Epiglottitis-specific case reports or trials distinguishing tuberculous from bacterial etiology, to define an appropriate target population
- Saudi Arabia market authorization pathway, since the product is not currently marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

