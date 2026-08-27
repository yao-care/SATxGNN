---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

# REMDESIVIR: From Viral Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase (RdRp), used against RNA viruses such as SARS-CoV-2 and Ebola.
The TxGNN model's top prediction for this drug is **Multiple Endocrine Neoplasia (MEN)**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no mechanistic overlap between an antiviral RdRp inhibitor and a genetic tumor-suppressor-driven endocrine syndrome — this is most consistent with model noise rather than a real signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Saudi Arabia and no local label data exists; known globally as an RNA-virus antiviral (RdRp inhibitor) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal MOA documentation is not available in this evidence pack (DG002), but the underlying evidence records consistently describe remdesivir as a nucleotide analog prodrug that, once activated intracellularly, inhibits the viral RNA-dependent RNA polymerase (RdRp) — the mechanism behind its established use against SARS-CoV-2, Ebola, and other RNA viruses.

Multiple Endocrine Neoplasia (MEN) is a hereditary endocrine tumor syndrome driven by germline mutations in *RET* (MEN2) or *MEN1* — tumor-suppressor/oncogene pathways governing cell proliferation, entirely unrelated to viral RNA replication. The evidence pack's own mechanistic assessment for this candidate explicitly concludes there is "no overlap" between remdesivir's RdRp-inhibition mechanism and MEN pathogenesis, and the candidate has zero supporting clinical trials or literature despite a high raw TxGNN score (rank 7,813 out of the model's full output).

Given the absence of any mechanistic plausibility or corroborating evidence, this specific prediction should be treated as a low-confidence model artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Remdesivir is not currently marketed in Saudi Arabia (0 authorizations on file), so no local product/authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other TxGNN-Predicted Indications (Reviewed for Context)

This evidence pack scored 6 candidate indications for remdesivir. All show similar or weaker support than the top-ranked candidate:

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|------|------|
| 2 | HIV infectious disease | 99.32% | L4 | 23 trials / 20 publications retrieved, but graded relevance "C" — nearly all are COVID-19/SARS-CoV-2 trials (ACTT/ACTIV-3 platform series) with a mismatched disease label, not genuine HIV-specific evidence. Retroviral replication depends on reverse transcriptase, not RdRp. |
| 3 | Simian immunodeficiency virus infection | 99.07% | L5 | No trials/literature; same RT-vs-RdRp mechanism mismatch; not a human clinical indication. |
| 4 | Feline acquired immunodeficiency syndrome | 99.07% | L5 | No trials/literature; veterinary indication, same mechanism mismatch. |
| 5 | Neurodevelopmental disorder (ataxic gait/absent speech/white matter) | 99.03% | L5 | No trials/literature; rare genetic disorder with no plausible antiviral mechanism link. |
| 6 | Homozygous familial hypercholesterolemia | 99.03% | L5 | No trials/literature; LDL receptor defect, unrelated to antiviral mechanism. |

The pattern across all 6 candidates — high raw scores but no mechanistic or empirical support — suggests this drug currently has no credible TxGNN-derived repurposing signal beyond its known antiviral use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (MEN) has zero clinical or literature evidence and an explicitly stated mechanistic disconnect. The next-best candidate (HIV) initially appears evidence-rich, but on inspection the retrieved trials and literature are predominantly COVID-19/SARS-CoV-2 studies with a mislabeled disease tag, not genuine HIV-focused evidence — and reverse-transcriptase-dependent HIV replication is not addressed by an RdRp inhibitor. No candidate in this pack currently clears a threshold to proceed.

**To proceed, the following is needed:**
- SFDA/TFDA package insert data (blocking gap — required for any safety pre-screen)
- Confirmed mechanism of action from DrugBank (currently a data gap)
- Manual re-triage of the "HIV infectious disease" evidence set to separate genuine HIV-relevant records from mislabeled COVID-19 trials
- If pursuing a repurposing hypothesis for remdesivir, prioritize indications consistent with its confirmed RdRp/RNA-virus mechanism (e.g., other RNA viral infections) rather than the candidates surfaced here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

