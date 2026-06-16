---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic used clinically to treat serious Gram-positive bacterial infections, including complicated skin infections, *Staphylococcus aureus* bacteremia, and right-sided infective endocarditis.
The TxGNN model predicts it may be effective for **Osteoarthritis** with a score of 99.86%, yet this appears to be a **false positive** — all **10 retrieved publications** relate to daptomycin treating bone and joint *bacterial infections*, not the degenerative joint disease known as osteoarthritis, and **0 clinical trials** have investigated this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-positive bacterial infections (skin/soft tissue infections, *S. aureus* bacteremia, right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed (0 registered products) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on published literature, daptomycin is a cyclic lipopeptide antibiotic that disrupts Gram-positive bacterial cell membrane integrity by binding to phosphatidylglycerol in a calcium-dependent manner, leading to membrane depolarisation and rapid bactericidal activity. It does not penetrate the cell wall and has no known direct action on mammalian cartilage, chondrocytes, or the inflammatory pathways driving osteoarthritis.

The TxGNN model's high prediction score most likely reflects a **knowledge graph artefact**: "osteoarthritis" and "osteoarticular infection" share overlapping semantic nodes in the biomedical knowledge graph (both involve joints and joint pathology). The 10 retrieved PubMed publications confirm this — all describe daptomycin's role in treating *bacterial infections of joints and prostheses* (periprosthetic joint infections, septic arthritis, osteomyelitis), none of which constitute evidence for treating osteoarthritis as a degenerative disease.

Osteoarthritis pathology involves cartilage matrix degradation, oxidative stress, mechanical wear, and low-grade synovial inflammation — none of which have any known pharmacological intersection with daptomycin's antibacterial mechanism. This prediction is therefore considered a **non-actionable false positive** for the osteoarthritis indication. Notably, the second-ranked prediction (rheumatoid arthritis, L4) carries a more plausible mechanistic rationale supported by 2025 animal studies and is discussed under Conclusion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for daptomycin in osteoarthritis.

---

## Literature Evidence

> ⚠️ **Important caveat**: All publications below relate to daptomycin treatment of *bone and joint bacterial infections* (periprosthetic joint infections, septic arthritis), **not** the degenerative joint condition osteoarthritis. These studies do not constitute evidence for the predicted repurposing indication.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospective Cohort | J Antimicrob Chemother | Daptomycin vs. standard therapy for osteoarticular infections associated with *S. aureus* bacteraemia — clinical outcomes comparison |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Case Series | J Antimicrob Chemother | Clinical efficacy and safety of daptomycin for hip and knee periprosthetic joint infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In Vitro Study | J Antibiotics | In vitro susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections to daptomycin and other antibiotics |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey | Int J Antimicrob Agents | Survey of infectious disease physicians on antibiotic preferences for prosthetic joint infections; daptomycin cited as alternative agent |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospective Cohort | Int Orthopaedics | Safety and efficacy of high-dose daptomycin combined with rifampicin for Gram-positive osteoarticular infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Retrospective Cohort | Surgical Infections | Microbiologic profile of staphylococci in osteoarticular infections over 10 years; daptomycin susceptibility profiled |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospective Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone, joint, and implant-associated Gram-positive infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry/Observational | Medicina Clinica | EU-CORE registry: Spanish experience with daptomycin across various Gram-positive infections including joint involvement |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Rep Orthopedics | *Corynebacterium striatum* septic arthritis in a patient referred for knee arthroplasty for osteoarthritis; daptomycin used as treatment |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM Case Reports | Septic arthritis due to *C. propinquum* in a native joint with underlying joint disease; daptomycin as part of treatment regimen |

---

## Saudi Arabia Market Information

Daptomycin has **no registered products** in Saudi Arabia (SFDA). There are currently 0 marketing authorizations on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: One published case report (PMID [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), *Am J Med Sci*, 2023) documents **daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis** — a secondary adverse effect arising from hyperuricaemia. This is a safety signal, not a therapeutic rationale. Clinicians should be aware that daptomycin itself can precipitate musculoskeletal complications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for osteoarthritis is assessed as a knowledge graph false positive — no mechanistic link exists between daptomycin's antibacterial action and osteoarthritis pathophysiology, no clinical trials have investigated this indication, and all retrieved literature addresses bone/joint *infections* rather than degenerative joint disease.

---

**Secondary Signal Worth Monitoring — Rheumatoid Arthritis (Rank 2, L4):**
Two 2025 publications (PMID [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/); PMID [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/)) report for the first time that daptomycin suppresses inflammatory cytokines (IL-6, TNF-α) and inhibits the NF-κB pathway in collagen-induced arthritis (CIA) mouse models, alleviating joint inflammation. A second group has synthesised daptomycin-derived cyclic lipopeptide analogues with improved anti-RA activity. While still at preclinical stage (L4), this mechanistic rationale is genuine and merits tracking as an early-stage research question.

**To proceed with either indication, the following is needed:**

- **MOA data** (DrugBank full record) to confirm pharmacological profile and flag off-target effects
- **SFDA package insert / safety data** to complete mandatory safety screening (currently Blocking data gap DG001)
- For the RA signal specifically:
  - Dose-response and PK/PD studies in inflammatory models
  - Toxicity profile at anti-inflammatory doses (daptomycin causes dose-dependent myopathy; anti-inflammatory doses may differ from antimicrobial doses)
  - Assessment of route compatibility (daptomycin is IV-only; RA therapy typically requires oral or SC routes for chronic use)
  - Phase 1 safety study before any Phase 2 efficacy evaluation can be designed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

