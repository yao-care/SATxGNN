---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Inflammatory Arthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor with established use globally for inflammatory arthritis conditions (osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis), though it currently holds no market authorisation in Saudi Arabia.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** — a broad category encompassing ankylosing spondylitis and axial spondyloarthritis — with **19 clinical trials** and **20 publications** supporting this direction, reaching the highest evidence grade (L1) in this evaluation.
This is the strongest actionable signal from the current prediction set; all other top-ranked predictions carry L5 evidence and a Hold decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Saudi Arabia |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not captured in this Evidence Pack. Based on well-established pharmacology, celecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor that blocks prostaglandin synthesis at sites of inflammation without meaningfully inhibiting the constitutively expressed COX-1 isoform. This selectivity produces anti-inflammatory and analgesic effects while substantially reducing the upper gastrointestinal toxicity associated with non-selective NSAIDs — a key differentiator in chronic inflammatory disease management.

Inflammatory spondylopathy — including ankylosing spondylitis (AS) and axial spondyloarthritis (axSpA) — is mechanistically driven by COX-2-mediated prostaglandin overproduction, which sustains periarticular inflammation, sacroiliac joint enthesitis, and the progressive vertebral ligament ossification that leads to ankylosis. NSAIDs are the established first-line pharmacological treatment for this disease class, and celecoxib has been studied in this context across multiple completed Phase 3 and Phase 4 randomised controlled trials in thousands of patients.

What elevates this prediction beyond standard NSAID repositioning is a 2025 systematic review and meta-analysis (PMID 39757202) that identifies celecoxib as the **only NSAID** capable of inhibiting radiographic bone progression in spondyloarthritis — an effect distinct from its prostaglandin-blocking activity and possibly mediated by COX-2-specific signalling in osteoblast differentiation. This structural protective potential substantially strengthens the mechanistic and clinical rationale, positioning celecoxib not merely as a symptomatic agent but as a potential disease-modifier in inflammatory spondylopathy.

---

## Clinical Trial Evidence

Ten trials selected from 19 retrieved; prioritised by direct celecoxib involvement and completed Phase 3–4 design.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | Landmark dose-comparison RCT: celecoxib 200 mg QD vs 200 mg BID vs diclofenac over 12 weeks in AS; established relative dosing and non-inferiority to diclofenac |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Multicenter double-blind RCT in Chinese AS patients: celecoxib vs diclofenac SR with 6-week extension at 400 mg; demonstrated efficacy and safety in Asian population |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Confirmatory RCT: celecoxib 200 mg QD vs 400 mg QD vs diclofenac TID in AS over 12 weeks; confirmed results from prior 6-week trial |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multicenter open-label RCT: celecoxib alone vs etanercept alone vs combination in active AS over 54 weeks; used MRI SPARCC sacroiliac joint scoring as primary endpoint |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: celecoxib added to golimumab vs golimumab alone in r-axSpA over 2 years; evaluated NSAIDs' contribution to structural spinal protection under anti-TNF therapy |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | Pilot study examining NSAID effects on MRI-detected inflammatory lesions in axial SpA; biological activity confirmation |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 vs non-selective COX inhibitors in axSpA; assessed disease activity and HRQoL; terminated before target enrolment |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Double-blind 6-week head-to-head comparison of 4 NSAIDs in axial SpA; terminated early due to low enrolment |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Completed | 547 | Post-marketing real-world study of etoricoxib and celecoxib use patterns in routine rheumatology practice in France |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Naxozol vs celecoxib in OA/RA/AS: celecoxib used as active comparator for gastro-protection and pain relief benchmarking |

---

## Literature Evidence

Ten publications selected from 20 retrieved; prioritised by study type (RCT / meta-analysis > cohort > review).

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review / Meta-analysis | BMB Reports | Celecoxib identified as the **only NSAID** to inhibit radiographic bone progression in SpA; proposed COX-2-specific mechanism independent of prostaglandin suppression |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Comprehensive synthesis of meta-analyses on celecoxib safety in chronic musculoskeletal conditions; supports a favourable cardiovascular and GI risk profile at recommended doses |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT (Head-to-head) | Clinical Rheumatology | Imrecoxib vs celecoxib in axSpA: both agents reduced sacroiliac joint inflammation; changes in bone metabolism and angiogenesis markers correlated with clinical response |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT (CONSUL Trial) | Annals of the Rheumatic Diseases | Adding celecoxib to golimumab did not significantly reduce radiographic spinal progression vs golimumab alone over 2 years in r-axSpA; important for patient selection in combination therapy |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Randomised comparison of imrecoxib vs celecoxib in axSpA; both effective; serum DKK-1 levels correlated with imaging SPARCC scores, highlighting biomarker potential |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | Journal of Rheumatology | Foundational RCT establishing celecoxib efficacy and tolerability in AS; formed basis for regulatory approvals in AS across multiple markets |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Cohort / RWE | Scandinavian Journal of Rheumatology | Nationwide retrospective cohort in Korea: cardiovascular and GI bleeding risk comparable between celecoxib and nsNSAIDs in AS patients |
| [32955700](https://pubmed.ncbi.nlm.nih.gov/32955700/) | 2021 | Biomarker Cohort | Irish Journal of Medical Science | IL-1β, IL-6, and IL-17A as predictive biomarkers for clinical response to celecoxib in AS; potential for precision patient selection |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2016 | Case-Control / RWE | Medicine | Taiwan NHI database study (n = 4,829 AS patients): celecoxib and sulfasalazine associated with reduced risk of coronary artery disease in AS |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Comprehensive clinical review of celecoxib for OA, RA, and AS; remains the most-cited overview of celecoxib's evidence base across inflammatory arthropathies |

---

## Saudi Arabia Market Information

Celecoxib currently holds **no market authorisation** in Saudi Arabia. No approved product licences, dosage forms, or indication records are on file in this database. Note that celecoxib (Celebrex®) is approved in multiple other jurisdictions (USA, EU, Japan, Taiwan) for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute pain, and primary dysmenorrhoea.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug-drug interaction data were not available in this Evidence Pack. Given that celecoxib is a COX-2 selective inhibitor, prescribers should be aware of the well-known class effects (cardiovascular risk at high doses/prolonged use, renal function monitoring, sulfonamide allergy cross-reactivity) until a formal pharmacovigilance dossier is compiled for the Saudi Arabia submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 and Phase 4 RCTs demonstrate celecoxib's efficacy and safety in ankylosing spondylitis and axial spondyloarthritis — the core conditions within inflammatory spondylopathy — and a 2025 meta-analysis uniquely positions celecoxib as the only NSAID with structural bone-protective effects in this disease class, supporting disease-modifying potential beyond symptomatic relief.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate Saudi SFDA market authorisation application; leverage existing approvals in the EU/US/Japan as reference
- **Safety dossier**: Compile formal warning and contraindication data (cardiovascular, renal, sulfonamide hypersensitivity) from the approved package insert for inclusion in evaluation
- **MOA documentation**: Obtain full pharmacological profile from DrugBank (COX-2 selectivity ratio, PK/PD parameters) to complete mechanistic link analysis
- **Patient stratification plan**: Define selection criteria by axSpA subtype (radiographic vs non-radiographic), cardiovascular risk profile, and prior NSAID failure status
- **Combination therapy guidance**: Clarify the role of celecoxib alongside TNF inhibitors in light of CONSUL trial results (structural protection benefit was not demonstrated in combination)
- **Local epidemiology**: Assess prevalence of inflammatory spondylopathy in Saudi Arabia to estimate patient population and health economic impact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

