---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 8
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Regorafenib: From Colorectal Cancer/GIST to Liposarcoma

## One-Sentence Summary

Regorafenib is a globally-approved oral multi-kinase inhibitor whose established indications (based on general pharmacological knowledge, not present in this Evidence Pack) include metastatic colorectal cancer, GIST, and hepatocellular carcinoma. The TxGNN model predicts it may be effective for **Liposarcoma**, but the **2 clinical trials** and **9 publications** currently available actually report **negative results for this specific subtype**, which weakens rather than supports the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in Evidence Pack ([Data Gap]); based on general pharmacological knowledge, regorafenib (Stivarga) is globally approved for metastatic colorectal cancer, GIST, and hepatocellular carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack ([Data Gap], DG002). Based on general pharmacological knowledge, regorafenib is an oral multi-kinase inhibitor targeting VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, and RAF, with proven anti-angiogenic efficacy in colorectal cancer and GIST.

Soft tissue sarcomas (STS) as a class have shown some sensitivity to anti-angiogenic multi-kinase inhibitors, which is the mechanistic basis for the TxGNN prediction extending regorafenib into sarcoma indications. However, liposarcoma (adipocytic sarcoma) is biologically distinct from other STS subtypes — it is typically driven by MDM2/CDK4 amplification rather than being a strongly angiogenesis-dependent tumor, which weakens the mechanistic rationale relative to other sarcoma subtypes.

Critically, this mechanistic weakness is borne out in the actual evidence: the REGOSARC trial (NCT01900743) explicitly reported efficacy in leiomyosarcoma, synovial sarcoma, and other non-adipocytic sarcomas, **but not in liposarcoma** (PMID 29902612). Separately, the SARC024 liposarcoma-specific cohort (PMID 32701199) concluded that results "do not support the routine use of regorafenib in this patient population." Despite a high TxGNN similarity score, the direct clinical evidence for this specific indication is negative, and this contradiction should be weighted more heavily than the model score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol testing regorafenib across multiple sarcoma subtypes (including dedifferentiated liposarcoma); results must be interpreted by subtype, not as a pooled outcome. |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC — randomized, double-blind, placebo-controlled trial with a dedicated liposarcoma cohort (Cohort A); the adipocytic sarcoma cohort did not show the benefit seen in other STS cohorts. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncol | REGOSARC primary results: regorafenib improved PFS in advanced STS after anthracycline failure. |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT (liposarcoma-specific) | The Oncologist | SARC024 liposarcoma cohort: results do not support routine use of regorafenib in this population. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT / post-crossover analysis | Eur J Cancer | Confirms REGOSARC efficacy in non-adipocytic STS but explicitly **not** in liposarcoma. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT secondary analysis | Cancer | Q-TWiST analysis of REGOSARC (NCT01900743) showing quality-adjusted survival benefit in doxorubicin-pretreated advanced non-adipocytic sarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol | BMC Cancer | REGOSARC study protocol describing rationale and design for the phase 2 trial. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's growing role across sarcoma subtypes, including liposarcoma. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review (type unconfirmed) | Crit Rev Oncol Hematol | Reviews maintenance therapy strategies in advanced STS following first-line treatment. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug: anlotinib) | Anti-cancer Drugs | Indirect reference — evaluates anlotinib, not regorafenib, in WDLS/DDLS; mentions regorafenib as a comparator TKI class. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report (different drug: pazopanib) | Rare Tumors | Indirect/low-relevance — pazopanib activity in Ewing sarcoma, a different subtype and different drug. |

---

## Saudi Arabia Market Information

Regorafenib is currently **not marketed** in Saudi Arabia (market status: 未上市, 0 authorizations on file). No product license records are available in this Evidence Pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multi-kinase inhibitor), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low to moderate — dominant toxicities for this drug class are hand-foot skin reaction, hypertension, diarrhea, fatigue, and hepatotoxicity rather than bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (regorafenib carries a hepatotoxicity warning in other markets), blood pressure, CBC, urinalysis (proteinuria), skin examination for hand-foot skin reaction |
| Handling Protection | As an oral antineoplastic agent, institutional hazardous-drug handling precautions (tablet splitting/crushing avoidance, PPE for handling) should apply per local cytotoxic drug handling policy |

*No drug-specific toxicity data was available in this Evidence Pack; the above is based on general knowledge of the regorafenib drug class and should be confirmed against the package insert once available.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for liposarcoma is high (99.76%), the direct clinical evidence contradicts the prediction — both the REGOSARC (NCT01900743) and SARC024 (NCT02048371) liposarcoma-specific cohorts failed to demonstrate meaningful benefit. Additionally, S1 safety review is blocked by a missing package insert (DG001), and MOA data is incomplete (DG002).

**To proceed, the following is needed:**
- SFDA package insert (warnings/contraindications) — currently blocking, required for S1 safety review (DG001)
- Complete DrugBank MOA data (DG002)
- Full-text verification of REGOSARC and SARC024 liposarcoma cohort results to confirm the magnitude/direction of the negative finding
- Consider evaluating an alternative predicted indication from the same Evidence Pack instead: **clear cell renal carcinoma** (rank 3, evidence level L2, decision stage S2, "Proceed with Guardrails") has a positive single-arm Phase 2 trial (PMID 22959186) and stronger mechanistic alignment with regorafenib's known anti-angiogenic profile.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

