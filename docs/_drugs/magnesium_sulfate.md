---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From No Registered Indication to Preeclampsia/Eclampsia

## One-Sentence Summary

> Magnesium sulfate (MgSO₄) currently has no marketing authorization or documented approved indication in Saudi Arabia.
> The TxGNN model assigns near-maximal confidence (**99.9992%**) to **Preeclampsia/Eclampsia**,
> an association backed by **50 clinical trials** and **20 publications**, including the landmark Magpie Trial and multiple completed Phase 2/3 RCTs — evidence that reflects MgSO4's globally established role as the WHO-recommended standard anticonvulsant, rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is not currently marketed in Saudi Arabia (no license/indication record) |
| Predicted New Indication | Preeclampsia/Eclampsia |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, magnesium sulfate acts as an NMDA-receptor antagonist with cerebral vasodilatory and anticonvulsant properties, and it is internationally recognized (WHO, ACOG, and other major guidelines) as the standard-of-care agent for preventing and treating seizures in preeclampsia and eclampsia.

Because this established indication is not reflected in the drug's `original_indications` or Saudi licensing records, the TxGNN prediction here functions less as a discovery of a *new* use and more as a confirmation of an *existing, well-documented* clinical role that has simply not been captured in the structured registry data.

The clinical trial and literature evidence — spanning dosing-regimen optimization (12h vs 24h, Pritchard regimen comparisons), large pragmatic trials (the CLIP cluster-RCT with n=87,500), and mechanistic/pharmacokinetic studies — consistently supports this indication, reinforcing that the mechanistic rationale is sound even though formal MOA documentation is currently a data gap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | Completed | 560 | Antenatal MgSO4 vs placebo in women at risk of preterm birth, assessing neuroprotection against cerebral palsy/death in preterm infants (MASP study) |
| [NCT01801410](https://clinicaltrials.gov/study/NCT01801410) | Phase 3 | Completed | 602 | Compared Foley balloon catheter vs oral misoprostol for labor induction in preeclamptic women receiving standard MgSO4 anticonvulsant therapy |
| [NCT01911494](https://clinicaltrials.gov/study/NCT01911494) | NA (cluster-RCT) | Completed | 87,500 | CLIP trial: community-level package of care, including MgSO4 protocols, for hypertensive disorders of pregnancy across multiple low-resource countries |
| [NCT03412552](https://clinicaltrials.gov/study/NCT03412552) | N/A | Completed | 1,238 | Risk analysis of ICU management, including MgSO4 seizure control, on maternal/fetal outcomes in severe preeclampsia/eclampsia |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1,114 | Multicenter RCT testing whether postpartum MgSO4 can be safely discontinued after ≥8 hours of pre-delivery treatment |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | RCT comparing 6-hour vs 24-hour postpartum MgSO4 duration when <8 hours given before delivery |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | NA | Completed | 114 | RCT comparing low-dose MgSO4 vs standard Pritchard regimen for seizure prevention/treatment in severe preeclampsia/eclampsia |
| [NCT06126068](https://clinicaltrials.gov/study/NCT06126068) | NA | Completed | 120 | RCT comparing loading-dose MgSO4 vs Pritchard regimen in a resource-poor Nigerian setting |
| [NCT04576364](https://clinicaltrials.gov/study/NCT04576364) | NA | Completed | 280 | RCT comparing 12-hour vs 24-hour postpartum MgSO4 duration to balance anticonvulsant efficacy against side-effect exposure |
| [NCT01030627](https://clinicaltrials.gov/study/NCT01030627) | Phase 4 | Completed | 85 | Pilot study of MgSO4 delivery via Springfusor pump for preeclampsia treatment in low-resource settings |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12576241](https://pubmed.ncbi.nlm.nih.gov/12576241/) | 2003 | RCT | Obstetrics and Gynecology | Livingston et al. RCT testing whether MgSO4 prevents disease progression in women with mild preeclampsia |
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS ONE | Randomized trial comparing Springfusor pump vs standard IM administration for MgSO4 acceptability in preeclampsia/eclampsia |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | Witlin & Sibai review of efficacy, benefits, and risks of MgSO4 seizure prophylaxis in preeclampsia/eclampsia |
| [41054655](https://pubmed.ncbi.nlm.nih.gov/41054655/) | 2025 | Review | Cureus | Consolidated review of MgSO4 pharmacology and clinical evidence across obstetric and pediatric emergency applications |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | Sibai's classic review establishing MgSO4 as the anticonvulsant of choice in preeclampsia-eclampsia |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Mechanistic review | Stroke | Analysis of MgSO4 action via relief of cerebral vasospasm in eclampsia |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | Belfort et al. on cerebral hemodynamics in preeclampsia and the rationale for MgSO4 use |
| [490496](https://pubmed.ncbi.nlm.nih.gov/490496/) | 1979 | Historical review | J Reprod Med | Pritchard's foundational paper establishing the MgSO4 dosing regimen still used today |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | Observational study | Biol Trace Elem Res | Incidence and risk factors for critical hypermagnesemia during MgSO4 therapy in severe preeclampsia |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | Review | Acta Obstet Gynecol Scand | Evaluation of interventions, including MgSO4 protocols, to reduce preeclampsia/eclampsia-related maternal mortality in low-income countries |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 2/3 RCTs and a very large pragmatic cluster trial (n=87,500), and MgSO4 is already a WHO-recognized standard-of-care anticonvulsant for preeclampsia/eclampsia globally. However, the drug has no current Saudi Arabia market authorization, and TFDA-equivalent safety labeling (warnings/contraindications) is a **Blocking** data gap.

**To proceed, the following is needed:**
- Official Saudi Arabia package insert / regulatory safety labeling (warnings and contraindications) — currently a Blocking gap
- Confirmed mechanism of action documentation from DrugBank or equivalent source — currently a High-severity gap
- Drug-drug interaction (DDI) data (current query status: not found)
- Formal regulatory pathway assessment for market entry, given the drug is not currently licensed in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

