---
layout: default
title: Luliconazole
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 7
---

# Luliconazole
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

# Luliconazole: From Dermatophytosis (Tinea Infections) to Pityriasis Versicolor

## One-Sentence Summary

Luliconazole is a topical imidazole-class antifungal internationally established for treating dermatophytosis and other superficial fungal infections; it is not currently marketed in Saudi Arabia. The TxGNN model predicts it may also be effective for **Pityriasis Versicolor**, with **1 clinical trial** and **3 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophytosis / tinea infections (topical antifungal; no Saudi Arabia license on file) |
| Predicted New Indication | Pityriasis versicolor |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known information, luliconazole is a topical imidazole-class antifungal that inhibits fungal sterol 14-α-demethylase, an enzyme required for ergosterol synthesis in the fungal cell membrane. Its efficacy against dermatophytes and other superficial fungal pathogens is well established internationally, and it has broad-spectrum in vitro activity extending to *Candida* species and *Malassezia* species.

Pityriasis versicolor is caused by *Malassezia* species, a fungal genus mechanistically within luliconazole's known spectrum of activity — the same sterol-synthesis-inhibition mechanism that underlies its established antifungal use is directly applicable here. PMID 12636984 provides direct in vitro confirmation that luliconazole (studied as NND-502) has strong activity against *Malassezia* species, and PMID 27559523 is a published randomized controlled comparison of topical luliconazole versus ketoconazole specifically in pityriasis versicolor patients, reinforcing that this is a mechanistically coherent and clinically plausible extension rather than a speculative repurposing target.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07333170](https://clinicaltrials.gov/study/NCT07333170) | Phase 4 | Not Yet Recruiting | 86 | Randomized controlled comparison of topical luliconazole 2% cream vs. topical ketoconazole 1% cream for pityriasis versicolor, testing whether luliconazole offers improved efficacy and shorter treatment duration than ketoconazole. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | RCT | Indian Dermatology Online Journal | Prospective, open, randomized controlled trial comparing topical ketoconazole and topical luliconazole in pityriasis versicolor at a tertiary care hospital. |
| [12636984](https://pubmed.ncbi.nlm.nih.gov/12636984/) | 2003 | In vitro (mechanistic) | International Journal of Antimicrobial Agents | In vitro activity of luliconazole (NND-502) against the three major *Malassezia* species, compared with lanoconazole, bifonazole, and terbinafine — confirms potent anti-*Malassezia* activity. |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In vitro | Journal de Mycologie Médicale | Confirms luliconazole's broad-spectrum antifungal activity against dermatophytes, *Candida albicans*, and *Malassezia* species, and notes its established clinical use for pityriasis versicolor, dermatophytosis, onychomycosis, and cutaneous/mucocutaneous candidiasis. |

## Saudi Arabia Market Information

Luliconazole is currently not marketed in Saudi Arabia — no authorization records are on file (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A published RCT directly comparing luliconazole to ketoconazole in pityriasis versicolor, combined with confirmatory in vitro evidence against *Malassezia* species and an ongoing Phase 4 head-to-head trial, supports an L2 evidence level. However, the drug is not yet marketed in Saudi Arabia and key safety documentation is missing, so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently blocking — flagged as Data Gap DG001)
- Detailed mechanism of action (MOA) data from DrugBank (Data Gap DG002)
- Results from the ongoing Phase 4 trial (NCT07333170) once recruitment completes
- A Saudi Arabia market entry / registration assessment, since the drug currently holds no local authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

