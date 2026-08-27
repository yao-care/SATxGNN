---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

Using the report structure from the drug-repurposing prompt. One judgment call up front, stated transparently: `predicted_indications[0]` (brachydactyly-syndactyly syndrome) and ranks 2/3/4/6/7/9/10 are explicitly flagged in their own `repurposing_rationale` as ultra-rare genetic syndromes with **zero** clinical/literature evidence ("model noise" / "high risk false positive"). The only two candidates with real evidence are rank 5 (osteoarthritis, L3/S1/Research Question) and rank 8 (spondyloarthropathy susceptibility, L3/**S2/Proceed with Guardrails** — the highest decision stage in the whole pack, and clinically grounded since sulfasalazine is an established DMARD for peripheral spondyloarthritis). I built the report around rank 8 rather than blindly following array index 0, since a report on a zero-evidence rare-disease node would not be useful.

---

# Sulfasalazine: From Rheumatoid Arthritis / Inflammatory Bowel Disease to Spondyloarthropathy

## One-Sentence Summary

> Sulfasalazine is a long-established DMARD used clinically for rheumatoid arthritis and inflammatory bowel disease (ulcerative colitis).
> The TxGNN model predicts it may be effective for **Spondyloarthropathy (genetic susceptibility node)**,
> a plausible extension given sulfasalazine's existing real-world use in peripheral spondyloarthritis, though the **13 publications** identified are mostly disease-mechanism/genetics reviews rather than direct treatment trials, and **no clinical trials** for this specific indication were found.

*(Note: TxGNN's highest-ranked outputs — rank 1–4, 6, 7, 9, 10 — are all ultra-rare congenital syndromes with no supporting evidence and are annotated in the source data itself as likely model noise; they are not discussed further here.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / ulcerative colitis (established clinical use; not present in this evidence pack — see Data Gaps) |
| Predicted New Indication | Spondyloarthropathy (susceptibility) |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, sulfasalazine is metabolized into 5-aminosalicylic acid (5-ASA) and sulfapyridine, and acts as an NF-κB and prostaglandin/leukotriene inhibitor with combined local (gut) and systemic anti-inflammatory effects. It is already a first-line, guideline-supported DMARD for peripheral forms of spondyloarthritis — including reactive arthritis, psoriatic arthritis, and inflammatory-bowel-disease-associated arthritis — which are clinically and mechanistically part of the same spondyloarthropathy disease family being predicted here.

The TxGNN node in question, "spondyloarthropathy, susceptibility to," represents a genetic-predisposition concept rather than the disease itself, which explains why the literature returned is dominated by pathogenesis, genetic-association, and disease-classification reviews rather than sulfasalazine treatment trials. Still, one directly relevant genetic-pharmacology study (PMID 25413361) examines NAT2 polymorphisms and their correlation with sulfasalazine-induced adverse reactions specifically in ankylosing spondylitis patients — indicating the drug is already used in this population.

Overall, the prediction is mechanistically reasonable and consistent with existing off-label/guideline practice, but the evidence base here is indirect (genetics/epidemiology of susceptibility, not treatment efficacy), so it should be read as reinforcing an already-known clinical use rather than establishing a genuinely novel indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25413361](https://pubmed.ncbi.nlm.nih.gov/25413361/) | 2014 | Genetic association | BMC Pharmacology & Toxicology | NAT2 polymorphisms in Han Chinese ankylosing spondylitis patients correlate with sulfasalazine-induced adverse drug reactions |
| [20436080](https://pubmed.ncbi.nlm.nih.gov/20436080/) | 2010 | Cohort | The Journal of Rheumatology | Long-term follow-up of undifferentiated spondyloarthritis patients |
| [10910178](https://pubmed.ncbi.nlm.nih.gov/10910178/) | 2000 | Review | Current Opinion in Rheumatology | Overview of juvenile spondyloarthropathies, cytokine and imaging findings |
| [19938189](https://pubmed.ncbi.nlm.nih.gov/19938189/) | 2009 | Review | World Journal of Gastroenterology | Rheumatic manifestations of IBD, including shared immune pathways relevant to sulfasalazine's dual GI/joint use |
| [18166219](https://pubmed.ncbi.nlm.nih.gov/18166219/) | 2008 | Review | Seminars in Arthritis and Rheumatism | Classification, genetic susceptibility, pathology and treatment response across the spondyloarthritis spectrum |
| [15922688](https://pubmed.ncbi.nlm.nih.gov/15922688/) | 2005 | Review | The American Journal of Medicine | Update on spondyloarthritis pathogenesis and management, including HLA-B27 |
| [1419506](https://pubmed.ncbi.nlm.nih.gov/1419506/) | 1992 | Review | Current Opinion in Rheumatology | Juvenile spondyloarthropathies and immunogenetic associations |
| [34599048](https://pubmed.ncbi.nlm.nih.gov/34599048/) | 2022 | Review (tangential) | The Journal of Rheumatology | Interplay between COVID-19 and spondyloarthritis or its treatment |
| [26061056](https://pubmed.ncbi.nlm.nih.gov/26061056/) | 2015 | Review (tangential) | Puerto Rico Health Sciences Journal | Rheumatic manifestations in Chikungunya infection, differential relevance to reactive/spondyloarthritis |
| [8105815](https://pubmed.ncbi.nlm.nih.gov/8105815/) | 1993 | Review | APMIS | Role of antibiotics (not sulfasalazine) in reactive arthritis pathogenesis |

---

## Saudi Arabia Market Information

Sulfasalazine currently has no marketing authorization on file in Saudi Arabia (0 authorizations; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA package-insert warnings/contraindications data (DG001) is flagged as a **Blocking** data gap in this evidence pack — it must be resolved before this candidate can enter the S1 safety screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The disease-level evidence (established off-label DMARD use in peripheral spondyloarthritis, one direct pharmacogenetic study) supports moving toward "Proceed with Guardrails," but the pack's own Blocking-severity gap (DG001 — no TFDA package insert data) means safety screening (S1) has not been completed. A recommendation cannot be finalized without it.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to unblock S1 safety evaluation (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Direct sulfasalazine treatment-efficacy studies in spondyloarthritis/peripheral SpA populations (current literature is mostly genetics/pathogenesis review, not interventional)
- Saudi Arabia market-authorization pathway assessment, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

