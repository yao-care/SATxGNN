---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 9
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster (VZV Infection) to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is the oral prodrug of penciclovir, an antiviral established for varicella-zoster virus (VZV) infections such as herpes zoster and chickenpox. The TxGNN model's top-ranked new-indication prediction is **Post-Infectious Neuralgia** (score 99.75%), but the two identified clinical trials test pain-management interventions during acute herpes zoster rather than famciclovir itself, and **no supporting literature** was retrieved — the signal is currently mechanistic/indirect only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes Zoster / VZV infection (inferred from repurposing rationale; formal Taiwan license text unavailable — see note below) |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> Note: `taiwan_regulatory.licenses` and `drug.original_indications` are both empty in this evidence pack — famciclovir is not currently marketed in Taiwan, so no local approved-indication text exists. The "Original Indication" above is drawn from the drug's own repurposing-rationale text (VZV/herpes zoster), not from a formal license record.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`drug.original_moa`) is flagged as a data gap (DG002, High severity, not yet confirmed via a direct DrugBank query). Based on the mechanistic reasoning embedded in this evidence pack, famciclovir is the prodrug of penciclovir: it is phosphorylated by virus-specific thymidine kinase into penciclovir triphosphate, which inhibits VZV/HSV DNA polymerase and blocks viral replication. Its established core use is treatment of VZV infections (herpes zoster and, in some formulations, chickenpox).

Post-infectious neuralgia — specifically postherpetic neuralgia (PHN) — is a well-recognized complication of herpes zoster, arising from VZV-induced nerve damage during the acute infection. Because famciclovir shortens the acute VZV disease course, there is a plausible mechanistic pathway by which earlier/adequate antiviral treatment could reduce the incidence or severity of PHN. However, the two trials surfaced by this search do not test famciclovir directly — they evaluate oxycodone and nerve-block/radiofrequency techniques for zoster-associated pain — so this remains a research hypothesis rather than a demonstrated repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Tests early oxycodone use during acute herpes zoster to prevent PHN; does **not** test famciclovir — indirect population overlap only (Grade C). |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not Yet Recruiting | 120 | Evaluates multimodal nerve block and pulsed radiofrequency for acute herpes zoster pain; non-antiviral intervention, does not evaluate famciclovir (Grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Famciclovir is currently **not marketed** in Taiwan (0 licenses on record). The TFDA package-insert warnings/contraindications lookup (DG001) is flagged as a **Blocking** data gap, meaning a formal safety pre-assessment (S1) cannot proceed until this is resolved.

---

## Other TxGNN-Predicted Indications Screened

This evidence pack screened 9 candidate indications for famciclovir. For context, the remaining 8 are summarized below:

| Rank | Disease | Evidence Level | Recommendation | Note |
|------|---------|----------------|-----------------|------|
| 2 | Sequela of COVID-19 | L5 | Hold | No mechanistic plausibility (famciclovir has no known anti-SARS-CoV-2 activity); only literature hit is an unrelated herpes-zoster formulation study — assessed as a TxGNN false positive. |
| 3 | Hepatitis C-induced liver cirrhosis | L5 | Hold | HCV replication does not depend on viral thymidine kinase; literature hit is a general HBV/HCV review that does not discuss famciclovir — assessed as a false positive. |
| 4 | Malignant pleural mesothelioma | L5 | Hold | No trials, no literature, no known mechanism — assessed as a TxGNN embedding false positive. |
| 5 | AIDS-related disorder | **L3** | Research Question | HIV/AIDS patients commonly develop opportunistic HSV/VZV/HHV-8 infections that famciclovir is pharmacologically suited to treat; 6 supporting papers (incl. one cohort study), but none is a dedicated RCT for this broad disease label. |
| 6 | Malignant epithelioid mesothelioma | L5 | Hold | No trials, no literature — assessed as a false positive. |
| 7 | Chickenpox | **L1** | Proceed with Guardrails | Strongest evidence in the pack (a completed Phase 3 RCT vs. aciclovir, a pediatric Phase 3 PK/safety study, 20 literature hits) — but this reflects famciclovir's existing core VZV indication, not a genuinely novel repurposing target. |
| 8 | Sarcomatoid mesothelioma | L5 | Hold | No trials, no literature — assessed as a false positive. |
| 9 | Malignant visceral pleura tumor | L5 | Hold | No trials, no literature — assessed as a false positive. |

Six of the nine candidates (all mesothelioma variants, HCV cirrhosis, and COVID-19 sequela) are explicitly judged in this evidence pack as mechanistically implausible TxGNN false positives. Only three carry genuine signal: post-infectious neuralgia (headline candidate above, L4), AIDS-related disorder (L3, worth a separate research track), and chickenpox (L1, but represents label extension of an existing use rather than repurposing).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package-insert warnings/contraindications lookup is currently a Blocking data gap — DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate indication (post-infectious neuralgia) has a plausible mechanistic rationale but no trial or literature evidence that directly tests famciclovir against this outcome — both available trials study non-antiviral interventions in the same patient population. Combined with the Blocking safety data gap (TFDA package insert unavailable) and famciclovir being unmarketed in Taiwan, this candidate is not ready to advance past a research question.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA package insert warnings/contraindications) — currently Blocking
- Resolve DG002 (confirmed MOA via direct DrugBank API query)
- A dedicated trial or observational study testing famciclovir specifically for PHN prevention/reduction (vs. current indirect pain-management trials)
- Separate evaluation of the AIDS-related-disorder track (L3, rank 5), which has stronger literature support and may merit its own research pathway
- Regulatory/market-entry assessment if any candidate advances, given famciclovir currently has zero licenses in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

