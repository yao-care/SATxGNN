---
layout: default
title: Zalcitabine
parent: 僅模型預測 (L5)
nav_order: 671
evidence_level: L5
indication_count: 3
---

# Zalcitabine
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

Using the report template above (no additional skill applies — this is a direct content-generation task with the format fully specified in the prompt). I'll flag one substantive issue before the table: the evidence pack's top-ranked prediction is a **veterinary** disease (feline AIDS), not a human indication, which materially changes the "reasonableness" and decision framing — I've called this out explicitly rather than glossing over it.

# Zalcitabine: From HIV/AIDS to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Zalcitabine (ddC) is a nucleoside reverse transcriptase inhibitor (NRTI) historically developed for HIV/AIDS treatment. The TxGNN model's top prediction is **Feline Acquired Immunodeficiency Syndrome** — a veterinary disease in cats, not a human indication — supported by **1 clinical trial** (unrelated drug/species, low relevance) and **8 publications**, all animal or in vitro studies. Because the predicted indication itself is non-human, this candidate is not directly actionable for human drug repurposing despite the high TxGNN score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS (HIV-1 infection) — general drug classification knowledge; not present in the evidence pack's regulatory data (drug is unmarketed, 0 licenses on file) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (veterinary indication) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in DrugBank sourcing). Based on known information, zalcitabine (ddC) is a nucleoside reverse transcriptase inhibitor used for HIV/AIDS treatment; its antiretroviral efficacy against HIV-1 has been established, and mechanistically the same reverse-transcriptase-inhibition activity is plausible against other retroviruses.

Feline immunodeficiency virus (FIV) and feline leukemia virus (FeLV) are lentiviruses/retroviruses that cause an AIDS-like disease in cats, and their reverse transcriptase is a validated target for the same class of nucleoside analogues (AZT, 3TC/lamivudine) used in HIV. This cross-species mechanistic parallel is almost certainly what TxGNN is capturing, and two of the cited studies (PMID 2544137, PMID 2540111) do test ddC directly in feline retroviral models.

**Important caveat:** the predicted indication is a veterinary disease, not a human one. Even with a mechanistically sound rationale, this specific prediction cannot translate into a human clinical indication — its value is limited to confirming that zalcitabine's NRTI activity generalizes across retroviruses (a pattern also seen in the rank 2 prediction, simian immunodeficiency virus infection, an animal-model disease in macaques). Neither prediction currently points to an actionable new human indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared boosted darunavir + lamivudine vs. boosted darunavir + emtricitabine/tenofovir in ARV-naïve HIV-1 patients. **Low relevance**: tests darunavir/lamivudine, not zalcitabine, in humans, not cats — same broad antiretroviral field only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Review | Vet Immunol Immunopathol | Reviews AZT/3TC efficacy against FIV infection in vitro and in vivo |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort | J Feline Med Surg | Long-term antiretroviral therapy (AZT) follow-up in FIV-infected cats over 5–6 years |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort | Viruses | Compared ZDV, ZDV+IFN-α, ZDV+3TC, ZDV+valproic acid protocols in naturally FIV-infected cats |
| [2540109](https://pubmed.ncbi.nlm.nih.gov/2540109/) | 1989 | Animal | Intervirology | FeLV-FAIDS model established for evaluating antiretroviral therapy in cats |
| [2544137](https://pubmed.ncbi.nlm.nih.gov/2544137/) | 1989 | Animal | Antiviral Research | **Zalcitabine (ddC) directly tested** — controlled-release capsular implant in FeLV-FAIDS cats |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Animal | Antiviral Research | ZDV+3TC+abacavir combination suppresses FIV replication in vitro |
| [2540111](https://pubmed.ncbi.nlm.nih.gov/2540111/) | 1989 | Animal | Intervirology | **Zalcitabine (ddC) directly tested** — nucleoside analogues (AZT, ddC, ddI, ddA) evaluated against FeLV in vitro and in FeLV-infected cats |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | Am J Vet Res | Characterized FIV-pPPR clone and 3TC-resistant mutants; nucleoside analogue susceptibility profiling |

Only two of the eight publications (PMID 2544137, 2540111) test zalcitabine itself; the remainder use related NRTIs (AZT/3TC/abacavir) as mechanistic analogues.

## Saudi Arabia Market Information

Zalcitabine is not marketed in Saudi Arabia — 0 authorizations are on file, so no product table can be produced.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in the current evidence pack; DDI lookup returned "not found.")

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 predicted indication (feline AIDS) is a veterinary, not human, disease — it cannot be pursued as a human repurposing candidate regardless of evidence strength. The rank-2 prediction (SIV) is likewise a non-human animal-model disease, and rank-3 has no supporting evidence at all (likely model noise).
- All available evidence for the top prediction is preclinical (animal/in vitro/cohort in cats); the one registered clinical trial is unrelated (different drug, different species).
- A Blocking-severity data gap exists on TFDA/SFDA package insert data (warnings, contraindications), which must be resolved before this candidate can even enter S1 safety screening.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the SFDA package insert for warnings/contraindications before any S1 safety evaluation
- Resolve DG002 (High): confirm mechanism of action via DrugBank API
- Re-run the TxGNN/evidence pipeline filtered to human-only disease ontologies, since the current top 3 predictions are either veterinary (feline AIDS), an animal-model-only disease (SIV), or unsupported (rare pediatric neurodevelopmental disorder)
- Re-query DDI database (current status: not found)
- Verify zalcitabine's current global regulatory status, since it is a legacy antiretroviral largely withdrawn from major markets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

