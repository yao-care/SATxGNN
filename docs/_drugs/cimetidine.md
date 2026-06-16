---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a first-generation histamine H2-receptor antagonist, established since the 1970s as a foundational treatment for peptic ulcer disease and gastric acid hypersecretion.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SSM)**,
with **no clinical trials** and **no publications** currently identified to directly support this specific application — the prediction rests entirely on mechanistic plausibility derived from knowledge-graph connections.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic Ulcer Disease (H2-receptor antagonist) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, cimetidine is the prototype competitive histamine H2-receptor antagonist — it blocks H2 receptors on gastric parietal cells to markedly suppress acid secretion. Importantly, cimetidine also possesses secondary properties beyond acid suppression: it exhibits weak anti-androgenic activity and exerts immunomodulatory effects via H2 receptor blockade on lymphocytes, natural killer cells, and regulatory T cells — properties not shared by newer H2 blockers such as ranitidine.

In Smouldering Systemic Mastocytosis (SSM), abnormally accumulating mast cells chronically release excessive histamine, prostaglandins, and tryptase. Histamine acting on both H1 and H2 receptors drives some of the most disabling symptoms in this condition: epigastric pain, peptic ulcer-like disease, diarrhoea, flushing, and nausea. Because of this, combined H1 + H2 antihistamine blockade is already considered standard symptomatic management in systemic mastocytosis broadly — which places cimetidine squarely within a pharmacologically plausible treatment framework for SSM-related symptoms.

The TxGNN model's high score (99.80%) almost certainly reflects strong knowledge-graph linkages across the mastocytosis → histamine excess → H2-receptor axis. However, no clinical trial or publication specifically addressing cimetidine in SSM was identified in the evidence search. The prediction represents biological plausibility, not demonstrated clinical benefit in this subtype. Cimetidine's potential role here would be purely symptomatic — reducing histamine-mediated gastrointestinal burden — and would not address the underlying mast cell burden or disease progression of SSM.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Drug interaction data was not retrievable for this report. Cimetidine is a known CYP450 inhibitor (CYP1A2, CYP2C9, CYP2D6, CYP3A4) and clinically significant interactions with co-administered drugs should be assessed before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at L5 — model prediction only. No clinical trials or publications specifically address cimetidine in Smouldering Systemic Mastocytosis. While H2 blockade is pharmacologically plausible and already incorporated into broad mastocytosis symptom management guidelines, the SSM subtype specifically has not been studied in this context, and the drug is not marketed in Saudi Arabia.

**To proceed, the following is needed:**

- Systematic review of H2 antagonists (class-level evidence) in broader systemic mastocytosis populations — existing guidelines may already support H2 blocker use, which would upgrade the evidence level
- Mechanism of action confirmation from DrugBank (DB00501), particularly for immunomodulatory and anti-androgenic properties relevant to SSM
- Safety profile from the package insert, with emphasis on long-term use risks and CYP450-mediated drug interactions (critical in SSM patients often on multiple agents)
- An observational registry study or retrospective chart review in SSM patients receiving combined H1 + H2 therapy to quantify symptomatic benefit versus H1 monotherapy
- Regulatory feasibility assessment for Saudi Arabia market entry, since no current authorisations exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

