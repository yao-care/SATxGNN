---
layout: default
title: Vidarabine
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 3
---

# Vidarabine
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

# Vidarabine: From Herpesvirus Infections (HSV/VZV) to Actinic Cheilitis

## One-Sentence Summary

Vidarabine is a nucleoside analog antiviral historically used against herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections. The TxGNN model's top-ranked prediction suggests possible efficacy for **Actinic Cheilitis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no corroborating evidence. Two secondary candidates from the same screen (angular cheilitis, drug-induced osteoporosis) are summarized below; angular cheilitis has one case report, but it documents a treatment **failure**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured data (original_indications field empty; original_moa flagged as Data Gap) |
| Predicted New Indication | Actinic Cheilitis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action data is available for vidarabine in this evidence pack (DrugBank MOA field flagged as a High-severity data gap, DG002). However, the repurposing rationale notes captured alongside each prediction describe vidarabine as an adenine nucleoside analog that, once phosphorylated intracellularly, competitively inhibits viral DNA polymerase — giving it activity against HSV and VZV. Notably, this activation does not depend on viral thymidine kinase (TK), which theoretically preserves activity against TK-deficient, acyclovir-resistant HSV strains.

This mechanism has no established connection to the top-ranked prediction, **actinic cheilitis**, which is a UV-induced premalignant keratinocyte dysplasia of the lip unrelated to viral infection. The same is true for **drug-induced osteoporosis**, where no pharmacological link to nucleoside antiviral activity is documented. The one candidate with a plausible mechanistic thread is **angular cheilitis**, since a minority of cases are HSV-1 related — but the only available clinical evidence for this indication is a case report in which vidarabine ointment *failed* to control an acyclovir-resistant HSV-1 infection (treatment ultimately succeeded with amenamevir instead).

Overall, the high TxGNN scores across these three candidates (all >99%) appear to be driven by embedding-level lexical/semantic similarity (e.g., "cheilitis") rather than by a validated pharmacological mechanism, and should be interpreted as hypothesis-generating only.

---

## Clinical Trial Evidence

**Actinic Cheilitis:** Currently no related clinical trials registered.

**Angular Cheilitis:** Currently no related clinical trials registered.

**Drug-Induced Osteoporosis:** Currently no related clinical trials registered.

---

## Literature Evidence

**Actinic Cheilitis:** Currently no related literature available.

**Angular Cheilitis:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38895086](https://pubmed.ncbi.nlm.nih.gov/38895086/) | 2024 | Case Report | EJHaem | Post-transplant patient with acyclovir-resistant HSV-1 angular cheilitis; vidarabine ointment (along with acyclovir and ganciclovir) **failed** to control the infection; resolved only after switching to amenamevir. |

**Drug-Induced Osteoporosis:** Currently no related literature available.

---

## Saudi Arabia Market Information

Vidarabine holds no market authorizations in Saudi Arabia (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications rest on model score alone (L5) or a single negative case report (L4 for angular cheilitis, S1) — none meet the bar of prospective clinical evidence. The one indication with real-world clinical data (angular cheilitis) shows vidarabine failing to achieve therapeutic effect. Combined with the absence of Saudi Arabia market presence and a Blocking-severity data gap on TFDA/package-insert safety information, there is currently no basis to advance any of these candidates past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Structured drug mechanism-of-action data from DrugBank — currently a High-severity data gap (DG002)
- Prospective clinical or in vitro mechanistic data specifically linking vidarabine to actinic cheilitis or drug-induced osteoporosis, given no current evidence exists
- If pursuing angular cheilitis, additional cases beyond the single negative report before drawing conclusions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

