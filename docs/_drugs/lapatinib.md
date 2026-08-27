---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: From HER2-Positive Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor used clinically for HER2-overexpressing breast cancer (based on general pharmacological knowledge; Saudi regulatory records show no approved indication text since the drug is not marketed there). The TxGNN model predicts a possible effect in **Dermatofibrosarcoma Protuberans (DFSP)**, but this prediction is currently **unsupported by any clinical trial or literature evidence** and is mechanistically discordant with the drug's known target profile.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (based on general drug knowledge; no Saudi regulatory record exists) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, lapatinib is a dual tyrosine kinase inhibitor targeting **EGFR and HER2 (ERBB2)**, and its efficacy in HER2-positive breast cancer is well established.

DFSP, however, is molecularly driven by a **COL1A1-PDGFB fusion gene** that causes constitutive **PDGFRB** activation — a distinct pathway from EGFR/HER2. The clinical standard-of-care targeted therapy for DFSP is **imatinib**, a PDGFR inhibitor, not an EGFR/HER2 inhibitor.

Because lapatinib does not target PDGFR, there is **no direct mechanistic link** between its known pharmacology and the DFSP driver pathway. The high TxGNN score (99.30%) most likely reflects structural or embedding-space similarity among tyrosine kinase inhibitors in the knowledge graph, rather than target-specific evidence. This prediction should be treated as a hypothesis-generating signal only, not as mechanistically validated.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Lapatinib is not marketed in Saudi Arabia (0 authorizations on record); no product license information is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on the TxGNN model score (L5, no clinical trials or literature), and the drug's known EGFR/HER2 mechanism is mechanistically discordant with the PDGFR-driven pathology of DFSP. Combined with a Blocking data gap on TFDA safety/label information, this candidate cannot advance to safety review at this time.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications, DDI) — currently a Blocking gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Preclinical or case-level evidence of lapatinib activity in PDGFR-driven or imatinib-resistant DFSP models
- Literature or trial search re-run after data gaps are resolved to reassess evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

