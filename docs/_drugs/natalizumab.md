---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody publicly known for treating relapsing forms of multiple sclerosis (and Crohn's disease); this evidence pack itself carries no confirmed original-indication or mechanism-of-action data (flagged as data gaps). The TxGNN model predicts possible effectiveness for **Bronchitis**, but this is currently backed by **0 clinical trials** and **0 publications**, and the proposed mechanism (systemic immunosuppression) runs counter to what treating an infectious/inflammatory airway disease would require.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (data gap); publicly known as Multiple Sclerosis / Crohn's disease, but unconfirmed by this dataset |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on publicly known information, natalizumab is a recombinant humanized IgG4 monoclonal antibody that binds the α4-subunit of α4β1/α4β7 integrins, blocking leukocyte adhesion to vascular endothelium and thereby reducing lymphocyte trafficking into the central nervous system and gut — the basis for its established use in multiple sclerosis and Crohn's disease.

Bronchitis, by contrast, is typically an infectious or irritant-driven inflammatory condition of the airways, where intact leukocyte trafficking supports pathogen clearance. A systemic immunosuppressant that blocks leukocyte migration would be expected, if anything, to impair clearance of respiratory infections rather than treat them. The evidence pack's own repurposing rationale for this candidate explicitly flags this as a mechanistic contradiction rather than a supporting hypothesis.

No clinical trials, case reports, or reviews connecting natalizumab to bronchitis were found in ClinicalTrials.gov, ICTRP, or PubMed (all three searches returned zero results). The TxGNN score of 99.46% therefore reflects a network-topology signal only, with no corroborating mechanistic or clinical evidence identified to date.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Natalizumab is not currently marketed in Saudi Arabia (0 authorizations on record). No product license or approved-indication text is available in this evidence pack.

## Safety Considerations

No structured warnings, contraindications, or drug-interaction data are available in this evidence pack — TFDA/SFDA package-insert data is marked as a **blocking** data gap (DG001) that must be resolved before any safety (S1) evaluation can proceed. Please refer to the official package insert for safety information once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (bronchitis) has zero clinical-trial or literature support, and the proposed mechanism actively conflicts with what would be needed to treat an infectious/inflammatory airway disease. Combined with blocking data gaps in TFDA safety information and drug MOA, and the fact that natalizumab is not marketed in Saudi Arabia, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications, DDI) — currently blocking (DG001)
- Verified original MOA and approved indications from DrugBank/regulatory source (DG002)
- Any clinical or preclinical evidence specifically linking natalizumab to bronchitis, should it emerge
- Note: among this drug's other predicted indications, rank 3 (psoriasis) has substantially more literature (19 PubMed hits, decision stage S1), but the majority of that evidence describes natalizumab **inducing or aggravating** psoriasis rather than treating it — worth a separate, dedicated evaluation rather than assuming therapeutic benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

