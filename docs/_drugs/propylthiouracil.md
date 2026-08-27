---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 525
evidence_level: L5
indication_count: 3
---

# Propylthiouracil
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

# Propylthiouracil: From Hyperthyroidism to Neonatal Thyrotoxicosis

## One-Sentence Summary

Propylthiouracil (PTU) is a thiourea-class antithyroid drug long established for treating hyperthyroidism, particularly Graves' disease during the first trimester of pregnancy. The TxGNN model predicts it may be effective for **Neonatal Thyrotoxicosis**, with **1 clinical trial** and **20 publications** currently supporting this direction. This is less a novel mechanistic leap than a formal recognition of an existing off-label clinical practice — treating maternal Graves' disease with PTU to control fetal/neonatal thyroid hormone exposure.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism / Graves' disease (established international use; no formal local approval record — see Market Information below) |
| Predicted New Indication | Neonatal Thyrotoxicosis |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap in this evidence pack). Based on known pharmacology, propylthiouracil is a thiourea-class antithyroid agent that inhibits thyroid peroxidase, blocking thyroid hormone synthesis; it also inhibits peripheral conversion of T4 to T3. Its efficacy in hyperthyroidism, especially Graves' disease, is well established, and it is the guideline-preferred antithyroid drug during the first trimester of pregnancy because methimazole carries a higher teratogenicity risk in early gestation.

The link to neonatal thyrotoxicosis is indirect but clinically grounded: PTU crosses the placenta, so treating a pregnant mother's Graves' disease with PTU reduces fetal and neonatal thyroid hormone synthesis, which can prevent or help manage neonatal thyrotoxicosis caused by transplacental transfer of maternal TSH-receptor-stimulating antibodies. This is an established clinical practice pattern rather than an entirely new mechanistic hypothesis.

Two caveats temper the strength of this prediction. First, PTU carries a hepatotoxicity black-box warning that limits its use in pediatric populations, so direct treatment of the neonate itself typically favors methimazole rather than PTU — the therapeutic pathway here is maternal treatment, not neonatal treatment. Second, no clinical trial has directly tested PTU in neonates for this indication; the single registered trial (below) evaluates treatment of the mother's Graves' disease, not the neonate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03066076](https://clinicaltrials.gov/study/NCT03066076) | Phase 3 | Unknown | 60 | Compares total thyroidectomy vs. thionamide antithyroid drugs (incl. PTU) in adults with moderate-to-severe Graves' ophthalmopathy; indirect evidence — treats the maternal/adult condition rather than testing PTU in neonates directly. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33349844](https://pubmed.ncbi.nlm.nih.gov/33349844/) | 2021 | Review/Guideline | J Clin Endocrinol Metab | Guideline review on testing, monitoring, and treatment of thyroid dysfunction in pregnancy, including antithyroid drug selection. |
| [31345521](https://pubmed.ncbi.nlm.nih.gov/31345521/) | 2019 | Review | Endocrinol Metab Clin North Am | High-risk Graves' disease patients treated with PTU in the first trimester, transitioning to methimazole afterward. |
| [32199749](https://pubmed.ncbi.nlm.nih.gov/32199749/) | 2020 | Review | Best Pract Res Clin Endocrinol Metab | Management of thyrotoxicosis during pregnancy, balancing maternal and fetal antithyroid drug risks. |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Overview of hyperthyroidism in pregnancy and its impact on maternal and fetal/neonatal outcomes. |
| [6387489](https://pubmed.ncbi.nlm.nih.gov/6387489/) | 1984 | Review | N Engl J Med | Classic review of antithyroid drug pharmacology and mechanisms of action, including thyroid peroxidase inhibition. |
| [25747892](https://pubmed.ncbi.nlm.nih.gov/25747892/) | 2015 | Cohort study | Thyroid | Integrated healthcare system cohort on gestational thyrotoxicosis, antithyroid drug use, and neonatal outcomes. |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Cohort/outcome study | Eur J Obstet Gynecol Reprod Biol | 32 pregnancies with hyperthyroidism treated with PTU or carbimazole; reports maternal/perinatal outcomes. |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Cohort study | Clin Endocrinol | 46 pregnancies with Graves' disease treated with PTU or carbimazole; correlates TSH-receptor antibody levels with neonatal thyroid function. |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | Neonatal thyrotoxicosis and maternal infertility in a family with a TRβ gene mutation (M313T). |
| [18558604](https://pubmed.ncbi.nlm.nih.gov/18558604/) | 2008 | Case report | Endocr Pract | Persistent neonatal thyrotoxicosis from a rare activating TSH-receptor mutation. |

## Saudi Arabia Market Information

Propylthiouracil is currently **not marketed** in Saudi Arabia — no product authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. No structured safety data (warnings, contraindications, or drug interactions) is currently available in this evidence pack — note that TFDA/SFDA package insert data is flagged as a **Blocking** data gap (DG001), which prevents a full S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic pathway — maternal PTU treatment reducing transplacental thyroid hormone exposure to the fetus/neonate — reflects an already-established clinical practice pattern, supported by multiple cohort studies and guideline reviews (L3 evidence). However, no trial or study directly tests PTU in neonates, and the drug's own hepatotoxicity warning generally steers direct neonatal treatment toward methimazole instead, so the therapeutic role of PTU here is maternal, not neonatal, treatment.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (blocking gap DG001) before any S1 safety assessment can proceed
- Confirmed mechanism-of-action documentation (gap DG002)
- Clarification of whether "neonatal thyrotoxicosis" in scope means maternal-source treatment or direct neonatal administration, since this materially changes the safety profile
- Note: two other TxGNN-predicted indications for this drug — "resistance to thyroid hormone due to a TRβ mutation" (highest TxGNN score, 99.66%, but scoring/evidence workup still pending) and "hyperthyroxinemia" (L4 evidence, Hold — too etiologically heterogeneous for a single recommendation) — remain in the evaluation pipeline and are not covered by this report's Go/Guardrails decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

