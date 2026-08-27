---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

# Ruxolitinib: From Myelofibrosis to Hemophagocytic Syndrome Associated with an Infection

*Note: Ruxolitinib is not marketed in Saudi Arabia and this evidence pack has no captured "original indication" or MOA record (see Data Gaps DG001/DG002). "Myelofibrosis" above reflects Ruxolitinib's well-known global approval as a JAK1/2 inhibitor, not a value extracted from this evidence pack.*

## One-Sentence Summary

Ruxolitinib is a JAK1/JAK2 inhibitor with no captured Saudi Arabia market presence in this evidence pack. Among **10 TxGNN-predicted indications** for this drug, **Hemophagocytic Syndrome Associated with an Infection** stands out as the lead candidate — it is the only one backed by real clinical evidence, with **2 clinical trials** (including one Phase 3 RCT) and **20 publications**, while the other 9 candidates (mostly PEComa-family tumours and sarcomas) remain unsupported model predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (drug not marketed in Saudi Arabia; DrugBank/MOA data pending — DG002) |
| Predicted New Indication | Hemophagocytic Syndrome Associated with an Infection |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ruxolitinib is not available in this evidence pack (DG002). Based on publicly known information, Ruxolitinib is a JAK1/JAK2 inhibitor; its efficacy in myeloproliferative and inflammatory conditions driven by cytokine signalling is well established, and this same mechanism plausibly extends to Hemophagocytic Syndrome (HLH/HPS).

Infection-associated HLH is driven by an IFN-γ/IL-6 cytokine storm that signals through JAK1/2–STAT1, the exact pathway Ruxolitinib inhibits. The repurposing rationale in this pack notes that this mechanistic link is direct, and is already validated clinically by a downstream-target drug (emapalumab, an anti-IFN-γ antibody) acting on the same axis. This is corroborated by a closely related but weaker candidate in the same pack — "acquired HLH associated with malignant disease" (rank 9, L4) — which shares the identical IFN-γ/JAK-STAT cytokine-storm mechanism but triggered by malignancy rather than infection, reinforcing that the pathway (not just the trigger) is what matters pharmacologically.

By contrast, the top-ranked TxGNN prediction by score alone (uterine PEComa) and several other high-scoring candidates (benign PEComa, lymphangiomyoma, lymphangioleiomyomatosis, lung PEComa) are driven by the TSC1/2–mTORC1 pathway, not JAK-STAT, and have no supporting trial or literature evidence in this pack — they are flagged Hold at evidence level L5 and are not carried forward in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Phase 3 | Unknown | 216 | Randomized trial of anakinra, tocilizumab alone or combined with ruxolitinib in severe stage 2b/3 COVID-19-associated hyperinflammatory disease (CRP >200 mg/L); status unconfirmed — completion/results need verification. |
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Phase 1 | Not Yet Recruiting | 16 | Pilot study of ruxolitinib for immune effector cell-associated HLH-like syndrome (IEC-HS) after CAR-T therapy; evaluates safety, optimal duration, and biomarkers of response. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Cohort | Blood | Ruxolitinib used as a first-line agent with response-based stratified treatment in pediatric HLH; addresses the lack of robust trials for frontline use. |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Cohort | British Journal of Haematology | Retrospective comparison of ruxolitinib-based regimen (n=53) vs. adjusted HLH-94 chemotherapy (n=42) in pediatric EBV-associated HLH. |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Case Series (n=12) | Annals of Hematology | Sintilimab combined with ruxolitinib as compassionate therapy in 12 adults with EBV-associated HLH. |
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Review/Guideline | Critical Care Medicine | Consensus-based guidelines for recognition, diagnosis, and management of HLH in critically ill children and adults. |
| [37702780](https://pubmed.ncbi.nlm.nih.gov/37702780/) | 2023 | Review | Innere Medizin | Review of HLH treatment in ICU patients, covering hereditary vs. acquired forms and emerging triggers (e.g., CAR-T immunotherapy). |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Review | QJM | Review of adult HLH, noting high mortality despite diagnostic and treatment advances. |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Preclinical/Mechanistic | Blood | Foundational mechanistic study showing ruxolitinib dampens T-cell activation and inflammation in a perforin-deficient murine HLH model. |
| [32530039](https://pubmed.ncbi.nlm.nih.gov/32530039/) | 2020 | Preclinical/Mechanistic | Blood | JAK/STAT pathway inhibition sensitizes CD8 T cells to dexamethasone-induced apoptosis, supporting combination therapy in hyperinflammation. |
| [36263041](https://pubmed.ncbi.nlm.nih.gov/36263041/) | 2022 | Case Report | Frontiers in Immunology | Ruxolitinib used as first-line therapy for secondary HLH in a patient with AIDS and severe immunodeficiency. |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Case Series | Journal of Pediatric Hematology/Oncology | Emapalumab combined with ruxolitinib and dexamethasone effectively treated EBV-associated HLH with multiorgan damage and severe infection. |

*10 additional case reports/series on ruxolitinib in infection-triggered HLH (EBV, adenovirus, Chlamydia, VEXAS-associated, post-transplant, pregnancy-associated) are available in the source data but omitted here for brevity.*

---

## Saudi Arabia Market Information

Ruxolitinib is not currently marketed in Saudi Arabia — no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — this is flagged as a **Blocking** data gap, DG001, that must be resolved before any S1 safety review.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Infection-associated HLH shares a direct, well-characterized IFN-γ/JAK-STAT mechanistic link with Ruxolitinib's known pharmacology, and is supported by one Phase 3 RCT plus a substantial body of cohort, review, and case-series literature (L2) — the strongest evidence base among all 10 TxGNN candidates for this drug.

**To proceed, the following is needed:**
- Confirm actual status/results of NCT04424056 (currently listed as "Unknown")
- Obtain SFDA package insert / label data for Ruxolitinib (DG001, Blocking)
- Obtain DrugBank MOA confirmation (DG002)
- Obtain drug interaction (DDI) data — current query returned no results
- Since Ruxolitinib is not marketed in Saudi Arabia, confirm import/named-patient access pathway before clinical use
- Deprioritize the 8 remaining low-evidence candidates (PEComa family, liposarcoma, familial rhabdoid tumor) pending new trial or literature data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

