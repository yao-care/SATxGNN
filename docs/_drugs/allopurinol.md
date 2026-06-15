---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout / Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor classically used to treat gout and hyperuricemia by reducing uric acid production.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
with **0 clinical trials** and **2 publications** currently offering only indirect mechanistic support for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricemia (known pharmacology; no Saudi Arabia registration on record) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, allopurinol inhibits xanthine oxidase (XO), the enzyme responsible for the final two steps in uric acid synthesis from hypoxanthine and xanthine. By blocking XO, allopurinol reduces uric acid production and is established as first-line therapy for gout and hyperuricemia.

The proposed link to hepatic porphyria runs through a shared metabolic crossover between purine metabolism and heme biosynthesis. 5-Aminolevulinate synthase (ALAS) is the rate-limiting enzyme in hepatic heme synthesis and is subject to negative feedback by a small cytosolic heme pool. One hypothesis (PMID 31443750) proposes that metabolic targeting of ALAS activity — including via inhibitors that affect heme utilisation — could attenuate acute porphyric attacks. The xanthine oxidase pathway intersects with this at the level of reactive oxygen species (ROS): XO-generated ROS can deplete the heme regulatory pool or co-factors that modulate ALAS expression.

However, this mechanistic chain is highly indirect. Neither retrieved publication directly studies allopurinol in hepatic porphyria: one is a mechanistic hypothesis involving tryptophan 2,3-dioxygenase (TDO) inhibitors, and the other examines carbamazepine's porphyrogenic effects in rat liver — a drug with no structural or pharmacological overlap with allopurinol. The overall mechanistic connection is speculative and not supported by experimental data. An additional safety concern exists: allopurinol is associated with DRESS syndrome and drug-induced hepatitis, which poses meaningful risk in patients with already-compromised hepatic function, as is typical in porphyria.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis / Mechanistic Review | Medical Hypotheses | Proposes that metabolic inhibition of heme utilisation by tryptophan 2,3-dioxygenase (TDO) or use of tryptophan could target ALAS activity as a therapy for acute hepatic porphyrias; does not specifically study allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (rat liver) | Biochemical Pharmacology | Examines how carbamazepine exacerbates hepatic porphyria via heme pool depletion in rat liver; allopurinol is not studied; relevant only as contextual evidence for heme pathway perturbation |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from repurposing rationale:** Allopurinol carries a known risk of DRESS syndrome and drug-induced hepatitis. For a target population with hepatic porphyria — where liver function is already compromised — this represents a material safety concern that must be characterised before any further development steps are considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole evidence base is a TxGNN graph-embedding prediction (score 99.95%) supported only by two indirectly relevant publications at the mechanistic hypothesis level (L4); no clinical trials exist, and the mechanistic link between xanthine oxidase inhibition and hepatic porphyria is speculative. Compounding this, allopurinol's known hepatotoxicity and DRESS risk create a specific safety concern for this patient population that has not been characterised.

**To proceed, the following is needed:**
- Confirm the mechanistic hypothesis in a validated in vitro or animal model of hepatic porphyria (e.g., measure effect of allopurinol on ALAS activity or heme pool in hepatocyte cultures)
- Obtain allopurinol's full mechanism of action data from DrugBank (DG002 remediation) to enable a rigorous mechanistic-link assessment
- Retrieve and review the package insert (DG001 remediation) to characterise hepatotoxicity and DRESS contraindications in the context of porphyria patients
- Conduct a targeted literature search specifically for allopurinol + porphyria (current search returned 0 direct hits); consider searching for xanthine oxidase inhibitors as a class in porphyria models
- If preclinical evidence is found, define a minimum safety monitoring plan for liver function and skin reactions before any human study is contemplated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

