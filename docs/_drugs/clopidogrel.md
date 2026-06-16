---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: From Atherothrombotic Disease Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a P2Y12 ADP receptor antagonist antiplatelet drug, widely used globally for preventing thrombotic events in patients with acute coronary syndrome, ischemic stroke, and peripheral artery disease.
The TxGNN model ranks **Migraine with Brainstem Aura** as its top predicted new indication (score 99.44%), with the closely related **Migraine Disorder** indication supported by **8 clinical trials** and **20 publications**.
While no clinical trials have specifically enrolled migraine with brainstem aura patients, indirect evidence from observational studies, pilot RCTs, one completed Phase 4 trial (CANOA, n=220), and a 2025 systematic review provides a mechanistically coherent rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atherothrombotic event prevention (ACS, ischemic stroke, PAD) — global approved use; no Saudi Arabia authorization on record |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrievable in this evidence pack. Based on well-established published pharmacology, clopidogrel is a thienopyridine prodrug that, after hepatic bioactivation via CYP2C19, irreversibly blocks the P2Y12 ADP receptor on platelet surfaces. This inhibits ADP-dependent platelet aggregation, reduces platelet-derived release of serotonin (5-HT) and thromboxane A2 (TXA2), and suppresses pro-thrombotic platelet activity. These effects are the basis of its approved cardiovascular and cerebrovascular indications.

The mechanistic bridge to migraine with brainstem aura centers on the **patent foramen ovale (PFO) / right-to-left shunt (RLS) hypothesis**. A PFO allows venous microemboli and vasoactive substances — including platelet-derived 5-HT and TXA2 — to bypass the pulmonary filter and enter the cerebral arterial circulation. Once in the brain, these mediators can trigger cortical spreading depression (CSD), the neurophysiological substrate of migraine aura. By inhibiting platelet activation, clopidogrel may simultaneously reduce paradoxical microembolism and curtail release of the vasoactive triggers that initiate CSD, thereby preventing migraine attacks. Preclinical data further show that P2Y12 receptors are expressed on microglia in the trigeminal nucleus caudalis, and P2Y12-mediated microglial activation via the RhoA/ROCK pathway contributes to chronic migraine sensitization (PMID 31722730), suggesting a central nervous system target beyond the platelet.

Migraine with brainstem aura is the subtype with the strongest epidemiological association with PFO and RLS, making the embolic-platelet hypothesis particularly compelling for this specific phenotype. However, a dedicated RCT for the brainstem aura subtype does not yet exist; all current clinical evidence is extrapolated from broader migraine with aura cohorts and post-cardiac-procedure settings. The TxGNN prediction leverages graph-level proximity between platelet biology, PFO pathophysiology, and the brainstem aura disease node — which is mechanistically defensible but clinically unconfirmed.

---

## Clinical Trial Evidence

No clinical trials specifically targeting **migraine with brainstem aura** with clopidogrel are currently registered. The following trials, retrieved for the closely related **Migraine Disorder** indication (TxGNN Rank #2, 99.43%), provide the most proximate indirect evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA trial: Clopidogrel + aspirin vs aspirin alone to prevent new-onset migraine following transcatheter ASD closure; primary analysis (JAMA 2015) and 12-month follow-up (JAMA Cardiology 2021) both published |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | COMPETE trial: Three-arm RCT comparing anticoagulation vs antiplatelet therapy (including clopidogrel) vs migraine-specific medication in PFO patients; largest ongoing study in this field |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING trial: PFO closure vs medication (including antiplatelet) for migraine relief; multicenter RCT, completion expected September 2025 |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial evaluating clopidogrel prophylaxis specifically for migraineurs with confirmed right-to-left shunt |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelet (clopidogrel arm included) for stroke recurrence; migraine episodes captured as secondary outcome |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | High-risk PFO percutaneous closure for migraine: multicenter RCT; clopidogrel used as post-procedure adjunct therapy |

---

## Literature Evidence

Publications retrieved for **Migraine with Brainstem Aura** (predicted_indications[0]), prioritized by study tier and direct relevance to clopidogrel in migraine:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | *Headache* | Comprehensive review of antithrombotic drugs (including clopidogrel) as migraine preventive medication; most current synthesis of the evidence base |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | *European Heart Journal* | PRIMA trial: Multicenter RCT of percutaneous PFO closure in migraine with aura refractory to medical treatment; establishes PFO–migraine with aura link in a controlled design |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | *Cephalalgia* | First pilot randomized controlled trial of clopidogrel as prophylactic treatment for migraine; anecdotal observations prompted this controlled assessment |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | *J Investigative Medicine* | Clopidogrel 75 mg/day added to existing regimen over 3–6 months reduced attack frequency in drug-refractory migraineurs with PFO; 56.8% PFO prevalence confirmed in cohort |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Prospective Observational | *Heart* | Seminal report: clopidogrel reduced migraine with aura after transcatheter PFO/ASD closure, triggering regimen changes in clinical practice |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Cohort | *Neurology* | Real-world clinical experience of thienopyridines (clopidogrel and prasugrel) in migraineurs with PFO; supports class-level antiplatelet effect on migraine |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Cohort | *Cephalalgia* | Clopidogrel as primary (not post-procedure) therapy for migraineurs with right-to-left shunt lesions; proposes platelet activation–paradoxical embolization–migraine mechanism |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | *Neurology* | TRACTOR study: Ticagrelor (non-thienopyridine P2Y12 inhibitor) tested in refractory migraine/PFO, showing similar effects; supports P2Y12 class-level mechanism rather than thienopyridine-specific effect |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Observational | *Cephalalgia* | De novo migraine after ASD closure ameliorated by antiplatelet therapy; clopidogrel specifically cited as migraine-modifying agent in post-procedure setting |
| [33815258](https://pubmed.ncbi.nlm.nih.gov/33815258/) | 2021 | Case Report | *Frontiers in Neurology* | New migraine-like headache with visual aura after posterior cerebral artery aneurysm coiling; illustrates vascular procedure–aura relationship relevant to the brainstem subtype |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
For the specific subtype of **migraine with brainstem aura**, no dedicated clinical trials exist and all current evidence is indirect — extrapolated from broader migraine with aura cohorts and post-cardiac-procedure populations. While the mechanistic hypothesis (P2Y12 inhibition → reduced microembolism and platelet-derived 5-HT → CSD prevention) is well-grounded, it remains unconfirmed in this subtype. Furthermore, clopidogrel is not currently approved or marketed in Saudi Arabia, which adds a significant regulatory barrier. Notably, the closely related **Migraine Disorder** indication (TxGNN Rank #2) carries stronger evidence (Level L2, "Proceed with Guardrails") anchored by the completed CANOA trial (NCT00799045, JAMA 2015, n=220), making that indication a more actionable near-term target.

**To advance the brainstem aura indication specifically, the following is needed:**

- **Subtype-specific clinical trial:** Enroll migraine with brainstem aura patients with confirmed PFO/RLS as a dedicated cohort, distinct from general migraine with aura populations
- **COMPETE trial results (NCT05546320, n=1,000):** Completion of this large three-arm RCT will provide the most definitive comparative data on antiplatelet therapy vs alternatives in PFO-associated migraine
- **MOA documentation:** Formal retrieval of clopidogrel's DrugBank MOA entry and TFDA package insert warnings and contraindications to complete the safety profile
- **Saudi Arabia regulatory pathway:** Since the drug has zero local authorizations, a new drug application or compassionate use framework would be required before any clinical evaluation in the Kingdom
- **CYP2C19 pharmacogenomics consideration:** Approximately 14–20% of populations of Middle Eastern descent carry reduced-function CYP2C19 alleles, which may impair clopidogrel bioactivation; pharmacogenomic screening protocols should be defined before any prospective study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

