---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Temsirolimus is an mTOR-inhibitor ("rapalog") globally approved for renal cell carcinoma, but it is currently **not marketed in Taiwan**.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **5 clinical trials** and **1 publication** currently supporting this direction — though most of the direct trial evidence involves related mTOR inhibitors (sirolimus, ridaforolimus, everolimus) rather than temsirolimus itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (internationally approved indication; no Taiwan license record exists to confirm a local label) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for temsirolimus is not available in the current evidence pack (DrugBank query returned a data gap). Based on information contained in the trial evidence itself, temsirolimus is an inhibitor of mTOR (mammalian target of rapamycin), a kinase that sits within two signaling complexes and drives multiple growth-promoting pathways; blocking it can suppress tumor growth (as described directly in the NCT02821507 trial summary).

Aberrant mTOR pathway activation has been implicated across several soft-tissue sarcoma subtypes, including liposarcoma, which is the rationale multiple sponsors have used to test mTOR inhibitors (sirolimus, ridaforolimus/AP23573, everolimus, and temsirolimus itself) in this population. This provides a plausible mechanistic bridge from temsirolimus's proven oncology use to a sarcoma-family indication.

However, it is important to note that only two of the five supporting trials (NCT01614795 and NCT00949325) use temsirolimus specifically — the other three use pharmacologically related but distinct mTOR inhibitors. The prediction is therefore best read as "class-level" mechanistic support rather than drug-specific confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; tests mTOR inhibition to prevent tumor growth |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (AP23573), an mTOR inhibitor, in patients with advanced sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + **temsirolimus** in pediatric recurrent/refractory solid tumors (sarcoma); temsirolimus dosed to block enzymes needed for cell growth |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (DDL) and leiomyosarcoma (LMS) |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | **Torisel (temsirolimus)** + liposomal doxorubicin in advanced soft tissue and bone sarcomas; dose-finding plus efficacy signal |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Reviews targeted treatment strategies across six molecularly-defined sarcoma subgroups, providing the classification framework underlying mTOR-inhibitor use in soft-tissue sarcomas |

## Taiwan Market Information

Temsirolimus is currently not marketed in Taiwan; no TFDA license records are available (0 authorizations on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (TFDA package insert / warnings and contraindications, DG001) prevents an initial safety screen (S1), and temsirolimus has no Taiwan marketing authorization. Supporting trial evidence for liposarcoma is largely class-level (sirolimus, ridaforolimus, everolimus) rather than temsirolimus-specific, and no completed randomized Phase 2/3 trial directly confirms this indication.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolve DG001
- DrugBank mechanism-of-action detail — resolve DG002
- Drug-drug interaction (DDI) database results (current query returned not_found)
- Trial/registry evidence specific to temsirolimus (rather than related mTOR inhibitors) in liposarcoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

