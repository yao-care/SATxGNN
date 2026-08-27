---
layout: default
title: Vindesine
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 5
---

# Vindesine
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

# Vindesine: From Cytotoxic Chemotherapy to Neuroblastoma

## One-Sentence Summary

Vindesine is a semisynthetic vinca-alkaloid cytotoxic agent; no specific original indication or market license is recorded in this evidence pack, and it is currently **not marketed in Saudi Arabia**. The TxGNN model's highest-ranked prediction, **ganglioneuroblastoma**, has no supporting studies, but the closely related and mechanistically analogous entity **neuroblastoma** (rank 3) is backed by **6 clinical trials** and **15 publications**, including a direct Phase II trial of vindesine in childhood malignancies. A second candidate, **myeloid leukemia**, is supported by an actively recruiting Phase 2 trial that explicitly includes vindesine, plus extensive historical literature on its use in blast crisis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack; vindesine is historically used as a vinca-alkaloid cytotoxic chemotherapy agent |
| Predicted New Indication | Neuroblastoma (mechanistically linked to the top-ranked but evidence-free prediction, ganglioneuroblastoma) |
| TxGNN Prediction Score | 99.86% (score 0.99863, rank 2981) |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question — see Conclusion) |

---

## Why is This Prediction Reasonable?

Detailed regulatory-grade mechanism-of-action documentation is not available in this pack, but the repurposing rationale itself provides a pharmacological basis: Vindesine is a vinca alkaloid that inhibits tubulin polymerization, blocking mitotic spindle formation. It is a close structural analog of vincristine, the vinca alkaloid that forms the backbone of standard pediatric neuroblastoma chemotherapy protocols (e.g., N2 elements combining vincristine, dacarbazine, ifosfamide, doxorubicin).

Neuroblastoma and ganglioneuroblastoma both arise from the same neural-crest lineage and share overlapping treatment protocols, which is consistent with vindesine's TxGNN top prediction (ganglioneuroblastoma, score 99.99%) even though no direct trials or literature exist for that specific diagnosis. The neuroblastoma evidence effectively substantiates the mechanistic direction of that top-ranked but otherwise unsupported prediction.

Direct clinical precedent exists: the German NB90 neuroblastoma therapy study explicitly dosed vindesine (3 mg/m² as part of the N1 chemotherapy element) alongside etoposide and cisplatin, and a CALGB Phase II study tested vindesine directly in childhood malignancies including neuroblastoma. This is a case where mechanistic plausibility and historical clinical use converge, though modern confirmatory trials designed specifically around this repurposing hypothesis are lacking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00526318](https://clinicaltrials.gov/study/NCT00526318) | N/A | Unknown | 360 | NB2004-HR protocol: pre-transplant chemotherapy + autologous stem cell transplant + isotretinoin in high-risk neuroblastoma |
| [NCT00017225](https://clinicaltrials.gov/study/NCT00017225) | Phase 2 | Completed | N/A | Combined chemotherapy, radiation, and peripheral stem cell transplantation in neuroblastoma |
| [NCT04221035](https://clinicaltrials.gov/study/NCT04221035) | Phase 3 | Recruiting | 800 | SIOPEN international randomized trial of induction/consolidation chemotherapy and radiotherapy for high-risk neuroblastoma |
| [NCT03042429](https://clinicaltrials.gov/study/NCT03042429) | Phase 3 | Completed | 360 | Chemotherapy + stem cell transplant + isotretinoin, testing added topotecan cycles for event-free survival |
| [NCT00002802](https://clinicaltrials.gov/study/NCT00002802) | Phase 3 | Completed | 500 | Multicentre trial comparing chemotherapy/bone marrow transplant regimens by risk stage |
| [NCT00410631](https://clinicaltrials.gov/study/NCT00410631) | Phase 3 | Unknown | 642 | NB2004 risk-adapted treatment protocol with combination chemotherapy and autologous stem cell transplant |

*Note: None of these trial titles explicitly name vindesine (relevance graded B — broad multi-agent protocols where vinca alkaloids are commonly included but not individually confirmed).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7038420](https://pubmed.ncbi.nlm.nih.gov/7038420/) | 1982 | RCT (Phase 2) | Medical and Pediatric Oncology | Phase II study of vindesine in 36 children with malignancies; effective at 4 mg/m² weekly infusion after early-regimen neurotoxicity/GI toxicity was mitigated |
| [9340428](https://pubmed.ncbi.nlm.nih.gov/9340428/) | 1997 | Cohort | Klinische Pädiatrie | NB90 neuroblastoma study: vindesine 3 mg/m² used within the N1 chemotherapy element; describes myelopoietic recovery kinetics |
| [21139829](https://pubmed.ncbi.nlm.nih.gov/21139829/) | 2010 | Case report | Rare Tumors | Adult epidural neuroblastoma treated with vindesine, cisplatin, and etoposide, achieving disease-free remission after surgery and chemotherapy |
| [6943380](https://pubmed.ncbi.nlm.nih.gov/6943380/) | 1981 | Preclinical/Cohort | J Natl Cancer Inst | Comparative cytotoxicity/kinetics of vincristine vs. vindesine; murine neuroblastoma cells ~5-fold less sensitive to vindesine than other lines |
| [2166461](https://pubmed.ncbi.nlm.nih.gov/2166461/) | 1990 | Preclinical | Anticancer Research | Gamma-linolenic acid enhanced vindesine (and other vinca alkaloid) cytotoxicity ~2-fold in human neuroblastoma cell lines |
| [3731152](https://pubmed.ncbi.nlm.nih.gov/3731152/) | 1986 | Preclinical | Cancer Treatment Reports | Differential drug sensitivity assay across 6 human neuroblastoma cell lines, including vindesine among tested antimitotics |
| [17141950](https://pubmed.ncbi.nlm.nih.gov/17141950/) | 2007 | Preclinical | Cancer Letters | MYCN expression affects chemosensitivity in neuroblastoma cells, relevant to multidrug resistance mechanisms |
| [11464889](https://pubmed.ncbi.nlm.nih.gov/11464889/) | 2001 | Cohort | Medical and Pediatric Oncology | Evaluated catecholamine metabolites, mIBG scan, and bone marrow cytology as treatment-response markers in stage 4 neuroblastoma |
| [12637472](https://pubmed.ncbi.nlm.nih.gov/12637472/) | 2003 | Review | J Clin Oncol | FDA review of pediatric oncology drug approvals and regulatory initiatives |
| [7968789](https://pubmed.ncbi.nlm.nih.gov/7968789/) | 1995 | Cohort | Medical and Pediatric Oncology | Spanish Pediatric Oncology Society protocol for stage III neuroblastoma using intensive induction chemotherapy |

---

## Additional Predicted Indication with Direct Supporting Evidence: Myeloid Leukemia

This candidate (TxGNN score 99.65%, evidence level L2) has weaker mechanistic novelty but stronger *direct* drug-specific evidence than neuroblastoma, and warrants parallel consideration.

**Clinical Trial**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07159620](https://clinicaltrials.gov/study/NCT07159620) | Phase 2 | Recruiting | 27 | Single-arm trial of venetoclax + azacitidine + chidamide + **vindesine** + dexamethasone in newly diagnosed ETP-ALL-like patients (explicitly names vindesine) |

**Literature (selected)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6957273](https://pubmed.ncbi.nlm.nih.gov/6957273/) | 1982 | Clinical study | Cancer Chemother Pharmacol | Single-agent vindesine in CML, CML blast crisis, and ANLL; rapid leukemic cell reduction in 31/36 patients |
| [274996](https://pubmed.ncbi.nlm.nih.gov/274996/) | 1978 | RCT (Phase 2) | Cancer Treatment Reports | Phase II vindesine trial for remission induction in acute leukemia and CML blast crisis; no cross-resistance with vincristine |
| [3857971](https://pubmed.ncbi.nlm.nih.gov/3857971/) | 1985 | Cohort | Cancer Treatment Reports | Vindesine + prednisone in 16 CML blast crisis patients; median chronic-phase duration 29 months |
| [6573959](https://pubmed.ncbi.nlm.nih.gov/6573959/) | 1983 | Cohort | Cancer Treatment Reports | Vindesine + prednisone in lymphoma and acute leukemia including CML blastic crisis; partial/complete responses observed |
| [3855698](https://pubmed.ncbi.nlm.nih.gov/3855698/) | 1985 | Cohort | Cancer Treatment Reports | Vindesine-prednisone in 8 CML blast crisis patients; complete remission in 3, partial in 3 |
| [9389357](https://pubmed.ncbi.nlm.nih.gov/9389357/) | 1997 | Review | Leukemia & Lymphoma | Review of vindesine's role in leukemia treatment, noting lack of cross-resistance with vincristine |

---

## Other Predicted Indications (Not Recommended for Further Action)

| Disease | TxGNN Score | Evidence Level | Recommendation | Reason |
|---------|------------|----------------|-----------------|--------|
| Ganglioneuroblastoma | 99.89% | L5 | Hold | No clinical trials or literature; pure model extrapolation |
| Vertebral anomalies / variable endocrine and T-cell dysfunction | 99.87% | L5 | Hold | Congenital syndrome with no biologically plausible mechanism for a cytotoxic chemotherapy agent |
| Retroperitoneal neoplasm | 99.86% | L4 | Hold | Anatomical classification spanning heterogeneous tumor types; evidence limited to historical case reports of cisplatin-based regimens, not vindesine-specific |

---

## Saudi Arabia Market Information

Vindesine currently has no marketing authorization or license record in Saudi Arabia (0 licenses on file).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid class) |
| Myelosuppression Risk | Dose-limiting toxicity; nadir at days 7–8 with recovery by days 11–13 (per literature on vindesine pharmacology) |
| Emetogenicity Classification | Low to moderate (typical of vinca alkaloid class) |
| Monitoring Items | CBC with differential, liver and renal function, neurological exam (severe neurotoxicity reported at higher bolus doses) |
| Handling Protection | Standard cytotoxic drug handling precautions required; vinca alkaloids are fatal if administered intrathecally and must never be prepared or dispensed in a manner allowing intrathecal use |

---

## Safety Considerations

Please refer to the package insert for safety information — no drug interaction, warning, or contraindication data is currently on file for vindesine.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Both viable candidates (neuroblastoma and myeloid leukemia) rest on decades-old, non-confirmatory studies (1978–2010) rather than modern trials designed to test the repurposing hypothesis directly, and vindesine is not currently marketed or licensed in Saudi Arabia. The evidence supports biological plausibility and historical clinical precedent, but not an immediate "Go" decision.

**To proceed, the following is needed:**
- Official package insert / SFDA-equivalent safety data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or manufacturer sources
- A modern, prospective trial (or at minimum a systematic review) specifically evaluating vindesine in neuroblastoma or myeloid leukemia, ideally tracking the ongoing NCT07159620 trial results
- Assessment of drug import/supply feasibility given the absence of any Saudi Arabia market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

