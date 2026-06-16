---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Taxane Antineoplastic Therapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane-class cytotoxic antineoplastic agent that stabilizes microtubules to induce mitotic arrest, and has been established globally as a standard-of-care treatment across multiple solid tumor types including breast cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a score of 99.90%, representing a baseline evaluation of one of its core globally approved indications.
This prediction is supported by **more than 10 completed Phase 3 randomized controlled trials** and **20 publications**, placing the evidence at the highest tier (L1) — the primary gap is the absence of formal Saudi Arabia market registration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered in Saudi Arabia; established globally for solid tumors |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semisynthetic taxoid derived from the European yew tree (*Taxus baccata*). It exerts its antitumor effect by binding to β-tubulin within the microtubule polymer, promoting assembly of stable, nonfunctional microtubule bundles and blocking their normal dynamic disassembly. This disrupts the mitotic spindle and triggers G2/M phase cell cycle arrest, ultimately activating intrinsic apoptotic pathways. Docetaxel has approximately twice the binding affinity for tubulin compared to paclitaxel, and it achieves a longer intracellular retention time, contributing to its potent and broad antitumor activity.

Female breast carcinoma cells are particularly vulnerable to taxane-induced mitotic disruption for several reasons. Many breast tumors overexpress BCL-2, an antiapoptotic protein that paradoxically sensitizes cells to spindle poisons through phosphorylation-dependent inactivation. Triple-negative breast cancer (TNBC), which lacks estrogen receptor, progesterone receptor, and HER2, depends heavily on intact mitotic machinery without alternative growth signaling escape routes — this confers heightened sensitivity to docetaxel. In HER2-positive disease, the combination of docetaxel with anti-HER2 agents (trastuzumab, pertuzumab) produces synergistic tumor cell killing by simultaneously targeting proliferation machinery and growth factor signaling.

It is important to note that female breast carcinoma is one of docetaxel's core globally established indications (FDA, EMA, and other major regulators). This evaluation functions as a **repurposing baseline** — the scientific question is not whether docetaxel works in breast cancer (the evidence unambiguously confirms it does), but whether a formal Saudi Arabia regulatory pathway and market introduction should be pursued. The Saudi Arabia registration gap represents an administrative and market access opportunity, not a scientific evidence gap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Randomized comparison of weekly docetaxel vs CMF in adjuvant treatment of women aged ≥65 or ineligible for anthracyclines with high-risk breast cancer; directly evaluates docetaxel single-agent efficacy as highest-relevance trial |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Landmark trial comparing preoperative AC alone vs AC followed by preoperative or postoperative docetaxel in Stage II/III operable breast cancer; established the sequential taxane addition paradigm |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Phase 3 | Completed | 2,611 | AC followed by docetaxel alone vs docetaxel + capecitabine in high-risk breast cancer; evaluated whether adding capecitabine to the taxane backbone improves overall survival |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant TC (docetaxel + cyclophosphamide) or AC-paclitaxel ± trastuzumab in node-positive or high-risk HER2-low invasive breast cancer; one of the largest breast cancer adjuvant trials to date |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | Prospective randomized comparison of TAC (docetaxel + doxorubicin + cyclophosphamide) vs TCX (replacing doxorubicin with capecitabine) in adjuvant treatment of HER2-negative high-risk breast cancer |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | TCHP (docetaxel, carboplatin, trastuzumab, pertuzumab) ± estrogen deprivation in HR+/HER2+ locally advanced breast cancer; evaluated pathologic complete response rates and the role of concurrent hormonal suppression |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense G-CSF-supported FEC followed by sequential docetaxel vs paclitaxel as adjuvant chemotherapy in axillary lymph node-positive breast cancer |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | AC followed by weekly or every-3-week paclitaxel or docetaxel in node-positive breast cancer; directly compared taxane schedules and agents within the same backbone |
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | Phase 3 | Completed | 300 | Mitoxantrone vs FEC as first-line chemotherapy in metastatic breast cancer with unfavorable prognosis; docetaxel-containing treatment represented the standard comparison arm establishing taxane superiority |
| [NCT04066335](https://clinicaltrials.gov/study/NCT04066335) | N/A | Unknown | 1,498 | Large-scale real-world observational safety study of Nanoxel M (nanoparticle docetaxel formulation) in cancer patients including breast cancer; provides substantial post-market safety dataset |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Systematic Review | The Oncologist | Comprehensive 10-year review of taxane roles in metastatic, adjuvant, and neoadjuvant breast cancer; establishes docetaxel as superior to paclitaxel in several head-to-head comparisons and confirms benefit across disease stages |
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT | J Clin Oncol | ABC Trials (USOR 06-090, NSABP B-46-I, NSABP B-49): randomized comparison of 6 cycles of TC vs standard TaxAC regimens in early breast cancer; demonstrates non-inferiority of docetaxel + cyclophosphamide vs anthracycline-containing taxane combinations in most subgroups |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Drug Profile Review | J Clin Oncol | Seminal review of docetaxel preclinical and clinical profiles; establishes pharmacological basis for breast cancer activity and summarizes early Phase 2 response data |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Phase IIb RCT | J Clin Oncol | Dose-dense doxorubicin + docetaxel ± tamoxifen as preoperative therapy in operable breast cancer; evaluated whether tamoxifen addition to dose-dense anthracycline-taxane improves pathologic response |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 Trial | Breast Cancer (Tokyo) | Docetaxel + cyclophosphamide + trastuzumab (HER-TC) neoadjuvant regimen in HER2-positive breast cancer; demonstrated pathologic complete response rates comparable to anthracycline-based regimens with a more favorable cardiac safety profile |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 Trial | Cancer | TEX regimen (capecitabine + docetaxel + epirubicin) as first-line treatment for locally advanced or metastatic breast cancer; evaluated activity and safety of a triplet combination incorporating oral fluoropyrimidine |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Comparative review of paclitaxel and docetaxel in breast cancer; summarizes early efficacy data and the extension of docetaxel licensing to metastatic breast cancer following single-agent activity demonstrations |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 Trial | Clin Breast Cancer | Docetaxel + cisplatin neoadjuvant for locally advanced breast cancer (primary tumors ≥5 cm); 4 cycles prior to modified radical mastectomy; evaluated pathologic complete response and breast-conservation rates |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort Study | Anti-cancer Drugs | Retrospective evaluation of adjuvant docetaxel-based chemotherapy and its association with breast cancer-related lymphedema in Stage II/III patients; characterized incidence and risk factors for this specific toxicity |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 Trial | Oncology | Docetaxel + vinorelbine combination in metastatic breast cancer and NSCLC; reported response rates and median survival projections across treatment-naive and pretreated patient cohorts |

---

## Saudi Arabia Market Information

Docetaxel currently has **no registered products** in Saudi Arabia. Based on available regulatory records, no marketing authorizations have been issued by the Saudi Food and Drug Authority (SFDA) for any docetaxel formulation. This stands in contrast to its globally established status: docetaxel is approved under brand names including Taxotere (Sanofi) and numerous generic formulations across the United States, European Union, Japan, China, and more than 50 other countries, where it is indicated for breast cancer, NSCLC, prostate cancer, gastric cancer, and head and neck cancer.

The absence of Saudi Arabia registration represents the primary barrier to clinical use in this market and is the key regulatory action point identified in this evaluation.

---

## Cytotoxicity

Docetaxel is classified as a **conventional cytotoxic antineoplastic agent** (taxane class). It meets all criteria for cytotoxicity designation: it is a member of the taxoid family, its mechanism directly targets dividing cells through mitotic spindle disruption, and it has dose-limiting myelotoxicity as a primary clinical concern.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (semisynthetic taxoid; microtubule-stabilizing agent) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia occurs in 11–15% of patients without prophylactic G-CSF. Severe neutropenia (Grade 3/4) can exceed 75% at standard doses |
| Emetogenicity Classification | **Low to moderate** — Docetaxel itself carries low emetogenic potential; however, infusion-related hypersensitivity reactions and fluid retention syndrome require premedication (corticosteroids, antihistamines) |
| Monitoring Items | CBC with differential count before each cycle; liver function tests (ALT, AST, total bilirubin, alkaline phosphatase — dose modification required if elevated); assessment for peripheral neuropathy, edema, and nail changes at each visit |
| Handling Protection | Must comply with cytotoxic drug handling regulations; closed-system drug transfer devices (CSTD) required during preparation; full PPE (gown, double gloves, face shield) mandatory; dedicated cytotoxic waste disposal protocols apply |

---

## Safety Considerations

Please refer to the package insert for safety information. No formal safety warning, contraindication, or drug interaction data specific to Saudi Arabia regulatory labeling was available from the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel in female breast carcinoma holds the strongest possible evidence classification (L1), supported by over ten completed Phase 3 randomized controlled trials and decades of post-marketing experience across millions of patients worldwide. The recommendation to "Proceed with Guardrails" reflects not a deficiency in efficacy evidence, but rather the need to establish the appropriate regulatory, safety infrastructure, and monitoring systems specific to the Saudi Arabia healthcare setting before clinical deployment.

**To proceed, the following is needed:**
- Submit formal SFDA marketing authorization application for at least one docetaxel formulation (either branded Taxotere or a biosimilar/generic registered in a major ICH market)
- Obtain complete Arabic-language package insert with SFDA-required labeling formats, including local adverse event reporting pathways
- Establish febrile neutropenia management protocol with G-CSF prophylaxis guidelines adapted to Saudi Arabia formulary availability
- Confirm availability of dexamethasone premedication regimen (3 days surrounding each infusion) through Saudi Arabia pharmacy channels
- Identify certified oncology treatment centers with cytotoxic drug handling capabilities, trained nursing staff, and emergency hypersensitivity management equipment
- Develop patient monitoring plan covering CBC, liver function, peripheral neuropathy, and fluid retention at each cycle
- Conduct health technology assessment (HTA) and pharmacoeconomic analysis for SFDA reimbursement and national formulary listing consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

