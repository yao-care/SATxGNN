---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase (PEG-asparaginase) is an enzyme therapy already established worldwide as a core component of combination chemotherapy for acute lymphoblastic leukemia (ALL). The TxGNN model's top-ranked prediction — **Precursor Lymphoblastic Lymphoma/Leukemia (ALL/LBL)** — is functionally the same disease group as its existing indication, so this result functions as a positive-control validation of the model rather than a genuinely new repurposing signal, and it is backed by **50 clinical trials** and **20 publications**, including several completed Phase 3 RCTs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (globally established use — no formal `original_indications` record in this evidence pack; supported by literature, e.g. PMID 30823860: "FDA approved for the first-line treatment of adult acute lymphoblastic leukemia") |
| Predicted New Indication | Precursor Lymphoblastic Lymphoma/Leukemia (ALL/LBL) |
| TxGNN Prediction Score | 99.96% (rank 1082) |
| Evidence Level | L1 |
| Market Status (this dataset) | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record (e.g. a DrugBank MOA field) is not available for pegaspargase — this is flagged in the evidence pack as data gap DG002 (High severity). However, the pack's clinical rationale supplies substantial mechanistic detail: PEG-asparaginase depletes circulating asparagine. Lymphoblasts characteristic of ALL/lymphoblastic lymphoma lack asparagine synthetase and cannot synthesize their own asparagine, making them highly sensitive to this depletion — a well-established, textbook mechanism rather than a speculative one.

Important caveat for interpretation: the predicted indication "precursor lymphoblastic lymphoma/leukemia" is not a novel disease target — it is essentially pegaspargase's own existing standard-of-care indication (ALL/LBL). The evidence pack's own rationale text explicitly notes this is "existing standard-of-care basis, not a genuine prediction." Practically, this rank-1 result should be treated as confirmation that TxGNN correctly recovers known drug-disease relationships, rather than as a candidate warranting new repurposing investment. If the goal is to identify genuinely novel indications, lower-ranked signals in this evidence pack (e.g. rank 7 "lymphoid neoplasm," rank 8 "Hodgkin's lymphoma" — where the underlying trial/literature evidence actually points to NK/T-cell lymphoma rather than classical Hodgkin lymphoma — and rank 10 CML blast phase) merit separate, more cautious evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03020030](https://clinicaltrials.gov/study/NCT03020030) | Phase 3 | Active, not recruiting | 560 | Standard multi-agent induction/consolidation chemotherapy backbone for newly diagnosed pediatric/adolescent ALL |
| [NCT04954326](https://clinicaltrials.gov/study/NCT04954326) | Phase 2 | Completed | 89 | RCT comparing pharmacokinetics of liquid vs. lyophilized pegaspargase formulations in newly diagnosed pediatric ALL |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2044 | Large French protocol optimizing L-asparaginase brand/dose/schedule in pediatric ALL |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | Methotrexate + vincristine + pegylated L-asparaginase + dexamethasone (MOAD) salvage regimen for relapsed/refractory ALL |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Completed | 649 | Predictive model for PEG-asparaginase hypersensitivity/inactivation to optimize ALL treatment outcomes |
| [NCT00003437](https://clinicaltrials.gov/study/NCT00003437) | Phase 3 | Unknown | 1800 | MRC UK trial comparing steroid/chemotherapy regimens (asparaginase-containing) in childhood ALL |
| [NCT00882206](https://clinicaltrials.gov/study/NCT00882206) | Phase 2 | Terminated | 15 | Decitabine + vorinostat added to a PEG-asparaginase-containing regimen for relapsed/refractory ALL/LL |
| [NCT00096135](https://clinicaltrials.gov/study/NCT00096135) | N/A | Completed | 168 | Chemotherapy + radiotherapy (asparaginase-containing regimen) for late isolated extramedullary ALL relapse |
| [NCT05873322](https://clinicaltrials.gov/study/NCT05873322) | N/A | Recruiting | 100 | Observational study of steroid + PEG-asparaginase-related glucose intolerance/diabetes in ALL and lymphoma |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5000 | Large international AIEOP-BFM ALL 2017 protocol using asparaginase-based, risk-stratified chemotherapy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232: dexamethasone + high-dose methotrexate improve outcomes in high-risk B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434: nelarabine tested in newly diagnosed T-cell ALL, Phase 3 |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231: bortezomib in newly diagnosed T-ALL/T-LL, Phase 3 |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001: efficacy/toxicity of pegaspargase vs. calaspargase pegol in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913: pegaspargase-modified risk-oriented program for adult ALL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Cohort | Leukemia | Venetoclax + hyper-CVAD/nelarabine/pegylated asparaginase in T-ALL/LBL, long-term follow-up |
| [38613330](https://pubmed.ncbi.nlm.nih.gov/38613330/) | 2025 | Cohort | J Oncol Pharm Pract | Retrospective review of pegaspargase toxicities and dosing pattern changes in ALL/lymphoma |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Cohort (Phase 2) | Int J Hematol | Phase 2 multicenter study of pegaspargase in Japanese patients with previously untreated ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert panel consensus on recognition/management of asparaginase-related adverse events in adults |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Classic review of PEG-asparaginase pharmacology, efficacy, and cytotoxicity |

## Market Information

No market authorizations are on record for pegaspargase in this dataset (0 licenses; market status: Not Marketed). No product-level license or approved-indication text is available to tabulate.

## Cytotoxicity

Pegaspargase is a cytotoxic antineoplastic agent (an asparagine-depleting enzyme used as chemotherapy for lymphoid malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme/biologic class (PEGylated L-asparaginase), non-alkylating asparagine-depletion mechanism |
| Myelosuppression Risk | Low relative to classic cytotoxic chemotherapy — asparaginase's mechanism largely spares bone marrow; the evidence pack's literature instead emphasizes hepatotoxicity, pancreatitis, hypertriglyceridemia, hyperglycemia, and hypersensitivity/anaphylaxis as the dominant toxicities (PMID 40109190 expert consensus) |
| Emetogenicity Classification | Not specified in evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests, lipase/amylase (pancreatitis), fasting glucose, coagulation profile/fibrinogen, triglycerides, plus routine CBC |
| Handling Protection | Standard cytotoxic drug handling precautions apply, pending confirmation against local (TFDA) handling regulations |

## Safety Considerations

Formal safety labeling (key warnings, contraindications, drug interactions) is not yet available in this evidence pack — this is flagged as a blocking data gap (DG001) pending retrieval of the TFDA/local package insert. Please refer to the package insert for safety information once available.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by L1-level evidence (multiple completed Phase 3 RCTs plus 50 trials and 20 publications), but it substantially overlaps with pegaspargase's own established indication rather than representing a novel repurposing candidate. Combined with the complete absence of local safety labeling and market-authorization data, this candidate should proceed only under guardrails focused on data completion rather than novel-indication development.

**To proceed, the following is needed:**
- TFDA/local package insert — warnings and contraindications (blocking gap, DG001)
- Formal DrugBank mechanism-of-action record (high-priority gap, DG002)
- Clarification of local market-authorization status (currently 0 licenses / not marketed) and whether an import or special-access pathway is intended
- Reframing of this candidate as a model-validation result; if the objective is genuine repurposing, prioritize review of the lower-confidence, more novel signals in this evidence pack (e.g., the "Hodgkin's lymphoma" label whose underlying trials/literature actually describe NK/T-cell lymphoma, and CML blast phase)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

