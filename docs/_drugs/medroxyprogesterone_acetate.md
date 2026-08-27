---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Established Hormonal Therapy to Amenorrhea

## One-Sentence Summary

> Medroxyprogesterone acetate (MPA) is a synthetic progestogen long used as an injectable/oral contraceptive and for hormone-related menstrual disorders, though its own approved-indication text is not captured in this evidence pack and the drug is **not currently marketed in Taiwan**. The TxGNN model's top prediction is **Amenorrhea**, supported by **10 clinical trials** and **20 publications** — but the underlying rationale itself notes this is a textbook, already-established clinical use of MPA rather than a genuinely novel hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty; drug not marketed in Taiwan, so no label text is available) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.9994% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available for this drug (Data Gap DG002). Based on the information present in the evidence pack, MPA is a potent progesterone-receptor agonist. Clinically, oral MPA (Provera®) is already used in the "progesterone withdrawal test" to induce withdrawal bleeding in patients with secondary amenorrhea caused by hormonal imbalance, while depot MPA (DMPA), the long-acting injectable contraceptive, produces amenorrhea as an expected pharmacological effect through ovulation suppression and endometrial atrophy.

Because MPA's contraceptive and menstrual-regulation uses already overlap heavily with amenorrhea management, the mechanistic link between the drug and this predicted indication is direct and pharmacologically well characterized — it is not a speculative cross-disease hypothesis.

Importantly, the rationale attached to this candidate explicitly flags that this represents an **established clinical practice, not a new hypothesis**. This should temper how the finding is used: it is best read as evidence consolidation supporting a known use case (useful for a dossier or label-expansion argument) rather than a discovery of previously unrecognized therapeutic activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT evaluating post-endometrial-ablation MPA on endometrial amenorrhea rates; direct relevance (Grade A) but terminated early, small sample |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Timing of postpartum DMPA administration and effect on breastfeeding, contraceptive continuation, and postpartum depression; amenorrhea is a known DMPA side effect rather than the primary endpoint |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1886 | Large RCT of bazedoxifene/conjugated estrogens on endometrial hyperplasia and osteoporosis prevention; indirect supporting evidence on endometrial/hormonal effects |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Examines whether progesterone-induced endometrial withdrawal bleeding is needed before ovulation induction in women with oligo-/amenorrhea |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | Recruiting | 120 | Relugolix vs placebo for heavy menstrual bleeding with uterine fibroids; comparator mechanism study, not an MPA intervention |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Tualang honey vs HRT safety profile in postmenopausal women; low direct relevance |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | Completed | 108 | HRT effect on disease activity, menopausal symptoms and bone mineral density in peri/postmenopausal women with SLE |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Vascular and inflammatory markers in young women with functional hypothalamic amenorrhea vs. regularly cycling women |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | N/A | Not yet recruiting | 276 | Traditional Chinese herbal formula for premature ovarian insufficiency; not an MPA intervention trial |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | Withdrawn | 0 | Estradiol and fear extinction for calorie-dense foods in anorexia nervosa; not related to MPA or amenorrhea treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | Comparative trial (n=100) | Contraception | Randomized comparison showing DMPA-induced amenorrhea can be reversed by switching to Cyclofem (82% resumed bleeding vs. 10% on continued DMPA) |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT (WHICH trial) | PLoS ONE | Compares DMPA-IM vs. NET-EN effects on estradiol levels and menstrual/psychological/behavioral measures relevant to HIV risk |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Review of combination injectable contraceptives, including bleeding-pattern/amenorrhea outcomes |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Earlier Cochrane review on combination injectable contraceptives |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counseling and side-effect management for DMPA users, including amenorrhea management strategies |
| [7139435](https://pubmed.ncbi.nlm.nih.gov/7139435/) | 1982 | Review | Canadian Medical Association Journal | "Should depot medroxyprogesterone acetate be considered for additional uses?" — directly addresses MPA repurposing |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intelligence & Clinical Pharmacy | Review of drug-induced infertility via hypothalamic-pituitary-gonadal axis effects |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Review | Int J Fertil Menopausal Stud | Overview of long-acting contraceptive options, including DMPA amenorrhea rates |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception review, including postpartum amenorrhea considerations |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review (IARC Monograph) | IARC Monographs | General pharmacological monograph on medroxyprogesterone acetate |

---

## Saudi Arabia / Taiwan Market Information

Currently no marketing authorization for MPA in Taiwan — market status is **未上市 (not marketed)** with **0 licenses** on file. No product-level dosage form or approved-indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug interaction data are currently available in this evidence pack (query status: not found), and TFDA package insert retrieval is flagged as a **Blocking** data gap (DG001) since the drug is not marketed in Taiwan.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between MPA and amenorrhea is strong and evidence level is L1, but this reflects consolidation of an already-established clinical use rather than a novel repurposing signal, and the drug currently has no marketing authorization in Taiwan — safety review cannot proceed to S1 until the TFDA package insert gap is closed.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (Blocking gap, DG001)
- Confirmed original approved indication(s) for MPA, since `original_indications` is currently empty
- DrugBank-sourced mechanism of action (High-priority gap, DG002)
- Clarification of regulatory pathway given zero existing Taiwan licenses (new drug application vs. label expansion)
- Assessment of whether the amenorrhea indication should be reframed as evidence-synthesis/dossier support rather than a true repurposing candidate, given its established off-label/on-label use elsewhere
- Lower-ranked candidates (breast fibrocystic disease, benign mammary dysplasia, endometriosis-related sites) remain at L3–L5 evidence with Hold/Research Question status and are not ready for further action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

