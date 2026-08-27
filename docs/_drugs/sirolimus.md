---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

Sirolimus (rapamycin) is an mTOR inhibitor whose established use is prevention of organ rejection after kidney transplantation.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **5 clinical trials** and **11 publications** currently supporting this direction — though only one trial tests sirolimus itself, the rest involve same-class mTOR inhibitors (temsirolimus, everolimus, ridaforolimus).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal transplant rejection prophylaxis (general drug knowledge; not present in evidence pack — `original_indications` and licenses are empty) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sirolimus is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, sirolimus is an mTOR (mechanistic target of rapamycin) inhibitor, originally developed and approved as an immunosuppressant to prevent kidney transplant rejection; its efficacy in that indication is well established.

Dedifferentiated liposarcoma shows documented activation of the Akt-mTOR and MAPK signaling pathways, which is mechanistically the same axis sirolimus targets. This provides a biological rationale for repurposing mTOR inhibitors in this tumor type.

However, of the 5 supporting clinical trials, only one (NCT02821507) directly tests sirolimus; the remaining four use closely related same-class agents (temsirolimus, everolimus/RAD001, ridaforolimus/AP23573). This means the mechanistic link is well supported at the drug-class level, but direct evidence for sirolimus itself in liposarcoma remains limited to a single Phase 2 trial.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma, based on preclinical evidence that mTOR inhibition prevents tumor growth |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (AP23573, mTOR inhibitor) dosed once daily x5 every 2 weeks in advanced sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus (sirolimus ester prodrug) in pediatric recurrent/refractory sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin dose-finding and efficacy study in advanced soft tissue/bone sarcoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clin Cancer Res | Phase 2 trial (SAR-096) of ribociclib + everolimus in dedifferentiated liposarcoma and leiomyosarcoma; synergistic growth inhibition via CDK4/mTOR co-targeting |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Review of novel therapeutics in soft tissue sarcoma, including FDA-approved molecularly targeted agents |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Cohort | Tumour Biol | Akt-mTOR and MAPK pathway activation demonstrated across 99 dedifferentiated liposarcoma specimens, with in vitro mTOR inhibitor antitumor effect |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine + rapamycin combination effective against well-differentiated liposarcoma via autophagy inhibition |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of rationale and trial results for molecular-targeted agents in advanced sarcomas |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | Randomized trial: sirolimus after cyclosporine withdrawal reduces cancer risk in renal transplant recipients |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | Effects of immunosuppressive drugs (including sirolimus) on malignancy development in transplant patients |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical | In Vivo | Rapamycin + chloroquine arrests tumor growth in a dedifferentiated liposarcoma PDOX mouse model |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows potent antitumor activity in bone/soft-tissue sarcoma models |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Review of targeted treatments for rare connective tissue tumors and sarcomas by molecular subgroup |

## Saudi Arabia Market Information

No marketing authorizations are currently registered — sirolimus has a market status of "Not Marketed" and 0 licenses on file in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack; DG001 — TFDA/regulatory package insert warnings — is flagged Blocking severity, meaning safety review cannot formally proceed until this is resolved.)

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale (Akt-mTOR/MAPK pathway activation in liposarcoma) is sound and supported by one direct sirolimus Phase 2 trial plus four same-class mTOR-inhibitor trials, but this falls short of confirmatory evidence for sirolimus specifically — it remains a research hypothesis rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- TFDA/local package insert data on warnings and contraindications (Blocking data gap — required before any safety evaluation)
- Confirmed mechanism of action documentation from DrugBank (High-priority data gap)
- A sirolimus-specific (not same-class) randomized controlled trial in liposarcoma to upgrade evidence from L2 toward L1
- Drug-drug interaction profile, given sirolimus's narrow therapeutic index and known CYP3A4/P-gp interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

