---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed for HIV-1 infection. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV infection)**, but this direction is currently supported by only **1 publication** and **0 clinical trials** — and that single publication argues the mechanism likely does *not* transfer to FIV.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (well-established use; not captured in the Saudi Arabia registry data below since the drug is unmarketed there) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack. Based on general pharmacological knowledge, nevirapine is a first-generation NNRTI that works by binding a hydrophobic allosteric pocket unique to HIV-1 reverse transcriptase (RT), blocking viral replication non-competitively.

The predicted indication, feline immunodeficiency virus (FIV)-associated acquired immunodeficiency syndrome in cats, is superficially attractive because FIV is a lentivirus closely related to HIV and causes an analogous immune-deficiency syndrome. This is presumably why the TxGNN knowledge graph links nevirapine to this disease with a very high score.

However, the one available publication (PMID 38031646) directly undermines this rationale: it compares NNRTI binding across HIV and FIV reverse transcriptases and indicates that FIV RT lacks the pocket structure NNRTIs require, meaning nevirapine and related NNRTIs are expected to have little to no activity against FIV. The mechanistic plausibility here is therefore low, and the high TxGNN score most likely reflects a knowledge-graph co-occurrence pattern (antiretroviral ↔ lentivirus) rather than genuine pharmacological applicability. Additionally, this indication is veterinary rather than human, which is outside the typical scope of human drug repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Structural/biochemical comparison | Journal of Veterinary Science | Compared NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human RT to assess whether they could treat FIV; structural differences between FIV and HIV RT suggest NNRTIs are unlikely to be effective against FIV. |

## Saudi Arabia Market Information

Nevirapine is not currently marketed in Saudi Arabia (0 registered authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The sole piece of evidence for the top-ranked indication is a structural/biochemical comparison study that argues *against* nevirapine's efficacy in FIV (species-specific RT pocket mismatch), not a study supporting it — this is disconfirming rather than confirming evidence. The other two TxGNN-ranked candidates (SIV infection, and a rare neurodevelopmental disorder) are similarly unsupported: SIV evidence is dominated by unrelated in vitro/animal screening studies showing NNRTIs generally fail against wild-type SIV RT, and the neurodevelopmental disorder candidate has zero literature or trial support and no plausible mechanistic link.
- Separately, the TFDA/Saudi package insert warnings and contraindications data (DG001) are marked as a **Blocking** gap, meaning the candidate cannot proceed to safety pre-screening (S1) regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001 (package insert warnings/contraindications) before any S1 safety evaluation can begin
- Confirmed mechanism-of-action data (DG002) to properly assess biological plausibility
- Direct in vivo or in vitro efficacy data for nevirapine specifically against FIV (not just structural comparison) if this indication is to be pursued further
- Given the disconfirming nature of current evidence, re-ranking or deprioritizing this candidate in favor of other TxGNN predictions should be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

