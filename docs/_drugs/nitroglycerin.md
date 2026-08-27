---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
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

# Nitroglycerin: From Vasodilator Therapy to Pulmonary Hypertension

## One-Sentence Summary

> Nitroglycerin (NTG, DB00727) is a classic nitric-oxide-donor vasodilator; this evidence pack does not contain a confirmed original regulatory indication (the drug is currently unmarketed in Saudi Arabia).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> with **13 clinical trials** and **20 publications** currently supporting this direction, though a critical safety data gap remains unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licenses on file (未上市); NTG is generically known as an organic nitrate vasodilator, but no approved-indication text is present in this evidence pack |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known pharmacology, nitroglycerin is a nitric oxide (NO) donor: it is metabolized in the liver and vasculature to release NO, which activates the soluble guanylate cyclase (sGC)/cGMP pathway, relaxing vascular smooth muscle. This is the same core pathway exploited by established pulmonary vasodilators such as inhaled nitric oxide and inhaled prostacyclin (PGI2).

Because the evidence pack contains no confirmed original indication, a direct "original vs. new indication" comparison cannot be drawn from regulatory data. However, the clinical evidence base independently shows that this mechanism already translates to pulmonary vascular effects: nebulized/inhaled NTG is used for acute pulmonary vasoreactivity testing in pulmonary arterial hypertension (PAH) and as adjunct therapy for persistent pulmonary hypertension of the newborn (PPHN), both of which are represented in the trial and literature evidence below.

The gap is that this body of evidence is largely acute, procedural, or small-cohort (vasoreactivity testing, perioperative use, neonatal PPHN) rather than confirmatory trials in a chronic PAH population — consistent with the model-assigned evidence level of L2.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | NA | Completed | 20 | Safety and efficacy of nebulized nitroglycerin as a vaso-reactive agent in pulmonary arterial hypertension |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | NA | Completed | 80 | Nebulized nitroglycerin as adjuvant therapy in persistent pulmonary hypertension of newborns (PPHN) |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Nebulized PGI2 vs. nebulized nitroglycerin for pulmonary hypertension after valve replacement surgery |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | IV L-citrulline (NO precursor pathway) vs. placebo in children undergoing cardiopulmonary bypass |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute effect of nitroglycerin infusion on cyclosporine-induced hypertension after cardiac transplantation |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High- vs. low-dose nitroglycerin in sympathetic crashing acute pulmonary edema |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs. furosemide guided by lung ultrasound in acute heart failure (N-FURIOUS pilot) |
| [NCT05373108](https://clinicaltrials.gov/study/NCT05373108) | Phase 4 | Completed | 19 | Endothelin-1 and vasomotor function in cardiac allograft vasculopathy after heart transplant |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function/rehabilitation in hypertension — skeletal muscle afferent feedback |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | Nebulized nitroglycerin as adjuvant in PPHN — RCT in 80 newborns, improved echocardiographic/clinical parameters |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT | J Cardiothorac Vasc Anesth | Dobutamine + nitroglycerin vs. milrinone for pulmonary hypertension in mitral valve surgery |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical Trial | Bull Eur Physiopathol Respir | Sublingual NTG/ISDN reduced pulmonary arterial pressure and PVR in COPD-related pulmonary hypertension (n=27×2) |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Cohort/Review | Cardiology in the Young | Nitroglycerin inhalation for acute PAH in children with congenital heart disease |
| [31425404](https://pubmed.ncbi.nlm.nih.gov/31425404/) | 2020 | Cohort (animal) | Shock | Pulmonary vasodilation by IV organic mononitrites vs. nitroglycerin in aortic cross-clamp induced acute PH (pigs) |
| [8689279](https://pubmed.ncbi.nlm.nih.gov/8689279/) | 1996 | Cohort/Review | New Horizons | Calcium blockade in pulmonary hypertension and hypoxic vasoconstriction |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Clinical study | Annals of Internal Medicine | NTG in 9 chronic pulmonary hypertension patients: cardiac index +40%, PVR −40%, mean PA pressure decreased |
| [15947535](https://pubmed.ncbi.nlm.nih.gov/15947535/) | 2005 | Retrospective cohort | Congestive Heart Failure | Acute hemodynamic effects of IV nitroglycerin and dipyridamole vs. IV epoprostenol in 59 PAH patients |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical study | Anesthesiology | Nitroglycerin inhalation improved postoperative hemodynamics in pulmonary hypertension patients after mitral valve replacement |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | J Am Coll Cardiol | Comprehensive review of nitroglycerin/nitrogen oxide mechanisms in cardiovascular therapeutics |

---

## Safety Considerations

Please refer to the package insert for safety information. **Note:** DG001 (TFDA/SFDA package insert warnings and contraindications) is flagged as a **Blocking** data gap — it must be resolved before this candidate can enter formal safety screening (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is mechanistically plausible (NO/cGMP-mediated pulmonary vasodilation) and supported by L2-level evidence — completed trials and RCTs in PPHN, acute vasoreactivity testing, and perioperative pulmonary hypertension — but no Phase 2/3 RCT has reached completion in a chronic PAH population, and the drug is not currently marketed in Saudi Arabia. Critically, DG001 (Blocking) means formal safety screening (S1) cannot proceed until TFDA/SFDA package insert data is obtained.

**To proceed, the following is needed:**
- SFDA package insert (warnings, contraindications, DDI) to resolve DG001 and unblock S1 safety screening
- Confirmed mechanism of action from DrugBank to resolve DG002
- Confirmation of original approved indication(s), since none are on file in this evidence pack
- A completed Phase 2/3 RCT in a chronic PAH population before advancing beyond "Research Question" stage
- Separate evaluation of rank-3 candidate (Prinzmetal angina), which has substantial trial/literature volume (7 trials, 20 publications) but pending relevance scoring not yet assessed in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

