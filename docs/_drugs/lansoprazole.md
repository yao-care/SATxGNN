---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

# Lansoprazole: From Proton Pump Inhibitor Use to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI); the evidence pack does not contain a confirmed original indication or Taiwan market license for this product. The TxGNN model predicts potential relevance to **Duodenogastric Reflux**, but this is currently supported only by **0 clinical trials** and **2 publications**, one of which is an animal study raising a safety caution rather than a treatment-efficacy signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no Taiwan license text available; lansoprazole is classified as a proton pump inhibitor) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lansoprazole is part of the proton pump inhibitor (PPI) class, which suppresses gastric acid secretion via irreversible inhibition of the H+/K+-ATPase in gastric parietal cells; this class is broadly used for acid-related conditions such as GERD, peptic ulcer disease, and H. pylori eradication.

Duodenogastric reflux involves backflow of duodenal contents (bile, pancreatic enzymes) into the stomach, and is mechanistically distinct from the acid-reflux pathology that PPIs are designed to treat. The rationale for TxGNN's prediction likely stems from shared anatomical/pathway proximity (gastroduodenal junction) rather than a direct pharmacological mechanism against bile/enzyme reflux itself.

Notably, the available literature does not clearly support a therapeutic benefit: one identified study examined the *combined* effect of duodenogastric reflux and acid inhibition on gastric carcinogenesis in rats, rather than demonstrating efficacy of lansoprazole in treating duodenogastric reflux. This warrants caution in interpreting the TxGNN score as clinically actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Preclinical (animal study) | Gastric Cancer | Examined combined effect of duodenogastric reflux and acid inhibition (lansoprazole) on gastric carcinogenesis in rats; suggests lansoprazole may promote gastric carcinogenesis in the presence of duodenogastric reflux — a safety signal, not an efficacy signal |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General review of PPI clinical use and pharmacokinetics (peptic ulcer, H. pylori, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome); does not specifically address duodenogastric reflux |

---

## Taiwan Market Information

Currently no market authorization data available — lansoprazole is not marketed in Taiwan (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications for lansoprazole are currently a blocking data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for lansoprazole in duodenogastric reflux is currently limited to model prediction plus two tangential publications — one of which flags a potential carcinogenicity risk when lansoprazole is combined with duodenogastric reflux, rather than supporting therapeutic benefit. Combined with the absence of any Taiwan market license and a blocking gap in TFDA safety data, this candidate does not meet the bar for S1 safety review.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data (DG002)
- Dedicated clinical or observational studies evaluating lansoprazole specifically for duodenogastric reflux (not just co-occurring acid inhibition)
- Clarification of the carcinogenicity signal from the 2004 rat study before any further development
- Confirmed original indication / regulatory status for lansoprazole in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

