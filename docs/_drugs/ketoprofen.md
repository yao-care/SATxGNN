---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From Unspecified Original Indication to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen (DrugBank DB01009) has no original indication or mechanism-of-action data on file in this evidence pack, and it is not currently marketed in Saudi Arabia. The TxGNN model's top prediction, **Acromesomelic Dysplasia, Hunter-Thompson Type**, is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags this specific prediction as likely graph-embedding noise rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (0 Saudi licenses; original_indications empty) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ketoprofen in this evidence pack. Based on general pharmacological knowledge, ketoprofen is a propionic-acid-derivative NSAID that inhibits COX-1/COX-2 and prostaglandin synthesis — a mechanism relevant to inflammatory and pain conditions.

However, for the top-ranked prediction, Acromesomelic Dysplasia, Hunter-Thompson Type, no such link applies. Per the evidence pack's own repurposing rationale, this is a GDF5/BMP signaling-pathway skeletal developmental disorder with no known relationship to COX inhibition or prostaglandin synthesis. The rationale explicitly attributes the high TxGNN score to likely graph-embedding noise, driven by the drug node's data sparsity (no original indication, no MOA, zero DDI records). The same caveat applies to ranks 2–7 and 9 in this evidence pack, which are all congenital/structural or genetic disorders without a plausible NSAID mechanism.

Two lower-ranked predictions are mechanistically more defensible: **spondyloarthropathy, susceptibility to** (rank 8) and **juvenile arthritis due to defect in LACC1** (rank 10) are both inflammatory joint diseases, a category where NSAIDs are an established symptomatic treatment class. These carry L4 evidence (mechanism-level plausibility, "Research Question" stage) rather than direct trial support, but represent a more scientifically grounded direction than the current top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Ketoprofen is not currently marketed in Saudi Arabia under this evidence pack (0 authorizations on file; `taiwan_regulatory.licenses` is empty).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has zero supporting clinical trials or literature (L5), and the model's own mechanistic rationale identifies it as likely embedding noise rather than a real signal, driven by sparse underlying drug data (no original indication, no MOA, no DDI records). This does not meet the bar to advance to safety screening (S1).

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Ketoprofen mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Original indication and Saudi Arabia licensing records, currently entirely absent from this evidence pack
- If pursuing repurposing research for ketoprofen, consider redirecting attention to the mechanistically plausible candidates in this same batch — **spondyloarthropathy, susceptibility to** and **juvenile arthritis due to defect in LACC1** — and seek targeted clinical/preclinical evidence for those indications rather than the current top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

