---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 2
---

# Minocycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Minocycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a broad-spectrum tetracycline-class antibiotic; this evidence pack does not contain a documented original indication or mechanism-of-action record (both flagged as data gaps). The TxGNN model predicts potential efficacy for **Punctate Epithelial Keratoconjunctivitis** (score 99.63%) and, secondarily, **Exposure Keratitis** (score 99.20%), but currently **zero clinical trials and zero publications** support either prediction — this is a model-prediction-only signal (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current data pack (original_indications empty; see DG002) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for minocycline in this data pack. Based on general pharmacological knowledge, minocycline is part of the tetracycline class of antibiotics, and its antibacterial efficacy is well established; mechanistically it may be applicable to ocular surface conditions through anti-inflammatory and matrix metalloproteinase (MMP-9) inhibitory activity shared across the tetracycline class.

For both predicted indications, no direct literature on minocycline was found. The mechanistic rationale is derived by analogy to doxycycline (a related tetracycline), which has documented use in ocular surface disease for its anti-inflammatory, anti-MMP-9, and anti-angiogenic properties that may support corneal epithelial repair and inflammation control. This is a pharmacological class-level extrapolation, not direct evidence for minocycline itself, and the TxGNN scores (99.63% / 99.20%) reflect model prediction only.

Given the absence of any clinical trial or publication data specific to minocycline in either indication, the biological plausibility should be treated as a hypothesis-generating signal requiring preclinical or early clinical confirmation before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. Searches of ClinicalTrials.gov and ICTRP for minocycline in both punctate epithelial keratoconjunctivitis and exposure keratitis (query date 2026-04-21) each returned 0 results.

---

## Literature Evidence

Currently no related literature available. PubMed searches for minocycline in both punctate epithelial keratoconjunctivitis and exposure keratitis (query date 2026-04-21) each returned 0 results.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this data pack (blocking gap DG001 — TFDA/SFDA package insert not yet retrieved), which precludes an initial safety screen (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) — no clinical trials, no publications, and no direct mechanistic data support either predicted indication for minocycline specifically.
- A blocking data gap (DG001: TFDA/SFDA package insert warnings and contraindications) prevents even an initial safety screen, and the drug is not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/SFDA package insert retrieval and parsing (DG001, blocking) to enable S1 safety screening
- DrugBank mechanism-of-action data (DG002) to properly assess mechanistic plausibility rather than class-level analogy
- Preclinical or case-level evidence specific to minocycline in ocular surface disease before pursuing further clinical evidence searches
- Confirmation of an ophthalmic-compatible dosage form, since both predicted indications require topical/ocular administration and no dosage-form-by-route data is currently available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

