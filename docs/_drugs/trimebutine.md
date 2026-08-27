---
layout: default
title: Trimebutine
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 2
---

# Trimebutine
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

# Trimebutine: From Irritable Bowel Syndrome to Migraine Disorder

## One-Sentence Summary

Trimebutine is a peripheral opioid receptor agonist originally used as a gastrointestinal antispasmodic/prokinetic for irritable bowel syndrome (IBS) and related functional GI disorders. The TxGNN model predicts a possible role in **Migraine Disorder**, but this direction is currently supported only by **4 publications and no dedicated clinical trials**, with the proposed mechanism being indirect (improving gastric emptying to enhance absorption of oral migraine drugs) rather than a direct action on migraine pathophysiology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable Bowel Syndrome / functional gastrointestinal motility disorder (GI antispasmodic-prokinetic; not separately confirmed in structured regulatory data) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for trimebutine is flagged as a data gap in the evidence pack (not queryable from DrugBank at the time of this pull). However, the supporting literature (PMID 16776704) describes trimebutine as a peripheral **mu/kappa/delta opioid receptor agonist** acting exclusively on the Meissner and Auerbach plexuses throughout the GI tract, with no systemic absorption — consistent with its known clinical use as a GI smooth-muscle antispasmodic and prokinetic agent (e.g., in IBS).

There is no known action of trimebutine on the trigeminovascular system, CGRP signaling, or serotonergic pathways that underlie migraine pathophysiology. The connection identified in the literature is **pharmacokinetic, not pathophysiological**: migraine attacks are frequently accompanied by gastroparesis, which delays absorption of oral abortive therapies such as triptans. Trimebutine's prokinetic effect on gastric emptying may therefore improve the absorption and onset of triptans when co-administered, rather than treat migraine directly.

This means the TxGNN signal likely reflects a genuine but **adjunctive/pharmacokinetic** relationship rather than a disease-modifying one — the mechanistic plausibility is real but indirect, which should temper expectations for trimebutine as a standalone migraine therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16776704](https://pubmed.ncbi.nlm.nih.gov/16776704/) | 2006 | RCT | Cephalalgia | Double-blind, randomized, cross-over, placebo-controlled study of rizatriptan alone vs. rizatriptan + trimebutine for acute migraine; rationale was that trimebutine's gastrokinetic effect could counter migraine-related gastroparesis and improve triptan absorption/efficacy |
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review | J Gastroenterol Hepatol | Reviews effectiveness of prokinetic agents (including trimebutine-class drugs) for conditions outside the GI tract, including CNS-related indications |
| [17046449](https://pubmed.ncbi.nlm.nih.gov/17046449/) | 2006 | Review | Lancet | General review on strategies to increase triptan effectiveness in migraine; relevant context for adjunctive gastrokinetic approaches, though abstract text not available |
| [16245431](https://pubmed.ncbi.nlm.nih.gov/16245431/) | 2005 | Case Report | Polski Merkuriusz Lekarski | Case of abdominal migraine in a 9-year-old girl; trimebutine (along with other antispasmodics) was tried without improvement — a negative/inconclusive data point, not supportive evidence |

---

## Taiwan Market Information

Trimebutine currently has no marketing authorization in Taiwan (0 licenses on record); no product or dosage-form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical evidence (a single small RCT) tested trimebutine as an *adjunct* to a triptan to improve absorption during gastroparesis — not as a treatment for migraine itself — and a case report found no benefit in a related pediatric syndrome. There is no direct mechanistic pathway linking trimebutine to migraine pathophysiology (trigeminovascular/CGRP/serotonergic systems), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Confirmed DrugBank/official MOA data for trimebutine (currently a blocking data gap, DG002)
- TFDA/regulatory package insert with warnings and contraindications (blocking data gap, DG001) before any safety review can begin
- A dedicated clinical trial evaluating trimebutine's effect on migraine outcomes (not merely triptan pharmacokinetics)
- Clarification of trimebutine's approved original indication(s), which were not populated in the source data

**Note:** A second TxGNN prediction for this drug, *migraine with brainstem aura* (score 99.54%), has zero supporting clinical trials or literature (Evidence Level L5, model prediction only) and is separately assessed as **Hold** — not pursued further in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

