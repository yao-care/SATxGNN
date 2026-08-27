---
layout: default
title: Isoprenaline
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Isoprenaline
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

# Isoprenaline: Original Indication Not Documented — Predicted New Indication: Nasal Cavity Disease

## One-Sentence Summary

Isoprenaline (DB01064) is a non-selective beta-adrenergic agonist; the evidence pack does not document its original approved indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts a possible effect on **Nasal Cavity Disease**, but this direction is currently supported by only **0 clinical trials** and **1 unrelated case report**, and the accompanying rationale flags it as a likely spurious embedding correlation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no licenses, no original_indications on file) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for isoprenaline is not available in this evidence pack (flagged as a High-severity data gap, DG002). Without a documented original indication or MOA, no mechanistic bridge to nasal cavity disease can be established from the supplied data.

The single literature record associated with this prediction (PMID 14711196) is a case report of perioperative ventricular tachycardia and coronary artery spasm following intranasal epinephrine administration during intubation — epinephrine, not isoprenaline, and cardiac arrhythmia, not nasal cavity disease. The evidence pack's own rationale explicitly characterizes this as an unrelated finding: "無明確機轉關聯；唯一文獻為圍術期心室頻脈合併冠狀動脈痙攣之病例報告，與鼻腔疾病無直接關係，疑似TxGNN embedding偽關聯" (no clear mechanistic link; the sole literature item is a case report of perioperative ventricular tachycardia with coronary spasm, unrelated to nasal cavity disease — likely a spurious TxGNN embedding correlation).

Given the absence of MOA data, the absence of any clinical trial evidence, and an explicit flag that the one supporting reference is mechanistically unrelated, this prediction should be treated as a hypothesis-generation signal only, not a mechanistically grounded candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Case Report | Japanese Heart Journal | Case of perioperative ventricular tachycardia and coronary artery spasm in a 26-year-old male after intranasal epinephrine (not isoprenaline) during intubation; not directly relevant to nasal cavity disease. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting literature for this prediction is mechanistically unrelated to nasal cavity disease (a cardiac arrhythmia case report involving a different drug), there are no clinical trials, and both the drug's original indication and mechanism of action are undocumented in this evidence pack — insufficient basis to advance.

**To proceed, the following is needed:**
- Original indication and approved-use history for isoprenaline (currently blocking, DG001/DG002)
- Mechanism of action data from DrugBank or another authoritative source
- TFDA/SFDA package insert warnings and contraindications (currently blocking for safety review, DG001)
- Literature or preclinical evidence specifically linking isoprenaline (not epinephrine or other adrenergic agents) to nasal cavity pathology
- Reassessment of whether this TxGNN prediction reflects a true signal or an embedding artifact before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

