---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
---

# Econazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Econazole: From Topical Antifungal Therapy to Vulvovaginal Candidiasis

## One-Sentence Summary

Econazole is a topical imidazole antifungal agent; because it is not currently marketed in Saudi Arabia (0 local licenses), no original indication text is recorded in this dataset. The TxGNN model returned seven candidate indications, but only one — **Vulvovaginal Candidiasis** — is backed by real-world evidence: **1 registered clinical trial** and **20 relevant publications**, including several head-to-head RCTs of econazole in this exact condition. The other six predictions (e.g., Majocchi granuloma, tinea profunda) currently have **no supporting trials or literature** and are model-only signals.

> **Note on candidate selection:** The Evidence Pack contains 7 TxGNN-ranked predictions. The top-ranked candidates by raw TxGNN score (Majocchi granuloma, ectothrix/endothrix infectious disease, tinea profunda) all scored ~99.97% but returned **zero** clinical trials or literature on targeted search — these are treated as low-confidence model artifacts (Evidence Level L5, decision stage S0, recommendation "Hold"). This report focuses on **Vulvovaginal Candidiasis** (rank 7, score 99.50%), which is the only candidate that reached decision stage S3 with Evidence Level L1. A summary of the lower-confidence candidates is provided in the Appendix for transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — econazole is not currently marketed in Saudi Arabia (no local license history in dataset) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.50% (rank 7854 in full model output) |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this dossier is not available (flagged as a High-severity data gap, DG002 — MOA not yet retrieved from DrugBank). Based on general pharmacological knowledge, econazole belongs to the **imidazole antifungal class**, which inhibits fungal lanosterol 14-α-demethylase, blocking ergosterol synthesis and disrupting the fungal cell membrane. This mechanism gives imidazoles broad activity against dermatophytes and *Candida* species, including *Candida albicans*, the predominant cause of vulvovaginal candidiasis.

Unlike the other candidates in this dataset (which rely on speculative extrapolation from econazole's antidermatophyte spectrum to anatomically or histologically distinct conditions such as Majocchi granuloma or tinea profunda), the link to vulvovaginal candidiasis is **direct rather than inferential**: econazole's anti-*Candida* activity is a core, well-documented part of its antifungal spectrum, and topical/vaginal econazole formulations have been used for decades in other markets for exactly this indication. In that sense, the TxGNN "prediction" for this indication is best understood as **confirming an already-established pharmacological use in a market where the drug is not yet registered**, rather than a novel mechanistic leap.

Because Saudi Arabia currently has zero licenses for econazole (market status: not marketed), the practical value of this prediction is primarily as a **market-entry / registration signal** — i.e., whether there is sufficient existing evidence to support a local marketing application for this indication — rather than as a discovery of a new pharmacological mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00915629](https://clinicaltrials.gov/study/NCT00915629) | N/A | Terminated | 134 | Tested the probiotic *Lactibiane Candisis 5M* for prevention of recurrent vulvovaginal candidiasis. Econazole was **not** the study drug — the trial only overlaps on disease population. Relevance graded "C" (low) and the trial was terminated before completion; it does not directly support econazole's efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7383476](https://pubmed.ncbi.nlm.nih.gov/7383476/) | 1980 | RCT | Obstetrics and Gynecology | Randomized comparison in 178 women: 1% econazole vaginal cream vs. 100 mg clotrimazole vaginal tablets, once daily × 7 days — comparable mycologic cure rates, low incidence of local adverse reactions in both arms. |
| [7820892](https://pubmed.ncbi.nlm.nih.gov/7820892/) | 1994 | RCT | The Ceylon Medical Journal | Double-blind comparative study of econazole vs. clotrimazole for vaginal candidiasis efficacy. |
| [984105](https://pubmed.ncbi.nlm.nih.gov/984105/) | 1976 | Multicentric Clinical Trial | American Journal of Obstetrics and Gynecology | Large multicentric study (996 women) of 150 mg econazole vaginal suppositories: 93.4% mycological cure rate, favorable tolerability across 30 lab safety variables. |
| [7428415](https://pubmed.ncbi.nlm.nih.gov/7428415/) | 1980 | Multicentric Comparative Trial | Current Medical Research and Opinion | 3-day therapy comparison: clotrimazole vaginal tablets vs. econazole ovules for vaginal candidiasis, follow-up at 1 and 4 weeks. |
| [2257961](https://pubmed.ncbi.nlm.nih.gov/2257961/) | 1990 | Randomized, Single-Blind Comparative Trial | The Journal of International Medical Research | Butoconazole nitrate cream (3-day) vs. econazole nitrate cream (7-day) in 75 patients with vulvovaginal candidiasis; comparable safety and efficacy profiles. |
| [18606589](https://pubmed.ncbi.nlm.nih.gov/18606589/) | 2008 | Clinical/Microbiological Study | Journal of Chemotherapy | Econazole-polycarbophil bioadhesive delivery system in 180 women — improved post-treatment negative culture rates vs. econazole alone, suggesting reduced recurrence potential. |
| [10821079](https://pubmed.ncbi.nlm.nih.gov/10821079/) | 2000 | Comparative Clinical Study | West African Journal of Medicine | Triple-arm comparison of econazole nitrate, miconazole, and nystatin vaginal tablets in 75 patients; econazole showed comparable antifungal action at 4-week follow-up. |
| [98315](https://pubmed.ncbi.nlm.nih.gov/98315/) | 1978 | Review | Drugs | Foundational review of econazole's antifungal activity and therapeutic efficacy, including topical dermatomycoses and vaginal use. |
| [6963163](https://pubmed.ncbi.nlm.nih.gov/6963163/) | 1982 | Review | Australian & New Zealand Journal of Obstetrics & Gynaecology | Review of 6 treatment regimens for vulvovaginal candidiasis and recurrence rates, contextualizing imidazole antifungal therapy including econazole. |
| [25442913](https://pubmed.ncbi.nlm.nih.gov/25442913/) | 2014 | In Vitro Susceptibility Study | Journal de Mycologie Médicale | In vitro susceptibility of 200 recent *Candida* clinical isolates to topical imidazoles (clotrimazole, miconazole, econazole) and nystatin — relevant to current resistance patterns. |

---

## Saudi Arabia Market Information

Econazole is currently **not marketed in Saudi Arabia** — the dataset shows 0 total licenses and no license records. There is no existing local product to reference for original indication text or authorized dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings, contraindications, and drug interaction data for econazole are not yet available in this dataset (a Blocking-severity data gap), which currently prevents progression to the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical RCTs and multicentric comparative trials (1976–2008) consistently demonstrate econazole's efficacy for vulvovaginal candidiasis, comparable to other established imidazole antifungals (clotrimazole, miconazole, butoconazole). This is Evidence Level L1, the strongest of all seven candidates evaluated. However, econazole has no current market presence or safety labeling on file in Saudi Arabia, so registration-relevant safety documentation must be secured before advancing further.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Local drug interaction (DDI) database query, since the current query returned "not found"
- Assessment of local registration pathway given zero existing Saudi Arabia licenses for this drug

---

## Appendix: Other TxGNN-Predicted Indications (Lower Confidence, Not Analyzed Further)

These candidates scored highest by raw TxGNN rank but returned no supporting clinical trials or literature on targeted search, and are held at decision stage S0 pending further evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Majocchi granuloma | 99.97% | L5 | Hold | No trials/literature; deep follicular infection unlikely to respond to topical therapy alone |
| 2 | Ectothrix infectious disease | 99.97% | L5 | Hold | Pathology classification term, not a discrete clinical indication; no evidence found |
| 3 | Endothrix infectious disease | 99.97% | L5 | Hold | Same as above; mechanism-only inference |
| 4 | Superficial mycosis | 99.97% | L3 | Research Question | 19 literature hits found, but all concern related imidazoles (sertaconazole, bifonazole, etc.) rather than econazole-specific trial data |
| 5 | Dermatophytosis of scalp or beard | 99.97% | L5 | Hold | All 20 retrieved publications were false-positive keyword matches (beard transplantation, unrelated topics) — no usable evidence |
| 6 | Tinea profunda | 99.96% | L5 | Hold | No trials/literature; topical penetration likely insufficient for deep dermatophyte infection |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

