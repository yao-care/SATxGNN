---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a well-established intravenous general anesthetic and sedative agent, used for induction/maintenance of general anesthesia and procedural sedation. The TxGNN model predicts it may be effective for **Migraine Disorder** at sub-anesthetic doses, with **5 clinical trials** and **19 publications** currently supporting this direction, including one completed Phase 2/3 RCT.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia induction/maintenance and procedural sedation (well-established use; no formal approved-indication text available — drug is not marketed in this jurisdiction) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for this candidate is currently a data gap (DrugBank MOA field not populated). Based on known pharmacology and the evidence-pack rationale, propofol is a **GABA-A receptor positive modulator** with central sedative effects, and it has been shown to suppress **cortical spreading depression (CSD)** — the neurophysiological correlate of migraine aura. This mechanism could interrupt cortical hyperexcitability and trigeminovascular activation that drive a migraine attack.

The link between propofol's original use (general anesthesia/sedation) and the predicted new indication (migraine) is not disease-similarity based but mechanism-based: sub-anesthetic ("low-dose") propofol infusion has been used off-label as an abortive agent for refractory migraine since at least 2000, well outside its anesthetic dose range. This gives a 20+ year track record of clinical observation layered on top of the CSD-suppression mechanism.

This mechanistic plausibility is reinforced by real clinical use: emergency departments (particularly pediatric EDs) have piloted low-dose propofol as second-line abortive therapy when first-line agents (NSAIDs, triptans, dopamine antagonists) fail, and the 2025 American Headache Society parenteral-therapy guideline update (PMID 41321235) now discusses propofol in this context — indicating the idea has moved from anecdote toward guideline-level discussion, though not yet to first-line recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Low-dose propofol as abortive therapy for pediatric migraine in the ED; core evidence for this indication, directly tests dose regimen in target population |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Low-dose propofol infusion as abortive treatment for pediatric migraine; evaluates efficacy, safe dosing limits, and duration of effect |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Low-dose propofol for severe refractory migraine in the ED; terminated early, small sample limits conclusions but supports feasibility |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Unknown | 130 | Compares propofol vs. sevoflurane anesthesia maintenance and postoperative headache incidence; indirect relevance (anesthesia side-effect study, not a migraine-treatment trial) |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | NA | Completed | 315 | Electroacupuncture vs. propofol-based anesthesia in cardiac surgery; propofol is background anesthetic only, low relevance to migraine indication |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Review/Guideline | Headache | 2025 AHS guideline update on parenteral migraine pharmacotherapy in the ED, includes propofol in evidence assessment |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Acad Emerg Med | Systematic review of propofol safety/efficacy for acute migraine treatment in the ED |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | Prospective RCT: low-dose propofol for pediatric migraine, favorable side-effect profile, potentially shorter ED length of stay |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | RCT: sumatriptan+propofol combination vs. sumatriptan+placebo for acute migraine |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | Pilot RCT | Emerg Med Australas | Pilot RCT: IV propofol at procedural sedation dose vs. standard therapy for ED migraine |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Systematic Review/Network Analysis | Headache | Compares parenteral agents (including propofol) for reducing relapse after acute migraine treatment |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic Review | Cephalalgia | Canadian Headache Society systematic review and recommendations on migraine treatment in emergency settings |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Retrospective/Case series | Expert Rev Neurother | Full drug profile of propofol for management of refractory ("super-refractory") migraine |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Case series | Headache | Original report describing unique effectiveness of IV propofol in treating intractable migraine |

## Saudi Arabia Market Information

Propofol currently has no registered market authorizations in this dataset (0 licenses, market status: 未上市/Not Marketed). No product-level authorization data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are currently a documented data gap — TFDA/SFDA package insert extraction is flagged as a **Blocking** gap in this evidence pack, meaning formal safety review cannot proceed until resolved.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2/3 RCT (NCT01604785) plus a consistent body of smaller RCTs, systematic reviews, and a 2026 professional-society guideline discussion support low-dose propofol as an abortive migraine therapy — sufficient to justify continued evaluation, but the evidence base remains ED/pediatric-skewed with small sample sizes and one terminated trial, so guardrails are warranted rather than an unconditional Go.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Formal DrugBank MOA confirmation (currently a data gap)
- Saudi Arabia regulatory/market status confirmation for propofol (currently shows 0 authorizations)
- Adult-population, adequately powered RCT data (existing strongest trial is pediatric; adult evidence is largely case series/small pilot RCTs)
- Head-to-head comparison against standard first-line abortive migraine therapies to establish relative positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

