---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab (Humira) is a fully human anti-TNF-α monoclonal antibody, widely established in the treatment of rheumatoid arthritis and related inflammatory conditions.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis (RV)**, a severe extra-articular manifestation of RA driven by immune complex deposition and TNF-α–mediated vascular inflammation.
Current evidence includes **5 clinical trials** (none with RV as primary endpoint) and **20 publications** (including 1 systematic review and 1 cohort study), placing this at an exploratory research stage with a bidirectional mechanistic caveat: adalimumab may both treat and paradoxically induce vasculitis-like reactions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record (not marketed in Saudi Arabia) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (MOA: Data Gap). Based on known information, adalimumab is a fully human IgG1 monoclonal antibody that directly neutralises both soluble and membrane-bound TNF-α, suppressing the NF-κB–driven downstream inflammatory cascade. Its efficacy across rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis is well established, and the mechanistic pathway is directly relevant to vasculitis driven by TNF-α.

Rheumatoid vasculitis is one of the most serious extra-articular manifestations of long-standing RA, characterised by immune complex deposition in vessel walls and sustained TNF-α–mediated endothelial inflammation. Because adalimumab's target (TNF-α) is a central driver of both RA-associated synovitis and the systemic vascular inflammation in RV, mechanistic bridging from the original indication to this new one is conceptually sound. A 2021 systematic review (PMID 33058033) specifically evaluated biological agents — including anti-TNF drugs — in RV treatment and confirmed biological plausibility.

However, a critical mechanistic paradox must be acknowledged: TNF-α also performs immune-regulatory, protective functions. Complete TNF-α blockade can impair immune complex clearance and has been associated with paradoxical vasculitis induction. Published cohort and case data (PMID 28123776; PMID 28719435) show that TNF inhibitors — including adalimumab — can themselves trigger leukocytoclastic and lupus-like vasculitis-like events in RA patients. This bidirectional risk profile makes patient selection and monitoring essential before any clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large retrospective study of IMID patients on biologics (including adalimumab); may capture vasculitis events (therapeutic and adverse) as indirect data |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multinational observational study of tocilizumab in RA after inadequate DMARD/biologic response; RA population may contain RV subgroup but RV is not a primary endpoint |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; no direct relevance to RV treatment |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional descriptive study of biologic DMARD patterns in Chinese RA patients; no RV efficacy data |

> **Note:** No clinical trials were identified with rheumatoid vasculitis as a primary endpoint. NCT05111743 (brolucizumab for AMD) was excluded as it involves an unrelated drug and indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-based systematic review on use of biological agents (including anti-TNFs) in RV treatment; confirms biological therapy as part of therapeutic armamentarium for this severe RA complication |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort Study | RMD Open | BSRBR-RA registry data comparing risk of lupus-like and vasculitis-like events in TNFi-treated vs nbDMARD-treated RA patients; quantifies bidirectional vasculitis risk with adalimumab |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Systematic Review | Clinical and Experimental Rheumatology | Systematic comparison of vasculitis characteristics in RA patients on anti-TNF vs not (n=2,707 patients, 18 vasculitis cases); key reference for understanding vasculitis in anti-TNF context |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 42-year-old female with RA-associated digital vasculitis (necrotising fingertip ulcers); responded well to adalimumab — direct evidence of therapeutic benefit |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis in RV patient 8 months after adalimumab dose reduction; suggests adalimumab may be required to maintain RV remission — withdrawal risk |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis emerging during combined abatacept and adalimumab therapy for RA; illustrates risk of autoimmune vasculitis as adverse effect during anti-TNF therapy |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | American Journal of Dermatopathology | First reported case of leukocytoclastic vasculitis with cutaneous perivascular hemophagocytosis following adalimumab initiation for RA; documents paradoxical vasculitis induction |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | Review of RA-associated episcleritis and scleritis (ocular vasculitis manifestations); discusses management including biologics, contextually relevant to RV extra-articular spectrum |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Néphrologie & Thérapeutique | ANCA-associated extracapillary necrotising glomerulonephritis during adalimumab therapy for RA; adds to the paradoxical vasculitis adverse event literature |
| [24558628](https://pubmed.ncbi.nlm.nih.gov/24558628/) | 2013 | Case Report | Case Reports in Nephrology | Adalimumab therapy exacerbating IgA nephropathy and inducing lupus autoantibodies in a psoriasis patient; demonstrates spectrum of autoimmune vascular adverse effects |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Editorial note:** All safety fields in this Evidence Pack are marked as unavailable (Data Gap). Given the bidirectional mechanistic risk identified in the literature — where adalimumab can both treat and paradoxically induce vasculitis-like reactions (PMID 28123776, PMID 28719435) — a thorough safety review of the current prescribing information is strongly recommended before any clinical use in rheumatoid vasculitis.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between TNF-α inhibition and rheumatoid vasculitis treatment is biologically plausible and supported by one systematic review and several case reports, reaching Level L3 evidence — but no dedicated RCT with RV as primary endpoint exists. Critically, the same drug class carries a documented risk of paradoxical vasculitis induction, which introduces a clinically important uncertainty that a Research Question designation appropriately reflects at this stage.

**To proceed, the following is needed:**
- **Detailed MOA and safety data**: Retrieve and review the full prescribing information (package insert) to characterise confirmed warnings, contraindications, and drug-drug interactions — currently all flagged as data gaps
- **Dedicated RV-focused prospective study**: The existing evidence is indirect; a phase 2 study specifically enrolling patients with confirmed rheumatoid vasculitis (ACR/EULAR criteria) and using validated RV activity endpoints (e.g., Birmingham Vasculitis Activity Score) is required to move beyond L3
- **Biomarker stratification plan**: Given paradoxical vasculitis risk, patient selection should include baseline ANA, ANCA, and immune complex profiling to identify those at risk for adverse vasculitis induction
- **Saudi Arabia regulatory pathway assessment**: With 0 current authorisations, a market entry strategy and regulatory feasibility analysis would be prerequisite to any local clinical programme
- **Safety monitoring protocol**: Define rules for early discontinuation (e.g., rising ANA titres, new ANCA positivity, skin biopsy surveillance) before any investigational use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

