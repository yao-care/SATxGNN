---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Abatacept (Orencia) is a selective T-cell costimulation modulator approved globally for rheumatoid arthritis (RA), blocking the CD28–CD80/86 co-stimulatory signal required for full T-cell activation.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** — a severe extraarticular complication of RA —
with **1 clinical trial registration** and **20 associated publications** identified, though evidence is predominantly case reports and narrative reviews rather than controlled trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis (globally approved; not registered in Saudi Arabia) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Abatacept is a fusion protein composed of the Fc region of IgG1 linked to the extracellular domain of CTLA-4. By binding CD80 and CD86 on antigen-presenting cells, it competitively blocks the CD28 co-stimulatory signal that T cells require for full activation. This selectively suppresses Th1 and Th17 pro-inflammatory subsets and indirectly reduces B-cell help and autoantibody production — the mechanism underlying its established efficacy in RA synovitis. Detailed MOA data from DrugBank was not available in this pack; the above is reconstructed from published case report descriptions (PMID 29930884, PMID 22124545).

Rheumatoid vasculitis (RV) is a serious extraarticular manifestation of long-standing seropositive RA. Its pathology centers on immune-complex deposition and T-cell-mediated vascular wall inflammation — the same CD28-driven adaptive immune axis that drives joint destruction in RA. Because RV and RA share this T-cell activation backbone, abatacept's mechanism maps plausibly onto RV. Multiple case reports describe clinical improvement or rapid symptom resolution following abatacept administration in biopsy-confirmed RV patients who had failed TNF inhibitors, IL-6 inhibitors, and steroids.

One important pharmacovigilance caveat must be highlighted: PMID 27052429 documents *new-onset* RV emerging **during** abatacept therapy, with subsequent improvement only after switching to rituximab. This paradoxical signal, combined with a separate case of ANCA-associated nephritis developing during abatacept treatment (PMID 36418100), underscores that the immunological relationship is not straightforward. ANCA-associated vasculitis in particular depends less on CD28 co-stimulation, meaning abatacept's benefit may be restricted to purely T-cell-driven RV subtypes. No prospective or controlled trial has tested abatacept specifically for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing elective shoulder arthroplasty; compares standard vs. shortened hold times for immunosuppressants including abatacept — not a vasculitis efficacy study |

> No clinical trials directly evaluating abatacept as a treatment for rheumatoid vasculitis are currently registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | Case series / Narrative review | *Cureus* | Abatacept used as therapeutic alternative for RV in a patient where rituximab (standard of care) was contraindicated due to common variable immunodeficiency; describes CTLA4-Ig mechanism rationale |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | Case report | *Modern Rheumatology* | Rapid clinical improvement of biopsy-confirmed RV with abatacept after sequential failure of methotrexate, TNF inhibitors, steroids, plasmapheresis, and IL-6 inhibitor |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | *Journal of Clinical Medicine* | Comprehensive overview of RA-associated episcleritis and scleritis; discusses management escalation to biologics including abatacept in refractory cases |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | Review | *Best Practice & Research Clinical Rheumatology* | CNS vasculitis, rheumatoid nodules, and meningitis in RA; examines biological agent implications for neurological and vascular extraarticular disease |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | Case series / Review | *Ophthalmic Plastic & Reconstructive Surgery* | Bilateral orbital vasculitis with eosinophilic infiltrate occurring in a patient already on abatacept; disease progressed despite cyclophosphamide, illustrating treatment complexity |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | Case report | *Joint Bone Spine* | ⚠️ **Negative signal**: New-onset RV developing *during* abatacept therapy; improvement achieved only after switching to rituximab |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case report | *Internal Medicine (Tokyo)* | ANCA-associated nephritis with MPO-ANCA elevation emerging during concurrent abatacept + adalimumab treatment; subsequently attenuated by tocilizumab |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort / Review | *Annals of the Rheumatic Diseases* | Serial ANA testing utility for predicting bDMARD-induced lupus and vasculitis in RA patients; includes signal data from abatacept-treated cohort |
| [41117362](https://pubmed.ncbi.nlm.nih.gov/41117362/) | 2026 | Commentary / Review | *European Journal of Clinical Investigation* | Early diagnostic and therapeutic approaches for inflammatory/autoimmune rheumatic diseases; addresses large-vessel vasculitis in the context of RA spectrum diseases |
| [24493331](https://pubmed.ncbi.nlm.nih.gov/24493331/) | 2015 | Case-based review | *Clinical Rheumatology* | Off-label abatacept use in myositis; reviews T-cell co-stimulation blockade rationale for autoimmune rheumatic conditions beyond RA |

---

## Saudi Arabia Market Information

Abatacept is **not currently registered** with the Saudi Food and Drug Authority (SFDA). No product authorizations were identified in the regulatory database query (query date: 2026-03-29). Market entry would require a new SFDA registration dossier.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Pharmacovigilance signals identified in this evidence review:**
> - **Paradoxical vasculitis**: One case report (PMID 27052429) describes new-onset rheumatoid vasculitis emerging during abatacept treatment, resolving only after switching to rituximab.
> - **ANCA-associated nephritis**: One case (PMID 36418100) documents MPO-ANCA elevation and pauci-immune crescentic glomerulonephritis developing during abatacept therapy.
> These events suggest that immune dysregulation under CD28 blockade may occasionally precipitate rather than suppress vascular inflammation in susceptible individuals.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic basis for abatacept in rheumatoid vasculitis is biologically plausible — both conditions share a CD28-driven T-cell activation mechanism — and isolated case reports confirm clinical responses in patients who had failed multiple prior therapies. However, the entire evidence base consists of case reports and reviews (Evidence Level L3), no controlled trials exist for this specific indication, and at least one paradoxical worsening signal has been documented. This combination places abatacept in the research hypothesis stage, not ready for clinical implementation without further prospective data.

**To proceed, the following is needed:**
- Prospective observational cohort or registry-based study specifically enrolling patients with biopsy-confirmed rheumatoid vasculitis
- Comparative effectiveness data versus rituximab (current de facto standard of care for RV) — head-to-head or propensity-matched registry data
- Patient stratification criteria to distinguish T-cell-driven RV (where abatacept may help) from ANCA-associated or immune-complex-dominant subtypes (where benefit is uncertain)
- Full MOA and pharmacology data from DrugBank to complete the mechanistic analysis
- SFDA registration strategy for the foundational RA indication as a prerequisite for any Saudi Arabia development pathway
- Safety monitoring plan addressing paradoxical vasculitis exacerbation and ANCA-associated renal events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

