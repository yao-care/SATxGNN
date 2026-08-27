---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine: From Vertigo to Migraine Disorder

## One-Sentence Summary

Flunarizine is a calcium channel blocker traditionally used for vertigo and vestibular disorders. The TxGNN model predicts it may be effective for **Migraine Disorder** (specifically migraine prophylaxis), a use already supported by an extensive body of real-world evidence — **19 clinical trials** and **20 publications** are currently on record for this drug-disease pair, including multiple head-to-head Phase 4 RCTs and a dedicated systematic review/meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vertigo (traditional use per literature; no formal license record found in this market) |
| Predicted New Indication | Migraine Disorder (prophylaxis) |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed original mechanism-of-action data from DrugBank is not available for this drug (Data Gap DG002). However, evidence from the clinical trial and literature records in this pack consistently describes flunarizine as a non-selective calcium channel antagonist (T-type/L-type) with additional antihistaminic and weak dopamine-antagonist activity. It acts on cerebral vascular smooth muscle and cortical neurons to inhibit vasospasm and cortical spreading depression — a mechanism that is already a standard pharmacological explanation for migraine prophylaxis, not a speculative link.

Flunarizine's traditional indication, vertigo/vestibular disorder, and the predicted new indication, migraine prophylaxis, share a common vascular and neuronal excitability pathophysiology. Both conditions involve dysregulation of cerebral blood flow and neuronal hyperexcitability, which calcium channel blockade can modulate.

This mechanistic overlap is reflected in decades of clinical use: flunarizine is already an established first- or second-line migraine prophylactic agent in many jurisdictions (Sibelium), with head-to-head trials against topiramate, propranolol, and amitriptyline. In this market, however, the drug is not currently registered or marketed, so the "new indication" signal here is best read as a market-entry / label-expansion opportunity rather than a mechanistically novel discovery — the EHF (European Headache Federation) 2023 critical re-appraisal (PMID 37723437) explicitly frames flunarizine as a "repurposed, first- or second-line treatment for migraine prophylaxis," reinforcing that this is a well-characterized rather than speculative association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Head-to-head comparison of flunarizine 10mg/day vs. topiramate 50mg/day for chronic migraine prophylaxis |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Three-arm comparison of greater occipital nerve block, topiramate, and flunarizine for episodic migraine |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Flunarizine vs. amitriptyline for migraine prophylaxis (Lahore, Pakistan); follow-up status uncertain |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Flunarizine vs. propranolol in pediatric migraine (ages 8-15), assessed via PedMIDAS score |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not Yet Recruiting | 460 | Pragmatic multicentre RCT comparing amitriptyline, flunarizine, topiramate, and propranolol as first-line migraine prophylaxis in primary care |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Pharmacokinetic drug interaction study of flunarizine and topiramate during mono- and concomitant therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Systematic Review / Meta-analysis | The Journal of Headache and Pain | European Headache Federation critical re-appraisal and meta-analysis of flunarizine for migraine prevention |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic Review / Meta-analysis | J Assoc Physicians India | Comparative efficacy and safety of amitriptyline vs. propranolol and flunarizine for migraine prophylaxis |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | Preventive medications (including flunarizine) compared across pediatric migraine trials |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic Review | Health Technology Assessment | Comparative clinical and cost-effectiveness of preventive drugs for chronic migraine |
| [40614441](https://pubmed.ncbi.nlm.nih.gov/40614441/) | 2025 | Clinical Study | Brain & Development | Topiramate vs. flunarizine compared on pain control and school/social performance in pediatric migraine |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurologica Scandinavica | Flunarizine plus transcutaneous supraorbital neurostimulation improves migraine prophylaxis vs. either alone |
| [35791513](https://pubmed.ncbi.nlm.nih.gov/35791513/) | 2022 | Clinical Study | Brain and Behavior | Flunarizine combined with duloxetine for chronic migraine comorbid with depression/anxiety |
| [33722518](https://pubmed.ncbi.nlm.nih.gov/33722518/) | 2022 | Controlled Study | Braz J Otorhinolaryngol | Propranolol, flunarizine, amitriptyline, and botulinum toxin compared for vestibular migraine |
| [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/) | 1997 | Observational Study | Pharmacy World & Science | Postmarketing study (n=686) of flunarizine vs. propranolol in migraine, and vs. betahistine in vertigo |
| [1889980](https://pubmed.ncbi.nlm.nih.gov/1889980/) | 1991 | Review | Headache | Mechanistic minireview establishing flunarizine's efficacy in migraine prophylaxis across controlled trials |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA warnings, contraindications, and drug-drug interaction data are not currently available for this drug in this evidence pack (Data Gap DG001, blocking).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence for flunarizine in migraine prophylaxis is strong (L1) — including multiple completed Phase 4 head-to-head RCTs against topiramate, propranolol, and amitriptyline, plus a dedicated EHF systematic review/meta-analysis. However, the drug is currently unregistered and unmarketed in this jurisdiction, and safety data (warnings, contraindications, DDI) has a blocking gap that must close before any S1 safety review can proceed.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, blocking) — required before S1 safety screening
- DrugBank-sourced mechanism of action confirmation (DG002)
- Formal regulatory pathway assessment given the drug's current "not marketed" status in this jurisdiction
- Drug-drug interaction data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

