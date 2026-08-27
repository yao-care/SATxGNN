---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 516
evidence_level: L5
indication_count: 9
---

# Pravastatin
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is an HMG-CoA reductase inhibitor (statin) whose established use is lowering LDL-cholesterol in hypercholesterolemia and dyslipidemia. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but the supporting evidence is thin and largely indirect — **1 clinical trial** (not testing pravastatin itself) and a handful of reviews/guidelines, so this signal should be treated as hypothesis-generating rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (general statin-class indication; not confirmed by a Saudi Arabia license record, as the product currently has no registered license there) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this Evidence Pack. Based on known pharmacology, pravastatin is a hydrophilic HMG-CoA reductase inhibitor that lowers hepatic cholesterol synthesis and upregulates LDL-receptor (LDLR) expression, thereby reducing circulating LDL-C. This mechanism is well-proven in hypercholesterolemia and has an established pediatric safety record, since pravastatin is not metabolized via CYP3A4 and has a comparatively favorable interaction profile among statins.

HoFH and general hypercholesterolemia sit on the same lipid-metabolism pathway, so the mechanistic link is plausible on its face. However, the evidence pack's own rationale flags an important limitation: HoFH patients have little or no functional LDL receptor activity, so a drug that works primarily by upregulating LDLR has intrinsically limited efficacy in this population. Clinically, statins (including pravastatin) are used in HoFH mainly as **background/adjunct therapy** alongside PCSK9 inhibitors, apheresis, or lomitapide, rather than as standalone treatment.

This means the prediction is directionally reasonable — pravastatin belongs in the HoFH treatment picture — but the strength of the signal reflects a supportive/background role rather than a primary new indication with independent efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor, not pravastatin) in children/adolescents with HoFH on top of background lipid-lowering therapy; confirms HoFH treatment landscape and unmet need but does not test pravastatin directly. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of statin use in children with familial hypercholesterolemia, including severe/homozygous cases; summarizes efficacy and long-term safety evidence. |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Cochrane Review | Cochrane Database Syst Rev | Earlier version of the same Cochrane review on statins in pediatric FH; forms part of the evidence base behind current guideline recommendations. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidemia management guideline placing statin therapy in the broader context of FH severity, including HoFH. |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (INTREPID) | Lancet HIV | Phase 4 RCT comparing pitavastatin vs pravastatin; while conducted in HIV patients rather than HoFH, it confirms pravastatin's low CYP450-mediated interaction potential relevant to statin selection in complex regimens. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Mechanistic/iPSC study | Stem Cell Res Ther | iPSC-derived, LDLR-deficient hepatocyte model used for CRISPR correction and FH modeling; supports the LDLR-pathway rationale mechanistically, though not statin-specific. |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Case study | Iran Biomed J | Identifies a novel LDLRAP1 splice-site variant causing FH; illustrates the genetic basis behind residual LDLR pathway function relevant to statin responsiveness. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Comparative statin review noting pravastatin's relative LDL-lowering potency versus rosuvastatin and other statins. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Review of ezetimibe as a cholesterol-absorption-inhibitor add-on, relevant to combination strategies used in severe FH including HoFH. |

---

## Saudi Arabia Market Information

Pravastatin currently has no registered market authorization in Saudi Arabia (market status: not marketed; total licenses: 0). No product-level license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for pravastatin in HoFH is plausible but limited — HoFH patients have minimal functional LDLR, so pravastatin's principal mechanism has restricted standalone efficacy and no direct pravastatin-in-HoFH trial exists. Evidence level is L3 (indirect/review-level), and the drug is not currently marketed in Saudi Arabia, so this candidate needs both clinical and regulatory groundwork before advancing.

**To proceed, the following is needed:**
- SFDA-approved package insert (warnings, contraindications) — currently a blocking data gap for the S1 safety review
- Confirmed mechanism-of-action documentation from DrugBank
- Pravastatin-specific HoFH clinical data (even as adjunct/background therapy alongside PCSK9 inhibitors, apheresis, or lomitapide)
- Drug-drug interaction data (current query returned no results)
- A market authorization pathway assessment for Saudi Arabia, since the product has no existing license there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

