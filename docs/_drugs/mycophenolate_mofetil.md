---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Transplant Rejection Prophylaxis to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF, DrugBank DB00688) is an immunosuppressant generally known for preventing organ transplant rejection (this original indication is **not confirmed by the source data** — see note below). The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **0 registered clinical trials** but **20 supporting publications**, most from exploratory pharmacokinetic and immunologic research conducted in the 2000s on MMF as an adjunct to HAART.

> **Note on Original Indication:** `drug.original_indications` and `taiwan_regulatory.licenses` are both empty in the evidence pack, so the original indication cannot be sourced from the data. The statement above reflects general pharmacological background knowledge only, not a verified source in this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not marketed in this market; commonly known as immunosuppressant for organ transplant rejection prophylaxis — unverified against source data) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 (observational/cohort studies; no registered clinical trials) |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data (`drug.original_moa`) is marked as a data gap. However, the repurposing rationale for this indication describes MMF's known mechanism: it inhibits inosine monophosphate dehydrogenase (IMPDH), depleting intracellular guanine nucleotide pools (particularly dGTP) in proliferating lymphocytes, which lack an alternative purine salvage pathway. This is the basis of MMF's antiproliferative, immunosuppressive effect.

In the context of HIV infection, this same mechanism has two theoretical points of relevance: (1) dGTP depletion pharmacologically potentiates nucleoside reverse transcriptase inhibitors such as abacavir by favoring incorporation of the active drug triphosphate over competing endogenous nucleotides, and (2) suppression of activated CD4+ T-cell proliferation reduces the pool of cells susceptible to productive HIV infection. This dual rationale drove a wave of exploratory studies in the early-to-mid 2000s testing MMF as an adjunct to HAART, particularly in abacavir-containing regimens and in multidrug-resistant HIV.

The supporting literature is consistent with this mechanism (e.g., depletion of intracellular dGTP correlating with decreased plasma HIV-1 RNA, PMID 12352149) but is dated, small in scale (pilot/cohort studies, single digit-to-low double-digit patient numbers), and has not been followed by modern confirmatory trials in the era of current antiretroviral standards of care.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF added during structured HAART interruption in 17 chronic HIV-1 patients (n=9 MMF vs n=6 control); assessed immune response and plasma/lymphatic tissue viral load |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort/prospective | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing ART in 5 heavily treatment-experienced patients was associated with depletion of intracellular dGTP and a decrease in plasma HIV-1 RNA |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | Drug interaction/PK study | Clin Pharmacokinet | Evaluated MMF's effect on antiretroviral pharmacokinetics and intracellular nucleoside triphosphate pools, including lamivudine-triphosphate |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD clinical study | Clin Pharmacokinet | PK/PD monitoring of low-dose MMF combined with abacavir, efavirenz, and nelfinavir in HIV-infected patients |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects observed combining MMF with HAART in treatment-naive acute/chronic HIV-1 patients |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical trial (treatment-naive) | AIDS | Assessed effect of MMF on HIV-1 RNA decay rate and the latently infected reservoir in treatment-naive patients starting antiretroviral therapy |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study (Phase 1-like) | J Acquir Immune Defic Syndr | Open-label pilot in 7 multidrug-resistant HIV/AIDS patients combining MMF with abacavir, ddI, amprenavir, ritonavir ± efavirenz; well tolerated |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Pilot combination study | AIDS | Evaluated amdoxovir (DAPD) with or without MMF for safety, tolerability, and antiretroviral activity in extensively treated HIV-1 patients |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Translational/mechanism study | J Clin Invest | Explored selective targeting of clonally expanded HIV-infected CD4+ T cells via antiproliferative drugs, mechanistically relevant to MMF's antiproliferative activity |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Reviewed immunosuppressive drug strategies, including MMF, targeting chronic immune activation in HIV disease progression |

---

## Saudi Arabia Market Information

Not marketed in Saudi Arabia — no product authorizations on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Warnings, contraindications, and drug-interaction data are marked as Blocking data gaps in this evidence pack — see DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IMPDH-inhibition mechanism provides a biologically plausible rationale, and early-2000s pilot/cohort studies suggest a possible synergy with NRTIs like abacavir. However, there are zero registered clinical trials for this indication, the supporting literature is over 15 years old and predates current ART standards, and safety/regulatory data (TFDA warnings, contraindications, DDI) are completely unavailable — a Blocking gap that prevents S1 safety review.

**To proceed, the following is needed:**
- TFDA/package insert safety data (key warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed drug-drug interaction profile, particularly with antiretrovirals
- Contemporary clinical trials evaluating MMF with modern ART regimens
- Confirmed original indication and MOA from DrugBank (DG002)
- Confirmation of Saudi Arabia market/regulatory status (currently 0 licenses / not marketed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

