---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

Using the evidence pack as given. Two flags worth stating up front before the report: (1) `predicted_indications[0]` (focal stiff limb syndrome, score 99.88%) has zero supporting trials/literature and its own `mechanistic_link` text explicitly says the score is likely a knowledge-graph artifact via the diabetes node — same for ranks 2–9. Ranks 1–9 are all L5/Hold with no real evidence. Rank 10 (Type 1 Diabetes Mellitus) is the only prediction with actual trial and literature support (L2, one completed Phase 2 RCT). Writing the report around rank 1 would be misleading for a decision document, so I built it around the evidence-backed candidate (T1DM) and flagged the noise-ranks separately, rather than following the literal `predicted_indications[0]` instruction into a report with no real content.

---

# Vildagliptin: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Vildagliptin is a DPP-4 inhibitor originally developed for Type 2 Diabetes Mellitus, with an extensive T2DM clinical trial record.
> The TxGNN model's top nine ranked predictions (stiff person syndrome spectrum, lipodystrophies, opsismodysplasia, pancreatic agenesis) carry no supporting evidence and are most likely knowledge-graph artifacts tied to the "diabetes" node.
> The one prediction with real substance is **Type 1 Diabetes Mellitus** (rank 10), supported by **2 directly relevant clinical trials** and **10 pieces of literature**, including one completed Phase 2 RCT testing vildagliptin (with rapamycin) for β-cell preservation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from extensive T2DM trial record in evidence pack; no formal label text available — see below) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from a formal source (e.g. package insert) is not available for vildagliptin. Based on the literature captured in this evidence pack, vildagliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor: it blocks degradation of the incretin hormones GLP-1 and GIP, raising their post-meal concentrations. This suppresses inappropriate glucagon secretion during hyperglycemia and supports residual β-cell insulin secretion — the mechanism that has made it effective in Type 2 Diabetes.

Type 1 Diabetes is pathophysiologically different (autoimmune β-cell destruction rather than insulin resistance), but patients — especially early in disease or with residual β-cell function ("honeymoon phase" or long-standing T1D with partial preservation) — may still benefit from glucagon suppression and incretin-mediated support of remaining β-cell function. This is the rationale reflected in the literature: DPP-4 inhibition has been shown to reduce glucagon during hyperglycemia while preserving glucagon counter-regulation during hypoglycemia in T1D patients, and combination with immune-modulating agents (rapamycin) has been tested specifically to recover β-cell function in long-standing T1D.

Importantly, most of the mechanistic and clinical evidence for T1D comes from vildagliptin used **as an adjunct** (to rapamycin, or as add-on therapy in closed-loop insulin systems), not as monotherapy replacing insulin. This meaningfully narrows the plausible use case from "treatment of T1D" to "adjunctive glycemic/β-cell support in T1D."

---

## Clinical Trial Evidence

Of the 50 trials returned for the "vildagliptin + Type 1 Diabetes" query, 48 were Type 2 Diabetes trials returned as search noise (graded "C — not relevant" in the source data) and are excluded here. Only two trials directly targeted a T1D population:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) | Phase 2 | Completed | 55 | Randomized, double-blind, placebo-controlled, 3-arm trial testing 4 weeks rapamycin, and rapamycin + 3 months vildagliptin, vs. placebo to increase endogenous insulin production and correct glycemic lability in long-standing T1D. |
| [NCT06021119](https://clinicaltrials.gov/study/NCT06021119) | Phase 3 | Completed | 50 | Vildagliptin as add-on therapy in adolescents/young adults with T1D on MiniMed 780G closed-loop system, to reduce Ramadan Iftar-related glucose excursions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT | J Clin Endocrinol Metab | Double-blind RCT: rapamycin + vildagliptin to restore β-cell function in long-standing T1D (publication of NCT02803892). |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | RCT/Mechanistic | J Clin Endocrinol Metab | Vildagliptin reduces glucagon during hyperglycemia while sustaining glucagon counter-regulation during hypoglycemia in T1D. |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | RCT | Diabetol Metab Syndr | Adjunctive oral vildagliptin during Ramadan fasting reduces Iftar-related glycemic excursions in adolescents/young adults with T1D on AHCL systems (publication of NCT06021119). |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | RCT | Diabetes Obes Metab | Vildagliptin add-on in adolescents with T1D and NASH: effects on MMP-14, liver stiffness, and subclinical atherosclerosis. |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Review | Expert Opin Investig Drugs | DPP-4 inhibitors modulate β-cell function in T1D and offer renal-protective effects in diabetic kidney disease. |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Review | Front Endocrinol | Mechanistic review of vildagliptin's effects on GLP-1/GIP signaling. |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Animal study | Curr Pharm Biotechnol | Vildagliptin induces β-cell neogenesis and improves lipid profile in a later phase of T1D (alloxan rat model). |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Animal study | Can J Physiol Pharmacol | Vildagliptin/pioglitazone combination improved glycemic control in T1D rats. |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Animal study | Arch Med Res | Vildagliptin ameliorates oxidative stress and pancreatic β-cell destruction in T1D rats. |
| [40562805](https://pubmed.ncbi.nlm.nih.gov/40562805/) | 2025 | Animal study | Sci Rep | Vildagliptin and linagliptin inhibit NLRP3-mediated pyroptosis in lung injury in T1D rats. |

---

## Saudi Arabia Market Information

Vildagliptin has no marketing authorization in Saudi Arabia in this dataset (0 licenses, market status "Not marketed"). No product/authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — including a **Blocking**-severity gap on TFDA/SFDA label warnings and contraindications, which must be resolved before any S1 safety review can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The T1D signal (rank 10) has genuine mechanistic and clinical backing — one completed Phase 2 RCT and a completed Phase 3 adjunct trial — but both studies test vildagliptin as an **add-on** (to rapamycin, or to closed-loop insulin therapy) rather than as a treatment replacing standard T1D care, and the evidence base is still small (n=55 and n=50). Combined with a Blocking-severity safety data gap and the drug currently having no marketing authorization in Saudi Arabia, this is not yet actionable — it is a research question, not a repurposing candidate ready for regulatory or clinical planning.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently Blocking
- Formal MOA documentation from DrugBank or SFDA source (currently Data Gap)
- Larger/confirmatory T1D trials evaluating vildagliptin specifically for β-cell preservation or adjunct glycemic control, not just T2DM-labeled trials misattributed by search
- Drug interaction data specific to T1D adjunct use (e.g., with insulin, closed-loop systems)
- Clarification on whether ranks 1–9 (stiff person syndrome spectrum, lipodystrophies, opsismodysplasia, pancreatic agenesis) reflect a TxGNN scoring/embedding issue worth flagging to the model team, since none carry any supporting evidence despite near-identical top-tier scores to the one credible prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

