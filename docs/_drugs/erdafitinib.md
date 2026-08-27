---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Erdafitinib: From FGFR-Driven Malignancy to Predicted Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is an FDA-approved FGFR (fibroblast growth factor receptor) tyrosine kinase inhibitor used in oncology; this evidence pack does not capture its specific original indication in structured form, but literature confirms its classification as a small-molecule kinase antagonist. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but currently **0 clinical trials** and **0 publications** directly support this specific direction, and the proposed mechanism is directionally ambiguous (inhibition could plausibly worsen rather than improve pulmonary vascular function).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (no licenses/original indications on file); literature confirms erdafitinib is an FDA-approved FGFR tyrosine kinase inhibitor (2019 approval, oncology class) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 (model prediction only — no supporting clinical trials or literature) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record (original_moa is a documented data gap). Based on known information from the supporting literature in this pack, erdafitinib belongs to the class of small-molecule FGFR tyrosine kinase inhibitors, approved by regulatory authorities in 2019 alongside other kinase antagonists (entrectinib, pexidartinib, fedratinib) for oncology indications driven by genetic alterations in kinase signaling.

The proposed link to pulmonary hypertension rests on the biological observation that FGF/FGFR signaling plays a role in pulmonary vascular remodeling, with some literature suggesting FGFR signaling can be protective to pulmonary vascular endothelium. However, this is precisely where the rationale becomes uncertain: if FGFR signaling is protective in this context, an FGFR *inhibitor* like erdafitinib could theoretically worsen rather than improve pulmonary vascular tone. No database-indexed evidence currently supports a therapeutic (rather than harmful) direction for this drug-disease pair.

Because the TxGNN score is high but is not corroborated by any disease-specific clinical trial or publication, and the underlying mechanistic hypothesis itself flags directional uncertainty, this candidate should be treated as a hypothesis-generating signal only, not as a validated repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Erdafitinib currently has no marketing authorization on file in Saudi Arabia (market status: Not Marketed; 0 total licenses). No product, dosage form, or approved indication text is available to report.

---

## Cytotoxicity

Erdafitinib is classified as an antineoplastic agent (FDA-approved FGFR tyrosine kinase inhibitor used in oncology per the literature evidence in this pack), so cytotoxicity information is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1–4 tyrosine kinase inhibitor), not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA package insert retrieval is flagged in this evidence pack as a Blocking data gap — DG001 — meaning this candidate cannot yet pass the S1 safety pre-screen until package insert warnings, contraindications, and DDI data are obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5 evidence) with zero corroborating clinical trials or literature specific to pulmonary hypertension, and the underlying mechanistic rationale is itself directionally ambiguous (FGFR inhibition could plausibly be harmful rather than beneficial to pulmonary vascular function). This does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Retrieval of TFDA/SFDA package insert data (contraindications, key warnings) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank — currently a High-severity data gap (DG002)
- Preclinical or mechanistic studies clarifying the direction of effect of FGFR inhibition on pulmonary vascular tone
- Any disease-specific clinical trial or case-report evidence for erdafitinib in pulmonary hypertension, to move this candidate beyond L5
- Drug-drug interaction (DDI) data, currently unavailable (query returned "not_found")

*Note: This evidence pack also lists five other lower-confidence candidates (kyphoscoliotic heart disease, amenorrhea, rheumatoid arthritis, ALS, brachydactyly-syndactyly syndrome). Rheumatoid arthritis and brachydactyly-syndactyly syndrome carry marginally stronger mechanistic plausibility (synovial angiogenesis and FGFR gain-of-function skeletal disorders, respectively) and were flagged as "Research Question" rather than "Hold" — these may warrant a separate, dedicated evaluation if this pulmonary hypertension lead is deprioritized.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

