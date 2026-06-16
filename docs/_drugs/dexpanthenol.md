---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dexpanthenol: From Topical Skin Care to Exanthem (Skin Rash)

## One-Sentence Summary

Dexpanthenol (provitamin B5, brand name Bepanthen®/Bepantol®) is a widely used topical agent known for its skin moisturizing, wound healing, and epithelial repair properties, though it carries no formally registered indication in Saudi Arabia.
The TxGNN model predicts it may be effective for **Exanthem (Skin Rash)** — the highest-actionability prediction in this candidate set — with **5 clinical trials including 1 completed Phase 3 RCT** directly evaluating Bepanthen® cream for skin eruption prevention.
Among all 7 predicted indications, exanthem is the only one with clinical trial evidence (Evidence Level L2), making it the primary candidate for further regulatory and clinical evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in Saudi Arabia (0 authorizations) |
| Predicted New Indication | Exanthem (Skin Rash) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, dexpanthenol is the alcohol analog of pantothenic acid (Vitamin B5) and serves as a direct precursor to Coenzyme A (CoA) in mammalian cells. It is the active ingredient in Bepanthen® (Bayer) and Bepantol® (Bayer), products widely used across dermatological and wound care applications globally.

Dexpanthenol's pharmacological effects are directly relevant to exanthem pathophysiology: it promotes keratinocyte proliferation, accelerates epidermal regeneration, sustains skin barrier hydration, and exerts anti-inflammatory effects on irritated tissue. When skin rash occurs — whether from drug toxicity, radiation, infection, or inflammation — the primary therapeutic need is rapid epithelial repair and barrier restoration, which maps precisely onto dexpanthenol's known mechanism. This is not a mechanistic stretch; the drug acts on the exact tissue type and cellular processes disrupted in exanthem.

Clinical precedent reinforces this reasoning. NCT01136005, a completed Phase 3 double-blind RCT enrolling 160 patients, directly tested Bepanthen® cream against Cetomacrogol cream for the preemptive prevention of papulopustular eruption in patients receiving EGFR inhibitor (EGFRI) therapy — one of the most clinically significant forms of drug-induced skin rash. This trial establishes a formal, high-quality clinical evidence base for dexpanthenol in rash management that goes beyond its traditional wound-healing use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Phase 3 double-blind RCT directly comparing Bepanthen® cream (dexpanthenol) vs. Cetomacrogol cream for preemptive prevention of ≥Grade 2 papulopustular eruption in EGFR inhibitor-treated patients; evaluated health-related quality of life (HRQoL) and adherence over 6-week skin treatment period — strongest direct evidence for dexpanthenol in skin rash |
| [NCT03852563](https://clinicaltrials.gov/study/NCT03852563) | N/A | Completed | 33 | Directly evaluated Bepantol® cream (dexpanthenol brand product) for skin recovery and reduction of skin rash following ablative laser dermatological procedures on the face; assessed redness, irritation, softness, and adverse effects over 3 weeks — provides direct dexpanthenol efficacy data in post-procedure rash recovery |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Evaluated topical imiquimod (5%, 0.05%, and nanoencapsulated formulations) for actinic cheilitis (potentially malignant lower lip lesion); dexpanthenol likely used as adjunct skin barrier care rather than primary study drug; trial terminated early, limiting citability |
| [NCT05699122](https://clinicaltrials.gov/study/NCT05699122) | N/A | Completed | 16 | Low-level laser therapy (LLLT) for incontinence-associated dermatitis (IAD) in elderly patients; dexpanthenol likely served as standard barrier care in the control arm; primary intervention was laser therapy, not dexpanthenol — indirect supporting role only |
| [NCT03866447](https://clinicaltrials.gov/study/NCT03866447) | Phase 4 | Unknown | 80 | Vitamin D and topical analogues for acne vulgaris; study drug is vitamin D derivatives, not dexpanthenol; connection to exanthem classification is uncertain; included due to knowledge-graph skin disease node clustering |

---

## Literature Evidence

Currently no related literature available for dexpanthenol in exanthem from the Evidence Pack database search.

---

## Saudi Arabia Market Information

Dexpanthenol currently has **no registered product authorizations** in Saudi Arabia. No licenses are on record as of the data cutoff date (2026-06-16).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT01136005, n=160) directly tested Bepanthen® cream for prevention of EGFRI-induced papulopustular skin eruption, and an additional completed trial (NCT03852563) evaluated Bepantol® cream for post-procedure skin rash recovery — both trials use branded dexpanthenol products as the primary study intervention, establishing L2-level evidence. The mechanistic basis (keratinocyte proliferation, epithelial regeneration, anti-inflammatory and barrier-restoration effects) aligns directly with exanthem pathophysiology.

**To proceed, the following is needed:**

- Obtain full published results from NCT01136005 (BeCet trial) to confirm primary efficacy outcomes and confirm the precise indication scope (EGFRI rash vs. broader exanthem classification)
- Conduct supplementary PubMed literature search to identify publications arising from NCT01136005 and NCT03852563
- Retrieve formal MOA documentation from DrugBank API to support mechanistic rationale section
- Obtain dexpanthenol package insert safety data (TFDA or EMA source) to complete contraindication and warning assessment
- Assess Saudi Arabia regulatory pathway for topical dexpanthenol product registration, including applicable dosage forms
- Evaluate route compatibility for the target indication (topical administration is expected; confirm if systemic formulations are relevant)
- Note for ophthalmology team: Punctate Epithelial Keratoconjunctivitis (rank 7, L4) is a secondary candidate of interest — Corneregel® 5% ophthalmic gel (dexpanthenol) is approved in Europe for corneal epithelial repair, warranting a dedicated literature search to characterize existing evidence before advancing to clinical trial discussion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

