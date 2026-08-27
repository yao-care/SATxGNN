---
layout: default
title: Tolfenamic Acid
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 10
---

# Tolfenamic Acid
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

Using the report template above (this is a document-generation task, not a coding/skill-triggering one) — here's the evaluation report for Tolfenamic Acid, focused on the top-ranked predicted indication (headache disorder / migraine).

# Tolfenamic Acid: From Pain/Inflammation (NSAID) to Headache Disorder (Migraine)

## One-Sentence Summary

Tolfenamic acid is a fenamate-class NSAID historically used (as Clotam, in Nordic markets) for pain, inflammation, and acute migraine attacks, though it currently has no market authorization on file in Saudi Arabia. The TxGNN model predicts it may be effective for **Headache Disorder (Migraine)**, with **0 registered clinical trials** but **20 supporting publications**, largely reflecting a substantial body of historical Nordic RCT evidence from the 1970s–2000s rather than modern registered trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Saudi Arabia — no SFDA-approved indication on file. Internationally documented as an NSAID (fenamate class) for pain, inflammation, and acute migraine attacks |
| Predicted New Indication | Headache disorder (Migraine) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for tolfenamic acid is not yet available in our records (flagged as a High-severity data gap). Based on available literature, however, tolfenamic acid is a fenamate-class NSAID with a dual mechanism: it inhibits both cyclooxygenase (COX-1/2, blocking prostaglandin synthesis) and 5-lipoxygenase (blocking leukotriene synthesis). This dual inhibition distinguishes it from most conventional NSAIDs, which act on the COX pathway alone.

The relationship between the drug's established uses and the predicted new indication is close rather than distant: tolfenamic acid was already marketed decades ago (as Clotam) in Finland, Denmark, and other Nordic countries specifically for acute migraine treatment and migraine prophylaxis, alongside general anti-inflammatory/analgesic use. In markets such as Saudi Arabia where the drug is not currently registered, the TxGNN prediction effectively surfaces a well-precedented indication rather than a novel mechanistic leap.

Mechanistically, this is plausible because migraine attacks are associated with prostaglandin- and leukotriene-mediated vasodilation and neurogenic inflammation. Tolfenamic acid's combined COX/5-LOX inhibition directly targets both of these pathways, which may explain both its acute abortive effect and its modest prophylactic benefit reported in older crossover trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | Compared tolfenamic acid, caffeine, metoclopramide, and their combinations in acute migraine attacks |
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT (double-blind crossover) | Acta Neurol Scand | Tolfenamic acid (200/400 mg) vs paracetamol (500/1000 mg) in migraine without aura |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | RCT (crossover) | Acta Neurol Scand | Tolfenamic acid superior to placebo for migraine prophylaxis (attack frequency, duration, severity) |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT (three-arm) | Acta Neurol Scand | Tolfenamic acid and propranolol both significantly reduced migraine attacks vs placebo |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT (double-blind crossover) | Lancet | Tolfenamic acid as effective as ergotamine for migraine attacks, with fewer GI side effects |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT (randomized double-blind crossover) | Acta Neurol Scand | Tolfenamic acid vs propranolol for migraine prophylaxis in 76 patients |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT (randomized double-blind parallel) | Medicina (Kaunas) | Tolfenamic acid 300mg vs pizotifen 1.5mg for migraine prevention in 192 patients |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT (randomized double-blind parallel) | Headache | Tolfenamic acid rapid release comparable to oral sumatriptan for acute migraine |
| [6984358](https://pubmed.ncbi.nlm.nih.gov/6984358/) | 1982 | Clinical study | Cephalalgia | Tolfenamic acid combined with caffeine, metoclopramide, or pyridoxine as adjuncts in acute migraine |
| [6691890](https://pubmed.ncbi.nlm.nih.gov/6691890/) | 1984 | PK study | Br J Clin Pharmacol | Migraine attacks delay absorption of oral tolfenamic acid; metoclopramide's effect studied |

## Saudi Arabia Market Information

Tolfenamic acid is not currently marketed in Saudi Arabia — no market authorization records are on file (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A substantial body of older Nordic RCT evidence (8+ randomized controlled trials, 1979–2002) supports efficacy of tolfenamic acid in both acute and prophylactic migraine treatment, consistent with the L2 evidence level. However, the drug has no current SFDA/TFDA package insert, safety warning, or DDI data on file, and is not marketed in Saudi Arabia, so it cannot yet pass a full safety review.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed structured mechanism-of-action data from DrugBank — currently a High-severity data gap
- Drug interaction (DDI) profile, as none is currently on file
- Assessment of whether historical (pre-registry) RCT evidence meets current regulatory evidentiary standards, or whether a modern confirmatory trial is needed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

