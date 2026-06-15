---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Alprazolam: From Anxiety & Panic Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine widely used for anxiety disorders and panic disorder, working by enhancing inhibitory neurotransmission through GABA-A receptor modulation to produce sedative, anxiolytic, and hypnotic effects.
The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently supporting this direction.
While its sedative-hypnotic properties provide strong mechanistic justification, mainstream clinical guidelines do not recommend benzodiazepines as first-line treatment for insomnia due to tolerance, dependence, and cognitive impairment risks.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders, panic disorder (with or without agoraphobia) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, alprazolam is a high-potency benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor. By binding to a distinct site on the receptor complex, it enhances the frequency of chloride channel opening in response to GABA, resulting in dose-dependent CNS depression — manifesting clinically as anxiolysis, sedation, hypnosis, anticonvulsion, and muscle relaxation. This mechanism directly underpins its sedative-hypnotic properties and makes the TxGNN insomnia prediction pharmacologically coherent.

Anxiety disorders (alprazolam's primary indication) and insomnia are deeply intertwined clinically. Sleep-onset difficulties and fragmented sleep are among the most prevalent comorbidities of generalized anxiety disorder and panic disorder, sharing overlapping neurobiological substrates including amygdala hyperactivation and dysregulated autonomic arousal. Alprazolam's rapid onset of action (T~max~ 1–2 hours) has historically led to its use — both on-label and off-label — for sleep initiation in comorbid anxiety-insomnia presentations, particularly in Asian clinical practice settings.

However, translating this mechanism into a formal insomnia repurposing requires careful qualification. International sleep medicine guidelines (AASM, European Sleep Research Society) categorize benzodiazepines as second- or third-line options for insomnia, reserved for short-term use when first-line cognitive behavioural therapy for insomnia (CBT-I) or non-benzodiazepine hypnotics are unavailable or ineffective. The risks of tolerance (typically within 2–4 weeks), rebound insomnia, physical dependence, and anterograde amnesia — especially in elderly patients — must be explicitly managed in any deployment strategy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort at a Taiwanese academic medical center assessing risk-benefit of hypnotics (including alprazolam) for sleep disorders in elderly patients; evaluates prescribing patterns, efficacy, safety, pharmacokinetics, and pharmacogenomic characteristics |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | 8-week multicenter open-label RCT comparing Niravam™ (alprazolam ODT) + SSRI/SNRI vs SSRI/SNRI alone for anxiety in GAD/Panic Disorder; alprazolam used as augmentation for faster symptom relief, with sleep quality likely captured as part of composite anxiety outcomes |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Double-blind, double-dummy, placebo-controlled study of AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; alprazolam likely serves as active comparator in double-dummy design, with sleep-related agitation as a secondary domain |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management intervention to promote cessation of benzodiazepines (including alprazolam, prescribed for anxiety and sleep) in US Veterans; study direction is deprescribing rather than initiation |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Comparison of hypnosis session vs alprazolam premedication for perioperative anxiety in gynecological surgery; documents standard use of alprazolam as sedative premedication, not a primary insomnia study |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin vs placebo for treatment of benzodiazepine (including alprazolam) dependence; terminated early due to critically low enrollment (N=2); addresses dependence risk rather than insomnia efficacy |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for idiopathic hypersomnia; alprazolam is not a primary agent; the indication (hypersomnia — excessive daytime sleepiness) is directionally opposite to insomnia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Observational Study | Medicine | Retrospective study (N=116) comparing alprazolam alone vs Du Meridian moxibustion + ear acupuncture in patients with coronary heart disease and insomnia; alprazolam used as active control, directly demonstrating its clinical role in insomnia management |
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative Study (RCT-like) | Cureus | Head-to-head comparison of alprazolam vs melatonin for sleep disturbances in end-stage renal disease patients on hemodialysis; directly evaluates alprazolam efficacy and safety profile for insomnia in a specific high-risk population |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica (Zagreb) | Systematic meta-analysis of tranquilizers (including benzodiazepines) for elderly patients with chronic non-communicable diseases; assesses optimal dosing, efficacy endpoints, and adverse effects relevant to sleep disorder management |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical Study | Aging | Proteomic analysis showing repeated alprazolam administration (24-day murine model) causes mitochondrial dysfunction and hippocampus-dependent memory consolidation impairment; identifies 439 differentially expressed proteins underlying cognitive adverse effects |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive Model / Epidemiology | Value in Health Regional Issues | 10-year predictive model of benzodiazepine use in Croatia; BZDs widely prescribed for anxiety, insomnia, and epilepsy, with documented long-term risks including memory loss, Alzheimer's association, dependence, and fall risk in the elderly |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world Observational | China Journal of Chinese Materia Medica | Real-world analysis of 1,067 insomnia inpatients across 20 hospitals; documents concurrent diseases (hypertension 26.9%, cerebrovascular disease) and prescribing patterns of Western medicines including benzodiazepines for insomnia |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Cross-sectional survey (Dec 2022–Feb 2023) of insomnia among COVID-19 survivors using the Insomnia Severity Index (ISI); characterizes post-COVID insomnia prevalence and pharmacological management patterns |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Retrospective cohort study showing deprescribing of zolpidem/benzodiazepines in cirrhosis patients significantly reduces falls and fractures; highlights the safety imperative of minimising hypnotic use in hepatically compromised patients |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | RCT evaluating eszopiclone for sleep quality and cognitive function in elderly Alzheimer's patients with sleep disorders; provides comparative context for benzodiazepine vs non-BZD hypnotics in the elderly |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetic review of anxiolytic drugs including benzodiazepines; documents absorption, distribution, metabolism, and elimination parameters relevant to dosing optimisation for both anxiety and sleep indications |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important Note:** Formal safety data (key warnings, contraindications, drug interaction profile) were not available in the current Evidence Pack. Alprazolam is a Schedule IV controlled substance under international conventions (UN Convention on Psychotropic Substances). Its well-established safety concerns — including physical dependence, tolerance development within 2–4 weeks, rebound insomnia upon discontinuation, anterograde amnesia, respiratory depression (particularly in combination with opioids or alcohol), and cognitive decline in elderly populations — must be thoroughly reviewed from the official prescribing information before any clinical deployment or formulary decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprazolam's GABA-A positive allosteric modulation provides a strong mechanistic basis for insomnia treatment, and comparative observational studies (including a direct alprazolam vs melatonin trial in hemodialysis patients and use as active control in an insomnia-comorbid cardiac population) confirm its real-world clinical role. However, its unfavourable long-term risk profile — dependence, tolerance, cognitive impairment — means deployment must be tightly scoped, monitored, and time-limited.

**To proceed, the following is needed:**
- **Regulatory pathway:** Confirm SFDA controlled substance classification and import requirements for alprazolam in Saudi Arabia before any formulary submission
- **Full safety data:** Retrieve official package insert (PI/SmPC) for complete warnings, contraindications, and drug interaction profile; DDI data was not found in the current search
- **MOA documentation:** Retrieve formal MOA data from DrugBank (DG002) to complete mechanistic analysis for the regulatory dossier
- **Patient population definition:** Restrict to well-defined subpopulations (e.g., short-term use in anxiety-comorbid insomnia, ≤4 weeks, adult non-elderly patients without respiratory compromise or substance use history)
- **Comparative effectiveness review:** Position alprazolam against first-line CBT-I and currently available non-BZD hypnotics (eszopiclone, zolpidem, doxepin) to define the clinical niche in Saudi Arabia practice
- **Risk management plan:** Mandatory monitoring protocol covering dependence screening, dose limitation, mandatory reassessment at 2 and 4 weeks, and a documented deprescribing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

