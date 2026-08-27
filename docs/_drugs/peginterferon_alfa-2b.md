---
layout: default
title: Peginterferon Alfa-2B
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 7
---

# Peginterferon Alfa-2B
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

# Peginterferon Alfa-2b: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2b (DrugBank DB00022) is a pegylated type I interferon internationally known for treating chronic viral hepatitis, though no Saudi Arabia (SFDA) marketing record or approved-indication text is currently on file for it. The TxGNN model's top prediction is **Hepatitis B Virus Infection**, with **50 linked clinical trials** and **19 PubMed publications** in the evidence pool — though it should be noted this predicted use substantially overlaps with the drug's already-established role in **chronic hepatitis B**, which the evidence pack lists separately (rank 7) with the same underlying evidence base.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in SFDA licensing data (drug not marketed); internationally recognized use is chronic hepatitis C/B treatment |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this record is marked as a data gap. However, based on well-established pharmacology captured elsewhere in this evidence pack (see the drug's rank-7 "chronic hepatitis B virus infection" entry), peginterferon alfa-2b is a type I interferon that binds IFNAR1/IFNAR2 receptors to activate the JAK-STAT pathway, inducing interferon-stimulated genes (ISGs) that directly suppress viral replication while also enhancing host immune clearance of cccDNA-infected hepatocytes. This is the accepted standard mechanism behind interferon-based HBV therapy, not a newly hypothesized pathway.

Because this mechanism is disease-agnostic within the hepatitis virus family, and because peginterferon alfa-2b already has a substantial evidence base in chronic hepatitis B (see rank 7 in this same evidence pack), the model's prediction of "Hepatitis B Virus Infection" is mechanistically coherent. Importantly, the evidence pack's own rationale flags that TxGNN appears to have split the HBV disease ontology into separate "acute/general" and "chronic" nodes, and that this rank-1 prediction and the rank-7 "chronic hepatitis B virus infection" prediction are, in practice, the same clinical indication. This means the finding should be read less as discovery of a genuinely novel use and more as confirmation of an already well-documented pharmacological role — which strengthens confidence in the underlying biology but reduces its value as a *repurposing* opportunity per se.

It is also worth noting that the underlying clinical trial dataset is noisy: a meaningful share of the 50 linked trials (e.g., taribavirin/ribavirin dose-finding studies, boceprevir triple-therapy trials) are HCV-focused rather than HBV-focused and have been graded "C" (low relevance) in the reviewer's own relevance assessment. The trials selected below were filtered toward those explicitly describing HBV-directed regimens.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05182463](https://clinicaltrials.gov/study/NCT05182463) | Phase 4 | Recruiting | 5000 | Real-world "E-Cure" study of peginterferon alfa-2b in inactive chronic hepatitis B patients |
| [NCT05792761](https://clinicaltrials.gov/study/NCT05792761) | N/A | Unknown | 1900 | "Sprout Project" — antiviral treatment strategies for chronic hepatitis B in children |
| [NCT06196632](https://clinicaltrials.gov/study/NCT06196632) | N/A | Unknown | 1000 | Logistic regression models to predict durable functional cure after peginterferon alfa-2b-based therapy in CHB |
| [NCT07071636](https://clinicaltrials.gov/study/NCT07071636) | Phase 4 | Not yet recruiting | 830 | Peginterferon alfa-2b + nucleos(t)ide analogues in CHB with/without MASLD |
| [NCT03181113](https://clinicaltrials.gov/study/NCT03181113) | N/A | Completed | 473 | Long-term benefit assessment in HBeAg-positive CHB patients previously treated with standard peginterferon alfa |
| [NCT01641926](https://clinicaltrials.gov/study/NCT01641926) | Phase 3 | Terminated | 402 | Head-to-head safety/efficacy of PEG-Intron vs. PEGASYS in HBeAg-positive and -negative CHB |
| [NCT06707922](https://clinicaltrials.gov/study/NCT06707922) | N/A | Enrolling by invitation | 350 | Long-term benefit of peginterferon alfa-2b combined with tenofovir (TDF) in CHB |
| [NCT07120750](https://clinicaltrials.gov/study/NCT07120750) | N/A | Not yet recruiting | 332 | Evaluates whether peginterferon alfa-2b reduces recurrence of HBV-related liver cancer after radical treatment |
| [NCT02327416](https://clinicaltrials.gov/study/NCT02327416) | Phase 3 | Unknown | 300 | "Anchor Study" — sequential peginterferon alfa-2b + entecavir + GM-CSF in NA-experienced CHB |
| [NCT00146705](https://clinicaltrials.gov/study/NCT00146705) | N/A | Completed | 266 | Long-term follow-up of peginterferon alfa-2b with/without lamivudine in chronic HBV infection |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25200354](https://pubmed.ncbi.nlm.nih.gov/25200354/) | 2014 | RCT | Journal of Clinical Virology | Randomized trial of peginterferon alfa-2b in Chinese HBeAg-positive chronic hepatitis B patients |
| [41366186](https://pubmed.ncbi.nlm.nih.gov/41366186/) | 2026 | RCT | Hepatology International | "Anchor" randomized controlled trial of entecavir + peginterferon alfa-2b ± GM-CSF for HBsAg loss in CHB |
| [17604363](https://pubmed.ncbi.nlm.nih.gov/17604363/) | 2007 | RCT | Hepatology | Peginterferon alfa-2b (± lamivudine) shown safe and effective in HBeAg-positive CHB with advanced fibrosis |
| [16167968](https://pubmed.ncbi.nlm.nih.gov/16167968/) | 2005 | Systematic Review | Alimentary Pharmacology & Therapeutics | Systematic review of pegylated interferon for chronic hepatitis B treatment |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Overview of hepatitis B treatment goals and response monitoring |
| [27190319](https://pubmed.ncbi.nlm.nih.gov/27190319/) | 2016 | Review | Clinical Infectious Diseases | Virus and host biomarker testing to guide chronic HBV management |
| [40390028](https://pubmed.ncbi.nlm.nih.gov/40390028/) | 2025 | Cohort | Virology Journal | Multicenter pilot study of recurrence risk factors after peginterferon alfa-2b-induced functional cure |
| [38089868](https://pubmed.ncbi.nlm.nih.gov/38089868/) | 2023 | Cohort | Frontiers in Medicine | Simple scoring system predicting HBsAg clearance with peginterferon alfa-2b in NA-experienced CHB |
| [24738850](https://pubmed.ncbi.nlm.nih.gov/24738850/) | 2014 | Review | Expert Opinion on Biological Therapy | Review of peginterferon alfa in chronic hepatitis B treatment, including super-/null-responder identification |
| [39176265](https://pubmed.ncbi.nlm.nih.gov/39176265/) | 2024 | Cohort | Frontiers in Cellular and Infection Microbiology | Peginterferon alfa-2b induces high functional cure rate in postpartum HBeAg-negative women with CHB |

---

## Saudi Arabia Market Information

Peginterferon alfa-2b currently holds no marketing authorization on record in Saudi Arabia (0 licenses; market status "Not Marketed"), so no product/dosage-form table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No SFDA warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query returned "not found").

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (established IFN alfa antiviral/immunomodulatory action against HBV) and is backed by an L1 evidence level, including multiple Phase 3/4 trials and large real-world cohorts (e.g., n=5,000 E-Cure study). However, the prediction largely restates the drug's already-known role in chronic hepatitis B (compare rank 7 in this same evidence pack) rather than identifying a distinct new indication, and the drug is not currently marketed or licensed in Saudi Arabia, so no local safety labeling exists yet.

**To proceed, the following is needed:**
- SFDA/TFDA package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source
- Clarification of whether "Hepatitis B Virus Infection" (rank 1) should be merged with "chronic hepatitis B virus infection" (rank 7) as a single candidate, since they appear to reflect the same TxGNN-split disease node
- Drug-drug interaction data (current query status: not found)
- A regulatory pathway assessment given the drug has no existing Saudi Arabia market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

