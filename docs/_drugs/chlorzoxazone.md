---
layout: default
title: Chlorzoxazone
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 9
---

# Chlorzoxazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Chlorzoxazone: From Musculoskeletal Pain to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is a centrally-acting skeletal muscle relaxant established for the relief of acute musculoskeletal pain and spasm, and is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Migraine Disorder** (score 99.73%), with **0 clinical trials** and **3 publications** providing indirect mechanistic support — none of which directly test chlorzoxazone in migraine patients.
Notably, among all 9 predicted indications, **Rheumatoid Arthritis** (rank 9) carries stronger actual evidence at Level L3 and may represent the higher-priority development track.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal pain and muscle spasm (established clinical use; no Saudi Arabia registration on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 — Preclinical / mechanistic studies only |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for chlorzoxazone in this Evidence Pack. Based on known information, chlorzoxazone is a centrally-acting skeletal muscle relaxant — its efficacy in relieving acute musculoskeletal pain and spasm has been established clinically, and the mechanistic pathway most relevant to migraine repurposing involves activation of Ca²⁺-activated K⁺ channels (SK/BK channels).

The proposed link to migraine centres on Familial Hemiplegic Migraine Type 1 (FHM1). Mutations in the *CACNA1A* gene — encoding the pore-forming α1A subunit of Cav2.1 voltage-gated calcium channels — produce neuronal calcium overload that drives both FHM1 episodes and episodic cerebellar ataxia. A preclinical study in *Cacna1a*-S218L mutant mice (PMID 23115190) demonstrated that Ca²⁺-activated K⁺ channel activators directly counteract this pathological Cav2.1 hyperactivation and alleviate ataxia — a mechanistic principle shared with FHM1-associated migraine. If chlorzoxazone genuinely activates SK/BK channels, the same mechanism could theoretically suppress the cortical spreading depression and neuronal hyperexcitability underlying migraine attacks.

However, this chain of reasoning spans multiple inferential steps: the three retrieved publications address vestibular and cerebellar pharmacology rather than migraine directly, the SK/BK activation claim for chlorzoxazone itself lacks published confirmation, and no human study has tested this hypothesis. The biological plausibility is coherent but remains firmly at the preclinical inference stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Pre-clinical (Animal) | *J Neuroscience* | Ca²⁺-activated K⁺ channel activators alleviate cerebellar ataxia in *CACNA1A*(S218L) mutant mice; mechanistic basis for targeting Cav2.1-driven neuronal hyperexcitability, relevant to FHM1 migraine pathophysiology |
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Narrative Review | *Journal of Neurology* | Pharmacotherapy of central vestibular syndromes and cerebellar disorders; discusses how K⁺ channel modulation normalises irregular Purkinje cell firing rates — contextualises the ionic mechanism |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Narrative Review | *Dtsch Arzteblatt Int* | Treatment overview of peripheral and central vestibular vertigo; vestibular migraine accounts for 11.4% of cases, bridging the cerebellar and migraine disease contexts |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (migraine disorder, 99.73%) rests on L4 evidence only — mechanistic inference from a single mouse model with no clinical trial registration and no direct human data — and chlorzoxazone is not registered in Saudi Arabia, making near-term clinical deployment impractical without regulatory groundwork.

---

**Higher-Priority Opportunity — Rheumatoid Arthritis:**

Among all 9 predicted indications, **Rheumatoid Arthritis** (rank 9, TxGNN score 99.05%) carries substantially stronger existing evidence and a preliminary *Research Question* recommendation (decision stage S1, evidence level L3):

| PMID | Year | Type | Key Relevance |
|------|------|------|---------------|
| [22258993](https://pubmed.ncbi.nlm.nih.gov/22258993/) | 2012 | Cochrane Systematic Review | Confirms muscle relaxants are used for RA pain management; establishes the drug class rationale |
| [5312143](https://pubmed.ncbi.nlm.nih.gov/5312143/) | 1970 | Clinical Study (Uncontrolled) | Chlorzoxazone + prednisolone combination reported in rheumatic disease patients |
| [817531](https://pubmed.ncbi.nlm.nih.gov/817531/) | 1976 | In vitro | Chlorzoxazone inhibits cathepsin B1 from bovine spleen — relevant to RA cartilage destruction pathway |
| [136142](https://pubmed.ncbi.nlm.nih.gov/136142/) | 1976 | In vitro | Chlorzoxazone inhibits neutral protease from human leukocyte granules — suggests potential anti-proteolytic mechanism in RA synovium |
| [40848494](https://pubmed.ncbi.nlm.nih.gov/40848494/) | 2025 | Analytical Chemistry | Chlorzoxazone + ibuprofen combination validated as therapeutic option for RA, ankylosing spondylitis, and sprains in clinical practice |
| [14019303](https://pubmed.ncbi.nlm.nih.gov/14019303/) | 1962 | Case Series | Chlorzoxazone in musculo-articular disease — earliest clinical report |

The RA evidence spans three mechanistic layers — symptom relief (muscle spasm/joint pain), anti-proteolytic enzyme inhibition, and CYP2E1-mediated inflammatory lipid metabolism — and should be evaluated on a dedicated, higher-priority track.

---

**To proceed with the migraine indication, the following is needed:**

- Confirmed MOA data from DrugBank: specifically, published evidence that chlorzoxazone activates SK/BK channels (distinct from its CYP2E1 inhibition role)
- Saudi Arabia regulatory pathway assessment: identification of markets where chlorzoxazone is currently registered (e.g., USA, Romania, Latin America) to inform a bridging strategy
- Safety documentation: package insert warnings, contraindications, and drug-drug interaction profile
- Targeted literature search: chlorzoxazone + potassium channel + FHM1 / migraine prophylaxis in human subjects
- Preclinical proof-of-concept: a migraine-specific animal model (e.g., cortical spreading depression assay) to validate the SK/BK hypothesis before any clinical planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

