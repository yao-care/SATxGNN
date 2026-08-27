---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 519
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pregabalin: From Neuropathic Pain to Migraine Prevention

## One-Sentence Summary

Pregabalin is a gabapentinoid originally used for neuropathic pain, epilepsy (adjunctive), generalized anxiety disorder, and fibromyalgia. The TxGNN model's top mechanistically-supported prediction is **Migraine Disorder** (prevention), backed by **3 clinical trials** and **19 publications**, though the only registered Phase 3 trial for this indication was withdrawn before completion. TxGNN also flagged five other candidates (tendinitis and four musculoskeletal/migraine-subtype indications), but none of these carry meaningful clinical evidence — they are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (licenses list is empty, MOA marked Data Gap). Pregabalin's globally approved indications are neuropathic pain, epilepsy (adjunctive therapy), generalized anxiety disorder, and fibromyalgia. |
| Predicted New Indication | Migraine Disorder (prevention) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Priority) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pregabalin is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacology, pregabalin is a gabapentinoid that binds the α2δ subunit of voltage-gated calcium channels, reducing excitatory neurotransmitter release and dampening central sensitization. Preclinical work (PMID 28223480, published in PNAS, and PMID 37924146) shows pregabalin raises the threshold for cortical spreading depression (CSD) and suppresses its propagation to subcortical structures — CSD is considered a core driver of migraine aura and attack initiation.

This mechanistic link connects pregabalin's proven neuropathic-pain/central-sensitization activity to migraine pathophysiology, which shares central sensitization as a key feature. Consistent with this, gabapentin — a closely related gabapentinoid — has a longer history of exploration in migraine prophylaxis, and several small RCTs and cohort studies (below) have tested pregabalin directly in both pediatric and adult migraine prevention.

The main caveat: the single Phase 3 RCT registered specifically for migraine prevention (NCT00447369) was **withdrawn** before generating results, so the L2 evidence level rests on smaller RCTs, cohort studies, and Cochrane-level reviews rather than a completed pivotal trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) | Phase 3 | Withdrawn | 70 | Designed as a randomized, blinded crossover study comparing pregabalin vs. sodium valproate for migraine prevention; withdrawn before enrollment completion, no efficacy data generated. |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Phase 4 | Completed | 200 | Studied fMRI-based "brain signatures" of chronic pain in chronic migraine and fibromyalgia patients; mechanistic/biomarker study, not a pregabalin efficacy trial. |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3300 | Pragmatic EMR-based quality-improvement study across 10 neurological disorders; observational, not a dedicated efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iranian J Child Neurology | Compared pregabalin vs. sodium valproate for pediatric migraine prophylaxis. |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Medica Iranica | Randomized trial comparing propranolol vs. pregabalin in childhood migraine prophylaxis. |
| [23797675](https://pubmed.ncbi.nlm.nih.gov/23797675/) | 2013 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of gabapentin/pregabalin for episodic migraine prophylaxis in adults. |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-analysis | JAMA Network Open | Compares preventive medications (including pregabalin) for pediatric migraine. |
| [19935409](https://pubmed.ncbi.nlm.nih.gov/19935409/) | 2010 | Open-label study | Clinical Neuropharmacology | Open-label study assessing pregabalin for chronic migraine prevention. |
| [21479703](https://pubmed.ncbi.nlm.nih.gov/21479703/) | 2011 | Cohort | J Headache Pain | 3-month follow-up on efficacy and tolerability of pregabalin as preventive migraine treatment. |
| [25669613](https://pubmed.ncbi.nlm.nih.gov/25669613/) | 2015 | Cohort | Int J Clin Pharmacol Ther | Evaluated pregabalin's effect on central sensitization/allodynia in migraine patients. |
| [28476535](https://pubmed.ncbi.nlm.nih.gov/28476535/) | 2017 | Review | Drug Discovery Today | Reviews animal pain/migraine models used in analgesic drug discovery, including pregabalin. |
| [37924146](https://pubmed.ncbi.nlm.nih.gov/37924146/) | 2023 | Preclinical | Molecular Brain | Chronic pregabalin protects against spreading depolarization in a familial hemiplegic migraine model. |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | Preclinical | PNAS | In vivo imaging shows pregabalin inhibits cortical spreading depression and its subcortical propagation. |

---

## Saudi Arabia Market Information

Pregabalin currently has no marketing authorization registered in this evidence pack (0 licenses, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA warnings, contraindications, and DDI queries all returned no data in this evidence pack — see data gaps below.)

---

## Other TxGNN-Predicted Indications (Screened, Lower Priority)

The same evidence pack screened five additional candidates for pregabalin. None currently warrant active investment:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Tendinitis | 99.71% | L4 | Hold | Highest raw TxGNN score, but supporting literature is limited to pregabalin's opioid-sparing use in post-arthroscopic analgesia — not treatment of tendon pathology itself. Mechanistic link is weak. |
| Idiopathic granulomatous myositis | 99.71% | L5 | Hold | No clinical trials or literature; likely a knowledge-graph proximity artifact. |
| Myositis fibrosa | 99.71% | L5 | Hold | No clinical trials or literature; same as above. |
| Inclusion body myositis | 99.52% | L5 | Hold | No clinical trials or literature; pregabalin's calcium-channel target has no known link to inflammatory myopathy pathology. |
| Migraine with brainstem aura | 99.43% | L5 | Hold | Same CSD-suppression hypothesis as migraine disorder, but no dedicated trials or case evidence for this subtype specifically. |

---

## Conclusion and Next Steps

**Decision: Hold (Research Priority)**

**Rationale:**
Migraine disorder is the only predicted indication with a coherent mechanism (CSD suppression, central sensitization) and a body of supporting RCTs/cohort studies (L2), but the sole registered Phase 3 trial was withdrawn without results, so no confirmatory pivotal trial exists. The remaining five predicted indications lack clinical or mechanistic support and should not be prioritized.

**To proceed, the following is needed:**
- SFDA/TFDA package insert warnings and contraindications (Blocking data gap — currently unavailable)
- Confirmed mechanism of action documentation from DrugBank (High-severity data gap)
- Drug interaction (DDI) profile (query returned no data)
- A properly powered, completed Phase 2/3 RCT specifically for migraine prevention, given the prior trial's withdrawal
- Saudi Arabia regulatory/marketing status confirmation (currently 0 registered licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

