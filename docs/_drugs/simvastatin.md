---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 575
evidence_level: L5
indication_count: 8
---

# Simvastatin
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a well-established HMG-CoA reductase inhibitor (statin) used to treat hypercholesterolemia and dyslipidemia. The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**, a genetically-driven subtype of hypercholesterolemia, with **19 clinical trials** and **18 publications** currently supporting this direction. Because statins — including simvastatin — are already guideline-recommended first-line therapy for FH, this prediction largely confirms existing standard-of-care rather than identifying a genuinely novel use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (well-established statin indication; formal regulatory indication text not available in this evidence pack) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug record is not available. Based on established pharmacological knowledge, simvastatin is a member of the statin (HMG-CoA reductase inhibitor) class; its efficacy in hypercholesterolemia has been proven for decades, and mechanistically it is directly applicable to familial hypercholesterolemia.

Simvastatin inhibits HMG-CoA reductase, blocking hepatic cholesterol biosynthesis and upregulating LDL receptor expression on hepatocytes. This is the core pharmacological mechanism for treating FH, a condition caused by mutations in LDLR, APOB, or PCSK9 that impair LDL clearance. Because the mechanism directly targets the pathway disrupted in FH, statin therapy (including simvastatin) is already embedded in standard-of-care guidelines for this population — this is not a speculative repurposing signal but a confirmation of established clinical practice, which explains the very high TxGNN score and the depth of Phase 3 evidence available.

The distinction worth noting for decision-makers: the "new indication" here is a genetically-defined subtype of the drug's original indication class, not a mechanistically distant disease. Evidentiary strength is high, but strategic novelty is low.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heterozygous FH. |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg added to atorvastatin or simvastatin in homozygous FH; efficacy and safety evaluation. |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label extension of NCT03884452; long-term safety/tolerability of ezetimibe + simvastatin in homozygous FH. |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Randomized, double-blind study of ezetimibe + simvastatin vs. simvastatin alone in adolescents with heterozygous FH. |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Japanese post-marketing re-examination study of VYTORIN (ezetimibe/simvastatin) real-world safety and efficacy. |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | SUPREME trial: niacin ER + simvastatin vs. atorvastatin on HDL-C and lipid effects in hyperlipidemia/mixed dyslipidemia. |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in children/adolescents with homozygous FH on background statin therapy. |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2341 | Long-term safety of alirocumab added to background lipid-modifying therapy (including statins) in high-CV-risk hypercholesterolemia. |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab vs. placebo add-on to stable statin therapy in heterozygous FH or high-CV-risk hypercholesterolemia. |
| [NCT01617655](https://clinicaltrials.gov/study/NCT01617655) | Phase 3 | Completed | 107 | Alirocumab vs. placebo add-on to lipid-modifying therapy in heterozygous FH with LDL-C ≥160 mg/dL. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | 2026 ACC/AHA multi-society dyslipidemia management guideline, replacing the 2018 cholesterol guideline. |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial publication: simvastatin with/without ezetimibe in FH; effect of add-on therapy on atherosclerosis progression. |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin therapy associated with reduced coronary artery disease events and all-cause mortality in heterozygous FH. |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of statins, including simvastatin, for children with FH. |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefit-risk assessment of simvastatin in FH, supporting long-term tolerability for lifelong therapy. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice (AACE/ACE) | Clinical practice guideline for dyslipidemia management and cardiovascular disease prevention. |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in FH patients requiring long-term therapy. |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | Cohort | International Angiology | Long-term efficacy and safety of ezetimibe/simvastatin combination in FH patients. |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | RCT | Nutrition, Metabolism and Cardiovascular Diseases | Head-to-head comparison of atorvastatin vs. simvastatin for LDL-C goal attainment in heterozygous FH. |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | Journal of Clinical Medicine | Cross-sectional study of cellular immunity parameters in children with FH treated with simvastatin. |

---

## Saudi Arabia Market Information

Simvastatin is currently **not marketed** in Saudi Arabia under this evidence pack (0 registered authorizations, no license records available). No product/authorization table can be produced from current data.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were available in this evidence pack (SFDA/TFDA package insert retrieval is flagged as a **Blocking** data gap — see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 RCTs (e.g., ENHANCE, NCT03884452) directly evaluating simvastatin in FH populations, and the mechanism of action directly addresses the LDL receptor pathway defect underlying FH. However, this candidate is not currently marketed in Saudi Arabia, and core safety/label data (warnings, contraindications) are missing, which blocks a full safety review.

**To proceed, the following is needed:**
- SFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Formal mechanism of action documentation from DrugBank — currently a High-severity data gap (DG002)
- Saudi Arabia market registration/authorization status specific to simvastatin (confirm whether other statin brands cover this indication locally)
- Formal DDI screening, given simvastatin's known CYP3A4-mediated interaction risk (myopathy/rhabdomyolysis) with agents such as protease inhibitors and certain antifungals/macrolides
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

