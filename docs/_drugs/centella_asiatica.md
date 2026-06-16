---
layout: default
title: Centella Asiatica
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 3
---

# Centella Asiatica
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

# CENTELLA ASIATICA: From Wound Healing & Skin Conditions to Insomnia

## One-Sentence Summary

Centella asiatica (Gotu Kola) is a traditional Ayurvedic and East Asian medicinal herb historically used for wound healing, microcirculatory disorders, and skin conditions, with no formally approved pharmaceutical indications currently on record in Saudi Arabia.
The TxGNN model predicts it may be effective for **Insomnia**, supported by **2 clinical trials** and **1 preclinical publication** directly targeting this indication — alongside substantially richer evidence for the mechanistically related indication of **Anxiety** (4 trials, 20 publications, Evidence Level L3).
The current evidence base for insomnia specifically remains at the preclinical stage (L4), placing this candidate in exploratory research territory.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved pharmaceutical indication on record; traditional use for wound healing and skin conditions |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data from regulatory databases is not available for Centella asiatica. Based on published pharmacological research, the herb's primary bioactive constituents are ursane triterpenoids — **asiaticoside**, **asiatic acid**, and **madecassoside** — which are believed to mediate its neuropsychiatric effects through multiple complementary pathways.

The most relevant mechanism for insomnia is **positive modulation of GABA-A receptors**: asiatic acid and madecassic acid have been shown to modulate GABA-A receptor subtypes (PMID 27062315), producing a calming effect mechanistically analogous to benzodiazepines but without the structural dependency risk. Additionally, Centella asiatica extracts suppress **HPA axis hyperactivity**, reducing circulating cortisol and corticosterone — a pathway directly implicated in hyperarousal-type insomnia. A third mechanism involves **Orexin/hypocretin pathway inhibition**: the 2024 zebrafish insomnia model study (PMID 38812527) demonstrated that the ethanol extract prolonged sleep duration and reduced hyperactivity by inhibiting Orexin signaling and downstream ERK1/2, Akt, and p38-MAPK phosphorylation, all of which are key drivers of the arousal system.

Insomnia and anxiety share substantial neurobiological overlap — both involve HPA dysregulation, GABAergic insufficiency, and monoaminergic imbalance — which explains why the TxGNN model simultaneously ranks anxiety (L3, rank 2) and insomnia (L4, rank 1) as top predictions. The human clinical evidence is currently stronger for anxiety (including a small human RCT in generalized anxiety disorder, PMID 20677602) than for insomnia specifically, where evidence has not yet advanced beyond the animal model stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | NA | Active, Not Recruiting | 30 | Nightly Brahmi-Gotu Kola oil foot massage (Padabhyanga) vs. organic sesame oil in perimenopausal women (ages 40–55); primary endpoints include sleep quality and mood disturbance — direct relevance to insomnia, but delivery is topical/massage rather than oral, limiting dose-response conclusions |
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Completed | 74 | Oral Inner Calm supplement + topical Super Calm regimen for skin health and inner wellness; Centella asiatica is a component ingredient, but primary endpoints are skin redness and sensitivity — sleep relevance is incidental and indirect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Preclinical (Animal Model) | F1000Research | Centella asiatica ethanol extract prolonged sleep duration and reduced hyperactivity in a zebrafish larvae insomnia model; mechanism identified as inhibition of Orexin, ERK1/2, Akt, and p38-MAPK signaling pathways — the most directly relevant mechanistic study for this indication |

---

## Saudi Arabia Market Information

No products containing Centella asiatica are currently registered with Saudi SFDA. There are 0 product authorizations on record, and the drug has no market presence in Saudi Arabia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data was found in the DDI database query. No warning or contraindication data from SFDA is currently available for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns Centella asiatica its highest prediction score for insomnia (99.94%), and the mechanistic rationale via GABAergic, Orexin, and HPA axis pathways is scientifically plausible, the evidence base for this specific indication remains entirely preclinical (L4). The only clinical trial with sleep as a direct endpoint (NCT07274371) uses a topical massage delivery method that cannot be equated with oral pharmacological use. No human RCT targeting insomnia as a primary endpoint currently exists.

**To proceed, the following is needed:**

- **Priority human study:** A small-scale proof-of-concept RCT using standardized oral Centella asiatica extract (defined asiaticoside content) with validated sleep endpoints — Polysomnography (PSG), Pittsburgh Sleep Quality Index (PSQI), or Insomnia Severity Index (ISI)
- **Dose standardization:** Establish reproducible dosing parameters based on triterpene content (asiaticoside ≥40%, common in TECA preparations)
- **MOA documentation:** Retrieve formal pharmacology data from DrugBank (DB14256) to complete mechanism characterization
- **Safety review:** Obtain Saudi SFDA package insert data and assess potential herb-drug interactions, particularly with CNS depressants and anxiolytics
- **Consider parallel track for Anxiety (L3):** The anxiety indication has substantially stronger evidence — including a human clinical study in generalized anxiety disorder (PMID 20677602) and multiple preclinical models — and may be a more immediately actionable regulatory pathway with a "Proceed with Guardrails" recommendation under the existing evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

