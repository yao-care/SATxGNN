---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 1
---

# Alpelisib
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

# Alpelisib: From PIK3CA-mutated Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a selective PI3Kα inhibitor used in the treatment of PIK3CA-mutated, hormone receptor-positive, HER2-negative advanced breast cancer.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension** with a score of 99.03%;
however, there are currently **0 directly relevant clinical trials** and **2 publications** — neither of which provides positive treatment evidence, and both actually present opposing safety signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PIK3CA-mutated HR+/HER2− advanced or metastatic breast cancer |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, alpelisib is a PI3Kα (phosphoinositide 3-kinase alpha) inhibitor. The PI3Kα/AKT/mTOR signalling pathway plays a role in vascular smooth muscle cell proliferation and endothelial dysfunction — both of which are implicated in pulmonary arterial remodelling. In theory, inhibiting PI3Kα could slow pathological remodelling of pulmonary vasculature, which is the mechanistic basis for the TxGNN prediction.

However, the available clinical and preclinical evidence points in the opposite direction. One published case report documents alpelisib-induced interstitial lung disease (ILD) in a breast cancer patient, indicating that the drug can cause direct pulmonary toxicity. A preclinical study further shows that PI3Kα pathway inhibition combined with doxorubicin leads to biventricular atrophy and right ventricular dysfunction — exactly the cardiac phenotype that is also seen in advanced pulmonary hypertension. These signals suggest that alpelisib may worsen, rather than relieve, the cardiopulmonary burden in this population.

The mechanistic hypothesis is therefore speculative, and the currently visible clinical signals are contradictory. Until dedicated mechanistic or early-phase clinical data specific to pulmonary hypertension become available, the prediction remains at the level of a model hypothesis only.

---

## Clinical Trial Evidence

The ClinicalTrials.gov search returned 1 result, but it was assessed as irrelevant (Relevance Grade C):

| Trial Number | Phase | Status | Enrollment | Assessment |
|-------------|-------|--------|-----------|------------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Real-world effectiveness study of ribociclib vs. alpelisib in HR+/HER2− advanced breast cancer. No pulmonary hypertension outcome assessed. Entered the result set due to keyword matching noise — provides no evidence for the predicted indication. |

> **No clinical trials directly evaluating alpelisib in pulmonary hypertension are currently registered.**

---

## Literature Evidence

Two publications were retrieved. Both are low-tier evidence, and notably, neither supports efficacy in pulmonary hypertension — they present cardiopulmonary safety concerns instead.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease (ILD) in a patient with advanced breast cancer. Demonstrates direct pulmonary toxicity as an adverse event of alpelisib — an opposing safety signal for repurposing to pulmonary hypertension. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical | J Am Heart Assoc | PI3Kα inhibition combined with doxorubicin causes biventricular atrophy and right ventricular dysfunction in animal models — a mechanism that may aggravate right heart strain in pulmonary hypertension patients. |

> ⚠️ **Both publications represent adverse effect evidence, not therapeutic evidence.** They do not support, and may actively undermine, the case for repurposing alpelisib in pulmonary hypertension.

---

## Cytotoxicity

Alpelisib is an antineoplastic drug (targeted kinase inhibitor, original indication: PIK3CA-mutated breast cancer).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα inhibitor |
| Myelosuppression Risk | Low (PI3K inhibitors are not primarily associated with significant myelosuppression; main dose-limiting toxicity is hyperglycaemia) |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting blood glucose / HbA1c (hyperglycaemia is the most common dose-limiting toxicity); liver function tests; pulmonary symptoms for ILD surveillance; skin assessment for rash |
| Handling Protection | Standard cytotoxic handling precautions apply per institutional policy |

> Note: Detailed toxicity data was not available in the current Evidence Pack. The above is based on drug class knowledge. Refer to the Piqray® (alpelisib) package insert for complete prescribing information.

---

## Safety Considerations

Based on the literature retrieved in this Evidence Pack, the following safety signals are relevant to this repurposing hypothesis:

- **Pulmonary Toxicity**: Alpelisib has documented cases of interstitial lung disease (ILD) as an adverse event (PMID 35730191). Repurposing in a population already experiencing pulmonary pathology (pulmonary hypertension) requires careful risk assessment.
- **Cardiac Risk**: Preclinical data show PI3Kα pathway inhibition may cause right ventricular atrophy and dysfunction (PMID 31039672), which is of particular concern in pulmonary hypertension patients who may already have compromised right heart function.

> Formal drug interaction data and package insert warnings were not available in this Evidence Pack. Please refer to the package insert for complete safety information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is currently at evidence level L5 (model prediction only), with no clinical trials targeting pulmonary hypertension, and the only available literature represents opposing safety signals — suggesting alpelisib may cause rather than treat pulmonary and right cardiac pathology.

**To proceed, the following is needed:**

- **MOA validation**: Obtain and confirm alpelisib's precise mechanism of action in the PI3Kα/AKT/mTOR pathway as it relates specifically to pulmonary vascular biology, not just oncology
- **Dedicated preclinical data**: Animal model studies evaluating alpelisib in established pulmonary hypertension models (e.g., monocrotaline or Sugen/hypoxia rat models) to determine net direction of effect
- **ILD and cardiac risk stratification**: A formal risk/benefit assessment addressing whether the known ILD and right ventricular toxicity risks are manageable or disqualifying in a PH patient population
- **Package insert review**: Retrieve TFDA and FDA package inserts to obtain complete contraindications, warnings, and drug interaction data (flagged as data gap DG001)
- **Regulatory pathway consultation**: Given 0 existing Saudi Arabia authorisations, an independent regulatory feasibility review is recommended before any further development investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

