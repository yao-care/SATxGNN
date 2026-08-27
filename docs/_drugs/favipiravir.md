---
layout: default
title: Favipiravir
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 3
---

# Favipiravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Favipiravir: From Antiviral Therapy to Infection-Associated Hemophagocytic Syndrome

## One-Sentence Summary

Favipiravir is a broad-spectrum RNA-dependent RNA polymerase (RdRp) inhibitor with known antiviral activity against RNA viruses; this evidence pack does not record a specific original indication or formal MOA entry for the drug. The TxGNN model predicts potential relevance to **hemophagocytic syndrome associated with an infection** (secondary HLH driven by RdRp-susceptible pathogens such as SFTS virus and Heartland virus), currently supported by **0 clinical trials** and **2 review-level publications**. Note: two other TxGNN-predicted indications (malignancy-associated HLH; a mitochondrial COX-deficiency disorder) received an equal or similar model score but carry **no supporting evidence and no plausible mechanistic link**, and are excluded from this report's primary recommendation (see rationale below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `original_indications` on file) |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action entry is not available for this drug in the evidence pack (`original_moa`: data gap). However, the TxGNN repurposing rationale itself supplies pharmacological context: Favipiravir acts as an RNA-dependent RNA polymerase (RdRp) inhibitor with activity against members of the *Bunyavirales* order, including SFTS virus and Heartland virus.

These viruses are known triggers of secondary (infection-associated) hemophagocytic lymphohistiocytosis (HLH) — a hyperinflammatory syndrome that can follow severe viral infection. The proposed link is therefore **indirect**: suppressing upstream viral replication could, in principle, remove the infectious trigger that drives the downstream immune-mediated HLH, rather than Favipiravir acting directly on HLH effector pathways (e.g., IFN-γ or JAK-STAT signaling).

This mechanistic path is biologically plausible but has not been directly tested — no clinical trials exist, and the two supporting publications are both narrative reviews of the underlying viral diseases (SFTS, Heartland virus), not studies of Favipiravir treating HLH itself. By contrast, the model assigned an equal score (0.9941) to "malignant disease-associated HLH," a condition with **no infectious trigger and no mechanistic connection** to an antiviral RdRp inhibitor — the evidence pack's own annotation attributes this to shared disease-ontology labeling rather than a real biological signal, and a third candidate (a mitochondrial cytochrome c oxidase deficiency) is likewise mechanistically unrelated. Both are treated as low-confidence artifacts here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30098914](https://pubmed.ncbi.nlm.nih.gov/30098914/) | 2018 | Review | Journal of Infection and Chemotherapy | Reviews SFTS virus pathophysiology and the rationale for specific antiviral therapy development in severe fever with thrombocytopenia syndrome, a Bunyavirales infection associated with secondary HLH. |
| [38399689](https://pubmed.ncbi.nlm.nih.gov/38399689/) | 2024 | Review | Microorganisms | Reviews Heartland virus disease (tick-borne Bunyavirales infection), including its hematologic complications (leukopenia, thrombocytopenia); underscores the underrecognized burden of this infection class. |

## Saudi Arabia Market Information

Favipiravir is not currently marketed in Saudi Arabia; no product authorizations are on file.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications and DDI data are marked as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any S1 safety review can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 (mechanistic/preclinical inference only) with zero clinical trials and only two indirect review-level publications describing the underlying viral diseases, not Favipiravir's effect on HLH itself. The mechanistic link is plausible but unproven and indirect (antiviral suppression of an upstream trigger, not direct action on HLH pathology), and a Blocking safety data gap (TFDA label/warnings) prevents any safety evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): TFDA package insert warnings and contraindications
- Resolve DG002 (High): formal DrugBank-sourced mechanism of action confirmation
- Preclinical or case-series evidence directly linking Favipiravir treatment to HLH outcomes in Bunyavirales-associated infection (not just treatment of the underlying viral infection)
- DDI data, since current query returned "not found"
- Clarification of Favipiravir's original approved indication(s), currently absent from this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

