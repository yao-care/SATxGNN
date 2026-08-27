---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line antituberculosis prodrug, used within standard combination regimens (e.g., with isoniazid and rifampicin) for tuberculosis treatment. The TxGNN model's top-ranked prediction suggests possible effectiveness for **Infectious Otitis Media**, but currently **no clinical trials and no publications** directly support this specific prediction — it is a model prediction only, with the underlying mechanistic rationale itself noting the link is weak unless the causative organism is *Mycobacterium tuberculosis*.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (antituberculous combination therapy) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information present in this evidence pack, Pyrazinamide is a prodrug converted intracellularly by macrophages into its active metabolite, pyrazinoic acid, which is active specifically against *Mycobacterium tuberculosis* in the acidic intracellular environment of infected macrophages.

The mechanistic link to "infectious otitis media" as a general diagnosis category is weak: pyrazinamide has no established activity against the common bacterial pathogens that cause ordinary infectious/suppurative otitis media (e.g., *Streptococcus pneumoniae*, *Haemophilus influenzae*). Its own rationale text explicitly states that if the causative organism is a general pyogenic bacterium rather than *M. tuberculosis*, there is no pharmacological basis for efficacy.

Notably, several lower-ranked but better-evidenced predictions in this candidate set (middle ear disease, chronic otitis media, suppurative otitis media, infectious otitis interna) are supported by literature — but that literature describes **tuberculous otitis media**, a rare extrapulmonary manifestation of TB already treated with standard anti-TB regimens containing pyrazinamide. This represents an extension of the drug's existing indication rather than a genuinely new repurposing opportunity, and it does not extend to non-tuberculous causes of otitis media, which is the specific top-ranked prediction here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Pyrazinamide is not currently marketed in Saudi Arabia (0 authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA package insert warnings/contraindications are an unresolved **Blocking** data gap — DG001 — which prevents a formal S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (infectious otitis media) has no supporting clinical trials or literature, and its own mechanistic rationale flags the pharmacological link as weak unless the pathogen is specifically *M. tuberculosis*. Combined with the Blocking data gap on TFDA safety labeling, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Formal MOA data from DrugBank/TFDA (DG002)
- TFDA package insert (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Clarification of disease-ontology mapping — determine whether "infectious otitis media" in this prediction is distinct from the tuberculous-otitis-media cluster (ranks 2, 4, 5, 10) that already has case-report-level support, since conflating the two would misrepresent the evidence strength
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

