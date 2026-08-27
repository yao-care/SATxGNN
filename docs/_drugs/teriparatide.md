---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Pregnancy and Lactation-Associated Osteoporosis (PLO)

## One-Sentence Summary

Teriparatide (PTH 1-34) is a bone-forming agent originally developed for **severe osteoporosis**. Among the ten TxGNN-predicted indications in this evidence pack, most (duodenal ulcer, esophageal malformation, Worth syndrome, etc.) carry high raw prediction scores but **no mechanistic or clinical support** and are explicitly flagged in the model's own rationale as implausible. The one candidate with real-world clinical use and a growing evidence base is **Pregnancy and Lactation-Associated Osteoporosis (PLO)** — supported by **2 clinical trials** (indirect) and **20 publications**, several of which report teriparatide use specifically in PLO patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe osteoporosis (global indication; no local approved-label text available — see below) |
| Predicted New Indication | Pregnancy and Lactation-Associated Osteoporosis (PLO) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for teriparatide in this dataset (data gap DG002). Based on the information captured in the evidence pack's own repurposing rationale, teriparatide is a recombinant fragment of human parathyroid hormone (PTH 1-34) — an osteoanabolic agent that intermittently stimulates osteoblast activity to increase bone formation. It is approved for severe osteoporosis on this pharmacological basis.

PLO is a rare but serious osteoporosis subtype occurring in the third trimester of pregnancy or during lactation, typically presenting as vertebral fragility fractures. Because PLO is mechanistically a form of osteoporosis — just occurring in a distinct hormonal/physiological context (pregnancy/lactation-driven bone resorption) rather than a new disease category — extending an osteoanabolic agent already proven in osteoporosis to this population is a much smaller mechanistic leap than most of the model's other top-ranked predictions. This is corroborated by real clinical practice: multiple retrospective cohorts and case series already describe teriparatide being used off-label in PLO patients, with reported improvements in bone mineral density.

**Note on candidate selection:** The nine other TxGNN-ranked indications in this pack (duodenal ulcer, non-syndromic esophageal malformation, duodenal obstruction, duodenogastric reflux, esophageal disease, Worth syndrome, autosomal dominant vitreoretinopathy, succinyl-CoA:3-ketoacid CoA transferase deficiency, amenorrhea) all scored higher or comparably on raw TxGNN score but were assigned **Evidence Level L4/L5 and a Hold recommendation**, with the model's own mechanistic rationale explicitly stating no biological link to PTH/bone metabolism pathways (in one case — Worth syndrome, a high-bone-density disorder — the mechanism is arguably contraindicated). PLO is therefore reported here as the clinically meaningful candidate.

---

## Clinical Trial Evidence

No trials directly studied teriparatide in PLO patients. The following are indirectly related PTH-pathway trials identified by the search:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Studied PTH(1-34)'s effect on osseous regeneration in the oral cavity (periodontal surgery). Not a PLO population; provides only indirect pharmacologic support (Relevance grade C). |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Studied bone loss in renal osteodystrophy (CKD-dialysis patients), not PLO, and did not specifically test teriparatide. Indirect support only for the PTH pathway in bone-loss disease (Relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Cohort | Geburtshilfe und Frauenheilkunde | Largest teriparatide-specific series: 47 women with PLO and postpartum vertebral fractures treated with teriparatide; assessed subsequent fracture risk and BMD change. |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Case series/Cohort | Calcified Tissue International | Multicenter retrospective cohort; 19 PLO patients treated with teriparatide (20 μg/day) plus calcium, compared with conventional management on BMD and trabecular bone score. |
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Cohort/Systematic Review | J Clin Endocrinol Metab | Systematic review and meta-analysis of comparative treatment effectiveness in PLO — optimal management still undefined. |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review | Osteoporosis International | Meta-analysis of 35 studies / 943 PAO patients on presentation, risk factors and treatment response; treatment-response data noted as inconclusive due to limited data. |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Cohort | Calcified Tissue International | Evaluated whether teriparatide can be discontinued without sequential antiresorptive therapy in PLO patients. |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Review focused specifically on teriparatide use strategies in PLO; notes treatment approaches remain poorly defined due to lack of RCTs. |
| [39156353](https://pubmed.ncbi.nlm.nih.gov/39156353/) | 2024 | Case Report | Cureus | Case of a PLO patient treated with teriparatide who later had a second successful pregnancy without recurrence. |
| [36764958](https://pubmed.ncbi.nlm.nih.gov/36764958/) | 2023 | Case Report | Calcified Tissue International | Case report describing bone microarchitecture and strength improvements during combined teriparatide and zoledronic acid treatment in a PLO patient with multiple vertebral fractures. |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | Calcified Tissue International | General review of PLO pathophysiology, presentation and treatment landscape. |
| [37175006](https://pubmed.ncbi.nlm.nih.gov/37175006/) | 2023 | Review | Diagnostics (Basel) | Narrative review on PLO diagnosis and management strategy given absence of standardized guidelines. |

---

## Saudi Arabia Market Information

Teriparatide currently has no marketing authorization on record in this dataset (`market_status: 未上市`, `total_licenses: 0`). No license entries are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Local warnings, contraindications, and drug-interaction data were not available in this evidence pack — TFDA/SFDA label data retrieval is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Teriparatide's use in PLO is mechanistically coherent (same osteoanabolic pathway as its approved osteoporosis indication) and is already supported by multiple retrospective cohorts and case series showing BMD improvement, reaching evidence level L3 / decision stage S2. However, no randomized controlled trials exist — expected for a rare condition — so evidence remains observational rather than confirmatory.

**To proceed, the following is needed:**
- Local (SFDA) package insert / label data — currently a blocking data gap (DG001)
- Formal DrugBank/mechanism-of-action documentation (DG002)
- Confirmation of teriparatide's registration and marketing pathway in Saudi Arabia (currently not marketed)
- A structured clinical protocol or registry-based study design for PLO, given the absence of RCT-level evidence
- Population-specific safety monitoring plan (pregnancy/lactation exposure, fetal/infant safety data)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

