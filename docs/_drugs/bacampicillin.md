---
layout: default
title: Bacampicillin
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Bacampicillin
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

# Bacampicillin: From Bacterial Infections to Epiglottitis

## One-Sentence Summary

Bacampicillin is an oral prodrug of ampicillin — a beta-lactam antibiotic used to treat susceptible bacterial infections — that rapidly releases ampicillin upon absorption. The TxGNN model predicts it may be effective for **Epiglottitis** with a prediction score of **99.92%**; however, currently **no clinical trials and no published literature** directly support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (via ampicillin prodrug mechanism) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for bacampicillin in this dataset. Based on known pharmacological information, bacampicillin is an ester prodrug of ampicillin — after oral administration, it is rapidly hydrolyzed in the gastrointestinal wall to release free ampicillin, which then exerts antibacterial activity by inhibiting bacterial cell wall synthesis through binding to penicillin-binding proteins (PBPs). This mechanism is shared across the beta-lactam class.

Epiglottitis is an acute, potentially life-threatening infection of the epiglottis, most commonly caused by *Haemophilus influenzae* type b (Hib), Group A *Streptococcus*, and *Staphylococcus aureus*. Ampicillin is recognized as one of the standard treatment agents for Hib-associated epiglottitis, making the mechanistic bridge between bacampicillin and this indication biologically coherent — the drug simply delivers ampicillin to achieve the intended antibacterial effect. The TxGNN high score (0.9992) likely reflects this established knowledge-graph connection between the ampicillin class and Hib-related upper airway infections.

An important practical caveat must be noted: epiglottitis is a medical emergency requiring airway management, and the clinical standard of care favors intravenous antibiotics (e.g., ceftriaxone, ampicillin-sulbactam). Bacampicillin is an oral formulation. Any legitimate role would be limited to post-acute step-down therapy, significantly narrowing the repurposing opportunity compared to what the TxGNN score might suggest.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bacampicillin's mechanism as an ampicillin prodrug provides genuine biological plausibility for epiglottitis (ampicillin is a recognized Hib treatment), but the evidence base is entirely model-driven (L5 — no clinical trials, no published literature). Furthermore, the oral route of administration is fundamentally mismatched with acute epiglottitis management, which requires IV antibiotics and immediate airway monitoring.

**To proceed, the following is needed:**
- Clarify clinical role scope: determine whether an oral beta-lactam has any place as step-down therapy in post-acute epiglottitis before pursuing formal study
- Obtain mechanism of action data (MOA) from DrugBank (DG002 — currently a data gap)
- Obtain package insert warnings, contraindications, and drug interaction data (DG001 — currently blocking S1 safety evaluation)
- Identify at least one case report or retrospective cohort demonstrating bacampicillin (or oral ampicillin) use in upper respiratory bacterial infections as a prerequisite for escalating to hypothesis-driven research
- Assess regulatory pathway for Saudi Arabia market entry, given zero current authorization status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

