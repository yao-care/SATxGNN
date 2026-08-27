---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 552
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Ritonavir is a well-known HIV-1 protease inhibitor used in antiretroviral therapy; original indication data and mechanism-of-action data are not available in this evidence pack, and the drug is not currently marketed in Saudi Arabia.
> The TxGNN model's top-ranked prediction is **simian immunodeficiency virus (SIV) infection** — an animal-model disease, not a human condition — supported by **0 clinical trials** and **12 publications**.
> The evidence pack's own analysis flags this as confirmation of ritonavir's known antiretroviral mechanism in a primate research model, **not** a genuine new human indication, and all three predicted indications are recommended **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — inferred from evidence-pack context; no license-based confirmation available (0 authorizations on file) |
| Predicted New Indication | Simian immunodeficiency virus infection (non-human primate disease model) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (Data Gap DG002 — DrugBank MOA field query pending). Based on information available within this evidence pack, ritonavir is an HIV-1 protease inhibitor and potent CYP3A4 inhibitor, with well-established antiretroviral efficacy in human HIV-1 infection. SIV shares a highly homologous protease structure with HIV-1, and direct in vitro susceptibility studies confirm ritonavir inhibits SIV protease at nanomolar potency comparable to HIV-1 (PMID 12709355, 15040537) — this is the mechanistic basis for the TxGNN association.

However, SIV infection is an experimental non-human primate disease model used in HIV/AIDS research (typically in macaques), not a human clinical indication. The evidence pack's own repurposing rationale explicitly notes this represents an extension/validation of ritonavir's already-known antiretroviral mechanism within an animal research system, rather than a novel therapeutic indication suitable for drug repurposing evaluation.

The rank-2 prediction (feline acquired immunodeficiency syndrome) follows a similar pattern — a veterinary disease of cats caused by FIV, another lentivirus with partial protease homology — but its single supporting "trial" (NCT02770508) is a human Phase 4 darunavir/lamivudine study, judged in the evidence pack to be a disease-ontology mismatch (feline AIDS vs. human AIDS name collision), not genuine supporting evidence. The rank-3 prediction (a rare neurodevelopmental white-matter disorder) has no mechanistic link, no trials, and no literature — a pure model-score artifact (L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility | Antimicrobial Agents and Chemotherapy | Ritonavir inhibited SIVmac239 in vitro (EC50 ≈13 nM), comparable to its potency against HIV-1 (EC50 ≈25 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility | Antiviral Therapy | Evaluated 16 approved anti-HIV-1 drugs, including ritonavir, against HIV-2, SIV and SHIV strains for treatment/PEP guidance |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model (macaque) | Journal of Virology | Quadruple antiretroviral therapy produced rapid viral decay in SIVmac251-infected macaques |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal model | mBio | Lentivirus (HIV/SIV) persisted in brain tissue despite effective ART, highlighting CNS reservoirs |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal model (macaque) | PLoS ONE | Combination ART plus HDAC inhibitor SAHA tested in SIV-infected rhesus macaques to probe latent reservoirs |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model (macaque) | Journal of Virological Methods | Oral HAART including lopinavir/ritonavir assessed for effect on CD8+ T-cell subsets in SHIV89.6P-infected macaques |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro mechanism | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 active against AZT- and ritonavir-resistant HIV-1 strains and SIV |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro mechanism | Journal of Virology | Studied protease-dependent processing of HIV-1 Vif protein, relevant to protease inhibitor mechanism |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model construction | Microbes and Infection | Constructed chimeric SHIV bearing HIV-1 protease for in vivo testing of protease inhibitors in macaques |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal ART study | PLoS Pathogens | Highly intensified multidrug ART achieved long-term viral suppression and reduced viral reservoir in SIVmac251-infected macaques |

---

## Saudi Arabia Market Information

Ritonavir currently holds no Saudi Arabia market authorizations (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA package insert warnings and contraindications are a blocking data gap — DG001 — pending PDF retrieval and parsing; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications for ritonavir lack an actionable human clinical pathway: the top prediction (SIV infection) and rank-2 (feline AIDS) are non-human/veterinary disease models rather than genuine new human indications — the latter's only "supporting" trial is a likely disease-ontology database mismatch — and rank-3 has zero supporting evidence (L5, model score only). No clinical trials support the top indication, and evidence is limited to preclinical/mechanistic and animal-model literature (L4).

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (Blocking gap DG001)
- Verified mechanism-of-action data from DrugBank (High-priority gap DG002)
- Re-run TxGNN disease mapping/QC to filter out non-human disease ontologies (SIV, FIV) and database mismatches before further evaluation
- If a genuine human-indication candidate emerges from re-screening, re-open evaluation at S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

