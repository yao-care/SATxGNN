---
layout: default
title: Zafirlukast
parent: 僅模型預測 (L5)
nav_order: 670
evidence_level: L5
indication_count: 2
---

# Zafirlukast
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

# Zafirlukast: From Asthma to Obstructive Lung Disease

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor (CysLT1) antagonist internationally indicated for the prophylaxis and maintenance treatment of chronic asthma. The TxGNN model predicts it may also be effective for **Obstructive Lung Disease (including COPD)**, a direction already supported by **0 clinical trials formally registered under this indication label** but **20 relevant publications**, including two dedicated clinical studies testing zafirlukast directly in COPD patients.

*(Note: A second, much weaker signal — "bronchitis," TxGNN score 99.93%, rank 1742 — was also predicted, but currently has zero supporting trials or literature and is scored L5/Hold. It is not the focus of this report.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory records (drug not marketed in Saudi Arabia); internationally labeled for chronic asthma prophylaxis and treatment |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data from DrugBank is currently a data gap. However, the supporting literature consistently and specifically describes zafirlukast's pharmacology: it is a selective, competitive antagonist of the cysteinyl leukotriene 1 (CysLT1) receptor, blocking LTD4/LTC4/LTE4-mediated bronchoconstriction, mucus hypersecretion, increased vascular permeability, and eosinophilic airway inflammation.

Asthma and obstructive lung disease (including COPD) share overlapping airway pathophysiology — bronchoconstriction, mucus hypersecretion, and inflammatory cell infiltration — and cysteinyl leukotrienes contribute to both, though their relative role is smaller in COPD than in asthma. This shared mechanistic basis is why leukotriene receptor antagonists have long been studied as an extension beyond asthma.

Critically, this is not a purely theoretical extrapolation: dedicated clinical studies have already tested zafirlukast directly in COPD patients. A randomised, double-blind, placebo-controlled crossover study (PMID 12877822) found zafirlukast improved airway function within 1–3 hours in severe COPD, and a separate clinical study (PMID 23741166) evaluated its effect on lung function in COPD. This existing direct evidence is why the prediction reaches L2 rather than remaining at a model-only L5 level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11694805](https://pubmed.ncbi.nlm.nih.gov/11694805/) | 2001 | RCT | Respiration | Compared salmeterol + zafirlukast combination vs. monotherapy in asthma and COPD; bronchodilator effects were additive |
| [12877822](https://pubmed.ncbi.nlm.nih.gov/12877822/) | 2003 | RCT (crossover) | Pulm Pharmacol Ther | Randomised, double-blind, placebo-controlled crossover trial: zafirlukast improved airway function within 1–3h in severe COPD patients |
| [23741166](https://pubmed.ncbi.nlm.nih.gov/23741166/) | 2013 | Clinical study | Med J Islamic Repub Iran | Evaluated zafirlukast's effect on improving lung function in COPD patients |
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Reviews leukotriene pathway inhibitors, including zafirlukast, in asthma and COPD; leukotrienes drive bronchoconstriction, mucus production, and eosinophil recruitment |
| [10023966](https://pubmed.ncbi.nlm.nih.gov/10023966/) | 1999 | Review | Lancet | Overview of leukotriene-receptor antagonists (zafirlukast, montelukast); good antiasthma activity across severity spectrum |
| [9463793](https://pubmed.ncbi.nlm.nih.gov/9463793/) | 1998 | Review | Drugs | Comprehensive review of zafirlukast pharmacology and therapeutic potential in chronic asthma |
| [31544544](https://pubmed.ncbi.nlm.nih.gov/31544544/) | 2019 | Review | Expert Rev Respir Med | Update on LTRA treatments in asthma, summarizing cysteinyl leukotriene-driven airway inflammation mechanisms |
| [11888331](https://pubmed.ncbi.nlm.nih.gov/11888331/) | 2002 | PK Study | Clin Pharmacokinet | Characterizes the pharmacokinetic profile of zafirlukast, a CysLT1 antagonist with bronchodilator and anti-inflammatory action |
| [27826703](https://pubmed.ncbi.nlm.nih.gov/27826703/) | 2017 | Review | Handb Exp Pharmacol | Reviews LTRAs, including zafirlukast, for long-term asthma management, allergic rhinitis, and exercise-induced asthma |
| [33446622](https://pubmed.ncbi.nlm.nih.gov/33446622/) | 2020 | Review | Med Lett Drugs Ther | Concise practice guidance on asthma drugs, including leukotriene receptor antagonists |

---

## Saudi Arabia Market Information

Zafirlukast is currently not marketed in Saudi Arabia — no authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zafirlukast's anti-leukotriene mechanism is already directly supported by two dedicated placebo-controlled/comparative clinical studies conducted specifically in COPD patients, plus multiple reviews describing the shared CysLT-driven pathophysiology between asthma and obstructive lung disease — placing this candidate at evidence level L2 rather than a pure model prediction. However, the drug is not currently marketed in Saudi Arabia, and formal MOA and safety documentation remain outstanding, so guardrails are warranted before further advancement.

**To proceed, the following is needed:**
- Official DrugBank/regulatory-sourced mechanism of action data (currently unavailable)
- SFDA-issued package insert warnings, contraindications, and drug-drug interaction (DDI) profile
- Regulatory pathway assessment given the drug's "not marketed" status in Saudi Arabia
- Larger, confirmatory trials in obstructive lung disease/COPD specifically, as existing supporting studies are small-sample and short-duration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

