---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib is an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases ALK, ROS1, and MET, approved for the treatment of ALK-positive and ROS1-positive advanced non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**,
however this direction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive / ROS1-positive advanced Non-Small Cell Lung Cancer |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the structured data source for this report. Based on published literature referenced within this evidence pack, crizotinib is an ATP-competitive inhibitor of three receptor tyrosine kinases: anaplastic lymphoma kinase (ALK), ROS proto-oncogene 1 receptor tyrosine kinase (ROS1), and MET (c-Met). It was first approved in 2011 for EML4-ALK rearranged advanced NSCLC, and subsequently for ROS1-fused NSCLC, where constitutive kinase activation drives uncontrolled tumor cell proliferation and survival.

Gingival fibromatosis is a rare benign connective tissue disorder characterised by progressive overgrowth of the gingival mucosa. Its known genetic drivers include mutations in *SOS1*, *HRAS*, and other yet-unidentified loci that regulate connective tissue remodelling — none of which intersect with the ALK/ROS1/MET signalling axis that crizotinib targets. Unlike malignant tumours where these kinases are aberrantly activated, gingival fibromatosis does not involve receptor tyrosine kinase-driven oncogenic signalling.

The high TxGNN prediction score (99.81%) therefore cannot be substantiated by any known mechanistic bridge. This signal is most likely attributable to graph topology propagation in the knowledge graph — a known false-positive pattern where nodes that are topologically proximal in the disease network receive high scores independent of true biological plausibility. No clinical or preclinical evidence exists to contradict this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Crizotinib is currently **not registered** in Saudi Arabia. No marketing authorisations have been issued.

---

## Cytotoxicity

Crizotinib is an antineoplastic targeted therapy approved for malignant indications. The following safety profile applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/ROS1/MET receptor tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; hepatotoxicity, cardiotoxicity, and interstitial lung disease are the primary toxicity concerns; haematological adverse events are less pronounced than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, total bilirubin), ECG monitoring for QT prolongation and bradycardia, chest imaging for interstitial lung disease / organising pneumonia, complete blood count |
| Handling Protection | Standard precautions for oral targeted therapy apply; refer to institutional cytotoxic drug handling guidelines |

> **Key toxicities identified in the evidence pack:** hepatotoxicity including fatal fulminant liver failure (PMID [26898609](https://pubmed.ncbi.nlm.nih.gov/26898609/)); simultaneous cardiac toxicities including bradycardia, QT prolongation, and ventricular fibrillation (PMID [29717400](https://pubmed.ncbi.nlm.nih.gov/29717400/)); drug-induced organising pneumonia / lung injury (PMID [37062732](https://pubmed.ncbi.nlm.nih.gov/37062732/)).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, gingival fibromatosis is driven by SOS1/HRAS mutations with no established connection to the ALK/ROS1/MET signalling axis. The complete absence of clinical trial or published literature support places this at L5 (model prediction only), and the mechanistic rationale is assessed as negative. This prediction is classified as a likely graph-diffusion false positive.

**To proceed, the following is needed:**
- Histological or molecular evidence of ALK, ROS1, or MET expression/activation in gingival fibromatosis tissue
- Preclinical studies (in vitro or in vivo) establishing a biological link between crizotinib's kinase targets and gingival fibromatosis pathogenesis
- Retrieval of full MOA and safety data via DrugBank API (Data Gap DG002)
- Retrieval of prescribing information and package insert warnings (Data Gap DG001)
- Saudi Arabia regulatory filing if clinical development is pursued (drug currently not registered in the market)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

