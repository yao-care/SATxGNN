---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin is a synthetic form of vitamin B12, classically used to correct vitamin B12 deficiency, pernicious anemia, and megaloblastic anemia.
The TxGNN model predicts it may be effective for **Biotin Metabolic Disease**, with **15 clinical trials** and **20 publications** identified — though the vast majority provide only indirect mechanistic support, with no trials directly testing cyanocobalamin in this indication.
Overall evidence remains at a preclinical/mechanistic level, and this prediction is best understood as a research hypothesis rather than a clinical repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B12 deficiency / Pernicious anemia / Megaloblastic anemia |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cyanocobalamin is a stable, synthetic form of vitamin B12 (cobalamin). Once absorbed, it is converted in the body to two active cofactor forms: **methylcobalamin** (required for methionine synthase) and **adenosylcobalamin** (required for methylmalonyl-CoA mutase). The latter enzyme catalyses the conversion of methylmalonyl-CoA to succinyl-CoA — a critical step in the degradation of propionyl-CoA derived from odd-chain fatty acids, certain amino acids, and the gut microbiome.

This is precisely where the metabolic overlap with biotin becomes relevant. **Biotin** serves as the essential cofactor for propionyl-CoA carboxylase — the enzyme immediately upstream of methylmalonyl-CoA mutase — as well as for three other carboxylases (pyruvate carboxylase, acetyl-CoA carboxylase, 3-methylcrotonyl-CoA carboxylase). Biotin metabolic diseases — primarily **biotinidase deficiency** and **holocarboxylase synthetase deficiency** — impair all biotin-dependent carboxylases simultaneously, disrupting propionate catabolism at the step just before where cobalamin acts. Both deficiencies produce overlapping biochemical phenotypes: elevated propionylcarnitine, organic aciduria, metabolic acidosis, and hyperammonemia.

The TxGNN model's high prediction score (0.996) most likely reflects this high degree of shared metabolic nodes in the knowledge graph. However, this mechanistic adjacency does not constitute clinical evidence: the standard treatment for biotin metabolic diseases remains **biotin supplementation itself**, and no study has yet demonstrated that cyanocobalamin monotherapy corrects the primary enzymatic defect in biotinidase deficiency or holocarboxylase synthetase deficiency. This prediction is a biologically coherent hypothesis that warrants preclinical investigation.

---

## Clinical Trial Evidence

No clinical trials directly testing cyanocobalamin for biotin metabolic disease were identified. The trials listed below are the most mechanistically adjacent among those retrieved:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Randomized multicentre trial of carglumic acid in propionic acidemia and methylmalonic acidemia — organic acidemias sharing the same propionate pathway disrupted in biotin metabolic disease; includes B12-responsive MMA patients |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Terminated | 5 | Biotin + dietary fibre supplementation pre-bariatric surgery to improve gut microbiota; biotin was an active intervention agent, but trial terminated early (n=5) — insufficient data |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Cross-over study comparing natural (Panmol) vs synthetic vitamin B complex, including B12 and biotin together — provides indirect bioavailability data for co-administration |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin and mineral supplementation (including B vitamins) in Type 2 diabetic patients with neuropathy and nephropathy; explores B vitamin efficacy in a metabolic disease context |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal patch delivery of vitamins (including B12 and biotin) in post-bariatric surgery patients; focuses on absorption route rather than disease treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Mechanistic review explicitly linking VitB12 as cofactor for both succinyl-CoA synthesis from methylmalonyl-CoA **and** biotin; characterises molecular overlaps in B12 deficiency states |
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Comprehensive review of vitamin-responsive disorders covering cobalamin, folate, **and biotin** together; covers inborn errors of cobalamin and biotin metabolism side-by-side |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Case series | Pediatric Research | In vivo ¹³C-propionate metabolism in patients with propionic acidemia, B12-responsive methylmalonic acidemia, and **multiple carboxylase deficiency** — directly demonstrates cobalamin and biotin pathway intersection in the same study population |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | Foundational review of megavitamin-responsive aminoacidopathies; articulates the cofactor therapy rationale for B-vitamin dependency syndromes including B12-responsive MMA |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | Systematic review of vitamin-responsive inborn errors of metabolism; covers both cobalamin and biotin-dependent enzyme defects |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases — reviews pharmacological vs nutritional dosing in vitamin dependency syndromes; mechanistically relevant |
| [7004517](https://pubmed.ncbi.nlm.nih.gov/7004517/) | 1980 | Review | Birth Defects Orig Art Series | Enzyme manipulation via specific megavitamin therapy in inborn errors of metabolism — discusses cofactor supplementation strategies including B12 and biotin |
| [5011556](https://pubmed.ncbi.nlm.nih.gov/5011556/) | 1972 | Review | Medical Journal of Australia | Early description of vitamin dependency syndromes; historical basis for cofactor therapy in B-vitamin responsive metabolic disorders |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Japanese review of vitamin dependency syndromes including B12 and biotin related conditions |
| [4609643](https://pubmed.ncbi.nlm.nih.gov/4609643/) | 1974 | Review | Clinics in Endocrinology & Metabolism | Foundational review of inborn errors of organic acid metabolism — propionate pathway disorders that underpin both B12-responsive MMA and biotin metabolic disease |

---

## Saudi Arabia Market Information

Cyanocobalamin currently has **no SFDA-approved products** registered in Saudi Arabia. The drug is not marketed in this market, and no authorisation records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model identifies a biologically coherent mechanistic link between cyanocobalamin and biotin metabolic disease via their shared role in the propionate degradation pathway, all identified evidence is indirect and mechanistic (L4). No clinical trial has directly evaluated cyanocobalamin in patients with biotinidase deficiency or holocarboxylase synthetase deficiency, and the established standard of care for these conditions is biotin itself — not cobalamin.

**To proceed, the following is needed:**

- **Preclinical validation**: Cell or animal model studies directly testing whether cyanocobalamin (or adenosylcobalamin) supplementation improves outcomes in biotin-deficient or biotinidase-deficient states
- **Patient subgroup identification**: Identify patients with biotin metabolic disease who co-present with cobalamin pathway dysfunction (e.g., elevated methylmalonic acid) — this subgroup would be the most logical target
- **MOA data**: Retrieve full mechanism of action from DrugBank (flagged as DG002) to confirm adenosylcobalamin's specific enzymatic role in this disease context
- **Safety profile**: Download and parse the SFDA/TFDA package insert (flagged as DG001) to complete the safety assessment before any clinical planning
- **Regulatory pathway**: Since cyanocobalamin is not marketed in Saudi Arabia, any clinical development would require de novo registration in addition to indication expansion — a significant regulatory burden to factor into the go/hold decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

