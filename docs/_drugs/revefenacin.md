---
layout: default
title: Revefenacin
parent: 僅模型預測 (L5)
nav_order: 542
evidence_level: L5
indication_count: 2
---

# Revefenacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Revefenacin: From Unregistered Status in Saudi Arabia to Predicted Efficacy in Bronchitis

## One-Sentence Summary

Revefenacin is a nebulized long-acting muscarinic antagonist (LAMA); it is not currently registered or marketed in Saudi Arabia, but is globally established (e.g. FDA-approved 2018) as a maintenance therapy for chronic obstructive pulmonary disease (COPD).
The TxGNN model's top-ranked new signal predicts it may also be effective for **Bronchitis**, but this is currently supported by only **1 clinical trial** (shared with the COPD/obstructive-lung-disease indication, not bronchitis-specific) and **0 dedicated publications**.
A second, much stronger signal — **Obstructive Lung Disease** (essentially the drug's already-established COPD indication) — is separately supported by **15 clinical trials** (including two completed Phase 3 pivotal RCTs, n=619 and n=611) and **20 publications**; this is noted below as important context even though it is not the primary "new indication" story.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Saudi Arabia (0 authorizations); per literature evidence in this pack, revefenacin is globally approved for maintenance treatment of COPD |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured MOA data for this candidate is marked as a data gap, but the literature evidence included in this pack consistently documents revefenacin's mechanism: it is a lung-selective, once-daily nebulized long-acting muscarinic antagonist (LAMA) that blocks M3 muscarinic receptors on airway smooth muscle, preventing acetylcholine-mediated bronchoconstriction and mucus hypersecretion, and is rapidly cleared by pulmonary esterases to limit systemic anticholinergic exposure (PMID [30803279](https://pubmed.ncbi.nlm.nih.gov/30803279/), [31245215](https://pubmed.ncbi.nlm.nih.gov/31245215/)).

Chronic bronchitis is clinically one of the phenotypic presentations of COPD, so a bronchodilator/anti-muscarinic mechanism proven in COPD is mechanistically plausible for bronchitis as well. However, the only trial currently linked to the bronchitis prediction (NCT01704404) is a Phase 2 PD/safety/PK dose-characterization study in COPD subjects, not a bronchitis-specific efficacy trial — it appears in both the bronchitis and obstructive-lung-disease evidence sets, suggesting the link may reflect disease-ontology overlap rather than direct bronchitis evidence.

Separately, the model also predicts "obstructive lung disease" (rank 2, score 99.10%) with L1 evidence — two completed Phase 3 RCTs (NCT02459080, n=619; NCT02512510, n=611) plus a 52-week active-controlled safety trial (NCT02518139, n=1060) and 20 supporting publications. This is essentially revefenacin's own core COPD indication being re-identified by the model, which validates the model's mechanistic reasoning but is not a "new" indication in the repurposing sense — it does, however, support that the mechanism-to-airway-obstruction link is real and strong, lending indirect plausibility to the bronchitis signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | Completed | 62 | Dose-response characterization of TD-4208 (revefenacin) after 7 days in COPD subjects; not bronchitis-specific — shared with the obstructive lung disease indication and graded C relevance (early PD/safety/PK study, not a bronchitis efficacy endpoint) |

---

## Literature Evidence

Currently no related literature available specifically for the bronchitis indication.

*(For context: 20 publications support revefenacin's efficacy/safety in the closely related obstructive lung disease/COPD indication, including reviews such as PMID [30803279](https://pubmed.ncbi.nlm.nih.gov/30803279/) and the regulatory approval summary PMID [30560478](https://pubmed.ncbi.nlm.nih.gov/30560478/) "Revefenacin: First Global Approval.")*

---

## Saudi Arabia Market Information

Revefenacin is not currently registered or marketed in Saudi Arabia (0 authorizations, no licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — DDI query returned no results, and no drug interaction database entry was found.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis signal rests on a single non-bronchitis-specific Phase 2 trial (evidence level L3, decision stage S1/"Research Question"), which is insufficient to support progression. The mechanistic plausibility is reinforced by the drug's strong, separately-evidenced COPD/obstructive lung disease data (L1, S3), but that data supports COPD, not bronchitis specifically, and Saudi Arabia currently has zero market presence for this drug.

**To proceed, the following is needed:**
- SFDA package insert / warnings & contraindications data (currently blocking safety review, DG001)
- Formal MOA confirmation from DrugBank (DG002)
- A bronchitis-specific (not COPD-shared) clinical trial or literature signal before advancing past S1
- Separately, consider whether the strong obstructive lung disease (COPD) evidence package (L1, 2 completed Phase 3 RCTs) warrants its own market-entry evaluation for Saudi Arabia, independent of this bronchitis repurposing question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

