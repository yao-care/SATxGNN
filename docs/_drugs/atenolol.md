---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension / Angina to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective beta-1 adrenergic receptor blocker widely used in clinical practice for hypertension and angina pectoris, though it currently holds no marketing authorization in Saudi Arabia.
The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction** with a score of **99.87%**, backed by **0 clinical trials** and **1 publication** directly supporting this specific sub-indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Angina pectoris (no Saudi Arabia regulatory record available) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on known pharmacological information, atenolol is a selective beta-1 adrenergic receptor blocker. By competitively blocking cardiac beta-1 receptors, it reduces heart rate and myocardial oxygen consumption — two central variables that determine infarct size and arrhythmia risk during acute ischemic events.

Posteroinferior myocardial infarction characteristically involves occlusion of the right coronary artery (RCA), which perfuses the inferior and posterior left ventricular walls and frequently the sinoatrial node. This territory is prone to reflex sinus tachycardia and surges in circulating catecholamines. Atenolol's ability to blunt this sympathoadrenergic response can reduce myocardial oxygen demand, limit infarct extension, and suppress ischemia-driven arrhythmias — effects that form the pharmacological rationale for the TxGNN prediction.

Beta-blockers as a class carry well-established post-MI evidence (mortality reduction, prevention of re-infarction), and atenolol's cardioselectivity (preferential beta-1 over beta-2 blockade) confers a relative advantage over non-selective agents in patients with coexisting airway disease. The TxGNN knowledge graph likely linked atenolol to this prediction through shared cardiovascular and ischemic disease nodes, consistent with this mechanistic reasoning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for atenolol in posteroinferior myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Single-blind Randomized Comparative Study | La Revue de medecine interne | Compared anti-ischemic activity of atenolol (200 mg) vs diltiazem (240 mg) in 23 patients undergoing exercise rehabilitation 4 weeks after limited postero-inferior or anterior MI with residual ischemia; assessed via computerized bicycle ergometer (Case-Marquette system) |

---

## Saudi Arabia Market Information

Atenolol is currently **not marketed in Saudi Arabia**. No product authorizations are on record (total licenses: 0). There is no approved indication text available from local regulatory filings.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic basis for atenolol's benefit in posteroinferior MI is pharmacologically coherent and consistent with established beta-blocker use in ischemic heart disease, evidence specific to this MI sub-type is limited to a single small (N=23) single-blind study from 1985, with no registered clinical trials and no Saudi Arabia regulatory footprint to draw from.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank (DB00335) to formalize mechanistic justification
- **Safety dossier**: Obtain SFDA-equivalent package insert covering warnings, contraindications, and major drug interactions (currently all gaps)
- **Regulatory pathway assessment**: Evaluate whether existing international approvals (e.g., EMA, FDA) for hypertension/angina could support a bridging strategy for Saudi Arabia market entry
- **Targeted clinical evidence review**: Conduct a systematic literature search for atenolol in acute MI (not limited to posteroinferior sub-type) to determine whether the L3 rating can be upgraded to L2 with broader evidence aggregation
- **Indication specificity check**: Consider whether "posteroinferior MI" should be evaluated as part of the broader acute MI indication rather than as a standalone repurposing target, given the established class effect of beta-blockers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

