---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Folic Acid: From Vitamin B9 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (vitamin B9) is a water-soluble B-vitamin classically used to treat and prevent folate deficiency; this evidence pack does not document a specific approved indication or mechanism of action. The TxGNN model predicts potential relevance to **Biotin Metabolic Disease**, but the **13 clinical trials** and **20 publications** identified are almost entirely general vitamin/nutrition studies rather than trials testing folic acid specifically in this disease — and the model's own rationale flags this as a likely category-proximity artifact rather than a validated mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no `original_indications` or license text available). Folic acid is broadly recognized as a treatment/prevention for folate deficiency — background knowledge, not sourced from this evidence pack. |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for folic acid in this evidence pack. Folic acid and biotin are both water-soluble B-group vitamins but participate in distinct metabolic pathways: folate is central to one-carbon metabolism and the methylation cycle, while biotin functions as an essential cofactor for carboxylase enzymes. Biotin metabolic disorders — such as biotinidase deficiency or holocarboxylase synthetase deficiency — are standardly treated with biotin supplementation itself, not folic acid.

The model's underlying rationale explicitly cautions that the high TxGNN score (99.49%) more likely reflects knowledge-graph proximity between "vitamin" and "metabolic disease" entity classes than a specific therapeutic mechanism connecting folic acid to biotin metabolic disease. No direct evidence in the supporting trials or literature demonstrates that folic acid treats or improves biotin metabolic disease. This prediction should therefore be treated as a hypothesis-generating signal rather than a clinically actionable finding.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | NA | Unknown | 200 | Cross-over RCT of Q10 ubiquinol + multivitamin B/E in autism (idiopathic and Phelan-McDermid syndrome); not disease- or drug-specific to folic acid/biotin metabolism |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1963 | General nutritional genomics platform studying diet-genome interactions; not disease-specific |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1000 | Fortified food vs. milk in malnourished children; measured serum/erythrocyte folic acid among several micronutrients, not a biotin metabolic disease trial |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption in post-bariatric surgery patients; general micronutrient deficiency, not biotin metabolic disease |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | NA | Completed | 39 | Targeted nutritional intervention for oxidative stress/methylation impairment in autism; not biotin metabolic disease |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment; intervention is iodine, not folic acid |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6824 | Universal newborn genomic screening (Baby Detect), may include biotinidase deficiency screening but is not a treatment trial |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation for neuropathy/nephropathy in type 2 diabetes; not biotin metabolic disease |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | NA | Completed | 40 | Multi-micronutrient intervention as palliative therapy in CHF; general nutritional support |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | NA | Completed | 202 | Multivitamin/mineral supplementation effect on impulsivity/aggression; not disease-specific |

All 10 trials above were graded "C" (low relevance) by the evidence review — none directly test folic acid as an intervention for biotin metabolic disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders including cobalamin, folate, biotin, B1 and E; folate and biotin are covered as distinct, separately-treated deficiency syndromes |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Reviews treatable inborn errors of metabolism, including biotin-responsive conditions, with movement disorder phenotypes |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Unclassified | Biologica Latina | Animal study inducing combined vitamin H (biotin) and folic acid deficiency via phthalylsulfathiazole diet; oldest direct biotin+folate co-deficiency evidence found |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Unclassified | Pediatric Clinics of North America | Reviews megavitamin-responsive aminoacidopathies, where B-complex vitamins act as coenzyme cofactors |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Unclassified | Advances in Human Genetics | Reviews vitamin-responsive inherited metabolic disorders broadly |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Unclassified | Ryoikibetsu Shokogun Shirizu | Reviews vitamin dependency syndromes |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Reviews vitamin involvement in metabolic diseases via malabsorption, metabolic errors, and vitamin-dependent syndromes |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterology Clinics of North America | Reviews vitamin/mineral deficiencies in IBD; not biotin metabolic disease-specific |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Molecular Sciences | Reviews B12 deficiency and nervous system effects; notes B12 as cofactor alongside biotin and folate in related biochemical reactions |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Unclassified | Archives de Pédiatrie | Reviews neonatal epilepsy secondary to inborn errors of metabolism, a category that includes biotin-responsive disorders |

No completed RCTs specific to folic acid in biotin metabolic disease were identified; all evidence above is review-level or historical animal/case literature.

## Saudi Arabia Market Information

Folic acid is currently **not marketed** in this jurisdiction (0 authorizations on record), so no product-level licensing table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no clinical trial or publication directly demonstrates folic acid efficacy in biotin metabolic disease, and the model's own mechanistic rationale attributes the score to vitamin/metabolic-disease category proximity rather than a validated pharmacological link. A Blocking data gap (missing package-insert warnings/contraindications) also prevents this candidate from entering the S1 safety review stage.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Verified mechanism of action data from DrugBank — currently a High-severity gap (DG002)
- Disease-specific studies testing folic acid directly in biotin metabolic disease patients (biotinidase deficiency, holocarboxylase synthetase deficiency), as none currently exist in the evidence base
- Independent mechanistic review to confirm or refute whether the TxGNN prediction reflects a real pharmacological relationship or a knowledge-graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

