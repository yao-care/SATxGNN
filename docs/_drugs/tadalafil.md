---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From PDE5 Inhibitor Indications to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a phosphodiesterase type 5 (PDE5) inhibitor whose established uses (erectile dysfunction, benign prostatic hyperplasia, pulmonary arterial hypertension) are not captured in this evidence pack (`original_indications` is empty). The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-growth disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known mechanistic link between PDE5 inhibition and this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (original_indications empty); tadalafil is generally known as a PDE5 inhibitor class drug |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa` = Data Gap, DG002, severity High). Based on general pharmacological knowledge, tadalafil inhibits PDE5, preventing cGMP breakdown and promoting vascular/smooth-muscle relaxation — the basis for its known use in erectile dysfunction, BPH, and pulmonary arterial hypertension.

For the top-ranked prediction, however, this mechanism does not translate into a plausible rationale. Ambras type hypertrichosis universalis congenita is a congenital disorder caused by an 8q chromosomal rearrangement, presenting as developmental/genetic generalized hypertrichosis — it has no established relationship to vascular smooth-muscle tone or NO-cGMP signaling. The evidence pack's own `repurposing_rationale` states explicitly that there is **no mechanistic connection**, and the pairing is corroborated by **zero** clinical trials, ICTRP records, or PubMed literature (confirmed via 3 independent queries, `query_log` ids 5–7).

Among the other 7 candidates in this pack, only two show any biological plausibility worth noting: **kyphoscoliotic heart disease** (rank 7) has a theoretical link via PDE5i's approved role in reducing pulmonary vascular resistance, but zero disease-specific trials or literature exist to support it; and **migraine with brainstem aura** (rank 8) is supported by a single case report (PMID 17059442) describing tadalafil-*induced* aura — this is an adverse-event signal, not a treatment-efficacy signal. All other candidates (hypertrichosis, odontal/periodontal malformation syndrome, Dandy-Walker–related syndrome, hair shaft abnormality, trichomegaly) have no direct drug-disease evidence. This pattern is consistent with a known TxGNN limitation: very high scores can reflect embedding-space proximity rather than a testable biological hypothesis, and should not be read as repurposing evidence on their own.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information

No marketing authorizations are recorded for tadalafil in this jurisdiction (0 authorizations; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Ambras type hypertrichosis universalis congenita) has zero clinical or literature evidence, and the evidence pack itself documents no plausible mechanistic link to PDE5 inhibition — this is a model score without a supportable biological hypothesis. No candidate in this set reaches beyond L4 evidence, and the drug is not currently marketed in this jurisdiction, so there is no near-term regulatory pathway regardless of indication.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, blocking — required before any S1 safety screening)
- Confirmed mechanism of action via DrugBank API (DG002, high priority)
- If pursuing repurposing further, re-scope candidate selection toward mechanistically plausible targets (e.g., pulmonary-hypertension-adjacent conditions such as kyphoscoliotic heart disease) rather than the current top-ranked score alone
- Clarification/correction of the migraine signal (rank 8) as a safety flag rather than a repurposing opportunity, to avoid downstream misclassification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

