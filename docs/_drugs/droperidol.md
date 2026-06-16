---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Droperidol
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

# Droperidol: From Acute Agitation & Antiemesis to Tourette Syndrome

## One-Sentence Summary

Droperidol is a butyrophenone neuroleptic used clinically for acute agitation, psychosis-related sedation, and post-operative nausea/vomiting — it is not currently marketed in Saudi Arabia.
The TxGNN model ranks **Tourette Syndrome** as its top new indication candidate (score 99.89%),
but direct evidence is limited: **0 registered clinical trials** and **1 indirect publication** (via haloperidol, not droperidol itself) currently exist for this specific pairing.

> **Note:** Although Tourette Syndrome is TxGNN's highest-ranked prediction, stronger clinical evidence exists for **headache disorders** (20 publications, 1 RCT, 1 clinical trial) and **acute mania in bipolar disorder** (Cochrane systematic review + RCT). Those indications are discussed separately in the Conclusion section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Saudi Arabia; pharmacologically known for acute agitation, procedural sedation, and antiemesis |
| Predicted New Indication (Rank 1) | Tourette Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical/class-effect inference; no direct droperidol trials) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Droperidol is a butyrophenone antipsychotic that exerts its primary effect through potent dopamine D2 receptor antagonism, with additional α₁-adrenergic and H₁ histamine antagonism. This pharmacological profile places it in the same class as haloperidol and pimozide — both of which are approved first-line agents for Tourette Syndrome (TS). The TxGNN prediction is therefore mechanistically coherent: TS is characterised by dopaminergic hyperactivity in the cortico-striato-thalamo-cortical circuit, and D2 blockade is the established therapeutic strategy.

The reasoning from mechanism to clinical application follows a class-effect logic. Haloperidol, the closest chemical relative of droperidol within the butyrophenone class, has decades of evidence supporting tic suppression in TS. Because droperidol shares the same receptor binding profile — and is in fact pharmacokinetically more potent than haloperidol — the model inference that it may produce a similar clinical effect is scientifically plausible.

However, plausibility is not evidence. No clinical trial or prospective study has directly evaluated droperidol for TS. The single supporting publication in this pack (PMID 791589, 1976) studies haloperidol, not droperidol. This is an indirect inference at best (L4), and the decision to proceed would require purpose-designed studies to establish direct efficacy and safety in this patient population.

---

## Clinical Trial Evidence

Currently no clinical trials for Droperidol in Tourette Syndrome are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Clinical Study (Indirect) | Current Psychiatric Therapies | Haloperidol (not droperidol) in severe behavioural disorders — cited as class-effect support only |

> **Limitation:** This study evaluates haloperidol, a related butyrophenone. No publication directly studies droperidol in Tourette Syndrome patients.

---

## Saudi Arabia Market Information

Droperidol has **no regulatory authorisations** in Saudi Arabia. It is not approved or marketed through the SFDA.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug interactions) from Saudi Arabian regulatory sources is not available for this drug.

Based on widely known pharmacological characteristics of droperidol, clinicians should be aware that this agent carries a **black-box warning in the United States (FDA, 2001)** for QT prolongation and risk of Torsades de Pointes, which significantly constrained its clinical use globally. This safety signal is particularly relevant for any new indication development and must be factored into any research protocol design.

Please refer to the current package insert and established pharmacovigilance resources for complete safety information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction for droperidol is Tourette Syndrome, supported by strong mechanistic reasoning (D2 antagonism, butyrophenone class effect with haloperidol/pimozide), but zero direct clinical evidence exists — the sole supporting publication studies a different drug. An L4 evidence level and a serious cardiac safety signal (QT prolongation) make immediate clinical development premature without foundational studies.

---

### Higher-Priority Repurposing Targets (Based on Existing Evidence)

While Tourette Syndrome receives the highest TxGNN score, the evidence landscape favours two other indications for near-term development consideration:

| Indication | Evidence Level | Clinical Evidence Highlights | Recommendation |
|-----------|---------------|------------------------------|----------------|
| **Headache Disorder / Migraine** | L2–L3 | 1 RCT (*Neurology* 2003, PMID 12552051); 1 randomised trial (*Am J Emerg Med* 2002, PMID 11781912); Cochrane systematic review; ≥20 publications; 1 registered trial (NCT01406860, terminated) | Proceed with Guardrails |
| **Manic Bipolar Affective Disorder** | L3 | Cochrane systematic review (PMID 27976370); RCT in acute agitation (PMID 321727); case series in mixed mania (PMID 9789713) | Proceed with Guardrails |
| **Tourette Syndrome** | L4 | Class-effect inference only; no direct data | Hold — Research Question |

---

**To advance the Tourette Syndrome hypothesis, the following is needed:**

- A prospective pilot study (Phase 1/2) of droperidol directly in TS patients — no such study exists
- Full pharmacovigilance review addressing QT prolongation risk in the TS population (often children and adolescents)
- MOA data confirmation via DrugBank API (currently a data gap)
- Saudi Arabia regulatory pathway assessment for a non-marketed drug entering a new indication
- Comparison against approved TS agents (haloperidol, fluphenazine, clonidine, guanfacine) to define the clinical niche

**To advance the Headache / Migraine indication (recommended near-term priority):**

- Confirm existing RCT data quality and update evidence review for post-2020 studies
- Assess dosing protocols for emergency department versus outpatient settings
- Address QT monitoring requirements in the headache population
- Explore SFDA new drug application pathway given Saudi Arabia non-marketing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

