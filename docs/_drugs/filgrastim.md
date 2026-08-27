---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF), conventionally used to stimulate neutrophil production and mobilize hematopoietic stem cells in patients undergoing chemotherapy or stem cell transplantation. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this direction is currently supported by only **14 clinical trials (none directly testing this indication)** and **1 mechanistic review article**. The mechanistic link is explicitly characterized as indirect and non-specific in the underlying evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia management / hematopoietic stem cell mobilization (G-CSF class); no formal Saudi Arabia license record exists |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for filgrastim is not available in this evidence pack (marked as a data gap). Based on known information, filgrastim is a recombinant G-CSF that mobilizes myeloid precursor cells — including the megakaryocyte lineage — from bone marrow into peripheral blood, and its efficacy in supporting neutrophil recovery after chemotherapy and in stem cell mobilization for transplantation is well established.

Primary release disorder of platelets is a defect in platelet granule content release rather than a defect in platelet or megakaryocyte production. The repurposing rationale in this evidence pack states the connection plainly: G-CSF's mobilization of megakaryocytic precursors could theoretically influence platelet generation, but there is no evidence that it corrects the granule-release defect itself. This is an indirect, non-specific mechanistic link rather than a targeted one.

Consistent with this, nearly all supporting clinical trials use filgrastim/G-CSF as a supportive agent for hematopoietic stem cell transplantation (HSCT) or chemotherapy-related cytopenia in hematologic malignancies — not as a treatment directed at platelet granule-release defects. No trial or publication in this evidence pack directly tests filgrastim in patients with this disorder.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for hematologic malignancies; G-CSF used only for stem cell mobilization/transplant support (Grade C — low relevance to target disease) |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous SCT in MCL/DLBCL; G-CSF as mobilization agent, not disease-targeted therapy (Grade C) |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | AHSCT vs. best available therapy for treatment-resistant relapsing multiple sclerosis; G-CSF as transplant-support agent (Grade C) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial of PTCy-based GVHD prophylaxis after mismatched unrelated donor PBSCT; relevance not yet graded |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT using busulfan/fludarabine/TBI for hematologic malignancies; relevance not yet graded |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved HLA-mismatched unrelated donor marrow transplant with PTCy; relevance not yet graded |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation prevention in acute lung injury/respiratory failure; relevance not yet graded |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplant in pediatric sarcomas; relevance not yet graded |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile (NLRP3 inhibitor) for moderate COVID-19 with early cytokine release syndrome; relevance not yet graded |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding of post-transplant cyclophosphamide with sirolimus/MMF for GVHD prophylaxis; relevance not yet graded |

Four additional trials in the evidence pack (NCT00076752, NCT00923364, NCT01503918, NCT00354172) were omitted from this table for length; none carry a relevance grade above "C" or "pending."

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Mechanistic Review | Frontiers in Immunology | G-CSF mobilization in healthy stem cell donors preferentially mobilizes lymphocyte subsets; a mechanistic study of donor mobilization biology, not of platelet release disorders |

## Saudi Arabia Market Information

Filgrastim is not currently marketed in Saudi Arabia — no license records exist in this evidence pack (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-interaction data are available in this evidence pack — DDI query returned no results, and TFDA package insert warnings/contraindications are flagged as data gaps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between G-CSF and primary release disorder of platelets is indirect and non-specific — G-CSF mobilizes megakaryocytic precursors but has no demonstrated effect on the underlying granule-release defect. No clinical trial or publication in this evidence pack directly tests filgrastim for this indication, and the drug is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data from DrugBank (currently a data gap)
- TFDA/SFDA package insert warnings and contraindications (currently a blocking data gap for safety screening)
- Drug interaction (DDI) data
- Disease-specific preclinical or mechanistic studies directly testing G-CSF's effect on platelet granule release, rather than its role as an HSCT-supportive agent
- Confirmation of original approved indication(s) and licensing status, since no local license record currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

