---
layout: default
title: Chlorphenoxamine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 1
---

# Chlorphenoxamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Chlorphenoxamine: From Antihistamine to Insomnia

## One-Sentence Summary

Chlorphenoxamine is a first-generation H1 antihistamine with significant anticholinergic properties, though no formal approved indication is currently documented in the regulatory database.
The TxGNN model predicts it may be effective for **Insomnia**, with a high prediction score of **99.42%**.
However, there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction, meaning this prediction rests entirely on pharmacological inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No documented indication (not currently marketed) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological information, Chlorphenoxamine is classified as a first-generation H1 antihistamine with notable anticholinergic (antimuscarinic) activity. First-generation antihistamines are lipophilic and readily cross the blood–brain barrier, where they block central H1 histamine receptors. This central H1 blockade produces sedation — the same mechanism exploited by widely used OTC sleep aids such as diphenhydramine and doxylamine.

The TxGNN model's high prediction score (0.994, rank 8,761 overall) most likely reflects this pharmacological class similarity. Within the knowledge graph, Chlorphenoxamine shares structural and mechanistic features with established sedating antihistamines that already have insomnia indications, making the model's inference biologically plausible even in the absence of direct clinical trial data.

It is important to note, however, that the model score is derived from graph topology and class-level features rather than from Chlorphenoxamine-specific insomnia studies. The complete absence of clinical trial and literature evidence, combined with the drug's non-marketed status, means this prediction cannot yet be upgraded beyond model-level evidence (L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** As a first-generation antihistamine with anticholinergic properties, class-level caution is warranted for patients with glaucoma, benign prostatic hyperplasia, urinary retention, or cognitive impairment. Concomitant use with other CNS depressants or anticholinergic agents may produce additive effects. These are class-level considerations and require verification against the actual product label before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is pharmacologically coherent — Chlorphenoxamine's class-level mechanism (central H1 blockade) is the established basis for sedating antihistamines used in insomnia — but the complete absence of clinical trial or literature evidence specific to this compound, combined with its non-marketed status and data gaps across MOA, safety warnings, and contraindications, means the evidence base is insufficient to proceed.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full DrugBank entry to confirm receptor binding profile and pharmacokinetic parameters (BBB penetration, half-life, sedation onset)
- **Safety data**: Obtain and parse the package insert (TFDA or original country of approval) to populate key warnings, contraindications, and drug interaction data — currently all marked as Data Gap
- **Literature search expansion**: Broaden PubMed search beyond the insomnia pairing to include sedation, antihistamine sleep, and Chlorphenoxamine-specific pharmacology studies
- **Regulatory status clarification**: Determine in which countries (if any) Chlorphenoxamine is currently approved, and whether any approval includes sedation or sleep-related indications
- **Comparative positioning**: Assess whether Chlorphenoxamine offers any advantage over already-established OTC sleep antihistamines (diphenhydramine, doxylamine) in terms of duration of action, tolerability, or next-day impairment before investing in a full repurposing program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

