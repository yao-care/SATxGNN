---
layout: default
title: Cefprozil
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

# Cefprozil: From Respiratory Tract Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an oral second-generation cephalosporin antibiotic, historically used for the treatment of upper and lower respiratory tract infections, pharyngitis/tonsillitis, and skin and soft tissue infections.
The TxGNN model predicts it may be effective for **urinary tract infection (UTI)**, with **3 randomized controlled trials** and **9 publications** currently supporting this direction.
The mechanistic rationale is strong — cefprozil's cell-wall inhibition mechanism directly targets the most common UTI pathogens — and several head-to-head RCTs against cefaclor demonstrate comparable clinical cure rates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory tract infections (upper/lower), pharyngitis, tonsillitis, skin and soft tissue infections |
| Predicted New Indication | Urinary Tract Infection (UTI) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefprozil acts by binding to **penicillin-binding proteins (PBPs)** — the enzymes responsible for the final cross-linking step of bacterial peptidoglycan cell wall synthesis. By irreversibly inhibiting PBP1a, PBP2b, and PBP2x, it prevents cell wall assembly and leads to bacterial lysis. This mechanism is shared across all β-lactam antibiotics and is directly effective against organisms that depend on a rigid peptidoglycan cell wall for structural integrity.

The most common uropathogens responsible for uncomplicated UTIs — **Escherichia coli**, **Klebsiella pneumoniae**, and **Proteus mirabilis** — are Gram-negative Enterobacteriaceae that remain susceptible to second-generation oral cephalosporins. In vitro studies consistently demonstrate that cefprozil inhibits >80% of E. coli and K. pneumoniae clinical isolates at concentrations achievable in urine after standard oral dosing. Because cefprozil achieves high urinary concentrations through renal excretion, the pharmacokinetic profile aligns well with UTI treatment requirements.

The mechanistic link is therefore **direct and pharmacologically sound**: the same PBP inhibition that makes cefprozil effective against streptococcal and staphylococcal respiratory pathogens applies equally to Gram-negative uropathogens. This is not a speculative repurposing — multiple comparative RCTs conducted in the early 1990s explicitly evaluated cefprozil in UTI settings and demonstrated clinical cure rates equivalent to cefaclor (a then-established first-line agent), providing strong empirical validation for the TxGNN model's prediction.

---

## Clinical Trial Evidence

No dedicated registered clinical trials for cefprozil in urinary tract infection were identified in ClinicalTrials.gov or ICTRP at the time of data collection (April 2026). The existing comparative RCT evidence predates the mandatory trial registration era (pre-2000), which explains the absence from registries rather than reflecting a lack of clinical investigation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | RCT | J Antimicrob Chemother | Cefprozil 500 mg once daily vs cefaclor 250 mg TID in 102 adults with acute uncomplicated UTI; cure rates comparable between arms |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | RCT | Clinical Therapeutics | Multicenter randomized study (n≥2 yrs); cefprozil once daily vs cefaclor TID for 10 days; satisfactory clinical response rates similar between groups |
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | RCT | Antimicrob Agents Chemother | 108 college women with acute UTI; cefprozil 500 mg QD vs cefaclor 250 mg TID × 10 days; clinical cure 94%, bacterial cure 93–94% in both groups |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Review | Drugs | Comprehensive review of antibacterial activity, pharmacokinetics, and therapeutic potential; confirms good in vitro activity against common UTI pathogens including E. coli and Klebsiella |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Review | Pediatric Annals | Pediatric-focused review; notes cefprozil's favorable GI tolerability and once/twice-daily dosing advantage; describes activity relevant to UTI |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Review | Am Fam Physician | Comparative review of newer oral cephalosporins; positions cefprozil as effective for urinary tract infections with convenient twice-daily dosing |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Clinical Study | Jpn J Antibiotics | Pediatric PK/PD study; includes UTI cases; high urinary concentrations of cefprozil demonstrated after oral dosing |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Clinical Study | Jpn J Antibiotics | 21 pediatric patients with bacterial infections including 3 UTI cases; bacterial eradication achieved in all culture-confirmed cases |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In Vitro | Chemotherapy | 637 clinical isolates from Taiwan; cefprozil inhibited >80% of E. coli and K. pneumoniae at 8 mg/L; activity comparable to other oral cephalosporins |

---

## Saudi Arabia Market Information

Cefprozil currently has **no registered authorizations** in Saudi Arabia (SFDA). The drug is not marketed in the Saudi market, and no product licenses were identified in the regulatory database.

---

## Safety Considerations

Detailed package insert warnings and contraindications for Saudi Arabia are not yet available in the current evidence pack (SFDA package insert data pending). Please refer to the **originator package insert and international SmPC** for comprehensive safety information including:

- Hypersensitivity reactions (cross-reactivity with other β-lactams; caution in penicillin-allergic patients)
- Clostridium difficile-associated diarrhea (applicable to all oral antibiotics)
- Renal dose adjustment requirements
- CNS effects at high doses (rare)

No drug-drug interaction data was identified in the DDI database query. Interactions typical for cephalosporins (e.g., warfarin potentiation, reduced renal clearance with probenecid) should be considered based on drug class.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three independent RCTs conducted in the 1990s demonstrated that cefprozil achieves clinical and bacterial cure rates equivalent to cefaclor in acute uncomplicated UTI in both adults and children, and the mechanistic basis (PBP inhibition targeting Enterobacteriaceae) is scientifically sound and well-characterized.

**To proceed, the following is needed:**

- **SFDA registration pathway**: Cefprozil is not currently marketed in Saudi Arabia; a full dossier submission (MAA) or import authorization process would be required before clinical use
- **Contemporary susceptibility data**: Updated antibiogram data from Saudi Arabia-specific clinical isolates to confirm cefprozil MICs against current local E. coli and Klebsiella strains, particularly given rising ESBL prevalence
- **SFDA package insert**: Obtain and review the complete Saudi Arabia-applicable label for definitive warnings, contraindications, and dosing guidance
- **Scope clarification**: Confine use to **uncomplicated lower UTI** (cystitis) in otherwise healthy adults — the existing RCT evidence does not support use in complicated UTI, pyelonephritis, or catheter-associated UTI
- **Antimicrobial stewardship alignment**: Confirm that cefprozil is positioned within local UTI treatment guidelines and does not displace agents preferred for antimicrobial stewardship purposes (e.g., nitrofurantoin or fosfomycin for uncomplicated cystitis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

