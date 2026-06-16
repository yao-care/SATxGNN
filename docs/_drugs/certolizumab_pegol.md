---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Certolizumab pegol (CZP, Cimzia®) is a PEGylated anti-TNF-α biologic approved in multiple countries for rheumatoid arthritis, Crohn's disease, psoriatic arthritis, and axial spondyloarthritis.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **3 clinical trials** and **8 publications** currently identified — however, a critical mechanistic paradox applies: the majority of identified literature describes CZP *causing* vasculitis as an adverse drug reaction, not treating it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis / Inflammatory Arthritis (Saudi Arabia regulatory record: none) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on contextual information from the included literature and trial records, certolizumab pegol is a PEGylated Fab' fragment of a recombinant humanized anti-TNF-α monoclonal antibody. Uniquely among TNF inhibitors, CZP lacks the Fc region — preventing complement fixation, Fc-receptor-mediated cytotoxicity, and active placental transfer. It selectively neutralizes both soluble and membrane-bound TNF-α, thereby suppressing downstream inflammatory mediators such as IL-6 and IL-8.

Rheumatoid vasculitis (RV) is a severe extra-articular complication of long-standing, seropositive rheumatoid arthritis. Its pathogenesis involves immune complex deposition in vessel walls, complement activation, and sustained TNF-α-driven vascular inflammation. Given that TNF-α is a central mediator of both synovial and systemic inflammatory cascades in RA, there is a biologically coherent rationale for a TNF inhibitor to reduce the immunological insult driving RV — and indeed, one published case report (PMID 34786446) documents CZP successfully treating leg ulcers caused by rheumatoid vasculitis.

However, a critical mechanistic paradox must be acknowledged upfront: anti-TNF agents, including CZP, are documented to **induce** paradoxical vasculitis as an adverse drug reaction through mechanisms including immune complex formation, altered TNF-dependent regulatory T-cell homeostasis, and interferon pathway upregulation. Six of the eight identified publications describe CZP-associated vasculitis as a harm rather than a benefit. This dual role — potential therapeutic and documented causative agent for vasculitis — represents a fundamental clinical ambiguity that makes the TxGNN prediction biologically interesting but clinically unresolved at this stage.

---

## Clinical Trial Evidence

No registered clinical trials directly evaluating certolizumab pegol for the treatment of rheumatoid vasculitis were identified. The three retrieved trials have low relevance (Grade C) to this indication:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Immunosuppressant management in rheumatology patients undergoing total shoulder arthroplasty; evaluates peri-operative drug holding strategies — no vasculitis treatment outcome |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | Observational | Completed | 184 | Real-world tocilizumab study in RA patients with inadequate DMARD response; records general RA outcomes with no vasculitis sub-analysis |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | Observational | Unknown | 750,000 | Pharmacovigilance study on risk of incident IMID in biologic-treated patients; safety monitoring in nature, not a vasculitis efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | CZP used to **treat** leg ulcers from rheumatoid vasculitis — the sole publication reporting CZP as a therapeutic agent for RV; clinical response observed |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Retrospective Cohort | RMD Open | Long-term follow-up of CZP in IMID-associated uveitis (N=80 patients, multicenter); supports CZP efficacy in immune-mediated vascular inflammation, not directly targeting RV |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Pharmacovigilance Analysis | RMD Open | Comparative infection frequency and type across immune-modulatory drugs from SmPC data; provides safety signal context for CZP class |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Adverse Event Case Report | Cureus | Anti-TNF-induced medium-vessel vasculitis in a 33-year-old female with seronegative RA switched to CZP — documents paradoxical vasculitis induction |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Adverse Event Case Report | J Clin Pharmacy & Therapeutics | Hypocomplementemic urticarial vasculitis (HUV) developing during CZP therapy for RA — first reported association between HUV and CZP |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Adverse Event Case Report | Proc Baylor Univ Med Ctr | Leukocytoclastic vasculitis as a drug reaction to CZP — first reported case of this reaction specific to CZP among TNF inhibitors |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Adverse Event Case Report | Mod Rheumatol Case Rep | Rapidly progressive glomerulonephritis after CZP initiation in a 30-year-old RA patient — possible autoimmune-mediated renal vasculitis |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Retrospective Case Series | Clinical Medicine & Research | Single-center adverse cutaneous event experience with biologics; includes vasculitis cases associated with TNF inhibitor class |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for certolizumab pegol in rheumatoid vasculitis sits at L4 (case report/mechanistic level only). More critically, 6 of 8 identified publications describe CZP as a **cause** of paradoxical vasculitis rather than a treatment, creating a fundamental benefit-risk ambiguity that must be resolved before this candidate advances.

**To proceed, the following is needed:**
- Systematic review or meta-analysis of published cases distinguishing CZP-*treated* RV from CZP-*induced* vasculitis, with characterization by vasculitis subtype (cutaneous leukocytoclastic, medium-vessel, renal)
- Formal MOA data from DrugBank (DG002 remediation) to define which RV immunological subtypes CZP's TNF-α pathway suppression would plausibly benefit versus harm
- Safety data from the SFDA/FDA/EMA package insert (DG001 remediation) to identify specific contraindications and warnings relevant to vascular adverse events
- Expert rheumatology consultation to evaluate whether RV subtype stratification (e.g., cutaneous-only vs. systemic/organ-threatening) could identify a safer, targetable patient population
- If a positive signal is confirmed: prospective registry or observational study design before considering a controlled trial

---

> **Note on Other High-Evidence Candidates:** While rheumatoid vasculitis (rank 1) is the focus of this report, the TxGNN prediction set also includes **Inflammatory Spondylopathy** (rank 3, L1 evidence, multiple completed Phase 3 RCTs including NCT01087762 and NCT02505542) and **Vertebral Disease** (rank 6, L1 evidence), both of which have substantially stronger clinical trial support for CZP. These candidates warrant priority consideration if the goal is near-term clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

