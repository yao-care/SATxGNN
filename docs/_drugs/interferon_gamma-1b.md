---
layout: default
title: Interferon Gamma-1B
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Interferon Gamma-1B
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

# Interferon Gamma-1b: From Chronic Granulomatous Disease to Heart Disease

## One-Sentence Summary

Interferon gamma-1b is a recombinant Th1 immune activator approved for chronic granulomatous disease (CGD) and severe malignant osteopetrosis. The TxGNN model predicts it may be effective for **Heart Disease**, but this is currently a **model-only prediction (L4)** — none of the 50 retrieved clinical trials directly test interferon gamma-1b in heart disease, and the 5 literature hits are indirect (mostly CGD-related cardiac complication case reports).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Granulomatous Disease (CGD) / Severe Malignant Osteopetrosis |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank MOA data for interferon gamma-1b is currently a data gap (DG002). Based on the evidence pack's mechanistic notes, interferon gamma-1b is a Th1 immune activator whose approved uses (CGD, malignant osteopetrosis) rely on macrophage activation and anti-infective/anti-inflammatory signaling.

There is no established pathophysiological pathway connecting this macrophage-activation mechanism to "heart disease" as a broad category. The retrieved literature largely consists of case reports describing cardiac infectious or inflammatory complications (endocarditis, pericarditis) occurring in immunodeficient or CGD patients — these describe complications arising *in* patients who might receive the drug for their primary immune condition, not evidence that interferon gamma-1b treats cardiac disease itself.

Given that "heart disease" is also an extremely broad, non-specific disease label, and the associated clinical trials in this evidence pack are predominantly unrelated exercise/rehabilitation or other-drug studies (graded "C" — not relevant), this prediction should be treated as a hypothesis generated purely by the TxGNN model rather than one supported by targeted evidence.

## Clinical Trial Evidence

Of the 50 retrieved trials, none directly evaluate interferon gamma-1b for heart disease. The trials below (first 10 in retrieval order) were graded by the pipeline's relevance assessment; most (Grade C) were judged unrelated to this drug–indication pair, and the remainder are ungraded ("pending") but do not involve interferon gamma-1b either.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03652519](https://clinicaltrials.gov/study/NCT03652519) | NA | Completed | 72 | Grade C – exercise/immune-signalling trial in MS; does not use interferon gamma-1b |
| [NCT04356248](https://clinicaltrials.gov/study/NCT04356248) | NA | Completed | 106 | Grade C – exercise training trial in MS; not a drug study |
| [NCT03672812](https://clinicaltrials.gov/study/NCT03672812) | Phase 3 | Completed | 50 | Grade C – studies liraglutide in brain-death organ donors; unrelated drug |
| [NCT07099911](https://clinicaltrials.gov/study/NCT07099911) | NA | Recruiting | 20 | Ungraded – neuromuscular electrical stimulation for glucose control, no drug arm |
| [NCT05650333](https://clinicaltrials.gov/study/NCT05650333) | Phase 1 | Completed | 15 | Grade C – studies ritlecitinib (JAK3 inhibitor) in alopecia areata; unrelated drug |
| [NCT05027958](https://clinicaltrials.gov/study/NCT05027958) | Early Phase 1 | Completed | 17 | Ungraded – mycobacterial antigen instillation immune-response study |
| [NCT02489383](https://clinicaltrials.gov/study/NCT02489383) | NA | Unknown | 60 | Ungraded – aerobic exercise training in asthma patients |
| [NCT00974142](https://clinicaltrials.gov/study/NCT00974142) | Phase 1/2 | Completed | 43 | Ungraded – oral cyclosporine A in advanced COPD |
| [NCT03904277](https://clinicaltrials.gov/study/NCT03904277) | N/A | Completed | 28 | Ungraded – patent foramen ovale physiology study, no drug intervention |
| [NCT02799095](https://clinicaltrials.gov/study/NCT02799095) | Phase 1/2 | Completed | 243 | Grade C – studies ALKS 4230 (IL-2 variant) in solid tumors; unrelated drug |

**No clinical trial in this evidence pack tests interferon gamma-1b for heart disease.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Systematic Review | Therapeutic Advances in Rare Disease | Reviews therapeutic interventions in Friedreich ataxia; not specific to heart disease or interferon gamma-1b efficacy |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Case Report | European Heart Journal – Case Reports | Case of prosthetic valve infective endocarditis from Mycobacterium chimaera after cardiac surgery; does not involve interferon gamma-1b treatment |
| [29456196](https://pubmed.ncbi.nlm.nih.gov/29456196/) | 2018 | Case Report | Journal of Cystic Fibrosis | Fungal airway infection responding to interferon-gamma therapy in a cystic fibrosis patient; respiratory, not cardiac |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Cohort/Validation Study | American Journal of Respiratory and Critical Care Medicine | Validates the 6-minute-walk test in idiopathic pulmonary fibrosis; no drug intervention |
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Case Report | Turk Kardiyoloji Dernegi Arsivi | Constrictive Aspergillus pericarditis in a child with chronic granulomatous disease and congestive heart failure; describes a cardiac complication of CGD, not a treatment trial |

**None of these publications report interferon gamma-1b being used to treat heart disease; the cardiac-related items describe complications occurring in immunocompromised/CGD patients.**

## Saudi Arabia Market Information

Interferon gamma-1b is currently **not marketed** in Saudi Arabia — no authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA package insert warnings and contraindications are a blocking data gap — DG001 — and drug interaction data was not found in the queried database.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no clinical trial or literature evidence directly supports interferon gamma-1b as a treatment for heart disease — the retrieved trials are predominantly unrelated studies, and the literature only shows indirect cardiac complications in immunodeficient patients. Combined with the drug's absence from the Saudi Arabian market, the evidence base does not support proceeding beyond hypothesis generation.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- Verified mechanism of action data from DrugBank — currently a high-severity data gap (DG002)
- A hypothesis-driven mechanistic rationale linking Th1/macrophage activation to a specific cardiac disease subtype (the current "heart disease" label is too broad to act on)
- At least one dedicated preclinical or clinical study testing interferon gamma-1b in a defined cardiac indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

