---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic with broad-spectrum gram-negative bactericidal activity, widely used for serious bacterial infections including urinary tract infections, pneumonia, and septicemia.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **0 clinical trials** and **1 publication** currently supporting this direction.
The mechanistic link is highly indirect, and the available evidence is insufficient to advance this prediction beyond an exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (no Saudi Arabia registration on record) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, ceftazidime is a third-generation cephalosporin β-lactam antibiotic; its efficacy in treating serious gram-negative bacterial infections — including those caused by *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*, and *Escherichia coli* — has been well established in clinical practice, and mechanistically it may be applicable to conditions where secondary bacterial infection triggers an inflammatory cascade leading to serum amylase elevation.

Hyperamylasemia is a biochemical marker (elevated serum amylase) rather than an independent disease entity. It most commonly signals acute pancreatitis or post-ERCP complications. The theoretical link between ceftazidime's antibacterial mechanism and serum amylase reduction is indirect: preventing bacterial translocation or bacteremia could theoretically limit the pancreatic inflammatory response that drives amylase release — but this causal chain has not been directly studied.

The sole supporting literature (PMID 11985972) evaluates whether routine prophylactic antibiotics — as a multimodal regimen, not ceftazidime specifically — reduce the incidence of post-ERCP pancreatitis. The study does not designate hyperamylasemia as a primary endpoint, and ceftazidime's individual contribution is indistinguishable from the combined antibiotic effect. The mechanistic connection therefore remains weak and inferential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | RCT (multi-antibiotic scheme; ceftazidime not studied in isolation) | Journal of Gastrointestinal Surgery | Prospective study evaluating whether prophylactic antibiotics reduce post-ERCP cholangitis and pancreatitis; provides indirect evidence that antibiotic prophylaxis may limit amylase-elevating inflammatory events, but does not assess ceftazidime as the active agent nor hyperamylasemia as a primary endpoint |

---

## Saudi Arabia Market Information

No authorizations registered in Saudi Arabia.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hyperamylasemia is a biochemical surrogate marker rather than a discrete therapeutic target, and the only supporting evidence is a single multi-antibiotic RCT that does not isolate ceftazidime's effect nor designate amylase elevation as a primary endpoint — this is insufficient mechanistic or clinical basis to proceed.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank to characterize whether any off-target pharmacology could influence pancreatic enzyme release
- Safety data (key warnings, contraindications) retrieved from the package insert PDF
- Reconsideration of whether the more appropriate clinical framing is **post-ERCP pancreatitis prevention** rather than hyperamylasemia per se, which would require a dedicated prospective study with amylase level as a co-primary endpoint
- Assessment of whether the higher-evidence indications in this evidence pack — particularly **urinary tract infection** (L2, Proceed with Guardrails) and **infectious otitis media** (L3, Proceed with Guardrails) — should be prioritized over this rank-1 prediction for regulatory and clinical development purposes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

