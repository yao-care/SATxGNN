---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone (NTBC) is an HPD-enzyme inhibitor established for treating Hereditary Tyrosinemia Type 1 (HT-1), a rare inborn error of tyrosine metabolism. The TxGNN model predicts it may also address **Renal Tubular Acidosis**, reflecting the drug's known renoprotective effect in HT-1 patients, with **0 clinical trials** and **2 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (inferred from supporting literature; not present in structured regulatory data) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Nitisinone (NTBC) inhibits 4-hydroxyphenylpyruvate dioxygenase (HPD), blocking an upstream step of the tyrosine degradation pathway and preventing accumulation of toxic metabolites such as succinylacetone. This is the mechanistic basis of its established use in Hereditary Tyrosinemia Type 1 (HT-1).

In HT-1, these toxic metabolites directly damage the renal proximal tubule, producing a Fanconi-syndrome-like renal tubular acidosis (RTA). Because NTBC therapy addresses the root metabolic defect driving HT-1, it plausibly resolves this secondary renal tubular dysfunction as well — which is what the supporting literature describes.

This predicted indication should therefore be understood as a **renoprotective effect secondary to treating HT-1**, not evidence that NTBC treats RTA of other etiologies (e.g., primary distal/proximal RTA, autoimmune-associated RTA). Any use of this prediction should be scoped strictly to RTA occurring in the context of HT-1.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular genetics and metabolism | Describes early effect of NTBC on renal tubular dysfunction in HT-1 patients; NTBC therapy improves renal tubular parameters alongside its established hepatic benefit. |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case series | Indian journal of gastroenterology | Case series of 4 children with tyrosinemia treated with NTBC; those on long-term therapy showed normal liver function, undetectable urine succinylacetone, and no renal tubular complications. |

## Saudi Arabia Market Information

Nitisinone currently holds no marketing authorization in Saudi Arabia (0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is biologically well-grounded — NTBC's role in halting toxic tyrosine metabolite accumulation directly explains the observed renal tubular benefit — but the supporting evidence is limited to one cohort study and one case series (L3), with no dedicated trials, and the effect is documented specifically in HT-1 patients rather than in a general RTA population.

**To proceed, the following is needed:**
- TFDA/regulatory package insert with warnings and contraindications (currently a Blocking data gap)
- Formal DrugBank/mechanism-of-action confirmation (currently a High-severity data gap)
- Clarification that any repurposing indication be scoped to "RTA secondary to HT-1," not general RTA
- Saudi Arabia regulatory and market-access assessment, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

