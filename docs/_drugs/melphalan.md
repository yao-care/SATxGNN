---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# MELPHALAN: From Multiple Myeloma to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is a classic alkylating chemotherapy agent, historically used for multiple myeloma and, in high-dose regimens, ovarian cancer.
The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**,
with **8 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Saudi Arabia licensing data (drug not marketed); classically used for multiple myeloma / ovarian cancer |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, melphalan is a bifunctional alkylating agent (nitrogen mustard/phenylalanine-derivative class) that cross-links DNA, causing cytotoxic damage to rapidly dividing cells. Its efficacy in multiple myeloma is well established, and at high doses it has been used with autologous stem cell rescue across multiple solid-tumor indications.

Gonadal germ cell tumors (testicular seminoma/non-seminoma) are highly chemosensitive, rapidly proliferating tumors — the same tumor biology profile that historically responds to alkylating agents. Melphalan already has a documented clinical history in this space: it is a component of high-dose "high-dose chemotherapy + autologous stem cell transplant (ASCT)" salvage regimens for relapsed or poor-prognosis germ cell tumors, alongside agents such as gemcitabine, docetaxel, and carboplatin.

Mechanistically, the TxGNN prediction is plausible because melphalan's cytotoxic activity is not tumor-type-specific — it depends on cellular proliferation rate, which is very high in germ cell tumors — and this is directly corroborated by a Phase 2 trial (NCT00936936) purpose-built for relapsed germ-cell tumors using a melphalan-containing regimen.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | High-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin → ifosfamide, carboplatin, etoposide) for poor-prognosis relapsed germ-cell tumors; directly designed for this indication |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Large-scale study of eight high-dose chemotherapy regimens with autologous transplant for hematologic malignancy and selected solid tumors |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan + melphalan + topotecan followed by autologous stem cell transplant in advanced/recurrent tumors |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with autologous stem cell transplant for high-risk/relapsed pediatric solid and brain tumors |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | High-dose chemotherapy regimens with/without total-body irradiation before ASCT for hematologic and solid tumors |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | Completed | 36 | Nonmyeloablative allogeneic transplant using melphalan/cladribine or total lymphoid irradiation for various hematologic conditions |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis (CNS involvement, not germ cell tumor itself) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Chemotherapy of testicular germinal tumors |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | The Urologic Clinics of North America | Seminoma treatment overview |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Cohort | Voprosy Onkologii | Experience treating testicular seminoma and its metastases with sarcolysin (melphalan) |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Basic/Mechanistic | Acta Unio Internationalis Contra Cancrum | Influence of hormonal and alkylating drugs on pituitary follicle-stimulating function |

---

## Saudi Arabia Market Information

Melphalan is currently **not marketed** in Saudi Arabia — no license records are available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High — dose-limiting toxicity; multiple trials in the evidence base pair melphalan with autologous stem cell rescue specifically to manage this |
| Emetogenicity Classification | Moderate to High (dose- and route-dependent; high-dose IV regimens are highly emetogenic) |
| Monitoring Items | CBC with differential, renal function (dose adjustment required), hepatic function |
| Handling Protection | Must follow standard cytotoxic drug handling and disposal protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One purpose-designed Phase 2 trial (NCT00936936) directly supports melphalan-containing high-dose chemotherapy in poor-prognosis relapsed germ-cell tumors, backed by several supporting Phase 1/2 ASCT trials and a mechanistically coherent rationale — sufficient to proceed but not yet at the strength of a confirmatory registration trial (L2 evidence).

**To proceed, the following is needed:**
- SFDA/TFDA package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action documentation
- A regulatory pathway assessment, since melphalan is not currently marketed in Saudi Arabia
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

