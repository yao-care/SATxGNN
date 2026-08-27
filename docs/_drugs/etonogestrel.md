---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a third-generation progestin used in long-acting reversible contraceptive implants (e.g., Implanon/Nexplanon).
The TxGNN model predicts it may be effective for **Amenorrhea (disease)**,
with **1 clinical trial** and **2 publications** currently identified, though the evidence is largely indirect (menstrual suppression observed as a side effect of contraceptive use, not a dedicated treatment target).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (long-acting implant) — based on known drug class; no Saudi Arabia license text available to confirm exact wording |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank MOA query flagged as a data gap). Based on known pharmacology, etonogestrel suppresses the hypothalamic-pituitary-ovarian axis (inhibiting the LH surge and ovulation) and induces endometrial atrophy — mechanisms already well documented in Implanon/Nexplanon as a common cause of amenorrhea/altered bleeding patterns during contraceptive use.

The connection between the original indication (contraception) and the predicted indication (amenorrhea) is therefore mechanistically plausible but not novel: it reflects a known pharmacological side effect being reframed as a potential therapeutic application (menstrual suppression), rather than a genuinely new biological target. The available clinical trial and literature evidence support this side effect but were not designed to test amenorrhea as a primary treatment endpoint, which limits how directly they support a repurposing claim.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Single-arm study assessing contraceptive efficacy/safety of the etonogestrel implant during extended use (years 4–5). Amenorrhea/bleeding pattern was a secondary safety observation, not the primary endpoint (relevance grade B — indirect). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomized comparison of Implanon vs. Norplant in 200 women; reports bleeding pattern and contraceptive efficacy data relevant to menstrual suppression, no pregnancies over ~340/329 woman-years. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT (protocol) | Trials | COVID-19 pneumonia treatment protocol (BIO101); abstract does not mention etonogestrel or amenorrhea — appears to be a low-relevance/possibly mismatched retrieval result. |

## Saudi Arabia Market Information

Product is not currently marketed in Saudi Arabia (0 authorizations on record).

## Safety Considerations

Please refer to the package insert for safety information. (Local warnings, contraindications, and drug interaction data could not be retrieved — TFDA package insert data is flagged as a **Blocking** gap that prevents initial S1 safety screening.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (missing local package insert / safety data, DG001) prevents initial S1 safety screening, and the amenorrhea evidence is indirect — derived from secondary bleeding-pattern observations in contraception trials rather than dedicated amenorrhea-treatment studies (Evidence Level L3).

**To proceed, the following is needed:**
- Local package insert / safety data (warnings, contraindications) — Blocking gap DG001
- Confirmed mechanism of action data from DrugBank — DG002
- A trial or study designed with amenorrhea/menstrual suppression as a primary endpoint
- Drug-drug interaction (DDI) data (currently not found)

*Note: Four additional lower-ranked predictions (breast fibrocystic disease, blunt duct/apocrine adenosis, benign mammary dysplasia) were also flagged by TxGNN with similarly high scores but no supporting trials or literature (Evidence Level L5, decision stage S0). These are assessed as likely knowledge-graph clustering artifacts around "hormonal drug–benign breast disease" nodes and are not recommended for further evaluation at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

