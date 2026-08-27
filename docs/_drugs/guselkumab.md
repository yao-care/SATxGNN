---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Plaque Psoriasis to Drug-induced Osteoporosis

## One-Sentence Summary

Guselkumab is a monoclonal antibody originally developed and approved for moderate-to-severe plaque psoriasis (anti-IL-23p19). The TxGNN model's top-ranked prediction is **Drug-induced Osteoporosis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model itself flags the mechanistic rationale as likely a graph-embedding artifact rather than genuine pathophysiological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (general drug knowledge; not locally verifiable — see note below) |
| Predicted New Indication | Drug-induced Osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan (TFDA) Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> Note: `taiwan_regulatory.licenses` is empty and `original_indications` is empty because guselkumab is not currently registered with TFDA (未上市). The original indication above reflects general public drug information, not a Taiwan-specific approval record.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a Blocking/High-severity data gap). Based on known information, guselkumab is a fully human IgG1 monoclonal antibody that selectively binds the p19 subunit of IL-23, blocking IL-23-driven Th17 cell activation — a mechanism well established in its approved use for plaque psoriasis.

For the top-ranked prediction, drug-induced osteoporosis, the evidence pack's own rationale is explicitly skeptical: it notes that the IL-23/Th17 axis has been indirectly linked to osteoclast activation in inflammatory arthritis, but "drug-induced osteoporosis" as a disease entity is defined by direct toxic mechanisms of causative agents (e.g., corticosteroids), which has no established pathophysiological connection to IL-23 inhibition. The model assessment concludes the high similarity score more likely reflects graph-embedding proximity than a credible mechanistic hypothesis. In other words, the strength of the numeric score (99.84%) should not be read as strength of biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Guselkumab is not currently marketed in Taiwan (TFDA market status: 未上市, 0 licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps or not found in this evidence pack; a TFDA package-insert PDF parse is required — see DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN similarity score but zero clinical or literature evidence (L5), and the pack's own mechanistic assessment considers the IL-23-to-osteoporosis link biologically implausible as currently framed. There is no basis to advance this specific indication.

**To proceed, the following is needed:**
- Confirmed drug MOA data (DrugBank/label-sourced), currently a High-severity data gap
- TFDA package insert (warnings, contraindications, DDI) — Blocking severity, required before any S1 safety screen
- Preclinical or mechanistic studies specifically linking IL-23 inhibition to bone metabolism/osteoporosis pathways, not just inflammatory arthritis
- If Taiwan registration is pursued, local regulatory filing data (license number, approved indication text)

---

**Note on this evidence pack:** two other candidates in the same `predicted_indications` list carry substantially stronger evidence and should be considered separately if the goal is identifying a viable repurposing/expansion candidate rather than following rank order:
- **Psoriasis** (rank 3, score 99.75%) — Evidence Level L1, decision stage S3, "Proceed with Guardrails." Supported by multiple completed Phase 3 RCTs (e.g., NCT02325219) and is already guselkumab's approved indication elsewhere (Tremfya) — not a novel hypothesis but a validated mechanism.
- **Ulcerative colitis** (rank 6, score 99.70%) — Evidence Level L1, decision stage S3, "Proceed with Guardrails." Supported by the QUASAR Phase 2b/3 program (PMID 39706209, 37659673) and FDA approval for UC in 2024/2025.

If a follow-up report is wanted for either of these, I can generate it using the same template with `predicted_indications[2]` (psoriasis) or `predicted_indications[5]` (UC) as the primary target.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

