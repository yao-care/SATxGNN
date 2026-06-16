---
layout: default
title: Doripenem
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 5
---

# Doripenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

The `txgnn-pipeline` skill covers technical pipeline management; report generation follows the system prompt template directly. Proceeding with the report now.

---

# Doripenem: From Serious Bacterial Infections to Hepatoportal Sclerosis

## One-Sentence Summary

Doripenem is a broad-spectrum carbapenem antibiotic originally used to treat serious hospital-acquired bacterial infections, including complicated intra-abdominal infections, complicated urinary tract infections, and hospital-acquired pneumonia.
The TxGNN model predicts it may be effective for **Hepatoportal Sclerosis**, but currently **0 clinical trials** and **0 publications** support this direction — placing this prediction at the lowest possible evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (complicated intra-abdominal infections, complicated urinary tract infections, hospital-acquired pneumonia) |
| Predicted New Indication | Hepatoportal Sclerosis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Doripenem belongs to the carbapenem class of β-lactam antibiotics. It works by covalently binding to penicillin-binding proteins (PBPs) — enzymes essential for bacterial cell wall cross-linking — thereby inhibiting cell wall synthesis and causing bacterial cell death. It is a last-resort antibiotic with broad coverage against gram-negative and gram-positive organisms, including many multidrug-resistant strains.

Hepatoportal sclerosis (also known as obliterative portal venopathy) is a rare vascular liver disease characterized by non-cirrhotic portal hypertension caused by obliteration of small portal vein branches, without an identifiable infectious trigger. The only theoretical bridge to an antibiotic is through the gut-liver axis: reducing intestinal bacterial load could in principle decrease bacterial translocation into the portal circulation, thereby lowering portal inflammatory burden. Animal model research on selective bowel decontamination (SBD) in hepatopulmonary syndrome has explored adjacent concepts, but nothing directly in hepatoportal sclerosis has ever been studied.

This predicted link is almost certainly non-pharmacological in origin. Hepatoportal sclerosis is not an infection-driven disease, Doripenem has no known vascular, anti-fibrotic, or anti-inflammatory mechanism, and the knowledge graph prediction score most likely reflects non-specific co-morbidity node linkages rather than a genuine drug-disease relationship. The same L5/Hold verdict applies uniformly to all five top-ranked predictions for this drug, all of which are rare hepatic or portal vascular conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Doripenem is not currently approved or marketed in Saudi Arabia. No authorizations were found in the SFDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for Doripenem are uniformly rated L5 (model prediction only, zero supporting clinical or preclinical evidence), and the top prediction — hepatoportal sclerosis — has no mechanistic plausibility beyond a highly speculative gut-liver axis hypothesis that has never been tested for this specific disease. Doripenem is also not registered in Saudi Arabia, adding a substantial regulatory hurdle before any clinical development could begin.

**To proceed, the following is needed:**

- Retrieve full MOA and toxicity profile from DrugBank (DB06211) and obtain SFDA package insert to assess key warnings and contraindications
- Commission a preclinical proof-of-concept study (animal model of non-cirrhotic portal hypertension) to test whether systemic carbapenem therapy reduces portal inflammatory markers — without this, there is no scientific basis to advance
- If the gut-decontamination hypothesis is the intended pathway, compare against orally non-absorbable antibiotics (e.g., rifaximin), which have more appropriate pharmacokinetics and existing hepatology evidence
- Reassess whether the TxGNN prediction cluster (all portal-vascular/hepatic rare diseases at identical scores) represents a genuine signal or a knowledge-graph artifact — consider flagging this drug for model calibration review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

