---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 6
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a human monoclonal antibody that inhibits BLyS (B-lymphocyte stimulator)/BAFF, originally approved for Systemic Lupus Erythematosus (SLE) and lupus nephritis. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **1 indirectly related clinical trial** and **0 publications** currently supporting this direction. Evidence remains at the mechanistic hypothesis stage (L4), and no direct clinical data exist for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE), Lupus Nephritis |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (Mechanistic hypothesis; no direct clinical data) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known information, belimumab is a human IgG1λ monoclonal antibody that selectively blocks soluble BLyS (B-lymphocyte stimulator, also known as BAFF — B-cell activating factor of the TNF family). By neutralizing BLyS, belimumab reduces the survival and differentiation of autoreactive B cells, thereby lowering pathological autoantibody titers. Its established efficacy in SLE — a prototypical B-cell-driven autoimmune disease — provides the conceptual bridge to other autoimmune conditions involving aberrant B-cell activity.

The mechanistic rationale for primary release disorder of platelets rests on the hypothesis that a subset of cases may involve an immune-mediated component. Analogous to immune thrombocytopenia (ITP), where anti-platelet IgG antibodies targeting GPIb or GPIIb-IIIa impair platelet function, BLyS/BAFF inhibition could theoretically suppress the autoreactive B cells responsible for generating anti-platelet autoantibodies — potentially restoring normal platelet granule release. The only retrieved trial (NCT01610492) demonstrates belimumab's capacity to suppress B-cell-driven autoantibody production in a different autoimmune context (idiopathic membranous glomerulonephropathy), lending indirect mechanistic plausibility.

However, this remains a conditional extrapolation. Primary release disorder of platelets is a heterogeneous category; the majority of cases are hereditary (dense granule deficiency, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome) and driven by structural or genetic defects rather than autoimmune mechanisms. Biological plausibility therefore depends entirely on confirming whether an immune-mediated subtype — with demonstrable anti-platelet autoantibodies — exists in a given patient population. Without this stratification, BLyS/BAFF inhibition lacks a mechanistic anchor.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label study of belimumab 10 mg/kg IV in anti-PLA2R autoantibody-positive idiopathic membranous glomerulonephropathy. Evaluated efficacy, safety and mechanism of B-cell suppression. **Relevance grade C** — targets a different autoimmune renal disease; provides indirect evidence of belimumab's capacity to reduce pathological autoantibody titers, but contains no platelet-specific endpoints or data. |

> No clinical trials directly investigating belimumab in primary release disorder of platelets were identified.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Belimumab is currently **not registered** with the Saudi Food and Drug Authority (SFDA). No approved products or marketing authorizations are on record.

---

## Safety Considerations

Detailed warning and contraindication data from local regulatory sources are not available in this evidence pack. Please refer to the manufacturer's package insert (Benlysta®) for complete safety information. Key areas to review include:

- **Serious and opportunistic infections** — risk of fatal infections; hold during active severe infections
- **Hypersensitivity and infusion-related reactions** — acute and delayed reactions reported
- **Progressive multifocal leukoencephalopathy (PML)** — rare but serious neurological risk
- **Neuropsychiatric events** — depression and suicidality signals in post-marketing data
- **Pregnancy** — FDA Category C; animal studies show neonatal B-cell depletion and immunosuppression; use in pregnant women (especially relevant to the FNAIT indication ranked #4) is a hard contraindication
- **Malignancy risk** — theoretical concern with prolonged B-cell suppression

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole identified trial (NCT01610492) targets idiopathic membranous glomerulonephropathy — a mechanistically adjacent but clinically distinct autoimmune disease — and provides no direct evidence for primary release disorder of platelets. The high TxGNN score (99.96%) likely reflects topological proximity of platelet-disorder nodes in the knowledge graph rather than indication-specific mechanistic signal. With zero direct clinical data and unconfirmed immune-mediated pathology in the target disease, advancement would be premature.

**To proceed, the following is needed:**

- **Subtype confirmation**: Determine whether an autoimmune/anti-platelet-antibody-mediated subtype of primary release disorder of platelets exists and estimate its prevalence; this is the single gating question for biological plausibility
- **MOA data**: Retrieve complete belimumab mechanism of action from DrugBank to support formal mechanistic linkage analysis
- **Regulatory safety data**: Obtain full SFDA or TFDA package insert to complete S1 safety screening (currently blocking per DG001)
- **Comparator landscape**: Assess whether rituximab or other B-cell-depleting agents have been studied in this indication, to inform positioning and avoid duplicating failed attempts
- **Biomarker strategy**: If the immune-mediated subtype is confirmed, define anti-platelet antibody titer (anti-GPIb/GPIIb-IIIa IgG) as a patient selection biomarker before designing any exploratory study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

