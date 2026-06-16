---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
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

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is a combination of diphenhydramine and 8-chlorotheophylline, classically used for prevention and treatment of motion sickness, nausea, and vomiting.
The TxGNN model predicts it may be effective for **Allergic Urticaria**,
with **0 clinical trials** and **1 pharmacokinetics publication** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Motion sickness, nausea, and vomiting |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Dimenhydrinate is a salt formulation comprising two active components: **diphenhydramine** (a first-generation H1 receptor antagonist) and **8-chlorotheophylline** (a mild CNS stimulant added to offset the sedating effect of diphenhydramine). The therapeutic rationale for motion sickness relies primarily on diphenhydramine's anticholinergic and antihistaminergic properties acting at the vestibular apparatus.

The mechanistic link to allergic urticaria is credible at the level of the diphenhydramine component: H1 receptor blockade competitively inhibits histamine binding, thereby suppressing mast cell–mediated vasodilation, pruritus, and wheal formation — which constitute the core pathophysiology of allergic urticaria. First- and second-generation H1 antihistamines are the first-line recommendation in EAACI/WAO urticaria treatment guidelines.

However, the case for **Dimenhydrinate specifically** (rather than diphenhydramine alone) is weak. The 8-chlorotheophylline component provides no known benefit in urticaria and carries potential risks including cardiac arrhythmia and CNS stimulation. Furthermore, first-generation antihistamines are increasingly supplanted by second-generation agents (e.g., cetirizine, fexofenadine) for urticaria due to their superior safety profile. The TxGNN prediction likely reflects the H1-blocking activity of the diphenhydramine moiety rather than a unique property of dimenhydrinate as a compound.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | PK Study | Veterinary Dermatology | Compared oral/IV pharmacokinetics of diphenhydramine and oral dimenhydrinate in healthy dogs; assessed pharmacodynamic suppression of histamine-induced wheal formation. Found dimenhydrinate may provide superior oral bioavailability of diphenhydramine but results were in an animal model only (pilot study). |

---

## Saudi Arabia Market Information

Dimenhydrinate is not currently registered or marketed in Saudi Arabia. No product authorizations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically plausible through the diphenhydramine component of dimenhydrinate, but the current evidence base consists of a single pilot pharmacokinetics study in dogs with no clinical human data for allergic urticaria. Additionally, the 8-chlorotheophylline component adds safety complexity without any known benefit for this indication, and the drug is not registered in Saudi Arabia.

**To proceed, the following is needed:**
- Clarify whether the intended clinical question is about **dimenhydrinate as a whole** or its active moiety **diphenhydramine** — the latter already has established evidence in urticaria, which would change the evidence level significantly
- Obtain formal MOA and safety data (package insert warnings, contraindications) from DrugBank or the SFDA package insert
- Conduct a targeted literature review for diphenhydramine in allergic urticaria to assess whether the H1-blocking evidence can be bridged to dimenhydrinate
- Evaluate whether a regulatory pathway exists in Saudi Arabia for the urticaria indication, given the current zero-license status
- If proceeding, a Phase 2 proof-of-concept clinical trial or comparative PK/PD study in humans would be the minimum threshold to advance beyond L4
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

