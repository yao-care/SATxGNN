---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix (Firmagon) is a GnRH receptor antagonist, internationally approved for the treatment of advanced hormone-sensitive prostate cancer by rapidly suppressing testosterone levels; it is not currently marketed in Saudi Arabia.
The TxGNN model predicts it may be effective for **Hypertrichosis**, yet **0 clinical trials** and **0 publications** currently support this direction.
Across all 10 top-ranked predictions, evidence remains at L5 (model prediction only), with central precocious puberty (rank 9) representing the sole indication with genuine mechanistic rationale worth further exploration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced hormone-sensitive prostate cancer (internationally approved; not marketed in Saudi Arabia) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Degarelix is a synthetic GnRH (gonadotropin-releasing hormone) receptor antagonist. By competitively blocking GnRH receptors in the anterior pituitary, it rapidly suppresses LH and FSH secretion — which in turn drives testosterone levels to castrate range within days, without the initial testosterone surge ("flare") seen with GnRH agonists. This mechanism is the basis for its established role in prostate cancer management.

The model's prediction of hypertrichosis rests on a partial hormonal logic: androgens (particularly dihydrotestosterone, DHT) are known to stimulate terminal hair follicle growth in androgen-sensitive body regions. In that narrow subset, suppressing testosterone via GnRH blockade could theoretically reduce hair growth. This reasoning is most applicable to androgen-dependent hirsutism in women with hyperandrogenism — a condition that overlaps clinically but is distinct from hypertrichosis as a disease entity.

The fundamental problem is that **hypertrichosis (as classified) is predominantly non-androgen-dependent**: it encompasses congenital genetic forms, drug-induced generalized hypertrichosis, and paraneoplastic types, where the GnRH axis plays no established pathological role. Without knowing the specific subtype, the mechanistic link is speculative and fragile. The complete absence of supporting clinical trials or literature across all 10 predicted indications reinforces that TxGNN has likely captured a weak structural graph association rather than a true pharmacological opportunity in this case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Degarelix is used for advanced prostate cancer (a malignancy), qualifying for this section as a non-cytotoxic antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal therapy — GnRH receptor antagonist (non-cytotoxic antineoplastic) |
| Myelosuppression Risk | Low — not a conventional cytotoxic; no bone marrow suppression expected |
| Emetogenicity Classification | Minimal (subcutaneous hormonal injection; not classified as emetogenic) |
| Monitoring Items | Serum testosterone and PSA, liver function tests, QTc interval (risk of QT prolongation, particularly with concomitant QT-prolonging drugs), bone mineral density (with prolonged androgen deprivation) |
| Handling Protection | Standard precautions; not classified under cytotoxic chemotherapy handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence or published literature connecting Degarelix to hypertrichosis. The mechanistic link is highly subtype-dependent and does not hold for the majority of hypertrichosis presentations, making this prediction insufficient to justify further investment at this time.

**To proceed toward any indication, the following is needed:**

- **MOA data gap resolution**: Retrieve full DrugBank MOA and toxicology profile (Data Gap DG002) before any mechanistic analysis can be considered complete
- **Safety package**: Obtain and review the full prescribing information / package insert warnings and contraindications (Data Gap DG001 — currently Blocking for safety pre-screening)
- **Subtype stratification for hypertrichosis**: If further exploration is desired, restrict scope strictly to androgen-dependent forms (e.g., hirsutism in hyperandrogenic women); exclude congenital and genetic subtypes entirely
- **Prioritize rank 9 — Central Precocious Puberty (CPP)**: Among all 10 predicted indications, CPP (rank 9, evidence L4) has the strongest pharmacological rationale — GnRH antagonists directly interrupt the overactivated hypothalamic-pituitary-gonadal axis that defines CPP pathology, and the class effect is already established through approved GnRH agonists (leuprolide, histrelin, triptorelin). A focused literature review and pediatric dosing/formulation assessment for Degarelix in CPP is the recommended next research question
- **Exclude mechanistically mismatched predictions**: Rank 2 (Ambras syndrome), rank 3 (Dandy-Walker malformation), rank 5 (genetic hair shaft abnormality), and rank 8 (familial male-limited precocious puberty) all have explicit mechanistic incompatibilities documented in the evidence pack and should be deprioritized with no further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

