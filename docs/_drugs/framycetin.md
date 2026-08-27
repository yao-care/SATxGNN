---
layout: default
title: Framycetin
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 7
---

# Framycetin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Framycetin: From Bacterial Infection to Urinary Tract Infection

## One-Sentence Summary

> Framycetin is an aminoglycoside bactericidal antibiotic; no original indication or MOA record is available in this evidence pack, and the drug is not currently marketed in Taiwan.
> Among TxGNN's predicted indications, **Urinary Tract Infection** is the only one with a plausible mechanistic link and supporting evidence (**0 clinical trials, 1 historical publication**), and is therefore the candidate carried forward in this report — the model's #1-ranked prediction (sclerosing cholangitis) was itself flagged by the evidence pack as a likely false positive with no mechanistic relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (drug not marketed in Taiwan; no approved indication text available). Known pharmacologically as an aminoglycoside antibacterial. |
| Predicted New Indication | Urinary Tract Infection (TxGNN rank 2; selected over the nominal rank-1 hit, see note below) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on indication selection:** TxGNN's top-scoring prediction (sclerosing cholangitis, 99.66%) is explicitly annotated in the evidence pack as a probable false positive — sclerosing cholangitis is an autoimmune/fibrotic biliary disease with no mechanistic relationship to an antibacterial agent. The same is true for rank 3 (congenital prothrombin deficiency, a genetic coagulation disorder) and rank 5 (Ureaplasma urethritis, a cell-wall-free organism intrinsically resistant to aminoglycosides). Urinary tract infection is the highest-ranked prediction with both a coherent mechanism and actual supporting literature, so it is used as the lead candidate here.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for framycetin is not available in this evidence pack (Data Gap, High severity). Based on known pharmacology, framycetin is an aminoglycoside antibiotic with bactericidal activity against gram-negative organisms — including *Escherichia coli*, *Proteus mirabilis*, and *Pseudomonas aeruginosa*, the most common pathogens in urinary tract infection.

This mechanistic fit is directly supported by historical evidence: a 1976 German urology paper describes framycetin sulfate (alongside kanamycin) used in bladder instillation/irrigation, where it completely suppressed growth of *P. mirabilis* and *P. aeruginosa* in an infected-bladder model. This indicates a real, if dated, precedent for local urinary-tract application of framycetin rather than a purely computational association.

However, this remains an early-stage, exploratory signal: there is only one historical publication, no registered clinical trials, and no modern efficacy or safety data. The predicted link is mechanistically credible but not clinically validated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [816047](https://pubmed.ncbi.nlm.nih.gov/816047/) | 1976 | Case series/Cohort (presumed — non-English abstract, study design not confirmed against full text) | Der Urologe. Ausg. A | In an experimental infected-bladder model, continuous irrigation with Actihaemyl alone promoted growth of *E. coli*, *P. mirabilis*, and *P. aeruginosa*; adding framycetin sulfate (or kanamycin) completely suppressed growth of *P. mirabilis* and *P. aeruginosa*. |

---

## Taiwan Market Information

Framycetin is not currently marketed in Taiwan (未上市); there are no license or product records on file.

---

## Safety Considerations

TFDA package insert warnings and contraindications for framycetin are not currently available. This is flagged as a **Blocking** data gap in the evidence pack — the package insert (warnings/contraindications) must be obtained before this candidate can enter Stage 1 (S1) safety assessment. No drug-drug interaction data was found.

Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (missing TFDA package insert) currently prevents any formal safety assessment, and the supporting evidence for urinary tract infection is limited to a single 46-year-old historical publication with no modern trials. The evidence level (L4) and decision stage (S1) reflect an early research signal, not a validated repurposing candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the Blocking gap and enable S1 safety review
- Confirmed mechanism of action data from DrugBank
- Contemporary literature/clinical trial search on framycetin (or intravesical aminoglycoside) for urinary tract infection, beyond the single 1976 report
- Route-of-administration data (available vs. required routes) to assess feasibility of local/intravesical use
- Re-confirmation that sclerosing cholangitis, congenital prothrombin deficiency, and Ureaplasma urethritis should remain deprioritized as mechanistically implausible TxGNN false positives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

