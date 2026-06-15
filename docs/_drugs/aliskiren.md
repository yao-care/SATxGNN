---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 7
---

# Aliskiren
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

# Aliskiren: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Aliskiren is the first oral direct renin inhibitor (DRI), originally indicated for the treatment of primary hypertension in adults by blocking the rate-limiting enzyme of the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**,
with **0 clinical trials** and **20 publications** retrieved — however, none of the publications directly address aliskiren for this specific indication, placing this prediction at model-only (L5) evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (not registered in Saudi Arabia) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 — Model prediction only, no targeted studies |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the regulatory database for this report. Based on established pharmacology, aliskiren is a direct renin inhibitor — it binds to the active site of renin, blocking its cleavage of angiotensinogen to angiotensin I, and thereby reducing the downstream production of angiotensin II and aldosterone. This upstream blockade of the entire RAAS cascade distinguishes it from ACE inhibitors and ARBs, which act at later steps in the same pathway. Its approved use in hypertension reflects this mechanism.

The theoretical connection between aliskiren and pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH) is, however, weak. The dominant pathophysiological drivers in Group 3 PH are hypoxic pulmonary vasoconstriction (HPV), HIF-1α pathway activation, endothelin-1/nitric oxide imbalance, and progressive pulmonary vascular remodeling — pathways in which RAAS plays a peripheral rather than central role. While angiotensin II does exert some vasoconstrictive effect in the pulmonary vasculature, it is not the rate-limiting driver of hypoxia-induced right-sided pressure elevation. RAAS blockade alone is unlikely to meaningfully reverse HIF-1α–driven remodeling.

The 20 publications retrieved from PubMed were identified via broad keyword association with "hypoxia" and represent general background literature on hypoxia biology in neurological, oncological, and physiological contexts. None specifically investigates aliskiren in pulmonary hypertension. The high TxGNN score therefore reflects graph-network inference from disease-drug structural similarity rather than direct experimental evidence, and should be interpreted as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ The publications below were retrieved by hypoxia-related keyword matching. None directly investigates aliskiren for pulmonary hypertension owing to lung disease and/or hypoxia — they provide general mechanistic background on hypoxia pathophysiology only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Describes the four core mechanisms of hypoxemia (V/Q mismatch, shunt, hypoventilation, low FiO₂); foundational reference for understanding Group 3 PH pathophysiology |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Summarizes how hypoxia drives angiogenesis, metabolic reprogramming, pH homeostasis, and vascular disease; contextualizes HPV and downstream remodeling |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Reviews therapeutic strategies modifying tumor hypoxia; discusses why HIF-1α activation confers resistance — applicable reasoning for Group 3 PH mechanisms |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Explores the HIF axis in innate immunity and inflammatory hypoxia; relevant to pulmonary vascular inflammatory remodeling in chronic lung disease |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Reviews dual protective/injurious role of hypoxia across organ systems; discusses systemic consequences of pulmonary hypoxemia |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Molecular mechanisms of acute and chronic hypoxia-induced dysfunction; provides biochemical context for chronic hypoxia sequelae |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Deubiquitinases regulate HIF-1α stability; discusses ubiquitin-proteasome control of hypoxia signaling — background for HIF-driven pulmonary remodeling |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hypoxia-vascular dysfunction interplay in multiple sclerosis; highlights how inflammatory hypoxia differs from ischemic hypoxia — relevant distinction for PH subtypes |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Commentary | Revista Médica del IMSS | Physiological acclimatization to hypobaric hypoxia at altitude; discusses morphological and genetic adaptations relevant to chronic hypoxemia models |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Science | Advanced Science | NAT10/HIF-1α positive feedback drives glycolysis in hypoxic cancer cells; illustrates how HIF-1α creates self-sustaining hypoxia tolerance — applicable to vascular cell biology |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical safety signal from published evidence**: The ALTITUDE trial (aliskiren in type 2 diabetes with cardiovascular or renal disease) was terminated early due to excess non-fatal strokes, hypotension, hyperkalemia, and acute kidney injury in patients receiving aliskiren combined with an ACE inhibitor or ARB. This combination is now contraindicated. Any repurposing study in patients with pulmonary disease and likely comorbid cardiovascular or renal conditions must explicitly evaluate dual RAAS blockade risk and screen for bilateral renal artery stenosis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-maximum TxGNN score (99.98%), the mechanistic connection between RAAS inhibition and Group 3 pulmonary hypertension is weak — the dominant pathology (HPV, HIF-1α, endothelin/NO imbalance) is not RAAS-driven — and no clinical trials or targeted literature support this specific indication, confirming L5 evidence status.

**To proceed, the following is needed:**

- Preclinical proof-of-concept in established Group 3 PH animal models (e.g., SU5416/hypoxia rat model or MCT model) to test whether renin inhibition modulates pulmonary vascular pressure
- Mechanistic studies clarifying whether RAAS contributes to HIF-1α activation or endothelin upregulation in chronic hypoxic lung disease
- Full MOA documentation from DrugBank to complete mechanistic gap analysis (DG002)
- SFDA/package insert safety data retrieval to complete S1 safety screening (DG001)
- Formal safety screening against renal function and cardiovascular comorbidity profile typical of Group 3 PH patients, given ALTITUDE trial risks

> **Higher-priority indications from this Evidence Pack**: **Malignant Renovascular Hypertension** (rank 4, L4 — strong RAAS mechanistic alignment) and **Cerebrovascular Disorder** (rank 7, L3 — 2 clinical trials including a Phase 2/3 MRI study, 13 publications, and direct animal neuroprotection data) demonstrate substantially better evidence and mechanistic fit. These indications are recommended for prioritization over the top-ranked TxGNN prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

