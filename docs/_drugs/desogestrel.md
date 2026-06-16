---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a third-generation progestogen widely used globally as a component in combined oral contraceptives and as a progestogen-only mini-pill (75 mcg, e.g. Cerazette) for contraception, though it holds no current registration in Saudi Arabia.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **2 clinical trials** and **16 publications** currently supporting this direction.
Critically, the mechanistic relationship is paradoxical: desogestrel's HPO axis suppression is a well-documented *cause* of amenorrhea as a side effect — not a treatment for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral contraception (progestogen component; no Saudi Arabia registration on record) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, desogestrel is a third-generation gonane progestogen and a prodrug that requires hepatic metabolism to its active form, etonogestrel. Etonogestrel binds progesterone receptors with high selectivity and low androgenicity, suppressing the hypothalamic-pituitary-ovarian (HPO) axis to inhibit follicular maturation and ovulation. This is the core mechanism behind its contraceptive effect at 75 mcg (progestogen-only pill) and its contribution to combined OC formulations.

The relationship between desogestrel and amenorrhea is directionally paradoxical. Rather than treating amenorrhea, desogestrel commonly induces it: approximately 20–30% of women using the 75 mcg mini-pill experience amenorrhea as a recognised consequence of sustained HPO suppression and endometrial atrophy. The two clinical trials identified in this evidence pack examine desogestrel in the context of athletic reproductive dysfunction and PCOS metabolic outcomes — neither uses "resolution of amenorrhea" as a primary endpoint.

The TxGNN graph model most likely captures a pharmacological network proximity between desogestrel and amenorrhea through shared hypothalamic-hormonal pathway nodes. However, directionality matters: in the known biology, desogestrel drives toward amenorrhea rather than away from it. A clinically meaningful repurposing hypothesis would require identifying a specific amenorrhea subtype — for example, anovulatory hyperandrogenic oligomenorrhea in PCOS — where cycle regulation via HPO modulation could be beneficial, and where desogestrel's antiandrogenic profile (raising SHBG, lowering free testosterone) might restore rather than further suppress menstrual cycling.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Examined body composition and hormonal changes in young female athletes with exercise-induced (hypothalamic) amenorrhea; assessed whether transdermal or oral estrogen improves bone density in estrogen-deficient amenorrheic athletes. Desogestrel was not the primary intervention; amenorrhea was an observed outcome rather than a treatment target. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | Compared effects of oral contraceptives (which may include desogestrel-containing preparations) versus a hormonal vaginal ring on androgen, insulin, lipid, and inflammatory parameters in women with PCOS over 59 weeks. Amenorrhea was not a primary endpoint; small sample and unknown status limit interpretability. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Clinical Trial | Gynecological Endocrinology | Head-to-head comparison of drospirenone-only pill (4 mg, 24+4 cycle) versus desogestrel 0.075 mg in women with cardiovascular risk factors; amenorrhea documented as a frequent bleeding outcome with the desogestrel arm over 9 cycles, illustrating desogestrel as an inducer rather than a resolver of amenorrhea. |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Systematic Review | Cochrane Database Syst Rev | Cochrane review comparing 20 µg versus >20 µg estrogen combined OCs, including desogestrel-containing formulations; lower estrogen dose associated with higher rates of amenorrhea and unscheduled bleeding. |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Systematic Review | Cochrane Database Syst Rev | Earlier edition of same Cochrane review; confirms the dose-dependent relationship between estrogen content in OCs and amenorrhea incidence. |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Trial | J Reprod Med | Evaluated bone mineral density in young women with hypothalamic amenorrhea treated with OCs at varying ethinyl estradiol doses; desogestrel-containing OCs used as a hormone replacement surrogate to address estrogen deficiency in amenorrheic women. |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacology | Acta Obstet Gynecol Scand Suppl | Foundational pharmacodynamic characterisation of desogestrel; evaluated androgenicity versus other progestogens and noted the mechanistic links between progestogen-associated hormonal suppression and amenorrhea/PCO-like features. |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Clinical Trial | Am J Obstet Gynecol | Tolerability profile of the desogestrel/ethinyl estradiol combination OC; documented non-contraceptive benefits (dysmenorrhea reduction, endometriosis improvement) and cycle-control side effects including amenorrhea. |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative Study | Br J Obstet Gynaecol | Compared two OC pills containing 150 µg desogestrel with 20 µg versus 30 µg ethinyl estradiol (Mercilon vs Marvelon); analysed cycle control and amenorrhea incidence differences between the two formulations. |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Cohort | Br Med Bull | Reviewed combined OC acceptability and use patterns based on large cohort data; discussed dose-related health risks, benefits, and menstrual pattern changes including amenorrhea. |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstet Gynecol Surv | Comprehensive review of three new third-generation progestogens (desogestrel, norgestimate, gestodene); covered pharmacokinetics, contraceptive efficacy, and tolerability at lower doses. |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Trial | Georgian Med News | Evaluated central-genesis oligomenorrhea and amenorrhea management in 159 infertile women; compared EEG-guided pathogenetic treatment versus standard hormone therapy, providing context for centrally-mediated amenorrhea treatment approaches. |

---

## Saudi Arabia Market Information

Desogestrel holds no current marketing authorisation in Saudi Arabia. The SFDA database query returned zero registered products, dosage forms, or approved indications. No authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a graph proximity between desogestrel and amenorrhea, but the established clinical biology shows that desogestrel *induces* amenorrhea (via HPO axis suppression) rather than resolving it — a directional mismatch that makes direct repurposing for amenorrhea treatment unsound without a refined subtype-specific hypothesis. Evidence is at L4 (mechanistic/indirect), and no trial has tested desogestrel as a treatment for amenorrhea.

**To proceed, the following is needed:**
- A refined clinical hypothesis specifying the amenorrhea subtype (e.g., anovulatory PCOS-associated oligoamenorrhea where cycle regulation — not suppression — is the goal) to distinguish therapeutic intent from known adverse effects
- Mechanism of action data from DrugBank (currently unavailable in this evidence pack)
- Safety data recovery: package insert warnings, contraindications, and DDI data are all currently marked as data gaps and must be resolved before any clinical evaluation
- Consideration of whether **acne (rank 4, L3, Proceed with Guardrails)** or **lactation disease/breastfeeding contraception (rank 7, L2, Proceed with Guardrails)** may represent better-evidenced and mechanistically cleaner repurposing candidates for priority development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

