---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
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

# Acetylsalicylic Acid: From Analgesia & Antiplatelet to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (Aspirin) is one of the world's most extensively studied medicines, originally established for analgesia, fever reduction, and antiplatelet cardiovascular protection.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a rare subtype of migraine with aura involving reversible brainstem symptoms such as dysarthria, vertigo, and diplopia,
with **0 clinical trials** and **19 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Analgesia, antipyretic, antiplatelet (established uses; no Saudi Arabia SFDA registration in current dataset) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetylsalicylic acid (ASA) works primarily by irreversibly inhibiting cyclooxygenase enzymes (COX-1 and COX-2), blocking the production of prostaglandins and thromboxane A₂ (TXA₂). Although formal DrugBank MOA data was not retrieved for this report, ASA's pharmacology is among the most well-characterized in medicine. Its analgesic and anti-inflammatory effects come from reduced prostaglandin synthesis at peripheral and central pain pathways, while its antiplatelet action stems from permanent inactivation of COX-1 in platelets — preventing TXA₂-mediated aggregation and vasoconstriction.

Migraine with brainstem aura (formerly known as basilar-type migraine) is characterized by fully reversible brainstem symptoms — including dysarthria, vertigo, tinnitus, diplopia, and bilateral paresthesias — that develop gradually before the headache phase. The core mechanisms involve cortical spreading depression (CSD) and trigeminovascular system activation with neurogenic inflammation. ASA's COX inhibition reduces prostaglandin synthesis at trigeminal nerve terminals, potentially lowering the neuroinflammatory threshold for aura generation. Critically, ASA's antiplatelet effect may also reduce microemboli that can initiate CSD — a particularly compelling link for the brainstem aura subtype, which shares overlapping vascular and platelet-dependent pathways with conditions such as patent foramen ovale (PFO)-associated migraine.

Clinical plausibility is reinforced by existing evidence: a double-blind RCT (PMID 10448545) demonstrated intravenous ASA efficacy in acute migraine with or without aura, and a retrospective cohort study of 203 migraine-with-aura patients (PMID 25729594) evaluated low-dose ASA specifically for prophylaxis. An observational case series (PMID 29017164) and a 2025 systematic review (PMID 39989443) further explore antithrombotic drugs — including ASA — in migraine prevention. The finding that switching from ASA to clopidogrel (another antiplatelet) reduced migraine-with-aura frequency post-PFO closure (PMID 16103551) also points to platelet-mediated 5-HT dynamics as an active pathway that ASA may modulate in brainstem aura.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT (Double-blind) | Cephalalgia | 278 patients with acute migraine (with or without aura) randomized to IV lysine-ASA (equiv. 1 g ASA), sumatriptan 6 mg SC, or placebo; ASA demonstrated significant efficacy in acute migraine relief compared to placebo |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Most up-to-date systematic review exploring antithrombotic drugs — including ASA — as migraine preventive therapy; directly addresses the repurposing question |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | Current Health Sciences Journal | 203 migraine with aura (MA) patients; 95 (46.8%) treated with low-dose ASA as antiplatelet prophylaxis; evaluated efficacy and tolerability specifically in MA prevention |
| [29017164](https://pubmed.ncbi.nlm.nih.gov/29017164/) | 2017 | Observational Case Series | European Neurology | Observational case series directly assessing aspirin prophylaxis outcomes in migraine with aura patients |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline Review (AHS) | Headache | American Headache Society 2015 evidence assessment of acute migraine pharmacotherapies; classifies ASA among evidence-supported acute migraine treatments |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Comprehensive review of migraine with aura covering CSD as the pivotal aura mechanism, ICHD-III criteria, and pathophysiology — provides mechanistic context for ASA's potential targets |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Clinical Study | Heart | Reports that switching anticoagulation from aspirin to clopidogrel after transcatheter PFO closure significantly reduced migraine with aura episodes; supports platelet-dependent antiplatelet mechanism in migraine with aura |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Reviews pathophysiologic, epidemiologic, and clinical differences between migraine with and without aura, including risk implications and management considerations |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: percutaneous PFO closure vs medical therapy in migraine with aura patients refractory to treatment; contextualizes vascular and embolic mechanisms in migraine with aura pathophysiology |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Reviews pharmacological treatment of migraine; identifies aspirin and caffeine-containing combination analgesics as standard of care for mild-to-moderate migraine attacks, including those with aura |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
While no clinical trials are registered specifically for migraine with brainstem aura, a 1999 double-blind RCT confirmed ASA efficacy in acute migraine with aura, retrospective and observational data directly support low-dose ASA prophylaxis in migraine with aura, and a 2025 systematic review has explicitly examined antithrombotics in this setting — collectively placing this TxGNN prediction within a biologically plausible and clinically explored framework. Evidence is currently at L3 (observational studies and systematic review), without a completed Phase 2/3 RCT targeting the brainstem aura subtype specifically.

**To proceed, the following is needed:**
- A prospective RCT or well-powered observational study specifically targeting **migraine with brainstem aura** (ICHD-III defined) rather than migraine with aura broadly
- Retrieval of complete MOA and safety data from DrugBank (DG002) and the SFDA/FDA package insert (DG001), including key warnings, contraindications, and drug–drug interactions
- Dose definition: clarify whether prophylactic low-dose (75–100 mg/day) or acute-treatment doses (900–1000 mg) are more appropriate for this indication
- Clarification of the Saudi Arabia SFDA registration status: aspirin is universally available globally, but the current dataset shows no SFDA registration — a registry cross-check is recommended before any formal submission pathway is planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

