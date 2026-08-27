---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2a is a pegylated type I interferon originally developed as combination therapy (with ribavirin) for chronic hepatitis C. The TxGNN model predicts it may also be effective for **hepatitis B virus infection (chronic hepatitis B)**, a direction already supported by **50 clinical trials** and **20 publications**, including multiple completed Phase 3/4 RCTs — this is less a novel hypothesis than a well-established use that is not yet reflected in this market's regulatory registry.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C (interferon-based combination antiviral therapy; per trial records in evidence pack) |
| Predicted New Indication | Hepatitis B Virus Infection (Chronic Hepatitis B) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank mechanism-of-action record is not available (flagged as a High-severity data gap). Based on the pharmacological evidence assembled in this pack, peginterferon alfa-2a is a pegylated form of interferon alfa-2a that signals through the JAK-STAT pathway to induce interferon-stimulated genes (ISGs). In chronic hepatitis B, this activity suppresses HBV cccDNA transcription and enhances host immune-mediated clearance of infected hepatocytes — a mechanism that is already clinically established, particularly in HBeAg-positive disease.

Chronic hepatitis C and chronic hepatitis B are both viral hepatidities where interferon's broad antiviral/immunomodulatory activity is directly applicable, since the drug does not depend on virus-specific targets the way direct-acting antivirals do. In fact, peginterferon alfa-2a (marketed globally as Pegasys) is already an approved therapy for chronic hepatitis B in many jurisdictions; the "prediction" here largely reflects an indication that exists elsewhere but is not present in this market's regulatory dataset (0 local authorizations).

This is further reinforced by the depth of clinical evidence: multiple completed Phase 3 and Phase 4 randomized trials — including a landmark 2005 NEJM registration trial in HBeAg-positive CHB — establish HBsAg/HBeAg seroconversion and viral suppression as reproducible outcomes, giving this prediction an unusually strong evidentiary base compared to typical TxGNN candidates.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00291616](https://clinicaltrials.gov/study/NCT00291616) | Phase 4 | Completed | 52 | RCT comparing thymosin alpha 1 + peginterferon alfa-2a vs. peginterferon alfa-2a alone in HBeAg-positive CHB; determined optimal antiviral treatment duration |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Phase 2b | Completed | 76 | Single-arm add-on of Pegasys to nucleos(t)ide analogue therapy in HBeAg-negative genotype D CHB with stable HBV DNA suppression |
| [NCT01237496](https://clinicaltrials.gov/study/NCT01237496) | Phase 3 | Completed | 17 | Immunology substudy of Pegasys in HBeAg-negative CHB; longitudinal HBV-specific T-cell response analysis |
| [NCT02604823](https://clinicaltrials.gov/study/NCT02604823) | Phase 4 | Completed | 307 | Efficacy and safety of Pegasys in naive/interferon- or lamivudine-pretreated HBeAg-positive CHB patients |
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | PARC study: PEG-IFN + ribavirin vs. PEG-IFN monotherapy for 1 year in HBeAg-negative CHB |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | Peginterferon alfa-2a vs. adefovir dipivoxil in lamivudine-resistant HBeAg-positive CHB |
| [NCT01730508](https://clinicaltrials.gov/study/NCT01730508) | N/A (observational) | Completed | 978 | Multicenter prospective cohort of Pegasys use in Chinese HBeAg-negative CHB patients under real-world labeling |
| [NCT00927082](https://clinicaltrials.gov/study/NCT00927082) | Phase 4 | Completed | 383 | Long-term post-treatment follow-up (NEPTUNE study) of Pegasys in HBeAg-positive CHB |
| [NCT02201407](https://clinicaltrials.gov/study/NCT02201407) | N/A (observational) | Completed | 50 | PRO B study: real-world effectiveness of standard-of-care peginterferon alfa-2a in CHB |
| [NCT01519921](https://clinicaltrials.gov/study/NCT01519921) | Phase 4 | Completed | 150 | Efficacy and safety of Pegasys in treatment-naive vs. YMDD-mutant HBeAg-positive CHB patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | New England Journal of Medicine | Landmark registration trial: peginterferon alfa-2a ± lamivudine vs. lamivudine alone in HBeAg-positive CHB |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT | Hepatology | Entecavir + peginterferon alfa-2a combination in HBeAg-positive immune-tolerant CHB (pediatric) |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + peginterferon alfa-2a in HBeAg-positive immune-tolerant CHB (adult) |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review / IPD Meta-analysis | Antiviral Therapy | Individual-participant meta-analysis defining peginterferon stopping rules in CHB |
| [31064399](https://pubmed.ncbi.nlm.nih.gov/31064399/) | 2019 | Cohort | Virology Journal | Serum HBV RNA levels as predictor of HBeAg seroconversion during peginterferon therapy |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Overview of chronic HBV infection natural history and treatment options |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Review of hepatitis B treatment goals and response monitoring |
| [18220290](https://pubmed.ncbi.nlm.nih.gov/18220290/) | 2008 | RCT (large multinational Phase 3) | Hepatology | HBeAg/HBV DNA as outcome predictors during peginterferon alfa-2a therapy (n=271) |
| [33339708](https://pubmed.ncbi.nlm.nih.gov/33339708/) | 2021 | Cohort | Journal of the Formosan Medical Association | Virological/immunological predictors of long-term outcomes after peginterferon in HBeAg-negative CHB |
| [33720089](https://pubmed.ncbi.nlm.nih.gov/33720089/) | 2021 | RCT | Journal of Pediatric Gastroenterology and Nutrition | Peginterferon alfa-2a + lamivudine or entecavir in children with immune-tolerant CHB |

---

## Saudi Arabia Market Information

Peginterferon alfa-2a currently has **no market authorization on file in Saudi Arabia** (0 licenses recorded; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) — multiple completed Phase 3/4 RCTs, including a landmark NEJM registration trial, support peginterferon alfa-2a's efficacy in chronic hepatitis B, and this use is already an established indication for the product (Pegasys) in other markets. However, the drug is currently unregistered in Saudi Arabia and a formal safety/warnings dataset is missing, so this cannot yet clear a full S1 safety review.

**To proceed, the following is needed:**
- SFDA-equivalent package insert with warnings, precautions, and contraindications (currently a Blocking data gap)
- Confirmed DrugBank mechanism-of-action record
- Formal drug-drug interaction (DDI) review (current query returned no results)
- Confirmation of local market entry/registration pathway for this indication in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

