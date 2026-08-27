---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Prednisone is a synthetic corticosteroid widely used across inflammatory, autoimmune, and oncologic combination regimens. The TxGNN model predicts it may be effective for **Alopecia Areata**, with a query returning **33 clinical trial records and 20 publications**, though most trial hits reference prednisone only as a background regimen in unrelated diseases (SLE, oncology) rather than as a tested intervention for alopecia areata; the disease-specific evidence is anchored by one completed Phase 3 RCT and a multi-decade body of dermatology case series/cohorts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug is not marketed in Saudi Arabia; no approved indication text available) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on known pharmacology, prednisone is a synthetic glucocorticoid that acts via the glucocorticoid receptor (GR) to suppress the NF-κB pathway, reducing peri-follicular CD8+ T-cell infiltration and Th1/Th17-driven inflammation — a mechanism that maps directly onto the autoimmune follicular attack underlying alopecia areata (AA).

This is not a novel hypothesis: systemic corticosteroids (alone or combined with methotrexate or JAK inhibitors) are already an established off-label dermatology practice for severe AA. Case reports and cohort studies date back to the 1950s–1970s, and more recent literature (2016–2026) documents combination regimens (methotrexate + low-dose prednisone; baricitinib + low-dose corticosteroids) specifically for the most refractory subtypes (alopecia totalis/universalis).

One caveat: the clinical trial search returned a large number of records (33) tagged to "alopecia areata," but the majority are actually systemic lupus erythematosus (SLE) or oncology trials in which prednisone appears only as a background standard-of-care component, not as a tested AA intervention. Only one trial directly evaluates prednisone in AA.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | RCT testing methotrexate vs. placebo, with secondary treatment by methotrexate + low-dose prednisone, in severe alopecia areata (regrowth rate <10% with standard care) |

**Note:** The remaining 32 trials returned by the search query are for unrelated indications (SLE, lupus nephritis, prostate/breast cancer, lymphoma) where prednisone appears only as a background or comparator regimen component — they were excluded as not directly relevant to alopecia areata and are not listed here.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 2-step double-blind RCT: methotrexate alone vs. methotrexate + low-dose prednisone in alopecia totalis/universalis |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Cohort | Archives of Dermatology | Immunologic studies of AA with prednisone treatment |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Cohort | Italian J Dermatol Venereol | Real-world evidence: AA comorbidities, treatment patterns, and economic burden in Italy |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort | Dermatology (Basel) | Efficacy/safety of methotrexate combined with low-to-moderate dose corticosteroids for severe AA |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Archives of Dermatology | Review of AA therapy efficacy, safety, and mechanism across treatment modalities |
| [41958306](https://pubmed.ncbi.nlm.nih.gov/41958306/) | 2026 | Review | J Eur Acad Dermatol Venereol | Retrospective case series: baricitinib + low-dose prednisone for very severe AA |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Review | Archives of Dermatology | Follow-up report on prednisone therapy for AA; documents long-term relapse and steroid side effects |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case Series | Clinical and Experimental Dermatology | 8-case series: baricitinib + low-dose corticosteroids for very severe AA |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Study | Annales de Dermatologie et Vénéréologie | Efficacy and safety of once-monthly oral pulsed prednisone in AA management |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Study | International Journal of Dermatology | Severe AA treated with systemic corticosteroids |

---

## Saudi Arabia Market Information

Prednisone currently has no marketing authorization on record in Saudi Arabia (0 total licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or DDI data were available in the evidence pack; the TFDA package-insert lookup for this candidate is flagged as a **Blocking** data gap that must be resolved before a formal S1 safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN scores this prediction near-maximal (99.99%), and it is corroborated by a completed Phase 3 RCT plus a multi-decade, mechanistically coherent body of case series and cohort literature — corticosteroids are already established off-label practice for severe AA. However, no dedicated prednisone-monotherapy RCT exists (evidence is combination-based), and this candidate is currently unmarketed in Saudi Arabia with a blocking gap in local safety labeling.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings, contraindications, and DDI data (blocking gap — required before S1 safety review)
- Detailed mechanism of action documentation (DrugBank MOA currently unavailable)
- Confirmation of regulatory pathway for a currently unmarketed product (import/registration or off-label use framework)
- Prednisone-specific (monotherapy or defined combination) efficacy data in AA to strengthen the evidence level beyond L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

