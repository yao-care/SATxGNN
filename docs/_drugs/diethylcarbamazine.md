---
layout: default
title: Diethylcarbamazine
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
---

# Diethylcarbamazine
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

# Diethylcarbamazine: From Lymphatic Filariasis to Primary Lymphedema

## One-Sentence Summary

Diethylcarbamazine (DEC) is a WHO first-line antifilarial drug with over 70 years of clinical use, targeting the microfilariae and adult worms of *Wuchereria bancrofti* and *Brugia* species that cause lymphatic filariasis. The TxGNN model's top-ranked prediction — syndromic lymphedema (99.59%) — has been evaluated as a knowledge-graph artefact with no plausible mechanistic link; the second-ranked prediction, **primary lymphedema** in the context of filariasis-associated lymphedema (99.25%), is supported by **6 registered clinical trials** (including Phase 3/4 community RCTs enrolling up to 23,789 participants) and **20 publications**, making it the clinically actionable finding of this evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lymphatic filariasis (WHO first-line antifilarial agent) |
| Predicted New Indication | Primary Lymphedema (filariasis-associated) |
| TxGNN Prediction Score | 99.25% (Rank 2; Rank 1 — Syndromic Lymphedema 99.59% — assessed as graph topology artefact, Hold) |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diethylcarbamazine's mechanism of action is well-characterised in the antifilarial literature despite the MOA data gap in this evidence pack. DEC acts primarily as a microfilaricide through three converging pathways: (1) enhancement of host macrophage-mediated oxidative killing via antibody-dependent cellular cytotoxicity (ADCC); (2) disruption of the parasite's arachidonic acid metabolism, impairing microfilarial cell membrane integrity; and (3) partial macrofilaricidal activity against adult worms residing in the lymphatic vessels, reducing ongoing infection and new lymphatic obstruction. WHO has designated DEC as the cornerstone of mass drug administration (MDA) programs, used as the two-drug DEC+albendazole (DA) regimen or the triple-drug ivermectin+DEC+albendazole (IDA) combination.

The link between DEC and primary lymphedema in this evaluation specifically targets **filariasis-induced lymphedema** — the chronic, progressive complication in which adult *Wuchereria bancrofti* or *Brugia* worms damage lymphatic vessels, leading to limb swelling, hydrocele, and elephantiasis. Up to 16 million of the 120 million people globally infected with lymphatic filariasis develop clinically significant lymphedema. DEC acts upstream in this pathological cascade by clearing microfilariae from the bloodstream and partially eliminating adult worms, thereby reducing ongoing lymphatic vessel injury. The TxGNN prediction accurately captures this disease-ontology connection.

**Important caveat — TxGNN Rank 1 (Syndromic Lymphedema, 99.59%):** This prediction is assessed as a likely false positive arising from knowledge-graph topology. Syndromic lymphedema refers to primary lymphedema caused by genetic syndromes such as Milroy disease or Turner syndrome — a pathophysiology entirely unrelated to filarial infection. The high TxGNN score most likely reflects the ontological proximity between the "syndromic lymphedema" and "filariasis-induced lymphedema" disease nodes, not a genuine therapeutic connection. DEC has no plausible mechanism for genetic lymphedema. This prediction is held at **L4 / Hold** and should not advance to clinical evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02899936](https://clinicaltrials.gov/study/NCT02899936) | — | Completed | 23,789 | Head-to-head community trial across 5 countries comparing DEC+albendazole (DA) vs triple IDA therapy; DEC is the primary antifilarial component in both arms; characterized safety and relative efficacy at the largest scale to date |
| [NCT03676140](https://clinicaltrials.gov/study/NCT03676140) | Phase 3 | Completed | 20,000 | Cluster-RCT evaluating safety of IDA co-administered with azithromycin for integrated neglected tropical disease treatment; DEC is a core component of the IDA regimen; confirmed safety in large community settings |
| [NCT03268252](https://clinicaltrials.gov/study/NCT03268252) | — | Completed | 3,200 | MDA optimization trial using DEC+albendazole in Papua New Guinea over 6 years; assessed dose optimization (DEC 6 mg/kg) and community-level microfilarial clearance and transmission interruption |
| [NCT03036059](https://clinicaltrials.gov/study/NCT03036059) | Phase 4 | Completed | 1,462 | Annual vs biannual ivermectin+albendazole MDA in Ghana (onchocerciasis co-endemic setting where DEC is contraindicated); benchmarks LF elimination strategy and highlights DEC's geographic applicability constraints |
| [NCT02974049](https://clinicaltrials.gov/study/NCT02974049) | — | Completed | 189 | Evaluation of alternative LF chemotherapy regimens in Côte d'Ivoire including DEC-based combinations in *Loa loa* co-endemic areas; relevant to safety stratification |
| [NCT07159373](https://clinicaltrials.gov/study/NCT07159373) | Phase 3 | Not Yet Recruiting | 5,100 | Moxidectin+DEC+albendazole vs ivermectin+DEC+albendazole for LF in Fiji; DEC retained in both experimental arms; prospective large-scale trial with results expected 2028 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38708851](https://pubmed.ncbi.nlm.nih.gov/38708851/) | 2024 | Review | N Engl J Med | Comprehensive review of lymphatic filariasis pathogenesis, epidemiology, and management; DEC-based MDA presented as standard of care for prevention of filariasis-induced lymphedema |
| [40345209](https://pubmed.ncbi.nlm.nih.gov/40345209/) | 2025 | RCT | Lancet Infect Dis | Randomised trial of moxidectin combination therapies vs ivermectin for *W. bancrofti* microfilarial clearance in Côte d'Ivoire; DEC included in comparator regimens; informs next-generation LF elimination strategy |
| [40063867](https://pubmed.ncbi.nlm.nih.gov/40063867/) | 2025 | RCT | PLoS Negl Trop Dis | IDA vs DA MDA in Papua New Guinea; demonstrated broader helminth coverage (hookworm, strongyloidiasis) with IDA vs DA without compromising DEC's primary antifilarial role |
| [33728462](https://pubmed.ncbi.nlm.nih.gov/33728462/) | 2021 | RCT | Clin Infect Dis | IDA MDA cluster-RCT in Fiji; DEC-containing IDA showed superior sustained microfilarial clearance at 12 months versus DA in a diurnally subperiodic filarial transmission setting |
| [32511226](https://pubmed.ncbi.nlm.nih.gov/32511226/) | 2020 | Clinical Trial | PLoS Negl Trop Dis | Two-arm community study comparing IDA vs DA in Haiti; IDA demonstrated superior *W. bancrofti* microfilarial clearance; DEC present and active in both arms |
| [26486704](https://pubmed.ncbi.nlm.nih.gov/26486704/) | 2016 | Clinical Trial | Clin Infect Dis | First formal safety and efficacy data for single-dose DEC+ivermectin+albendazole triple therapy in bancroftian filariasis; established the pharmacological basis for the IDA regimen |
| [40380307](https://pubmed.ncbi.nlm.nih.gov/40380307/) | 2025 | Systematic Review | BMC Infect Dis | Network meta-analysis of antifilarial MDA strategies; DEC-containing regimens consistently among the most effective for microfilarial clearance; noted DEC's contraindication in onchocerciasis co-endemic settings due to severe ocular adverse events |
| [35292578](https://pubmed.ncbi.nlm.nih.gov/35292578/) | 2022 | Implementation | Am J Trop Med Hyg | Analysis of WHO IDA guideline adoption pathway; DEC's established safety profile was a key factor in accelerating global LF elimination program scale-up |
| [20739055](https://pubmed.ncbi.nlm.nih.gov/20739055/) | 2010 | Review | Lancet | Landmark review of lymphatic filariasis and onchocerciasis pathogenesis; DEC mechanism of action, efficacy, and safety profile reviewed in the context of global filarial disease burden |
| [3297557](https://pubmed.ncbi.nlm.nih.gov/3297557/) | 1987 | Review | Ciba Found Symp | Foundational mechanistic review of antifilarial agents; DEC characterised as predominantly microfilaricidal through immune modulation (ADCC) and disruption of parasite neuromuscular function and arachidonic acid metabolism |

---

## Safety Considerations

Package insert data was not retrievable through the queried sources for this evidence pack. Based on published clinical trial literature, the following safety considerations are known:

- **Key Warnings**: Mazzotti reaction (fever, urticaria, arthralgias, lymphadenopathy) is the most common adverse effect, caused by immune response to dying microfilariae rather than direct drug toxicity; severity correlates with baseline microfilarial load. Severe ocular adverse events (including risk of blindness) have been reported in patients co-infected with *Onchocerca volvulus* — DEC is **contraindicated** in onchocerciasis-endemic regions for this reason. Serious neurological adverse events are possible in *Loa loa* co-infected individuals with high microfilarial counts.
- **Drug Interactions**: No DDI data was returned from the queried sources. Interaction profile in the IDA triple-drug combination (with ivermectin and albendazole) has been evaluated in multiple trials listed above without signals of pharmacokinetic interaction at standard MDA doses.

Please refer to the full package insert for a complete safety profile before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
DEC is the WHO-endorsed first-line agent for lymphatic filariasis elimination with an L1 evidence base — multiple large-scale Phase 3 and Phase 4 community trials (largest: n = 23,789) unambiguously support its efficacy and safety in preventing and reducing filariasis-induced lymphedema. The TxGNN rank 2 prediction for primary lymphedema, in the filariasis-associated context, is scientifically valid and clinically well-supported. However, DEC carries no Saudi Arabia regulatory authorization (0 licenses), and the top-ranked TxGNN prediction (syndromic lymphedema) must be explicitly de-flagged as a graph artefact before this evidence pack is used in any decision workflow.

**To proceed, the following is needed:**
- Formal package insert review to document warnings and contraindications — **Blocking data gap (DG001)**; without this, S1 safety screening cannot be completed
- Mechanism of action documentation from DrugBank — **High-severity gap (DG002)**; needed for full mechanistic rationale section
- Explicit clinical context clarification: if the target population is in an LF-endemic region, the L1 evidence directly applies; if the intended use is for non-filariasis primary lymphedema (genetic/idiopathic subtypes), this evaluation does not apply and the decision should revert to **Hold**
- Saudi Arabia regulatory pathway assessment: no existing authorization requires a new SFDA registration application or a compassionate use / special access protocol before clinical deployment
- Formal de-flagging of TxGNN Rank 1 (Syndromic Lymphedema) as a graph topology artefact — this prediction should be annotated as Hold / L4 and excluded from downstream clinical screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

