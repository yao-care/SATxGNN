---
layout: default
title: Dipivefrin
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 1
---

# Dipivefrin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# DIPIVEFRIN: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dipivefrin is a prodrug of epinephrine historically used to lower intraocular pressure (IOP) in open-angle glaucoma by enhancing corneal penetration of its active metabolite. The TxGNN model predicts a potential application in **Primary Hereditary Glaucoma** (score: 99.45%), citing IOP reduction as a shared therapeutic endpoint; however, **no directly relevant clinical trials or published literature** were identified to support this specific repurposing direction. Evidence remains at a mechanistic-hypothesis stage (L4), and the drug is not currently registered in Saudi Arabia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (general pharmacological record; not registered in Saudi Arabia) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dipivefrin is a dipivalyl ester prodrug of epinephrine, engineered to achieve substantially greater corneal penetration than epinephrine alone. After topical instillation, corneal esterases rapidly hydrolyze it to release active epinephrine, which then exerts dual adrenergic effects: β-receptor stimulation suppresses aqueous humor production, while α-receptor stimulation promotes uveoscleral outflow. This two-pronged IOP-lowering mechanism underpins its established role in open-angle glaucoma and ocular hypertension.

Primary hereditary glaucoma — encompassing congenital and juvenile-onset forms — shares the same fundamental consequence as open-angle glaucoma: chronically elevated IOP causing progressive optic nerve damage. The critical distinction, however, is etiology. Hereditary glaucoma arises from structural malformation of the trabecular meshwork (commonly linked to mutations in *CYP1B1* or *MYOC*), rather than a functional outflow deficiency. Adrenergic agents that enhance aqueous drainage are mechanistically well-suited to functional obstruction but face an attenuated response when the drainage architecture is anatomically abnormal — the drug cannot correct what is structurally absent.

The TxGNN model's high-confidence score (99.45%) reflects the topological proximity of "primary hereditary glaucoma" and "open-angle glaucoma" within the disease knowledge graph, and the convergent endpoint of IOP reduction. While this mechanistic bridge is scientifically coherent and positions dipivefrin as a plausible adjunctive IOP-lowering agent, it is unlikely to be curative in a structurally driven disease. This prediction is best treated as a hypothesis-generating signal warranting targeted preclinical investigation before any clinical planning is considered.

---

## Clinical Trial Evidence

One trial was retrieved during the database query. Upon expert review, it is **not relevant** to dipivefrin pharmacotherapy or primary hereditary glaucoma — it represents a false-positive match arising from proximity between adjacent ophthalmology disease nodes in the TxGNN knowledge graph.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03763721](https://clinicaltrials.gov/study/NCT03763721) | N/A | Completed | 65 | Evaluated intra-operative OCT imaging guidance for posterior lamellar keratoplasty (corneal transplant surgery). No dipivefrin involvement; no hereditary glaucoma treatment focus. **Not relevant to this repurposing candidate.** |

No directly relevant clinical trials for dipivefrin in primary hereditary glaucoma are currently registered.

---

## Literature Evidence

Currently no related literature available.

No PubMed publications were identified specifically investigating dipivefrin or its active metabolite epinephrine in the context of primary hereditary glaucoma.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction carries a mechanistically coherent rationale — dipivefrin delivers IOP-lowering epinephrine to the anterior chamber, and sustained IOP elevation is the defining harm in primary hereditary glaucoma — but the structural trabecular mesh defect underlying the hereditary form fundamentally limits pharmacological efficacy. With no clinical trials, no published literature, no Saudi Arabia registration, and all safety data pending, the evidence base is insufficient to advance beyond a research hypothesis at this stage.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or animal model) demonstrating IOP-lowering efficacy of dipivefrin or epinephrine in hereditary/congenital glaucoma models carrying *CYP1B1* or *MYOC* mutations
- Mechanism of action documentation from DrugBank to confirm the full adrenergic receptor binding and off-target profile
- Safety data retrieval: key warnings, contraindications, and drug interaction profile from the original package insert
- Clinical context assessment — determining whether pharmacological adjuncts have a defined role alongside first-line surgical interventions (goniotomy, trabeculotomy) in hereditary glaucoma management
- Saudi Arabia regulatory pathway scoping if preclinical data proves supportive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

