---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract-Surgery Ocular Inflammation to Eye Disease

## One-Sentence Summary

> Nepafenac is a topical ophthalmic NSAID whose established clinical use is controlling pain and inflammation after cataract and other ocular surgeries.
> The TxGNN model predicts high relevance for **eye disease** (a broad category), with **41 clinical trials** and **20 publications** currently available as supporting evidence.
> Notably, the evidence itself indicates this "prediction" largely reconfirms the drug's already-established use rather than identifying a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on file for this market (drug unmarketed); trial evidence confirms established use in post-cataract-surgery ocular inflammation/pain |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is a prodrug that, after topical ocular administration, is hydrolyzed by intraocular esterases into its active metabolite, amfenac. Amfenac inhibits COX-1 and COX-2, reducing prostaglandin synthesis and thereby producing ocular anti-inflammatory, analgesic, and anti-cystoid-macular-edema (CME) effects.

"Eye disease" is a broad TxGNN category, and the underlying clinical trial and literature evidence overwhelmingly concerns nepafenac's use around cataract surgery (postoperative pain, inflammation, and CME prevention) — which is the drug's well-established, already-approved application in multiple markets. The evidence pack's own repurposing rationale flags this explicitly: this is not a novel repurposing target but an existing, proven use being surfaced by the model.

This matters for interpretation: the very high evidence level (L1) reflects the depth of evidence behind nepafenac's *known* ophthalmic anti-inflammatory role, not a new mechanistic hypothesis. Any regulatory value here lies in confirming and formally registering an already-supported use in this market, rather than pursuing a novel therapeutic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084576](https://clinicaltrials.gov/study/NCT02084576) | Phase 4 | Completed | 40 | Nepafenac 0.1% vs ketorolac 0.4% for prevention of cystoid macular edema after phacoemulsification (direct efficacy endpoint) |
| [NCT00347204](https://clinicaltrials.gov/study/NCT00347204) | Phase 4 | Completed | 40 | Head-to-head RCT vs Acular LS for postoperative pain control after PRK |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Large comparison of nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of post-cataract-surgery inflammation and pain |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Nepafenac 0.1% reduced macular volume after epiretinal membrane surgery vs placebo |
| [NCT01939691](https://clinicaltrials.gov/study/NCT01939691) | Phase 4 | Terminated | 9 | Nepafenac vs difluprednate for uveitic macular edema; terminated early, underpowered |
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Large pivotal study of nepafenac 0.3% for prevention/treatment of post-cataract-surgery inflammation and pain |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Nepafenac 0.3% QD superior to vehicle in diabetic patients following cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% QD demonstrated superiority over vehicle in diabetic subjects post-cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Adjunctive nepafenac 0.3% vs placebo for prevention of pseudophakic cystoid macular edema |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Bioequivalence study of generic nepafenac 0.3% vs Ilevro for post-cataract-surgery pain/inflammation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone acetate 1% for postoperative inflammation control after micro-incisional cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology. Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation control after laser peripheral iridotomy |
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review/Meta-analysis | Eur J Ophthalmol | Nepafenac's effect on macular swelling and visual outcomes after cataract surgery |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic and therapeutic agents, including topical NSAIDs, for non-infectious corneal injury |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Cohort | Curr Eye Res | Intracameral nepafenac safety and efficacy in inhibiting prostaglandin synthesis during phacoemulsification |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Cohort | Acta Ophthalmol | Nepafenac vs preservative-free diclofenac for postoperative management after cataract surgery |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 RCT | J Cataract Refract Surg | Once-daily nepafenac 0.3% to prevent/treat ocular inflammation and pain after cataract surgery |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | Prophylactic nepafenac vs ketorolac vs placebo for postoperative macular edema after phacoemulsification |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | Comparative study | Int J Ophthalmol | Bromfenac vs nepafenac vs diclofenac for prevention of cystoid macular edema after phacoemulsification |
| [19040348](https://pubmed.ncbi.nlm.nih.gov/19040348/) | 2008 | RCT | J Ocul Pharmacol Ther | Nepafenac dosing frequency (QD/BID/TID) for ocular pain and inflammation after cataract surgery |

---

## Saudi Arabia Market Information

Nepafenac currently has no marketing authorizations registered in Saudi Arabia (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by an unusually deep evidence base (multiple large completed Phase 3 RCTs, e.g. NCT01109173 with n=2120), but this evidence supports nepafenac's already-established use in post-cataract-surgery ocular inflammation and pain rather than a novel therapeutic hypothesis — the "eye disease" prediction should be understood as a confirmation, not a discovery.

**To proceed, the following is needed:**
- Local package insert / label data (warnings, contraindications) — currently a Blocking data gap
- Verified mechanism-of-action documentation from DrugBank or equivalent source
- Confirmation of local marketing/registration status and pathway, given the drug is currently unmarketed in this jurisdiction
- Narrowing of the broad "eye disease" prediction to a specific, registrable indication (e.g., post-surgical ocular inflammation/pain) before regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

