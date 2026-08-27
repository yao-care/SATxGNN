---
layout: default
title: Fosfomycin
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Broad-Spectrum Antibacterial Therapy to Gonococcal Urethritis

## One-Sentence Summary

Fosfomycin is a broad-spectrum antibacterial agent whose established clinical role (per the evidence gathered, including complicated UTI/pyelonephritis trials) is treating gram-negative bacterial infections of the urinary tract.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis**, with **0 registered clinical trials** but **6 supporting publications** (including 1 RCT) currently backing this direction — evidence that is real but dated, and complicated by current antimicrobial resistance trends.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Saudi Arabia market authorization on file to extract an approved indication text from |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, severity High). Based on the information available in the evidence pack, fosfomycin is a bactericidal antibiotic that inhibits an early, distinct step in bacterial cell wall synthesis — blocking the MurA enzyme and thereby peptidoglycan precursor formation. This mechanism is referenced in the supporting clinical trial literature for related indications (e.g., the ZEUS Phase 2/3 trial for complicated UTI, PMID 30861061), and it is the same target that underlies fosfomycin's established antibacterial spectrum.

*Neisseria gonorrhoeae* is a gram-negative diplococcus with a typical peptidoglycan cell wall, making MurA a mechanistically valid target for this organism. Fosfomycin's broad gram-negative coverage — already demonstrated in genitourinary infections such as complicated UTI and pyelonephritis — extends plausibly to gonococcal urethritis on the same structural basis.

That said, the mechanistic rationale comes with an important caveat: under current global antimicrobial resistance trends, most treatment guidelines no longer list fosfomycin as first-line therapy for gonorrhea. Any repurposing pathway would need to be paired with local susceptibility/resistance monitoring rather than treated as a straightforward mechanism-driven extension.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clinical Microbiology and Infection | Open-label RCT in 126 men with uncomplicated gonococcal urethritis; fosfomycin trometamol 3g given on days 1, 3, and 5 was evaluated against comparator therapy |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical study | Chemotherapy | 70 patients with acute/subacute gonococcal urethritis treated with IM fosfomycin; 86–92% bacteriological and clinical cure rates depending on dosing regimen |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Clinical/Bacteriological study | Chemotherapy | 959 patients across multiple Spanish hospitals treated for various infections, including gonococcal urethritis, confirming broad-spectrum in vitro and clinical activity |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Cohort (secondary analysis) | Sexually Transmitted Infections | Secondary analysis of the NABOGO trial assessing spontaneous clearance of asymptomatic anogenital and pharyngeal *N. gonorrhoeae* infections (not a fosfomycin efficacy study) |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Review | Zhonghua Nan Ke Xue (National Journal of Andrology) | Review of diagnosis and treatment of male genitourinary infection involving non-gonococcal *Neisseria* species |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Case report | Journal Français d'Ophtalmologie | Case of gonococcal conjunctivitis with corneal perforation following urethritis, resistant to penicillins/tetracyclines/fluoroquinolones, managed with parenteral antibiotics |

## Saudi Arabia Market Information

No market authorizations on file — fosfomycin is not currently marketed in Saudi Arabia (0 registered licenses).

## Safety Considerations

Please refer to the package insert for safety information. Note that TFDA/SFDA package insert warnings and contraindications are currently a blocking data gap (DG001) that prevents completion of the S1 safety pre-assessment for this candidate.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One RCT plus several older clinical studies support fosfomycin's efficacy against gonococcal urethritis, and the mechanistic rationale (MurA inhibition against a peptidoglycan-walled organism) is sound. However, evidence is dated (most studies from the 1970s–2016), current resistance trends limit fosfomycin's standing as first-line gonorrhea therapy, and there is no existing market authorization in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (blocking S1 safety assessment — DG001)
- Detailed mechanism of action data (DG002)
- Local/regional antimicrobial susceptibility data for *N. gonorrhoeae* against fosfomycin
- Regulatory pathway assessment, since the drug currently has zero market authorizations in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

