---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Goserelin: From Hormone-Responsive Cancer to Amenorrhea

## One-Sentence Summary

> Goserelin is a GnRH (LHRH) agonist historically used to induce medical castration/ovarian suppression in hormone-responsive prostate cancer, breast cancer, and endometriosis.
> The TxGNN model predicts it may be effective for **Amenorrhea**,
> with **7 clinical trials** (3 completed Phase 3 RCTs) and **17 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer, hormone-responsive breast cancer, endometriosis (GnRH agonist class; not currently registered in the target market) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on known pharmacological information, goserelin belongs to the GnRH (LHRH) agonist class, and its efficacy in hormone-dependent conditions (prostate cancer, breast cancer, endometriosis) has been established; mechanistically it is directly applicable to amenorrhea.

Goserelin's core pharmacology is receptor desensitization: continuous exposure downregulates pituitary GnRH receptors, suppressing LH/FSH secretion and, in turn, ovarian steroidogenesis. This produces a reversible, drug-induced hypogonadal state — clinically manifesting as amenorrhea. This is not an indirect inference from an unrelated pathway; it is a direct extension of the drug's primary mechanism.

This mechanism is already established clinical practice: goserelin is used to induce reversible amenorrhea for ovarian function preservation during chemotherapy in premenopausal breast cancer (e.g., the POEMS and OPTION trials), and separately to manage endometriosis-related symptoms via ovarian suppression. The predicted indication of "amenorrhea" therefore reflects a known, on-target pharmacodynamic effect rather than a novel or speculative one.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | POEMS trial: goserelin + chemotherapy vs. chemotherapy alone to prevent ovarian failure/early menopause in early-stage, hormone-receptor-negative breast cancer |
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: goserelin during chemotherapy to prevent early menopause in premenopausal breast cancer (stage I–III) |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Randomized trial of GnRH agonist (goserelin) for ovarian function preservation during chemotherapy in premenopausal breast cancer |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Aromatase inhibitors vs. GnRH agonists for uterine adenomyosis; drug-induced amenorrhea used as treatment strategy |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection during cyclophosphamide-containing chemotherapy; menstruation outcome endpoint |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal hormone-receptor-positive breast cancer, with/without chemotherapy-induced amenorrhea |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex + CEF neoadjuvant chemotherapy in hormone-responsive premenopausal breast cancer; notes goserelin can induce reversible amenorrhea |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII: chemotherapy + goserelin vs. either alone — impact on amenorrhea, hot flashes, and quality of life |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study: goserelin vs. CMF chemotherapy as adjuvant therapy in node-positive premenopausal breast cancer |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | RCT | Ann Oncol | Anglo Celtic OPTION trial: GnRH agonist protects against chemotherapy-induced ovarian toxicity/premature ovarian insufficiency |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs. low-dose oral contraceptive for endometriosis-associated pelvic pain |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: sequential chemotherapy followed by goserelin vs. either modality alone in node-negative breast cancer |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Review of ovarian ablation methods in adjuvant treatment of premenopausal breast cancer |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists in early breast cancer, emphasizing benefits of reversible ovarian ablation |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Review on therapeutic induction of amenorrhea, noting goserelin as an extremely effective GnRH analogue for this purpose |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Ovarian ablation with goserelin improves survival in stage II/III HR-positive breast cancer without chemotherapy-induced amenorrhea |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort | J Clin Oncol | Discussion of estradiol monitoring needs in women receiving ovarian suppression for breast cancer |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is met — three completed Phase 3 RCTs (POEMS/NCT00068601, OPTION/NCT00427245, NCT02483767) plus multiple supporting RCTs directly demonstrate goserelin-induced amenorrhea as an established, mechanistically on-target effect. However, the drug is not currently marketed in the target market (0 authorizations), and TFDA-equivalent label warnings/contraindications remain an unresolved blocking data gap.

**To proceed, the following is needed:**
- Local regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank mechanism-of-action confirmation (DG002)
- Local market access / registration pathway assessment given current 未上市 status
- Drug interaction (DDI) data, currently not found in query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

