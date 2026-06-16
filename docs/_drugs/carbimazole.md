---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 3
---

# Carbimazole
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

# Carbimazole: From Hyperthyroidism to Neonatal Thyrotoxicosis

## One-Sentence Summary

Carbimazole is an antithyroid prodrug (converted to methimazole in vivo) used internationally to suppress thyroid hormone synthesis in hyperthyroidism, including Graves' disease.
The TxGNN model generated three thyroid-related predictions; **Neonatal Thyrotoxicosis** (Rank #2, 99.41%) is the most clinically actionable, supported by **no registered clinical trials** but **20 publications**.
Notably, the top-ranked prediction (RTH-β, 99.71%) carries a fundamental mechanistic contradiction and is recommended to Hold — TxGNN score alone does not determine actionability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism (Graves' disease, toxic multinodular goiter) |
| Predicted New Indication | Neonatal Thyrotoxicosis (TxGNN Rank #2; highest actionable prediction) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L3 (Observational studies and case series) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## TxGNN Prediction Summary (All Three Indications)

Three predictions were generated. Their clinical relevance and recommendations differ significantly:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Issue |
|------|---------------------|-------------|----------------|----------------|-----------|
| #1 | Resistance to Thyroid Hormone (RTH-β) | 99.71% | L5 | **Hold** | Mechanistic contradiction — reducing T4 worsens RTH-β |
| #2 | Neonatal Thyrotoxicosis | 99.41% | L3 | **Proceed with Guardrails** | Strong mechanistic alignment; supported by case series and cohort data |
| #3 | Hyperthyroxinemia | 99.21% | L4 | **Research Question** | Heterogeneous condition; efficacy depends entirely on underlying etiology |

> ⚠️ **Critical Note:** RTH-β patients have elevated T4 as a *compensatory* response — their peripheral tissues resist thyroid hormone, so the pituitary drives TSH high to maintain normal metabolism. Treating this with carbimazole would remove the compensation and precipitate clinical hypothyroidism. This indication is contraindicated despite having the highest TxGNN score.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data package. Based on established pharmacology, carbimazole is a prodrug rapidly converted to methimazole after oral absorption. Methimazole inhibits **thyroid peroxidase (TPO)**, the enzyme responsible for organification and coupling of iodine residues during thyroid hormone synthesis. This directly and specifically reduces T3 and T4 production in thyroid follicular cells. The drug does not affect pre-formed circulating hormone or peripheral conversion of T4 to T3.

In neonatal thyrotoxicosis, the pathophysiology is well-defined: maternal Graves' disease generates TSH receptor–stimulating antibodies (TRAb/TSI) that cross the placenta from approximately week 20 of gestation, stimulating the neonatal thyroid gland to overproduce T3 and T4. Carbimazole's TPO-inhibiting mechanism directly suppresses this overproduction, making it mechanistically precise for this condition.

The distance between carbimazole's established use (adult hyperthyroidism) and the predicted indication (neonatal thyrotoxicosis) is extremely short — both involve the same biochemical defect (excess thyroid hormone synthesis via TPO activity). Neonatal thyrotoxicosis is essentially a transient, antibody-mediated hyperthyroidism occurring in newborns. International clinical guidelines (European Thyroid Association, Endocrine Society) already recognize antithyroid drugs as the first-line treatment for neonatal thyrotoxicosis, which makes the TxGNN prediction biologically and clinically sound.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications.

---

## Literature Evidence

*(10 most relevant publications selected from 20 identified for Neonatal Thyrotoxicosis; prioritized by direct clinical relevance and carbimazole use)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Case Report | Endocrinology, Diabetes & Metabolism Case Reports | 3-week-old infant with thyrotoxicosis-induced severe hypercalcaemia; thyrotoxicosis treated with carbimazole; calcium normalized as thyroid function improved |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Case Series | Indian Journal of Pediatrics | Fetal hyperthyroidism in two siblings treated with intrauterine and postnatal carbimazole; prior pregnancies resulted in stillbirths without treatment — highlights life-saving role |
| [29494342](https://pubmed.ncbi.nlm.nih.gov/29494342/) | 2018 | Case Report | Journal of Pediatric Endocrinology & Metabolism | Severe neonatal hyperthyroidism from transplacental TRAbs born to a mother with autoimmune hypothyroidism (not Graves'); expands the clinical scenario beyond classical Graves' disease |
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Review | Indian Journal of Endocrinology and Metabolism | Comprehensive review of fetal and neonatal thyrotoxicosis: epidemiology (1/70 Graves' pregnancies), pathophysiology, antithyroid drug management, and mortality |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | The Lancet Diabetes & Endocrinology | Evidence-based guidelines on hyperthyroidism in pregnancy; covers neonatal risk stratification and antithyroid drug selection including carbimazole |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Case Series | Clinical Endocrinology | Congenital thyrotoxicosis in premature infants; reported mortality up to 25%; maternal TBII index predictive of severity; antithyroid drug response documented |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Cohort | Clinical Endocrinology | 46 Graves' disease pregnancies; carbimazole and PTU treatment correlated with neonatal thyroid function and TSH receptor antibody levels; foundational dataset |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Cohort | European Journal of Obstetrics, Gynecology and Reproductive Biology | 32 pregnancies with hyperthyroidism managed with carbimazole/PTU; maternal and neonatal outcomes documented over 7 years |
| [2315685](https://pubmed.ncbi.nlm.nih.gov/2315685/) | 1990 | Case Report | Scottish Medical Journal | Neonatal thyrotoxicosis with TSH receptor antibodies from post-thyroidectomy mother; neonatal thyrotoxicosis resolved with carbimazole therapy |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Case Report | Drug Safety – Case Reports | Neonate on carbimazole + propranolol for thyrotoxicosis developed severe hypotension after amlodipine — critical drug-drug interaction warning specific to this population |

---

## Saudi Arabia Market Information

Carbimazole currently has **no approved authorizations in Saudi Arabia**. No licensing data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Neonatal-specific safety signals identified from the literature:**

- **Drug interaction in neonates:** PMID 27747714 documents severe hypotension when oral carbimazole is combined with amlodipine in neonates also receiving propranolol. Calcium channel blockers should be used with extreme caution in carbimazole-treated neonates.
- **Teratogenic risk (prenatal exposure only):** PMID 12124735 describes a possible association between maternal carbimazole use in the first trimester and choanal atresia in the neonate. This risk applies to *maternal* use during organogenesis and does not apply to postnatal treatment of the neonate directly.

---

## Conclusion and Next Steps

**Decision by Indication:**

| Indication | Decision | One-Line Rationale |
|------------|----------|--------------------|
| RTH-β (Rank #1) | **Hold** | Carbimazole would remove the compensatory T4 elevation that sustains normal metabolism; risk of iatrogenic hypothyroidism |
| Neonatal Thyrotoxicosis (Rank #2) | **Proceed with Guardrails** | Mechanism is precise, clinical evidence is consistent, and international guidelines support antithyroid drugs as first-line |
| Hyperthyroxinemia (Rank #3) | **Research Question** | Must be sub-stratified by etiology before any use recommendation; not evaluable as a single indication |

---

**Primary Decision: Proceed with Guardrails (Neonatal Thyrotoxicosis)**

**Rationale:**
Multiple cohort studies and case series consistently document carbimazole's effectiveness in neonatal thyrotoxicosis, the mechanism (transplacental TRAb → excess TPO activity) is well-understood and directly targeted, and international endocrinology societies recognize antithyroid drugs as standard of care. The L3 evidence base is sufficient to develop institutional protocols, though the absence of randomized trials warrants careful monitoring.

**To proceed, the following is needed:**

- Weight-based dosing protocol for neonatal carbimazole (standard adult doses are not applicable)
- Defined monitoring schedule: thyroid function tests (T3, T4, TSH) every 3–7 days initially, CBC and liver enzymes to monitor for agranulocytosis and hepatotoxicity
- Drug interaction review before co-prescribing any antihypertensive agents (see amlodipine warning above)
- Clear endpoint for treatment discontinuation (TRAb clearance typically occurs within 3–12 weeks as maternal antibodies wane)
- Registration or compassionate use pathway in Saudi Arabia (currently not marketed)
- Multidisciplinary sign-off from neonatology and pediatric endocrinology before clinical deployment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

