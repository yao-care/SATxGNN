---
layout: default
title: Prednisolone
parent: 僅模型預測 (L5)
nav_order: 517
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone: From Inflammatory/Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Prednisolone is a well-established systemic glucocorticoid used broadly across inflammatory and autoimmune conditions, though this evidence pack has no recorded original-indication text or MOA data on file. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **18 clinical trials retrieved** (2 judged directly relevant after manual screening) and **20 publications** — including one placebo-controlled RCT — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no `original_indications` entries; general corticosteroid anti-inflammatory/immunosuppressive use per known pharmacology) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known pharmacology, prednisolone is a synthetic glucocorticoid that binds the glucocorticoid receptor to suppress pro-inflammatory cytokine production and T-cell–mediated immune responses — the basis for its broad use across inflammatory and autoimmune disease.

Alopecia areata (AA) is now understood as a T-cell–mediated autoimmune disease in which loss of the hair follicle's immune privilege allows CD8+ T-cell infiltration around the follicle bulb. Because systemic corticosteroids suppress exactly this kind of T-cell–driven autoimmune inflammation, oral pulse corticosteroid therapy — including methylprednisolone/prednisolone regimens — is already an established (if second-line) clinical option for severe or treatment-resistant AA, documented across case series, retrospective cohorts, and one placebo-controlled RCT.

This means the TxGNN hit is less a "novel" repurposing hypothesis and more a **validation signal**: the model correctly recovered an indication where corticosteroid pulse therapy already has real-world clinical precedent. Note also that the clinical-trial evidence returned by the search includes a large amount of noise — most of the 18 trials retrieved are unrelated Phase 2/3 SLE trials of other investigational drugs (IL-2 mutein, anti-ILT7 antibody, baricitinib, sirolimus, etc.) that were manually excluded as irrelevant; only trials directly involving corticosteroid pulse therapy in AA were retained below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone (higher dose, more frequent pulses) in patients with severe, treatment-resistant AA, testing whether higher-intensity pulse dosing overcomes prior treatment failure. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (Observational) | Completed | 296 | Safety/effectiveness study of tofacitinib in alopecia; participants received tofacitinib with or without adjuvant prednisolone. |

*Note: 16 additional trials were retrieved by the search but excluded — they involve unrelated investigational drugs (e.g. efavaleukin alfa, ALPN‑101, VIB7734, baricitinib, sirolimus) tested in systemic lupus erythematosus, not prednisolone in alopecia areata.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT (placebo-controlled) | J Am Acad Dermatol | First randomized, double-blind, placebo-controlled trial of oral pulse prednisolone in AA — the controlled efficacy anchor for this indication. |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Compares immunosuppressants, hair growth stimulants, and contact immunotherapy (including corticosteroids) across AA treatments. |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic Review | Australas J Dermatol | Systematic review of RCT evidence for systemic AA treatments, including corticosteroids. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, and adverse effects of different corticosteroid pulse regimens in AA. |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatol Ther | Methylprednisolone alone vs. methylprednisolone + methotrexate in 26 patients with extensive AA; combination not clearly superior to monotherapy. |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Clinical Study | Dermatoendocrinol | Medium-dose prednisolone pulse therapy effective in early-stage AA; significant steroid side effects can lead to discontinuation. |
| [36681881](https://pubmed.ncbi.nlm.nih.gov/36681881/) | 2023 | Retrospective Cohort | J Eur Acad Dermatol Venereol | French retrospective cohort on long-term patient-reported experience of methylprednisolone pulse ± methotrexate in AA. |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Retrospective Study | J Eur Acad Dermatol Venereol | Continuation rates of steroid-sparing agents (azathioprine/methotrexate/cyclosporine) following corticosteroid therapy in 138 chronic AA patients. |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Case Series | J Dtsch Dermatol Ges | Sequential high- then low-dose systemic corticosteroid regimen in severe childhood AA; rapid response but relapse common after discontinuation. |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Case Series | J Dermatolog Treat | Combination cyclosporine + methylprednisolone pulse therapy in severe/chronic AA. |

---

## Saudi Arabia Market Information

Currently no marketed authorization records for prednisolone in Saudi Arabia (0 licenses on file, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — TFDA/Saudi package insert warnings and contraindications are flagged as a **Blocking** severity gap that must be resolved before any safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 4 trial and one placebo-controlled RCT, backed by multiple retrospective cohorts and case series, support corticosteroid pulse therapy (methylprednisolone/prednisolone) as an existing clinical option for severe/treatment-resistant alopecia areata — this is a validation of known off-label practice rather than a purely novel hypothesis. However, the drug is not currently marketed in Saudi Arabia and core safety documentation is entirely missing.

**To proceed, the following is needed:**
- TFDA/Saudi package insert data — warnings, contraindications, drug interactions (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-severity gap, DG002)
- Saudi Arabia market registration status, given 0 current licenses
- Harmonized pulse-dosing protocol, since regimens vary considerably across the cited studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

