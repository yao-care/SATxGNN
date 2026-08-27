---
layout: default
title: Zuclopenthixol
parent: 僅模型預測 (L5)
nav_order: 677
evidence_level: L5
indication_count: 9
---

# Zuclopenthixol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Zuclopenthixol: From Antipsychotic Therapy to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Zuclopenthixol is a thioxanthene-class typical antipsychotic, with no confirmed original indication data or approved regulatory license currently available for this drug. The TxGNN model predicts a possible link to **retinal dystrophy with or without extraocular anomalies**, but the supporting literature does not actually discuss zuclopenthixol, and **no clinical trials** exist for this drug-disease pair — the extremely high TxGNN score (99.99%) is very likely a model prediction artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (evidence pack notes drug class: typical antipsychotic, thioxanthene) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap in the evidence pack). Based on general pharmacological knowledge referenced within the evidence pack's own rationale, zuclopenthixol is a typical (first-generation) antipsychotic of the thioxanthene class, whose primary activity is D1/D2 dopamine receptor antagonism, used in psychotic disorders.

Retinal dystrophy with or without extraocular anomalies is a congenital/hereditary ophthalmic condition, with pathology typically driven by photoreceptor gene mutations and ocular developmental abnormalities. There is no established pharmacological or mechanistic pathway connecting dopamine receptor antagonism to retinal photoreceptor degeneration or ocular developmental biology.

The TxGNN score of 0.9999 is unusually high, but this pattern is consistent with a known behavior of graph neural network predictions on rare-disease nodes with sparse connectivity — very high scores can reflect model noise rather than true biological signal, especially when (as here) no clinical trials exist and the retrieved literature does not mention the drug at all. The same pattern (near-1.0 scores with zero supporting evidence) is seen across all other predicted indications for this drug, reinforcing that these predictions should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

**Note:** None of the retrieved publications below mention zuclopenthixol directly — they were retrieved based on disease-term matching and reflect general ophthalmology literature on congenital/developmental eye disorders, not drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections and cellulitis staging secondary to sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Diagnostic approach to diplopia from ocular, neurologic, or extraocular muscle disorders |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric congenital/developmental ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated anterior segment dysgenesis |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Simple vs. complicated congenital ptosis and levator muscle dystrophy |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome: vitreoretinal degeneration with extraocular manifestations |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | International Journal of Molecular Sciences | Optic nerve/retinal abnormalities in congenital fibrosis of extraocular muscles (KIF21A/TUBB3) |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia with absent extraocular muscles/optic nerve |

---

## Saudi Arabia Market Information

Currently no marketing authorization registered in Saudi Arabia.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) in the evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial evidence, no drug-specific literature, and no plausible mechanistic link between zuclopenthixol's dopaminergic antipsychotic activity and a congenital retinal developmental disorder. The drug is also not currently marketed in Saudi Arabia (0 authorizations). This pattern — near-maximal TxGNN scores with zero corroborating evidence — repeats across all 9 predicted indications in this candidate set (hydranencephaly, CDG, CMT1G, myopia subtypes, polymicrogyria, glycine encephalopathy), suggesting these are model artifacts rather than actionable repurposing signals.

**To proceed, the following is needed:**
- TFDA/regulatory package insert with warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action (DrugBank query, currently a High-severity data gap)
- Original approved indication(s) for zuclopenthixol (not present in current dataset)
- Drug-disease-specific literature or preclinical mechanistic studies actually linking zuclopenthixol to retinal/ophthalmic pathology, before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

