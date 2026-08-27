---
layout: default
title: Viloxazine
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Viloxazine
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

# Viloxazine: From an Unlicensed Legacy Drug to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

> Viloxazine (DB09185) is not currently marketed in this jurisdiction, and no locally approved indication is on file.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)** —
> a prediction already validated abroad, since viloxazine ER (Qelbree®/SPN-812) received FDA approval for pediatric and adult ADHD in 2021.
> **14 clinical trials** and **20 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (0 local licenses; drug not marketed locally) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal MOA documentation for viloxazine is not yet on file (Data Gap DG002). However, the evidence pack's own mechanistic analysis indicates viloxazine is a selective norepinephrine reuptake inhibitor (NRI) with weak 5-HT2C antagonist / 5-HT2B agonist activity — a pharmacological profile that directly targets the prefrontal cortex noradrenergic/dopaminergic dysregulation implicated in ADHD pathology.

This is not a purely speculative model output: viloxazine extended-release (marketed as SPN-812/Qelbree®) already received FDA approval in 2021 for ADHD in children, adolescents, and adults, making this a **confirmed repurposing case** rather than an untested hypothesis. The TxGNN prediction here effectively recovers a real-world, regulator-validated indication.

The "未上市" (not marketed) status in this dataset reflects a **local regulatory gap**, not an evidence gap — viloxazine has simply not yet been registered or authorized in this market, despite having an established efficacy and safety record elsewhere.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03247556](https://clinicaltrials.gov/study/NCT03247556) | Phase 3 | Completed | 297 | Pivotal trial of viloxazine ER 400/600 mg in adolescents (12–17) with ADHD |
| [NCT03247517](https://clinicaltrials.gov/study/NCT03247517) | Phase 3 | Completed | 310 | Pivotal trial of viloxazine ER 200/400 mg in adolescents with ADHD |
| [NCT03247530](https://clinicaltrials.gov/study/NCT03247530) | Phase 3 | Completed | 477 | Pivotal trial of viloxazine ER 100/200 mg in children (6–11) with ADHD |
| [NCT03247543](https://clinicaltrials.gov/study/NCT03247543) | Phase 3 | Completed | 313 | Pivotal trial of viloxazine ER 200/400 mg (high dose) in children with ADHD |
| [NCT04016779](https://clinicaltrials.gov/study/NCT04016779) | Phase 3 | Completed | 374 | Randomized, double-blind, placebo-controlled flexible-dose trial in adults (18–65) with ADHD |
| [NCT02633527](https://clinicaltrials.gov/study/NCT02633527) | Phase 2 | Completed | 222 | Dose-ranging proof-of-concept study in children with ADHD, basis for Phase 3 design |
| [NCT04786990](https://clinicaltrials.gov/study/NCT04786990) | Phase 4 | Completed | 96 | Open-label safety trial of viloxazine combined with psychostimulants in children/adolescents |
| [NCT02736656](https://clinicaltrials.gov/study/NCT02736656) | Phase 3 | Active, not recruiting | 1400 | Long-term open-label extension study of safety/efficacy in pediatric ADHD |
| [NCT06185985](https://clinicaltrials.gov/study/NCT06185985) | Phase 4 | Completed | 161 | Decentralized real-world trial in adults with ADHD and mood symptoms |
| [NCT04143217](https://clinicaltrials.gov/study/NCT04143217) | Phase 3 | Completed | 159 | Long-term open-label extension study of safety/efficacy in adult ADHD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35896943](https://pubmed.ncbi.nlm.nih.gov/35896943/) | 2022 | RCT | CNS Drugs | Phase III RCT confirming efficacy and safety of viloxazine ER in adults with ADHD |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Cohort/Network Meta-analysis | Lancet Psychiatry | Comparative cardiovascular safety of ADHD medications across age groups |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | Systematic Review/Meta-analysis | CNS Drugs | Systematic review of nonstimulant medications, including viloxazine, for adult ADHD |
| [38137075](https://pubmed.ncbi.nlm.nih.gov/38137075/) | 2023 | Systematic Review/Meta-analysis | Brain Sciences | Efficacy and safety meta-analysis of SPN-812 (viloxazine ER) in children/adolescents |
| [35615643](https://pubmed.ncbi.nlm.nih.gov/35615643/) | 2022 | Systematic Review/Meta-analysis | J Cent Nerv Syst Dis | Systematic review and meta-analysis of RCTs on viloxazine for ADHD |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Bayesian Network Meta-analysis | J Psychiatr Res | Efficacy/safety of monoamine reuptake inhibitors (including viloxazine) in ADHD |
| [41123831](https://pubmed.ncbi.nlm.nih.gov/41123831/) | 2025 | Review | CNS Drugs | Review of viloxazine ER pharmacology and use in adult ADHD |
| [34975586](https://pubmed.ncbi.nlm.nih.gov/34975586/) | 2021 | Review | Frontiers in Psychiatry | Review of viloxazine's FDA approval basis: four Phase 3 studies in >1,000 pediatric patients |
| [36168642](https://pubmed.ncbi.nlm.nih.gov/36168642/) | 2022 | Review | Health Psychology Research | Review of viloxazine as a nonstimulant ADHD treatment option |
| [38502148](https://pubmed.ncbi.nlm.nih.gov/38502148/) | 2024 | Review | Expert Rev Neurother | Review of viloxazine ER as an emerging treatment for pediatric/adolescent ADHD |

---

## Saudi Arabia Market Information

No marketing authorizations are currently on file — viloxazine has 0 registered licenses and is not marketed in this jurisdiction, despite FDA approval in the United States (as Qelbree®/SPN-812) for the same predicted indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted ADHD indication is backed by an unusually strong evidence base — 5 completed pivotal Phase 3 RCTs plus multiple systematic reviews/meta-analyses — and is already an FDA-approved use (Qelbree®). The main barrier is not clinical evidence but the complete absence of local regulatory and safety documentation (0 licenses, no package insert data on file).

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings, contraindications, and DDI data (blocking gap DG001)
- Confirmed, sourced mechanism of action documentation (DG002)
- A local registration/market-entry assessment leveraging the existing FDA approval dossier for viloxazine ER
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

