---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Pancreatic Agenesis

## One-Sentence Summary

Insulin human is the foundational exogenous insulin replacement therapy for diabetes mellitus. Among the 10 new indications TxGNN predicted for this drug, most of the top-scored candidates (autoimmune oophoritis, stiff person syndrome spectrum, several lipodystrophies) have **no supporting evidence**, and some may reflect a causal-direction confusion (insulin injection is a known *cause* of localized lipoatrophy, not a treatment for it). The only candidate reaching a meaningful evidence stage is **Pancreatic Agenesis** — ranked 9th by TxGNN score but the sole indication with an evidence level of **L3** and **19 supporting publications**, because insulin deficiency is the direct clinical consequence of this condition.

> **Note on selection**: This report evaluates Pancreatic Agenesis rather than the #1-ranked TxGNN prediction (Autoimmune Oophoritis), because the top-ranked candidate has zero clinical trials or literature support and a "Hold" recommendation. Pancreatic Agenesis is the only candidate in this evidence pack that advanced past S0.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (regulatory indication text not available in this evidence pack — `taiwan_regulatory.licenses` is empty) |
| Predicted New Indication | Pancreatic Agenesis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on known pharmacology, insulin human acts as an exogenous replacement for endogenous insulin, and its efficacy in diabetes mellitus is well established.

Pancreatic agenesis is a rare congenital disorder in which the pancreas fails to develop, causing absolute insulin deficiency and neonatal/early-onset diabetes. Because insulin human's core mechanism is direct hormone replacement, its applicability here is not a novel repurposing hypothesis but a **direct pharmacological extension**: patients with pancreatic agenesis lack endogenous insulin entirely and require exogenous insulin as standard of care, in the same way as other forms of severe insulin-deficient diabetes (e.g., Wolcott-Rallison syndrome, MODY5/HNF1B-related pancreatic phenotypes).

Importantly, the 19 supporting publications are largely background/mechanistic literature on pancreas development, monogenic diabetes syndromes, and insulin biology — not interventional trials of insulin specifically in pancreatic agenesis patients. This should be interpreted as **confirmation of an already-established treatment paradigm**, not evidence of a new therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23006325](https://pubmed.ncbi.nlm.nih.gov/23006325/) | 2012 | Basic/Genetics | J Clin Invest | Pancreas-specific deletion of GATA4/GATA6 in mice causes pancreatic agenesis, establishing the molecular basis of the human disorder |
| [21050479](https://pubmed.ncbi.nlm.nih.gov/21050479/) | 2010 | Review/Case Series | Orphanet J Rare Dis | Wolcott-Rallison syndrome: neonatal insulin-requiring diabetes with skeletal dysplasia, most common cause of neonatal diabetes in consanguineous families |
| [33527355](https://pubmed.ncbi.nlm.nih.gov/33527355/) | 2021 | Genetics | J Pathol | Mouse model of MODY5/HNF1B pancreatic phenotype, relevant to monogenic pancreatic insufficiency |
| [10960489](https://pubmed.ncbi.nlm.nih.gov/10960489/) | 2000 | Review | Pediatr Res | Reviews how impaired pancreatic development links to adult-onset diabetes |
| [3286444](https://pubmed.ncbi.nlm.nih.gov/3286444/) | 1988 | Review/Genetics | Horm Metab Res | Mutant insulin syndromes presenting with abnormal endogenous insulin/proinsulin molecules |
| [29687501](https://pubmed.ncbi.nlm.nih.gov/29687501/) | 2018 | Review | Diabet Med | Cystic fibrosis-related diabetes as another insulin-deficient state requiring insulin therapy |
| [27189025](https://pubmed.ncbi.nlm.nih.gov/27189025/) | 2015 | Review | Nat Rev Dis Primers | General review of Type 2 diabetes mellitus pathophysiology and management (background) |
| [39326417](https://pubmed.ncbi.nlm.nih.gov/39326417/) | 2024 | Basic/Translational | Cell | Stem-cell-derived islet transplantation achieved insulin independence in a Type 1 diabetes patient |
| [32618633](https://pubmed.ncbi.nlm.nih.gov/32618633/) | 2020 | Review | Curr Opin Endocrinol Diabetes Obes | Beta-cell dysfunction in early Type 1 diabetes |
| [24559925](https://pubmed.ncbi.nlm.nih.gov/24559925/) | 2014 | Review | Vitam Horm | Zinc transporters and their role in pancreatic beta-cell insulin metabolism |

*9 additional background publications (SARS-CoV-2/pancreatic islet effects, glucagon physiology, obesity studies, etc.) were excluded from this table as lower direct relevance.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `taiwan_regulatory`/`safety` fields for this drug are currently a Blocking data gap — TFDA/SFDA package insert warnings and contraindications have not yet been retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (DG001: TFDA/SFDA package insert warnings/contraindications) means this candidate cannot yet pass the S1 safety pre-assessment gate, regardless of indication-level evidence. Separately, Pancreatic Agenesis — the only indication in this pack with real evidentiary support (L3, 19 publications) — represents existing standard-of-care insulin replacement rather than a novel repurposing opportunity, so it should not be filed as a new indication claim. The remaining 9 predicted indications (led by the top-scored Autoimmune Oophoritis) have no clinical trial or literature support, and several (the lipodystrophy cluster) likely reflect a causal-direction artifact in the knowledge graph, since insulin injection is a known cause of localized lipoatrophy rather than a treatment for it.

**To proceed, the following is needed:**
- Retrieve TFDA/SFDA package insert (warnings, contraindications) to resolve DG001 before any safety pre-assessment
- Obtain formal mechanism-of-action documentation (DG002) from DrugBank
- If pursuing Pancreatic Agenesis further, reframe as "standard-of-care confirmation" rather than a repurposing candidate — no new clinical development pathway is implied
- Re-examine the lipodystrophy-cluster predictions for causal-direction errors before any further evidence collection is invested in them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

