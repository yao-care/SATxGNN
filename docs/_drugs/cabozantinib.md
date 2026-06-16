---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# CABOZANTINIB: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-target tyrosine kinase inhibitor (TKI) approved globally for renal cell carcinoma (RCC), hepatocellular carcinoma, and medullary thyroid cancer, but currently not registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **1 clinical trial** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal cell carcinoma (global approval; not registered in Saudi Arabia) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, cabozantinib is a small-molecule inhibitor that simultaneously targets multiple receptor tyrosine kinases — primarily VEGFR2, MET, and AXL — and its efficacy in renal cell carcinoma has been extensively validated across multiple Phase 3 trials (METEOR, CheckMate 9ER, COSMIC-313), establishing it as a cornerstone treatment for RCC globally.

Liposarcoma is a subtype of soft tissue sarcoma (STS) in which MET overexpression and AXL-driven tumor invasion are recognized oncogenic mechanisms, alongside VEGF-driven tumor angiogenesis. Cabozantinib's simultaneous blockade of MET, VEGFR, and AXL provides a biologically plausible mechanism for activity in liposarcoma: MET inhibition can disrupt tumor growth signals and invasive capacity, VEGFR blockade cuts off tumor blood supply, and AXL inhibition may counter treatment-resistance pathways common in mesenchymal tumors.

While RCC and liposarcoma differ histologically, both share dependence on VEGF-driven angiogenesis and, in relevant subsets, MET pathway activation. An active Phase 2 randomized trial (NCT05836571) is currently exploring cabozantinib in combination with dual immune checkpoint blockade in advanced soft tissue sarcoma — a broader population that includes liposarcoma — lending translational plausibility to this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomized comparison of Cabozantinib + Ipilimumab + Nivolumab vs. Ipilimumab + Nivolumab alone in advanced soft tissue sarcoma; liposarcoma is included as a recognized STS subtype, but subgroup-specific liposarcoma outcomes have not yet been reported |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Neoadjuvant Trial | American Journal of Clinical Oncology | Phase 1 study of concurrent cabozantinib and radiation therapy as neoadjuvant treatment in extremity soft tissue sarcoma; assessed safety profile with particular attention to fistula and perforation risk; cabozantinib demonstrated activity across multiple STS subtypes |

---

## Saudi Arabia Market Information

Cabozantinib is currently not approved or registered in Saudi Arabia (0 authorizations on record). Globally, the drug is commercially available under the brand names **Cabometyx** (for RCC and hepatocellular carcinoma) and **Cometriq** (for medullary thyroid cancer). Any use in Saudi Arabia at present would require import authorization, compassionate use, or expanded access mechanisms.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-kinase inhibitor (VEGFR2/MET/AXL/RET); not conventional cytotoxic |
| Myelosuppression Risk | Low to moderate (thrombocytopenia and neutropenia reported but generally less severe than conventional chemotherapy) |
| Emetogenicity Classification | Low to moderate (oral agent; nausea and vomiting reported in a minority of patients) |
| Monitoring Items | CBC with differential, liver function (ALT/AST/bilirubin), renal function, thyroid function, blood pressure, urine protein, serum electrolytes |
| Handling Protection | Standard oral antineoplastic handling precautions apply; classified as a hazardous drug — use appropriate PPE when handling or dispensing |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.83%), and the mechanistic rationale — MET/VEGFR/AXL multi-target blockade in MET-overexpressing soft tissue sarcoma — is scientifically credible. However, current evidence is limited to one Phase 2 trial in broad soft tissue sarcoma (without liposarcoma-specific outcomes) and a Phase 1 safety study, placing this at L3 evidence. No liposarcoma-specific RCT exists to date.

**To proceed, the following is needed:**

- Confirm the proportion of liposarcoma patients enrolled in NCT05836571 and monitor for subgroup efficacy data when the trial completes (expected May 2026)
- Obtain full MOA data from DrugBank (currently missing from this evidence pack)
- Review the complete package insert for contraindications, drug interactions, and special population warnings before any clinical application
- Assess Saudi Arabia regulatory pathway options (registration, compassionate use, or import authorization), as the drug is currently not marketed locally
- If NCT05836571 soft tissue sarcoma data is supportive, consider proposing a liposarcoma-enriched Phase 1b/2 expansion cohort or an investigator-initiated study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

