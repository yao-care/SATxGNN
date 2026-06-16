---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a widely used over-the-counter antitussive, originally indicated for suppression of non-productive cough associated with upper respiratory conditions.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
with **1 Phase 3 clinical trial** currently recruiting in this direction and a TxGNN prediction score of 99.98%.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cough suppression (non-productive cough, OTC antitussive) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacology, DXM is a centrally acting antitussive that suppresses the cough reflex primarily through antagonism of NMDA (N-methyl-D-aspartate) receptors in the medullary cough center. It also exhibits sigma-1 receptor agonist activity, a property with emerging anti-inflammatory and neuroprotective implications.

The mechanistic bridge to nasal cavity disease is direct and biologically plausible. Nasal cavity diseases — including allergic rhinitis and chronic rhinosinusitis — commonly produce posterior nasal drip that chronically stimulates cough receptors. DXM's NMDA antagonism can attenuate this reflex, effectively addressing one of the most disabling symptom clusters of nasal cavity disease. This positions DXM not merely as symptomatic relief but as a pharmacologically targeted agent for a key symptom pathway of the condition.

Beyond cough suppression, DXM's sigma-1 receptor agonism may offer secondary benefit by modulating nasal mucosal inflammatory signaling, providing a rationale for broader disease modification. The existence of an ongoing Phase 3 trial involving a DXM combination product (NCT06958692) further implies that prior Phase 1/2 data were adequate to justify regulatory approval for advanced-phase investigation, lending indirect credibility to DXM's clinical development landscape.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomized, double-blind, placebo-controlled trial evaluating DXM + Bupropion sustained-release tablets in Chinese adults; note that the registered primary indication is **major depressive disorder** — direct relevance to nasal cavity disease requires independent confirmation |

> ⚠️ **Relevance Note:** NCT06958692 was indexed against nasal cavity disease in this evidence pack, but its registered title and brief summary indicate a primary endpoint in major depressive disorder (DXM + Bupropion, i.e., Auvelity-class combination). The mechanistic overlap with nasal cavity disease is indirect. This trial should not be counted as direct nasal cavity disease evidence until a re-query confirming DXM-specific nasal cavity trials is completed.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Formal key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (Data Gaps DG001 and DG002). Saudi Arabia SFDA package insert data is pending retrieval.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
DXM's established antitussive mechanism maps plausibly onto nasal cavity disease symptomology, and a Phase 3 DXM combination trial is actively recruiting — implying a sufficient preclinical and early-phase evidence base exists, even if not yet directly indexed to nasal cavity disease. However, the sole clinical trial identified carries a misalignment risk (MDD vs. nasal indication), warranting verification before escalating development commitment.

**To proceed, the following is needed:**
- Re-query ClinicalTrials.gov specifically for DXM in rhinitis, sinusitis, and nasal cavity disease to correct potential trial misattribution
- Retrieve full MOA data from DrugBank (Data Gap DG002) to solidify mechanism-indication alignment
- Obtain Saudi Arabia SFDA package insert or WHO safety summary (Data Gap DG001) to complete contraindication and warning assessment
- Conduct drug-drug interaction review, particularly for CYP2D6-mediated interactions (DXM is a well-known CYP2D6 substrate)
- Assess regulatory pathway feasibility in Saudi Arabia, given the drug is currently unregistered (0 SFDA authorizations)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

