---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 3
---

# Clonazepam
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

# Clonazepam: From Epilepsy/Panic Disorder to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a long-established high-potency benzodiazepine, widely used for epilepsy, panic disorder, and anxiety through enhancement of GABA-A receptor-mediated inhibition.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**,
with **no registered clinical trials** and **20 publications** currently supporting this direction — including a 2017 Cochrane systematic review and the 2025 AASM Clinical Practice Guideline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy, Panic Disorder, Anxiety Disorders (no registered products in Saudi Arabia) |
| Predicted New Indication | Restless Legs Syndrome (RLS) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 (Systematic reviews & authoritative clinical guidelines) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clonazepam is a high-potency, long-acting benzodiazepine that acts by potentiating GABA-A receptor-mediated chloride ion influx, thereby enhancing CNS inhibitory neurotransmission. This mechanism reduces neuronal hyperexcitability across spinal and supraspinal circuits, including those governing motor control during sleep. While detailed MOA data is not currently available from the structured data source (DrugBank query gap), clonazepam's pharmacological class and receptor target are well established in the clinical literature.

Restless Legs Syndrome is characterised by an irresistible urge to move the legs at rest, often accompanied by unpleasant sensory dysaesthesias and Periodic Limb Movements during Sleep (PLMS). The primary pathophysiology involves dysfunction of dopaminergic and iron-metabolism pathways, making dopamine agonists the first-line standard of care. However, GABAergic circuits play a modulatory role in motor suppression during sleep — and clonazepam's capacity to suppress PLMS and consolidate sleep through sedation and motor inhibition provides a mechanistically rational, albeit symptomatic (second-line), basis for its use in RLS.

Historically, clonazepam has been one of the most commonly employed benzodiazepines in RLS management. A 2024 historical review (PMID 38708125) covering a survey of 16,694 RLS patients found that approximately 25% were treated with benzodiazepines — with clonazepam being the most studied agent within this class for this indication. The 2025 AASM Clinical Practice Guideline and the 2017 Cochrane Systematic Review both formally acknowledge the role of clonazepam in RLS and PLMD treatment, providing strong guideline-level endorsement that directly supports the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no registered clinical trials (ClinicalTrials.gov or ICTRP) specifically evaluating clonazepam for restless legs syndrome have been identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Practice Guideline | J Clin Sleep Med | AASM 2025 guideline for RLS and PLMD treatment in adults and children; formally establishes evidence-based recommendations covering the role of benzodiazepines alongside dopaminergic agents |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review of benzodiazepines for RLS; found limited high-quality RCT evidence but confirmed clonazepam is widely used (~25% of treated patients) with demonstrated sleep-quality benefit |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Prospective RCT | J Mid-Life Health | Directly compared clonazepam vs nortriptyline in women >40 with RLS; evaluated rate, frequency, and severity of RLS symptoms as primary endpoints |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | Randomised Double-Blind Crossover | Acta Neurol Scand | Earliest controlled trial: clonazepam significantly improved subjective sleep quality and leg dysaesthesia vs placebo in 6 RLS patients; concluded it is "safe and effective" for RLS, pending long-term confirmation |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Historical Review | Tremor Other Hyperkinetic Mov | Reviewed 17 articles on clonazepam use in RLS/PLMS; survey of 16,694 patients confirmed ~25% benzodiazepine use; most comprehensive historical synthesis to date |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review & Meta-analysis | J Clin Sleep Med | Assessed pharmacological efficacy across drug classes in suppressing PLMS; clonazepam identified as an effective suppressor with quantified effect size |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review | Mov Disord | Movement Disorder Society task force evidence-based review classifying therapeutic efficacy of each RLS drug; provides standardised classification of clonazepam's evidence status |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Narrative Review | Neurotherapeutics | Comprehensive RLS treatment review discussing evolving standard of care; contextualises clonazepam among dopaminergic agents, alpha-2-delta ligands, and opioids |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | Brazilian Study Group expert consensus on RLS; identifies Class I evidence agents (dopamine agonists) and places clonazepam in the secondary treatment tier |
| [12531130](https://pubmed.ncbi.nlm.nih.gov/12531130/) | 2002 | Narrative Review | Sleep Med Rev | Global therapeutic considerations for RLS and PLMS; reviews clonazepam alongside dopaminergic, opioid, and anticonvulsant options in the pre-alpha-2-delta era |

---

## Saudi Arabia Market Information

Clonazepam currently has **no registered products** with the SFDA in Saudi Arabia. There are 0 active authorisations on record. This represents a significant regulatory gap that would need to be addressed before any clinical deployment in the Saudi Arabia market.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and DDI profile) is not available in the current evidence pack. Please refer to the package insert for safety information.

> **Clinical note for pharmacist review:** Clonazepam belongs to the benzodiazepine class. Key safety considerations documented in the broader clinical literature include: physical dependence and tolerance risk with long-term use; next-day residual sedation due to long half-life (18–60 hours); cognitive impairment, particularly in elderly patients; increased fall risk; and Schedule IV controlled substance status in many jurisdictions. These characteristics classify it as a second-line agent for RLS and necessitate a structured monitoring protocol for any repurposing pathway.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The 2025 AASM Clinical Practice Guideline and the 2017 Cochrane Systematic Review — both Tier 1 evidence sources — formally acknowledge clonazepam as a recognised second-line treatment for RLS and PLMD. At least one prospective RCT (PMID 31942156) directly evaluated clonazepam in RLS patients, and the earliest randomised double-blind crossover trial dates to 1984. GABAergic suppression of PLMS provides a mechanistically coherent basis. However, no large Phase 3 RCTs exist, no registered clinical trials are currently active for this indication, clonazepam is not marketed in Saudi Arabia, and its dependence and cognitive-impairment liability impose meaningful guardrails.

**To proceed, the following is needed:**

- **Regulatory pathway assessment:** Confirm the SFDA registration strategy and controlled substance scheduling classification in Saudi Arabia before any clinical use
- **Full safety profile:** Obtain and review the complete package insert (warnings, contraindications, black-box warnings if applicable), which is currently a Blocking data gap (DG001)
- **MOA documentation:** Retrieve structured MOA data from DrugBank to complete the mechanistic linkage analysis (DG002)
- **DDI profile:** Conduct a targeted DDI review — particularly relevant for RLS patients who may be co-administered dopamine agonists, iron supplements, or CNS depressants
- **Population-specific risk stratification:** Establish monitoring protocols for elderly patients (fall risk, cognitive effects) and patients with substance-use history (dependence risk), given that RLS is prevalent in older adults
- **Comparative effectiveness positioning:** Define the intended place-in-therapy (e.g., for patients refractory or intolerant to dopamine agonists and alpha-2-delta ligands) to guide target population selection and benefit-risk framing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

