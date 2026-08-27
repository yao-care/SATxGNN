---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 6
---

# Rifaximin
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

# Rifaximin: From Undocumented Original Indication to Oral Candidiasis

## One-Sentence Summary

Rifaximin's original indication and mechanism of action are not documented in this evidence pack (drug is not marketed in Saudi Arabia). The TxGNN model predicts potential effectiveness for **Oral Candidiasis**, but this is currently supported by only **0 clinical trials** and **1 publication** — and that publication describes rifaximin as a *risk factor* for candidiasis, not a treatment for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — rifaximin is not marketed in Saudi Arabia and no original indication data was provided in this evidence pack |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for rifaximin in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale that was captured alongside the prediction, rifaximin is a gut-non-absorbed rifamycin-class antibiotic that inhibits bacterial RNA polymerase — it has no known antifungal activity.

This is a critical mismatch: Oral Candidiasis is a fungal infection, and rifaximin's mechanism does not target fungi. The single literature record available (PMID 34180023) does not describe rifaximin treating candidiasis — it describes rifaximin use as **favouring** the emergence of micafungin-resistant *Candida* infections in transplant patients, most likely by disrupting gut bacterial flora and allowing fungal overgrowth. In other words, the available evidence points in the *opposite* direction from the repurposing hypothesis: rifaximin may be a risk factor for candidiasis rather than a therapeutic candidate for it.

The high TxGNN prediction score (99.75%) most likely reflects a statistical co-occurrence pattern in the underlying knowledge graph (drug and disease appearing together in the same clinical contexts) rather than a genuine treatment relationship. This prediction should be treated as a signal requiring mechanistic and clinical scrutiny, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort/Case series | Annals of Hematology | In allogeneic HSCT recipients, rifaximin prophylaxis was associated with a higher incidence of micafungin-resistant *Candida* spp. infections — consistent with rifaximin acting as a risk factor for candidiasis via gut flora disruption, not as a treatment |

**Note:** This is a directional contradiction, not supporting evidence. No literature currently supports rifaximin as a treatment for oral candidiasis.

---

## Saudi Arabia Market Information

Rifaximin currently holds no marketing authorizations in Saudi Arabia (market status: Not Marketed; 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/SFDA package insert warnings and contraindications for rifaximin are currently unavailable and marked as a **Blocking** data gap (DG001) — this must be resolved before any S1 safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available literature evidence contradicts rather than supports the repurposing hypothesis — it identifies rifaximin as a factor that *favours* candidiasis rather than treats it. Combined with the absence of antifungal mechanism, zero clinical trials, and the drug's non-marketed status in Saudi Arabia, there is currently no credible basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action via DrugBank API — currently a High-severity gap (DG002)
- A plausible antifungal or immunomodulatory mechanism to reconcile the prediction with rifaximin's known pharmacology
- Independent, mechanistically-grounded evidence (not co-occurrence-based) before any further evaluation of oral candidiasis as an indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

