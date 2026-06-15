---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 2
---

# Biotin
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

# Biotin: From Nutritional Supplementation to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7) is a water-soluble B-complex vitamin essential for carboxylase enzyme function, traditionally used to correct biotin deficiency states.
The TxGNN model predicts it may be effective for **Dyspepsia**, with **2 clinical trials** and **7 publications** identified — though none directly evaluate biotin as a treatment for dyspepsia.
Overall evidence supporting this repurposing direction remains indirect and mechanistically speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Biotin deficiency (nutritional supplement; no formal regulatory indication found in this dataset) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the dataset. Based on known pharmacology, biotin is a coenzyme for four critical mitochondrial carboxylases — pyruvate carboxylase, acetyl-CoA carboxylase, propionyl-CoA carboxylase, and 3-methylcrotonyl-CoA carboxylase — all of which participate in fatty acid synthesis and energy metabolism. This energy-regulatory role is the mechanistic basis for TxGNN's prediction.

The repurposing rationale provided in this Evidence Pack suggests that biotin, by supporting carboxylase activity in intestinal epithelial cells, may help maintain the mucosal energy homeostasis that keeps gastrointestinal lining integrity intact. When biotin is deficient, gastrointestinal mucosal damage and digestive discomfort can occur — an observation documented in case reports. Additionally, intestinal flora are known to synthesize biotin endogenously, and supplementation may indirectly restore gut microbiome balance disrupted after *Helicobacter pylori* eradication therapy.

However, these mechanistic links are indirect inferences rather than established pharmacology. There are no controlled clinical studies demonstrating that biotin supplementation reduces dyspeptic symptoms in patients with adequate biotin status. The TxGNN graph-based model captures network-level associations that may not translate to direct therapeutic efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Observational study of serum micronutrient levels (including biotin) in post-bariatric surgery patients using transdermal patches. Dyspepsia was not a primary endpoint; relevance to biotin treatment of dyspepsia is very low. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | RCT comparing oxycodone vs. pregabalin for postoperative pain control. Contains no biotin component and is unrelated to dyspepsia; likely a database retrieval artefact. |

> **Note:** Both trials received a relevance grade of C. Neither trial was designed to evaluate biotin as a treatment for dyspepsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Study | Minerva Gastroenterologica e Dietologica | Open multicentric study evaluating a multi-ingredient supplement (sodium alginate, calcium carbonate, pineapple, papaya, ginger, α-galactosidase, fennel — brand name contains "Bioten") in functional dyspepsia post–H. pylori treatment. Biotin is not an isolated active ingredient; benefit cannot be attributed to biotin alone. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | The Journal of Dermatology | Infant diagnosed with dyspepsia as a neonate and fed amino acid formula developed biotin deficiency (alopecia, dermatitis). Serum and urine biotin below normal range. Demonstrates that dyspepsia context can accompany biotin deficiency, but does not support biotin as a dyspepsia treatment. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Clinical/Experimental | Experimental & Clinical Gastroenterology | Evaluated a prebiotic supplement (inulin, oligofructose, plus vitamins including biotin, zinc, selenium) for gut microbiota correction in pulmonary patients on antibiotics. Biotin is one of many co-ingredients; no isolated effect on dyspepsia assessable. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | International Journal of Molecular Medicine | Investigated stomach antral endocrine cells in IBS patients. No biotin component; retrieved as indirect association through GI endocrine pathophysiology. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World Journal of Gastrointestinal Endoscopy | Studied oxyntic mucosa endocrine cells in IBS patients. No biotin component; indirect GI mechanistic association only. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Immunohistochemical Study | Journal of Clinical Pathology | Examined IL-10 localisation in *H. pylori*–associated gastritis. No biotin component; retrieved as indirect GI inflammation context. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Research | Kidney International | Small bowel T cells and mucosal inflammation in IgA nephropathy patients. No biotin relevance; peripheral association only. |

---

## Saudi Arabia Market Information

No regulatory authorizations for Biotin were found in the Saudi Arabia dataset. The drug is currently classified as **Not Marketed** with zero registered licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score to biotin–dyspepsia, but the retrieved clinical evidence (2 trials, 7 publications) is entirely indirect — no study has evaluated biotin as a standalone intervention for dyspepsia in biotin-replete patients. Combined with zero Saudi Arabia authorizations and missing MOA and safety data, the current evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**

- **Mechanistic study**: Confirm whether biotin supplementation has measurable effects on gastric motility, mucosal energy metabolism, or enteric nervous system function in dyspepsia models
- **MOA data**: Retrieve full DrugBank mechanism of action entry (DG002 remediation)
- **Safety data**: Obtain package insert warnings and contraindications (DG001 remediation — currently Blocking)
- **Targeted literature search**: Re-query PubMed with stricter MeSH terms (Biotin AND functional dyspepsia AND randomized) to rule out missed trials
- **Proof-of-concept data**: At minimum, a prospective pilot study or mechanistic human study demonstrating biotin's effect on gastric function before advancing to Phase 2 design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

