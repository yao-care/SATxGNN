---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: From Glaucoma / Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor (CAI) internationally established for reducing intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with **1 completed Phase 2 clinical trial** directly testing dorzolamide in pediatric hereditary glaucoma supporting this direction.
The same IOP-lowering mechanism underpins both the established use and this prediction, making the model's output pharmacologically consistent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (internationally recognized; not registered in Saudi Arabia) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (1 completed Phase 2 trial) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dorzolamide is a second-generation topical carbonic anhydrase inhibitor (CAI). Its core mechanism of action involves blocking the enzyme carbonic anhydrase II in the ciliary body epithelium of the eye, which reduces bicarbonate and fluid secretion into the anterior chamber. The net result is a lower rate of aqueous humor production and a reduction in intraocular pressure (IOP). Critically, this mechanism is independent of the underlying cause of elevated IOP — it acts upstream of the pathological process itself.

Primary hereditary glaucoma is a genetically determined form of glaucoma, most commonly arising from mutations in genes such as *CYP1B1* or *MYOC*, and typically presents in infancy or early childhood with high IOP, corneal enlargement (buphthalmos), and progressive optic nerve damage. Despite its genetic origin, the fundamental driver of vision loss is the same as in adult open-angle glaucoma: sustained elevated IOP injuring the optic nerve. Since dorzolamide reduces IOP by suppressing aqueous humor secretion rather than by modifying trabecular outflow, it can effectively lower pressure regardless of whether the dysfunction is inherited or acquired.

Dorzolamide is therefore a pharmacologically rational candidate for primary hereditary glaucoma. One completed Phase 2 trial (NCT01527682) directly tested its ocular hypotensive effect in pediatric patients with hereditary glaucoma who were refractory to surgical procedures, providing early clinical support that the prediction is more than theoretical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Evaluated the ocular hypotensive effect of dorzolamide vs. latanoprost in pediatric patients with primary hereditary glaucoma refractory to surgical procedures; safety was a co-endpoint |

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dorzolamide's carbonic anhydrase inhibition mechanism is directly applicable to primary hereditary glaucoma, but evidence is limited to a single small Phase 2 trial (n=37), the drug has no current registration in Saudi Arabia, and essential safety documentation (contraindications, warnings, drug interactions) has not yet been retrieved into the Evidence Pack.

**To proceed, the following is needed:**
- Clarify the Saudi Arabia regulatory pathway — SFDA registration or named-patient importation — before any clinical deployment
- Retrieve and review the published results and safety data from NCT01527682
- Complete safety documentation: obtain contraindications, key warnings, and drug interaction profile (DG001 remediation via package insert PDF)
- Obtain detailed mechanism of action documentation from DrugBank (DG002 remediation)
- Evaluate whether the extensive evidence base for open-angle glaucoma (41+ clinical trials, 20+ publications at ranks 6–7) could support a broader glaucoma indication registration in Saudi Arabia as a prerequisite step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

