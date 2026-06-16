---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatin: From Carbapenem Adjunct to Staphylococcus Aureus Infection

## One-Sentence Summary

Cilastatin is a renal dehydropeptidase-1 (DHP-1) inhibitor with no independent antimicrobial activity; it is always co-administered with imipenem as the fixed combination **imipenem/cilastatin** to prevent renal tubular degradation of imipenem and maintain effective systemic drug concentrations.
The TxGNN model predicts that the imipenem/cilastatin combination may be effective for **Staphylococcus aureus infection**, with **3 clinical trials** and **20 publications** currently providing supporting context.
Evidence quality, however, is predominantly observational and historically dated, placing this prediction at the research-question stage rather than ready for direct clinical deployment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No standalone approved indication; cilastatin functions solely as a DHP-1 inhibitor co-drug within the imipenem/cilastatin combination |
| Predicted New Indication | Staphylococcus aureus infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cilastatin itself has no antimicrobial mechanism — it competitively inhibits renal DHP-1, the enzyme responsible for degrading imipenem in proximal renal tubules. Without cilastatin, imipenem would be rapidly hydrolysed in the kidney, producing nephrotoxic metabolites and failing to achieve therapeutic systemic concentrations. All clinical evidence for "cilastatin" therefore belongs entirely to the **imipenem/cilastatin combination**, and this repurposing assessment must be understood in that context.

Imipenem, the active partner, binds penicillin-binding proteins (PBPs) and inhibits bacterial cell wall synthesis. It has documented in vitro and in vivo activity against methicillin-susceptible *Staphylococcus aureus* (MSSA), and early clinical studies (1986–1994) confirmed clinical cure in soft tissue, bacteraemic, and skeletal MSSA infections. The mechanistic bridge is thus well-founded for MSSA. For methicillin-resistant *S. aureus* (MRSA), however, the picture is considerably more complex: MRSA expresses PBP2a (encoded by *mecA*), which confers intrinsic resistance to all β-lactams including carbapenems. Imipenem is bacteriostatic rather than bactericidal against MRSA at clinically achievable concentrations, substantially limiting monotherapy utility.

The residual interest in imipenem/cilastatin for MRSA stems from observed in vitro and in vivo **synergy with partner agents** — particularly arbekacin, fosfomycin, cefotiam, and vancomycin — where adding imipenem reduces MICs and improves killing kinetics. A 2020 case commentary in *Antimicrobial Agents and Chemotherapy* described successful salvage therapy with imipenem/cilastatin + fosfomycin for a refractory MRSA bacteraemic case where both vancomycin and daptomycin had failed, illustrating the niche role of this combination in individualised rescue situations. TxGNN likely captures this relationship through knowledge-graph edges linking imipenem/cilastatin to *S. aureus*-associated infection nodes, but the underlying evidence does not yet support a defined, registrable indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | IMI/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP adults; imipenem/cilastatin serves as backbone active comparator, confirming its gold-standard role in serious Gram-positive and Gram-negative infections — indirect support for SA pneumonia coverage |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | Terminated | 108 | Two tigecycline doses vs imipenem/cilastatin for hospital-acquired pneumonia (≥70% VAP); terminated early and results are limited, but trial design validates imipenem/cilastatin as comparator for serious bacterial pneumonia including SA aetiology |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone vs linezolid + carbapenem in MRSA VAP patients; most directly relevant to SA — investigates whether adding a carbapenem to linezolid improves outcomes in MRSA pneumonia; status unknown reduces confidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical Study (non-RCT) | Antimicrob Agents Chemother | Imipenem-cilastatin in 23 patients (11 MRSA, 12 MSSA); soft tissue, endovascular, and skeletal infections; MIC90 6.25 μg/mL for MSSA — foundational clinical evidence, now decades old |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case Report | Antimicrob Agents Chemother | Commentary on imipenem/cilastatin + fosfomycin for refractory MRSA bacteraemia after vancomycin and daptomycin failure; argues for individualised combination salvage strategies |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | Clinical Study (non-RCT) | Jpn J Antibiotics | Arbekacin + imipenem/cilastatin combination against clinical MRSA isolates; MICs in combination significantly lower than either agent alone; clinical benefit in MRSA infections documented |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | Preclinical | J Antimicrob Chemother | Vancomycin + imipenem synergy against MRSA in vitro (34/36 isolates showed synergy or additivity) and in neutropenic mouse thigh model; supports dual-agent rationale |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | Animal Study | J Antimicrob Chemother | Imipenem-cilastatin vs vancomycin in rabbit MRSA aortic valve endocarditis; imipenem bacteriostatic in vitro (MBC90 32 mg/L) but showed favourable in vivo efficacy by certain criteria — important nuance for MRSA endocarditis |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | Preclinical | J Antimicrob Chemother | Imipenem/cilastatin + cefotiam synergy in mouse MRSA bacteraemia model (ratios 1:5–1:160); effective against both β-lactamase-producing and non-producing MRSA; mechanism explored via in vitro PK system |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | Comprehensive review of MRSA virulence, key clinical trials, and resistance implications; places carbapenem-based combinations as investigational options for severe refractory MRSA |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label antibiotic use vs formal recommendations for MDR bacteria including MRSA; discusses carbapenem combinations as an option when licensed anti-MRSA agents are unavailable or have failed |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Review | Am Fam Physician | Diabetic foot infection review; identifies *S. aureus* and β-haemolytic streptococci as dominant pathogens in mild-moderate untreated infections; severe polymicrobial cases may require broad-spectrum coverage including carbapenems |
| [1771308](https://pubmed.ncbi.nlm.nih.gov/1771308/) | 1991 | Review | Semin Respir Infect | Antibiotic therapy of pleural empyema; notes SA as a relevant nosocomial pathogen; polymicrobial aetiology supports broad-spectrum carbapenem coverage in severe cases |

---

## Saudi Arabia Market Information

Cilastatin (as imipenem/cilastatin combination) is **not currently marketed in Saudi Arabia**. There are no SFDA-registered products and no recorded licenses. Any future use would require a full regulatory submission pathway.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug–drug interactions) is not available in this evidence pack.

Please refer to the package insert for safety information.

> **Notable adverse events identified in the literature:**
> - **Leukocytoclastic vasculitis** (PMID [9158321](https://pubmed.ncbi.nlm.nih.gov/9158321/), 1997): First reported case of imipenem/cilastatin-induced vasculitic skin reaction presenting as maculopapular rash progressing to leukocytoclastic pattern.
> - **Acute eosinophilic pneumonia** (PMID [26944380](https://pubmed.ncbi.nlm.nih.gov/26944380/), 2016): Drug-induced eosinophilic pneumonia one day after initiation, presenting with fever, acute hypoxic respiratory distress, and diffuse ground-glass opacities on CT; resolved on drug withdrawal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for imipenem/cilastatin in *Staphylococcus aureus* infection is confined to small non-RCT clinical studies from 1986–1994, animal models, in vitro synergy experiments, and isolated case reports — none of which constitute a contemporary controlled trial targeting SA as the primary indication. Critically, MRSA's intrinsic PBP2a-mediated resistance limits monotherapy applicability, and combination synergy data, while intriguing, has not been validated in prospective trials.

**To proceed, the following is needed:**

- **MSSA vs. MRSA stratification**: Clearly separate the two scenarios — MSSA infections represent a mechanistically sound target; MRSA requires combination strategy and should be evaluated as a distinct research question
- **Modern PK/PD analysis**: Confirm that imipenem achieves >40–50% T>MIC for MSSA isolates at approved dosing regimens in the target patient populations
- **Phase 2 RCT for MSSA bacteraemia**: Compare imipenem/cilastatin to anti-staphylococcal penicillins (nafcillin/flucloxacillin) or cefazolin, the current first-line agents for MSSA bacteraemia
- **MRSA combination validation**: A prospective pilot study (Phase 2) testing imipenem/cilastatin + fosfomycin in documented MRSA bacteraemia refractory to vancomycin/daptomycin
- **SFDA regulatory pathway**: Assess registration requirements for imipenem/cilastatin in Saudi Arabia before any clinical programme is initiated
- **Full safety profile**: Obtain complete package insert data including contraindications, black-box warnings, and drug interaction profile (currently all are data gaps)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

