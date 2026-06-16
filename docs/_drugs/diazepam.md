---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Diazepam is a long-established benzodiazepine, primarily known for treating anxiety disorders, muscle spasms, alcohol withdrawal, and acute seizures.
The TxGNN model predicts it may be effective for **Insomnia**, with **1 direct head-to-head RCT** and **multiple clinical and review publications** supporting this well-characterized hypnotic use.
The mechanistic rationale is clear — diazepam enhances GABA-A receptor activity, producing central inhibition that shortens sleep onset and prolongs total sleep time — but its long half-life and dependence liability place it firmly in second-line territory by modern clinical standards.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders, muscle spasms, seizures, alcohol withdrawal (established uses; no formal regulatory record in this dataset) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | ~100.00% (0.9999975) |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diazepam is a positive allosteric modulator (PAM) of the GABA-A receptor. By binding to the benzodiazepine site on the receptor complex, it increases the frequency of chloride ion channel opening in response to GABA, amplifying central inhibitory neurotransmission throughout the brain. This mechanism directly suppresses the cortical and limbic hyperarousal that underlies both anxiety and difficulty sleeping — explaining why sedation has been a clinically recognized effect of diazepam since its introduction in the 1960s.

The relationship between the anxiety context and insomnia is not incidental. Both conditions share overlapping GABAergic dysregulation, and insomnia frequently co-occurs with or is secondary to anxiety states. A 1981 double-blind RCT (PMID 6113175) directly evaluated diazepam 5 mg versus lormetazepam 1 mg in 100 outpatients with sleep disorders: diazepam demonstrated objective hypnotic efficacy, reducing sleep onset latency and prolonging uninterrupted sleep, though lormetazepam performed better on several endpoints. More recently, a 2024 review in *Bioorganic Chemistry* (PMID 39581171) explicitly lists insomnia among the established clinical indications of diazepam-class GABA-A PAMs.

The main caveat is pharmacokinetic: diazepam's elimination half-life of 20–100 hours (with an active metabolite, desmethyldiazepam, adding further) produces daytime residual sedation, accumulation with repeated dosing, tolerance, physical dependence, and elevated fall risk in elderly patients. These properties have led modern clinical guidelines to favor shorter-acting benzodiazepines (temazepam, lorazepam) and non-benzodiazepine alternatives (Z-drugs, orexin receptor antagonists, melatonin receptor agonists) as preferred first-line hypnotics. The TxGNN high score reflects sound mechanistic grounding, but current repurposing value lies in niche populations or settings where these safer alternatives are unavailable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Randomized study evaluating the effect of tapering pace on discontinuation success in insomnia patients using benzodiazepine hypnotics; confirms long-term BZD use (including diazepam class) as the clinical reality in insomnia management |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, Not Recruiting | 260 | Blinded hypnotic tapering protocol combined with CBT for Insomnia (CBTI); randomized trial validates the need for structured discontinuation strategies for insomnia patients on BZDs |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled multicenter RCT of ramelteon as adjunct to facilitate dose reduction or interruption of BZD/non-BZD hypnotics in chronic insomnia; directly involves benzodiazepine hypnotic use as starting condition |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort at a Taiwanese academic medical center examining medication patterns, efficacy, safety, and pharmacogenetics of commonly prescribed hypnotics (including BZDs) in elderly patients |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | Randomized controlled trial comparing Acceptance and Commitment Therapy (ACT) versus standard psychological support added to a BZD withdrawal program in adults with hypnotic-dependent insomnia |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel mechanism-targeting intervention to help older adults discontinue sleeping medications (hypnotics including BZDs); addresses the chronic dependence problem in elderly insomnia patients |
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | N/A | Unknown | 74 | Head-to-head comparison of single-dose clonazepam versus intermittent oral diazepam for prevention of recurrent febrile seizures in children; diazepam is used as the active reference arm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Research | Double-blind 7-day RCT (N=100): diazepam 5 mg vs. lormetazepam 1 mg in outpatients with sleep disorders; both improved sleep, but lormetazepam was significantly superior in reducing sleep onset latency and prolonging uninterrupted sleep — establishes diazepam's hypnotic efficacy with comparative limitations |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Comprehensive review of small-molecule GABA-A receptor modulators; explicitly identifies diazepam as a prototype PAM with therapeutic effects for epilepsy, anxiety, and insomnia, and documents associated side effects including sedation and dependence |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Animal Study | Nature Neuroscience | Long-term diazepam administration in mice impairs structural plasticity of dendritic spines and causes cognitive decline via microglial TSPO-mediated spine engulfment; critical safety signal for chronic hypnotic use |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Systematic Review | Front Pharmacology | Systematic review of Chinese herbal formulae for insomnia; uses diazepam as the standard positive pharmacological control in preclinical sleep models, confirming its conventional reference status as a sedative-hypnotic |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical Study | Cell Mol Biol Lett | Clinical and mechanistic study demonstrating long-term BZD/Z-drug use (including diazepam) for insomnia and anxiety exacerbates breast cancer risk via GABA-A receptor pathways; highlights safety concern for chronic hypnotic prescription |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Review | J Family Practice | Systematic review of published clinical trials on benzodiazepine therapy for insomnia in community-dwelling elderly; concludes BZDs improve objective sleep parameters but evidence for long-term effectiveness is absent and injury risk is elevated |
| [6135990](https://pubmed.ncbi.nlm.nih.gov/6135990/) | 1983 | Review | N Engl J Med | Landmark NEJM review of benzodiazepine pharmacology including clinical use for insomnia; establishes the evidence framework for BZD hypnotics including diazepam in the pre-Z-drug era |

---

## Saudi Arabia Market Information

Diazepam currently has **no registered products in Saudi Arabia**. There are zero active licenses on record in this dataset. Regulatory registration would be required before any formal repurposing pathway could proceed through the Saudi Food and Drug Authority (SFDA).

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on established pharmacological knowledge of diazepam as a class:

- **Long half-life risk**: Elimination half-life of 20–100 hours plus active metabolite (desmethyldiazepam) leads to accumulation with repeated dosing, residual daytime sedation, and psychomotor impairment
- **Dependence and withdrawal**: Physical dependence develops with regular use; abrupt discontinuation risks rebound insomnia, anxiety, and seizures
- **Elderly-specific hazards**: Elevated fall and fracture risk, cognitive impairment, and paradoxical excitation reactions — particularly relevant given insomnia prevalence in older adults
- **Drug interaction potential**: CNS depressants, opioids, and alcohol may cause additive sedation; cytochrome P450 interactions possible

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam's GABA-A positive allosteric modulation provides a mechanistically sound and historically validated basis for hypnotic use, supported by at least one completed head-to-head RCT and a robust body of clinical literature. However, its pharmacokinetic profile (long half-life, active metabolite, accumulation) and dependence liability mean it is no longer a preferred first-line hypnotic agent, positioning any repurposing effort as a second-line or special-population use case.

**To proceed, the following is needed:**

- Obtain and review full package insert (SFDA/reference market SmPC) to document approved indications, warnings, and contraindications
- Retrieve DrugBank MOA data to formally complete mechanistic analysis
- Clarify whether this is a true repurposing scenario or re-registration of an existing global indication in the Saudi Arabia market
- Define the target population precisely (e.g., short-term situational insomnia, anxiety-comorbid insomnia) where diazepam's risk-benefit profile is most favorable
- Conduct comparative effectiveness mapping against current Saudi Arabia-available first-line options (orexin antagonists, Z-drugs, melatonin agonists)
- Design a risk management framework covering dependence monitoring, use duration limits, contraindications in elderly patients, and prescriber education requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

