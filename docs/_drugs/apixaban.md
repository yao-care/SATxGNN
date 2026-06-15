---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 1
---

# Apixaban
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

# Apixaban: From Thromboembolic Prevention to Migraine Disorder

## One-Sentence Summary

Apixaban is an oral Factor Xa inhibitor widely used for stroke prevention in atrial fibrillation and treatment of venous thromboembolism.
The TxGNN model predicts it may have efficacy in **migraine disorder**,
though current evidence — comprising **1 indirectly related clinical trial** and **4 case-level publications** — is preliminary and internally conflicting.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Stroke prevention (non-valvular atrial fibrillation); VTE treatment and prophylaxis |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Apixaban is a selective, reversible inhibitor of coagulation Factor Xa — a pivotal enzyme in the common coagulation pathway. It is approved globally for stroke prevention in non-valvular atrial fibrillation, treatment of deep vein thrombosis (DVT) and pulmonary embolism (PE), and VTE prophylaxis after joint replacement surgery.

The mechanistic hypothesis linking Apixaban to migraine originates from the **thromboembolism theory of migraine with aura**: patent foramen ovale (PFO), a small septal opening between the cardiac atria, is significantly more prevalent among migraine-with-aura patients than in the general population. The theory proposes that microthrombi bypass pulmonary filtration via the PFO, enter cerebral circulation, and trigger cortical spreading depression (CSD) — the electrophysiological phenomenon underlying aura. Anticoagulation could theoretically block this pathway.

However, existing case reports reveal a critical mechanistic gap: warfarin (a vitamin K antagonist that broadly inhibits Factors II, VII, IX, and X, including thrombin generation) is associated with migraine resolution in several reported cases, whereas Apixaban (a selective Factor Xa inhibitor) did not replicate this benefit — and in at least one documented case actively worsened migraine. This divergence raises the possibility that **thrombin itself** plays a direct, independent neuromodulatory role in migraine pathophysiology — one that selective Factor Xa inhibition cannot address. This mechanistic hypothesis remains speculative and lacks direct pharmacological validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared PFO percutaneous closure, oral anticoagulation, and antiplatelet therapy for prevention of stroke recurrence. Primary endpoint was stroke, not migraine. Apixaban was not explicitly designated as the anticoagulant agent. Provides only indirect contextual relevance to migraine through the established PFO–migraine epidemiological association. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Pilot Clinical Trial | Lupus | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies (aPL). A subset showed symptomatic improvement on antithrombotic therapy, supporting a thrombotic mechanism in aPL-positive migraine. Apixaban-specific outcomes were not isolated. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | The Neurologist | Reports a case of migraine with aura that **worsened** after initiating Apixaban. Accompanying literature review concludes that the impact of direct oral anticoagulants (DOACs) on migraine is unclear, and current evidence is scarce and conflicting. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | Headache | A 55-year-old woman experienced complete migraine-with-aura remission for 12 years on warfarin; symptoms returned within 3 weeks of switching to Apixaban and resolved again upon warfarin resumption. Suggests warfarin's broader mechanism — including upstream thrombin suppression — may be the critical pharmacological difference. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | Headache | Vestibular migraine resolved on combined warfarin and topiramate therapy. Provides contextual support for anticoagulation in migraine but does not involve Apixaban. |

---

## Taiwan Market Information

Apixaban currently holds **no marketing authorizations in Taiwan** and is not commercially available through regulated channels.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Available evidence for Apixaban in migraine disorder is limited to L4 — case reports and one retrospective pilot study with no dedicated prospective trials. Most critically, the case reports most directly relevant to Apixaban specifically report **neutral or negative outcomes**, in contrast to positive results seen with warfarin, making the benefit hypothesis for this drug class uncertain at best.

**To proceed, the following is needed:**
- Prospective controlled studies specifically evaluating Apixaban or other Factor Xa inhibitors in migraine-with-aura patients with confirmed PFO
- Mechanistic investigation of thrombin's direct role in cortical spreading depression, to determine whether Factor Xa inhibition alone is a pharmacologically sufficient target
- Complete safety dataset: package insert warnings, contraindications, and drug–drug interaction profile before any clinical consideration
- MOA data from DrugBank to support mechanistic plausibility analysis
- Clarification of whether the repurposing rationale applies to a PFO-positive migraine subpopulation specifically, rather than migraine disorder broadly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

