---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 6
---

# Finasteride
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

# Finasteride: From Androgenetic Alopecia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5α-reductase inhibitor globally known for treating androgenetic alopecia (male pattern hair loss) and benign prostatic hyperplasia. The TxGNN model's top prediction is **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital generalized hypertrichosis — but this evidence pack currently contains **zero clinical trials and zero publications** supporting the link, and the drug's own mechanistic rationale flags the biological plausibility as weak to non-existent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Androgenetic alopecia / Benign prostatic hyperplasia (well-established globally; no local license data available in this pack) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, finasteride is a type II 5α-reductase inhibitor that blocks conversion of testosterone to dihydrotestosterone (DHT); its established efficacy is in androgen-dependent hair loss and prostate enlargement.

Ambras syndrome, however, is a congenital, non-androgen-dependent form of generalized hypertrichosis, linked to a chromosome 8q12 structural abnormality that drives extra hair follicle development from early development onward. This pathology does not operate through the testosterone/DHT axis that finasteride targets — the drug's own repurposing rationale for this candidate explicitly states the mechanistic link is "weak to non-existent."

The prediction most plausibly reflects a knowledge-graph association through the shared category of "hair growth/follicle disorders" rather than a genuine shared causal pathway. By contrast, rank #2 in this pack — general "hypertrichosis (disease)," which includes androgen-dependent hirsutism — has a more defensible mechanistic story (finasteride's known anti-androgen effect on hair growth) and is the only candidate in this pack with any clinical trial or literature support (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package insert warnings/contraindications are marked as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety screening can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a very high TxGNN similarity score but is supported by no clinical trials, no literature, and no market/regulatory data, and the mechanistic rationale itself concludes the disease pathway (congenital 8q12-related follicle proliferation) does not align with finasteride's DHT-blocking mechanism. This meets the L5 definition (model prediction only, no actual studies) and does not warrant advancement at this time.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (Blocking gap, DG001)
- Formal MOA documentation via DrugBank API (High-priority gap, DG002)
- If this specific ultra-rare congenital indication is still of interest: genetic/mechanistic studies showing any androgen-pathway involvement in 8q12-driven follicle proliferation (none currently exists)
- Consider redirecting evaluation effort to rank #2 in this pack, "hypertrichosis (disease)" (score 99.99%, Evidence Level L4, decision stage S1) — it has 1 clinical trial (low relevance, Phase 4) and 4 literature reviews discussing finasteride's role in androgen-dependent hair growth conditions, making it the more evidence-backed candidate among the six predictions screened for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

