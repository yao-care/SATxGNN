---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

> **Note on TxGNN top prediction:** The highest-ranked prediction (rank 1, "obsolete bundle branch block", score 99.94%) carries an "obsolete" prefix indicating a retired Disease Ontology term with no current clinical mapping and zero supporting evidence. It is excluded from this report. The analysis below focuses on **rank 2 — Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)** — the highest-ranked clinically valid target.

---

## One-Sentence Summary

Adenosine is an endogenous purine nucleoside established globally as a first-line agent for terminating supraventricular tachycardia (SVT) via transient AV nodal blockade; it has no current Saudi Arabia market authorisation.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**,
with **1 active Phase 2a clinical trial** and **13 relevant publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Supraventricular tachycardia (SVT) — established global clinical use; no Saudi Arabia regulatory data on record |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Adenosine acts primarily through the A1 adenosine receptor, which is coupled to inhibitory Gi-proteins. Activation of A1 receptors suppresses adenylyl cyclase, thereby reducing intracellular cyclic AMP (cAMP) levels. Lower cAMP attenuates PKA-mediated phosphorylation of the cardiac ryanodine receptor (RyR2) at Ser2808 and Ser2814 — the precise molecular switch that catecholamines exploit to trigger abnormal calcium release from the sarcoplasmic reticulum.

CPVT is caused by gain-of-function mutations in RyR2 or CASQ2 that render the calcium release channel hypersensitive to catecholamine-driven PKA phosphorylation. During physical or emotional stress, excessive β-adrenergic stimulation amplifies cAMP, producing uncontrolled SR calcium leakage and life-threatening ventricular arrhythmias. Because adenosine directly opposes this cascade upstream of RyR2, the mechanistic rationale for repurposing is strong and biologically specific to the CPVT disease mechanism — not merely coincidental cardiac overlap.

This theoretical link is reinforced by converging clinical and translational data. A published case report (PMID 18313614) demonstrated that intravenous ATP — the immediate metabolic precursor of adenosine — successfully terminated bidirectional ventricular tachycardia in a CPVT patient, providing direct human proof-of-concept for the adenosine signalling pathway in this arrhythmia. Furthermore, an ongoing Phase 2a clinical trial (NCT07263139) is currently recruiting CPVT patients to evaluate AGP100, an adenosine receptor agonist, specifically for this indication — confirming that the adenosine axis is actively recognised as a therapeutic target by independent investigators.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | Evaluating AGP100 (adenosine receptor agonist) for safety, tolerability, and exploratory efficacy in CPVT patients. Trial start: January 2026; expected completion: June 2027. CPVT causes dangerous tachycardia under physical/emotional stress and current treatments do not always prevent arrhythmias during strenuous exercise. No results available yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | Heart Rhythm | ATP (adenosine's direct precursor) terminated bidirectional ventricular tachycardia in a confirmed CPVT patient — the most direct clinical evidence linking the adenosine purinergic pathway to arrhythmia suppression in CPVT |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review | Europace | ESC/HRS/APHRS/LAHRS multi-society consensus on pharmacological provocation testing in cardiac electrophysiology; covers adenosine's diagnostic role in arrhythmia evaluation |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical Study | Heart Rhythm | Postpacing abnormal repolarization characterised in CPVT patients with RyR2 mutations; clarifies electrophysiological phenotype directly relevant to adenosine-based intervention |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Mechanistic | BBA | ATP directly binds the central domain of RyR2 at sites associated with CPVT mutations; mechanistically links adenosine/ATP purine signalling to the core structural pathology of CPVT |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical | Cardiovascular Research | PDE2A/PDE4B gene therapy reduces cardiomyocyte cAMP compartmentation and prevents heart failure and arrhythmias in mice; reinforces cAMP→PKA→RyR2 as the shared mechanistic axis targeted by adenosine |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In vitro | Journal of Physiology | Human cardiac-neural microtissues reveal CPVT is also a disease of the sympathetic neuron; opens a neuromodulatory rationale for A1 receptor agonism beyond cardiomyocyte-only targeting |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Clinical Review | Paediatric Anaesthesia | Paediatric arrhythmia management including CPVT channelopathies; discusses adenosine use in SVT differential diagnosis and arrhythmia risk under anaesthesia |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclinical | Communications Biology | TECRL knockout in cardiomyocytes (a CPVT-linked gene) causes mitochondrial dysfunction and aggravated cardiac arrhythmia; contextualises multi-pathway vulnerability in CPVT beyond RyR2 alone |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | JAPI | Classification and management of idiopathic ventricular tachycardia; adenosine sensitivity is an established diagnostic criterion for outflow tract VT, highlighting its broader antiarrhythmic utility |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical | Science Translational Medicine | Selective RyR2 stabilisation normalises SR Ca²⁺ leak and improves survival in pressure-overload and MI mouse models; reinforces RyR2 calcium leak suppression — the mechanism shared with adenosine A1 signalling — as a valid arrhythmia target |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The adenosine A1 receptor → cAMP↓ → PKA↓ → RyR2 phosphorylation↓ cascade directly addresses the core pathophysiology of CPVT at a mechanistic level, with human case-report proof-of-concept (ATP terminating CPVT bidirectional VT) and an active Phase 2a trial of an adenosine receptor agonist specifically in CPVT patients providing sufficient grounds to advance — but the very short IV half-life of native adenosine (~10 seconds) and absent Saudi Arabia regulatory status require a structured development plan before clinical commitment.

**To proceed, the following is needed:**
- Await results from NCT07263139 (AGP100 Phase 2a trial; expected June 2027) to establish whether A1 agonism is clinically effective and tolerable in CPVT
- Clarify whether the development candidate is native adenosine IV (acute termination) or a longer-acting A1 agonist such as AGP100 (chronic prevention) — these represent distinct clinical strategies with different regulatory pathways
- Obtain complete safety data including key warnings, contraindications, and drug interaction profile (currently absent from the Evidence Pack)
- Conduct dose-ranging studies specific to CPVT arrhythmia suppression during standardised exercise stress testing
- Establish a pharmacokinetic/pharmacodynamic rationale for practical dosing given adenosine's extremely short plasma half-life
- Submit Saudi Arabia market authorisation application if proceeding with a locally approved formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

