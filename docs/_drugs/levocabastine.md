---
layout: default
title: Levocabastine
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 2
---

# Levocabastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Levocabastine: From Allergic Rhinitis/Conjunctivitis to Allergic Urticaria

## One-Sentence Summary

> Levocabastine is a selective H1-antihistamine currently formulated only as a nasal spray (allergic rhinitis) and eye drops (allergic conjunctivitis).
> The TxGNN model predicts it may be effective for **allergic urticaria**,
> but this direction is currently supported by only **0 clinical trials** and **2 publications**, neither of which directly studies urticaria.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (intranasal) / allergic conjunctivitis (ophthalmic) — topical formulations only; no formal Saudi Arabia license record available |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA: data gap). Based on known information, levocabastine is a selective H1-receptor antagonist, marketed only in topical intranasal and ophthalmic forms for allergic rhinitis and allergic conjunctivitis, both IgE/mast-cell–mediated conditions.

Allergic urticaria shares the same core pathophysiology — mast-cell degranulation releasing histamine that activates H1 receptors in the skin — so the pharmacological rationale for cross-applicability is plausible in principle.

However, the two supporting publications do not directly study urticaria: one is a nasal-allergen-challenge RCT in allergic rhinitis, and the other is a pharmacokinetic review of H1-antihistamines as a class. There is also an unresolved route-of-administration gap — it is unclear whether a topical (nasal/ophthalmic) formulation can achieve the systemic exposure needed to treat urticaria, or whether a new formulation would be required. The evidence therefore supports the mechanism indirectly, not the indication directly.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8938880](https://pubmed.ncbi.nlm.nih.gov/8938880/) | 1996 | RCT | Rhinology | Double-blind, placebo-controlled, cross-over trial in 22 allergic rhinitis patients; intranasal levocabastine significantly reduced sneezing severity (p<0.001) in a nasal allergen challenge model. Not urticaria-specific. |
| [1685361](https://pubmed.ncbi.nlm.nih.gov/1685361/) | 1991 | Review | Clinical Pharmacokinetics | Reviews pharmacokinetics/pharmacodynamics of second-generation H1-antihistamines (including levocabastine) used for allergic rhinoconjunctivitis and chronic urticaria as a drug class; no urticaria-specific data on levocabastine itself. |

## Saudi Arabia Market Information

Levocabastine is not currently marketed in Saudi Arabia; no authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (mechanistic rationale only, no clinical trial or urticaria-specific literature), and a Blocking data gap on TFDA warnings/contraindications prevents the candidate from clearing the S1 safety pre-screen.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) to clear the S1 safety review
- Confirmed mechanism-of-action data from DrugBank
- Urticaria-specific clinical or preclinical evidence (current literature only addresses rhinitis and PK review)
- Assessment of whether existing topical (nasal/ophthalmic) formulations can achieve exposure sufficient for urticaria, or whether new formulation development is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

