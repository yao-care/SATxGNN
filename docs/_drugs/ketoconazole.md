---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketoconazole: From Fungal Infections to Acne Vulgaris

## One-Sentence Summary

Ketoconazole (DrugBank DB01026) is a broad-spectrum imidazole antifungal, historically used to treat fungal infections such as dermatophytosis, candidiasis, and seborrheic dermatitis. The TxGNN model predicts it may also be effective for **Acne (Acne Vulgaris)**, with **1 clinical trial** and **15 publications** currently identified, though most literature evidence is mechanistic/preclinical rather than clinical. The drug is not currently marketed in Saudi Arabia, which limits immediate actionability of this signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (antifungal, imidazole class) — no Saudi Arabia–specific approved indication text available; drug not marketed |
| Predicted New Indication | Acne (Acne Vulgaris) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (mechanistic/preclinical evidence predominant; one small trial still active, not yet completed) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ketoconazole is not available in this Evidence Pack (data gap). Based on known pharmacology, ketoconazole is an imidazole antifungal that inhibits fungal cytochrome P450-dependent 14α-demethylase, and at higher concentrations also inhibits mammalian steroidogenic P450 enzymes — the basis for its historical off-label use in Cushing's syndrome.

The link to acne is supported by two mechanistic in vitro studies identified in the literature evidence: ketoconazole inhibits *Propionibacterium (Cutibacterium) acnes* lipase activity (PMID 28111792) and shows in vitro activity against *P. acnes* comparable to other azole antifungals (PMID 20045949). Since *P. acnes* lipase-driven sebum metabolism is a key contributor to acne inflammation, an antimicrobial/anti-lipase mechanism distinct from ketoconazole's original antifungal indication offers a plausible biological rationale for repurposing.

A currently active (not yet recruiting-complete) trial (NCT07237763) is directly testing topical ketoconazole 2% cream against topical adapalene 2% cream in mild acne, suggesting this hypothesis is already being tested clinically, though results are not yet available.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | NA (topical) | Active, not recruiting | 52 | Randomized comparison of topical ketoconazole 2% cream vs. topical adapalene 2% cream in mild comedonal and papulopustular acne, evaluating ketoconazole as a lower-side-effect alternative to topical retinoids |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | In vitro / mechanistic study | Microbiology and Immunology | Ketoconazole inhibits *P. acnes* lipase activity, supporting a possible anti-acne mechanism distinct from its antifungal action |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biological & Pharmaceutical Bulletin | Azole antifungals, including ketoconazole, show in vitro activity against *P. acnes* isolated from acne patients |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series / therapeutic trial | Clinical and Experimental Dermatology | Pityrosporum (Malassezia) folliculitis in Saudi Arabia, often misdiagnosed as acne vulgaris; discusses azole-based diagnosis and treatment |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | The Keio Journal of Medicine | Reviews Pityrosporum (Malassezia) ovale's role in skin diseases including folliculitis resembling acne |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | Overview of systemic acne treatment options, contextualizing where antimicrobial approaches fit alongside antibiotics |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Archives of Dermatology | Neonatal *Malassezia furfur* pustulosis presenting similarly to neonatal acne, linking fungal pathogens to acneiform eruptions |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clinical Evidence | PCOS review noting acne as an associated hyperandrogenic symptom |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Review / clinical | Polski Tygodnik Lekarski | Hyperandrogenic PCOS treatment reduces acne and hirsutism, relevant to antiandrogenic mechanisms shared with azoles |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | Pharmaceuticals (Basel) | Reviews adapalene, the active comparator used in NCT07237763, for first-line acne treatment |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | FP Essentials | Overview of common infant skin rashes including neonatal acne, relevant to differential diagnosis |

---

## Saudi Arabia Market Information

Ketoconazole is not currently marketed in Saudi Arabia (0 authorizations on record) — no product license information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A **Blocking** data gap (DG001) exists — TFDA/SFDA package insert warnings and contraindications have not been retrieved, which by policy prevents this candidate from entering the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale (anti-*P. acnes* lipase activity) is plausible and one relevant trial is underway, but no completed clinical trial or systematic evidence yet confirms efficacy in acne. More critically, a **Blocking** safety data gap (package insert warnings/contraindications not retrieved) and the drug's non-marketed status in Saudi Arabia prevent any safety pre-screening or regulatory pathway assessment at this time.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse TFDA/SFDA package insert for warnings and contraindications
- Resolve DG002 (High): obtain confirmed mechanism of action data from DrugBank
- Await completion of NCT07237763 for direct clinical efficacy/safety data in acne
- Assess regulatory pathway feasibility given ketoconazole's current non-marketed status in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

