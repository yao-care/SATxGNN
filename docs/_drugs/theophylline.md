---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 614
evidence_level: L5
indication_count: 7
---

# Theophylline
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

# Theophylline: From Bronchodilator Therapy to Thrombotic Disease

## One-Sentence Summary

Theophylline is a methylxanthine historically used as a bronchodilator for asthma and COPD, though Saudi Arabia-specific licensing and mechanism-of-action records are currently unavailable in this dataset. The TxGNN model predicts it may also be effective for **Thrombotic Disease**, but this direction is currently supported by **0 clinical trials** and **19 publications**, nearly all of which are only tangentially related (platelet-detection methodology or unrelated drugs) rather than direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchodilator therapy for asthma/COPD (well-established pharmacological use; no Saudi Arabia-specific approved indication text on file) |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory record (Data Gap). Based on known pharmacology, theophylline is a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist of the methylxanthine class; its bronchodilator and anti-inflammatory efficacy in asthma and COPD is well established.

The proposed link to thrombotic disease rests on a shared second-messenger pathway: PDE inhibition raises intracellular cAMP, which relaxes airway smooth muscle in the respiratory context but, in platelets, elevated cAMP is associated with reduced platelet activation and aggregation — a mechanism analogous to cilostazol, an approved PDE3 inhibitor used for antiplatelet therapy. This makes the hypothesis mechanistically plausible in principle.

However, the retrieved literature does not actually substantiate this specific hypothesis. The 19 publications are largely methodological (platelet activation marker assays, sample-processing studies) or concern unrelated drugs/diseases, with no study directly evaluating theophylline's antithrombotic efficacy. As the underlying rationale itself notes, this remains a model-score-driven hypothesis (L5, no direct clinical or preclinical confirmation) rather than an evidence-backed candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Review of ticlopidine's antiplatelet pharmacokinetics; does not address theophylline |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Platelet/neutrophil activation by age and gender in Behçet's disease; no theophylline intervention |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Methodology | Cells | Effect of anticoagulation/sample processing on blood-derived microRNA signatures |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Review of prostaglandins/thromboxane/prostacyclin in platelet aggregation and atherosclerosis |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methodology | British Journal of Haematology | Radioimmunoassay for platelet factor 4; theophylline used only as an anticoagulant reagent additive |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Methodology | Platelets | Measurement of soluble CLEC-2 as a platelet activation marker for thrombotic risk detection |
| [197665](https://pubmed.ncbi.nlm.nih.gov/197665/) | 1977 | Review | Stroke | Review of brain edema classification and imaging in stroke; unrelated to theophylline |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflammatory Bowel Diseases | Platelet-leukocyte aggregate formation in IBD; no theophylline treatment arm |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Other | Analytica Chimica Acta | Electrochemical aptasensor for detecting theophylline concentration (analytical chemistry, not therapeutic) |
| [29956444](https://pubmed.ncbi.nlm.nih.gov/29956444/) | 2018 | Methodology | Journal of Thrombosis and Haemostasis | Differential exocytic cargo release from endothelial Weibel-Palade bodies; no theophylline intervention |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is high (99.62%), the evidence level is L5 — there are no registered clinical trials, and the retrieved literature does not directly support a theophylline–thrombotic disease link (it is largely methodological or concerns unrelated drugs). A blocking data gap (SFDA/TFDA package insert warnings and contraindications unavailable) also prevents even a baseline safety review.

**To proceed, the following is needed:**
- SFDA package insert data — warnings, precautions, and contraindications (Blocking gap, required before any S1 safety assessment)
- Confirmed original indication and mechanism-of-action (MOA) documentation from DrugBank or equivalent source
- Preclinical studies (e.g., platelet aggregation assays) directly testing theophylline's antithrombotic activity, rather than inference from cilostazol analogy
- If preclinical signal emerges, a targeted literature/clinical trial search specifically on "theophylline AND antiplatelet/thrombosis" rather than broad platelet-methodology hits
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

