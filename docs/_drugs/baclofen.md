---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 2
---

# Baclofen
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist widely used for the treatment of spasticity associated with multiple sclerosis and spinal cord injury. The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**, with **0 clinical trials** and **10 publications** (primarily narrative reviews and animal studies) currently supporting this direction. A secondary prediction for **Nicotine Dependence** carries stronger clinical evidence (3 trials, 20 publications, L3) and is detailed in a dedicated section below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Spasticity (muscle spasms associated with multiple sclerosis, spinal cord lesions) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally documented in the evidence pack. Based on available information, Baclofen is a selective GABA-B receptor agonist that reduces neuronal excitability by hyperpolarizing neurons in the spinal cord and brain, making it effective for muscle spasticity. Its potential relevance to ADHD rests on a separate but related pathway.

GABA-B receptor agonism is theorized to modulate dopamine and norepinephrine tone in the prefrontal cortex — precisely the neurotransmitter systems implicated in ADHD pathophysiology. By suppressing mesolimbic dopamine activity via nucleus accumbens inhibition, baclofen could theoretically dampen the dysregulated reward signalling and impaired executive function that characterize ADHD.

Animal studies using spontaneously hypertensive rats (SHR), a validated ADHD model, demonstrate that GABA-B agonists alter cortical and hippocampal EEG patterns consistent with improved attentional states. However, this mechanistic link remains indirect and extrapolated from preclinical models. No human clinical trials have tested baclofen specifically in ADHD populations, and the theoretical GABA-B–prefrontal circuit connection has not been clinically validated for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review/Meta-analysis | Cureus | Efficacy of behavioral interventions, antipsychotics, and alpha agonists for Tourette's tics; ADHD as major comorbidity discussed |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Narrative Review | Clinical Neuropharmacology | Mood stabilizers in autism spectrum disorders; addresses attention deficits and GABAergic treatment approaches in neurodevelopmental conditions |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Narrative Review | International Review of Neurobiology | Emerging treatments for Tourette syndrome including baclofen for tics; ADHD as a primary comorbidity throughout |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Clinical Review | Journal of Child Neurology | Baclofen used in 450 patients with tics/Tourette's syndrome rated on Yale Global Tic Severity Scale; suggests GABAergic modulation of comorbid ADHD symptoms |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Clinical Review | Paediatric Drugs | Overview of Tourette syndrome pharmacotherapy; clonidine and dopamine antagonists as first-line agents, contextualising the ADHD comorbidity treatment gap |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical Review | L'Encephale | Off-label methylphenidate prescribing in adult ADHD in France; illustrates the significant unmet need and off-label prescribing landscape in adult ADHD |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study (EEG, SHR model) | Brain Research | GABA-B agonists alter cortical and hippocampal EEG in spontaneously hypertensive rats (SHR, ADHD model); most directly relevant mechanistic evidence |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | α2A-adrenergic receptor stimulation in ventral hippocampus reduces impulsive decision-making in rodents; supports noradrenergic circuits in ADHD impulsivity |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and basolateral amygdala dissociable contributions to effortful decision-making; relevant to ADHD cognitive effort deficits |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | European Journal of Neuroscience | Habenula functional integrity required for social play in rats; relevant to monoaminergic regulation implicated in ADHD reward processing |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.32%), evidence for baclofen in ADHD is limited to animal models and indirect mechanistic reasoning, with no human clinical trials identified. The GABA-B agonism to prefrontal dopamine/norepinephrine modulation hypothesis is biologically plausible but has not been tested in any clinical ADHD population.

**To proceed, the following is needed:**
- At least one prospective pilot clinical study testing baclofen in ADHD (adult or pediatric)
- Formal mechanism of action documentation linking GABA-B agonism to prefrontal executive function
- Safety data specific to use alongside common ADHD medications (methylphenidate, atomoxetine) — drug interaction profile unknown
- Taiwan TFDA package insert review for contraindications and warnings before any clinical consideration

---
---

## Secondary Predicted Indication: Nicotine Dependence

**TxGNN Score: 99.19% | Evidence Level: L3 | Recommendation: Research Question**

### Why is This Prediction Reasonable?

Baclofen, as a GABA-B receptor agonist, directly suppresses dopamine release in the nucleus accumbens — the central node of the brain's reward circuit through which nicotine exerts its addictive effects. By blunting this mesolimbic dopamine signal, baclofen theoretically reduces the reinforcing properties of nicotine, attenuates craving, and dampens withdrawal manifestations.

Multiple preclinical studies confirm that baclofen reduces nicotine-induced conditioned place preference, discriminative stimulus effects, and drug-seeking reinstatement after extinction. This mechanism is highly consistent with baclofen's established (and in France, approved) role in alcohol use disorder, suggesting a shared GABA-B modulatory pathway across substance dependencies rather than a drug- or substance-specific effect.

One completed Phase 2 fMRI trial (NCT01821560, n=44) in cigarette smokers represents the most clinically informative data point. Two additional trials were terminated early, limiting efficacy conclusions but not raising overt safety signals.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Perfusion fMRI examining baclofen's effects on brain and behavioral responses to appetitive smoking cues in nicotine-dependent smokers; only completed efficacy-adjacent trial in this indication |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Baclofen vs. placebo for reducing smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers; terminated early (reason not publicly documented; partial data may have informational value) |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Formal test of the GABAergic hypothesis of nicotine dependence; terminated extremely early due to insufficient enrollment; no meaningful efficacy conclusions possible |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Pilot RCT (Conference Abstract) | Neuropsychopharmacology | Double-blind, placebo-controlled trial of baclofen for concurrent alcohol and nicotine dependence; most direct clinical evidence for the nicotine indication |
| [11403726](https://pubmed.ncbi.nlm.nih.gov/11403726/) | 2001 | Controlled Clinical Study | Nicotine & Tobacco Research | Single-dose baclofen (20 mg) in 16 smokers using within-subjects design; reduced subjective cigarette effects and smoking satisfaction vs. placebo |
| [34601742](https://pubmed.ncbi.nlm.nih.gov/34601742/) | 2021 | Clinical Guidelines | Medical Journal of Australia | Australian guidelines for alcohol treatment; discusses GABA-B agonists including baclofen, relevant to cross-addiction mechanistic framework |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Repurposing Review | International Review of Neurobiology | Comprehensive review of drug repurposing for alcohol dependence; baclofen listed as approved (France) with discussion of cross-substance dependence potential |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | European Neuropsychopharmacology | Baclofen prevents drug-induced reinstatement of extinguished nicotine-seeking and nicotine conditioned place preference in rodents |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and physical withdrawal manifestations in mice; dose-dependent effects observed |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | Baclofen (3 mg/kg) reduces nicotine conditioned place preference and discriminative stimulus in rats, while preserving food-reinforced behavior |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for tobacco cessation; baclofen identified as investigational GABAergic agent with preclinical support |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opinion on Emerging Drugs | Emerging drugs for tobacco dependence; GABA-B agonists including baclofen discussed as mechanistically promising candidates |
| [10805604](https://pubmed.ncbi.nlm.nih.gov/10805604/) | 2000 | Animal Study | Psychopharmacology | GABA-B receptor manipulation in the ventral tegmental area reduces nicotine self-administration in rats; foundational mechanistic study |

### Conclusion for Nicotine Dependence

**Decision: Research Question**

**Rationale:**
Nicotine dependence carries meaningfully stronger evidence than ADHD — one completed Phase 2 trial, a 41-patient terminated efficacy trial, multiple converging animal studies, and a biologically coherent GABA-B → mesolimbic dopamine mechanism. The indication is also structurally analogous to baclofen's approved use in alcohol use disorder (France), strengthening the cross-substance dependence rationale.

**To proceed, the following is needed:**
- Full publication of NCT01821560 results (fMRI endpoints and behavioral outcomes)
- Clarification of termination reasons for NCT00257894 and NCT01228994 before committing to a new trial design
- A well-powered Phase 2 randomised controlled trial with abstinence as the primary endpoint
- Drug interaction assessment with standard smoking cessation pharmacotherapies (varenicline, bupropion, NRT)
- Taiwan regulatory pathway assessment: baclofen's non-marketed status in Taiwan means a new IND application would be required for any clinical study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

