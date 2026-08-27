---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Inflammatory Arthritis to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Meloxicam is a COX-2 preferential NSAID established for inflammatory arthritis in adults.
> Among 10 TxGNN-predicted indications in this evidence pack, **Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis (JIA)** stands out as the most clinically credible, supported by **1 Phase 4 safety registry publication** on NSAID use in JIA — though **no dedicated clinical trials** for this drug-indication pair exist yet.
> Note: TxGNN's raw #1-ranked prediction (acromesomelic dysplasia) was not used as the headline, because the evidence pack's own mechanistic analysis explicitly found no plausible pathophysiological link for that and 6 other top-10 candidates (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Saudi Arabia approved-label text on record (drug not marketed there); per evidence-pack rationale, meloxicam's established class use is as a COX-2 preferential NSAID for inflammatory arthritis |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.44% (rank 8 of candidates; score not the highest in the set — see selection note below) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Selection note:** This evidence pack contains 10 TxGNN-predicted indications, all with near-identical raw scores (99.3%–99.9%). The pack's own `repurposing_rationale` text flags 7 of the 10 (ranks 1–5, 9, 10) as mechanistically implausible — mostly ultra-rare monogenic skeletal/immune disorders with no inflammatory pathology for an NSAID to act on. Of the remaining 3, this report features rank 8 (JIA, L3, "Proceed with Guardrails") because it has the best evidence level and the only literature citation. Rank 6 (spondyloarthropathy susceptibility, L4, "Proceed with Guardrails") has a stronger mechanistic argument but zero supporting trials or literature and targets a genetic-susceptibility record rather than the disease itself; rank 7 (rheumatoid nodulosis, L4, "Research Question") is weaker still.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for meloxicam is not available from DrugBank in this pack (flagged as data gap DG002, High severity). Based on the mechanistic evidence supplied, meloxicam is characterized as a COX-2 preferential non-steroidal anti-inflammatory drug (NSAID), and the pack's rationale for a related candidate (rank 6, spondyloarthropathy) states it is "clinical routine first-line therapy" for inflammatory joint disease via suppression of inflammatory prostaglandin synthesis.

Polyarticular JIA — particularly the rheumatoid-factor-positive subtype — is a chronic inflammatory arthritis in children with pathophysiology closely paralleling adult rheumatoid/inflammatory arthritis, the disease class meloxicam already treats. NSAIDs, including nonselective agents, are already used in routine pediatric rheumatology practice for JIA symptom control, which is consistent with the mechanistic rationale supplied in this pack ("meloxicam is used clinically for JIA symptom control in multiple countries with pediatric NSAID approvals").

Because the pathophysiology (synovial inflammation, prostaglandin-mediated pain and swelling) is the same target meloxicam's COX-2 inhibition already addresses in adult inflammatory arthritis, the mechanistic extension to JIA is plausible. However, this pack contains no meloxicam-specific clinical trial evidence for this exact indication — only a broader NSAID-class safety registry (see Literature Evidence below) — so the mechanistic plausibility currently outruns the direct evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort / Safety Registry (Phase 4) | Pediatric Rheumatology Online Journal | Long-term safety and developmental outcomes in JIA patients treated in routine practice with celecoxib or nonselective NSAIDs (nsNSAIDs, the class meloxicam belongs to); supports real-world use of NSAIDs in JIA populations |

---

## Saudi Arabia Market Information

Meloxicam is not marketed in Saudi Arabia under this evidence pack (0 authorizations on record); no market authorization data available.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not available in this evidence pack (flagged as data gap DG001, **Blocking** severity — TFDA/SFDA label warnings and contraindications must be obtained before any S1 safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between meloxicam's established anti-inflammatory action and JIA's inflammatory pathology is plausible, and one Phase 4 registry publication supports real-world NSAID-class use in this population — but there is no meloxicam-specific trial evidence for this indication, and safety/labeling data are entirely missing (Blocking gap), so this cannot move past a guarded, evidence-gathering stage.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — Blocking gap DG001
- DrugBank-sourced mechanism of action confirmation — High-priority gap DG002
- Meloxicam-specific (not NSAID-class-general) clinical evidence in RF-positive polyarticular JIA, or additional literature beyond the single 2014 safety registry
- Saudi Arabia regulatory/market-entry assessment, since the drug currently holds 0 local authorizations
- Re-evaluation of rank 6 (spondyloarthropathy) as a secondary candidate if further evidence emerges, given its stronger mechanistic rationale despite currently having zero trials or literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

