---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 2
---

# Interferon Beta-1B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Interferon Beta-1b: From Not Marketed in Saudi Arabia to Hairy Cell Leukemia

## One-Sentence Summary

> Interferon Beta-1b (DrugBank DB00068) is not currently marketed in Saudi Arabia, so no approved original indication is on file in this evidence pack.
> The TxGNN model's top-ranked prediction is **Hairy Cell Leukemia**, supported by **0 clinical trials** and **4 publications** (all from 1987–1990).
> A second, much better-evidenced prediction — **Autoimmune Disease of the Central Nervous System** (i.e., multiple sclerosis) — is also present in this pack, backed by **24 clinical trials** and **19 publications**; this largely reflects the drug's globally established use as Betaferon®/Betaseron® rather than a novel hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Saudi Arabia (0 licenses on file) |
| Predicted New Indication | Hairy Cell Leukemia |
| TxGNN Prediction Score | 99.16% (rank 11,789) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the evidence pack. Based on general pharmacological class knowledge, Interferon Beta-1b is a Type I interferon with direct antiproliferative and immunomodulatory activity — a class effect shared with interferon alfa, which has documented efficacy in hairy cell leukemia.

The repurposing rationale extracted from the model output states: Type I interferons (including beta-ser/beta-1b) have direct antiproliferative and immunomodulatory effects on hairy cells, and were shown in the late 1980s to induce remission, mechanistically paralleling interferon alfa's established effect in this disease. However, this link is inferred indirectly from alfa-interferon class effects rather than from beta-1b-specific mechanistic evidence, and all supporting literature predates 1991 — well before modern targeted therapies (e.g., purine analogs, BRAF inhibitors) became standard of care for hairy cell leukemia.

Separately, this evidence pack also contains a second, much more substantially supported prediction — "autoimmune disease of central nervous system" — which corresponds to multiple sclerosis, the condition Interferon Beta-1b (Betaferon®/Betaseron®) is already approved for in many other countries. This is not a novel biological hypothesis so much as a reflection of the drug's known therapeutic identity; it is included below for completeness since it appears in the source data.

## Clinical Trial Evidence

Currently no related clinical trials registered for hairy cell leukemia.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Prospective Comparative Study (Phase 2-like) | Cancer | 10 HCL patients treated with recombinant beta-ser-interferon (90×10⁶ U SC TIW); 63% normalized peripheral counts, 25% partial hematologic improvement |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Case Series | American Journal of Hematology | 12 HCL patients treated with IV beta-ser interferon (90 million U TIW); most had 90–100% marrow hairy-cell involvement |
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Retrospective Cohort (institutional experience) | Leukemia | UCLA experience: 51 HCL patients on Type I interferons; 71% response rate in the beta-serine-interferon subgroup (early follow-up) |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Case Report | American Journal of Clinical Oncology | Beta-ser-interferon failure case rescued by deoxycoformycin; interferon is the prior-failed therapy, not the study drug |

## Additional Predicted Indication: Autoimmune Disease of the Central Nervous System (Multiple Sclerosis)

This second candidate ranks just below hairy cell leukemia (TxGNN score 99.02%, rank 13,377) but has substantially deeper evidence, largely because it mirrors Interferon Beta-1b's known real-world indication (Betaferon®/Betaseron® for MS) rather than a genuinely new hypothesis.

**Evidence Level:** L2 (a completed Phase 3 trial arm — the BENEFIT long-term extension — plus a completed Phase 2/3 RCT, supported by numerous completed Phase 2/4 studies and two Cochrane systematic reviews; the pack does not include the original pivotal placebo-controlled Phase 3 registration trial as a separately listed record, so L1's "≥2 completed Phase 3 RCTs" is not strictly confirmed from this data alone).

**Clinical Trial Evidence (top 10 of 24)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00185211](https://clinicaltrials.gov/study/NCT00185211) | Phase 3 | Completed | 468 | Long-term extension of the double-blind, placebo-controlled BENEFIT study; compares early vs. delayed IFN beta-1b initiation in CDMS/first demyelinating event |
| [NCT01795872](https://clinicaltrials.gov/study/NCT01795872) | Phase 4 | Completed | 278 | BENEFIT 11: 11-year follow-up on disability, cognition, and disease course after early vs. delayed IFN beta-1b |
| [NCT00893217](https://clinicaltrials.gov/study/NCT00893217) | Phase 2 | Completed | 71 | Double-blind RCT comparing Betaseron 500 mcg vs. 250 mcg SC every other day for safety/tolerability in RRMS |
| [NCT01432704](https://clinicaltrials.gov/study/NCT01432704) | Phase 2/3 | Completed | 70 | Double-blind, placebo-controlled RCT of oral vitamin D3 add-on to IFN beta-1b in MS |
| [NCT00202995](https://clinicaltrials.gov/study/NCT00202995) | Phase 4 | Terminated | 91 | Randomized comparison of Copaxone vs. high-dose interferon (Betaseron/Rebif) on relapse rates |
| [NCT01333501](https://clinicaltrials.gov/study/NCT01333501) | Phase 4 | Completed | 151 | Randomized, active-controlled pilot comparing fingolimod vs. IFN beta-1b on cognitive symptoms and brain atrophy in RRMS |
| [NCT01317004](https://clinicaltrials.gov/study/NCT01317004) | Phase 4 | Completed | 61 | Randomized, open-label comparison of fingolimod vs. prior DMT (incl. IFN beta-1b) on treatment satisfaction |
| [NCT01158183](https://clinicaltrials.gov/study/NCT01158183) | N/A | Completed | 226 | ROBUST: 12-month US real-world observational outcomes study of Betaseron in relapsing MS |
| [NCT00819000](https://clinicaltrials.gov/study/NCT00819000) | N/A | Completed | 2878 | TOP MS: large real-world study of MS disease management and treatment adherence/compliance |
| [NCT01111656](https://clinicaltrials.gov/study/NCT01111656) | Phase 2 | Completed | 28 | SWABIMS follow-up: atorvastatin 40mg add-on vs. IFN beta-1b monotherapy in RRMS |

**Literature Evidence (top 10 of 19)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38032059](https://pubmed.ncbi.nlm.nih.gov/38032059/) | 2023 | Systematic Review / Network Meta-analysis | Cochrane Database of Systematic Reviews | Comparative adverse-effect profile of MS immunotherapies including interferon beta |
| [25062935](https://pubmed.ncbi.nlm.nih.gov/25062935/) | 2014 | Systematic Review | Cochrane Database of Systematic Reviews | Interferons-beta vs. glatiramer acetate for relapsing-remitting MS |
| [11971121](https://pubmed.ncbi.nlm.nih.gov/11971121/) | 2002 | Review | Neurology | Mechanisms of action of interferons and glatiramer acetate in MS |
| [19707422](https://pubmed.ncbi.nlm.nih.gov/19707422/) | 2009 | Review | Biologics: Targets & Therapy | Review of IFN beta-1b efficacy in early and relapsing MS |
| [8808634](https://pubmed.ncbi.nlm.nih.gov/8808634/) | 1996 | Review | Clinical Immunology and Immunopathology | IFN beta-1b lessens MS attack frequency and MRI-assessed disease burden; immune-modulatory mechanism |
| [9007089](https://pubmed.ncbi.nlm.nih.gov/9007089/) | 1996 | Mechanistic Study | Annals of Neurology | IFN beta-1b inhibits gelatinase secretion and T-cell migration — proposed mechanism for clinical benefit |
| [15007120](https://pubmed.ncbi.nlm.nih.gov/15007120/) | 2004 | RCT Follow-up Analysis | Neurology | IFN beta-1b slows progression of brain atrophy over 3 years in RRMS |
| [16542163](https://pubmed.ncbi.nlm.nih.gov/16542163/) | 2006 | Observational Head-to-Head | Acta Neurologica Scandinavica | 6-year comparison of IFN beta-1a vs. beta-1b efficacy and safety |
| [25482255](https://pubmed.ncbi.nlm.nih.gov/25482255/) | 2014 | Review | Neurologia i Neurochirurgia Polska | Long-term (16–21 year) follow-up of the pivotal IFN beta-1b trial and effect on survival |
| [8069001](https://pubmed.ncbi.nlm.nih.gov/8069001/) | 1994 | Review | The Annals of Pharmacotherapy | Early pharmacology, efficacy, and dosing review of IFN beta-1b for RRMS |

## Saudi Arabia Market Information

Interferon Beta-1b is not currently marketed in Saudi Arabia — 0 authorizations are on file, and no license records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently available for this drug; the DDI query returned "not found.")

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (missing TFDA/local package insert) prevents entry into S1 safety pre-assessment, and the hairy cell leukemia evidence base consists only of small legacy studies from 1987–1990 with no contemporary trials (L3). The better-evidenced CNS autoimmune disease (MS) prediction largely reflects the drug's already-established use elsewhere rather than novel efficacy, and equally cannot proceed without local safety documentation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required to clear the S1 safety gate
- DrugBank-sourced mechanism of action data
- Drug interaction (DDI) data, currently unavailable
- If pursuing hairy cell leukemia: contemporary evidence (post-2000) given current standard-of-care has moved to purine analogs/targeted agents
- If pursuing the CNS autoimmune disease indication: clarify whether this should be pathwayed as a market-registration case (given established global approval as Betaferon®/Betaseron®) rather than a de novo repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

