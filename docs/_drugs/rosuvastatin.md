---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hypercholesterolemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) originally used to treat hypercholesterolemia and dyslipidemia. The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, but this direction is currently supported only by **0 clinical trials** and **2 case-report/review publications** that address adjacent lipid disorders rather than CETP deficiency itself — evidence is very weak at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (general statin-class indication; no SFDA-specific approved-indication text available in this evidence pack) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacological information, rosuvastatin is a hydroxymethylglutaryl coenzyme A (HMG-CoA) reductase inhibitor — its efficacy in hypercholesterolemia/dyslipidemia is well established, working primarily by upregulating hepatic LDL receptors and lowering LDL-C synthesis.

CETP deficiency, however, is characterized by markedly *elevated* HDL-C and *reduced* LDL-C — a lipid profile that does not clearly align with rosuvastatin's primary LDL-lowering mechanism. The two supporting publications in this evidence pack are not actually about CETP deficiency: one describes complete ApoA-I deficiency and the other describes hepatic lipase deficiency, both rare lipid-metabolism disorders that are mechanistically adjacent to, but distinct from, CETP deficiency. Both are case reports/reviews (Tier 3), not direct clinical evidence for this indication.

Overall, the mechanistic rationale is indirect and the supporting literature addresses neighboring conditions rather than the predicted disease itself, so the prediction should be treated as a hypothesis-generating signal rather than an actionable repurposing candidate at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case Report/Review | Journal of Clinical Lipidology | Describes complete ApoA-I deficiency in an Iraqi Mandaean family (new APOA1 nonsense mutation), associated with premature atherosclerosis; not a CETP deficiency study |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case Report | BMJ Case Reports | Describes hepatic lipase deficiency in a Middle-Eastern-Arabic male, with the first report of CETP activity/mass measured in a hepatic lipase deficiency patient from this ethnic group |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between rosuvastatin's LDL-lowering action and CETP deficiency's HDL-elevated/LDL-reduced phenotype is not well aligned, and the only supporting literature discusses adjacent-but-different lipid disorders (ApoA-I deficiency, hepatic lipase deficiency) rather than CETP deficiency itself. With no clinical trials and only Tier-3 case-level literature, this candidate sits at evidence level L4 (mechanism/preclinical only) and does not currently support progression.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently a Blocking data gap preventing initial safety screening
- Confirmed mechanism of action (MOA) data from DrugBank — currently a High-severity data gap
- Direct clinical or mechanistic evidence specific to CETP deficiency (not adjacent lipid disorders)
- Clarification of whether rosuvastatin's effect is relevant to CETP-deficient patients' cardiovascular risk management rather than the genetic disorder itself
- Market-entry assessment, since rosuvastatin is not currently marketed in Saudi Arabia (0 licenses on file)

*Note: Other TxGNN-predicted indications in this evidence pack (e.g., familial hypercholesterolemia and hyperlipidemia, both L1/"Proceed with Guardrails") scored similarly high but fall within rosuvastatin's existing approved indication class rather than representing genuine repurposing — they are not novel findings and are not the focus of this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

