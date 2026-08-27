---
layout: default
title: Secnidazole
parent: 僅模型預測 (L5)
nav_order: 567
evidence_level: L5
indication_count: 7
---

# Secnidazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Secnidazole: From Unmarketed Antimicrobial to Vaginal Discharge (Bacterial Vaginosis)

## One-Sentence Summary

Secnidazole is a 5-nitroimidazole antimicrobial with no marketing authorization in Taiwan and no locally recorded original indication. Among TxGNN's seven predicted indications, the strongest evidence-backed candidate is **Vaginal Discharge (Bacterial Vaginosis)**, supported by **5 clinical trials** (including 2 completed Phase 3 RCTs) and **16 publications** — a finding consistent with secnidazole's existing FDA-approved use (Solosec®) for bacterial vaginosis and trichomoniasis in other markets.

*Note: TxGNN's raw highest-scoring prediction is "postmenopausal atrophic vaginitis" (99.70%), but this candidate has zero supporting trials or literature (L5/Hold) and the evidence pack itself flags it as likely reflecting "vaginal-related" semantic proximity in the knowledge graph rather than a real pharmacological link. This report focuses on the indication with actual clinical support.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — secnidazole holds no marketing license in Taiwan (0 licenses on record) |
| Predicted New Indication | Vaginal Discharge (Bacterial Vaginosis) |
| TxGNN Prediction Score | 99.41% (rank 8872) |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for secnidazole is not available (DrugBank MOA field is a data gap). Based on known pharmacology, secnidazole is a second-generation 5-nitroimidazole antimicrobial, mechanistically related to metronidazole and tinidazole: the drug is reduced intracellularly under anaerobic conditions in bacteria and protozoa, generating cytotoxic intermediates that damage microbial DNA.

Bacterial vaginosis (BV) is the single most common cause of abnormal vaginal discharge, and *Trichomonas vaginalis* infection is a related anaerobic-protozoal cause of the same symptom complex. Because secnidazole's antimicrobial mechanism directly targets the anaerobic bacteria and protozoa responsible for these conditions, the TxGNN prediction of "vaginal discharge" is mechanistically coherent rather than a graph-embedding artifact — unlike several of the other predicted indications in this pack (see note below).

This is further reinforced by real-world regulatory precedent: a single-dose oral granule formulation of secnidazole (Solosec®, 2g) is already FDA-approved in the United States specifically for bacterial vaginosis and trichomoniasis, meaning the "repurposing" signal here largely reflects an indication secnidazole is already validated for elsewhere, but which has not yet been registered or evaluated for the Taiwan market.

**Note on other TxGNN predictions in this pack:** Four of the seven predicted indications (postmenopausal atrophic vaginitis, ulceration of vulva, vulvar neoplasm, leukoplakia of vagina) have no supporting trials or literature (L5, decision stage S0, recommendation Hold) and are plausibly non-infectious or proliferative conditions unrelated to secnidazole's antimicrobial mechanism. Vulvovaginal candidiasis (L4, Research Question) is supported only indirectly — the sole related trial actually tests fluconazole (an antifungal) with secnidazole as a co-treatment for concurrent BV, not as direct antifungal evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Phase 4 | Completed | 40 | Post-marketing safety study of single 2g oral dose Solosec (secnidazole) in adolescent girls with bacterial vaginosis |
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Phase 3 | Completed | 147 | Randomized, placebo-controlled, delayed-treatment, double-blind study of single-dose secnidazole 2g for trichomoniasis/BV-related discharge |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Phase 3 | Completed | 118 | Fluconazole + secnidazole combination for symptomatic vaginal discharge (BV and Candida co-infection) |
| [NCT02147899](https://clinicaltrials.gov/study/NCT02147899) | Phase 2 | Completed | 215 | Randomized, double-blind, placebo-controlled study of SYM-1219 (secnidazole) single dose for bacterial vaginosis |
| [NCT05033743](https://clinicaltrials.gov/study/NCT05033743) | Phase 2/3 | Completed | 24 | Pilot study of weekly secnidazole granules (18 weeks) as suppressive therapy to prevent recurrent BV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | RCT | American Journal of Obstetrics and Gynecology | Phase 3 double-blind placebo-controlled trial of single-dose oral secnidazole 2g granules for BV |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | RCT | Infectious Diseases in Obstetrics and Gynecology | Multicenter double-dummy Phase 3 study: secnidazole non-inferior to metronidazole for BV |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | RCT | Indian Journal of Pharmacology | Comparative single-dose trial of metronidazole, tinidazole, secnidazole, and ornidazole in BV |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Systematic Review / Network Meta-analysis | Frontiers in Cellular and Infection Microbiology | Network meta-analysis comparing efficacy/safety of BV drug therapies |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Systematic Review / Meta-analysis | European Journal of Obstetrics, Gynecology, and Reproductive Biology | Efficacy and safety of single-dose oral secnidazole 2g for BV |
| [9617020](https://pubmed.ncbi.nlm.nih.gov/9617020/) | 1998 | Cohort/Comparative Trial | Ginecología y Obstetricia de México | Oral itraconazole + secnidazole vs. vaginal ovules for symptomatic vaginitis |
| [30424704](https://pubmed.ncbi.nlm.nih.gov/30424704/) | 2019 | Review | Postgraduate Medicine | Clinical primer on BV diagnosis and treatment approaches |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Phase 3 Open-Label Study | Journal of Women's Health | Safety of single-dose oral granule secnidazole 2g in women and adolescents with BV |
| [31513780](https://pubmed.ncbi.nlm.nih.gov/31513780/) | 2020 | Review | American Journal of Obstetrics and Gynecology | Comprehensive diagnostic/management approach to noncandidal vaginitis |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In Vitro (Preclinical) | Microbiology Spectrum | In vitro antitrichomonal activity of 5-nitroimidazole drugs including secnidazole |

*Additional support: [PMID 33768237](https://pubmed.ncbi.nlm.nih.gov/33768237/) (Clinical Infectious Diseases, 2021) is a Phase 3 RCT specifically confirming secnidazole efficacy for trichomoniasis — the closely related indication "Trichomonal Vulvovaginitis" (rank 5) also reaches L1/Proceed with Guardrails on this evidence pack.*

---

## Taiwan Market Information

Secnidazole currently holds **no marketing authorization in Taiwan** (0 licenses on record; market status: 未上市/Not Marketed). No product name, dosage form, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently unavailable — TFDA labeling data is an unresolved blocking gap, see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vaginal discharge (bacterial vaginosis) and the closely related trichomonal vulvovaginitis are both supported by L1 evidence — multiple completed Phase 2/3/4 RCTs and an existing FDA-approved product (Solosec®) for these exact uses — making this a credible, low-novelty-risk repurposing candidate. However, secnidazole is not currently licensed in Taiwan, and safety labeling data needed for a formal S1 safety review is missing.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001 — blocking gap; requires PDF retrieval and parsing from TFDA)
- Complete mechanism-of-action documentation from DrugBank (DG002 — high severity)
- A Taiwan marketing authorization or import registration pathway assessment, since the drug is currently unlicensed
- The four low-evidence predictions (postmenopausal atrophic vaginitis, ulceration of vulva, vulvar neoplasm, leukoplakia of vagina) should remain at **Hold** pending any clinical or mechanistic evidence — current data suggests these may be knowledge-graph noise rather than true signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

