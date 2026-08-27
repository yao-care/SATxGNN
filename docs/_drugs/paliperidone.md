---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy With or Without Extraocular Anomalies

## One-Sentence Summary

Paliperidone (9-hydroxyrisperidone) is an established atypical antipsychotic already used to treat schizophrenia. The TxGNN model's top-ranked prediction is **Retinal Dystrophy With or Without Extraocular Anomalies**, but this signal is currently supported by **0 clinical trials** and **15 publications, none of which mention paliperidone or any antipsychotic** — the literature only shares topical overlap (ophthalmology). The evidence pack's own analysis flags this as a likely embedding-level false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per known drug class; detailed MOA/indication text not on file) |
| Predicted New Indication | Retinal Dystrophy With or Without Extraocular Anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for paliperidone in this evidence pack. Based on known drug-class information, paliperidone is an atypical antipsychotic whose efficacy in schizophrenia is well established; the underlying pharmacology (D2/5-HT2A receptor antagonism) is not documented here in structured form.

However, this specific prediction does not hold up under scrutiny. Retinal dystrophy with or without extraocular anomalies is a hereditary/structural ophthalmic disorder, and there is no known pathophysiological link between D2/5-HT2A receptor antagonism and retinal dystrophy. The 15 associated publications are all background literature on congenital ophthalmic conditions (orbital infections, diplopia, congenital ptosis, Wagner-Stickler syndrome, congenital cranial dysinnervation disorders, etc.) — **not one addresses paliperidone or any antipsychotic drug**.

The most plausible explanation is that the high TxGNN score reflects an embedding-space proximity artifact (the model may be clustering rare/genetic disease categories near each other) rather than a genuine pharmacological signal. Nine of the ten predicted indications in this evidence pack are rare genetic/structural disorders (myopia subtypes, hydranencephaly, congenital glycosylation disorders, Charcot-Marie-Tooth, glycine encephalopathy) with identical L5/Hold status and no supporting evidence — reinforcing that this cluster of predictions should not be prioritized for further investigation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections secondary to sinusitis; no drug relevance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Diagnostic approach to diplopia from ocular/neurologic/muscular causes |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric congenital ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and development |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Clinical features of simple vs. complicated congenital ptosis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex, vitreoretinal degeneration |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders and ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis/treatment of maculopathy with cavitary optic disc anomalies |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | International Journal of Molecular Sciences | Optic nerve/retinal abnormalities in congenital fibrosis of extraocular muscles |

None of the above literature discusses paliperidone, antipsychotics, or any pharmacological intervention — all are disease-background papers.

## Saudi Arabia Market Information

Paliperidone is currently **not marketed** in this market (0 authorizations on file), so no product/license table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not corroborated by any clinical trial or drug-relevant literature, and no mechanistic pathway connects paliperidone's antipsychotic pharmacology to a hereditary retinal dystrophy. The evidence pack's own rationale assessment concludes this is likely an embedding-level false positive, and eight of the other nine predicted indications for this drug show the identical pattern (L5, no evidence, no mechanistic plausibility).

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (DrugBank) to formally rule out any indirect pathway
- Any preclinical or case-level evidence linking antipsychotics to retinal/ophthalmic disease modulation, if it exists
- TFDA/regulatory package insert data (currently blocking — DG001) before any safety review can begin

**Note:** A separate, better-supported signal exists lower in this same evidence pack — **treatment-refractory schizophrenia** (rank 10, TxGNN score 99.80%, Evidence Level L2, recommendation *Proceed with Guardrails*, backed by a completed Phase 4 trial (NCT01860781, n=30) and 2 literature reviews). That signal is not a novel repurposing candidate (paliperidone already treats schizophrenia) but reflects a clinically actionable extension to a treatment-resistant subpopulation, and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

