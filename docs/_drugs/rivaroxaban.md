---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban: From Venous Thromboembolism/Atrial Fibrillation to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct oral Factor Xa inhibitor whose established clinical use context — evident throughout this evidence pack — is treatment/prevention of venous thromboembolism (DVT/PE) and stroke prevention in atrial fibrillation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **4 publications** currently identified, none of which directly test rivaroxaban as an RA therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Venous thromboembolism (DVT/PE) treatment/prevention and stroke prevention in non-valvular atrial fibrillation *(inferred from trial/literature context in this evidence pack; no formal regulatory indication text available — see Data Gaps below)* |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap requiring a DrugBank API query). Based on known information, rivaroxaban is a direct Factor Xa inhibitor used for thromboembolic disease; its efficacy in venous thromboembolism and atrial fibrillation-related stroke prevention is well established, but no MOA data specific to inflammatory or autoimmune pathways is present here.

The proposed rationale linking rivaroxaban to rheumatoid arthritis rests on a chronic-inflammation-hypercoagulability hypothesis: RA patients have elevated VTE risk due to persistent inflammation, and thrombin generation is known to interact bidirectionally with inflammatory pathways ("thrombin-inflammation crosstalk"). This provides a plausible biological rationale for why TxGNN may have linked the two entities.

However, none of the four literature items retrieved actually study rivaroxaban as a treatment for RA itself. They instead cover VTE diagnosis/management, thrombin generation assays in autoimmune disease more broadly, anticoagulant adherence in atrial fibrillation, and a case report where RA appears only as a comorbidity in a patient on anticoagulation for an unrelated embolic event. The association therefore currently reflects "RA patients who happen to require anticoagulation" rather than evidence that rivaroxaban treats RA.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Compares medication adherence to rivaroxaban vs. apixaban in non-valvular atrial fibrillation; an adherence study, not related to RA. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of diagnosis and treatment of lower-extremity DVT/PE; general VTE epidemiology, no RA content. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Discusses thrombin generation assay as a tool to assess hypercoagulability in autoimmune diseases (e.g., antiphospholipid syndrome); does not evaluate rivaroxaban efficacy in RA. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | Case of perioperative thromboembolic cerebral infarction in an 88-year-old woman with atrial fibrillation and RA on oral steroids; illustrates comorbidity, not treatment evidence. |

## Saudi Arabia Market Information

Rivaroxaban is not currently marketed in this jurisdiction — no authorization records are available (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no clinical trials and no literature directly support rivaroxaban as a treatment for rheumatoid arthritis — all identified evidence describes RA patients as an anticoagulation *population*, not RA as a treatment *target*. The mechanistic link (thrombin-inflammation crosstalk) remains a hypothesis without supporting preclinical or clinical data specific to this drug-indication pair. Additionally, local safety documentation is missing, which blocks any preliminary safety assessment.

**To proceed, the following is needed:**
- MOA data from DrugBank (High-severity data gap, DG002)
- SFDA/local package insert warnings and contraindications (Blocking data gap, DG001) — required before any S1 safety screening
- Resolution of the "not_found" DDI query status
- Dedicated preclinical or mechanistic studies testing rivaroxaban's effect on RA disease activity, rather than incidental anticoagulation-in-RA-patients data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

