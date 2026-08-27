---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 2
---

# Temozolomide
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

# Temozolomide: From Glioblastoma/Malignant Glioma to Adult Astrocytic Tumour

## One-Sentence Summary

> Temozolomide is an oral alkylating chemotherapy agent whose established, guideline-defining use is newly diagnosed and recurrent glioblastoma/malignant astrocytoma (the "Stupp protocol").
> The TxGNN model predicts it may be effective for **Adult Astrocytic Tumour**,
> with **2 clinical trials** and **20 publications** currently supporting this direction — though, as detailed below, this largely reflects an already-established standard of care rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glioblastoma / malignant (anaplastic) astrocytoma — per literature evidence in this pack (Stupp protocol, PMID 15758009); not documented in Saudi Arabia regulatory records because the drug is currently unmarketed there |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral alkylating agent (a prodrug) that spontaneously converts to its active metabolite MTIC at physiological pH. MTIC methylates DNA at the O6-guanine position, producing lesions that trigger tumour-cell apoptosis. As a small, lipophilic molecule, it readily crosses the blood-brain barrier, which directly explains its mechanistic fit for primary brain tumours such as glioma and astrocytoma.

Importantly, this "predicted" indication is not a true departure from the drug's known use. Adult astrocytic tumour (including glioblastoma) is temozolomide's core, guideline-defined indication — the pivotal EORTC-NCIC trial (Stupp et al., NEJM 2005) established concomitant radiotherapy plus temozolomide, followed by adjuvant temozolomide, as the standard of care for newly diagnosed glioblastoma. Subsequent Phase 3 trials (EF-14, CeTeG/NOA-09, NOA-08) further reinforce this role in different patient subgroups and combination regimens.

The practical implication is that the TxGNN signal here should be read as **confirmation of an already-proven indication**, not as discovery of a new therapeutic avenue. The evidence pack itself flags this: the mechanistic link is described as the drug's "core/standard indication," and the evidence level should be interpreted with that context in mind — high scientific confidence, but low novelty as a repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized comparison of temozolomide alone vs. PCV (procarbazine, lomustine, vincristine) in recurrent WHO Grade III/IV astrocytic tumours — core Phase 3 evidence for this indication |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of cabozantinib (XL184) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; temozolomide used as a combination-partner backbone rather than as the study drug |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark EORTC-NCIC trial establishing concomitant + adjuvant temozolomide with radiotherapy as standard of care for newly diagnosed glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (5-year follow-up) | Lancet Oncol | 5-year follow-up confirms durable survival benefit of radiotherapy + temozolomide over radiotherapy alone |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Adding bevacizumab to standard temozolomide/radiotherapy did not improve overall survival in newly diagnosed glioblastoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09: lomustine-temozolomide combination improved survival vs. temozolomide alone in MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | EF-14: Tumor-Treating Fields plus maintenance temozolomide improved survival vs. temozolomide alone |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08: dose-dense temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG-BN007: dual immune checkpoint blockade (ipilimumab + nivolumab) evaluated against standard therapy in MGMT-unmethylated glioblastoma |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Cohort | J Neurooncol | Exploratory cohort of anaplastic astrocytoma/oligoastrocytoma patients treated with concurrent radiotherapy and temozolomide |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of glioblastoma and other primary adult brain malignancies, including current management standards |
| [39516198](https://pubmed.ncbi.nlm.nih.gov/39516198/) | 2024 | Basic Research (Mechanism) | Nat Commun | Single-cell regulatory profiling method reveals transcriptional/regulatory programs underlying neural cancer plasticity, relevant to glioma biology |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine / DNA-methylating class — per mechanism described in the evidence pack) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (EORTC-NCIC/Stupp, EF-14, CeTeG/NOA-09, NOA-08) provide L1-level evidence that temozolomide is effective in adult astrocytic tumours — but this reflects confirmation of an already-established standard of care rather than a novel repurposing opportunity. The drug is currently unmarketed in Saudi Arabia with no license records, and safety/interaction data are entirely unavailable in this evidence pack.

**To proceed, the following is needed:**
- SFDA-approved package insert (warnings, contraindications) — currently a Blocking data gap preventing S1 safety review
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Drug-drug interaction data (current query returned no results)
- A market-entry assessment clarifying whether local registration for astrocytic tumour is commercially/regulatorily meaningful, given the indication is already globally established rather than newly discovered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

