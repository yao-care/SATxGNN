---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Congenital HIV Infection (Perinatal Transmission)

## One-Sentence Summary

Etravirine (DrugBank DB06414) is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally approved for treatment-experienced HIV-1 infection. Among TxGNN's top-ranked candidates, the two highest-scoring predictions (simian and feline immunodeficiency virus infection) are non-human veterinary disease entities with no supporting evidence and are excluded from this evaluation. The most clinically substantive prediction is **congenital/perinatal HIV infection**, supported by **13 clinical trials** and **1 publication**, representing a population extension of etravirine's existing antiretroviral indication rather than a novel mechanistic hypothesis.

> **Note on prediction selection:** TxGNN's rank 1–2 hits ("simian immunodeficiency virus infection," "feline acquired immunodeficiency syndrome") are animal-model disease ontology terms, not human indications — the evidence pack's own rationale flags them as lacking cross-species RT binding evidence. Rank 3 is a rare neurodevelopmental disorder with a purely speculative NRTI-class analogy (etravirine is an NNRTI) and zero supporting studies. This report therefore focuses on **rank 4 — congenital human immunodeficiency virus** — the highest-ranked prediction with actual clinical trial and literature support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in treatment-experienced patients (publicly known approved use; no Taiwan license record available — drug is not marketed locally) |
| Predicted New Indication | Congenital / perinatal HIV infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from the evidence pack is marked as a data gap (DG002, pending DrugBank API lookup). Based on the drug's known pharmacology and the repurposing rationale captured in this evidence pack, etravirine is an NNRTI that non-competitively binds HIV-1 reverse transcriptase to block viral replication, and is an already-approved antiretroviral agent.

Congenital/perinatal HIV infection is not a mechanistically distinct disease from etravirine's core indication — it is the same virus (HIV-1) in a different patient population (infants and children infected via mother-to-child transmission, and pregnant women being treated to prevent transmission). The mechanistic link is therefore direct rather than speculative: etravirine's RT-inhibition activity applies identically in this population, and the prediction represents a population/label extension rather than a novel biological hypothesis.

This is reflected in the supporting evidence: several trials and the one literature report directly address etravirine use in pregnant HIV-1-infected women and pediatric/perinatal contexts (e.g., PK studies, case reports on antiretroviral-experienced pregnant patients), rather than exploring an unrelated disease mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04630002](https://clinicaltrials.gov/study/NCT04630002) | Phase 1 | Completed | 54 | Direct etravirine drug-drug interaction study with darunavir/ritonavir and GSK3640254 in healthy adults |
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | Single-arm PK study of etravirine (alone or with darunavir/ritonavir or rilpivirine) specifically in HIV-1-infected **pregnant women** |
| [NCT01199731](https://clinicaltrials.gov/study/NCT01199731) | Phase 2b | Terminated | 30 | Open-label etravirine 200mg BID used as the control arm in NNRTI-resistant, treatment-experienced HIV-1 adults |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1578 | IMPAACT P1026s — PK of antiretroviral and TB drugs in pregnant and postpartum women and their infants |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | Switch to long-acting cabotegravir + rilpivirine from INI/NNRTI/PI-based regimens in virologically suppressed HIV-1 adults; drug arm not confirmed as etravirine |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Switch to dolutegravir + rilpivirine from current regimen in virologically suppressed HIV-1 adults; drug arm not confirmed |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | Same design as above (parallel study cohort); drug arm not confirmed |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3b | Active, not recruiting | 1049 | Long-acting cabotegravir + rilpivirine dosing interval (Q8W vs Q4W) in suppressed HIV-1 adults |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | Long-acting IM cabotegravir + rilpivirine for maintenance after switching from an integrase-inhibitor regimen |
| [NCT01458132](https://clinicaltrials.gov/study/NCT01458132) | N/A | Completed | 19 | GSK observational drug-exposure registry for long-term follow-up; possible etravirine-adjacent GSK/ViiV cohort, not confirmed |

Two additional registered records (NCT04273165, a Friedreich Ataxia trial flagged as a likely data-matching error, and NCT07412977, a not-yet-recruiting French pregnancy cohort with no drug specified) were excluded as not relevant to this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Review/Clinical Practice | Antiviral Therapy | Case report of darunavir and etravirine (with/without raltegravir) use in two highly treatment-experienced pregnant women, discussing management options where standard regimens are inadequate |

---

## Saudi Arabia Market Information

Etravirine is currently **not marketed in Taiwan** — no product licenses or authorization records exist in the evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are marked as data gaps in this evidence pack — TFDA package insert retrieval, DG001, is flagged as Blocking for safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Congenital/perinatal HIV represents a population extension of etravirine's already-approved mechanism, supported by direct pregnancy-specific PK and case-report data (L2 evidence) — this is fundamentally different in risk profile from the top TxGNN-ranked but non-human/unsupported predictions (SIV, FIV, rare neurodevelopmental disorder), which should be held with no further action.

**To proceed, the following is needed:**
- TFDA package insert retrieval (DG001, Blocking) — required before any S1 safety pre-screening can proceed
- DrugBank MOA confirmation (DG002)
- Confirmation of which switch/maintenance trials (NCT02951052, NCT02429791, NCT02422797, NCT03299049, NCT02938520, NCT01458132) actually included an etravirine treatment arm, since current grading only infers population relevance
- Pediatric/perinatal dosing and safety data specific to congenital HIV, since Taiwan has no existing marketing authorization or label to reference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

