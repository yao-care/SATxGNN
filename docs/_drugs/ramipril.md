---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension to Pulmonary Hypertension Due to Lung Disease/Hypoxia

## One-Sentence Summary

Ramipril is a well-established angiotensin-converting enzyme (ACE) inhibitor used for hypertension and cardiovascular risk reduction. The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH)**, but this is currently supported by **0 clinical trials** and only **20 background/tangential publications**, none of which directly test ramipril in this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor) — specific approved-label text not present in this evidence pack |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap, DG002). Based on known pharmacology, ramipril is an ACE inhibitor that suppresses the renin-angiotensin-aldosterone system (RAAS), reducing systemic vascular resistance and vascular remodeling — the basis for its established use in hypertension and post-MI cardiovascular risk reduction (e.g., the HOPE trial).

WHO Group 3 pulmonary hypertension (due to lung disease and/or hypoxia) is mechanistically different from systemic hypertension: it is driven primarily by hypoxic pulmonary vasoconstriction and lung parenchymal remodeling, not by classical systemic RAAS activation. The rationale captured for this candidate is explicit on this point: ACE inhibition could theoretically reduce pulmonary vascular remodeling via RAAS suppression, but this is not the dominant pathway in Group 3 PH, and systemic blood-pressure lowering from ramipril could worsen right-ventricular perfusion in patients who are already hemodynamically compromised.

Given this weak and potentially risky mechanistic link, the absence of any disease-specific clinical or preclinical evidence, and the model's own L5/Hold classification, this prediction should be treated as a hypothesis-generating signal only, not a basis for clinical evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Reviews hypoxia's role in brain aging and neurodegeneration (Alzheimer's, Parkinson's); altitude/hypoxia exposure shows mixed effects on aging |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Reviews clinical evidence and molecular mechanisms of hypoxia-induced cognitive impairment |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Research | Advanced Science | Identifies a NAT10/SEPT9/HIF-1α feedback loop driving glycolysis and anti-angiogenic resistance under hypoxia in gastric cancer |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Reviews hypoxia-mediated regulation of growth, metabolism, and disease (vascular disease, inflammation, cancer) |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Reviews deubiquitinases (DUBs) regulating HIF stability under hypoxia in cancer |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Reviews mechanisms of hypoxemia, including V/Q mismatch and right-to-left shunt |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Reviews therapeutic strategies targeting tumor hypoxia and resistance to radiotherapy/immunotherapy |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Revista Médica del IMSS | Reviews hypobaric (altitude) hypoxia and physiological adaptation |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Review | Journal of Applied Physiology | Overview of hypoxia research directions (abstract not available in source) |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Reviews the role of hypoxia in multiple sclerosis pathology and symptoms |

**Note:** None of these publications specifically evaluate ramipril or pulmonary hypertension treatment — they are general hypoxia-biology literature returned by the search, consistent with the L5 (model-prediction-only) evidence rating.

---

## Saudi Arabia Market Information

Ramipril is not currently marketed in Saudi Arabia — 0 authorizations on record.

---

## Safety Considerations

Please refer to the package insert for safety information. (The TFDA/SFDA package insert — warnings, contraindications, and DDI data — is flagged as a blocking data gap, DG001, and must be resolved before any S1 safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no supporting clinical trials, only tangential background literature, and a mechanistic rationale that is explicitly weak and potentially risky (Group 3 PH is hypoxia-driven, not RAAS-driven, and systemic hypotension could worsen right-heart perfusion). Combined with an L5 evidence level and ramipril's current unmarketed status in Saudi Arabia, there is no basis to proceed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications, DDI) — currently a blocking gap (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Disease-specific preclinical or clinical studies of ACE inhibition in WHO Group 3 pulmonary hypertension
- If pursuing this drug further, consider re-prioritizing toward higher-evidence candidates in the same evidence pack (e.g., rank 10, cerebral artery occlusion, rated L2/Proceed with Guardrails) rather than this L5/Hold candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

