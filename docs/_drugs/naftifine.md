---
layout: default
title: Naftifine
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 8
---

# Naftifine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Naftifine: From Dermatophytosis (Tinea) to Cutaneous Candidiasis

## One-Sentence Summary

Naftifine is an allylamine-class topical antifungal whose established clinical use, per the literature on file, is treatment of dermatophyte skin infections (tinea pedis/cruris/corporis) — though it currently has no registered indication or market presence in Saudi Arabia. The TxGNN model predicts it may also be effective for **Cutaneous Candidiasis**, a prediction already partly corroborated by **9 older publications** (including a 1988 double-blind RCT), though **no clinical trials specific to this indication are currently registered**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in Saudi Arabia (drug not marketed). Literature indicates naftifine's established use is topical treatment of dermatophytosis (tinea pedis/cruris/corporis). |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action field for naftifine is currently a data gap, but the literature evidence collected in this pack describes it directly: naftifine is a synthetic allylamine that inhibits squalene epoxidase, blocking ergosterol biosynthesis in the fungal cell membrane. This gives it potent fungicidal activity against dermatophytes and — at lower potency — fungistatic activity against *Candida* species (PMID 1723367, PMID 18346400).

Dermatophytosis and cutaneous candidiasis are both superficial fungal skin infections, but they are caused by biologically distinct organisms (keratinophilic dermatophytes vs. *Candida* yeasts), so the mechanistic overlap is real but only partial — naftifine's action against *Candida* is fungistatic rather than fungicidal, and generally weaker than azole antifungals such as clotrimazole.

Notably, this "new" indication is not entirely novel: a 1988 double-blind, vehicle-controlled RCT (PMID 3048914, n=60) already reported 77% mycological cure in cutaneous candidiasis at 2 weeks post-treatment, and a 1984 multicenter double-blind contralateral comparison against clotrimazole (PMID 6388169) found comparable early cure rates (63.5% vs. 56% at day 7) in a mixed dermatophytosis/candidosis population. TxGNN's prediction is therefore best read as a rediscovery of decades-old clinical evidence rather than a novel repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6388169](https://pubmed.ncbi.nlm.nih.gov/6388169/) | 1984 | RCT (multicenter, double-blind, contralateral vs. clotrimazole) | Zeitschrift für Hautkrankheiten | 126 patients with dermatophytosis/candidosis; naftifine cure rate 63.5% vs. clotrimazole 56% at 7 days, similar tolerability |
| [3048914](https://pubmed.ncbi.nlm.nih.gov/3048914/) | 1988 | Clinical trial (double-blind, vehicle-controlled) | Cutis | 60 patients with cutaneous candidiasis; naftifine cream 1% twice daily x3 weeks; 77% mycological cure at 2 weeks post-treatment |
| [2620916](https://pubmed.ncbi.nlm.nih.gov/2620916/) | 1989 | Clinical evaluation (open-label) | Giornale italiano di dermatologia e venereologia | 29 patients with mixed dermatomycoses (16 tinea corporis, 11 pityriasis versicolor, 2 cutaneous candidiasis); mean treatment 32.9 days |
| [1723367](https://pubmed.ncbi.nlm.nih.gov/1723367/) | 1991 | Review | Drugs | Describes naftifine's mechanism (squalene epoxidase inhibition), possible anti-inflammatory properties, and clinical/mycological activity in dermatophytoses |
| [18346400](https://pubmed.ncbi.nlm.nih.gov/18346400/) | 2008 | Review | Journal of Cutaneous Medicine and Surgery | Confirms fungicidal activity vs. dermatophytes and good activity against *Candida* and *Aspergillus* species |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | Journal of Drugs in Dermatology | Overview of topical antifungal therapy optimization for superficial cutaneous fungal infections, including yeast infections |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Pending classification | Drugs | Review of fenticonazole (a comparator antimycotic), not naftifine-specific; included as background evidence |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Pending classification | Drugs | Review of terbinafine (a comparator allylamine), notes allylamines are fungistatic against *Candida albicans* |
| [20677526](https://pubmed.ncbi.nlm.nih.gov/20677526/) | 2010 | Pending classification | Journal of Drugs in Dermatology | Naftifine review; abstract not available in this evidence pack |

## Safety Considerations

Please refer to the package insert for safety information. Note: the underlying evidence pack flags TFDA/SFDA package-insert warnings and contraindications as a **Blocking** data gap (DG001) — this currently prevents the candidate from clearing the S1 safety pre-screening stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Naftifine is not currently marketed in Saudi Arabia (0 authorizations), and a Blocking data gap in TFDA/SFDA safety labeling prevents even initial (S1) safety screening. While L2-level evidence (a 1984 comparative RCT and a 1988 vehicle-controlled RCT) supports historical antifungal activity against cutaneous candidiasis, that evidence is 35–40 years old and does not substitute for current safety documentation or a registration pathway.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications, DDI) — DG001
- Formal mechanism-of-action documentation from DrugBank — DG002
- Confirmation of Saudi Arabia market entry / registration status for naftifine
- Updated clinical evidence, as existing supportive trials predate modern GCP standards
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

