---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Endogenous Hormone to Amenorrhea

## One-Sentence Summary

Progesterone is the body's own progestogen hormone, and the evidence pack does not contain structured data on a specific approved original indication (DrugBank `original_indications` is empty and MOA is flagged as a data gap). The TxGNN model predicts it may be effective for **Amenorrhea**, and this prediction is supported by **50 clinical trials** and **18 publications**, most of which reflect progesterone/progestins' long-established role as the standard diagnostic and therapeutic agent for secondary (anovulatory) amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — `original_indications` is empty and no Saudi license text is available) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002: MOA is flagged as a High-severity data gap). Based on general pharmacological knowledge, progesterone is the endogenous steroid hormone of the hypothalamic-pituitary-ovarian axis, and its clinical uses (luteal support, hormone replacement, menstrual cycle regulation) sit squarely within the same physiological system that amenorrhea disorders affect.

The repurposing rationale extracted from the evidence pack notes that progesterone/progestins are already the standard diagnostic and therapeutic tool for secondary amenorrhea — particularly amenorrhea caused by chronic anovulation. The "progesterone challenge test," in which administration of progesterone and observation of subsequent withdrawal bleeding is used both diagnostically (to distinguish anovulatory causes from hypoestrogenic or outflow-tract causes) and therapeutically (to induce a menstrual cycle), is routine gynecologic practice.

Mechanistically, this is a direct rather than speculative link: progesterone withdrawal is the physiological trigger for endometrial shedding. The evidence pack's own annotation cautions that this looks like a "new indication" mainly because the DrugBank `original_indications` field is empty — i.e., this is better characterized as confirmation of an existing standard-of-care use than a genuinely novel therapeutic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-ablation medroxyprogesterone acetate on endometrial amenorrhea rates; progestin analog rather than progesterone itself, and terminated before completion. |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Tested whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction with clomiphene in women with oligo-/amenorrhea. |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A (multicenter RCT) | Unknown | 330 | Chinese multicenter RCT comparing Progesterone Capsules, a TCM formula, and their combination for menstrual disorders. |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1845 | Large RCT of combined estradiol + progesterone for vasomotor symptoms in postmenopausal women with an intact uterus — uses actual progesterone, not an analog. |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Phase 3 | Unknown | 90 | Multicentric RCT of subcutaneous progesterone (25mg, luteal-phase) for endometrial polyp regression in premenopausal women. |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | RCT on timing of postpartum depot medroxyprogesterone acetate (DMPA) and its effect on breastfeeding/contraceptive continuation. |
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Comparative trial of gonadotropin therapy specifically in subjects with Amenorrhea I or anovulatory cycles — amenorrhea-specific population, though the tested drug is a gonadotropin, not progesterone. |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | Tested goserelin (ovarian suppression) during chemotherapy to prevent ovarian failure/amenorrhea in early breast cancer — relevant to the broader amenorrhea-prevention context. |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | Romosozumab plus physiologic estrogen/cyclic progesterone replacement for bone density in functional hypothalamic amenorrhea. |
| [NCT02858336](https://clinicaltrials.gov/study/NCT02858336) | N/A | Completed | 38 | NIH natural-history study characterizing functional hypothalamic amenorrhea and effects of diet/exercise on menstrual cycles. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Reviews diagnostic and therapeutic use of oral micronized progesterone, including its role via hypothalamic kisspeptin/neurokinin B/dynorphin neurons in LH/FSH regulation. |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Reviews etiology and management of amenorrhea in adolescents/young adults, centered on hypothalamic-pituitary-ovarian axis dysfunction. |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Classic primary-care review of the diagnostic evaluation of amenorrhea, including the progesterone challenge test. |
| [40474175](https://pubmed.ncbi.nlm.nih.gov/40474175/) | 2025 | Retrospective cohort | BMC Surgery | High-dose estrogen/progesterone sequential therapy combined with hysteroscopic adhesiolysis for infertility/amenorrhea from severe intrauterine adhesions. |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Updated meta-analysis of risk factors and prognostic significance of chemotherapy-induced amenorrhea in premenopausal breast cancer. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | Endocrine background of hormonal endometriosis treatment, discussing progesterone-resistance as a core pathogenic mechanism. |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Reviews etiology, symptoms and treatment options for premature ovarian insufficiency, a major cause of amenorrhea. |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Reviews intrauterine adhesions (Asherman's syndrome), a structural cause of amenorrhea. |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of postmenopausal vaginal bleeding; frames menopause as clinically defined by 12 months of amenorrhea. |
| [36653588](https://pubmed.ncbi.nlm.nih.gov/36653588/) | 2023 | Review | Reproductive Sciences | Reviews methods for repairing/regenerating injured endometrium, relevant to amenorrhea from intrauterine adhesions and thin endometrium. |

---

## Saudi Arabia Market Information

Progesterone is currently **not marketed** in Saudi Arabia (0 approved products / authorizations on record). No SFDA license or approved-indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack; the DDI query also returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between progesterone and amenorrhea is strong and well-established (the progesterone challenge test is routine clinical practice), and the evidence level is L2 per the scoring in this evidence pack. However, most identified trials involve progestin analogs (e.g., medroxyprogesterone acetate) rather than progesterone itself, the highest-quality trial (NCT02449161) was terminated, and the drug is currently unmarketed in Saudi Arabia with no safety labeling data on file — so guardrails are needed before advancing.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) to close the Blocking-severity S1 safety data gap (DG001)
- DrugBank/product-label mechanism of action detail to close the High-severity gap (DG002)
- Confirmation of whether the intended indication is genuinely "new" versus already-recognized off-label/standard practice, given the empty `original_indications` field
- A regulatory pathway assessment for Saudi Arabia market entry, since the drug currently has zero local authorizations
- Prioritization of trials/publications using progesterone itself (not progestin analogs) specifically in amenorrhea populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

