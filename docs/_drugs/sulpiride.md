---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 9
---

# Sulpiride
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

# Sulpiride: Original Indication Not on File — TxGNN Signal for Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

The evidence pack does not record Sulpiride's original approved indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts a possible link to **Retinal Dystrophy with or without Extraocular Anomalies**, but this is supported by **0 clinical trials** and **15 loosely related publications**, none of which studies Sulpiride itself — the evidence pack's own mechanistic analysis flags the prediction as a likely knowledge-graph artifact rather than a real pharmacological connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (no licenses / indications on file) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Sulpiride is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the limited information available, Sulpiride is known as a selective D2/D3 dopamine receptor antagonist, typically used in psychiatric/neurological contexts — but the original approved indication itself is not documented here.

The predicted indication, retinal dystrophy with or without extraocular anomalies, is a congenital developmental disorder group typically caused by structural gene defects (e.g., PAX6, SOX2, and other retinal-development genes). There is no established pathogenic connection between dopamine receptor signaling and this disease group.

**This prediction should be treated with caution.** The mechanistic assessment for this candidate explicitly notes that the high TxGNN score most likely reflects "ophthalmology-related node proximity" in the knowledge graph — a structural/statistical artifact — rather than a genuine pharmacological relationship. Eight additional TxGNN-predicted indications for Sulpiride (rare congenital/genetic disorders, including hydranencephaly, polymicrogyria syndromes, CMT type 1G, X-linked myopias, a glycosylation disorder, and glycine encephalopathy) show the same pattern: very high model scores, zero clinical trials, zero or negligible literature, and no plausible mechanistic link to D2/D3 antagonism. This pattern across the full candidate list further supports treating the top prediction as unconfirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

**Note:** None of the publications below study Sulpiride directly — they are general ophthalmology/genetics literature on the disease phenotype (retinal dystrophy, congenital extraocular anomalies) surfaced by topical relevance, not drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections and cellulitis staging secondary to sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic clinical approach to diplopia (ocular/neurologic/muscular causes) |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric congenital ocular pathologies (microphthalmos, coloboma, ROP, etc.) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated anterior segment dysgenesis |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis classification and associated extraocular muscle fibrosis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration with extraocular manifestations |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Ophthalmoplegia within Congenital Cranial Dysinnervation Disorders (CCDDs) |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia with absent extraocular muscles/optic nerve |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | International Journal of Molecular Sciences | Optic nerve/retinal abnormalities in Congenital Fibrosis of Extraocular Muscles (KIF21A/TUBB3) |

## Saudi Arabia Market Information

Sulpiride is currently **not marketed** in Saudi Arabia — no product authorizations are on file (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable in this evidence pack — TFDA package insert retrieval is flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or drug-specific literature support use of Sulpiride in retinal dystrophy with or without extraocular anomalies, and the disease's known genetic etiology has no established link to D2/D3 dopamine receptor antagonism. The evidence pack's own mechanistic review flags the TxGNN score as a probable knowledge-graph artifact rather than a real signal, and all other predicted indications for this drug show the identical no-evidence, no-mechanism pattern.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature — currently a High-severity gap (DG002)
- Sulpiride's original approved indication(s), to properly assess indication-to-indication rationale
- Preclinical or mechanistic studies directly linking dopaminergic signaling to retinal/extraocular developmental pathways, if any exist
- Independent confirmation that the TxGNN score is not an artifact of ophthalmology-node clustering in the knowledge graph before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

