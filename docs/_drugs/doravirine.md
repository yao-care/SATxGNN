---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine is a third-generation Non-Nucleoside Reverse Transcriptase Inhibitor (NNRTI) originally developed for the treatment of HIV-1 infection in adults.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection** — a primate lentiviral disease closely related to HIV-1 —
with **0 clinical trials** and **1 indirectly related publication** currently available to support this direction.
The mechanistic rationale is plausible given phylogenetic similarities between SIV and HIV-1 reverse transcriptases, though known species-specific divergence in the NNRTI binding pocket is a key scientific concern that has not yet been empirically resolved for doravirine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (not registered in Saudi Arabia regulatory data) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data could not be retrieved from the queried sources. Based on known pharmacological class information embedded in the repurposing rationale, doravirine is a third-generation NNRTI that targets HIV-1 reverse transcriptase (RT). It binds to the NNRTI binding pocket (NNIBP) — a region adjacent to the polymerase active site — and allosterically inhibits viral RNA-to-DNA reverse transcription. Compared to earlier NNRTIs, doravirine was designed with an improved resistance barrier against common mutations such as K103N and Y188L.

SIV and HIV-1 are both members of the primate lentivirus family, sharing similar reverse transcriptase architecture and replication strategies. This phylogenetic proximity is the primary basis for the TxGNN prediction: if doravirine potently inhibits HIV-1 RT, a structurally analogous target in SIV may respond similarly. SIV infection in non-human primates is also the leading animal model for HIV pathogenesis and vaccine/therapeutic research, giving this repurposing question additional translational relevance.

However, there is a well-documented mechanistic caveat. The NNIBP is highly species-specific in its three-dimensional conformation. Studies on earlier NNRTIs — including nevirapine and efavirenz — have consistently demonstrated substantially reduced or absent activity against SIV reverse transcriptase due to differences in pocket geometry. As a third-generation NNRTI, doravirine is subject to the same structural constraint. No direct in vitro or in vivo data evaluating doravirine against any SIV strain are currently available, leaving this prediction mechanistically plausible but empirically unverified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Doravirine in Simian Immunodeficiency Virus Infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Review of islatravir (ISL), a novel reverse transcriptase translocation inhibitor (NRTTI), for HIV-1 treatment and prevention — provides context on the RT-inhibitor class landscape but does not evaluate doravirine or SIV activity directly |

> **Note:** The single retrieved publication covers islatravir — a mechanistically distinct antiretroviral in a different drug class — not doravirine. No publications directly evaluating doravirine against SIV reverse transcriptase were identified. The relevance of this reference to the current repurposing question is indirect at best.

---

## Saudi Arabia Market Information

Doravirine is currently **not registered or marketed in Saudi Arabia**. No authorization records were found in the regulatory database query (query date: 2026-03-29, result count: 0).

---

## Safety Considerations

Please refer to the originator's global prescribing information for safety data.

> Warning and contraindication data were not retrievable from the sources queried for this market context. Clinicians and researchers should consult the full prescribing information for Pifeltro® (doravirine, MSD/Merck) for comprehensive guidance on warnings, contraindications, drug interactions, and special population considerations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is limited to a model prediction (L4) with no registered clinical trials and only a single tangentially related publication covering a different drug. While the mechanistic rationale connecting NNRTI activity to SIV reverse transcriptase inhibition is scientifically coherent, well-established species-specific limitations of NNRTIs at the SIV binding pocket — documented for multiple earlier agents in the same class — represent a substantive scientific risk that cannot be dismissed without empirical data.

**To proceed, the following is needed:**

- **In vitro RT inhibition assay:** Evaluate doravirine against purified SIV RT (ideally SIVmac239 or SIVcpz strains) to establish whether measurable inhibitory activity exists before committing to animal studies
- **Structural analysis:** Conduct computational docking or obtain crystallographic data comparing doravirine binding at HIV-1 RT vs. SIV RT to quantify binding pocket divergence and predict activity loss
- **Targeted literature search:** Systematic review of any conference abstracts, preprints, or unpublished reports evaluating NNRTI activity (particularly third-generation agents) against SIV isolates
- **MOA documentation:** Formal retrieval of complete doravirine pharmacology data via DrugBank API to fill the current mechanism-of-action data gap
- **Safety data retrieval:** Download and parse the originator package insert to populate warning, contraindication, and drug interaction fields required for a complete S1 safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

