---
layout: default
title: Ciprofibrate
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Ciprofibrate
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

# Ciprofibrate: From Dyslipidemia to Hyperlipoproteinemia

## One-Sentence Summary

Ciprofibrate is a fibric acid derivative (PPAR-α agonist) with established lipid-lowering efficacy approved in multiple European markets, but currently not registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia** with a confidence score of **99.97%**,
supported by **0 registered clinical trials** and **20 peer-reviewed publications** spanning 1982–2007, including comparative RCTs and large multicenter studies directly validating its efficacy across Type IIa, IIb, and IV hyperlipoproteinemia subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia; pharmacologically classified as a lipid-lowering agent (fibrate class) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, ciprofibrate belongs to the fibric acid derivatives (fibrate class) and acts as a **PPAR-α (peroxisome proliferator-activated receptor alpha) agonist**. This mechanism activates lipoprotein lipase (LPL), inhibits apolipoprotein C-III (apoC-III) synthesis, promotes HDL production, and reduces VLDL secretion — directly targeting multiple lipid metabolic pathways that are dysregulated in hyperlipoproteinemia. The near-perfect TxGNN score (99.97%) reflects this tight mechanistic alignment between the drug's pharmacology and the target indication within the knowledge graph.

Ciprofibrate has been approved and clinically used in European markets (including France, the United Kingdom, and Czech Republic) under the brand name Lipanor® for several decades. The three main subtypes of atherogenic hyperlipoproteinemia it addresses — Type IIa hypercholesterolemia, Type IIb combined hyperlipidemia, and Type IV hypertriglyceridemia — represent the core mechanistic targets of fibrate therapy. At the standard dose of 100 mg/day, ciprofibrate produces significant reductions in total cholesterol, LDL-C, triglycerides, VLDL, and apolipoprotein B, while raising HDL-C and apolipoprotein A-I levels. A Czech multicenter study (n = 633) demonstrated cholesterol reductions of 13%, triglyceride reductions of over 41%, and HDL-C increases of 15% at three months.

Beyond lipid parameters, the supporting literature also documents pleiotropic cardiovascular benefits consistent with PPAR-α agonism: reductions in circulating fibrinogen, improvements in endothelial function (flow-mediated dilation), and modulation of adhesion molecules (sVCAM-1, sICAM-1, E-selectin). The breadth and consistency of this evidence base across four decades and multiple patient populations make the prediction highly credible. The key constraint for Saudi Arabia is the absence of local regulatory registration, not the absence of clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the hyperlipoproteinemia indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9015467](https://pubmed.ncbi.nlm.nih.gov/9015467/) | 1996 | Comparative RCT | Postgraduate Medical Journal | Multicenter open parallel-group RCT (n=174): ciprofibrate 100 mg/day vs. sustained-release bezafibrate 400 mg/day in Type II hyperlipidemia over 8 weeks; both agents significantly reduced LDL-C and total cholesterol with comparable efficacy and tolerability |
| [6753860](https://pubmed.ncbi.nlm.nih.gov/6753860/) | 1982 | RCT (Double-blind) | Atherosclerosis | Randomized placebo-controlled double-blind trial of ciprofibrate 50 or 100 mg/day in Type II hypercholesterolemia (n=20 completers); significant lipid reductions at both doses, well tolerated throughout the 12-week treatment period |
| [8831920](https://pubmed.ncbi.nlm.nih.gov/8831920/) | 1996 | Clinical Trial | Atherosclerosis | Large-scale efficacy and safety review of ciprofibrate 100 mg/day in approximately 3,000 patients across Type IIa, IIb, and IV hyperlipoproteinemia; significant reductions in TC, TG, LDL-C, and apoB alongside HDL-C increases confirmed across all subtypes |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | Comparative Trial | Atherosclerosis | Double-blind 3-month head-to-head comparison: ciprofibrate 100 mg (single daily dose) vs. fenofibrate 300 mg (three daily doses); both significantly reduced TC, LDL-C, VLDL-C, and apoB (p<0.001) and increased HDL-C (p<0.01) and total apoA (p<0.05) |
| [2289217](https://pubmed.ncbi.nlm.nih.gov/2289217/) | 1990 | Multicenter Clinical Trial | Clinical Therapeutics | Italian multicenter study (n=127, 23 centers): diet-resistant Type IIa/IIb/IV hyperlipidemic patients receiving ciprofibrate 100 mg/day for 12 weeks; significant improvement in all lipid parameters including significant apoB reduction and apoA-I increase |
| [11048518](https://pubmed.ncbi.nlm.nih.gov/11048518/) | 2000 | Multicenter Clinical Trial | Vnitrni Lekarstvi | Czech multicenter study (n=633, 23 centers): combined hyperlipoproteinemia patients on ciprofibrate 100 mg/day for 3 months; cholesterol −13%, triglycerides −41%, HDL-C +15%, LDL-C significantly decreased |
| [12915663](https://pubmed.ncbi.nlm.nih.gov/12915663/) | 2003 | Clinical Study | Journal of Clinical Endocrinology & Metabolism | Ciprofibrate 100 mg/day in Type IIb hyperlipoproteinemia (n=10): marked reduction of large VLDL-1 (−40%, p=0.001) and small VLDL-2 (−25%); improved HDL-mediated cellular cholesterol efflux, demonstrating beneficial modulation of atherogenic lipoprotein phenotype |
| [15547649](https://pubmed.ncbi.nlm.nih.gov/15547649/) | 2004 | Clinical Study | Angiology | Ciprofibrate therapy reduced soluble VCAM-1, ICAM-1, and E-selectin in obese dyslipidemic men with and without Type 2 diabetes, demonstrating anti-inflammatory pleiotropic effects relevant to atherosclerosis prevention |
| [17414592](https://pubmed.ncbi.nlm.nih.gov/17414592/) | 2007 | Clinical Study | American Journal of Therapeutics | Ciprofibrate significantly decreased non-HDL cholesterol and triglycerides while increasing HDL-C in patients with Frederickson Type IV dyslipidemia phenotype, confirming efficacy specifically in the hypertriglyceridemia-predominant subtype |
| [3318453](https://pubmed.ncbi.nlm.nih.gov/3318453/) | 1987 | Review | American Journal of Medicine | Systematic 7-year literature review of fibric acid derivatives (bezafibrate, ciprofibrate, fenofibrate): confirms consistent lipid-lowering effects of ciprofibrate across Type IIA, IIB, and IV hyperlipoproteinemia; positions ciprofibrate within the fibrate class comparative evidence base |

---

## Saudi Arabia Market Information

Ciprofibrate is currently **not registered** in Saudi Arabia. No marketing authorizations are on file (0 licenses). Registration through the SFDA would be a prerequisite before clinical deployment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Full safety data (package insert warnings, contraindications, drug interactions) were not available in this evidence pack. Before proceeding with any regulatory submission or clinical use, the following safety domains should be prioritized for data collection: hepatotoxicity monitoring, myopathy risk (particularly with concurrent statin use), dose adjustment in renal impairment, cholelithiasis risk inherent to fibrate class, and anticoagulant interaction (fibrates are known to potentiate warfarin effects via protein-binding displacement and CYP modulation).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ciprofibrate's efficacy in hyperlipoproteinemia is supported by a robust and consistent body of literature across four decades, including multiple comparative RCTs and large multicenter studies involving thousands of patients. The primary barrier to deployment in Saudi Arabia is the absence of local SFDA registration and formal safety documentation — not a lack of clinical evidence.

**To proceed, the following is needed:**
- Compile a complete regulatory dossier for SFDA registration application, drawing on existing European approval data (Lipanor® authorizations)
- Obtain and review the full prescribing information (package insert) to document contraindications, warnings, and precautions — currently missing from the evidence pack
- Confirm drug interaction profile, particularly with anticoagulants (warfarin), statins (myopathy risk with combination therapy), and cyclosporine
- Establish a local monitoring protocol: liver function tests (AST/ALT), renal function (eGFR), and creatine kinase (CK) at baseline and at regular intervals
- Define patient selection criteria aligned with approved European subtypes (Type IIa, IIb, IV hyperlipoproteinemia) and exclusion criteria (severe hepatic or renal impairment, cholelithiasis, pregnancy)
- Assess post-marketing safety reports from European markets for any emerging signals not captured in the pre-2010 literature base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

