---
layout: default
title: Pheniramine
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 3
---

# Pheniramine
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

# Pheniramine: From Allergic Symptom Relief to Allergic Urticaria

## One-Sentence Summary

Pheniramine is a first-generation alkylamine H1-antihistamine; no specific original indication record or marketing license exists in this dataset, but the drug class is classically used for allergic symptom relief (rhinitis, pruritus, urticaria). The TxGNN model predicts it may be effective for **Allergic Urticaria**, with only **1 clinical trial (low relevance, likely a database mismatch)** and **20 publications** — mostly case reports and reviews of the related compound chlorpheniramine — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not licensed in Saudi Arabia); class-level use is allergic symptom relief |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 (preclinical/mechanistic and case-level evidence only) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for pheniramine itself is not available in this dataset (Data Gap DG002). Based on known pharmacology, pheniramine belongs to the alkylamine class of first-generation H1-receptor antagonists — the same class as chlorpheniramine and dexchlorpheniramine. H1 blockade inhibits histamine-driven vasodilation and vascular permeability, the core pathophysiology of urticarial wheal-and-flare reactions.

Because allergic urticaria and other histamine-mediated allergic conditions (e.g. allergic rhinitis, angioedema) share the same H1-receptor pathway, a class-level mechanistic link to urticaria is pharmacologically plausible. This is reinforced by the literature base returned for this prediction, which is dominated by chlorpheniramine (a close structural analog) studies explicitly covering chronic urticaria, and by two case reports involving pheniramine itself in acute allergic/hypersensitivity settings.

However, this mechanistic plausibility is class-level reasoning, not drug-specific confirmation. The one clinical trial returned (NCT02082054) was flagged by the evidence review as a likely atropine/chlorpheniramine database mismatch rather than a genuine pheniramine trial, and no RCT or systematic review directly evaluates pheniramine in allergic urticaria.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Dose-ranging study of atropine combined with pseudoephedrine/chlorpheniramine in seasonal allergic rhinitis. **Relevance: Grade C** — title centers on atropine dosing, not pheniramine; likely a drug-class/database mismatch rather than direct trial evidence for this candidate. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised comparative study | Eur J Pharm Sci | Randomised Phase 1 trial comparing oral bilastine and parenteral dexchlorpheniramine (a pheniramine analog) on histamine-induced wheal-and-flare response |
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine (close analog), covering use in chronic urticaria, asthma, and other allergic conditions |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Surveillance/Cohort | Methods Find Exp Clin Pharmacol | Large-scale surveillance (n=1,742) of sedative profiles across H1-antihistamines, disease-dependent |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case report | Cureus | Immediate hypersensitivity reaction to pheniramine itself, in a patient with multiple drug hypersensitivity syndrome |
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case report | Indian J Pharmacol | Serious adverse event (loss of consciousness) following concurrent IV pheniramine and hydrocortisone for an allergic reaction |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case report/Pharmacovigilance review | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus retrospective pharmacovigilance review; notes chlorpheniramine's common use across urticaria and rhinitis |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Review/Case series | Am J Med | Atrial fibrillation as a cardiovascular complication of anaphylaxis |
| [32641443](https://pubmed.ncbi.nlm.nih.gov/32641443/) | 2020 | Case report | BMJ Case Rep | Urticaria and angioedema as a prodromal cutaneous sign of COVID-19 |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Case report | Contact Dermatitis | Palpebral angioedema and allergic contact dermatitis from a cerumenolytic agent |
| [25372261](https://pubmed.ncbi.nlm.nih.gov/25372261/) | 2014 | Case report | Cutis | Flurbiprofen-induced unilateral eyelid angioedema |

---

## Saudi Arabia Market Information

Pheniramine currently has no marketing authorization on file in Saudi Arabia (market status: Not Marketed, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently on file — TFDA package insert data is flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for pheniramine specifically in allergic urticaria is limited to case reports and analog (chlorpheniramine/dexchlorpheniramine)-based studies (L4); the one clinical trial identified is likely an unrelated database match. Combined with the absence of Saudi Arabia market presence and a Blocking safety data gap (no package insert warnings/contraindications on file), this candidate does not yet meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data specific to pheniramine — currently High priority gap (DG002)
- A pheniramine-specific clinical trial or controlled study in urticaria/allergic skin conditions (current trial evidence is not usable)
- Drug interaction (DDI) database entry, currently not found

*Note: Two additional TxGNN predictions for this drug (nasal cavity disease, acute laryngopharyngitis) were also reviewed and scored L4/L5 with Hold recommendations — animal-model-only or no supporting evidence respectively — and are not advanced further at this stage.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

