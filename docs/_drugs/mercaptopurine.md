---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a long-established thiopurine antimetabolite that forms the backbone of maintenance therapy for acute lymphoblastic leukemia (ALL) and acute promyelocytic leukemia (APL). The TxGNN model predicts it may also be effective for broader **Myeloid Leukemia**, with **29 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia / Acute Promyelocytic Leukemia (established maintenance therapy backbone; no formal Saudi Arabia registration record on file) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mercaptopurine is a thiopurine purine analog that inhibits de novo purine synthesis and DNA replication, exerting cytotoxic effects on highly proliferative cells such as leukemic blasts.

Mercaptopurine has long been a standard component of ALL and APL maintenance regimens, typically combined with methotrexate (MTX). Because myeloid leukemia (AML/APL) blasts share the same high-proliferation, purine-synthesis-dependent biology as lymphoblastic leukemia cells, the mechanistic rationale for extending 6-MP use into myeloid leukemia maintenance is directly supported rather than purely speculative — multiple Phase 3/4 trials (e.g., AIDA, PETHEMA LPA2005) already incorporate 6-MP + MTX maintenance specifically for APL, a myeloid leukemia subtype.

The TxGNN prediction therefore aligns with an evidence base that already exists in the literature, rather than proposing a mechanistically novel repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: RCT of maintenance therapy (6-MP-containing regimen) vs. observation in low/intermediate-risk APL — directly relevant, Grade A |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | GOELAMS SA-2002: post-remission maintenance in elderly AML, regimen includes 6-MP; primary variable was androgen addition, Grade B |
| [NCT02845232](https://clinicaltrials.gov/study/NCT02845232) | N/A | Completed | 214 | Economic analysis of transfusion costs in elderly AML; confirms 6-MP as standard-era background therapy, Grade C |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea+VPA vs. 6-MP+VPA combination in AML/high-risk MDS patients unfit for standard therapy |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | ApoAML trial: venetoclax + 6-mercaptopurine oral combination in relapsed/refractory AML |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin/chemo ± arsenic trioxide as consolidation, followed by maintenance with intermittent tretinoin + mercaptopurine + methotrexate in untreated APL |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1068 | AIDA protocol guideline for newly diagnosed APL; maintenance includes ATRA + methotrexate + 6-mercaptopurine |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000: risk-adapted APL therapy; 2-year maintenance with 6-mercaptopurine, methotrexate, and ATRA |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005: risk-adapted APL treatment; maintenance therapy with ATRA + low-dose methotrexate + mercaptopurine |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | AIDA-based APL treatment with ATRA maintenance and ATRA + methotrexate + mercaptopurine salvage therapy for relapse |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Oral maintenance chemotherapy with 6-MP + methotrexate in transplant-ineligible AML patients, assessing leukemia-free and overall survival |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Cohort | Cancer Investigation | High-dose 6-MP followed by intermediate-dose cytarabine during first remission of pediatric AML |
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | pending | Int J Hematol | JALSG-AML92: induction regimen with daunorubicin, cytarabine, and 6-mercaptopurine in adult AML |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | pending | Cancer Chemother Pharmacol | Nationwide randomized comparison of daunorubicin vs. aclarubicin combined with cytarabine, 6-MP, and prednisolone in untreated AML |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | pending | J Clin Oncol | Japan Leukemia Study Group randomized trial of induction/consolidation regimens including 6-MP in adult AML |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | pending | Int J Hematol | Intensive individualized induction with behenoyl cytarabine, daunorubicin, and 6-mercaptopurine in adult AML |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | pending | Chinese Medical Journal | Combination chemotherapy with cytarabine, daunorubicin, and 6-mercaptopurine for AML remission induction |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case series | Minnesota Medicine | Early treatment of AML with 6-mercaptopurine and cyclophosphamide |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | pending | Rinsho Ketsueki (Jpn J Clin Hematol) | Review of current therapy for AML and APL |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | pending | Blood | Juvenile chronic myeloid leukemia treated with sequential subcutaneous cytarabine and oral mercaptopurine |

---

## Saudi Arabia Market Information

Mercaptopurine currently has **no marketing authorization on record in Saudi Arabia** (`market_status: 未上市`, 0 licenses). No product-level dosage form or approved indication text is available for this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine analog / thiopurine antimetabolite) |
| Myelosuppression Risk | High — dose-limiting toxicity; extensively documented in the literature as being driven by TPMT/NUDT15 metabolizer status, with genotype-guided dosing now standard practice |
| Emetogenicity Classification | Low (oral thiopurine, generally classified as minimal-to-low emetogenic risk) |
| Monitoring Items | CBC with differential, liver function tests, renal function; TPMT and NUDT15 genotyping/phenotyping recommended prior to and during dosing |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations (PPE, closed-system preparation where applicable) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The L1 evidence level is supported by a Phase 3 RCT (NCT00492856) directly evaluating maintenance therapy in a myeloid leukemia subtype (APL), plus decades of established real-world use of 6-MP + MTX maintenance across multiple AIDA/PETHEMA Phase 3/4 protocols. However, the drug has no current market authorization in Saudi Arabia and no local safety documentation is on file.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening can proceed)
- Detailed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Local drug-drug interaction (DDI) data confirmation
- Regulatory pathway analysis for first-time market entry, given the drug's "not marketed" status in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

