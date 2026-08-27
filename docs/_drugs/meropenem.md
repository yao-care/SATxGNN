---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# MEROPENEM: From Unspecified Indication to Bacterial Arthritis

## One-Sentence Summary

MEROPENEM is a broad-spectrum carbapenem antibiotic; the evidence pack does not record its original approved indication or Saudi Arabia licensing history (0 licenses on file, market status: not marketed). The TxGNN model predicts it may be effective for **Bacterial Arthritis**, but this is currently supported by only **1 clinical trial** (in a different drug and population) and **no literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — the evidence pack contains no original indication or license data for this drug |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for MEROPENEM (flagged as a High-severity data gap in the source data). Based on the information available in the evidence pack, MEROPENEM is a broad-spectrum carbapenem antibiotic that acts by inhibiting bacterial penicillin-binding proteins (PBPs), thereby blocking cell wall synthesis — this mechanism is referenced consistently across all ten TxGNN-predicted indications in this pack, not just bacterial arthritis.

For bacterial arthritis specifically, the pathogens most commonly implicated (S. aureus, streptococci, and gram-negative bacilli) generally fall within meropenem's known antimicrobial spectrum, and carbapenems are used clinically as empirical therapy in immunocompromised or multidrug-resistant patients. However, the mechanistic plausibility is not yet backed by indication-specific trial or literature evidence — the one linked trial studies a different drug (levofloxacin) in a different population (pediatric leukemia/HSCT bacteremia prevention), which the evidence pack itself grades as only "C" relevance (no direct connection to bacterial arthritis treatment).

It is also worth noting that among the ten TxGNN-predicted indications in this pack, **urinary tract infection** (rank 6) has substantially stronger evidence (L1, multiple completed Phase 3 RCTs directly involving meropenem or meropenem-vaborbactam) than bacterial arthritis (rank 1, L4). The rank-1 prediction reflects the highest TxGNN model score, not the strongest clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Evaluated levofloxacin (not meropenem) to prevent bacteremia in children with acute leukemia or undergoing HSCT; graded "C" relevance — different drug and different clinical question than bacterial arthritis treatment |

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

No authorizations on file — MEROPENEM is not currently marketed in Saudi Arabia under this evidence pack (0 licenses recorded).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/SFDA package insert warnings and contraindications are flagged as a Blocking data gap (DG001) in the source data — this must be resolved before any safety evaluation can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (bacterial arthritis) is supported only by L4-level evidence — a single Phase 3 trial that studied a different drug in an unrelated population — with no supporting literature. Combined with a Blocking-severity data gap on safety (no TFDA/SFDA warnings or contraindications available), the evidence base is insufficient to proceed past a research-question stage.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action (MOA) data from DrugBank
- Original approved indication(s) and Saudi Arabia licensing history for MEROPENEM
- Indication-specific clinical trials or literature directly evaluating meropenem in bacterial arthritis
- If pursuing a repurposing candidate from this pack, consider prioritizing **urinary tract infection** (rank 6, L1 evidence, multiple completed Phase 3 RCTs) as a stronger starting point than bacterial arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

