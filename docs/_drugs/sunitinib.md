---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sunitinib is a multi-targeted tyrosine kinase inhibitor whose established global indications include advanced/metastatic renal cell carcinoma (RCC) (cited as public background knowledge within this evidence pack; Saudi Arabia regulatory registration data itself is a data gap).
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **3 clinical trials** and **9 publications** currently supporting this direction — though evidence comes mainly from non-GIST soft-tissue-sarcoma basket trials rather than a liposarcoma-specific pivotal study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (cited in evidence pack as globally-approved public background knowledge; local TFDA/SFDA indication text not available — Data Gap DG001) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sunitinib is not formally documented in this evidence pack (Data Gap DG002). Based on known information referenced within the pack's own rationale notes, sunitinib is a multi-targeted receptor tyrosine kinase inhibitor acting on VEGFR1-3, PDGFRα/β, KIT, RET, and CSF1R, and its efficacy in VEGF/PDGFR-driven tumours such as renal cell carcinoma has been established.

Liposarcoma is a heterogeneous soft-tissue sarcoma family, and certain subtypes (notably myxoid liposarcoma) show angiogenesis-dependence and PDGFR pathway involvement. This gives a plausible mechanistic bridge from sunitinib's known anti-angiogenic/anti-PDGFR activity to liposarcoma. However, response across liposarcoma subtypes is inconsistent, and unlike dermatofibrosarcoma protuberans (which has a well-defined COL1A1-PDGFB driver), liposarcoma has no single dominant, targetable oncogenic fusion — so the mechanistic case is directionally reasonable but not histology-specific.

Supporting this, the strongest clinical evidence comes from Phase 2 trials of sunitinib conducted in broader non-GIST soft-tissue sarcoma populations (which included liposarcoma patients) rather than a dedicated liposarcoma trial, consistent with the "Research Question" stage assigned to this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label trial of sunitinib malate in unresectable/metastatic soft tissue sarcoma explicitly including leiomyosarcoma, liposarcoma, fibrosarcoma and MFH; directly relevant. |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Continuous-dosing sunitinib in non-GIST sarcomas (metastatic/locally advanced/recurrent), directly covering liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket study of oral **regorafenib** (not sunitinib) across sarcoma subtypes; only the disease population overlaps, drug is different. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase2 | International Journal of Cancer | Phase II study of sunitinib malate in relapsed/refractory STS, focused on leiomyosarcoma, liposarcoma and MFH — direct efficacy/safety evidence. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Cohort | American Journal of Surgical Pathology | Clinicopathologic series of myxoid inflammatory myofibroblastic sarcoma; a distinct sarcoma entity, only tangentially related to liposarcoma. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Reviews genetic/epigenetic/transcriptomic alterations in liposarcoma relevant to target-therapy selection. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Reviews medical treatment of soft tissue sarcomas by histological subtype, including targeted agents. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Reviews emerging (targeted) therapies for adult soft tissue sarcoma. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven STS therapy review; notes trabectedin's high activity specifically in myxoid liposarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial Protocol | BMC Cancer | REGOSARC trial protocol evaluating **regorafenib** (not sunitinib) in advanced STS. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Case Report | Oncotarget | Genomic profiling of extraskeletal myxoid chondrosarcoma; evaluates sunitinib activity in a subset of EMC patients. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case Report | Anticancer Research | Case of long-lasting clinical benefit from sunitinib malate in a heavily pre-treated metastatic liposarcoma patient. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted receptor tyrosine kinase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the liposarcoma indication currently rests on non-GIST sarcoma basket trials and case reports rather than a liposarcoma-specific pivotal study, and response across STS histology subtypes is inconsistent — consistent with the pack's own "Research Question" staging (L2/S2) for this prediction.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently Blocking Data Gap DG001)
- Confirmed mechanism of action data for sunitinib (currently High-severity Data Gap DG002)
- A liposarcoma-subtype-specific prospective trial (particularly myxoid/dedifferentiated liposarcoma)
- Confirmation of Saudi Arabia marketing/regulatory status, since sunitinib currently has 0 local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

