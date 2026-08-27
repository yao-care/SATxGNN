---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is a broad-spectrum second-generation antiepileptic drug, established globally for partial-onset seizures and, as adjunctive therapy, for myoclonic and generalized tonic-clonic seizures in juvenile myoclonic epilepsy.
The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype),
with **9 clinical trials** and **20 publications** currently identified, though none target this specific reflex-epilepsy phenotype directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset seizures (mono/adjunctive therapy) and myoclonic/generalized tonic-clonic seizures in juvenile myoclonic epilepsy (established global indication; formal Saudi Arabia label text is not yet available — product not marketed there) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank/TFDA is not available (flagged as a High-severity data gap). Based on information available within this evidence pack, levetiracetam belongs to the SV2A (synaptic vesicle protein 2A) modulator class of antiepileptics — it binds SV2A to regulate neurotransmitter release and dampen abnormal, synchronized neuronal firing. This broad-spectrum anti-hyperexcitability mechanism is the basis for its established efficacy in generalized and myoclonic epilepsy syndromes, including juvenile myoclonic epilepsy (JME).

Visual epilepsy — seizures triggered by photic/visual stimuli — is generally classified within the idiopathic generalized epilepsy (IGE) spectrum, the same category in which levetiracetam already has proven efficacy (e.g., myoclonic seizures in JME, photosensitivity-associated IGE). Mechanistically, an SV2A modulator that suppresses cortical hyperexcitability would plausibly extend to visually-provoked reflex seizures, since the underlying cortical hyperexcitability circuitry overlaps substantially with other IGE subtypes.

However, the identified trials and literature largely address levetiracetam's use for *general* seizure prophylaxis (intracerebral hemorrhage, TBI, neonatal seizures) or for migraine with visual aura, rather than photosensitive/visually-induced epilepsy specifically. The mechanistic rationale is therefore an analogy from adjacent IGE evidence rather than a direct, indication-specific confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | RCT of prophylactic levetiracetam for functional outcome after acute intracerebral haemorrhage; early seizures occur in up to 40% of ICH cases on continuous EEG. |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for prophylactic treatment of migraine with or without aura (including visual disturbances). |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Efficacy of levetiracetam in control of neonatal seizures vs. traditional phenobarbital first-line therapy. |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of new AEDs (including levetiracetam) as first-choice bitherapy in focal epilepsy. |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam's effect on hippocampal hyperactivity in psychosis, using a visual scene-processing fMRI task. |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | AVASPA gene therapy for Canavan disease (levetiracetam not the study drug; low direct relevance). |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated (n=1) | 1 | Pharmacologic modulation of hippocampal hyperactivity in psychosis using levetiracetam; terminated early. |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST trial: optimal duration/choice of AEDs (phenytoin vs. levetiracetam) after traumatic brain injury. |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | RCT of cognitive/neuropsychological effects of adjunctive levetiracetam in children with refractory partial-onset seizures. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | PEACH trial: prophylactic levetiracetam tested to reduce acute seizure risk after intracerebral haemorrhage. |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs. phenobarbital for neonatal seizures; no FDA-approved therapy currently exists for this population. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network Meta-analysis | Journal of Neurology | Compares efficacy/safety of antiseizure medications, including levetiracetam, for idiopathic generalized epilepsies. |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in IGE, specifically juvenile myoclonic epilepsy. |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in ICH, TBI, and subarachnoid hemorrhage; efficacy/dosing remain unclear. |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Clinical Practice Guideline | Neurocritical Care | Neurocritical Care Society guideline on seizure prophylaxis in moderate-severe TBI. |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | "Spotlight on levetiracetam" — summarizes approved indications, including adjunctive treatment of myoclonic seizures in JME. |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Initial management of seizure in adults. |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Review of status epilepticus diagnosis, monitoring, and treatment. |
| [29037435](https://pubmed.ncbi.nlm.nih.gov/29037435/) | 2018 | Review (veterinary) | Vet Clin North Am Small Anim Pract | Feline epilepsy management; levetiracetam noted as useful for certain seizure types in cats — low direct human relevance. |

## Saudi Arabia Market Information

Levetiracetam currently holds no marketing authorization in Saudi Arabia (0 licenses on file); the product's status is recorded as **not marketed**, so no product/dosage-form/indication details are available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no identified trial or publication directly studies levetiracetam in visually-induced/photosensitive epilepsy — the supporting evidence is drawn by analogy from levetiracetam's established efficacy in adjacent idiopathic generalized epilepsy syndromes (myoclonic seizures, JME) and from general seizure-prophylaxis trials (ICH, TBI, neonatal). This is classified as evidence level L3, insufficient to justify direct clinical progression.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- DrugBank-sourced mechanism of action confirmation (currently a High-severity data gap)
- A trial or case series specifically enrolling patients with visually-induced/reflex (photosensitive) epilepsy, rather than general seizure-prophylaxis populations
- Saudi Arabia regulatory dossier and marketing authorization data, since the product is not currently marketed there

*Note: within the same evidence pack, a separate predicted indication — status epilepticus (rank 9, TxGNN score 99.91%) — shows substantially stronger direct evidence (L1, multiple completed Phase 3 RCTs including ESETT/NEJM 2019, recommendation "Proceed with Guardrails") and may warrant its own evaluation report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

