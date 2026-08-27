---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 524
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Propranolol: From β-Blockade in Cardiovascular/Hepatic Disease to the Cardiomyopathy Spectrum

## One-Sentence Summary

Propranolol is a non-selective β-adrenergic blocker with established use in hypertension, arrhythmia, and (per the supporting literature in this pack) prevention of variceal bleeding in cirrhotic portal hypertension. TxGNN generated **6 predicted indications**, but only two — **cardiomyopathy** and **cirrhotic cardiomyopathy** — are backed by actual clinical trial or literature evidence; the other four (including the two highest TxGNN scores) have zero supporting records and are flagged by the model rationale itself as likely graph noise. The drug is **not currently marketed in Saudi Arabia**, so any next step also requires a market-entry decision, not just a clinical one.

> **Note on data completeness:** `original_moa` and `original_indications` are marked as Data Gaps in the evidence pack, and TFDA package-insert warnings/contraindications are also gaps. The mechanistic description below is reconstructed from the `repurposing_rationale` text embedded in the individual indication records, not from a dedicated MOA field.

---

## Quick Overview — All Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Distal myopathy, Tateyama type | 99.40% | L5 | S0 | Hold |
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | S0 | Hold |
| 3 | Hypertrophic cardiomyopathy due to intensive athletic training | 99.17% | L5 | S0 | Hold |
| 4 | Chondroma | 99.14% | L5 | S0 | Hold |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L3 | S1 | Research Question |
| 6 | Cardiomyopathy | 99.12% | L3 | S2 | **Proceed with Guardrails** |

| Item | Content |
|------|------|
| Original Indication | Not available (data gap in this pack) — literature references indicate established use in hypertension/arrhythmia and cirrhotic variceal bleeding prophylaxis |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Overall Recommended Decision | Proceed with Guardrails (cardiomyopathy), Research Question (cirrhotic cardiomyopathy), Hold (all others) |

**Why 4 of 6 candidates are excluded from further discussion:** Ranks 1–4 have identical evidence — zero clinical trials, zero literature, L5 (model-prediction-only). The rationale text for each explicitly calls these graph-embedding artifacts (e.g., rank 1's TIA1-related rare myopathy has "no known mechanistic overlap" with β-blockade; chondroma is "likely a false positive, unlike propranolol's established mechanism in infantile hemangioma"). These are not carried into the detailed sections below.

---

## Why is This Prediction Reasonable?

Detailed MOA data is not available in this pack (Data Gap). Based on the mechanistic notes embedded in the evidence records, propranolol is a **non-selective β1/β2-adrenergic receptor antagonist**. Its negative inotropic and negative chronotropic effects reduce myocardial contractility and heart rate, which is the established basis for its use in **hypertrophic obstructive cardiomyopathy (HOCM)** — reducing left ventricular outflow tract pressure gradients and improving symptoms. This is not a novel hypothesis but an extension of a long-standing clinical practice, reflected in decades of literature (earliest identified record from 1972).

For **cirrhotic cardiomyopathy**, the mechanistic link runs through propranolol's well-established role in portal hypertension management (variceal bleeding prophylaxis). The same β-blockade that lowers portal pressure also affects cardiac electrophysiology (QTc correction) and systemic hemodynamics — but the literature is explicitly two-sided: some studies show benefit (QTc correction), while others (e.g., PMID 32446716) raise safety concerns that non-selective β-blockers may impair circulatory homeostasis and renal function in patients with refractory ascites ("window hypothesis"). This bidirectionality is why this candidate sits at L3/S1 (Research Question) rather than further along.

The four excluded candidates (distal myopathy, congenital thin-filament myopathy, athletic hypertrophic cardiomyopathy, chondroma) have no comparable mechanistic story connecting β-adrenergic blockade to their pathology, and no trial or literature evidence — consistent with model noise rather than a genuine signal.

---

## Clinical Trial Evidence

### Cardiomyopathy (Rank 6)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Phase 4 | Enrolling by Invitation | 20 | N-of-1 trials testing whether stopping beta-blockers improves wellbeing in transthyretin cardiac amyloidosis (deprescribing study, not efficacy) |
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Phase 3 | Unknown | 90 | Propranolol + gabapentin for paroxysmal sympathetic hyperactivity after traumatic brain injury (not a cardiomyopathy indication; propranolol is adjunct) |
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Phase 4 | Completed | 9 | N-of-1 deprescribing trial of beta-blockers in HFpEF; reflects existing safety/functional data in heart failure, not new-indication efficacy |

### Cirrhotic Cardiomyopathy (Rank 5)

Currently no related clinical trials registered.

---

## Literature Evidence

### Cardiomyopathy (Rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Cohort | British Heart Journal | Combined nifedipine + propranolol superior to nifedipine alone in hypertrophic obstructive cardiomyopathy; reduced LV outflow pressure |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Cohort | British Heart Journal | Propranolol effects on myocardial oxygen consumption and hemodynamics in HOCM |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Cohort | European Heart Journal | Propranolol and verapamil effects on LV diastolic stiffness in HOCM |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Cohort | Journal of Cardiac Failure | Hemodynamic predictors of propranolol tolerance and long-term effects in dilated cardiomyopathy |
| [3189143](https://pubmed.ncbi.nlm.nih.gov/3189143/) | 1988 | Cohort | American Heart Journal | Acute hemodynamic comparison of pindolol vs propranolol in dilated cardiomyopathy |
| [3673167](https://pubmed.ncbi.nlm.nih.gov/3673167/) | 1987 | Cohort | Zeitschrift für Kardiologie | Combined nifedipine + propranolol in HOCM, 6–24 month follow-up |
| [2920304](https://pubmed.ncbi.nlm.nih.gov/2920304/) | 1989 | Cohort | Canadian Journal of Cardiology | Disopyramide + propranolol combination in HOCM |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Cohort | Cardiology | Propranolol vs disopyramide effects on LV function at rest/exercise in HOCM |
| [11300365](https://pubmed.ncbi.nlm.nih.gov/11300365/) | 2000 | Cohort | Cardiovascular Drugs and Therapy | Verapamil vs propranolol on coronary vasomotion response in symptomatic HOCM |
| [36104228](https://pubmed.ncbi.nlm.nih.gov/36104228/) | 2022 | Case Report | International Heart Journal | Low-dose propranolol + cibenzoline for infantile mitochondrial cardiomyopathy with LVOT stenosis |

*(9 additional cohort/review/case reports on propranolol in HOCM/dilated cardiomyopathy exist in the pack but are omitted here per the 10-record limit.)*

### Cirrhotic Cardiomyopathy (Rank 5)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25250684](https://pubmed.ncbi.nlm.nih.gov/25250684/) | 2015 | Cohort | J Pediatr Gastroenterol Nutr | Incidence and risk factors of cirrhotic cardiomyopathy in children with portal hypertension |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Cohort | Journal of Hepatology | Non-selective beta-blockers may impair circulatory homeostasis and renal function in refractory ascites — key safety signal |
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Cohort | Frontiers in Pharmacology | Propranolol corrects prolonged QT intervals in cirrhotic patients |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Cohort | PLoS ONE | Blunted cardiovascular response to propranolol correlates with cirrhosis severity |
| [15387011](https://pubmed.ncbi.nlm.nih.gov/15387011/) | 2004 | Cohort | Ugeskrift for Læger | QTc prolongation and electromechanical dyssynchrony in cirrhotic cardiomyopathy |

---

## Saudi Arabia Market Information

No marketing authorizations exist — `taiwan_regulatory.market_status` = **未上市 (Not marketed)**, `total_licenses` = 0, `licenses` = empty. Propranolol has no registered product record in this dataset for the Saudi market.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and `ddi` are all Data Gaps in this pack; TFDA insert parsing is a Blocking data gap per `DG001`.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for *cardiomyopathy*, specifically the HOCM subtype) · **Research Question** (for *cirrhotic cardiomyopathy*) · **Hold** (for the other 4 candidates)

**Rationale:**
- The HOCM literature is deep (10+ studies spanning 1972–2022) and consistent with a real, long-established clinical mechanism — this is closer to "already-known off-label use" than a novel discovery, so it can proceed with monitoring guardrails rather than a full new-indication workup.
- Cirrhotic cardiomyopathy has plausible mechanism and 5 supporting cohort studies, but the evidence is bidirectional (QTc benefit vs. hemodynamic/renal risk in refractory ascites), so it needs a defined research question before any guardrail-based deployment.
- The remaining 4 candidates (ranks 1–4) have no clinical trial or literature support and are explicitly flagged in their own rationale as likely graph-embedding noise; no further evaluation is warranted without new evidence.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking gap (`DG001`)
- Confirmed drug-level MOA and original indication list (currently Data Gap)
- Sub-type stratification for "cardiomyopathy" trials (HOCM vs. dilated vs. amyloid) before treating them as one evidence body
- A defined clinical question and risk-stratification criterion (e.g., ascites severity) before advancing cirrhotic cardiomyopathy past S1
- A market-entry assessment, since propranolol currently has zero authorizations in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

