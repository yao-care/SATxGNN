---
layout: default
title: Stavudine
parent: 僅模型預測 (L5)
nav_order: 583
evidence_level: L5
indication_count: 3
---

# Stavudine
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

# STAVUDINE: From HIV/AIDS (NRTI Antiretroviral) to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Stavudine is a thymidine-analogue nucleoside reverse transcriptase inhibitor (NRTI) known clinically for HIV/AIDS treatment; however, this Evidence Pack does not contain confirmed original-indication or regulatory data for it.
> The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, a non-human primate lentiviral disease,
> with **0 clinical trials** and **4 publications** currently supporting this direction — and those publications are animal-model/toxicity studies, not efficacy trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (blocking data gap — see below) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known information embedded in this Evidence Pack's own rationale text, stavudine is a thymidine-analogue NRTI whose established antiretroviral activity works by inhibiting the reverse transcriptase enzyme shared across lentiviruses.

SIV and HIV are both lentiviruses with closely related reverse transcriptase machinery, which is the mechanistic basis for TxGNN's prediction. However, this is not a human clinical indication — SIV does not infect humans, and the "disease" here is a non-human primate research model, not a treatable human condition.

Critically, the strongest piece of literature evidence (PMID 22013040) is a **safety signal, not efficacy evidence**: it reports fatal pancreatitis in SIV-infected macaques treated with stavudine plus didanosine after immune-checkpoint blockade. This weighs against, rather than for, pursuing this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22013040](https://pubmed.ncbi.nlm.nih.gov/22013040/) | 2012 | Animal toxicity study (macaque) | Journal of Virology | Fatal pancreatitis in SIV-infected macaques treated with ddI + stavudine after CTLA-4/IDO blockade — safety warning, not efficacy data |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro pharmacology/susceptibility | Antiviral Therapy | Susceptibility of HIV-2, SIV and SHIV strains to approved anti-HIV-1 compounds, relevant to post-exposure prophylaxis |
| [9021177](https://pubmed.ncbi.nlm.nih.gov/9021177/) | 1997 | In vitro pharmacology (different compound) | Antimicrobial Agents and Chemotherapy | Study of a different macrolide compound (SRR-SB3); stavudine not the primary study agent |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | In vitro pharmacology | Journal of Virology | Dideoxynucleoside susceptibility of human foamy virus; found zidovudine (not stavudine) most active |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert warnings and contraindications are a **blocking data gap** — DG001 — and must be resolved before any S1 safety review can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (SIV infection) is a non-human primate research model, not a human disease, and its strongest supporting literature reports a fatal toxicity signal rather than efficacy. The two lower-ranked predictions are even weaker: rank 2 (feline immunodeficiency syndrome) is a veterinary indication supported mainly by studies of *stampidine*, a different prodrug molecule, and rank 3 (a rare neurodevelopmental disorder) has zero clinical trials or literature support and is contradicted by stavudine's known mitochondrial-toxicity/neuropathy risk. Combined with two unresolved data gaps — no TFDA package insert (blocking) and no confirmed MOA (high) — this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) to unblock S1 safety review (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- A human-relevant predicted indication with actual clinical trial or human-subject literature support, since all three current predictions are non-human or unsupported
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

