---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet Therapy to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a well-established antiplatelet and vasodilatory agent, most recognized globally for its combined use with aspirin (Aggrenox) in secondary stroke prevention, though it currently holds no regulatory approval in Saudi Arabia.
The TxGNN model's top-ranked prediction places it as a candidate for **Prinzmetal Angina (variant angina)** with a score of 99.99% — however, published evidence reveals a **critical safety concern**: dipyridamole functions as a vasospasm *provocateur* rather than a therapeutic agent in this condition, with **0 clinical trials** and **15 publications**, nearly all in a diagnostic rather than therapeutic context.
Stronger repurposing signals with L1 evidence exist for **Stroke Disorder** (Rank 2) and **Transient Ischemic Attack** (Rank 5), both supported by multiple completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Saudi Arabia regulatory approval on record; dipyridamole is an established antiplatelet agent used in combination therapy for stroke prevention |
| Predicted New Indication | Prinzmetal Angina (Variant Angina) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (Mechanistic studies and diagnostic literature; no therapeutic RCTs) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | ⚠️ Hold (Potential Contraindication) |

---

## Why is This Prediction Reasonable?

Dipyridamole inhibits phosphodiesterase (PDE), preventing the breakdown of cyclic AMP (cAMP) and cyclic GMP (cGMP) within platelets, and simultaneously blocks adenosine reuptake — raising extracellular adenosine concentrations at the vascular level. Together, these mechanisms inhibit platelet aggregation and induce coronary and peripheral vasodilation. These properties underlie its established role as an antiplatelet agent (most notably combined with aspirin as Aggrenox, FDA-approved for secondary stroke prevention) and as a pharmacological stress agent in myocardial perfusion scintigraphy.

Prinzmetal (variant) angina is characterized by episodic, rest-associated chest pain caused by coronary arterial vasospasm rather than fixed atherosclerotic obstruction. At first glance, dipyridamole's vasodilatory mechanism might seem relevant. However, the clinical evidence points in the opposite direction: dipyridamole-induced adenosine potentiation creates a **coronary steal phenomenon**, and abrupt reversal of vasodilation — for example by aminophylline administration — can trigger intense rebound vasospasm. PMID 3421166 explicitly documents this mechanism, recording that dipyridamole stress testing provokes acute vasospastic episodes in variant angina patients. Accordingly, the **dipyridamole stress test is used as a diagnostic tool to provoke and confirm vasospastic attacks** — not as a treatment.

Standard therapy for Prinzmetal angina consists of calcium channel blockers (diltiazem, amlodipine) and long-acting nitrates. The TxGNN model's high prediction score most likely reflects adenosine/vascular network proximity within the pharmacological knowledge graph, rather than true therapeutic potential. **This prediction should be interpreted as a safety signal, not a repurposing opportunity.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dipyridamole in Prinzmetal angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Clinical Observation (Safety Alert) | American Journal of Cardiology | Dipyridamole stress testing triggers coronary vasospasm in variant angina patients via aminophylline-induced rebound after vasodilation withdrawal — **critical safety warning against therapeutic use** |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Diagnostic Study | British Heart Journal | Short-term reproducibility of exercise testing in 25 patients with exercise-induced ST-segment elevation; dipyridamole echocardiography used as a vasospasm provocateur, not a treatment |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Echocardiographic Study | J Am Coll Cardiology | Increased myocardial echodensity during dipyridamole-induced ischemic episodes — documents dipyridamole as an ischemia trigger across different pathogenetic mechanisms |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Prognostic Cohort | Rev Port Cardiologia | 3-year prognosis assessment in patients with suspected CAD and normal dipyridamole-thallium scintigraphy — diagnostic application only |
| [3915223](https://pubmed.ncbi.nlm.nih.gov/3915223/) | 1985 | Pharmacological Provocation Study | Cardiologia (Rome) | Cardiovascular effects of provocation tests; dipyridamole used as a stress challenge agent to evaluate coronary function |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic Imaging Study | Japanese Circulation Journal | Dipyridamole-loading myocardial imaging for CAD diagnosis; sensitivity 66% alone, rising to 87% combined with exercise — confirms diagnostic rather than therapeutic role |
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Japanese Circulation Journal | 26 patients with angina at rest (including 13 Prinzmetal's) given propranolol, diltiazem, dipyridamole, atropine, phenoxybenzamine; propranolol tended to aggravate attacks; dipyridamole not identified as effective treatment |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological basis for noninvasive functional evaluation of coronary stenosis; discusses dipyridamole as a stress test modality alongside exercise and dobutamine |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Clinical Descriptive Study | Zhonghua Xin Xue Guan Bing Za Zhi | Comparison of clinical characteristics of typical vs. atypical coronary artery spasm; highlights heterogeneity of vasospastic disease |
| [6125623](https://pubmed.ncbi.nlm.nih.gov/6125623/) | 1982 | Review | Kardiologiia | Review of diagnostic and treatment challenges in stenocardia; dipyridamole discussed in a diagnostic context |

---

## Saudi Arabia Market Information

Dipyridamole currently holds **no regulatory authorizations in Saudi Arabia**. The drug is not marketed in Saudi Arabia, with zero product licenses on record. No authorization table can be generated.

Note: The Aggrenox formulation (dipyridamole 200 mg extended-release + aspirin 25 mg) is FDA-approved for secondary stroke prevention and is marketed in multiple jurisdictions — this combination represents a potential future registration candidate for Saudi Arabia.

---

## Safety Considerations

**Key Safety Signal (from clinical literature):**
Dipyridamole potentiates endogenous adenosine, which can precipitate coronary vasospasm, significant hypotension, bradycardia, and bronchospasm. PMID 3421166 specifically documents dipyridamole-induced coronary vasospasm in variant angina patients — establishing Prinzmetal angina as a **contraindication context, not a treatment indication**.

Additionally, the Rank 4 prediction (Sick Sinus Syndrome 2, autosomal dominant) highlights another potential contraindication class: dipyridamole-mediated adenosine elevation may aggravate sinoatrial conduction impairment in patients with sick sinus syndrome.

Please refer to the full package insert for comprehensive safety information including warnings, contraindications, and drug interactions (formal package insert data was not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision for Primary Prediction (Prinzmetal Angina): ⚠️ Hold**

**Rationale:**
Published clinical literature consistently demonstrates that dipyridamole *provokes* rather than treats coronary vasospasm in Prinzmetal angina. Therapeutic use in this population risks precipitating acute ischemic events. The high TxGNN score reflects adenosine/vascular pharmacological network proximity — not clinical therapeutic potential.

---

**Full Prediction Landscape — All 10 Indications:**

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|----------------|---------|
| 1 | Prinzmetal Angina | 99.99% | L4 | ⚠️ Hold (Safety Concern — Contraindicated) |
| 2 | Stroke Disorder | 99.95% | L1 | **Proceed with Guardrails** |
| 3 | Thrombotic Disease | 99.94% | L3 | Research Question |
| 4 | Sick Sinus Syndrome 2 (AD) | 99.89% | L5 | ⚠️ Hold (Potential Contraindication) |
| 5 | Transient Ischemic Attack | 99.87% | L1 | **Proceed with Guardrails** |
| 6 | Sarcoglycanopathy | 99.82% | L5 | Hold |
| 7 | Wildervanck Syndrome | 99.78% | L5 | Hold |
| 8 | Macrocephaly / Dysmorphic Facies / Psychomotor Retardation | 99.77% | L5 | Hold |
| 9 | Cavernous Sinus Thrombosis | 99.72% | L5 | Hold |
| 10 | Lateral Sinus Thrombosis | 99.72% | L5 | Hold |

**The most clinically meaningful repurposing opportunities are Ranks 2 and 5:**

- **Stroke Disorder (Rank 2, L1):** Supported by multiple large completed Phase 3/4 RCTs — JASAP (n=1,295), PRoFESS (n=20,332), ESPRIT (n=4,500), EARLY (n=551) — plus Cochrane systematic reviews and individual-patient-data meta-analyses. Dipyridamole + aspirin (Aggrenox) is FDA-approved for secondary stroke prevention. Saudi Arabia regulatory submission is a viable pathway.
- **Transient Ischemic Attack (Rank 5, L1):** Shares the same evidence base as stroke disorder; TIA patients are co-enrolled in most pivotal trials. ESPS-2 confirmed dipyridamole + aspirin significantly reduces post-TIA stroke recurrence.

**To proceed (Stroke / TIA — the actionable indications):**
- Resolve data gaps: obtain MOA entry from DrugBank API and download package insert for Saudi Arabia safety screening
- Assess regulatory pathway for Aggrenox or generic dipyridamole SR registration with SFDA
- Confirm contraindication status in target populations with sick sinus syndrome, asthma, or hemodynamic instability
- Engage Saudi neurology / stroke medicine key opinion leaders for local clinical adoption feasibility
- Develop pharmacovigilance and monitoring plan for post-registration safety (headache, hypotension, bronchospasm are known class effects)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

