---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibric-acid derivative internationally used to treat hyperlipidemia and mixed dyslipidemia (elevated triglycerides, low HDL), though it is not currently marketed in Saudi Arabia and no local approved-indication text is on file. The TxGNN model's top-ranked prediction for this drug is **Homozygous Familial Hypercholesterolemia (HoFH)**, but the supporting evidence is thin: **1 clinical trial** (studying a different drug, alirocumab, in an overlapping patient population) and **11 publications**, mostly guidelines/reviews rather than fenofibrate-specific HoFH trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Saudi Arabia license text on file (drug not marketed locally); internationally established for hyperlipidemia/mixed dyslipidemia as diet adjunct |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on known pharmacology, fenofibrate is a PPAR-alpha agonist that upregulates lipoprotein lipase (LPL) and lowers apoC-III, producing its well-established effects: substantial triglyceride reduction and moderate HDL elevation, with a comparatively modest effect on LDL-C.

Homozygous Familial Hypercholesterolemia is caused by near-complete loss of LDL-receptor function, so LDL clearance is almost entirely receptor-dependent. Since fenofibrate's PPAR-alpha/LPL mechanism does not restore LDL-receptor activity, its LDL-lowering effect in HoFH patients is expected to be limited. Standard HoFH therapy relies on statins, PCSK9 inhibitors, lomitapide, and LDL apheresis — fenofibrate is, at best, a theoretical adjunct rather than a primary mechanism match. This is consistent with the model's own evidence trail: the one linked trial studies alirocumab (a PCSK9 inhibitor), not fenofibrate, with only patient-population overlap, and the literature is dominated by general dyslipidemia guidelines and reviews rather than fenofibrate-specific HoFH data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of **alirocumab** (PCSK9 inhibitor, not fenofibrate) in children/adolescents (8–17y) with HoFH; evaluated LDL-C reduction at Week 12/24/48 on top of background lipid-lowering therapy. Relevance grade C — study drug differs from fenofibrate; only the patient population overlaps. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical (fenofibrate) | Pharmacological Research Communications | 22 type II hyperlipoproteinemia patients on fenofibrate 300mg/day; one HoFH patient showed the greatest fall in total/LDL cholesterol among the cohort. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK study | Pharmacotherapy | Characterizes pharmacokinetic interaction of lomitapide (approved HoFH adjunct) with commonly co-used lipid drugs including fenofibrate. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Notes fenofibrate monotherapy's most definite indication is severe hypertriglyceridemia (TG>500mg/dL); modest cardiovascular event reduction. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review/Case series | Internal Medicine Journal | Discusses liver transplantation for HoFH alongside emerging lipid-lowering therapies when standard drugs/apheresis are insufficient. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management and cardiovascular disease prevention guideline. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | Reviews pharmacologic/surgical treatment of dyslipidemic children and adolescents, including fenofibrate among agents used in familial hypercholesterolemia. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews statins and PCSK9 inhibitors for LDL-C reduction in severe hypercholesterolemia. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe, a selective cholesterol absorption inhibitor, as a non-statin lipid-lowering option. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology and therapeutic potential of atorvastatin in hyperlipidaemias. |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | Canadian Journal of Cardiology | Advances in dyslipidemia drug treatment, focused on atorvastatin. |

---

## Saudi Arabia Market Information

Fenofibrate is not currently marketed in Saudi Arabia — no authorization records are available (`market_status: 未上市`, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No key warnings, contraindications, or DDI data are currently on file — TFDA package insert data is flagged as a Blocking data gap, which also prevents a full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for fenofibrate in HoFH is Level L4 — mechanism-based reasoning only, with no direct fenofibrate trial or literature data in this indication. The single linked trial evaluates a different drug (alirocumab), and HoFH's near-total LDL-receptor loss is not well-addressed by fenofibrate's PPAR-alpha/LPL mechanism.

**To proceed, the following is needed:**
- Fenofibrate-specific clinical data (trial or observational) in confirmed HoFH patients, ideally as add-on to standard therapy (statin/PCSK9i/lomitapide/apheresis)
- TFDA/Saudi package insert warnings and contraindications (currently Blocking data gap — required before any S1 safety screening)
- Detailed mechanism of action (MOA) data from DrugBank (currently High-severity data gap)
- Note: within this same evidence pack, the rank-2 candidate **hyperlipoproteinemia** already carries L1-level evidence (multiple completed Phase 3 fenofibrate RCTs) and a "Proceed with Guardrails" recommendation — if the strategic goal is any lipid-indication expansion for fenofibrate, that candidate is substantially more actionable than HoFH.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

