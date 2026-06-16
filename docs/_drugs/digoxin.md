---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 6
---

# Digoxin
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

The txgnn-pipeline skill is for technical pipeline operations — it doesn't override the report generation task. Proceeding with the report per the system prompt format.

---

# Digoxin: From Heart Failure to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside historically used to treat heart failure and control ventricular rate in atrial fibrillation.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (coronary artery vasospastic angina),
with **0 clinical trials** and **2 publications** currently in evidence — neither of which directly supports this use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; atrial fibrillation rate control (based on pharmacological class; no Saudi Arabia regulatory record) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Digoxin is a cardiac glycoside that works by inhibiting the Na⁺/K⁺-ATPase pump on cardiomyocytes. This raises intracellular sodium, which in turn increases intracellular calcium via the Na⁺/Ca²⁺ exchanger, producing a positive inotropic effect (stronger heart contractions). Digoxin also activates the vagus nerve, slowing conduction through the AV node and reducing heart rate — making it useful in heart failure with reduced ejection fraction and in ventricular rate control for atrial fibrillation.

The TxGNN prediction likely traces back to Digoxin's historical use in **angina decubitus** (recumbent angina), where its vagal-stimulating effect was thought to modify coronary tone. Since Prinzmetal angina and angina decubitus both occur predominantly at rest and share similar clinical presentation patterns, the knowledge graph may have created a proximity-based association between Digoxin and Prinzmetal angina.

However, this prediction carries a significant mechanistic concern. Prinzmetal angina is driven by **coronary artery vasospasm**, and Digoxin's core mechanism — increasing intracellular Ca²⁺ — could theoretically **worsen** vasospasm by enhancing smooth muscle contractility. The established standard of care for Prinzmetal angina is calcium channel blockers (e.g., amlodipine, diltiazem), which directly counteract this effect. The predicted mechanism and the known pathophysiology are in direct opposition, representing a potential safety risk rather than a therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Narrative Review | Chinese Medical Sciences Journal | Hemodynamic monitoring of 30 angina decubitus patients showing increased pulmonary artery pressure preceding attacks; discusses treatment mechanisms for rest angina but does not evaluate Digoxin for Prinzmetal angina specifically |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Narrative Review | Acta Physiologica et Pharmacologica Bulgarica | Review of circadian rhythms in antihypertensive pharmacology; discusses time-of-day cardiovascular event patterns but is not a study of Digoxin in vasospastic angina |

> **Note:** Both publications are Tier 3 Narrative Reviews with indirect relevance only. Neither provides supportive evidence for Digoxin use in Prinzmetal angina.

---

## Saudi Arabia Market Information

Digoxin is not currently registered or marketed in Saudi Arabia. No regulatory authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Pharmacological safety flag:** Based on mechanistic reasoning, Digoxin's elevation of intracellular Ca²⁺ poses a theoretically **contraindicated** profile for Prinzmetal angina — a condition where calcium channel blockade is the standard of care. This concern should be explicitly addressed before any further evaluation of this repurposing candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is limited to two tangentially related narrative reviews (L4), and more critically, Digoxin's core mechanism of increasing intracellular Ca²⁺ is mechanistically opposed to the treatment goal in Prinzmetal angina — where coronary vasospasm must be relieved, not potentiated. This prediction is most likely a knowledge graph proximity artifact arising from Digoxin's historical association with angina decubitus, not a genuine therapeutic signal.

**To proceed, the following is needed:**
- Preclinical vasospasm model studies (e.g., isolated coronary artery ring assays) to determine whether Digoxin worsens, is neutral, or has a paradoxical benefit on coronary artery tone
- Full MOA documentation from DrugBank (Data Gap DG002) to confirm or refute the Ca²⁺-mediated vasospasm concern
- Pharmacovigilance review: case reports of Digoxin use in patients with co-existing vasospastic angina
- Safety and regulatory data from the package insert (Data Gap DG001) before any clinical feasibility assessment can be initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

