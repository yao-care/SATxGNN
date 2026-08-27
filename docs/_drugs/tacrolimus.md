---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 594
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: From Organ Transplant Rejection to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor best known for preventing organ transplant rejection and, in its topical form (Protopic®), for treating atopic dermatitis. The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**, with **2 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap). Per general pharmacological knowledge: organ transplant rejection prophylaxis (systemic); atopic dermatitis (topical, Protopic®) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available in the evidence pack (data gap, severity: High). Based on known pharmacology, tacrolimus is a calcineurin inhibitor that suppresses T-cell activation and downregulates pro-inflammatory cytokine release (IL-2, IFN-γ, etc.). Its efficacy in preventing organ transplant rejection and in treating atopic dermatitis (topical formulation) is well established, and mechanistically it is plausible that this anti-inflammatory activity extends to other T-cell-mediated dermatoses.

Seborrheic dermatitis shares immunopathological features with atopic dermatitis: both involve a T-cell-driven inflammatory response, in the case of seborrheic dermatitis triggered in part by *Malassezia* yeast colonization. Because topical tacrolimus already has a mature safety and efficacy record from decades of use in atopic dermatitis, extending it to seborrheic dermatitis represents a comparatively low-risk, mechanistically grounded repurposing hypothesis rather than an entirely novel pharmacological application.

This rationale is directly supported by real-world evidence: topical tacrolimus (Protopic®) has already been studied in multiple completed Phase 3/4 trials specifically for facial seborrheic dermatitis maintenance therapy, indicating that clinical investigators independently arrived at the same mechanistic hypothesis well before this TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated 0.1% tacrolimus ointment as maintenance treatment for severe facial seborrheic dermatitis in adults, aiming to reduce relapse frequency and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed proactive (once/twice weekly) 0.1% tacrolimus ointment to maintain remission and reduce exacerbation incidence in adult facial seborrheic dermatitis |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter double-blind RCT comparing tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT | J Am Acad Dermatol | Single-blind RCT comparing hydrocortisone 1% vs. tacrolimus 0.1% ointment in adults with facial seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Ann Parasitol | Clinical trial (n=60) comparing sertaconazole 2% cream vs. tacrolimus 0.03% cream for seborrheic dermatitis |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative Trial | Indian J Dermatol Venereol Leprol | Compared 2-day oral itraconazole plus topical tacrolimus vs. topical tacrolimus alone for maintenance therapy in Vietnam |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort/Open-label | Ann Dermatol | Maintenance therapy with 0.1% tacrolimus ointment for facial seborrheic dermatitis, extending the proactive-treatment strategy proven in atopic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviewed pathophysiology, safety, and efficacy of topical calcineurin inhibitors as a corticosteroid-sparing option for seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Cochrane Network Meta-Analysis | Clin Exp Allergy | Cochrane NMA of topical anti-inflammatory treatments for eczema, comparing relative efficacy/safety across agent classes including calcineurin inhibitors |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label Pilot Study | J Am Acad Dermatol | Open-label pilot study (n=18): 61% of patients achieved complete clearance of seborrheic dermatitis within 28 days of 0.1% tacrolimus |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Early review of topical tacrolimus and pimecrolimus exploring off-label use in seborrheic dermatitis, psoriasis, lichen planus, and other dermatoses |

## Safety Considerations

Please refer to the package insert for safety information. TFDA-equivalent label warnings, contraindications, and drug-drug interaction data could not be retrieved for this candidate (query status: not found), and this gap is flagged as **Blocking** for safety pre-assessment.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3/4 trials plus a substantial literature base (including a direct head-to-head RCT vs. corticosteroid and vs. antifungal comparators) support tacrolimus's efficacy in facial seborrheic dermatitis, and the mechanistic rationale is strong given its established role in atopic dermatitis. However, the drug is currently unmarketed in Saudi Arabia and core safety documentation is missing.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert (warnings, contraindications) — currently a Blocking data gap preventing S1 safety pre-assessment
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Saudi Arabia market authorization pathway assessment, since the drug has zero existing local licenses
- Drug-drug interaction data (current query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

