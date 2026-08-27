---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 3
---

# Linaclotide
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

# LINACLOTIDE: From IBS-C/Chronic Constipation to Cauda Equina Syndrome

## One-Sentence Summary

> Linaclotide is a guanylate cyclase-C (GC-C) receptor agonist used to treat IBS-C and chronic constipation, acting locally on the intestinal epithelium.
> The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but this direction currently has **0 clinical trials** and **0 publications** supporting it, and the drug's own repurposing rationale flags the signal as likely spurious.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | IBS-C / Chronic Constipation (per rationale text; no official Taiwan-approved indication text on file — not yet marketed) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal `original_moa` record is marked as a data gap. However, the repurposing rationale supplied with this evidence pack describes Linaclotide as a GC-C receptor agonist that acts almost exclusively on intestinal epithelial cells — it is minimally absorbed into systemic circulation after oral dosing. Locally, it activates intracellular cGMP signaling, which increases chloride/bicarbonate secretion and accelerates intestinal transit. This mechanism underlies its established use in IBS-C and chronic constipation.

Cauda equina syndrome, by contrast, is a neurosurgical emergency caused by compression of the lumbosacral nerve roots (commonly from disc herniation, tumor, or trauma), with the core pathology being direct neural injury — not a disorder of intestinal secretion. While patients with cauda equina syndrome frequently develop secondary "neurogenic bowel" symptoms, there is no known pharmacological pathway linking GC-C receptor activation to relief of nerve root compression or neural repair.

The evidence pack's own analysis concludes this high TxGNN score most likely reflects the model conflating "Linaclotide treats bowel-related symptoms" with "cauda equina syndrome's bowel complications" — a symptom-level correlation in the knowledge graph rather than a genuine mechanistic relationship. Because Linaclotide has negligible systemic bioavailability, there is no plausible route by which it could act on nerve tissue itself. The same caveat applies to the two lower-ranked predictions (neurogenic bladder, insomnia), both of which the rationale attributes to disease-comorbidity signal bleed rather than direct drug action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Linaclotide is not currently marketed in Taiwan (0 authorizations on file), so no product/license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on the TxGNN model score (L5, no supporting trials or literature), and the accompanying mechanistic analysis argues the signal likely arises from symptom-level/comorbidity confounding in the knowledge graph rather than a true drug-disease relationship — Linaclotide's negligible systemic absorption makes a direct effect on nerve root compression biologically implausible.

**To proceed, the following is needed:**
- Confirmed original MOA and indication documentation (currently a Blocking/High-severity data gap — TFDA package insert warnings/contraindications, DrugBank MOA)
- Preclinical or mechanistic studies specifically addressing neurogenic bowel dysfunction (a plausible secondary application) rather than cauda equina syndrome itself
- Any emerging clinical trial or case-report evidence before this candidate is reconsidered for advancement past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

