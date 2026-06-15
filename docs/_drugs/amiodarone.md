---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a Class III antiarrhythmic agent with broad multichannel-blocking properties, widely used in clinical practice for the management of life-threatening ventricular and supraventricular arrhythmias.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**,
with **0 clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ventricular arrhythmias (Class III antiarrhythmic; no Saudi Arabia registration on file) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (Mechanistic rationale only; no clinical trials identified) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiodarone is a broad-spectrum antiarrhythmic agent with properties spanning multiple Vaughan-Williams classes: it blocks voltage-gated sodium channels (Nav), potassium channels (Kv), and calcium channels (Cav), and exerts non-competitive beta-adrenergic receptor (β-AR) blockade. Detailed DrugBank MOA data was not available for this evaluation, but the drug's electrophysiological profile is well documented in the clinical literature and is central to understanding its potential in CPVT.

CPVT is a rare inherited channelopathy caused by mutations in the RYR2 (ryanodine receptor type 2) or CASQ2 (calsequestrin-2) genes. These mutations cause spontaneous calcium release from the sarcoplasmic reticulum during adrenergic stimulation, producing delayed afterdepolarizations (DADs) that trigger ventricular tachycardia. Amiodarone's β-AR blockade can attenuate catecholamine-driven calcium dysregulation, while its Nav and Kv channel-blocking effects may suppress the resulting triggered activity. However, amiodarone does not directly stabilize the RYR2 channel — the primary pathological mechanism — making its mechanistic fit less optimal than flecainide, which has a direct RYR2-blocking effect.

The TxGNN prediction likely reflects amiodarone's broad antiarrhythmic efficacy across ventricular arrhythmia subtypes. Available evidence consists entirely of case reports, case series, and general arrhythmia reviews; no studies are specifically designed to evaluate amiodarone in CPVT. Its clinical role in CPVT is best understood as a bridging or add-on therapy in refractory cases where first-line agents (beta-blockers, flecainide) have failed, or in acute hemodynamic crises where parenteral antiarrhythmic control is urgently needed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for amiodarone in catecholaminergic polymorphic ventricular tachycardia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Comprehensive review of pharmacologic treatment of ventricular arrhythmias; contextualizes amiodarone among antiarrhythmic options |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Cohort/Registry | Life (Basel) | Systematic review of CPVT clinical characteristics, genetic findings (RYR2/CASQ2), and arrhythmic outcomes in Chinese patients |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective Cohort | Rev Cardiovasc Med | CPVT clinical characteristics, genetic basis, and healthcare resource utilization in a retrospective Chinese cohort |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | PACE | Flecainide — not amiodarone — suppressed ICD-induced arrhythmic storm in a CPVT patient with CASQ2 mutation; highlights the comparative limitations of amiodarone |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Reports | Child with cardiac arrest due to CPVT; refractory pulseless VT required 40 defibrillation shocks; multimodal antiarrhythmic therapy including amiodarone was administered |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | CPVT in a teenager finally resolved by right cardiac sympathetic denervation after failure of pharmacotherapy including amiodarone |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old; illustrates the diagnostic challenge and acute management needs |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Delayed CPVT diagnosis (6 years) in a child with RYR2 c.7580T>G mutation; underlines the importance of early genetic testing |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Esp Cardiol | Arrhythmic storm triggered by ICD discharge in a CPVT patient; amiodarone mentioned in the acute management context |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesth Analg | Neonate with long QT syndrome and refractory ventricular tachycardia; amiodarone was used as part of multimodal pharmacotherapy alongside lidocaine and esmolol |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for amiodarone in CPVT is limited to indirect case reports and general arrhythmia reviews, with no dedicated clinical trials. While a plausible mechanistic pathway exists via β-AR blockade, amiodarone does not address the primary RYR2/CASQ2 pathophysiology and is mechanistically inferior to established CPVT therapies such as beta-blockers and flecainide.

**To proceed, the following is needed:**
- Prospective observational studies or registries specifically evaluating amiodarone as adjunctive therapy in refractory CPVT
- Complete DrugBank MOA data to formally assess target engagement relevant to RYR2/CASQ2 signaling pathways
- Pediatric safety data for chronic amiodarone use, as CPVT predominantly presents in children and young adults
- Saudi Arabia regulatory pathway assessment, given zero market authorizations and the absence of any local safety or pharmacovigilance data
- Comparative efficacy data positioning amiodarone relative to flecainide and nadolol/propranolol in the CPVT treatment algorithm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

