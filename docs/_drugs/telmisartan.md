---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension Management to Recurrent Intracerebral Hemorrhage Prevention

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 (AT1) receptor blocker (ARB); the evidence pack does not contain a formally documented original indication or MOA text (both flagged as data gaps), but the drug's own literature evidence base consistently describes it as an antihypertensive ARB. TxGNN screened 10 candidate new indications for telmisartan — the single highest-scoring prediction (Prinzmetal angina, 99.98%) has **zero** supporting trials or literature, while the two best-*evidenced* candidates, **cerebral artery occlusion** and **recurrent intracerebral hemorrhage (ICH) prevention**, are each backed by a completed large-scale RCT (n=1,228 and n=1,671 respectively) plus a substantial preclinical literature base. Overall evidence quality is still exploratory (L2 at best), and a Blocking data gap (missing TFDA label/safety data) prevents formal safety screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Taiwan license records; original_indications field empty) |
| Predicted New Indication (best-evidenced) | Recurrent Intracerebral Hemorrhage / Cerebral Artery Occlusion (ischemic stroke prevention) |
| Predicted New Indication (highest model score) | Prinzmetal angina (no supporting evidence) |
| TxGNN Prediction Score | 99.93% (ICH) / 99.95% (cerebral artery occlusion) / 99.98% (Prinzmetal angina, top rank) |
| Evidence Level | L2 (ICH and cerebral artery occlusion); L5 for most other candidates |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## All 10 Predicted Indications at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Prinzmetal angina | 99.98% | L5 | Hold |
| 2 | Brain stem infarction | 99.98% | L5 | Hold |
| 3 | ABri amyloidosis | 99.97% | L5 | Hold |
| 4 | Cerebral artery occlusion | 99.95% | L2 | Research Question |
| 5 | Pulmonary hypertension (lung disease/hypoxia) | 99.93% | L5 | Hold |
| 6 | Pulmonary hypertension (unclear multifactorial) | 99.93% | L5 | Hold |
| 7 | Malignant renovascular hypertension | 99.93% | L4 | Proceed with Guardrails |
| 8 | Malignant hypertensive renal disease | 99.93% | L4 | Proceed with Guardrails |
| 9 | Intracerebral hemorrhage (recurrence prevention) | 99.93% | L2 | Research Question |
| 10 | Braddock syndrome | 99.92% | L5 | Hold |

Ranks 7–8 (renovascular/renal hypertension) have no dedicated trials but score higher on recommendation because they are direct pharmacological extensions of telmisartan's known antihypertensive/AT1-blocking action. Ranks 1–3, 5–6, and 10 returned no clinical trial or literature hits in ClinicalTrials.gov, ICTRP, or PubMed searches and are treated as model noise pending further data.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the literature evidence retrieved for this drug, telmisartan is consistently characterized as a highly lipid-soluble AT1 receptor (angiotensin II type 1) blocker with partial PPARγ agonist activity ("metabo-sartan"), used for blood pressure control.

For **cerebral artery occlusion**, the mechanistic link runs through blood-pressure lowering plus AT1-blockade-mediated anti-inflammatory and antioxidative effects. Multiple rodent transient middle cerebral artery occlusion (tMCAO) studies show telmisartan reduces infarct volume, oxidative stress markers, and pro-inflammatory signaling (e.g., Egr-1, MCP-1, TNF-α), and a completed Phase 4 trial (n=1,228) demonstrated cardiovascular event and biomarker benefits in high-risk hypertensive patients.

For **recurrent intracerebral hemorrhage prevention**, the rationale is that blood pressure is the single most modifiable risk factor for ICH recurrence. The completed Phase 3 TRIDENT trial (n=1,671) tested a fixed-dose triple antihypertensive combination (which may include an ARB-class agent) specifically in patients with a history of ICH, and animal studies show telmisartan reduces oxidative stress and vasospasm after subarachnoid/intracerebral hemorrhage.

For **malignant renovascular hypertension / malignant hypertensive renal disease**, the link is the most direct of all: these are severe forms of the condition telmisartan's AT1-blocking mechanism is designed to treat. No indication-specific trials exist, but the mechanistic plausibility is high — tempered by the known risk of ARBs precipitating acute kidney injury in bilateral renal artery stenosis, which is why these are flagged "Proceed with Guardrails" rather than "Research Question."

---

## Clinical Trial Evidence

### Cerebral Artery Occlusion

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1,228 | Open-label PROBE study comparing telmisartan (ARB) vs. ordinary therapy on cardiovascular biomarkers and event onset in high-risk hypertensive patients; indirect relevance (Grade B). |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; terminated with only 4 enrolled, underpowered (Grade C). |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated with 1 participant, no usable evidence (Grade C). |

### Recurrent Intracerebral Hemorrhage

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: fixed low-dose "Triple Pill" BP-lowering strategy vs. standard care for preventing recurrent stroke in patients with prior ICH; largest and most directly relevant trial in this evidence pack (Grade A). |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; terminated, underpowered (Grade C). |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated, no usable evidence (Grade C). |

### Other Indications

Currently no related clinical trials registered for Prinzmetal angina, brain stem infarction, ABri amyloidosis, either pulmonary hypertension subtype, malignant renovascular hypertension, malignant hypertensive renal disease, or Braddock syndrome.

---

## Literature Evidence

### Cerebral Artery Occlusion (selected from 17 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Cohort/Animal | J Neurotrauma | AT1 blocker telmisartan reduces cerebral infarct volume and peri-infarct cPLA2 levels in experimental stroke. |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Animal | PLoS ONE | Head-to-head comparison of telmisartan, ramipril, and combination across multiple rat stroke models for prevention and neuroprotection. |
| [18360031](https://pubmed.ncbi.nlm.nih.gov/18360031/) | 2008 | Animal | Hypertens Res | Telmisartan attenuates focal brain ischemia in atherosclerotic ApoE-deficient mice. |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | Animal | J Hypertens | Low-dose telmisartan prevents ischemic brain damage via PPARγ activation in diabetic mice. |
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | Animal | J Stroke Cerebrovasc Dis | Telmisartan reduces oxidative stress and phosphorylated α-synuclein accumulation after tMCAO in SHR-SR rats. |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | Animal | J Stroke Cerebrovasc Dis | Telmisartan ameliorates inflammatory responses (MCP-1, TNF-α, Iba-1) after tMCAO in SHR-SR rats. |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Animal mechanistic | J Stroke Cerebrovasc Dis | PPARγ activation by telmisartan inhibits Egr-1, reducing brain injury in an ischemic stroke model. |

### Recurrent Intracerebral Hemorrhage (selected from 11 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial protocol | Int J Stroke | Rationale/design paper for the TRIDENT trial (single-pill BP-lowering combination for ICH secondary prevention). |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Cohort (PRoFESS sub-analysis) | Int J Stroke | Race-ethnic differences in ischemic vs. hemorrhagic stroke recurrence rates in a >20,000-patient secondary prevention trial. |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Animal | J Pharmacol Exp Ther | AT1 receptor blockade (telmisartan) reduces apoptosis, inflammation, and oxidative stress in an experimental ICH model. |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Animal | Neurol Res | Telmisartan ameliorates oxidative stress and cerebral vasospasm after subarachnoid hemorrhage. |
| [15834293](https://pubmed.ncbi.nlm.nih.gov/15834293/) | 2005 | Comparative pharmacology | J Hypertens | Telmisartan vs. ramipril effects on cerebrovascular structure in spontaneously hypertensive rats. |

### Other Indications

Currently no related literature available for Prinzmetal angina, brain stem infarction, ABri amyloidosis, malignant renovascular hypertension, malignant hypertensive renal disease, or Braddock syndrome. Literature retrieved for the two pulmonary hypertension entries and ABri amyloidosis consisted of generic hypoxia/amyloidosis biology unrelated to telmisartan specifically, and is not included here as evidence.

---

## Taiwan Market Information

Telmisartan currently has **no marketing authorization on record in Taiwan** (market status: 未上市 / not marketed; 0 licenses). No product name, dosage form, or approved-indication data is available from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were all flagged as data gaps in this evidence pack — TFDA label data is a Blocking-severity gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (missing TFDA package insert / warnings and contraindications) prevents this candidate from entering the S1 safety pre-screen, regardless of the indication-level evidence strength. Among the 10 predicted indications, only cerebral artery occlusion and recurrent ICH prevention reach L2/S2 ("Research Question") — supported by one completed Phase 4 (n=1,228) and one completed Phase 3 (n=1,671) trial respectively — while the remaining candidates, including the single highest-scoring prediction (Prinzmetal angina), have no clinical or literature support at all (L5/S0).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to clear the S1 safety gate (DG001, Blocking)
- Formal mechanism-of-action documentation from DrugBank (DG002, High)
- Confirmation of Taiwan market/licensing status, since no authorizations are currently on record
- If pursuing cerebral artery occlusion or ICH prevention specifically: a focused review of the TRIDENT trial's actual drug regimen (to confirm telmisartan's specific contribution vs. the combination pill) and DDI data given the renal/hyperkalemia risk relevant to the renovascular/renal hypertension candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

