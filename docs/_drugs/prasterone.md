---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone (DHEA): From Unrecorded Original Indication to 10 TxGNN-Predicted Candidates

## One-Sentence Summary

> Prasterone (DHEA, DrugBank DB01708) is an endogenous adrenal androgen precursor; no approved original indication or detailed mechanism-of-action data is available in this evidence pack, and the drug is currently **not marketed** in the covered market.
> The TxGNN model surfaced **10 candidate indications**, topped by **Heparin Cofactor II Deficiency** (score 99.99%), but **9 of the 10 candidates have zero supporting clinical trials or literature**, and several are mechanistically counter-indicated.
> Only one candidate — **scleroderma (systemic sclerosis)** — is backed by actual literature (6 observational cohort studies) and reaches evidence stage S1.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication on record in this evidence pack) |
| Predicted New Indication (top TxGNN rank) | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## All 10 TxGNN-Predicted Candidates

| Rank | Disease | Score | Evidence Level | Stage | Recommendation |
|------|---------|-------|-----------------|-------|-----------------|
| 1 | Heparin cofactor 2 deficiency | 99.99% | L5 | S0 | Hold |
| 2 | Factor 5 excess with spontaneous thrombosis | 99.98% | L5 | S0 | Hold |
| 3 | Antithrombin deficiency type 2 | 99.98% | L5 | S0 | Hold |
| 4 | Thrombophilia | 99.91% | L4 | S0 | Hold |
| 5 | Severe nonproliferative diabetic retinopathy | 99.25% | L5 | S0 | Hold |
| 6 | Thrombophilia due to protein S deficiency (AR) | 99.13% | L5 | S0 | Hold |
| **7** | **Scleroderma (systemic sclerosis)** | 99.11% | **L4** | **S1** | **Research Question** |
| 8 | Complement component 4a deficiency | 99.05% | L5 | S0 | Hold |
| 9 | Pseudo-von Willebrand disease | 99.01% | L5 | S0 | Hold |
| 10 | Primary release disorder of platelets | 99.01% | L5 | S0 | Hold |

**Note:** Rank 7 (scleroderma) is the only candidate that has moved past pure model prediction. It is discussed separately below alongside the top-ranked candidate.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for prasterone is flagged as a data gap in this evidence pack. Based on the information available, prasterone is an adrenal androgen precursor (endogenous DHEA); no original approved indication is recorded here, so its established efficacy profile cannot be used to anchor the new predictions.

For the top-ranked candidate and the five other thrombophilia/coagulation-factor-deficiency candidates (ranks 1, 2, 3, 4, 6, and 9–10 to a lesser extent), the underlying diseases are hypercoagulable or clotting-factor disorders that would generally require an anticoagulant or factor-replacement mechanism to treat. Androgen compounds such as DHEA are pharmacologically associated with erythropoiesis stimulation and a **procoagulant** tendency rather than an antithrombotic one — a direction supported indirectly by one of the retrieved papers (PMID 24152686), a case report of an ovarian Leydig cell tumor causing extreme hyperandrogenism, erythrocytosis, and recurrent pulmonary embolism. This suggests the TxGNN embedding proximity for these candidates may reflect graph-topology adjacency between "endocrine" and "hemostasis" gene neighborhoods rather than a genuine therapeutic mechanism, and in some cases the direction of effect may run opposite to what treatment would require.

The scleroderma candidate (rank 7) stands apart: six independent cohort studies consistently report that patients with systemic sclerosis have significantly **lower** serum DHEA/DHEA-S levels, correlating with disease severity. This forms a coherent "hormone deficiency → replacement" hypothesis (DHEA's known immunomodulatory and anti-inflammatory properties could plausibly address the HPA-axis/adrenal androgen deficit seen in SSc). However, all six studies are observational associations between endogenous hormone level and disease state — none is an interventional trial of DHEA treatment — so causality and efficacy remain unestablished.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for the top-ranked candidate, Heparin Cofactor II Deficiency, or for any of the other 9 candidates).

---

## Literature Evidence

For the top-ranked candidate (Heparin Cofactor II Deficiency): currently no related literature available.

Literature exists for two lower-ranked candidates and is summarized here for completeness:

**Rank 4 — Thrombophilia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23683262](https://pubmed.ncbi.nlm.nih.gov/23683262/) | 2013 | Cohort/Case-control | J Chin Med Assoc | Thrombophilia associated with recurrent pregnancy loss in PCOS patients — not a DHEA intervention study |
| [25531921](https://pubmed.ncbi.nlm.nih.gov/25531921/) | 2015 | Review/Guideline | Hum Fertil | IVF adjuvant practice guideline; may reference DHEA as an ovarian-response adjuvant, not as thrombophilia treatment |
| [24152686](https://pubmed.ncbi.nlm.nih.gov/24152686/) | 2014 | Case Report | J Clin Endocrinol Metab | Ovarian Leydig cell tumor → extreme hyperandrogenism, erythrocytosis, and recurrent pulmonary embolism — signals androgen-driven thrombotic **risk**, not benefit |
| [6241118](https://pubmed.ncbi.nlm.nih.gov/6241118/) | 1984 | Review | Clin Obstet Gynecol | Pathophysiology of pregnancy-induced hypertension; no direct DHEA-thrombophilia link |

**Rank 7 — Scleroderma (systemic sclerosis)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9159534](https://pubmed.ncbi.nlm.nih.gov/9159534/) | 1997 | Cohort | Br J Rheumatol | High prolactin / low DHEA-S in patients with severe systemic sclerosis |
| [11247320](https://pubmed.ncbi.nlm.nih.gov/11247320/) | 2001 | Cohort | Clin Exp Rheumatol | DHEA-S levels evaluated against SSc disease severity |
| [12073659](https://pubmed.ncbi.nlm.nih.gov/12073659/) | 2002 | Review | Orvosi Hetilap | Adrenal/gonadal androgens (incl. DHEA) implicated in autoimmune polyarthritis pathogenesis; immunosuppressive effect via IL-6 inhibition |
| [16855152](https://pubmed.ncbi.nlm.nih.gov/16855152/) | 2006 | Cohort | Ann N Y Acad Sci | Androgen and prolactin levels in SSc relative to disease severity |
| [17086608](https://pubmed.ncbi.nlm.nih.gov/17086608/) | 2006 | Cohort | J Rheumatol | Blunted adrenocortical/adrenomedullary response to hypoglycemia in premenopausal SSc patients |
| [25524921](https://pubmed.ncbi.nlm.nih.gov/25524921/) | 2015 | Cohort | Rheumatology (Oxford) | Androgen status in post-menopausal SSc patients |

---

## Saudi Arabia Market Information

No product is currently registered or marketed (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (top-ranked candidate, Heparin Cofactor II Deficiency) — **with Scleroderma flagged separately as a Research Question**

**Rationale:**
- The top TxGNN-ranked candidate and 8 of the remaining 9 candidates have no clinical trial or literature support (L5, pure model prediction), and several (thrombophilia-spectrum diseases) run mechanistically counter to DHEA's known procoagulant/androgenic tendency.
- The one candidate with actual supporting evidence, scleroderma, is based entirely on observational association (low endogenous DHEA-S correlating with disease severity) rather than interventional data, so it warrants tracking as a research question rather than a Go decision.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently a blocking data gap)
- Detailed original mechanism of action (MOA) data from DrugBank or equivalent source
- For scleroderma: an interventional trial of exogenous DHEA supplementation in SSc patients to establish causality/efficacy, not just association
- For the six thrombophilia-spectrum candidates: a targeted pharmacology review to confirm/refute the apparent procoagulant-direction conflict before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

