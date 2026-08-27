---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost: From Pulmonary Arterial Hypertension to HIV-Associated and Other PAH-Subtype Extensions

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (PGI2) analogue with an established vasodilatory/antiplatelet mechanism used to treat **Pulmonary Arterial Hypertension (PAH)**. This evidence pack evaluates **9 TxGNN-predicted indications** simultaneously; the strongest signal is **PAH associated with HIV infection**, supported by **1 completed Phase 3 RCT** and **4 publications**, while several other PAH-etiology subtypes (congenital heart disease, connective tissue disease) show moderate support and two dermatologic predictions (hypotrichosis, alopecia areata) have **no corroborating evidence whatsoever**.

> ⚠️ Note: This is a **multi-indication candidate pack** (`TW-DB01088-multi`). Rather than reporting a single prediction, this report ranks all 9 candidates by evidence strength so reviewers can triage which are worth pursuing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original / Established Indication | Pulmonary Arterial Hypertension (idiopathic/primary) — established use; **not derivable from Saudi Arabia licensing data**, as no local authorizations exist |
| Predicted New Indications Assessed | 9 (TxGNN model outputs) |
| Highest-Evidence New Indication | PAH associated with HIV infection |
| TxGNN Prediction Score (Highest-Evidence Indication) | 99.21% |
| Evidence Level (Highest-Evidence Indication) | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Overall Recommended Decision | **Mixed** — see per-indication table below |

### Predicted Indications Ranked by Evidence Strength

| Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---|---|---|---|---|
| PAH associated with HIV infection | 99.21% | L1 | S3 | Proceed with Guardrails |
| PAH associated with congenital heart disease | 99.32% | L2 | S2 | Proceed with Guardrails |
| PAH associated with connective tissue disease | 99.21% | L2 | S2 | Proceed with Guardrails |
| PAH associated with chronic hemolytic anemia | 99.21% | L4 | S1 | Research Question |
| PAH associated with schistosomiasis | 99.21% | L4 | S1 | Research Question |
| Pulmonary arteriovenous malformation (disease) | 99.31% | L4 | S0 | Hold |
| Hypotrichosis simplex of the scalp | 99.45% | L5 | S0 | Hold |
| Congenital hypotrichosis milia | 99.33% | L5 | S0 | Hold |
| Diffuse alopecia areata | 99.10% | L5 | S0 | Hold |

Note: TxGNN score alone (all ≥99%) is **not a reliable differentiator** here — every candidate scores similarly high, but actual clinical/mechanistic support ranges from a completed Phase 3 RCT down to zero literature or trial hits. Evidence level and recommendation, not raw score, should drive triage.

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack (flagged as Data Gap DG002, severity High). Based on known pharmacology, Iloprost belongs to the **prostacyclin (PGI2) analogue class**; its efficacy in treating Pulmonary Arterial Hypertension is well established through IP-receptor–mediated pulmonary vasodilation, antiplatelet activity, and anti-proliferative effects on pulmonary vascular smooth muscle.

**PAH-subtype extensions (HIV, congenital heart disease, connective tissue disease) are mechanistically sound.** All three belong to WHO Group 1 PAH — the same disease category already treated by Iloprost — differing only in etiology (viral endothelial injury, congenital shunt physiology, or autoimmune vasculopathy) rather than in the final common pathway of pulmonary vascular remodeling and vasoconstriction that Iloprost targets. This is best understood as **extending an existing approved drug class to specific etiological subgroups**, not as a novel indication hypothesis. The chronic hemolytic anemia and schistosomiasis-associated PAH predictions (WHO Group 5/mixed Group 4-5) are more speculative: the pathophysiology (hemolysis-driven endothelial dysfunction, granulomatous vascular obstruction) is only partially analogous to classic PAH, and no direct trial or literature evidence exists for these specific subgroups.

**The hypotrichosis, congenital hypotrichosis milia, and diffuse alopecia areata predictions are not mechanistically supported** and should be treated as likely model artifacts. Hair-loss conditions are driven by follicular/immune biology (autoimmune T-cell attack in alopecia areata; developmental/genetic defects in congenital hypotrichosis) that has no established connection to prostacyclin-receptor vasodilation. The evidence pack itself flags these as "推測性連結" (speculative association) with zero supporting trials or publications.

---

## Clinical Trial Evidence

| Predicted Indication | Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---------|------|------|------|---------|
| PAH – congenital heart disease | [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Evaluated safety, tolerability, and hemodynamic effects of Iloprost in adults with PAH related to congenital systemic-to-pulmonary shunts (Eisenmenger physiology); likely observational/prospective design rather than confirmatory RCT. |
| PAH – HIV infection | [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Multicenter, double-blind, randomized, placebo-controlled crossover study (PROWESS 15) of a single Iloprost dose on exercise capacity in symptomatic PAH patients, including idiopathic, familial, HIV-associated, and drug/toxin-induced PAH. Crossover design limits long-term outcome interpretation but provides solid acute efficacy/safety data. |

No registered clinical trials were found for: hypotrichosis simplex of the scalp, congenital hypotrichosis milia, pulmonary arteriovenous malformation, PAH associated with connective tissue disease, PAH associated with chronic hemolytic anemia, PAH associated with schistosomiasis, or diffuse alopecia areata.

---

## Literature Evidence

### PAH associated with congenital heart disease (top 10 of 20 identified)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Investigated endothelial dysfunction biomarkers (NO, ET-1, ADMA, Gal-3, BNP, UA) in CHD-PAH and the effect of Iloprost on their regulation. |
| [29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/) | 2018 | Cohort | Pediatric Cardiology | Evaluated acute safety and hemodynamic effects of inhaled Iloprost in children with PAH associated with simple CHD during catheterization. |
| [36010107](https://pubmed.ncbi.nlm.nih.gov/36010107/) | 2022 | Case Series | Children (Basel) | 5 Eisenmenger syndrome (CHD) patients treated long-term with combination sildenafil + bosentan + Iloprost; describes clinical course. |
| [25316472](https://pubmed.ncbi.nlm.nih.gov/25316472/) | 2014 | Case Report | Saudi Medical Journal | Unrepaired VSD with severe PAH showed dramatic clinical improvement (SpO2 60%→90%) after intensive inhaled Iloprost + sildenafil. |
| [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/) | 2015 | Cohort | Pediatric Pulmonology | Retrospective study of long-term inhaled Iloprost effects in children with pulmonary hypertension (including CHD etiology). |
| [19436672](https://pubmed.ncbi.nlm.nih.gov/19436672/) | 2009 | Review | Vasc Health Risk Manag | Reviews inhaled Iloprost use for pediatric PAH control, including CHD-associated cases. |
| [16919006](https://pubmed.ncbi.nlm.nih.gov/16919006/) | 2006 | Review | Eur J Clin Invest | Reviews treatment options in pediatric PAH, noting CHD as a leading etiology alongside idiopathic PAH. |
| [27053694](https://pubmed.ncbi.nlm.nih.gov/27053694/) | 2016 | Cohort/Consensus | Heart | Expert consensus on hemodynamic assessment and acute vasoreactivity testing in pediatric pulmonary vascular disease. |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Cohort | Prog Pediatr Cardiol | Discusses non-CHD-associated pediatric PAH, providing differential context for CHD-PAH management. |
| [30719004](https://pubmed.ncbi.nlm.nih.gov/30719004/) | 2018 | Cohort | Front Pharmacol | Cardiac MRI study showing acute inhaled Iloprost improves right ventricular function in PAH patients. |

### PAH associated with connective tissue disease (top 10 of 20 identified)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27651181](https://pubmed.ncbi.nlm.nih.gov/27651181/) | 2017 | Cohort | Respirology | Long-term outcomes of domiciliary IV Iloprost in idiopathic and CTD-associated PAH from a large UK referral center. |
| [21925064](https://pubmed.ncbi.nlm.nih.gov/21925064/) | 2011 | Cohort | Eur J Intern Med | Long-term effects of intermittent IV Iloprost infusion on pulmonary arterial pressure in CTD patients. |
| [26155616](https://pubmed.ncbi.nlm.nih.gov/26155616/) | 2015 | Cohort | Terapevticheskii Arkhiv | Evaluated efficacy of IV Iloprost in FC IV PAH associated with diffuse connective tissue disease. |
| [29718009](https://pubmed.ncbi.nlm.nih.gov/29718009/) | 2018 | Cohort | Rev Invest Clin | Characterized pulmonary vasoreactivity phenotypes in CTD-associated PAH. |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of PAH associated with connective tissue disease. |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Reviews PAH treatment in CTD, including prostanoid therapy. |
| [11936539](https://pubmed.ncbi.nlm.nih.gov/11936539/) | 2002 | Review | Eur Respir J | Reviews pulmonary hypertension in collagen vascular disease, noting prostacyclin therapy improves exercise capacity/hemodynamics. |
| [14583573](https://pubmed.ncbi.nlm.nih.gov/14583573/) | 2003 | Cohort/Registry | Ann Rheum Dis | Registry study of prevalence and outcome in systemic sclerosis-associated PAH. |
| [37728697](https://pubmed.ncbi.nlm.nih.gov/37728697/) | 2023 | Real-World Cohort | Adv Ther | US claims-based analysis of real-world treatment patterns in CTD-related PAH. |
| [19487219](https://pubmed.ncbi.nlm.nih.gov/19487219/) | 2009 | Review | Rheumatology (Oxford) | Reviews PAH as the most devastating vascular complication of systemic sclerosis. |

### PAH associated with HIV infection

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | Mt Sinai J Med | Reviews HIV-related pulmonary arterial hypertension, noting ~0.5% incidence in HIV-infected individuals and unclear pathogenesis. |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | Am J Respir Med | Reviews prostanoid therapy across PAH etiologies, explicitly including HIV-associated PAH. |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry/Cohort | Terapevticheskii Arkhiv | Six-year National Registry analysis of PAH prevalence, clinical course, and therapy (multi-etiology, includes HIV). |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Reviews controlled trials of prostacyclin/analogues across PAH etiologies including HIV infection. |

### Other predicted indications

- **Pulmonary arteriovenous malformation (disease):** 1 tangential publication ([PMID 15929019](https://pubmed.ncbi.nlm.nih.gov/15929019/), 2005, case report on pulmonary hypertension in hereditary hemorrhagic telangiectasia) — addresses secondary hypertension, not the structural malformation itself.
- **PAH associated with chronic hemolytic anemia:** Currently no related literature available.
- **PAH associated with schistosomiasis:** 1 tangentially related publication ([PMID 24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/)) on pediatric inhaled Iloprost in general PH, not schistosomiasis-specific.
- **Hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata:** Currently no related literature available.

---

## Saudi Arabia Market Information

Iloprost currently has **no marketing authorization in Saudi Arabia** (market status: 未上市 / Not Marketed; total authorizations: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ Critical data gap: TFDA/SFDA package insert warnings and contraindications for Iloprost could not be retrieved (Data Gap DG001, severity **Blocking**). This directly prevents this candidate from entering the S1 safety pre-assessment stage for **any** of the predicted indications above, regardless of clinical/mechanistic evidence strength.

---

## Conclusion and Next Steps

**Decision: Mixed — Proceed with Guardrails (PAH-subtype indications) / Research Question (hemolytic anemia, schistosomiasis) / Hold (AVM, hypotrichosis, alopecia)**

**Rationale:**
- **PAH associated with HIV infection** has the strongest support (completed Phase 3 RCT, consistent mechanism with an already-approved drug class) and can proceed with guardrails around the crossover trial design and small sample size (n=64).
- **PAH associated with congenital heart disease** and **PAH associated with connective tissue disease** are supported by consistent cohort/registry evidence and a shared, well-understood mechanism (WHO Group 1 PAH), justifying guarded progression.
- **Chronic hemolytic anemia– and schistosomiasis-associated PAH** have plausible but unproven mechanistic rationale and no direct evidence — these remain open research questions, not repurposing candidates ready for action.
- **Pulmonary arteriovenous malformation, hypotrichosis simplex, congenital hypotrichosis milia, and diffuse alopecia areata** lack mechanistic plausibility, clinical trials, or literature support and should be held pending stronger justification or dismissed as low-value model outputs.
- **No indication can advance past S1** until the blocking safety data gap (TFDA/SFDA package insert) is resolved.

**To proceed, the following is needed:**
- Retrieve and parse the Iloprost package insert (warnings, contraindications, DDI) from TFDA/SFDA — this is a **blocking** prerequisite for all candidates (DG001).
- Obtain confirmed DrugBank mechanism-of-action data to strengthen the mechanistic case for PAH-subtype extensions (DG002).
- For HIV-PAH: seek additional confirmatory (non-crossover) trial data or real-world outcomes data given the small sample size.
- For chronic hemolytic anemia– and schistosomiasis-associated PAH: commission a targeted literature/trial search before any further evaluation; current absence of evidence may simply reflect these being under-studied rather than truly ineffective.
- For the three hair/scalp-condition predictions: no further investment recommended without a specific, independently derived mechanistic hypothesis, given the complete absence of supporting data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

