---
layout: default
title: Trihexyphenidyl
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism/Extrapyramidal Symptoms to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Trihexyphenidyl is a classic anticholinergic agent conventionally used for Parkinsonism and drug-induced extrapyramidal symptoms; however, its **confirmed original indication and mechanism-of-action data are not available in the current evidence pack** (flagged as data gaps). The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, with a prediction score of **99.92%**, but this is currently supported by only **1 loosely related publication** and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (drug is not marketed in this jurisdiction; no approved indication text on file) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trihexyphenidyl is currently unavailable (data gap), and this evidence pack contains no confirmed original indication record — the drug shows zero market authorizations and no license history. In general pharmacological terms, trihexyphenidyl is known as an antimuscarinic (anticholinergic) agent classically used for Parkinsonian and drug-induced extrapyramidal symptoms, but this background is not substantiated by the source data here and should be independently verified before use.

The single literature item retrieved for the ADHD prediction (PMID 21506147) is a case series on primary tic disorder co-occurring with dystonia — it does not directly study trihexyphenidyl for ADHD treatment. Pharmacologically, anticholinergic agents are more associated with central cognitive/attentional suppression than improvement, which runs counter to the therapeutic direction needed for ADHD. The high TxGNN score most plausibly reflects a learned association between tic-disorder/dystonia and ADHD comorbidity patterns in the knowledge graph, rather than direct mechanistic or clinical evidence supporting a treatment effect.

Given the absence of confirmed MOA and original-indication data, combined with the mismatch between the cited literature's subject and the predicted indication, this candidate should be treated as a low-confidence signal requiring further mechanistic and clinical validation before any development consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series (Tier 3) | Movement Disorders | Describes a series of patients with primary tic disorder and persistent dystonia; does **not** directly address ADHD or trihexyphenidyl efficacy in ADHD |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted ADHD indication is supported by only one publication that does not directly address ADHD or trihexyphenidyl's efficacy in it, with zero clinical trials and no confirmed mechanism-of-action or original-indication data. The available rationale suggests the signal may reflect a comorbidity association in the knowledge graph rather than a genuine treatment effect, and evidence is insufficient to advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking data gap — DG001; source: TFDA official site, PDF parsing)
- Confirmed mechanism-of-action data (High-priority data gap — DG002; source: DrugBank API)
- Clinical or mechanistic studies directly evaluating trihexyphenidyl in ADHD (current literature is off-target)
- Confirmed original approved indication and regulatory history to establish a baseline safety/efficacy profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

