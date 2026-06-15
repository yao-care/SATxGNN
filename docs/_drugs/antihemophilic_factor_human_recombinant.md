---
layout: default
title: Antihemophilic Factor Human Recombinant
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 8
---

# Antihemophilic Factor Human Recombinant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Antihemophilic Factor (Human Recombinant): From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Antihemophilic Factor (Human Recombinant) is a recombinant blood coagulation Factor VIII (rFVIII), classically used to control and prevent bleeding episodes in patients with Hemophilia A (congenital FVIII deficiency).
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with a prediction score of 99.96%;
however only **2 publications** currently support this direction and **no clinical trials** have been registered for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A — congenital Factor VIII deficiency (not registered in Saudi Arabia) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (genetic/mechanistic studies only) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, Antihemophilic Factor (Human Recombinant) is a recombinant form of human coagulation Factor VIII; its efficacy in controlling bleeding in Hemophilia A has been well-established over decades, and mechanistically it may provide compensatory support in primary platelet release disorders.

Recombinant FVIII functions as a critical cofactor in the intrinsic tenase complex (FVIIIa + FIXa), dramatically amplifying thrombin generation. Thrombin itself is a potent platelet activator via PAR-1 and PAR-4 receptors. In primary platelet release disorders — characterized by impaired dense granule or alpha-granule secretion — this downstream thrombin amplification pathway could theoretically compensate for inadequate primary hemostasis by maximizing activation of the platelets that are present.

However, this remains a compensatory downstream mechanism rather than targeted therapy. The two supporting publications (a large-scale GWAS linking FVIII/VWF levels to platelet aggregation, and a three-generational pedigree study showing compound FVIII/PTGS-1 variants amplify hemorrhage severity) provide biological plausibility for a FVIII–platelet interaction but constitute indirect genetic evidence only. This mechanistic link is exploratory and does not yet constitute clinical evidence of therapeutic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38320121](https://pubmed.ncbi.nlm.nih.gov/38320121/) | 2024 | Genetic Association Study (GWAS) | Blood | Whole-genome sequencing of up to 45,289 TOPMed participants identifies genetic loci associated with circulating FVIII and VWF levels; confirms FVIII and VWF are critical to both coagulation and platelet aggregation, providing indirect genetic context for an FVIII–platelet release link |
| [27629384](https://pubmed.ncbi.nlm.nih.gov/27629384/) | 2016 | Mechanistic/Genetic Study | J Thromb Haemost | Three-generational pedigree study demonstrating that co-existent damaging variants in FVIII and prostaglandin synthase-1 (PTGS-1/COX-1) amplify hemorrhage severity; PTGS-1 variant causes functional defects in the arachidonic acid platelet pathway, showing FVIII level interacts with platelet secretion-related pathways |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high score (99.96%) reflects graph-level proximity among hemophilia-spectrum bleeding disorders rather than direct therapeutic evidence. Available support consists of two genetic studies (L4), no registered clinical trials, and no Saudi Arabia regulatory standing — insufficient to advance this repurposing hypothesis.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept:** At least one in vitro or animal study specifically testing whether rFVIII-mediated thrombin amplification improves hemostasis in a platelet release disorder model
- **MOA documentation:** Retrieve complete FVIII mechanism of action and pharmacodynamic profile from DrugBank to enable formal mechanistic analysis
- **Safety dossier:** Obtain package insert warnings and contraindications (currently a Blocking data gap per DG001) before any clinical feasibility assessment
- **Case series search:** Conduct a targeted literature search for cases where rFVIII was used off-label in patients with combined FVIII deficiency and platelet secretion defects, which may provide real-world mechanistic clues
- **Comparator assessment:** Evaluate whether established rescue therapies for platelet release disorders (e.g., desmopressin, platelet transfusion) leave an unmet need that rFVIII could address

> **Note on a higher-priority candidate:** Among all eight predicted indications, **Acquired Coagulation Factor Deficiency (rank 4, evidence level L2)** carries substantially stronger evidence — 5 clinical trials (including Phase 2/3 completed studies of recombinant porcine FVIII in acquired hemophilia A) and 20 publications, with guideline support from UKHCDO/ISTH for human rFVIII use in low-titer inhibitor patients. This indication warrants a separate **Proceed with Guardrails** evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

