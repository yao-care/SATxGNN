---
layout: default
title: Butenafine
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 5
---

# Butenafine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Butenafine: From Dermatophytosis to Cutaneous Candidiasis

## One-Sentence Summary

Butenafine is a topical benzylamine-class antifungal internationally approved (e.g., by the FDA) for dermatophyte infections including tinea pedis, tinea cruris, and tinea corporis, though it currently holds no Taiwan market authorization.
The TxGNN model predicts it may be effective for **Cutaneous Candidiasis**,
with **0 clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan registration; internationally used for dermatophytosis (tinea pedis / tinea cruris / tinea corporis) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on published pharmacological literature, butenafine is a synthetic benzylamine antifungal that inhibits squalene epoxidase — an enzyme essential for ergosterol biosynthesis in fungal cell membranes. This is structurally and mechanistically related to the allylamine class (e.g., terbinafine), and the ergosterol synthesis pathway is shared across both dermatophytes and *Candida* species, providing a theoretical basis for cross-indication activity.

Dermatophytosis and cutaneous candidiasis are both superficial skin mycoses caused by fungi that depend on ergosterol for membrane integrity. Butenafine's high lipophilicity and demonstrated skin penetration profile support its potential to reach concentrations adequate to inhibit *Candida* at the cutaneous level. In animal models (guinea pig), butenafine has shown activity against superficial candidiasis when evaluated alongside other antifungals.

However, the clinical evidence gap is significant. Butenafine's validated spectrum is primarily against dermatophytes (*Trichophyton*, *Microsporum*, *Epidermophyton*). In vitro data against *Candida* species shows variable minimum inhibitory concentrations, and no dedicated clinical trial for cutaneous candidiasis has been registered. The TxGNN score (99.33%) reflects disease graph proximity and mechanistic plausibility, not confirmed clinical efficacy. This prediction should be treated as a hypothesis-generating signal requiring prospective validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | Journal of Drugs in Dermatology | Reviews topical antifungal agents for superficial cutaneous fungal infections including dermatophytosis and yeast infections; discusses butenafine's role and activity spectrum among available topical agents |
| [11893219](https://pubmed.ncbi.nlm.nih.gov/11893219/) | 2002 | Review | Am J Clin Dermatology | Narrative review of six novel antimycotics including butenafine; describes its potential applications across cutaneous and mucosal fungal diseases, though primary evidence cited is for dermatophytes |
| [11302816](https://pubmed.ncbi.nlm.nih.gov/11302816/) | 2001 | In Vitro Study | Antimicrobial Agents and Chemotherapy | Evaluated KP-103 triazole against dermatomycosis pathogens including *Candida* species and dermatophytes in guinea pig models of tinea pedis and cutaneous candidiasis; butenafine referenced as a comparator antifungal in MIC assays |

---

## Taiwan Market Information

Butenafine currently holds no approved drug license in Taiwan. No registered products or authorized indications are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The three identified publications are indirect reviews and one in vitro comparator study — none constitute direct clinical evidence for butenafine in cutaneous candidiasis; the TxGNN prediction reflects mechanistic and disease-graph plausibility only, and no registered clinical trial exists to date.

**To proceed, the following is needed:**

- Dedicated in vitro susceptibility studies (MIC determination by CLSI/EUCAST method) for butenafine against key cutaneous *Candida* species (*C. albicans*, *C. tropicalis*, *C. parapsilosis*)
- Animal model proof-of-concept (e.g., guinea pig cutaneous candidiasis model) to confirm in vivo fungicidal activity
- Mechanism of action data retrieval from DrugBank API to formally document the squalene epoxidase inhibition pathway
- Taiwan package insert and TFDA warning database review to identify safety contraindications prior to any trial initiation
- Pilot clinical study (open-label or Phase 2 RCT) comparing topical butenafine 1% cream vs. standard-of-care (e.g., clotrimazole) in patients with confirmed cutaneous candidiasis
- Consider bridging from the stronger L1 evidence base for **Superficial Mycosis** (TxGNN rank 2, score 99.02%, supported by 3 RCTs) as the primary regulatory registration pathway; cutaneous candidiasis can be explored as a label extension thereafter
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

