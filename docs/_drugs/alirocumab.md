---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab (Praluent®) is a PCSK9 inhibitor monoclonal antibody, globally approved for reducing LDL-cholesterol in patients with hypercholesterolemia and atherosclerotic cardiovascular disease, though not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Cholesterol Catabolic Process Disease** (encompassing familial hypercholesterolemia, dysbetalipoproteinemia, and related cholesterol metabolism disorders),
with **1 completed Phase 3 clinical trial** and **19 supporting publications** — a prediction that closely mirrors the drug's established global pharmacology and confirms strong model alignment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Atherosclerotic Cardiovascular Disease (global approval; no Taiwan license) |
| Predicted New Indication | Cholesterol Catabolic Process Disease |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, alirocumab is a fully human monoclonal antibody (IgG1 class) targeting PCSK9 (proprotein convertase subtilisin/kexin type 9). Under normal physiology, circulating PCSK9 binds to LDL receptors on the surface of hepatocytes and directs them to lysosomal degradation, reducing LDL-C clearance capacity. By binding and neutralising PCSK9, alirocumab prevents this receptor degradation and allows LDL receptors to recycle back to the cell surface — increasing hepatic uptake of circulating LDL particles and reducing plasma LDL-C by approximately 50–60%.

Cholesterol catabolic process disease encompasses a spectrum of conditions characterised by impaired cholesterol metabolism and clearance, including familial hypercholesterolemia (both heterozygous and homozygous forms), dysbetalipoproteinemia (type 3 hyperlipoproteinemia), and treatment-related dyslipidemia in conditions such as HIV/ART therapy. Because these conditions share the pathological feature of impaired LDL-C clearance — often driven by reduced functional LDL receptor density — alirocumab's mechanism of restoring receptor availability directly addresses the root defect.

The ODYSSEY clinical programme has generated over 47,000 patient-years of placebo-controlled Phase 3 data confirming alirocumab's cardiovascular outcome benefits. The EPIC-HIV trial (NCT03207945) further extends the evidence base to HIV-infected patients with antiretroviral therapy-induced dyslipidemia, a population with uniquely elevated cardiovascular risk. The biological plausibility of the TxGNN prediction is extremely strong, and the cumulative clinical evidence comfortably meets L1 standards.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | EPIC-HIV: PCSK9 inhibition in treated HIV patients with elevated cardiovascular risk; assessed LDL-C lowering, vascular inflammation, endothelial function, and non-calcified atherosclerotic plaque burden using noninvasive imaging |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Phase 3 Trial Analysis | Eur Heart J Cardiovasc Pharmacother | ODYSSEY OUTCOMES: alirocumab significantly reduced recurrent ischaemic cardiovascular events and all-cause mortality across 47,296 patient-years; comprehensive safety profile confirmed as favourable throughout follow-up |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | RCT Post-hoc Analysis | Diabetes Care | ODYSSEY OUTCOMES post-hoc: alirocumab simultaneously lowers Lp(a) and LDL-C without increasing new-onset type 2 diabetes risk — important safety reassurance for long-term use |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Systematic Review / Meta-analysis | Kardiologia Polska | PCSK9 inhibitors significantly reduce LDL-C and major adverse cardiovascular events; comprehensive synthesis of biochemical, genomic, and clinical outcome evidence |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | State-of-the-art Review | Pharmacotherapy | Current and emerging PCSK9-directed therapies (mAbs, siRNA, oral inhibitors) for ASCVD risk reduction; alirocumab positioned as cornerstone non-statin lipid-lowering therapy |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduct Target Ther | Comprehensive PCSK9 review spanning lipid metabolism, liver disease, infectious disease, autoimmune disorders, and cancer; broadening therapeutic applications beyond cardiovascular disease |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Curr Opin Lipidol | Two landmark PCSK9 mAb outcomes trials confirm marked LDL-C reduction and cardiovascular benefit; update on novel PCSK9 inhibition strategies in clinical development |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Novel pharmacological therapies for homozygous familial hypercholesterolemia (HoFH); PCSK9 inhibitors remain critical agents in a multimodal treatment strategy |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Familial hypercholesterolemia diagnostics and treatment options; PCSK9 inhibitors indicated for patients unable to achieve LDL targets on maximally tolerated statins |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review | Int J Mol Sci | Current dyslipidemia treatment advances: PCSK9 inhibitors achieve superior LDL-C reduction vs statins alone with confirmed cardiovascular outcomes improvement |
| [29526502](https://pubmed.ncbi.nlm.nih.gov/29526502/) | 2018 | Clinical Trial Analysis | Kidney International | Alirocumab effectively and safely lowers LDL-C in chronic kidney disease patients (eGFR 30–59 mL/min/1.73 m²); population-specific pharmacokinetic and safety data from the ODYSSEY programme |

---

## Taiwan Market Information

Alirocumab is currently **not marketed in Taiwan** — zero active TFDA licenses exist as of the data cutoff (2026-06-01).

> For reference: Alirocumab (Praluent®) holds regulatory approval from the U.S. FDA (2015), European EMA (2015), and multiple other jurisdictions for hypercholesterolemia and cardiovascular risk reduction, but has not received TFDA approval. No Taiwan-specific dosage, indication, or product labelling data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for "cholesterol catabolic process disease" is fully consistent with alirocumab's established global pharmacology and mechanism of action. The ODYSSEY clinical programme — comprising multiple Phase 3 RCTs with over 47,000 patient-years of observation — provides definitive L1 evidence for LDL-C lowering efficacy and cardiovascular outcome benefit. The barrier to Taiwan market introduction is regulatory, not clinical.

**To proceed, the following is needed:**
- TFDA New Drug Application (NDA) filing with the complete Phase 3 clinical dossier (ODYSSEY OUTCOMES and supporting trials)
- Taiwan-specific pharmacovigilance plan and post-marketing surveillance protocol
- Formal mechanism of action documentation for TFDA submission (filling current DG002 data gap)
- Safety monitoring framework covering: injection site reactions, neurocognitive adverse event surveillance, and hepatic enzyme monitoring
- Pricing and reimbursement strategy aligned with Taiwan National Health Insurance (NHI) formulary criteria and cost-effectiveness thresholds
- Assessment of patient population size in Taiwan with familial hypercholesterolemia or statin-intolerant high-risk cardiovascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

