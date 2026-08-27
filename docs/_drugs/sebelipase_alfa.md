---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase (LAL) enzyme replacement therapy, originally developed for Lysosomal Acid Lipase Deficiency (LAL-D). The TxGNN model's top prediction is **Scheie syndrome**, but this direction currently has **0 clinical trials** and **0 publications** in support — the high score appears to reflect semantic clustering among rare genetic storage disorders rather than a real pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal Acid Lipase Deficiency (LAL-D) — no Saudi Arabia license record on file; inferred from literature evidence in this pack |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information recoverable from the literature evidence in this pack, sebelipase alfa (Kanuma®) is a recombinant human lysosomal acid lipase (LAL) enzyme replacement therapy — it restores LAL enzyme activity in patients whose lysosomes cannot hydrolyze cholesteryl esters and triglycerides, and its efficacy in LAL-D (encompassing both Wolman disease and cholesteryl ester storage disease) has been demonstrated in multiple completed trials.

Scheie syndrome, however, is a mild form of Mucopolysaccharidosis type I (MPS I), caused by deficiency of **alpha-L-iduronidase (IDUA)** — an entirely different lysosomal enzyme acting on glycosaminoglycan degradation, not lipid metabolism. There is no shared substrate, pathway, or enzyme target between LAL and IDUA.

The repurposing rationale accompanying this prediction explicitly notes that the association is most likely driven by TxGNN grouping Scheie syndrome and LAL-D together as "rare genetic metabolic/storage diseases" in its embedding space, rather than by any real shared biology. No clinical trial or literature evidence was found linking sebelipase alfa to Scheie syndrome, consistent with this being a model-prediction artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Sebelipase alfa is not currently marketed in Saudi Arabia — no active authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA/SFDA package insert warnings and contraindications are an unresolved Blocking data gap — DG001 — and DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.80%), there is no mechanistic plausibility (different target enzyme — LAL vs. IDUA), no clinical trial evidence, and no literature support for using sebelipase alfa in Scheie syndrome. This meets the criteria for L5 — model prediction only, no actual studies.

**To proceed, the following is needed:**
- Independent mechanistic review confirming (or ruling out) any indirect pathway link between LAL and IDUA-related storage disease biology
- At minimum, preclinical or case-level evidence before this candidate could be reconsidered
- Resolution of the Blocking data gap on TFDA/SFDA package insert warnings and contraindications (DG001) and MOA (DG002), which currently prevent any safety pre-assessment for this drug generally

**Note for portfolio prioritization:** within this same evidence pack, two other candidates show substantially stronger support and warrant separate evaluation — *cholesteryl ester storage disease* (rank 4, 9 trials incl. 2 completed Phase 3 studies, 19 publications) and *Wolman disease* (rank 5, L2/S3, "Proceed with Guardrails") — both of which fall within sebelipase alfa's already-established LAL-D mechanism, unlike Scheie syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

