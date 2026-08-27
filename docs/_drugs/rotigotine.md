---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

> Rotigotine is a non-ergot dopamine receptor agonist approved for Parkinson's disease and restless legs syndrome (RLS).
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> currently supported only by **0 clinical trials** and **3 mechanistic/review publications** — no direct human evidence exists yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease / Restless legs syndrome (RLS) — not captured in the current evidence pack; local (this-market) license data is unavailable since the drug is not marketed here |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L4 |
| Local Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for rotigotine is flagged as a data gap in this evidence pack. Based on established pharmacological knowledge referenced in the repurposing rationale, rotigotine is a non-ergot dopamine receptor agonist with affinity D3 > D2 > D1, and it also carries partial α2-adrenergic agonist activity. It is approved as a transdermal patch for Parkinson's disease and RLS.

The link to ADHD rests on two threads rather than a direct clinical precedent. First, RLS and ADHD frequently co-occur in pediatric populations, giving an epidemiological (not causal) bridge between the drug's approved indication and the candidate indication. Second, ADHD pathophysiology is widely attributed to prefrontal-striatal dopaminergic hypofunction, with the dopamine D4 receptor polymorphism (DRD4) specifically implicated — and drugs acting on the α2A adrenoceptor (e.g., guanfacine) are already used clinically in ADHD.

One literature source (PMID 34182128) shows that α2A adrenoceptors heteromerize with polymorphic variants of the D4 receptor, altering pharmacological/functional response in a way relevant to impulsive-control disorders including ADHD. Since rotigotine engages both dopamine receptors and α2-adrenergic sites, this provides a plausible — but entirely theoretical — mechanistic rationale. No study has tested rotigotine directly in ADHD patients or animal models; the connection is inferred from receptor pharmacology, not empirical outcome data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic/Receptor Pharmacology | Pharmacological Research | α2A adrenoceptor–dopamine D4 receptor heteromerization shapes pharmacological/functional differences relevant to impulsive-control disorders including ADHD |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Review of RLS in children and pharmacological treatment options; notes clinical overlap between pediatric RLS and ADHD |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General overview of RLS pathophysiology and diagnostic criteria; background context for RLS-ADHD comorbidity, no direct ADHD treatment data |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — one of which, local package-insert warnings/contraindications, is flagged as a **Blocking** gap that must be resolved before any safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (shared dopaminergic/α2-adrenergic pharmacology, RLS-ADHD comorbidity) is biologically plausible but remains purely theoretical — there are zero clinical trials, case reports, or even preclinical studies testing rotigotine directly in ADHD. Combined with a Blocking safety data gap (no local package-insert warnings/contraindications available) and the fact that rotigotine is not currently marketed in this jurisdiction, the evidence does not support advancing past the research-question stage.

**To proceed, the following is needed:**
- Local regulatory package-insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed, structured MOA data from DrugBank or equivalent source
- Preclinical/animal studies directly testing rotigotine (or its receptor profile) in ADHD models
- Any case reports or off-label use data in ADHD or comorbid RLS-ADHD pediatric populations
- Drug-drug interaction profile, since none is currently available (query returned not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

