---
layout: default
title: Potassium Iodide
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 2
---

# Potassium Iodide
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

# Potassium Iodide: From Unlisted Indication (Not Marketed in Taiwan) to Nasal Cavity Disease

## One-Sentence Summary

> Potassium iodide (KI, DrugBank DB06715) is not currently marketed in Taiwan and has no approved indication on record in this evidence pack.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **0 clinical trials** and **4 case-report publications**
> (mostly veterinary, one human) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — potassium iodide is not currently marketed in Taiwan |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for potassium iodide is not available in this evidence pack, and no original indication or Taiwan marketing history could be retrieved either — KI currently holds zero authorizations in Taiwan.

Based on the literature that was found, KI has known antifungal and anti-oomycete activity, thought to work by enhancing neutrophil fungicidal activity, disrupting pathogen cell membranes, and immunomodulation. All four supporting publications describe successful KI (or a closely related iodide salt) treatment of fungal/oomycete infections localized to the nasal cavity: rhinofacial pythiosis in sheep, mycotic rhinitis (*Aspergillus fumigatus*) in a horse, *Pseudallescheria boydii* nasal infection in a horse, and nasofacial zygomycosis in a human patient. This gives a mechanistically coherent link between KI's antifungal activity and the TxGNN-predicted indication.

However, "nasal cavity disease" is a broad diagnostic category, while the actual evidence is narrowly confined to specific fungal/oomycete infection subtypes — three of four cases are veterinary rather than human, and one case used sodium iodide rather than potassium iodide. The prediction should be read as applying to fungal/oomycete nasal infections specifically, not to nasal cavity disease in general.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case report (veterinary) | Veterinary Research Communications | Oral potassium iodide combined with topical clotrimazole successfully treated *Aspergillus fumigatus* mycotic rhinitis in a horse with nasal obstruction, discharge, and bleeding |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case report (veterinary) | Journal de Mycologie Médicale | KI treatment successfully resolved rhinofacial pythiosis (*Pythium insidiosum*, an oomycete) in sheep, presenting with nasal masses and facial deformity |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case report (veterinary) | Journal of the American Veterinary Medical Association | Horse with *Pseudallescheria boydii* nasal cavity infection treated with intranasal miconazole plus IV sodium iodide (related iodide compound, not potassium iodide) |
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case report (human, Portuguese) | Revista do Instituto de Medicina Tropical de São Paulo | Human case of nasofacial zygomycosis (mucormycosis) that responded rapidly to potassium iodide therapy — the only human case among the four |

## Taiwan Market Information

Potassium iodide is not currently marketed in Taiwan; no authorization records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to four case reports (L4, mostly veterinary, one using a related but different iodide salt) with no clinical trials, and potassium iodide is not currently marketed in Taiwan. Critically, TFDA package insert data (warnings/contraindications) is a **Blocking** data gap that prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications (Blocking gap — required before S1 safety review)
- Confirmed mechanism of action (MOA) data from DrugBank
- Original approved indication(s) and any prior Taiwan regulatory history
- Human clinical evidence beyond isolated case reports, ideally targeting fungal/oomycete nasal infections specifically rather than "nasal cavity disease" broadly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

