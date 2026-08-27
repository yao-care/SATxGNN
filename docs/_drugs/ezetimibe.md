---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol-absorption inhibitor whose established use is lowering LDL cholesterol, typically as an add-on to statin therapy in hypercholesterolemia/dyslipidemia. TxGNN predicts strong applicability to **Hyperlipoproteinemia** (a broader hyperlipidemia classification), supported by **50 clinical trials** and **19 publications**, with the underlying NPC1L1-inhibition mechanism already clinically validated rather than newly hypothesized.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the structured regulatory record (no license text on file); per the evidence pack's own mechanistic notes, ezetimibe's established use is LDL-C lowering, combined with a statin |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is not yet available in this evidence pack (data gap DG002, "作用機轉 (MOA)"). However, the TxGNN mechanistic rationale attached to every predicted indication in this pack consistently describes ezetimibe as a selective inhibitor of the intestinal brush-border transporter NPC1L1 (Niemann-Pick C1-Like 1), which blocks absorption of both dietary and biliary cholesterol and thereby lowers LDL-C.

Hyperlipoproteinemia is a broad diagnostic classification that encompasses hypercholesterolemia and mixed dyslipidemia — the population ezetimibe is already used to treat, generally in combination with a statin (reduced cholesterol synthesis + reduced intestinal absorption). This means the prediction is less a novel repurposing hypothesis and more a confirmation/extension of an already-validated pharmacological role, which is consistent with the pack's own assessment ("非新假說").

Mechanistically, this makes the prediction highly plausible: the trial and literature record below directly tests ezetimibe (alone or combined with statins/fenofibrate/other lipid-lowering agents) in hyperlipidemic and familial hypercholesterolemia populations, including a large-scale Japanese post-marketing surveillance study (n=11,332).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg added to atorvastatin/simvastatin in homozygous familial hypercholesterolemia — efficacy and safety |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia — cholesterol-lowering efficacy/safety |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A (post-marketing) | Completed | 11,332 | Japan real-world drug-use surveillance of Zetia (ezetimibe) mono/combination therapy, 12-week |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Phase 3 | Completed | 450 | VICTORION-INITIATE: "inclisiran-first" vs usual care in ASCVD with elevated LDL-C; ezetimibe as background therapy |
| [NCT00701883](https://clinicaltrials.gov/study/NCT00701883) | Phase 2 | Completed | 183 | MBX-8025 (PPAR-δ agonist) ± atorvastatin in obese hyperlipidemic patients |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Phase 1 | Completed | 18 | PK interaction study: Vytorin (ezetimibe+simvastatin) with Niaspan (extended-release niacin) |
| [NCT04272697](https://clinicaltrials.gov/study/NCT04272697) | N/A | Recruiting | 75,000 | European Atherosclerosis Society Familial Hypercholesterolaemia registry/collaboration |
| [NCT05974345](https://clinicaltrials.gov/study/NCT05974345) | N/A | Completed | 204,691 | In-silico secondary-data analysis of inclisiran's impact on MACE in ASCVD |
| [NCT05255094](https://clinicaltrials.gov/study/NCT05255094) | Phase 3 | Completed | 464 | AK102 (PCSK9 inhibitor) efficacy/safety in primary hypercholesterolemia and mixed hyperlipidemia |
| [NCT04656028](https://clinicaltrials.gov/study/NCT04656028) | N/A | Active, not recruiting | 180 | GENMOTIV-FH: genetic testing + motivational counseling on adherence in familial hypercholesterolemia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM trial: obicetrapib + ezetimibe fixed-dose combination for LDL-C reduction, Phase 3 double-blind |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in HeFH patients not at LDL-C goal despite existing lipid-lowering therapy |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Familial hypercholesterolemia overview; ezetimibe among established LDL-C lowering treatments |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH epidemiology, underdiagnosis/undertreatment in India |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | Global burden and management approaches for FH |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | FH pathophysiology and genetics (LDLR/APOB/PCSK9) |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Molecular Sciences | Postprandial hyperlipidemia pathophysiology, diagnosis, treatment |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Review/Guidance | European Heart Journal | EAS consensus on FH underdiagnosis/undertreatment and screening guidance |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Research advances in current hyperlipidemia-targeting drugs |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors, statin-intolerant/FH context |

---

## Taiwan Market Information

Ezetimibe is currently **not marketed in Taiwan** (`market_status = 未上市`), and there are **0 authorization records** on file. No product license table can be produced from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently unavailable — TFDA package insert extraction is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by an L1 evidence level — a large, directly relevant clinical trial base (including a real-world surveillance study of 11,332 patients) and a mechanistically well-established rationale (NPC1L1 inhibition). However, this indication substantially overlaps with ezetimibe's already-established combination use with statins rather than representing a genuinely novel repurposing hypothesis, and the drug is not currently marketed in Taiwan.

*(Note: two other TxGNN-predicted indications for this candidate — familial hypercholesterolemia, also L1/Proceed with Guardrails, and largely the same established-use overlap; and CYP7A1-deficiency hypercholesterolemia, L4/Research Question, mechanism-only evidence — were assessed separately. Cholesterol-ester transfer protein deficiency was scored L5/Hold due to lack of mechanistic overlap and is not recommended for further evaluation.)*

**To proceed, the following is needed:**
- TFDA package insert extraction (warnings, contraindications) — currently Blocking (DG001)
- Formal DrugBank mechanism-of-action record (DG002)
- Confirmation of Taiwan regulatory/licensing pathway, given current "not marketed" status
- Drug-drug interaction database confirmation (currently `not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

